---
name: excalidraw
description: >
  Obsidian Excalidraw 플러그인용 .excalidraw.md 파일을 생성한다.
  플로우차트, 시스템 아키텍처, 시퀀스 다이어그램, 블록 다이어그램 등 모든 유형의 다이어그램을 지원한다.
  사용자가 다이어그램, 플로우차트, 아키텍처 그림, 시각화, 도식, 구성도, 흐름도를 요청하거나
  Excalidraw 파일 생성을 언급할 때 반드시 이 스킬을 사용할 것.
  ".excalidraw.md 만들어줘", "구성도 그려줘", "흐름 다이어그램으로 정리해줘" 같은 요청에도 트리거한다.
---

# Obsidian Excalidraw 다이어그램 생성 스킬

Obsidian Excalidraw 플러그인의 `.excalidraw.md` 파일을 생성한다. Obsidian 플러그인은 excalidraw.com과 호환되지 않는 부분이 많아 아래 규칙을 반드시 따라야 한다. 규칙을 어기면 텍스트 중복 렌더링, 화살표 부유, 레이아웃 붕괴가 발생한다.

---

## 파일 구조

```
---
excalidraw-plugin: parsed
tags: [excalidraw]
---

# Excalidraw Data

## Text Elements

%%
## Drawing
```json
{ ... }
```
%%
```

핵심:
- `## Text Elements` 섹션은 **반드시 비워둔다** — 내용을 넣으면 Drawing JSON의 텍스트와 이중 렌더링됨
- Drawing 블록은 **plain `json`** 포맷으로 작성 — `compressed-json` 사용 금지 (Obsidian이 저장 시 자동 압축하는 건 정상)
- 한글 텍스트는 JSON 레벨에서 **Unicode escape** 필수 — `주문` → `\uc8fc\ubb38`. 단, 수동으로 escape 문자열을 만들지 말고 JSON 직렬화 시 `ensure_ascii=true` 옵션으로 자동 처리할 것. 수동 escape + JSON 직렬화를 동시에 하면 이중 escape(`\\uc8fc\\ubb38`)가 되어 escape 문자가 그대로 표시된다.

---

## 절대 사용 금지 속성

Obsidian Excalidraw 플러그인에서 작동하지 않는 속성들이다. 사용하면 텍스트 미표시, 화살표 부유 등 심각한 렌더링 오류가 발생한다.

| 속성 | 이유 |
|---|---|
| `label` | Obsidian 미지원 — 텍스트 미표시 |
| `textAlign: "center"` | 무시됨. x좌표를 텍스트 시작점으로 렌더링 |
| `containerId` / `boundElements` | 텍스트-도형 바인딩 미작동 |
| `startBinding` / `endBinding` | 화살표-도형 연결 미작동 |

---

## 텍스트 작성

모든 텍스트는 `label`이 아닌 **별도 `type: "text"` 요소**로 작성한다.

```json
{
  "id": "t_example",
  "type": "text",
  "x": 120,
  "y": 45,
  "width": 160,
  "height": 24,
  "text": "\uc8fc\ubb38 \uc11c\ube44\uc2a4",
  "fontSize": 18,
  "fontFamily": 4,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "#e5e5e5",
  "opacity": 100
}
```

규칙:
- `fontFamily: 4` (산세리프) 항상 사용. `1`(Virgil 손글씨) 사용 금지
- `textAlign`은 항상 `"left"` — `"center"`는 Obsidian에서 무시됨
- 시각적 중앙 정렬은 x좌표를 직접 계산: `x = 박스.x + (박스.width - 텍스트폭) / 2`

텍스트 너비 추정 (fontFamily: 4) — 넉넉하게 잡아야 텍스트가 박스를 넘치지 않는다:
- 영문 일반 글자 ≈ fontSize × 0.62
- 영문 넓은 글자(m, w, M, W) ≈ fontSize × 0.75
- 영문 좁은 글자(i, l, j, !, |, :, ;) ≈ fontSize × 0.35
- 한글/CJK ≈ fontSize × 1.05
- 공백 ≈ fontSize × 0.35

**박스 크기는 텍스트 기준으로 결정한다 (text-first sizing):**

텍스트 너비를 먼저 계산하고, 좌우 패딩(최소 30px씩)을 더해 박스 폭을 결정한다. 절대로 박스 크기를 먼저 정하고 텍스트를 억지로 넣지 않는다.

