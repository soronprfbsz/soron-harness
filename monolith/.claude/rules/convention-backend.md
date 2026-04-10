---
paths:
  - "backend/**"
---

# Backend Conventions

이 프로젝트의 백엔드 코드 작성 시 아래 컨벤션을 반드시 준수하세요.
상세 내용은 링크된 스킬 파일을 참고합니다.

## 적용 스킬
- [네이밍 규칙](backend/.claude/skills/convention-naming/SKILL.md)
- [프로젝트 구조](backend/.claude/skills/convention-project-structure/SKILL.md)
- [API 설계](backend/.claude/skills/convention-api/SKILL.md)
- [TDD](backend/.claude/skills/convention-tdd/SKILL.md)
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
- URL prefix: /api/

### TDD
- 테스트 먼저 → 최소 구현 → 리팩터
- tests/는 app/ 미러 구조
