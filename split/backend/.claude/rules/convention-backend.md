# Backend Conventions

이 프로젝트의 코드 작성 시 아래 컨벤션을 반드시 준수하세요.
상세 내용은 링크된 스킬 파일을 참고합니다.

## 적용 스킬
- [네이밍 규칙](.claude/skills/convention-backend-naming/SKILL.md)
- [프로젝트 구조](.claude/skills/convention-backend-project-structure/SKILL.md)
- [API 설계](.claude/skills/convention-backend-api/SKILL.md)
- [TDD](.claude/skills/convention-backend-tdd/SKILL.md)
- [Git 컨벤션](.claude/skills/convention-backend-git/SKILL.md)
- [DB 네이밍](.claude/skills/convention-backend-database/SKILL.md)
- [코드 리뷰](.claude/skills/convention-backend-code-review/SKILL.md)

## 핵심 요약 (Quick Reference)

### 네이밍
- 함수/변수: snake_case | 클래스: PascalCase | 상수: UPPER_SNAKE_CASE
- 파일: snake_case.py | 도메인 디렉토리: 단수형 소문자

### DB
- 테이블: 단수형 snake_case (예약어만 복수형) | PK: `id` | FK: `{entity}_id`
- 제약조건: `pk_`/`fk_`/`uq_`/`ck_` 접두사 | 인덱스: `idx_` 접두사
- Boolean: `is_`/`has_`/`can_` | 타임스탬프: `_at` | COMMENT 필수

### 구조 (DDD)
- 도메인별: domains/{name}/ 하위에 routers, services, repositories, schemas, models
- 공통: common/ 하위에 config.py, database.py, middleware/, exceptions/, logging/, models/, utils/
- 의존 방향: routers → services → repositories (단방향)
- 도메인 간 의존: service → service만 허용

### API
- RESTful, 복수형 리소스명, BaseResponse 래핑
- URL prefix: /api/

### TDD
- 테스트 먼저 → 최소 구현 → 리팩터
- tests/는 app/ 미러 구조
