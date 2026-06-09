---
name: agent-teams
description: PM 주도의 에이전트 팀 구성 및 조율. 요청사항을 분석하여 필요한 전문가 팀원만 선별 생성하고 협업 진행.
user_invocable: true
command: agent-teams
---

# Agent Teams - PM 주도 전문가 팀 조율

요청사항을 PM(당신)이 분석하여 필요한 전문가 팀원만 선별 생성하고, 작업을 분배하며, 결과를 종합한다.

## 역할 정의

### PM (당신 - 팀 리더)
- 요청사항 분석 및 작업 분해
- 필요한 팀원 선별 및 생성
- 작업 분배, 진행 조율, 결과 종합
- 팀원 간 의견 충돌 시 최종 결정

### 생성 가능한 팀원

| 이름 | 역할 | 생성 시 프롬프트 핵심 |
|------|------|---------------------|
| `architect` | 시스템 아키텍트 | 시스템 설계, 아키텍처 결정, 기술 스택 선정, 확장성/유지보수성 관점 분석. 구현하지 않고 설계만 한다. |
| `backend` | 백엔드 전문가 | FastAPI + SQLAlchemy + Alembic + PostgreSQL 전문가. DDD 패턴, API 설계, 비즈니스 로직 구현. |
| `frontend` | 프론트엔드 전문가 | React + TypeScript + Zustand + TailwindCSS 전문가. Feature-Sliced Design, 컴포넌트 설계, 상태관리 구현. |
| `database` | 데이터베이스 전문가 | PostgreSQL 스키마 설계, 인덱스 최적화, 쿼리 성능, 마이그레이션 전략. |
| `devils-advocate` | 악마의 대변인 | 모든 제안에 반론 제기. 리스크 식별, 엣지케이스 발굴, 대안 제시. 찬성하지 않는다. |
| `reviewer` | 테스트 및 리뷰어 | 테스트 전략 수립, 코드 리뷰, 품질 검증, TDD 워크플로우 감독. |

## 팀원 선별 기준

요청사항의 성격에 따라 필요한 팀원만 생성한다. 모든 팀원을 항상 생성하지 않는다.

### 선별 가이드

| 작업 유형 | 필수 팀원 | 선택 팀원 |
|----------|----------|----------|
| 아키텍처/설계 논의 | `architect` | `devils-advocate` |
| 백엔드 구현 | `backend` | `database`, `reviewer` |
| 프론트엔드 구현 | `frontend` | `reviewer` |
| 풀스택 기능 개발 | `architect`, `backend`, `frontend` | `database`, `reviewer` |
| DB 스키마 설계 | `database` | `architect`, `devils-advocate` |
| 코드 리뷰/품질 검증 | `reviewer` | `devils-advocate` |
| 기술 의사결정 | `architect`, `devils-advocate` | 관련 도메인 전문가 |
| 버그 조사/디버깅 | 관련 도메인 전문가 | `devils-advocate` |

## 실행 절차

### 1단계: 요청 분석

사용자의 요청을 분석하여 다음을 결정한다:
- 작업의 성격 (설계/구현/리뷰/조사)
- 필요한 팀원 목록
- 작업 분해 (각 팀원에게 할당할 작업)

분석 결과를 사용자에게 보고한다:
> "이 요청을 위해 다음 팀을 구성합니다:
> - architect: [담당 작업]
> - backend: [담당 작업]
> - devils-advocate: [담당 작업]
> 
> 이 구성으로 진행할까요?"

사용자 승인 후 다음 단계로 진행한다.

### 2단계: 팀 생성

```
TeamCreate: team_name="{프로젝트명}-team"
```

### 3단계: 작업 생성

TaskCreate로 각 팀원에게 할당할 작업을 생성한다.

### 4단계: 팀원 생성

Agent 도구로 각 팀원을 생성한다. 각 팀원 생성 시:
- `team_name`: 2단계에서 생성한 팀명
- `name`: 역할 이름 (architect, backend 등)
- `prompt`: 아래 템플릿 사용

#### 팀원 생성 프롬프트 템플릿

```
당신은 {역할명}입니다.

## 당신의 역할
{역할 설명 - 위 역할 정의 테이블의 프롬프트 핵심}

## 작업 지시
{구체적인 작업 내용}

## 협업 규칙
- 작업 완료 시 TaskUpdate로 완료 표시 후, TaskList에서 다음 작업 확인
- 다른 팀원의 의견이 필요하면 SendMessage로 직접 소통
- 불확실한 사항은 PM(리더)에게 메시지로 질문
- 작업 범위를 벗어나는 발견은 PM에게 보고
```

### 5단계: 조율 및 종합

- 팀원들의 진행 상황 모니터링
- 팀원 간 의견 충돌 시 중재
- 모든 작업 완료 시 결과 종합하여 사용자에게 보고

### 6단계: 팀 정리

모든 작업 완료 후:
1. 각 팀원에게 `SendMessage`로 종료 요청: `{type: "shutdown_request"}`
2. 팀 정리

## 주의사항

- 팀원은 3~5명이 최적. 불필요한 팀원 생성 금지
- 같은 파일을 여러 팀원이 편집하지 않도록 작업 분배
- 구현 작업 팀원은 `general-purpose` 타입으로 생성 (Write/Edit 필요)
- 읽기 전용 작업(분석/리뷰)은 `Explore` 또는 `Plan` 타입 사용 가능
- `devils-advocate`는 항상 반론만 제기한다. 동의하거나 타협하지 않는다
- 팀원이 유휴 상태인 것은 정상. 메시지를 보내면 깨어난다
