---
name: convention-frontend-state
description: Zustand 상태관리 컨벤션
---

# State Management Convention (Frontend - Zustand)

## 스토어 구조

```tsx
// entities/user/model/store.ts
import { create } from "zustand";

interface UserState {
  users: User[];
  isLoading: boolean;
  fetchUsers: () => Promise<void>;
  addUser: (user: User) => void;
}

export const useUserStore = create<UserState>((set) => ({
  users: [],
  isLoading: false,
  fetchUsers: async () => {
    set({ isLoading: true });
    const users = await userApi.getAll();
    set({ users, isLoading: false });
  },
  addUser: (user) => set((state) => ({ users: [...state.users, user] })),
}));
```

## 규칙
- 스토어 위치: 해당 슬라이스의 model/ 세그먼트
- 스토어명: use{Entity}Store
- 서버 상태 vs 클라이언트 상태 분리
  - 서버 상태: TanStack Query 또는 스토어 내 async action
  - 클라이언트 상태: Zustand (UI 상태, 폼 상태)

## Selector 패턴

```tsx
// 개별 selector로 불필요한 리렌더 방지
const users = useUserStore((state) => state.users);
const isLoading = useUserStore((state) => state.isLoading);
```

## Slice 패턴 (대규모 스토어)

```tsx
const createUserSlice = (set) => ({
  users: [],
  addUser: (user) => set((state) => ({ users: [...state.users, user] })),
});
```
