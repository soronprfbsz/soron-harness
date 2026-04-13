---
paths:
  - "web/**"
---

# Web Conventions (React + TypeScript)

SPA 대시보드. 상세 스킬 참조:
- [네이밍](web/.claude/skills/convention-web-naming/SKILL.md)
- [프로젝트 구조](web/.claude/skills/convention-web-project-structure/SKILL.md)
- [컴포넌트](web/.claude/skills/convention-web-component/SKILL.md)
- [상태관리](web/.claude/skills/convention-web-state/SKILL.md)
- [TDD](web/.claude/skills/convention-web-tdd/SKILL.md)
- [Git](.claude/skills/convention-git/SKILL.md)
- [Code Review](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약

### 네이밍
- 변수/함수: `camelCase` | 컴포넌트: `PascalCase`
- 훅: `use` 접두사 | 상수: `UPPER_SNAKE_CASE`
- 파일: 컴포넌트=`PascalCase.tsx`, 유틸=`camelCase.ts`

### 구조 (FSD)
- `src/{app,pages,widgets,features,entities,shared}`
- Import: 상위→하위만, 슬라이스 간 직접 import 금지

### 컴포넌트
- 단일 책임, 150줄 초과 분리, Props 인터페이스 필수, `any` 금지

### 상태관리
- Zustand: `use{Entity}Store`, selector 패턴
