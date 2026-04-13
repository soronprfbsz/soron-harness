# Harness Engineering Design Spec

## 개요

FastAPI 백엔드와 React 프론트엔드 프로젝트를 위한 Claude Code 하네스 템플릿.
스킬, 룰, 훅, AGENTS.md를 정의하여 실제 프로젝트에 복사해 바로 사용할 수 있는 구조.

## 레포지토리 구조

```
soron-harness/
├── backend/
│   ├── AGENTS.md
│   ├── docs/
│   │   └── architecture.md
│   └── .claude/
│       ├── settings.json
│       ├── hooks/
│       │   └── pre_write.py
│       ├── rules/
│       │   └── convention-backend.md
│       └── skills/
│           ├── convention-naming/SKILL.md
│           ├── convention-project-structure/SKILL.md
│           ├── convention-api/SKILL.md
│           ├── convention-tdd/SKILL.md
│           ├── convention-git/SKILL.md
│           └── convention-code-review/SKILL.md
└── frontend/
    ├── AGENTS.md
    ├── docs/
    │   └── architecture.md
    └── .claude/
        ├── settings.json
        ├── hooks/
        │   └── pre_write.py
        ├── rules/
        │   └── convention-frontend.md
        └── skills/
            ├── convention-naming/SKILL.md
            ├── convention-project-structure/SKILL.md
            ├── convention-component/SKILL.md
            ├── convention-state/SKILL.md
            ├── convention-tdd/SKILL.md
            ├── convention-git/SKILL.md
            └── convention-code-review/SKILL.md
```

배포: `backend/` 또는 `frontend/` 내부를 실제 프로젝트 루트에 복사.

---

## 기술 스택

### 백엔드
- FastAPI + SQLAlchemy + Alembic + PostgreSQL

### 프론트엔드
- React + TypeScript + Zustand + TailwindCSS

---

## 백엔드 아키텍처 (DDD)

```
app/
├── domains/
│   └── {domain}/
│       ├── routers.py
│       ├── services.py
│       ├── repositories.py
│       ├── schemas.py
│       └── models.py
├── common/
│   ├── config.py
│   ├── database.py
│   ├── middleware/
│   ├── exceptions/
│   ├── logging/
│   ├── models/
│   └── utils/
├── main.py
└── tests/
```

---

## 프론트엔드 아키텍처 (Feature-Sliced Design)

```
src/
├── app/
│   ├── providers/
│   ├── styles/
│   └── index.tsx
├── pages/
│   └── {page}/ui/, index.ts
├── widgets/
│   └── {widget}/ui/, index.ts
├── features/
│   └── {feature}/ui/, model/, api/
├── entities/
│   └── {entity}/ui/, model/, api/
├── shared/
│   ├── ui/
│   ├── lib/
│   ├── api/
│   └── config/
└── tests/
```

레이어 규칙: `app > pages > widgets > features > entities > shared` (상위에서 하위만 import, 역방향 금지)

---

## 스킬 정의

### 백엔드 스킬

| 스킬 | 내용 |
|------|------|
| convention-naming | snake_case(변수/함수), PascalCase(클래스), UPPER_SNAKE(상수), snake_case.py(모듈) |
| convention-project-structure | DDD 레이아웃, domains/ + common/ 구조, 도메인별 파일 구성 |
| convention-api | RESTful 엔드포인트, 복수형 리소스명, HTTP 메서드 매핑, BaseResponse 래핑, 에러 코드 체계 |
| convention-tdd | pytest 기반, 테스트 먼저 → 최소 구현 → 리팩터, 픽스처 패턴, tests/ 미러 구조 |
| convention-git | Conventional Commits(feat/fix/refactor...), 브랜치 전략 |
| convention-code-review | 타입힌트, docstring, 테스트 커버리지, 보안 체크리스트 |

### 프론트엔드 스킬

| 스킬 | 내용 |
|------|------|
| convention-naming | camelCase(변수/함수), PascalCase(컴포넌트/파일), use접두사(훅), UPPER_SNAKE(상수) |
| convention-project-structure | FSD 레이아웃, 레이어 규칙, 슬라이스/세그먼트 구성 |
| convention-component | 단일 책임, 프레젠테이션/컨테이너 분리, props 인터페이스, 컴포넌트 크기 기준 |
| convention-state | Zustand 스토어 구조, slice 패턴, selector, 서버/클라이언트 상태 분리 |
| convention-tdd | vitest + React Testing Library, 사용자 행위 중심 테스트 |
| convention-git | Conventional Commits(feat/fix/refactor...), 브랜치 전략 |
| convention-code-review | 접근성, 타입 안전성, 불필요한 리렌더 방지, 테스트 커버리지 |

---

## convention-backend.md / convention-frontend.md (참조 형식)

PreToolUse 훅으로 매 Write/Edit 시 주입되는 파일.
상단에 스킬 파일 경로 나열 + 하단에 핵심 요약 인라인.

```markdown
# Backend Conventions

## 적용 스킬
- [네이밍](.claude/skills/convention-naming/SKILL.md)
- [프로젝트 구조](.claude/skills/convention-project-structure/SKILL.md)
- ...

## 핵심 요약 (Quick Reference)
### 네이밍
- 함수/변수: snake_case | 클래스: PascalCase | 상수: UPPER_SNAKE
### 구조
- 도메인별: domains/{name}/ 하위에 routers/services/repositories/schemas/models
- 공통: common/ 하위에 config, database, middleware, exceptions, logging, models, utils
...
```

---

## PreToolUse 훅

### settings.json

```jsonc
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "python .claude/hooks/pre_write.py"
      }
    ]
  }
}
```

### pre_write.py

- `.claude/rules/convention-{backend|frontend}.md`를 읽어 stdout 출력
- Claude가 해당 내용을 컨텍스트로 수신
- 추후 파일 경로 필터링, 로깅 등 로직 추가 가능

---

## AGENTS.md

세션 시작 시 항상 로드. 최소한의 라우터 역할만 수행.

### 백엔드

```markdown
# Backend Project

FastAPI + SQLAlchemy + Alembic + PostgreSQL

## 참조 문서
- 아키텍처: [docs/architecture.md](docs/architecture.md)
- 컨벤션: [.claude/rules/convention-backend.md](.claude/rules/convention-backend.md)

## 필수 규칙
- TDD: 테스트 먼저 -> 구현 -> 리팩터
- Conventional Commits 준수
- Write/Edit 전 컨벤션 확인 (PreToolUse 훅으로 자동 주입)
```

### 프론트엔드

```markdown
# Frontend Project

React + TypeScript + Zustand + TailwindCSS

## 참조 문서
- 아키텍처: [docs/architecture.md](docs/architecture.md)
- 컨벤션: [.claude/rules/convention-frontend.md](.claude/rules/convention-frontend.md)

## 필수 규칙
- TDD: 테스트 먼저 -> 구현 -> 리팩터
- Conventional Commits 준수
- FSD 레이어 규칙 준수
- Write/Edit 전 컨벤션 확인 (PreToolUse 훅으로 자동 주입)
```
