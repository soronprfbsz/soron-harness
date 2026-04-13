---
name: convention-api-naming
description: Python 네이밍 컨벤션 (API 레이어)
---

# Python 네이밍 규칙 (API)

| 대상 | 규칙 | 예시 |
|------|------|------|
| 파일 | snake_case.py | `router.py`, `schema.py`, `service.py` |
| 도메인 디렉토리 | 단수형 소문자 | `auth`, `device`, `alert` |
| 클래스 | PascalCase | `DeviceService`, `AlertRepository` |
| 함수/메서드 | snake_case | `get_device()`, `create_alert_rule()` |
| 변수 | snake_case | `device_id`, `alert_count` |
| 상수 | UPPER_SNAKE_CASE | `MAX_PAGE_SIZE`, `JWT_ALGORITHM` |
| Boolean | is_, has_, can_ | `is_active`, `has_permission` |
| Private | _ 접두사 | `_hash_password()` |
| DB 테이블 | 단수형 snake_case | `device`, `alert_history` |
| DB 예외 | 예약어는 복수형 | `users`, `groups` |
| Pydantic 스키마 | `{Entity}{Action}` | `DeviceCreate`, `DeviceResponse` |
| Enum | PascalCase + UPPER_SNAKE 멤버 | `class Status(str, Enum): ACTIVE = "active"` |

## 규칙
- 모든 함수에 파라미터/반환 타입힌트 필수
- 의미 없는 이름 금지
- 양성 Boolean (`is_active`, not `is_not_active`)
