---
name: convention-api
description: FastAPI REST API 설계 컨벤션
---

# API Design Convention (Backend)

## 엔드포인트 네이밍
- 복수형 리소스: `/users`, `/orders`
- 중첩 리소스: `/users/{user_id}/orders`
- 행위 엔드포인트: `/orders/{order_id}/cancel` (POST)

## HTTP 메서드 매핑
- GET: 조회 (단건/목록)
- POST: 생성
- PUT: 전체 수정
- PATCH: 부분 수정
- DELETE: 삭제

## 응답 포맷

```python
from pydantic import BaseModel
from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
```

## 라우터 패턴

```python
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=BaseResponse[list[UserResponse]])
async def get_users(service: UserService = Depends(get_user_service)):
    users = await service.get_all()
    return BaseResponse(success=True, data=users)
```

## 에러 처리
- HTTP 상태코드 준수: 400(잘못된 요청), 404(미존재), 422(검증 실패), 500(서버 오류)
- 커스텀 예외 → exception handler에서 BaseResponse 형태로 변환

## 버저닝
- URL prefix: `/api/v1/users`
- main.py에서 `app.include_router(router, prefix="/api/v1")`
