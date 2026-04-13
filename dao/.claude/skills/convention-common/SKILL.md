---
name: convention-common
description: 전 레이어 공통 컨벤션. DateTime, 로깅, DB 네이밍, 에러 응답 규칙.
---

# Common Convention (전 레이어 공통)

## DateTime

| 구분 | 규칙 |
|------|------|
| DB 저장 | UTC (`TIMESTAMPTZ`, `DateTime64(3, 'UTC')`) |
| API 전송 | ISO 8601 UTC (`2026-04-13T09:30:00Z`) |
| Python | `datetime.now(timezone.utc)` — naive datetime 금지 |
| Go | `time.Now().UTC()` |
| Web | dayjs로 UTC→KST 변환 (표시 직전에만) |

## 로깅

| 구분 | Go (Collector) | Python (Consumer/API) | Web |
|------|---------------|----------------------|----------|
| 라이브러리 | zerolog | structlog | console |
| 포맷 | JSON | JSON | - |
| 출력 | stdout | stdout | console |
| 타임스탬프 | UTC ISO 8601 | UTC ISO 8601 | - |

**공통 규칙:**
- 민감정보 (비밀번호, 토큰, API키) 로깅 금지
- 구조화 필드 사용 (문자열 연결 금지)
- request_id 전파 (API)
- component/topic 명시 (Collector/Consumer)

## DB 네이밍 (PostgreSQL)

| 대상 | 규칙 | 예시 |
|------|------|------|
| 테이블 | 단수형 snake_case | `device`, `alert_history` |
| 예외 | 예약어는 복수형 | `users`, `groups` |
| PK | `id` (테이블 접두사 없음) | `id` |
| FK | `{엔티티}_id` (단수형) | `device_id`, `role_id` |
| Boolean | `is_`, `has_`, `can_` | `is_active`, `has_pending` |
| Timestamp | `_at` 접미사 | `created_at`, `updated_at` |
| 인덱스 | `idx_{table}_{column}` | `idx_device_ip_address` |
| FK 제약 | `fk_{table}_{ref}` | `fk_device_group` |
| 유니크 | `uq_{table}_{column}` | `uq_users_email` |

## DB 네이밍 (ClickHouse)

| 대상 | 규칙 |
|------|------|
| 테이블 | 단수형 snake_case (`metric`, `log`, `trace_span`) |
| 차원 테이블 | `dim_` 접두사 (`dim_device`) |
| 엔진 | MergeTree (팩트), ReplacingMergeTree (차원) |
| 파티션 | `toYYYYMMDD(timestamp)` |

## API 에러 응답

```json
{
  "error": {
    "code": "DEVICE_NOT_FOUND",
    "message": "장비를 찾을 수 없습니다",
    "details": null
  }
}
```

- 에러코드: `{DOMAIN}_{ERROR_TYPE}` (UPPER_SNAKE_CASE)
- 5xx에 내부 정보 노출 금지

## Git Convention

- Conventional Commits: `{type}({scope}): {description}`
- Types: feat, fix, refactor, test, docs, chore
- 브랜치: `feat/{기능}`, `fix/{설명}`, `hotfix/{설명}`
- main → develop → feature branches
- Squash merge (feature→develop), Merge commit (develop→main)
