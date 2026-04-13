---
name: convention-consumer-clickhouse
description: ClickHouse 벌크 적재 패턴 (clickhouse-connect)
---

# ClickHouse Writer 규칙

## 라이브러리
- **clickhouse-connect** (공식 클라이언트)

## INSERT 규칙

```python
def insert_metrics(self, batch: list[MetricRow]) -> None:
    """벌크 INSERT — column_names 명시 필수"""
    self.client.insert(
        "dao.metric",
        data=[[r.device_id, r.metric_name, r.value, r.unit, r.timestamp, r.label]
              for r in batch],
        column_names=["device_id", "metric_name", "value", "unit", "timestamp", "label"],
    )
```

- **방식**: 벌크 INSERT (column-oriented)
- **column_names**: 반드시 명시 (순서 실수 방지)
- **타임아웃**: INSERT 30초, 연결 10초

## 중복 제거
- `(device_id, timestamp, metric_name)` 조합으로 체크
- MergeTree 엔진이 ORDER BY 기반으로 최종 머지

## 스키마 매핑

| Python 타입 | ClickHouse 타입 |
|------------|----------------|
| `uuid.UUID` → `str` | UUID |
| `str` | String, LowCardinality(String) |
| `float` | Float64 |
| `datetime` | DateTime64(3, 'UTC') |
| `dict[str, str]` | Map(String, String) |

## 연결 관리

```python
client = clickhouse_connect.get_client(
    host=config.clickhouse_host,
    port=config.clickhouse_port,
    database="dao",
    username=config.clickhouse_user,
    password=config.clickhouse_password,
)
```

## 재시도
- 연결 실패: exponential backoff (1s, 2s, 4s)
- INSERT 실패: 3회 재시도 → 로깅 후 다음 배치
