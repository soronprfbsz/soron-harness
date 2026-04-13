# Frontend Architecture

## 기술 스택
- React + TypeScript + Zustand + TailwindCSS

## Feature-Sliced Design 구조

```
src/
├── app/               # 앱 초기화, 프로바이더, 글로벌 스타일
├── pages/             # 페이지 (라우트 단위)
├── widgets/           # 독립적 UI 블록
├── features/          # 사용자 인터랙션
├── entities/          # 비즈니스 엔티티
├── shared/            # 재사용 공통 코드 (ui, lib, api, config)
└── tests/
```

## 레이어 규칙
- import 방향: app → pages → widgets → features → entities → shared
- 역방향 금지, 같은 레이어 슬라이스 간 직접 import 금지
- 각 슬라이스는 index.ts를 통해 public API만 노출

## 세그먼트 구성
- ui/: 컴포넌트
- model/: 스토어, 타입, 비즈니스 로직
- api/: API 호출
- lib/: 유틸리티 (shared에서만)
- config/: 설정 (shared에서만)
