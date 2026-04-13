---
name: convention-web-component
description: React 컴포넌트 설계 규칙
---

# 컴포넌트 설계

## 원칙
- **단일 책임**: 하나의 역할만
- **150줄 초과 시 분리** 검토
- **Props 인터페이스** 필수 정의
- **`any` 금지**
- **시맨틱 HTML** 사용

## 패턴

```tsx
interface DeviceCardProps {
  device: Device;
  onSelect: (id: string) => void;
}

export function DeviceCard({ device, onSelect }: DeviceCardProps) {
  const handleClick = () => onSelect(device.id);

  return (
    <article className="device-card" onClick={handleClick}>
      <h3>{device.name}</h3>
      <p>{device.ipAddress}</p>
    </article>
  );
}
```

## 규칙
- 컴포넌트당 하나의 파일
- default export 지양, named export 사용
- 비즈니스 로직은 훅으로 분리
- 조건부 렌더링: 삼항 또는 early return
