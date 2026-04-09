---
name: convention-code-review
description: 프론트엔드 코드 리뷰 체크리스트
---

# Code Review Checklist (Frontend)

작업 완료 전 아래 항목을 확인한다.

## 타입 안전성
- [ ] 컴포넌트 Props 인터페이스 정의
- [ ] any 타입 사용 없음
- [ ] API 응답 타입 정의

## 테스트
- [ ] 새 컴포넌트에 대한 테스트 존재
- [ ] 사용자 행위 중심 테스트
- [ ] 모든 테스트 통과: `npx vitest run`

## 접근성
- [ ] 시맨틱 HTML 사용 (div 남용 금지)
- [ ] 인터랙티브 요소에 aria 속성
- [ ] 키보드 네비게이션 가능

## 성능
- [ ] 불필요한 리렌더 방지 (selector 사용)
- [ ] 큰 리스트 가상화 검토
- [ ] 이미지 lazy loading

## FSD 규칙
- [ ] 레이어 import 방향 준수 (상위 → 하위)
- [ ] 슬라이스 간 직접 import 없음
- [ ] index.ts를 통한 public API 노출
