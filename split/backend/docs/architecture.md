# Backend Architecture

## 기술 스택
- FastAPI + SQLAlchemy + Alembic + PostgreSQL

## DDD 구조

```
app/
├── domains/           # 도메인별 비즈니스 로직
│   └── {domain}/
│       ├── routers.py       # API 엔드포인트
│       ├── services.py      # 비즈니스 로직
│       ├── repositories.py  # DB 접근
│       ├── schemas.py       # Pydantic 스키마
│       └── models.py        # SQLAlchemy 모델
├── common/
│   ├── config.py            # 환경 설정
│   ├── database.py          # DB 엔진, 세션
│   ├── middleware/         # 미들웨어
│   ├── exceptions/          # 예외 처리
│   ├── logging/             # 로깅
│   ├── models/              # Base, Mixin
│   └── utils/               # 헬퍼
├── main.py
└── tests/
```

## 의존성 규칙
- routers → services → repositories (단방향)
- 도메인 간: service → service만 허용
- 공통 코드: common/에 위치

## 새 도메인 추가 절차
1. `app/domains/{name}/` 디렉토리 생성
2. 필요한 파일만 생성 (routers, services, repositories, schemas, models)
3. `tests/domains/{name}/` 디렉토리에 테스트 추가
4. `app/main.py`에 라우터 등록
