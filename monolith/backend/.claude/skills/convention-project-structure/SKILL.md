---
name: convention-project-structure
description: FastAPI 백엔드 DDD 프로젝트 구조
---

# Project Structure (Backend - DDD)

## 디렉토리 레이아웃

```
app/
├── domains/           # 도메인별 비즈니스 로직
│   └── {domain}/
│       ├── routers.py       # API 엔드포인트 정의
│       ├── services.py      # 비즈니스 로직
│       ├── repositories.py  # DB 접근 계층
│       ├── schemas.py       # Pydantic 요청/응답 스키마
│       └── models.py        # SQLAlchemy 모델
├── common/            # 공통 인프라 및 도메인 횡단 모듈
│   ├── config.py            # 환경 설정 (pydantic-settings)
│   ├── database.py          # DB 엔진, 세션 팩토리
│   ├── dependency.py        # FastAPI 공통 의존성
│   ├── schema.py            # 공통 Pydantic 스키마 (BaseResponse 등)
│   ├── seeds.py             # 초기 데이터 시딩
│   ├── middlewares/         # 미들웨어 (error_handler, logging, request_id 등)
│   ├── exceptions/          # 커스텀 예외, 핸들러
│   ├── models/              # 공통 모델 (Base, TimestampMixin)
│   ├── logging/             # 비즈니스 로깅 (도메인별 로거)
│   ├── {topic}/             # 도메인 횡단 관심사별 서브폴더 (자유 생성)
│   └── utils/               # 순수 범용 헬퍼 (분류 안 되는 것만)
├── main.py            # FastAPI app 생성, 라우터 등록
└── tests/             # domains/ 미러 구조
    ├── domains/
    │   └── {domain}/
    └── common/
```

## common/ 구조 원칙

common/ 하위에는 고정된 폴더만 있는 것이 아니다. 도메인 횡단 관심사가 생기면 주제별 서브폴더를 자유롭게 생성한다.

예시:
```
common/
├── market/              # 시장 운영 관련 (hours, calendar, timezone)
├── stock/               # 종목 공통 헬퍼 (code, resolver)
├── notification/        # 알림 (telegram, slack 등)
├── logging/             # 비즈니스 로깅 (도메인별 로거)
└── utils/               # 위 어디에도 속하지 않는 순수 유틸만
```

서브폴더 생성 기준:
- 관련 파일이 2개 이상이면 서브폴더로 그룹화
- 파일 1개뿐이면 common/ 루트에 단일 파일로 배치
- utils/는 최후의 수단 — 주제별 폴더에 넣을 수 있으면 그쪽에 배치

## domains/ 구조 원칙

domains/{name}/ 하위도 고정 파일(routers, services, repositories, schemas, models)에 한정되지 않는다. 도메인 내부 복잡도가 올라가면 필요에 따라 파일/폴더를 추가한다.

예시:
```
domains/order/
├── routers.py
├── services.py
├── repositories.py
├── schemas.py
├── models.py
├── events.py            # 도메인 이벤트
├── constants.py         # 도메인 상수
└── helpers/             # 도메인 내부 헬퍼
```

## 규칙
- 새 도메인 추가 시 domains/{name}/ 하위에 필요한 파일만 생성
- 도메인 간 의존: services 레벨에서만 다른 도메인의 service를 import
- routers → services → repositories 단방향 의존
- models, schemas는 같은 도메인 내에서만 정의
- 공통 테이블(Base, Mixin)은 common/models/에 위치
- common/, domains/ 모두 필요 시 폴더/파일 자유 생성 가능
