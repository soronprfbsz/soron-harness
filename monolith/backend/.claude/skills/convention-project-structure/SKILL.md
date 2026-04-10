---
name: convention-project-structure
description: FastAPI 백엔드 DDD 프로젝트 구조
---

# Project Structure (Backend - DDD)

## 디렉토리 레이아웃

app/
├── domains/           # 도메인별 비즈니스 로직
│   └── {domain}/
│       ├── routers.py       # API 엔드포인트 정의
│       ├── services.py      # 비즈니스 로직
│       ├── repositories.py  # DB 접근 계층
│       ├── schemas.py       # Pydantic 요청/응답 스키마
│       └── models.py        # SQLAlchemy 모델
├── common/            # 공통 인프라
│   ├── config.py            # 환경 설정 (pydantic-settings)
│   ├── database.py          # DB 엔진, 세션 팩토리
│   ├── middlewares/         # CORS, 인증 등
│   ├── exceptions/          # 커스텀 예외, 핸들러
│   ├── logging/             # 로깅 설정
│   ├── models/              # 공통 모델 (Base, TimestampMixin)
│   └── utils/               # 범용 헬퍼
├── main.py            # FastAPI app 생성, 라우터 등록
└── tests/             # domains/ 미러 구조
    ├── domains/
    │   └── {domain}/
    └── common/

## 규칙
- 새 도메인 추가 시 domains/{name}/ 하위에 필요한 파일만 생성
- 도메인 간 의존: services 레벨에서만 다른 도메인의 service를 import
- routers → services → repositories 단방향 의존
- models, schemas는 같은 도메인 내에서만 정의
- 공통 테이블(Base, Mixin)은 common/models/에 위치
