---
name: convention-component
description: React 컴포넌트 설계 컨벤션
---

# Component Design Convention (Frontend)

## 단일 책임
- 하나의 컴포넌트 = 하나의 역할
- 150줄 초과 시 분리 검토

## Props 인터페이스

```tsx
interface UserCardProps {
  user: User;
  onSelect: (id: string) => void;
  isActive?: boolean;
}

export function UserCard({ user, onSelect, isActive = false }: UserCardProps) {
  return (/* ... */);
}
```

## 컴포넌트 분류
- UI 컴포넌트 (shared/ui): 비즈니스 로직 없음, props만으로 동작
- Feature 컴포넌트 (features/): 특정 비즈니스 로직 포함
- Page 컴포넌트 (pages/): 레이아웃 조합, 데이터 페칭 진입점

## 패턴
- children 패턴: 레이아웃/래퍼 컴포넌트
- 합성 패턴: 복잡한 UI 조합
- 제어/비제어: 폼 입력은 제어 컴포넌트 우선

## TailwindCSS
- 인라인 className 사용
- 반복 스타일은 @apply 또는 공통 컴포넌트로 추출
- 조건부 스타일: clsx 또는 cn 유틸 사용
