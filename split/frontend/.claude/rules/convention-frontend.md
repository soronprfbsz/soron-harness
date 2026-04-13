# Frontend Conventions

이 프로젝트의 코드 작성 시 아래 컨벤션을 반드시 준수하세요.
상세 내용은 링크된 스킬 파일을 참고합니다.

## 적용 스킬
- [네이밍 규칙](.claude/skills/convention-frontend-naming/SKILL.md)
- [프로젝트 구조](.claude/skills/convention-frontend-project-structure/SKILL.md)
- [컴포넌트 설계](.claude/skills/convention-frontend-component/SKILL.md)
- [상태관리](.claude/skills/convention-frontend-state/SKILL.md)
- [TDD](.claude/skills/convention-frontend-tdd/SKILL.md)
- [Git 컨벤션](.claude/skills/convention-frontend-git/SKILL.md)
- [코드 리뷰](.claude/skills/convention-frontend-code-review/SKILL.md)

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
