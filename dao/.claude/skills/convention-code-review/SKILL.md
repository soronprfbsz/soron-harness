---
name: convention-code-review
description: 4-레이어 통합 코드 리뷰 체크리스트 (Collector/Consumer/API/Web)
---

# Code Review Checklist

작업 완료 전 해당 레이어의 항목을 확인한다.

## 공통
- [ ] 모든 테스트 통과
- [ ] 해당 레이어 네이밍 컨벤션 준수
- [ ] 불필요한 코드/주석 제거
- [ ] DateTime: UTC 저장, naive datetime 없음
- [ ] 민감 정보 하드코딩 없음
- [ ] 로깅: 구조화 JSON, stdout, 민감정보 금지

## Collector (Go)
- [ ] receiver → processor → exporter 단방향 의존
- [ ] 에러 래핑 (`fmt.Errorf("component: %w", err)`)
- [ ] Kafka Key = device_id
- [ ] 테이블 드리븐 테스트 존재
- [ ] `go vet` / `golangci-lint` 통과

## Consumer (Python)
- [ ] consumers → validators → writers 단방향 의존
- [ ] Pydantic 스키마 검증 존재
- [ ] 수동 커밋 (auto.commit=False)
- [ ] 배치 처리 + 플러시 타임아웃 적용
- [ ] ClickHouse INSERT에 column_names 명시
- [ ] 검증 실패 시 메시지 드롭 (프로세스 중단 안 함)

## API (Python/FastAPI)
- [ ] router → service → repository 단방향 의존
- [ ] 도메인 간 직접 repository 접근 없음
- [ ] 모든 함수에 타입힌트 존재
- [ ] Pydantic 스키마로 입력 검증
- [ ] 에러 응답: `{ error: { code, message, details } }`
- [ ] SQL 인젝션 방지 (ORM/파라미터 바인딩)
- [ ] JWT/RBAC 권한 검증 적용

## Web (React/TypeScript)
- [ ] FSD 레이어 import 방향 준수 (상위→하위만)
- [ ] 슬라이스 간 직접 import 없음
- [ ] index.ts를 통한 public API 노출
- [ ] Props 인터페이스 정의, `any` 없음
- [ ] Zustand selector 패턴 (리렌더 방지)
- [ ] 시맨틱 HTML 사용
- [ ] 사용자 행위 중심 테스트
