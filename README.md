# soron-harness

Claude Code 하네스 템플릿. 실제 프로젝트에 복사하여 컨벤션을 자동 적용.

## 템플릿

| 템플릿 | 용도 | 스택 |
|--------|------|------|
| `backend/` | FastAPI 단독 | FastAPI + SQLAlchemy + Alembic + PostgreSQL (DDD) |
| `frontend/` | React 단독 | React + TypeScript + Zustand + TailwindCSS (FSD) |
| `monolith/` | 백+프론트 모노리스 | 위 둘을 하나의 레포에서 경로 기반으로 분기 |
| `common/` | 공통 스킬 | agent-teams, obsidian, excalidraw |

## 사용법

```bash
# 단독 프로젝트
cp -r backend/{.claude,docs,AGENTS.md} /path/to/my-fastapi-project/
cp -r frontend/{.claude,docs,AGENTS.md} /path/to/my-react-project/

# 모노리스
cp -r monolith/{.claude,docs,AGENTS.md,backend,frontend} /path/to/my-monolith/

# 공통 스킬 추가 (선택)
cp -r common/.claude/skills/* /path/to/my-project/.claude/skills/
```

## 동작 방식

1. **세션 시작** — `AGENTS.md` + `.claude/rules/` 로드
2. **Write/Edit** — PreToolUse 훅이 컨벤션 요약을 컨텍스트에 주입
3. **상세 참조** — 필요 시 `.claude/skills/` 내 스킬 파일을 Read
