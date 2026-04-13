---
name: convention-backend-naming
description: FastAPI 백엔드 네이밍 컨벤션
---

# Naming Convention (Backend)

## 변수 / 함수
- snake_case 사용
- 동사로 시작하는 함수명: `get_user()`, `create_order()`
- 불리언: is/has/can 접두사: `is_active`, `has_permission`

## 클래스
- PascalCase 사용
- 모델: `User`, `OrderItem`
- 스키마: `UserCreate`, `UserResponse`
- 서비스: `UserService`
- 리포지토리: `UserRepository`

## 상수
- UPPER_SNAKE_CASE: `MAX_RETRY_COUNT`, `DEFAULT_PAGE_SIZE`

## 모듈 / 파일
- snake_case.py: `user_service.py`, `order_repository.py`
- 도메인 디렉토리: 단수형 소문자: `user/`, `order/`

## API 엔드포인트
- 복수형 소문자: `/users`, `/orders/{order_id}/items`
