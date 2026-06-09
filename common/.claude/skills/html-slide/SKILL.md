---
name: html-slide-presentation
description: 다크테마 HTML 슬라이드 프레젠테이션을 생성하는 스킬. 사용자가 "슬라이드 만들어줘", "프레젠테이션 만들어줘", "프레젠테이션 HTML", "유튜브 발표자료", "다크테마 슬라이드", "강의 자료 HTML", "슬라이드 HTML", "발표 자료", "프레젠테이션 생성" 등을 언급할 때 반드시 이 스킬을 사용한다. 순수 HTML/CSS/JS 단일 파일로 생성하며, 외부 라이브러리 없이 키보드 네비게이션과 전체화면을 지원한다. HTML 프레젠테이션을 요청받으면 무조건 이 스킬을 트리거하라.
---

# HTML 슬라이드 프레젠테이션 스킬

 **다크테마 HTML 슬라이드**를 단일 `.html` 파일로 생성한다.
외부 프레임워크 없이 순수 HTML/CSS/JS만 사용. Pretendard 폰트 CDN만 허용.

---

## 작업 순서

1. **주제/내용 파악** — 사용자 제공 내용을 슬라이드 구조로 분해
2. **슬라이드 수 결정** — 5~15장 (주제당 1장 원칙)
3. **컴포넌트 선택** — 아래 "슬라이드 유형별 템플릿 매핑" 참고
4. **[components.md](components.md) 읽기** — 선택한 컴포넌트의 HTML/CSS 코드 확인
5. **[boilerplate.md](boilerplate.md) 읽기** — 전체 HTML 보일러플레이트 확인
6. **단일 HTML 파일 생성** — 모든 CSS/JS 인라인 포함
7. **파일 저장** — `/mnt/user-data/outputs/presentation.html`로 저장 후 `present_files`

---

## 디자인 시스템

### 색상 팔레트

```css
/* 배경 */
--bg-primary: #0a0a0a;    --bg-slide: #111111;
--bg-card: #1a1a1a;        --bg-card-hover: #222222;

/* 강조색 */
--accent-orange: #ff6b35;  /* 주강조 — 제목, 번호, 핵심어 */
--accent-green: #00d084;   /* 보조 — 뱃지, 긍정 상태 */
--accent-purple: #a855f7;  /* 포인트 — 특수 강조 */
--accent-blue: #3b82f6;    /* 정보 — 링크, 보조 */

/* 비교 카드 전용 */
--card-good-bg: #0d2a15;   --card-good-border: #166534;  --card-good-text: #4ade80;
--card-bad-bg: #2a0f0f;    --card-bad-border: #7f1d1d;   --card-bad-text: #f87171;

/* 텍스트 */
--text-primary: #ffffff;   --text-secondary: #aaaaaa;  --text-muted: #666666;

/* 테두리 */
--border: #2a2a2a;         --border-accent: #333333;
```

### 강조색 선택 기준

| 상황 | 색 |
|------|---|
| 제목 핵심어, 번호 뱃지, 일반 강조 | `--accent-orange` |
| 완료/공개/긍정 상태, **장점** | `--accent-green` / `--good-tx` |
| 특수 포인트 | `--accent-purple` |
| 링크, 정보성 | `--accent-blue` |
| **한계/주의/위험 신호** | `--bad-tx` (`.hr` 클래스) |

### 장점/한계 색상 코드 (불릿 리스트)

장점과 한계가 같은 리스트에 섞여 있을 때, 라벨과 불릿을 색상으로 분리해 시각적 가독성을 높인다:

- **장점**: `<li class="good"><strong class="hg">장점</strong> ...` → 불릿·라벨 모두 초록 (긍정 신호)
- **한계**: `<li class="bad"><strong class="hr">한계</strong> ...` → 불릿·라벨 모두 빨강 (주의 신호)

비교 카드(`.card.good` / `.card.bad`) **내부**의 불릿은 카드 색상에 자동 동기화된다 — 별도 클래스 불필요.

### 타이포그래피