```
박스.width = max(텍스트폭 + 60, 최소폭)
박스.height = max(텍스트높이 + 32, 최소높이)
텍스트.x = 박스.x + (박스.width - 텍스트폭) / 2
텍스트.y = 박스.y + (박스.height - 텍스트높이) / 2
```

텍스트 높이: `fontSize × 1.4`

---

## 도형 작성

```json
{
  "id": "box1",
  "type": "rectangle",
  "x": 400,
  "y": 50,
  "width": 920,
  "height": 506,
  "strokeColor": "#f59e0b",
  "backgroundColor": "#1a1200",
  "fillStyle": "solid",
  "strokeWidth": 3,
  "roughness": 0,
  "opacity": 100,
  "roundness": {"type": 3}
}
```

- `roughness: 0` → 매끈한 선
- `roundness: {"type": 3}` → 둥근 모서리

도형 높이 역산 — 임의 설정 금지, 내부 요소 합으로 계산:

```
도형 높이 = 상단패딩(20) + 타이틀높이 + 간격(16) + 내부요소높이합 + 내부간격합 + 하단패딩(20)
```

표준 패딩:
- 외곽 박스 상하좌우 여백: 20px
- 타이틀 → 첫 내부 요소: 16px
- 내부 요소 간: 16px

---

## 캔버스 사용 원칙

- 캔버스는 **넉넉하되 과하지 않게** 사용한다 — 좁으면 겹치고, 너무 넓으면 빈 공간이 과해진다
- 같은 계층의 도형 간격: **30~60px** (화살표 공간 확보)
- 다른 계층(Stage) 간 간격: **60~100px** (서브타이틀 + 화살표 공간)
- 도형 내부 패딩은 상하좌우 균일하게 (최소 좌우 30px, 상하 16px)
- 서브타이틀/주석은 박스 하단 **6~10px 아래**에 배치
- 간격은 겹침이 없는 최소값을 기준으로 잡되, 의미 있는 그룹 사이에만 넓게 준다

---

## 화살표 작성

`startBinding`/`endBinding`이 작동하지 않으므로 **좌표를 직접 계산**한다.

### 핵심 원칙

1. **화살표는 반드시 도형의 가장자리(edge)에서 시작/종료**해야 한다
2. 두 도형이 수직/수평으로 정렬되지 않으면 **반드시 꺾이는(bent) 화살표**를 사용한다 — 직선 화살표는 정렬된 경우에만 사용
3. **한 도형에 여러 화살표가 연결될 때**: 연결점을 도형 중심에서 일정 간격(30~50px)으로 분산시켜 겹침을 방지한다

### 수평 화살표 (좌→우)

두 도형이 같은 높이에 있을 때, 우측 경계에서 좌측 경계로 연결:
```
출발 x = 출발도형.x + 출발도형.width       (우측 경계)
출발 y = 출발도형.y + 출발도형.height / 2   (세로 중앙)
width  = 도착도형.x - 출발x
points = [[0, 0], [width, 0]]
```

### 수직 꺾임 화살표 (위→아래, 핵심 패턴)

두 도형이 상하 관계이지만 x좌표가 다를 때 사용한다. **직선 수직 화살표로 그리면 도형에 연결되지 않으므로 반드시 꺾어야 한다.**

```
출발 x = 출발도형.x + 출발도형.width/2 + src_offset   (하단 중앙 + 오프셋)
출발 y = 출발도형.y + 출발도형.height                  (하단)
도착 x = 도착도형.x + 도착도형.width/2 + dst_offset   (상단 중앙 + 오프셋)
도착 y = 도착도형.y                                    (상단)
dx = 도착x - 출발x
dy = 도착y - 출발y
mid = dy * 0.5                                         (중간 꺾임 지점)
points = [[0, 0], [0, mid], [dx, mid], [dx, dy]]
```

x좌표가 거의 같으면(|dx| < 5) 꺾임 없이 직선 `[[0, 0], [0, dy]]`로 그린다.

### 수평 꺾임 화살표 (좌→우, 높이가 다를 때)

```
출발 x = 출발도형.x + 출발도형.width    (우측 경계)
출발 y = 출발도형.y + 출발도형.height/2  (세로 중앙)
도착 x = 도착도형.x                     (좌측 경계)
도착 y = 도착도형.y + 도착도형.height/2  (세로 중앙)
dx = 도착x - 출발x, dy = 도착y - 출발y
mid = dx / 2
points = [[0,0], [mid, 0], [mid, dy], [dx, dy]]
```

