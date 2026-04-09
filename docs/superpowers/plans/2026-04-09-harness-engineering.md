# Harness Engineering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** FastAPI 백엔드와 React 프론트엔드를 위한 Claude Code 하네스 템플릿(스킬, 룰, 훅, AGENTS.md)을 구축한다.

**Architecture:** backend/과 frontend/ 두 루트 디렉토리 각각에 .claude/(skills, rules, hooks), docs/, AGENTS.md를 배치. 실제 프로젝트에 디렉토리 내용을 통째로 복사하면 바로 동작하는 구조.

**Tech Stack:** Claude Code hooks (Python), Markdown skills/rules

---

## File Map

### Backend

| Action | Path |
|--------|------|
| Create | `backend/AGENTS.md` |
| Create | `backend/docs/architecture.md` |
| Create | `backend/.claude/settings.json` |
| Create | `backend/.claude/hooks/pre_write.py` |
| Create | `backend/.claude/rules/convention-backend.md` |
| Create | `backend/.claude/skills/convention-naming/SKILL.md` |
| Create | `backend/.claude/skills/convention-project-structure/SKILL.md` |
| Create | `backend/.claude/skills/convention-api/SKILL.md` |
| Create | `backend/.claude/skills/convention-tdd/SKILL.md` |
| Create | `backend/.claude/skills/convention-git/SKILL.md` |
| Create | `backend/.claude/skills/convention-code-review/SKILL.md` |

### Frontend

| Action | Path |
|--------|------|
| Create | `frontend/AGENTS.md` |
| Create | `frontend/docs/architecture.md` |
| Create | `frontend/.claude/settings.json` |
| Create | `frontend/.claude/hooks/pre_write.py` |
| Create | `frontend/.claude/rules/convention-frontend.md` |
| Create | `frontend/.claude/skills/convention-naming/SKILL.md` |
| Create | `frontend/.claude/skills/convention-project-structure/SKILL.md` |
| Create | `frontend/.claude/skills/convention-component/SKILL.md` |
| Create | `frontend/.claude/skills/convention-state/SKILL.md` |
| Create | `frontend/.claude/skills/convention-tdd/SKILL.md` |
| Create | `frontend/.claude/skills/convention-git/SKILL.md` |
| Create | `frontend/.claude/skills/convention-code-review/SKILL.md` |

---

## Task 1: Backend Skills

**Files:**
- Create: `backend/.claude/skills/convention-naming/SKILL.md`
- Create: `backend/.claude/skills/convention-project-structure/SKILL.md`
- Create: `backend/.claude/skills/convention-api/SKILL.md`
- Create: `backend/.claude/skills/convention-tdd/SKILL.md`
- Create: `backend/.claude/skills/convention-git/SKILL.md`
- Create: `backend/.claude/skills/convention-code-review/SKILL.md`

- [ ] **Step 1: convention-naming/SKILL.md 작성**

```markdown
---
name: convention-naming
description: FastAPI 백엔드 네이밍 컨벤션
---

# Naming Convention (Backend)

## 변수 / 함수
- snake_case 사용
- 동사로 시작하는 함수명: `get_user()`, `create_order()`
- 불리언: is/has/can 접두사: `is_active`, `has_permission`

## 클래스
- PascalCase 사용
- 모델: `User`, `OrderItem`
- 스키마: `UserCreate`, `UserResponse`
- 서비스: `UserService`
- 리포지토리: `UserRepository`

## 상수
- UPPER_SNAKE_CASE: `MAX_RETRY_COUNT`, `DEFAULT_PAGE_SIZE`

## 모듈 / 파일
- snake_case.py: `user_service.py`, `order_repository.py`
- 도메인 디렉토리: 단수형 소문자: `user/`, `order/`

## DB 테이블
- 복수형 snake_case: `users`, `order_items`
- 조인 테이블: `user_roles`

## API 엔드포인트
- 복수형 소문자: `/users`, `/orders/{order_id}/items`
```

- [ ] **Step 2: convention-project-structure/SKILL.md 작성**

```markdown
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
```

- [ ] **Step 3: convention-api/SKILL.md 작성**