폰트: `'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif`
CDN: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css`

#### 폰트 크기 위계 (전체 통일 필수 — clamp로 반응형)

| 요소 | 크기 | weight | 절대 규칙 |
|------|------|--------|----------|
| 표지 메인 타이틀 | `clamp(40px, 4.5vw, 84px)` | 800 | **표지에서만** 사용 |
| 슬라이드 타이틀 | `clamp(30px, 3.3vw, 62px)` | 800 | **모든** 콘텐츠 슬라이드 동일 |
| 소제목 | `clamp(22px, 2.2vw, 42px)` | 700 | 카드/섹션 소제목 |
| 본문 텍스트 | `clamp(18px, 1.55vw, 30px)` | 400 | 리스트 항목, 설명 |
| 카드 내 텍스트 | `clamp(16px, 1.35vw, 26px)` | 400 | 비교 카드 예시 |
| 카드 설명 | `clamp(15px, 1.25vw, 24px)` | 400 | 비교 카드 부연 |
| 요약/결론 텍스트 | `clamp(17px, 1.45vw, 28px)` | 400 | 슬라이드 하단 요약 |
| 피처 설명 | `clamp(17px, 1.45vw, 28px)` | 400 | 예시 박스 위 설명 |
| 피처 포인트 | `clamp(17px, 1.45vw, 28px)` | 400 | 글머리 기호 항목 |
| 코드/예시 박스 | `clamp(15px, 1.2vw, 22px)` | 400 | monospace 예시 |
| 테이블 헤더 | `clamp(14px, 1.15vw, 20px)` | 500 | muted 색상 |
| 테이블 셀 | `clamp(16px, 1.25vw, 24px)` | 400 | 가독성 우선 |
| 섹션 라벨 | `clamp(14px, 1.3vw, 22px)` | 500 | letter-spacing: 3px |
| 배지 번호 (대) | `clamp(16px, 1.5vw, 26px)` | 700 | 슬라이드 번호 배지 |
| 배지 번호 (소) | `clamp(14px, 1.3vw, 22px)` | 700 | 리스트 항목 배지 |

**★ clamp(최소, vw비례, 최대)**: 작은 화면에서도 읽히고, 큰 화면에서는 시원하게 표시됨

### ⭐ 레이아웃 그리드 (모든 슬라이드 공통)

```
슬라이드: 1920 × 1080px (16:9)

┌──────────────────────────────────────────────────────┐
│  padding: 60px 80px                                   │
│  ┌─Badge─┐  ← 좌상단 고정                              │
│  └───────┘  gap: 16px                                 │
│  ┌──────── Title Area ───────────────────────────┐    │
│  │ 동일 위치/크기 (w: 1760px = 1920-80*2)          │    │
│  └───────────────────────────────────────────────┘    │
│  gap: 32px                                            │
│  ┌──────── Content Area ─────────────────────────┐    │
│  │ 유형별 내부만 변경 (flex-grow)                    │    │
│  └───────────────────────────────────────────────┘    │
│                                      Page # (우하단)  │
└──────────────────────────────────────────────────────┘
```

```css
/* ★ 슬라이드: 뷰포트 전체 + 콘텐츠 중앙 + 폭 제한 */
.slide {
  position: fixed; inset: 0;
  display: none; flex-direction: column;
  justify-content: center;          /* 수직 중앙 */
  align-items: center;              /* 가로 중앙 */
  padding: 6vh 7vw;
  background: var(--bg-primary);
}
.slide.active { display: flex; animation: fadeIn 0.3s ease; }
.slide > * { width: 100%; max-width: 1100px; } /* ★ 콘텐츠 폭 제한 */
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

