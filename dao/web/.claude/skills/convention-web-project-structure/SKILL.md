---
name: convention-web-project-structure
description: React FSD (Feature-Sliced Design) 구조
---

# Web 프로젝트 구조 (FSD)

```
web/src/
├── app/                         # 앱 초기화, 라우팅
│   ├── App.tsx
│   ├── router.tsx
│   └── providers/
├── pages/                       # 라우트별 페이지
│   ├── dashboard/
│   ├── device-list/
│   ├── log-explorer/
│   ├── trace-view/
│   ├── alert-management/
│   └── settings/
├── widgets/                     # 페이지 구성 위젯
│   ├── device-overview/
│   └── metric-chart/
├── features/                    # 사용자 액션
│   ├── auth/
│   ├── device-crud/
│   └── alert-rule/
├── entities/                    # 비즈니스 엔티티
│   ├── device/
│   ├── metric/
│   └── user/
└── shared/                      # 공유
    ├── ui/
    ├── api/
    ├── lib/
    └── config/
```

## Import 규칙

```
app → pages → widgets → features → entities → shared (상위→하위만)
```

- 같은 레이어 슬라이스 간 직접 import 금지
- 각 슬라이스 `index.ts`로 public API 노출