```markdown
---
name: convention-api
description: FastAPI REST API 설계 컨벤션
---

# API Design Convention (Backend)

## 엔드포인트 네이밍
- 복수형 리소스: `/users`, `/orders`
- 중첩 리소스: `/users/{user_id}/orders`
- 행위 엔드포인트: `/orders/{order_id}/cancel` (POST)

## HTTP 메서드 매핑
- GET: 조회 (단건/목록)
- POST: 생성
- PUT: 전체 수정
- PATCH: 부분 수정
- DELETE: 삭제

## 응답 포맷

```python
from pydantic import BaseModel
from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None
```

## 라우터 패턴

```python
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=BaseResponse[list[UserResponse]])
async def get_users(service: UserService = Depends(get_user_service)):
    users = await service.get_all()
    return BaseResponse(success=True, data=users)
```

## 에러 처리
- HTTP 상태코드 준수: 400(잘못된 요청), 404(미존재), 422(검증 실패), 500(서버 오류)
- 커스텀 예외 → exception handler에서 BaseResponse 형태로 변환

## 버저닝
- URL prefix: `/api/v1/users`
- main.py에서 `app.include_router(router, prefix="/api/v1")`
```

- [ ] **Step 4: convention-tdd/SKILL.md 작성**

```markdown
---
name: convention-tdd
description: FastAPI 백엔드 TDD 워크플로우
---

# TDD Convention (Backend)

## 워크플로우
1. 실패하는 테스트 작성
2. 테스트를 통과하는 최소 구현
3. 리팩터링 (테스트 유지)

## 테스트 구조
- tests/ 디렉토리는 app/ 미러 구조
- 파일명: `test_{모듈명}.py`
- 함수명: `test_{행위}_{조건}_{기대결과}()`

## 픽스처 패턴

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

@pytest.fixture
def sample_user():
    return {"name": "홍길동", "email": "hong@example.com"}
```

## 테스트 레이어
- Unit: services, repositories 개별 테스트 (의존성 mock)
- Integration: 라우터 → 서비스 → DB 통합 테스트
- conftest.py에 공통 픽스처 정의

## 실행

```bash
pytest tests/ -v                          # 전체
pytest tests/domains/user/ -v             # 도메인별
pytest tests/domains/user/test_services.py::test_name -v  # 단건
```
```

- [ ] **Step 5: convention-git/SKILL.md 작성**

```markdown
---
name: convention-git
description: Git 커밋 및 브랜치 컨벤션
---

# Git Convention

## Conventional Commits

```
<type>(<scope>): <description>
```

### Type
- feat: 새 기능
- fix: 버그 수정
- refactor: 리팩터링 (기능 변경 없음)
- test: 테스트 추가/수정
- docs: 문서 변경
- chore: 빌드, 설정 변경

### Scope
- 도메인명 또는 공통 영역: `feat(user): add login endpoint`

### Description
- 소문자 시작, 마침표 없음, 명령형
- 영어 작성: `add user login endpoint`

## 브랜치 전략
- main: 프로덕션
- develop: 개발 통합
- feature/{도메인}-{기능}: `feature/user-login`
- fix/{이슈번호}-{설명}: `fix/123-login-error`

## 커밋 단위
- 하나의 논리적 변경 = 하나의 커밋
- TDD: 테스트+구현을 하나의 커밋으로
```

- [ ] **Step 6: convention-code-review/SKILL.md 작성**

```markdown
---
name: convention-code-review
description: 백엔드 코드 리뷰 체크리스트
---

# Code Review Checklist (Backend)

작업 완료 전 아래 항목을 확인한다.

## 타입 안전성
- [ ] 모든 함수에 파라미터/반환 타입힌트 존재
- [ ] Optional 타입 적절히 사용

## 테스트
- [ ] 새 기능에 대한 테스트 존재
- [ ] 엣지 케이스 테스트 포함
- [ ] 모든 테스트 통과: `pytest tests/ -v`

## 보안
- [ ] SQL 인젝션 방지 (ORM 사용, raw query 지양)
- [ ] 사용자 입력 Pydantic 스키마로 검증
- [ ] 민감 정보 하드코딩 없음 (config.py에서 환경변수로)

