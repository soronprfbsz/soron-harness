---
name: convention-backend-code-review
description: 백엔드 코드 리뷰 체크리스트
---

# Code Review Checklist (Backend)

작업 완료 전 아래 항목을 확인한다.

## 타입 안전성
- [ ] 모든 함수에 파라미터/반환 타입힌트 존재
- [ ] Optional 타입 적절히 사용

## 테스트
- [ ] 새 기능에 대한 테스트 존재
- [ ] 엣지 케이스 테스트 포함
- [ ] 모든 테스트 통과: `pytest tests/ -v`

## 보안
- [ ] SQL 인젝션 방지 (ORM 사용, raw query 지양)
- [ ] 사용자 입력 Pydantic 스키마로 검증
- [ ] 민감 정보 하드코딩 없음 (config.py에서 환경변수로)

## 구조
- [ ] routers → services → repositories 단방향 의존
- [ ] 도메인 간 직접 repository 접근 없음
- [ ] 공통 로직은 common/에 위치

## 네이밍
- [ ] 이 프로젝트의 네이밍 컨벤션 준수
