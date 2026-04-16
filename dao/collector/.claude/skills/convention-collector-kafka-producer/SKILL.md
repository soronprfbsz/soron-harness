---
name: convention-collector-kafka-producer
description: Kafka Producer 규칙 (franz-go)
---

# Kafka Producer 규칙

## 라이브러리
- **franz-go** (twmb/franz-go)

## Key/Value 규칙
- **Key**: `device_id` (metrics/logs) / `trace_id` (traces) — 같은 키 → 같은 파티션 → 순서 보장
- **Value**: JSON 직렬화 (`encoding/json`)
- **토픽**: `metrics`, `logs`, `traces`
- ⚠️ `events` 토픽은 collector가 발행하지 않는다. Consumer Layer에서 임계치 감지 후 발행.

## 배치 설정
- 100건 또는 5초 timeout (Batch 프로세서에서 처리)
- 발행 실패 시 재시도 3회, 이후 로깅 후 드롭

## 메시지 포맷

```json
{
  "device_id": "550e8400-...",
  "metric_name": "cpu_usage_percent",
  "value": 72.5,
  "unit": "%",
  "timestamp": "2026-04-13T04:30:00.000Z",
  "label": {"host": "server-01"}
}
```

## 에러 처리

```go
record := &kgo.Record{
    Topic: topic,
    Key:   []byte(deviceID),
    Value: jsonBytes,
}

producer.Produce(ctx, record, func(r *kgo.Record, err error) {
    if err != nil {
        log.Error().Err(err).Str("topic", topic).Msg("produce failed")
        return
    }
    log.Debug().Int32("partition", r.Partition).Int64("offset", r.Offset).Msg("produced")
})
```

## Flush
- Shutdown 시 반드시 `producer.Flush(ctx)` 호출
- 버퍼에 남은 메시지 모두 전송 완료 후 종료
