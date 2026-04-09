# soron-harness

Claude Code 하네스 템플릿. 실제 프로젝트에 복사하여 컨벤션을 자동 적용.

## 대상 스펙

### Backend
- **Framework:** FastAPI
- **ORM:** SQLAlchemy + Alembic
- **DB:** PostgreSQL
- **Architecture:** DDD (Domain-Driven Design)
- **Test:** pytest

### Frontend
- **Framework:** React + TypeScript
- **State:** Zustand
- **Style:** TailwindCSS
- **Architecture:** Feature-Sliced Design (FSD)
- **Test:** vitest + React Testing Library

## 구조

```
soron-harness/
├── backend/           # FastAPI 프로젝트용 하네스
│   ├── AGENTS.md
│   ├── docs/architecture.md
│   └── .claude/
│       ├── settings.json          # PreToolUse 훅 설정
│       ├── hooks/pre_write.py     # Write/Edit 시 컨벤션 주입
│       ├── rules/convention-backend.md
│       └── skills/                # 6개 컨벤션 스킬
└── frontend/          # React 프로젝트용 하네스
    ├── AGENTS.md
    ├── docs/architecture.md
    └── .claude/
        ├── settings.json
        ├── hooks/pre_write.py
        ├── rules/convention-frontend.md
        └── skills/                # 7개 컨벤션 스킬
```

## 사용법

```bash
# FastAPI 프로젝트에 적용
cp -r backend/.claude  /path/to/my-project/
cp -r backend/docs     /path/to/my-project/
cp    backend/AGENTS.md /path/to/my-project/

# React 프로젝트에 적용
cp -r frontend/.claude  /path/to/my-project/
cp -r frontend/docs     /path/to/my-project/
cp    frontend/AGENTS.md /path/to/my-project/
```

복사 후 Claude Code에서 Write/Edit 실행 시 PreToolUse 훅이 컨벤션을 자동 주입합니다.

## 동작 방식

1. **세션 시작** — `AGENTS.md`와 `.claude/rules/` 로드
2. **Write/Edit 실행** — PreToolUse 훅이 `pre_write.py` 실행 → 컨벤션 요약을 컨텍스트에 주입
3. **상세 참조** — Claude가 필요 시 `.claude/skills/` 내 개별 스킬 파일을 Read
