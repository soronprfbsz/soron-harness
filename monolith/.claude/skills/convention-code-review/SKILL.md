---
name: convention-code-review
description: 백엔드/프론트엔드 통합 코드 리뷰 체크리스트
---

# Code Review Checklist

작업 완료 전 해당 영역의 항목을 확인한다.

## 공통
- [ ] 모든 테스트 통과
- [ ] 이 프로젝트의 네이밍 컨벤션 준수
- [ ] 불필요한 코드/주석 제거

## Backend (Python)
- [ ] 모든 함수에 파라미터/반환 타입힌트 존재
- [ ] Optional 타입 적절히 사용
- [ ] 새 기능에 대한 pytest 테스트 존재
- [ ] SQL 인젝션 방지 (ORM 사용, raw query 지양)
- [ ] 사용자 입력 Pydantic 스키마로 검증
- [ ] 민감 정보 하드코딩 없음
- [ ] routers → services → repositories 단방향 의존
- [ ] 도메인 간 직접 repository 접근 없음

## Frontend (TypeScript/React)
- [ ] 컴포넌트 Props 인터페이스 정의
- [ ] any 타입 사용 없음
- [ ] 새 컴포넌트에 대한 vitest 테스트 존재
- [ ] 사용자 행위 중심 테스트
- [ ] 시맨틱 HTML 사용
- [ ] 불필요한 리렌더 방지 (selector 사용)
- [ ] FSD 레이어 import 방향 준수
- [ ] 슬라이스 간 직접 import 없음
- [ ] index.ts를 통한 public API 노출
