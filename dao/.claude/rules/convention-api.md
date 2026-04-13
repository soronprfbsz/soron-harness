---
paths:
  - "api/**"
---

# API Conventions (Python/FastAPI)

단일 FastAPI, DDD. 상세 스킬 참조:
- [네이밍](api/.claude/skills/convention-api-naming/SKILL.md)
- [프로젝트 구조](api/.claude/skills/convention-api-project-structure/SKILL.md)
- [API 설계](api/.claude/skills/convention-api-rest-design/SKILL.md)
- [Database](api/.claude/skills/convention-api-database/SKILL.md)
- [TDD](api/.claude/skills/convention-api-tdd/SKILL.md)
- [Git](.claude/skills/convention-git/SKILL.md)
- [Code Review](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약

### 네이밍
- 파일/변수/함수: `snake_case` | 클래스: `PascalCase`
- 상수: `UPPER_SNAKE_CASE` | 도메인: 단수형 소문자
- DB 테이블: 단수형 (`users`/`groups` 제외)

### 구조
- `app/domains/{name}/{router,schema,service,repository,model}.py`
- 의존: router → service → repository (단방향)

### API
- URL: `/api/{리소스}` 복수형, JSON: camelCase
- 에러: `{ error: { code, message, details } }`

### 인증
- JWT + RBAC (Super Admin/Admin/Operator/Viewer)
