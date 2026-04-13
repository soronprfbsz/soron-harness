---
name: convention-frontend-naming
description: React 프론트엔드 네이밍 컨벤션
---

# Naming Convention (Frontend)

## 변수 / 함수
- camelCase: `userName`, `fetchUsers()`
- 불리언: is/has/can 접두사: `isLoading`, `hasError`
- 이벤트 핸들러: handle 접두사: `handleClick`, `handleSubmit`

## 컴포넌트
- PascalCase: `UserProfile`, `OrderList`
- 파일명 = 컴포넌트명: `UserProfile.tsx`

## 훅
- use 접두사: `useAuth`, `useUserStore`
- 파일명: `useAuth.ts`

## 상수
- UPPER_SNAKE_CASE: `API_BASE_URL`, `MAX_ITEMS`

## 타입 / 인터페이스
- PascalCase: `UserResponse`, `OrderFormProps`
- Props: 컴포넌트명 + Props: `UserProfileProps`

## 디렉토리
- FSD 레이어: 소문자 복수형: `pages/`, `features/`
- 슬라이스: 소문자 케밥케이스: `user-profile/`
- 세그먼트: 소문자: `ui/`, `model/`, `api/`
