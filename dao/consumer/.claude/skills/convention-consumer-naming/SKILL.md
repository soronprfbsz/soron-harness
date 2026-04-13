---
name: convention-consumer-naming
description: Python 네이밍 컨벤션 (Consumer 레이어)
---

# Python 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 파일 | snake_case.py | `metrics_consumer.py`, `clickhouse_writer.py` |
| 패키지/디렉토리 | snake_case | `consumers`, `writers`, `validators` |
| 클래스 | PascalCase | `MetricsConsumer`, `ClickHouseWriter` |
| 함수/메서드 | snake_case | `consume_batch()`, `insert_metrics()` |
| 변수 | snake_case | `batch_size`, `poll_timeout` |
| 상수 | UPPER_SNAKE_CASE | `DEFAULT_BATCH_SIZE`, `MAX_RETRIES` |
| Boolean | is_, has_, can_ 접두사 | `is_valid`, `has_pending` |
| Private | _ 접두사 | `_validate_schema()`, `_flush_batch()` |
| Enum 클래스 | PascalCase | `class Severity(IntEnum):` |
| Enum 멤버 | UPPER_SNAKE_CASE | `CRITICAL = 1`, `WARNING = 2` |

## 규칙

- 의미 없는 이름 금지 (`data`, `result`, `temp`)
- 단일 문자 변수 금지 (루프 `i`, `j`, `k` 제외)
- 약어는 표준만 허용 (UUID, API, DB, HTTP)
- 양성 Boolean (`is_active`, not `is_not_active`)
- 모든 함수에 파라미터/반환 타입힌트 필수