## 구조
- [ ] routers → services → repositories 단방향 의존
- [ ] 도메인 간 직접 repository 접근 없음
- [ ] 공통 로직은 common/에 위치

## 네이밍
- [ ] 이 프로젝트의 네이밍 컨벤션 준수
```

- [ ] **Step 7: 커밋**

```bash
git add backend/.claude/skills/
git commit -m "feat(backend): add convention skills"
```

---

## Task 2: Backend Rules, Hooks, Docs, AGENTS.md

**Files:**
- Create: `backend/.claude/rules/convention-backend.md`
- Create: `backend/.claude/hooks/pre_write.py`
- Create: `backend/.claude/settings.json`
- Create: `backend/docs/architecture.md`
- Create: `backend/AGENTS.md`

- [ ] **Step 1: convention-backend.md 작성**

```markdown
# Backend Conventions

이 프로젝트의 코드 작성 시 아래 컨벤션을 반드시 준수하세요.
상세 내용은 링크된 스킬 파일을 참고합니다.

## 적용 스킬
- [네이밍 규칙](.claude/skills/convention-naming/SKILL.md)
- [프로젝트 구조](.claude/skills/convention-project-structure/SKILL.md)
- [API 설계](.claude/skills/convention-api/SKILL.md)
- [TDD](.claude/skills/convention-tdd/SKILL.md)
- [Git 컨벤션](.claude/skills/convention-git/SKILL.md)
- [코드 리뷰](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약 (Quick Reference)

### 네이밍
- 함수/변수: snake_case | 클래스: PascalCase | 상수: UPPER_SNAKE_CASE
- 파일: snake_case.py | 도메인 디렉토리: 단수형 소문자
- DB 테이블: 복수형 snake_case

### 구조 (DDD)
- 도메인별: domains/{name}/ 하위에 routers, services, repositories, schemas, models
- 공통: common/ 하위에 config.py, database.py, middlewares/, exceptions/, logging/, models/, utils/
- 의존 방향: routers → services → repositories (단방향)
- 도메인 간 의존: service → service만 허용

### API
- RESTful, 복수형 리소스명, BaseResponse 래핑
- URL prefix: /api/v1/

### TDD
- 테스트 먼저 → 최소 구현 → 리팩터
- tests/는 app/ 미러 구조
```

- [ ] **Step 2: pre_write.py 작성**

```python
#!/usr/bin/env python3
"""PreToolUse hook: Write/Edit 실행 전 컨벤션 규칙을 stdout으로 주입."""

from pathlib import Path


def main():
    rules_path = Path(__file__).parent.parent / "rules" / "convention-backend.md"
    if rules_path.exists():
        print(rules_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: settings.json 작성**

```json
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

- [ ] **Step 4: docs/architecture.md 작성**

```markdown
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
│   ├── middlewares/         # 미들웨어
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
```

- [ ] **Step 5: AGENTS.md 작성**

```markdown
# Backend Project

FastAPI + SQLAlchemy + Alembic + PostgreSQL

## 참조 문서
- 아키텍처: [docs/architecture.md](docs/architecture.md)
- 컨벤션: [.claude/rules/convention-backend.md](.claude/rules/convention-backend.md)

## 필수 규칙
- TDD: 테스트 먼저 → 구현 → 리팩터
- Conventional Commits 준수
- Write/Edit 전 컨벤션 확인 (PreToolUse 훅으로 자동 주입)
```

- [ ] **Step 6: 커밋**

```bash
git add backend/.claude/rules/ backend/.claude/hooks/ backend/.claude/settings.json backend/docs/ backend/AGENTS.md
git commit -m "feat(backend): add rules, hooks, docs, and AGENTS.md"
```

---

## Task 3: Frontend Skills

**Files:**
- Create: `frontend/.claude/skills/convention-naming/SKILL.md`
- Create: `frontend/.claude/skills/convention-project-structure/SKILL.md`
- Create: `frontend/.claude/skills/convention-component/SKILL.md`
- Create: `frontend/.claude/skills/convention-state/SKILL.md`
- Create: `frontend/.claude/skills/convention-tdd/SKILL.md`
- Create: `frontend/.claude/skills/convention-git/SKILL.md`
- Create: `frontend/.claude/skills/convention-code-review/SKILL.md`

- [ ] **Step 1: convention-naming/SKILL.md 작성**

```markdown
---
name: convention-naming
description: React 프론트엔드 네이밍 컨벤션
---

# Naming Convention (Frontend)

## 변수 / 함수
- camelCase: `userName`, `fetchUsers()`
- 불리언: is/has/can 접두사: `isLoading`, `hasError`
- 이벤트 핸들러: handle 접두사: `handleClick`, `handleSubmit`

## 컴포넌트
- PascalCase: `UserProfile`, `OrderList`
- 파일명 = 컴포넌트명: `UserProfile.tsx`

## 훅
- use 접두사: `useAuth`, `useUserStore`
- 파일명: `useAuth.ts`

## 상수
- UPPER_SNAKE_CASE: `API_BASE_URL`, `MAX_ITEMS`

## 타입 / 인터페이스
- PascalCase: `UserResponse`, `OrderFormProps`
- Props: 컴포넌트명 + Props: `UserProfileProps`

## 디렉토리
- FSD 레이어: 소문자 복수형: `pages/`, `features/`
- 슬라이스: 소문자 케밥케이스: `user-profile/`
- 세그먼트: 소문자: `ui/`, `model/`, `api/`
```

- [ ] **Step 2: convention-project-structure/SKILL.md 작성**

```markdown
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
```

- [ ] **Step 3: convention-component/SKILL.md 작성**

```markdown
---
name: convention-component
description: React 컴포넌트 설계 컨벤션
---

# Component Design Convention (Frontend)

## 단일 책임
- 하나의 컴포넌트 = 하나의 역할
- 150줄 초과 시 분리 검토

## Props 인터페이스

```tsx
interface UserCardProps {
  user: User;
  onSelect: (id: string) => void;
  isActive?: boolean;
}

export function UserCard({ user, onSelect, isActive = false }: UserCardProps) {
  return (/* ... */);
}
```

## 컴포넌트 분류
- UI 컴포넌트 (shared/ui): 비즈니스 로직 없음, props만으로 동작
- Feature 컴포넌트 (features/): 특정 비즈니스 로직 포함
- Page 컴포넌트 (pages/): 레이아웃 조합, 데이터 페칭 진입점

## 패턴
- children 패턴: 레이아웃/래퍼 컴포넌트
- 합성 패턴: 복잡한 UI 조합
- 제어/비제어: 폼 입력은 제어 컴포넌트 우선

## TailwindCSS
- 인라인 className 사용
- 반복 스타일은 @apply 또는 공통 컴포넌트로 추출
- 조건부 스타일: clsx 또는 cn 유틸 사용
```

- [ ] **Step 4: convention-state/SKILL.md 작성**

```markdown
---
name: convention-state
description: Zustand 상태관리 컨벤션
---

# State Management Convention (Frontend - Zustand)

## 스토어 구조

```tsx
// entities/user/model/store.ts
import { create } from "zustand";

interface UserState {
  users: User[];
  isLoading: boolean;
  fetchUsers: () => Promise<void>;
  addUser: (user: User) => void;
}

export const useUserStore = create<UserState>((set) => ({
  users: [],
  isLoading: false,
  fetchUsers: async () => {
    set({ isLoading: true });
    const users = await userApi.getAll();
    set({ users, isLoading: false });
  },
  addUser: (user) => set((state) => ({ users: [...state.users, user] })),
}));
```

## 규칙
- 스토어 위치: 해당 슬라이스의 model/ 세그먼트
- 스토어명: use{Entity}Store
- 서버 상태 vs 클라이언트 상태 분리
  - 서버 상태: TanStack Query 또는 스토어 내 async action
  - 클라이언트 상태: Zustand (UI 상태, 폼 상태)

## Selector 패턴

```tsx
// 개별 selector로 불필요한 리렌더 방지
const users = useUserStore((state) => state.users);
const isLoading = useUserStore((state) => state.isLoading);
```

## Slice 패턴 (대규모 스토어)

```tsx
const createUserSlice = (set) => ({
  users: [],
  addUser: (user) => set((state) => ({ users: [...state.users, user] })),
});
```
```

- [ ] **Step 5: convention-tdd/SKILL.md 작성**

```markdown
---
name: convention-tdd
description: React 프론트엔드 TDD 워크플로우
---

# TDD Convention (Frontend)

## 워크플로우
1. 실패하는 테스트 작성
2. 테스트를 통과하는 최소 구현
3. 리팩터링 (테스트 유지)

## 도구
- 테스트 러너: vitest
- 컴포넌트 테스트: React Testing Library
- 사용자 이벤트: @testing-library/user-event

## 테스트 작성 원칙
- 사용자 행위 중심: 구현 세부사항이 아닌 사용자가 보는 것을 테스트
- getByRole, getByText 우선 (getByTestId는 최후 수단)

## 테스트 패턴

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { UserCard } from "./UserCard";

describe("UserCard", () => {
  it("사용자 이름을 표시한다", () => {
    render(<UserCard user={{ name: "홍길동" }} />);
    expect(screen.getByText("홍길동")).toBeInTheDocument();
  });

  it("클릭 시 onSelect를 호출한다", async () => {
    const onSelect = vi.fn();
    render(<UserCard user={{ id: "1", name: "홍길동" }} onSelect={onSelect} />);
    await userEvent.click(screen.getByRole("button"));
    expect(onSelect).toHaveBeenCalledWith("1");
  });
});
```

## 실행

```bash
npx vitest run                           # 전체
npx vitest run src/features/auth/        # 슬라이스별
npx vitest run src/features/auth/ui/LoginForm.test.tsx  # 단건
```
```

- [ ] **Step 6: convention-git/SKILL.md 작성**

```markdown
---
name: convention-git
description: Git 커밋 및 브랜치 컨벤션
---

# Git Convention

## Conventional Commits

```
<type>(<scope>): <description>
```

### Type
- feat: 새 기능
- fix: 버그 수정
- refactor: 리팩터링 (기능 변경 없음)
- test: 테스트 추가/수정
- docs: 문서 변경
- chore: 빌드, 설정 변경

### Scope
- FSD 슬라이스명 또는 레이어: `feat(user): add profile card`

### Description
- 소문자 시작, 마침표 없음, 명령형
- 영어 작성: `add user profile card`

## 브랜치 전략
- main: 프로덕션
- develop: 개발 통합
- feature/{슬라이스}-{기능}: `feature/user-profile`
- fix/{이슈번호}-{설명}: `fix/123-login-error`

## 커밋 단위
- 하나의 논리적 변경 = 하나의 커밋
- TDD: 테스트+구현을 하나의 커밋으로
```

- [ ] **Step 7: convention-code-review/SKILL.md 작성**

```markdown
---
name: convention-code-review
description: 프론트엔드 코드 리뷰 체크리스트
---

# Code Review Checklist (Frontend)

작업 완료 전 아래 항목을 확인한다.

## 타입 안전성
- [ ] 컴포넌트 Props 인터페이스 정의
- [ ] any 타입 사용 없음
- [ ] API 응답 타입 정의

## 테스트
- [ ] 새 컴포넌트에 대한 테스트 존재
- [ ] 사용자 행위 중심 테스트
- [ ] 모든 테스트 통과: `npx vitest run`

## 접근성
- [ ] 시맨틱 HTML 사용 (div 남용 금지)
- [ ] 인터랙티브 요소에 aria 속성
- [ ] 키보드 네비게이션 가능

## 성능
- [ ] 불필요한 리렌더 방지 (selector 사용)
- [ ] 큰 리스트 가상화 검토
- [ ] 이미지 lazy loading

## FSD 규칙
- [ ] 레이어 import 방향 준수 (상위 → 하위)
- [ ] 슬라이스 간 직접 import 없음
- [ ] index.ts를 통한 public API 노출
```

- [ ] **Step 8: 커밋**

```bash
git add frontend/.claude/skills/
git commit -m "feat(frontend): add convention skills"
```

---

## Task 4: Frontend Rules, Hooks, Docs, AGENTS.md

**Files:**
- Create: `frontend/.claude/rules/convention-frontend.md`
- Create: `frontend/.claude/hooks/pre_write.py`
- Create: `frontend/.claude/settings.json`
- Create: `frontend/docs/architecture.md`
- Create: `frontend/AGENTS.md`

- [ ] **Step 1: convention-frontend.md 작성**

```markdown
# Frontend Conventions

이 프로젝트의 코드 작성 시 아래 컨벤션을 반드시 준수하세요.
상세 내용은 링크된 스킬 파일을 참고합니다.

## 적용 스킬
- [네이밍 규칙](.claude/skills/convention-naming/SKILL.md)
- [프로젝트 구조](.claude/skills/convention-project-structure/SKILL.md)
- [컴포넌트 설계](.claude/skills/convention-component/SKILL.md)
- [상태관리](.claude/skills/convention-state/SKILL.md)
- [TDD](.claude/skills/convention-tdd/SKILL.md)
- [Git 컨벤션](.claude/skills/convention-git/SKILL.md)
- [코드 리뷰](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약 (Quick Reference)

### 네이밍
- 변수/함수: camelCase | 컴포넌트: PascalCase | 훅: use접두사 | 상수: UPPER_SNAKE_CASE
- 파일: 컴포넌트=PascalCase.tsx, 유틸=camelCase.ts

### 구조 (FSD)
- 레이어: app → pages → widgets → features → entities → shared
- 상위에서 하위만 import, 역방향/동일레이어 슬라이스 간 금지
- 각 슬라이스는 index.ts로 public API 노출

### 컴포넌트
- 단일 책임, 150줄 초과 시 분리 검토
- Props 인터페이스 필수 정의

### 상태관리
- Zustand: use{Entity}Store, selector 패턴으로 리렌더 방지
- 서버 상태 / 클라이언트 상태 분리

### TDD
- 테스트 먼저 → 최소 구현 → 리팩터
- vitest + React Testing Library, 사용자 행위 중심
```

- [ ] **Step 2: pre_write.py 작성**

```python
#!/usr/bin/env python3
"""PreToolUse hook: Write/Edit 실행 전 컨벤션 규칙을 stdout으로 주입."""

from pathlib import Path


def main():
    rules_path = Path(__file__).parent.parent / "rules" / "convention-frontend.md"
    if rules_path.exists():
        print(rules_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: settings.json 작성**

```json
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

- [ ] **Step 4: docs/architecture.md 작성**

```markdown
# Frontend Architecture

## 기술 스택
- React + TypeScript + Zustand + TailwindCSS

## Feature-Sliced Design 구조

```
src/
├── app/               # 앱 초기화, 프로바이더, 글로벌 스타일
├── pages/             # 페이지 (라우트 단위)
├── widgets/           # 독립적 UI 블록
├── features/          # 사용자 인터랙션
├── entities/          # 비즈니스 엔티티
├── shared/            # 재사용 공통 코드 (ui, lib, api, config)
└── tests/
```

## 레이어 규칙
- import 방향: app → pages → widgets → features → entities → shared
- 역방향 금지, 같은 레이어 슬라이스 간 직접 import 금지
- 각 슬라이스는 index.ts를 통해 public API만 노출

## 세그먼트 구성
- ui/: 컴포넌트
- model/: 스토어, 타입, 비즈니스 로직
- api/: API 호출
- lib/: 유틸리티 (shared에서만)
- config/: 설정 (shared에서만)
```

- [ ] **Step 5: AGENTS.md 작성**

```markdown
# Frontend Project

React + TypeScript + Zustand + TailwindCSS

## 참조 문서
- 아키텍처: [docs/architecture.md](docs/architecture.md)
- 컨벤션: [.claude/rules/convention-frontend.md](.claude/rules/convention-frontend.md)

## 필수 규칙
- TDD: 테스트 먼저 → 구현 → 리팩터
- Conventional Commits 준수
- FSD 레이어 규칙 준수
- Write/Edit 전 컨벤션 확인 (PreToolUse 훅으로 자동 주입)
```

- [ ] **Step 6: 커밋**

```bash
git add frontend/.claude/rules/ frontend/.claude/hooks/ frontend/.claude/settings.json frontend/docs/ frontend/AGENTS.md
git commit -m "feat(frontend): add rules, hooks, docs, and AGENTS.md"
```
