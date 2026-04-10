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
- 백엔드: 도메인명: `feat(user): add login endpoint`
- 프론트엔드: FSD 슬라이스명: `feat(user): add profile card`
- 공통: `chore(deps): update dependencies`

### Description
- 소문자 시작, 마침표 없음, 명령형
- 영어 작성

## 브랜치 전략
- main: 프로덕션
- develop: 개발 통합
- feature/{영역}-{기능}: `feature/user-login`, `feature/user-profile`
- fix/{이슈번호}-{설명}: `fix/123-login-error`

## 커밋 단위
- 하나의 논리적 변경 = 하나의 커밋
- TDD: 테스트+구현을 하나의 커밋으로