### 연결점 분산 (여러 화살표 → 한 도형)

N개의 화살표가 한 도형의 같은 변(상단/하단/좌측/우측)에 연결될 때:
```
간격 = 40~60px
오프셋 목록: [-(N-1)/2 × 간격, ..., 0, ..., +(N-1)/2 × 간격]
```

예: 3개 화살표가 도형 상단에 연결 → `dst_offset` = -50, 0, +50

이렇게 하면 화살표가 도형 중앙 한 점에 집중되지 않고 가장자리를 따라 분산된다.

---

## 레이아웃 설계 패턴

세로 중앙 정렬:
```
작은도형.y = 큰도형.y + (큰도형.height - 작은도형.height) / 2
```

도형 내 텍스트 세로 중앙 정렬:
```
텍스트.y = 도형.y + (도형.height - 텍스트.height) / 2
```

도형 수정 후 반드시 재점검:
1. 패딩 — 상하좌우 여백이 의도한 값인지
2. 텍스트 위치 — 중앙 정렬 x 좌표가 올바른지
3. 화살표 — 출발/도착 좌표가 변경된 도형 경계에 맞는지
4. 인접 도형 — 겹침이나 간격 틀어짐 없는지

---

## 표준 색상 팔레트 (다크 테마)

| 용도 | strokeColor | backgroundColor |
|---|---|---|
| 초록 (성공, Producer) | `#22c55e` | `#0d2a15` |
| 빨강 (오류, Broker) | `#ef4444` | `#2a0f0f` |
| 파랑 (정보, Consumer) | `#4a9eed` | `#0a1a2e` |
| 주황 (클러스터, 강조) | `#f59e0b` | `#1a1200` |
| 보라 (보조 시스템) | `#8b5cf6` | `#1a0a2e` |
| 회색 (Replica, 보조) | `#6b7280` | `#252525` |
| 노랑 (강조 텍스트) | `#fbbf24` | — |
| 캔버스 배경 | `#1a1a2e` | — |

---

## Drawing JSON 구조

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [ ... ],
  "appState": {
    "viewBackgroundColor": "#1a1a2e",
    "gridSize": 20
  }
}
```

`elements` 배열 순서 = z-order. 먼저 작성한 것이 아래 레이어.
외곽 박스 → 내부 도형 → 텍스트 → 화살표 순서로 작성한다.

---

## 작업 순서

1. **레이아웃 설계** — 도형별 x, y, width, height를 역산 공식으로 먼저 계산
2. **도형 작성** — 외곽 박스 → 내부 도형 순서 (z-order)
3. **텍스트 작성** — 각 도형 직후에 해당 텍스트 요소 작성, 한글은 Unicode escape
4. **화살표 작성** — 연결할 도형 좌표 확인 후 경계에 맞게 계산
5. **좌표 검증** — 모든 화살표의 출발/도착이 도형 경계에 정확히 맞는지 재확인
6. **파일 출력** — `.excalidraw.md` 파일 구조에 맞게 완성

### MCP 도구가 있는 경우

5단계와 6단계를 아래로 대체:
- `Excalidraw:create_view`로 미리보기 확인
- `mcp-obsidian:obsidian_patch_content`로 저장 (target: "Excalidraw Data", target_type: "heading", operation: "replace")
- Obsidian에서 실제 렌더링 확인 후 수정

### MCP 도구가 없는 경우

- 완성된 `.excalidraw.md` 파일 전체를 아티팩트로 출력
- 사용자가 Obsidian 볼트에 직접 저장

---

## 자주 발생하는 문제

| 문제 | 원인 | 해결 |
|---|---|---|
| 텍스트 두 번 렌더링 | Text Elements에 내용 있음 | 섹션 비울 것 |
| 텍스트가 좌측에 붙음 | textAlign: center 사용 | textAlign: left + x 수동 계산 |
| 텍스트 미표시 | label 속성 사용 | type: text 별도 요소로 작성 |
| 화살표 공중 부유 | 화살표 y가 도형 범위 밖 | 도형의 y~y+h 범위 안에 배치 |
| 도형 하단 여백 이상 | 높이를 임의 설정 | 내부 요소 합 + 패딩으로 역산 |
| 내부 도형이 외곽보다 넓음 | width 별도 계산 안 함 | 내부 width = 외곽 width - 패딩*2 |
