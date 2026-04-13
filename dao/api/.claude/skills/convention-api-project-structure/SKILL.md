---
name: convention-api-project-structure
description: FastAPI DDD 프로젝트 구조
---

# API 프로젝트 구조 (DDD)

```
api/
├── app/
│   ├── main.py                  # FastAPI 앱 팩토리
│   ├── domains/                 # 도메인별 분리
│   │   ├── auth/                # JWT 인증
│   │   ├── admin/               # 사용자/역할/그룹
│   │   ├── asset/               # 장비/인터페이스/정책
│   │   ├── query/               # 메트릭/로그/트레이스 조회
│   │   ├── alert/               # 알림 규칙/이력/채널
│   │   └── report/              # PDF 리포트
│   │   └── {domain}/
│   │       ├── router.py        # FastAPI 라우터
│   │       ├── schema.py        # Pydantic 스키마
│   │       ├── service.py       # 비즈니스 로직
│   │       ├── repository.py    # DB 접근
│   │       └── model.py         # SQLAlchemy 모델
│   └── common/
│       ├── config.py            # pydantic-settings
│       ├── database.py          # PG + CH 연결
│       ├── exception.py         # 에러 핸들링
│       ├── schema.py            # CamelModel, ListResponse
│       └── middleware/
│           ├── auth.py          # JWT + RBAC
│           └── logging.py       # request_id
├── tests/                       # app/ 미러
├── alembic/
├── pyproject.toml
└── Dockerfile
```

## 의존 방향

```
router → service → repository (단방향)
```

- 도메인 간: service → service만 허용
- common: 모든 모듈에서 import 가능
- middleware: router에서만 적용

## 패키지 관리
- uv (pyproject.toml + uv.lock)
- 마이그레이션: alembic
