---
name: convention-api-database
description: PostgreSQL + ClickHouse DB 네이밍/설계 규칙
---

# Database 규칙

## PostgreSQL 네이밍

| 대상 | 규칙 | 예시 |
|------|------|------|
| 테이블 | 단수형 snake_case | `device`, `alert_history` |
| 예외 | 예약어 복수형 | `users`, `groups` |
| PK | `id` (접두사 없음) | `id SERIAL PRIMARY KEY` |
| FK | `{엔티티}_id` 단수형 | `device_id`, `role_id` |
| Boolean | is_, has_, can_ | `is_active`, `is_monitored` |
| Timestamp | _at 접미사 | `created_at`, `updated_at` |
| 인덱스 | `idx_{table}_{column}` | `idx_device_ip_address` |
| FK 제약 | `fk_{table}_{ref}` | `fk_device_group` |
| 유니크 | `uq_{table}_{column}` | `uq_users_email` |
| 체크 | `ck_{table}_{column}` | `ck_device_status` |

## PostgreSQL 타입
- 문자열: `VARCHAR(n)` 또는 `TEXT`
- 시간: `TIMESTAMPTZ` (naive 금지)
- UUID: `UUID DEFAULT gen_random_uuid()`
- JSON: `JSONB`
- Enum: `VARCHAR` + CHECK 제약

## ClickHouse 네이밍

| 대상 | 규칙 | 예시 |
|------|------|------|
| 팩트 테이블 | 단수형 | `metric`, `log`, `trace_span` |
| 차원 테이블 | `dim_` 접두사 | `dim_device` |
| 엔진 | MergeTree(팩트), ReplacingMergeTree(차원) | |
| 파티션 | `toYYYYMMDD(timestamp)` | |
| TTL | 명시 필수 | `TTL timestamp + INTERVAL 90 DAY` |
| LowCardinality | 카디널리티 < 10,000 | `LowCardinality(String)` |

## Dimension Sync
- PostgreSQL CUD → ClickHouse dim_device INSERT
- ReplacingMergeTree(updated_at) → 자동 머지로 최신 유지
