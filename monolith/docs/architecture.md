# Monolith Architecture

## 기술 스택

### Backend (backend/)
- FastAPI + SQLAlchemy + Alembic + PostgreSQL

### Frontend (frontend/)
- React + TypeScript + Zustand + TailwindCSS

## 프로젝트 구조

```
project/
├── backend/
│   └── app/
│       ├── domains/
│       │   └── {domain}/
│       │       ├── routers.py
│       │       ├── services.py
│       │       ├── repositories.py
│       │       ├── schemas.py
│       │       └── models.py
│       ├── common/
│       │   ├── config.py
│       │   ├── database.py
│       │   ├── middlewares/
│       │   ├── exceptions/
│       │   ├── logging/
│       │   ├── models/
│       │   └── utils/
│       ├── main.py
│       └── tests/
└── frontend/
    └── src/
        ├── app/
        ├── pages/
        ├── widgets/
        ├── features/
        ├── entities/
        ├── shared/
        └── tests/
```

## 백엔드 의존성 규칙
- routers → services → repositories (단방향)
- 도메인 간: service → service만 허용

## 프론트엔드 레이어 규칙
- import 방향: app → pages → widgets → features → entities → shared
- 역방향 금지, 같은 레이어 슬라이스 간 직접 import 금지
- 각 슬라이스는 index.ts를 통해 public API만 노출
