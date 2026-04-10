---
name: convention-project-structure
description: React 프론트엔드 FSD 프로젝트 구조
---

# Project Structure (Frontend - Feature-Sliced Design)

## 레이어 구조

```
src/
├── app/               # 앱 초기화, 프로바이더, 글로벌 스타일
│   ├── providers/
│   ├── styles/
│   └── index.tsx
├── pages/             # 페이지 (라우트 단위)
│   └── {page}/
│       ├── ui/
│       └── index.ts
├── widgets/           # 독립적 UI 블록 (헤더, 사이드바)
│   └── {widget}/
│       ├── ui/
│       └── index.ts
├── features/          # 사용자 인터랙션 (로그인, 댓글 작성)
│   └── {feature}/
│       ├── ui/
│       ├── model/
│       └── api/
├── entities/          # 비즈니스 엔티티 (User, Order)
│   └── {entity}/
│       ├── ui/
│       ├── model/
│       └── api/
├── shared/            # 재사용 가능한 공통 코드
│   ├── ui/            # 공통 UI 컴포넌트
│   ├── lib/           # 유틸리티
│   ├── api/           # API 클라이언트, 인터셉터
│   └── config/        # 환경 설정, 상수
└── tests/
```

## 레이어 규칙
- import 방향: app → pages → widgets → features → entities → shared
- 상위에서 하위만 import 가능, 역방향 금지
- 같은 레이어 내 슬라이스 간 직접 import 금지

## Public API
- 각 슬라이스는 index.ts를 통해 public API만 노출
- 슬라이스 내부 파일 직접 import 금지
