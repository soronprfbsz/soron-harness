---
name: convention-consumer-tdd
description: Consumer 레이어 TDD 규칙 (pytest)
---

# Consumer TDD

## 프레임워크
- **pytest** + **pytest-asyncio** (비동기 테스트 시)

## 구조
- `tests/` = `src/` 미러 구조
- 테스트 파일: `test_{모듈명}.py`
- 테스트 함수: `test_{동작}_{조건}_{예상결과}()`

## TDD 사이클
1. **Red**: 실패하는 테스트 작성
2. **Green**: 테스트를 통과하는 최소 구현
3. **Refactor**: 코드 정리 (테스트는 통과 유지)

## 테스트 패턴

### Consumer 테스트
```python
def test_metrics_consumer_validates_valid_message():
    consumer = MetricsConsumer(config, mock_writer)
    msg = {"device_id": "...", "metric_name": "cpu", "value": 50.0, ...}
    assert consumer.validate(msg) is True

def test_metrics_consumer_rejects_invalid_schema():
    consumer = MetricsConsumer(config, mock_writer)
    msg = {"invalid": "data"}
    assert consumer.validate(msg) is False
```

### Writer 테스트
```python
def test_clickhouse_writer_inserts_batch(mock_client):
    writer = ClickHouseWriter(mock_client)
    batch = [MetricRow(...), MetricRow(...)]
    writer.write(batch)
    mock_client.insert.assert_called_once()
```

## Mock 전략
- Kafka: MockConsumer 또는 testcontainers
- ClickHouse: mock writer (단위) / testcontainers (통합)
- 파일시스템/네트워크: 항상 mock

## 커버리지
- `pytest --cov=src tests/`
- 최소 80% 목표