/* 전체화면 시 네비바 숨김 */
body.fs .nav { opacity: 0; pointer-events: none; }
```

**★ 핵심:**
- `position: fixed; inset: 0` → 뷰포트 전체 꽉 채움
- `justify-content: center` + `align-items: center` → 수직+가로 중앙
- `.slide > * { max-width: 1100px }` → 콘텐츠가 가로로 너무 퍼지지 않도록 제한
- 폰트는 `clamp(최소, vw비례, 최대)` 사용
- 전체화면 진입 시 `body.fs` 클래스 → 네비바 숨김

```javascript
// 전체화면 진입/해제 시 네비바 토글
document.addEventListener('fullscreenchange', () => {
  document.body.classList.toggle('fs', !!document.fullscreenElement);
});
```

### 간격 토큰 (vh/vw 비율 기반)

| 간격 유형 | 값 | 용도 |
|-----------|-----|------|
| 슬라이드 상하 패딩 | 6vh | 최상단/최하단 |
| 슬라이드 좌우 패딩 | 7vw | 모든 요소 좌/우 끝 |
| 배지→타이틀 | 2vh | 배지 하단 ~ 타이틀 |
| 타이틀→콘텐츠 | 4vh | 타이틀 ~ 첫 콘텐츠 |
| 비교 카드 간 | 2vw | 좌우 카드 사이 |
| 리스트 아이템 간 | `clamp(18px, 2.8vh, 40px)` | 번호 포인트 간 |
| 카드 내부 패딩 | `clamp(22px, 2.5vw, 44px)` | 상하좌우 비례 |
| 요약 텍스트 상단 | 3.5vh | 카드/콘텐츠 → 요약 |
| 라벨→카드 | 1.8vh | 비교 라벨 → 카드 |
| 섹션 라벨→타이틀 | 2.5vh | 표지 라벨 → 메인 타이틀 |
| 설명→예시박스 | 3vh | 피처 설명 → 코드 박스 |

---

## 슬라이드 유형별 템플릿 매핑

각 슬라이드의 콘텐츠를 아래 유형 중 하나로 매핑하여 일관된 프레젠테이션을 만든다.

| 콘텐츠 유형 | 사용할 컴포넌트 | 예시 |
|------------|----------------|------|
| 표지 | 1. 표지 슬라이드 | 시리즈명 + 메인 제목 + 설명 |
| 핵심 개념 설명 | 2. 번호 뱃지 리스트 | 항목별 단계적 설명 |
| 비교/대조 | 5. 비교 카드 (Good vs Bad) | 비효율 vs 효율 |
| 상황별 안내 | 6. 상황 A/B 카드 | 긍정 상황 vs 주의 상황 |
| 기능/설정 안내 | 7. 피처 카드 | 설명 + 예시 + 보충 포인트 |
| 데이터/현황 | 3. 테이블 / 8. 플랜 테이블 | 비교표, 현황 정리 |
| 여러 항목 나열 | 4. 카드 그리드 | 3열 카드 나열 |
| 강조 한 문장 | 1. 대형 타이틀 (표지 변형) | 핵심 메시지 전달 |

→ 각 컴포넌트의 HTML/CSS 코드는 **[components.md](components.md)** 참조

---

## 일관성 규칙 (절대 위반 금지)

- **타이틀 위치 변경 금지** — Title Area의 위치는 모든 콘텐츠 슬라이드에서 동일
- **타이틀 크기 변경 금지** — 모든 콘텐츠 슬라이드 타이틀은 36px 고정
- **좌우 마진 불일치 금지** — padding-left/right(80px)은 모든 요소에 동일 적용
- **비교 카드 크기 불일치 금지** — 좌측 카드와 우측 카드는 반드시 동일 크기 (flex: 1)
- **간격 불일치 금지** — 같은 유형의 간격은 슬라이드 전체에서 동일한 토큰 값 사용
- **슬라이드 번호(`.pg`) 누락 금지** — 모든 콘텐츠 슬라이드 우하단에 페이지 번호 표시
- **상단 프로그레스바(`.prog` + `.prog-fill`) 누락 금지** — 화면 최상단 3px 두께. 슬라이드 진행률을 좌→우로 채워 시각화. 전체화면에서도 유지
- **폰트 크기 임의 변경 금지** — 폰트 크기 위계 표의 값만 사용

### 배지(.badge) 사용 정책

- 슬라이드 좌상단 큰 배지는 **기본 미사용**. 타이틀이 슬라이드의 주인공이며, 상단 배지는 시각적 노이즈를 유발한다.
- 배지는 **"2. 번호 뱃지 리스트" 컴포넌트 내부**에서 순서 있는 항목을 시각화할 때만 사용한다 (`.badge.sm`).
- 페이지 번호는 우하단 `.pg`로 충분하다.

---

## 금지 사항

- `reveal.js` 등 외부 프레임워크 CDN 의존 금지 (Pretendard 폰트 CDN만 허용)
- 밝은 배경(흰색/베이지) 사용 금지
- 슬라이드당 텍스트 과밀 금지 (1슬라이드 = 1메시지 원칙)
- `font-size` 14px 미만 사용 금지 (가독성)

---

## 참고 파일

| 파일 | 언제 읽는가 |
|------|-----------|
| [references/components.md](components.md) | 컴포넌트 선택 후, HTML/CSS 코드를 확인할 때 |
| [references/boilerplate.md](boilerplate.md) | 최종 HTML 파일을 조립할 때 |
