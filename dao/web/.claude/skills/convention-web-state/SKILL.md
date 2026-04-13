---
name: convention-web-state
description: Zustand 상태관리 규칙
---

# 상태관리 (Zustand)

## Store 네이밍
- `use{Entity}Store`

## Selector 패턴

```tsx
// Store 정의
interface DeviceStore {
  devices: Device[];
  selectedId: string | null;
  setDevices: (devices: Device[]) => void;
  selectDevice: (id: string) => void;
}

export const useDeviceStore = create<DeviceStore>((set) => ({
  devices: [],
  selectedId: null,
  setDevices: (devices) => set({ devices }),
  selectDevice: (id) => set({ selectedId: id }),
}));

// 사용 — selector로 리렌더 방지
const devices = useDeviceStore((s) => s.devices);
const selectDevice = useDeviceStore((s) => s.selectDevice);
```

## 서버/클라이언트 분리
- **서버 상태**: TanStack Query (캐싱, 리페칭, 낙관적 업데이트)
- **클라이언트 상태**: Zustand (UI 상태, 필터, 선택)

## 규칙
- Store 파일당 하나의 엔티티
- 전체 store 구독 금지 (`useStore()` → `useStore(s => s.field)`)
- 비동기 로직은 store 외부 (TanStack Query 또는 서비스)
