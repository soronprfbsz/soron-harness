---
name: convention-api-rest-design
description: REST API 설계 규칙 (FastAPI)
---

# API 설계 규칙

## URL 패턴
- `/api/{리소스}` 복수형 kebab-case
- `GET /api/devices` — 목록
- `POST /api/devices` — 생성
- `GET /api/devices/{id}` — 단건
- `PUT /api/devices/{id}` — 수정
- `DELETE /api/devices/{id}` — 삭제

## JSON 네이밍
- Request/Response body: **camelCase**
- Pydantic: `alias_generator=to_camel`

## 응답 포맷

### 단일 리소스
```json
{ "id": 1, "name": "switch-01", "ipAddress": "10.0.0.1" }
```

### 리스트
```json
{ "items": [...], "total": 100, "page": 1, "perPage": 20 }
```

### 에러
```json
{ "error": { "code": "DEVICE_NOT_FOUND", "message": "장비를 찾을 수 없습니다", "details": null } }
```

## 에러 코드
- 형식: `{DOMAIN}_{ERROR_TYPE}` (UPPER_SNAKE_CASE)
- 공통: `VALIDATION_ERROR`, `UNAUTHORIZED`, `FORBIDDEN`, `NOT_FOUND`, `INTERNAL_ERROR`
- 도메인: `AUTH_TOKEN_EXPIRED`, `DEVICE_IP_CONFLICT`, `ALERT_RULE_INVALID`

## 상태 코드
200, 201, 204, 400, 401, 403, 404, 409, 422, 500

## 인증
- JWT (access + refresh token)
- RBAC: Super Admin / Admin / Operator / Viewer
- Bearer token in Authorization header

## Pydantic 패턴

```python
from pydantic.alias_generators import to_camel

class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class DeviceCreate(CamelModel):
    name: str
    ip_address: str
    device_type_id: int
```

## DateTime
- ISO 8601 UTC (`2026-04-13T09:30:00Z`)
- `datetime.now(timezone.utc)` — naive 금지
