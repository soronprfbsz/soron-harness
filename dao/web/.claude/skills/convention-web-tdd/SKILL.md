---
name: convention-web-tdd
description: Web TDD 규칙 (vitest + RTL)
---

# Web TDD

## 프레임워크
- **vitest** + **React Testing Library**

## TDD 사이클
1. Red → Green → Refactor

## 테스트 패턴

### 컴포넌트 테스트
```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('DeviceCard shows device name and responds to click', async () => {
  const onSelect = vi.fn();
  render(<DeviceCard device={mockDevice} onSelect={onSelect} />);

  expect(screen.getByText('switch-01')).toBeInTheDocument();
  await userEvent.click(screen.getByRole('article'));
  expect(onSelect).toHaveBeenCalledWith(mockDevice.id);
});
```

### 훅 테스트
```tsx
import { renderHook, act } from '@testing-library/react';

test('useDeviceStore updates selected device', () => {
  const { result } = renderHook(() => useDeviceStore());
  act(() => result.current.selectDevice('device-1'));
  expect(result.current.selectedId).toBe('device-1');
});
```

## 규칙
- 사용자 행위 중심 (클릭, 입력, 확인)
- `getByRole`, `getByText` 선호 (구현 세부 의존 금지)
- `any` 타입 금지 (테스트 코드도)
- Mock: API는 MSW (Mock Service Worker)
