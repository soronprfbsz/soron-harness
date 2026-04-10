# Monolith Project

FastAPI (backend/) + React + TypeScript + Zustand + TailwindCSS (frontend/)

## 참조 문서
- 아키텍처: [docs/architecture.md](docs/architecture.md)
- 백엔드 컨벤션: [.claude/rules/convention-backend.md](.claude/rules/convention-backend.md)
- 프론트엔드 컨벤션: [.claude/rules/convention-frontend.md](.claude/rules/convention-frontend.md)

## 필수 규칙
- TDD: 테스트 먼저 → 구현 → 리팩터
- Conventional Commits 준수
- backend/ 작업 시 DDD 패턴 준수
- frontend/ 작업 시 FSD 레이어 규칙 준수
- Write/Edit 전 컨벤션 확인 (PreToolUse 훅으로 자동 주입)
