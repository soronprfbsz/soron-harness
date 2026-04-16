---
name: convention-consumer-project-structure
description: Python Consumer 프로젝트 디렉토리 구조
---

# Consumer 프로젝트 구조

```
consumer/
├── src/
│   ├── __init__.py
│   ├── main.py                  # CLI 엔트리 (--topic metrics|logs|traces|events)
│   ├── consumers/               # Kafka 소비자 (토픽별)
│   │   ├── __init__.py
│   │   ├── base.py              # BaseConsumer ABC
│   │   ├── metrics_consumer.py  # metrics 소비 + EventDetect → events 발행
│   │   ├── logs_consumer.py     # logs 소비 + EventDetect → events 발행
│   │   ├── traces_consumer.py
│   │   └── events_consumer.py   # events 소비 → alert_history
│   ├── eventdetector/           # 임계치 감지 로직 (Consumer Layer)
│   │   ├── __init__.py
│   │   ├── rule.py              # 임계치 규칙 로드 (PG)
│   │   └── detector.py          # 메시지 검사 → 이벤트 생성
│   ├── producers/               # Kafka 이벤트 발행 (events 토픽)
│   │   ├── __init__.py
│   │   └── event_producer.py    # confluent-kafka Producer
│   ├── writers/                 # DB 적재
│   │   ├── __init__.py
│   │   ├── clickhouse_writer.py
│   │   └── postgres_writer.py
│   ├── validators/              # 스키마 검증
│   │   ├── __init__.py
│   │   └── schema.py
│   └── common/                  # 공통
│       ├── __init__.py
│       ├── config.py            # pydantic-settings
│       └── logging.py           # structlog
├── tests/                       # src/ 미러
│   ├── consumers/
│   ├── eventdetector/
│   ├── producers/
│   ├── writers/
│   └── validators/
├── pyproject.toml
├── Dockerfile
└── Makefile
```

## 의존 방향

```
consumers → validators → writers (단방향)
consumers → eventdetector → producers (이벤트 발행 경로)
common은 모든 모듈에서 import 가능
```

- consumers/는 writers/를 직접 호출하지 않음 (BaseConsumer 인터페이스)
- validators/는 writers/를 import하지 않음
- writers/는 consumers/를 import하지 않음
- metrics_consumer / logs_consumer는 eventdetector 호출 후 producers로 events 토픽 발행
- events_consumer는 events 토픽을 소비만 함 (자기 자신에게 발행 금지)

## 패키지 관리
- uv (pyproject.toml + uv.lock)
- .venv 프로젝트 루트
