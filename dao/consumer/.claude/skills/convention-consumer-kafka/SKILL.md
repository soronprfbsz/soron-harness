---
name: convention-consumer-kafka
description: Kafka Consumer 패턴 (confluent-kafka)
---

# Kafka Consumer 규칙

## 라이브러리
- **confluent-kafka** (librdkafka 기반)

## Consumer 설정
- **Group ID**: `obsv-{topic}-consumer` (예: `obsv-metrics-consumer`)
- **auto.offset.reset**: `earliest` (메시지 유실 방지)
- **enable.auto.commit**: `False` — 적재 성공 후 수동 커밋
- **격리**: 토픽별 독립 프로세스 (장애 격리)

## BaseConsumer ABC

```python
from abc import ABC, abstractmethod

class BaseConsumer(ABC):
    def __init__(self, config: ConsumerConfig, writer: BaseWriter):
        self.consumer = Consumer(config.kafka_config)
        self.writer = writer
        self.batch: list[dict] = []
        self.last_flush = time.monotonic()

    @abstractmethod
    def validate(self, message: dict) -> bool:
        """메시지 스키마 검증"""

    @abstractmethod
    def transform(self, message: dict) -> dict:
        """적재 전 변환"""

    def run(self) -> None:
        """메인 소비 루프"""
        self.consumer.subscribe([self.topic])
        while self.running:
            msg = self.consumer.poll(timeout=1.0)
            if msg and not msg.error():
                data = json.loads(msg.value())
                if self.validate(data):
                    self.batch.append(self.transform(data))
            if self._should_flush():
                self._flush()

    def _should_flush(self) -> bool:
        return (len(self.batch) >= self.batch_size
                or time.monotonic() - self.last_flush >= self.flush_timeout)

    def _flush(self) -> None:
        if self.batch:
            self.writer.write(self.batch)
            self.consumer.commit()
            self.batch.clear()
            self.last_flush = time.monotonic()
```

## 배치 규칙
- 크기: **5,000건** 또는 **5초** timeout → 플러시
- INSERT 실패: 배치 재시도 3회 → 로깅 후 드롭
- 개별 검증 실패: 해당 메시지만 드롭, 배치 계속

## 에러 처리
- Kafka 연결 실패: 재시도 + 로깅 (프로세스 유지)
- 치명적 에러: graceful shutdown → Docker restart
