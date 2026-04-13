---
name: convention-web-naming
description: React/TypeScript 네이밍 컨벤션 (Web 레이어)
---

# React/TypeScript 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 변수/함수 | camelCase | `deviceList`, `handleClick` |
| 컴포넌트 | PascalCase | `DeviceCard`, `AlertTable` |
| 컴포넌트 파일 | PascalCase.tsx | `DeviceCard.tsx` |
| 훅 | use 접두사 | `useDeviceStore`, `useMetricQuery` |
| 훅 파일 | camelCase.ts | `useDeviceStore.ts` |
| 유틸/서비스 | camelCase.ts | `apiClient.ts`, `formatDate.ts` |
| 디렉토리 | kebab-case | `device-list/`, `alert-management/` |
| 상수 | UPPER_SNAKE_CASE | `API_BASE_URL`, `MAX_RETRY` |
| Props 타입 | `{Component}Props` | `DeviceCardProps` |
| 이벤트 핸들러 | `handle{Event}` | `onClick` → `handleClick` |
| 타입/인터페이스 | PascalCase | `Device`, `MetricPoint` |
| Enum | PascalCase | `enum Severity { Critical, Warning }` |

## 규칙
- `any` 타입 금지
- Props 인터페이스 필수 정의
- 의미 없는 이름 금지
