# 슬라이드 컴포넌트 레퍼런스

각 컴포넌트의 상세 HTML 구조와 CSS 코드. 모든 크기는 clamp()로 반응형.

## 목차

1. [표지 슬라이드](#1-표지-슬라이드)
2. [번호 뱃지 리스트](#2-번호-뱃지-리스트)
3. [테이블](#3-테이블)
4. [카드 그리드](#4-카드-그리드)
5. [비교 카드 (Good vs Bad)](#5-비교-카드)
6. [상황 A/B 카드](#6-상황-ab-카드)
7. [피처 카드](#7-피처-카드)
8. [플랜 비교 테이블](#8-플랜-비교-테이블)

---

## 1. 표지 슬라이드

표지에는 번호 뱃지 없음. 표지 제목만 4.5vw, 나머지 콘텐츠 슬라이드는 3.3vw.

```html
<div class="slide cover active">
  <div class="lbl">CLAUDE CODE · 시리즈명 · 2026</div>
  <h1 class="ttl">메인 타이틀<br><span class="ho">강조 키워드</span></h1>
  <p class="desc">설명 텍스트를 여기에</p>
  <span class="pg">1</span>
</div>
```

```css
.lbl { color: var(--orange); font-size: clamp(14px,1.3vw,22px); font-weight: 500; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 2.5vh; }
.ttl { font-size: clamp(40px,4.5vw,84px); font-weight: 800; line-height: 1.2; }
.desc { font-size: clamp(18px,1.6vw,30px); color: var(--t2); margin-top: 3.5vh; line-height: 1.6; }
.ho { color: var(--orange); } .hg { color: var(--green); } .hp { color: var(--purple); }
```

---

## 2. 번호 뱃지 리스트

핵심 개념을 번호 순으로 설명할 때 사용.

```html
<div class="slide">
  <div class="badge">1</div>
  <h2 class="ct">타이틀 <span class="ho">강조</span> 나머지</h2>
  <div class="li"><div class="badge sm">1</div><p>내용 텍스트 <strong>강조 키워드</strong></p></div>
  <div class="li"><div class="badge sm">2</div><p>내용 텍스트 <strong>강조 키워드</strong></p></div>
  <span class="pg">2</span>
</div>
```

```css
.badge { width: clamp(36px,3.2vw,58px); height: clamp(36px,3.2vw,58px); border-radius: 50%; background: var(--orange); color: #fff; font-weight: 700; font-size: clamp(16px,1.5vw,26px); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.badge.sm { width: clamp(32px,2.8vw,50px); height: clamp(32px,2.8vw,50px); font-size: clamp(14px,1.3vw,22px); }
.ct { font-size: clamp(30px,3.3vw,62px); font-weight: 800; line-height: 1.25; margin: 2vh 0 4vh; }

.li { display: flex; align-items: center; gap: clamp(14px,1.4vw,28px); margin-bottom: clamp(18px,2.8vh,40px); }
.li p { font-size: clamp(18px,1.55vw,30px); line-height: 1.55; }
.li strong { color: var(--orange); }
```

---

## 3. 테이블

데이터/현황을 표로 정리. 태그 뱃지 포함 가능.

```html
<table>
  <thead><tr><th>컬럼1</th><th>컬럼2</th></tr></thead>
  <tbody>
    <tr><td><span class="tag tg">초급</span></td><td>내용</td></tr>
  </tbody>
</table>
```

```css
table { width: 100%; border-collapse: collapse; }
th { background: var(--card); color: var(--t2); font-weight: 500; padding: clamp(12px,1.5vh,22px) clamp(14px,1.4vw,28px); text-align: left; border-bottom: 1px solid var(--bd); font-size: clamp(14px,1.15vw,20px); }
td { padding: clamp(14px,1.7vh,24px) clamp(14px,1.4vw,28px); border-bottom: 1px solid var(--bd); font-size: clamp(16px,1.25vw,24px); }

.tag { padding: 4px 12px; border-radius: 7px; font-size: clamp(11px,.9vw,16px); font-weight: 600; white-space: nowrap; }
.tg { background: rgba(0,208,132,.15); color: var(--green); border: 1px solid rgba(0,208,132,.3); }
.to { background: rgba(255,107,53,.15); color: var(--orange); border: 1px solid rgba(255,107,53,.3); }
.tp { background: rgba(168,85,247,.15); color: var(--purple); border: 1px solid rgba(168,85,247,.3); }
.tx { background: rgba(255,255,255,.05); color: var(--t2); border: 1px solid var(--bd); }
```

---

## 4. 카드 그리드

여러 항목을 2열 또는 3열로 나열.

```html
<div class="cards" style="display:grid;grid-template-columns:repeat(3,1fr);gap:2vw">
  <div class="card"><h3>제목</h3><p>설명</p></div>
</div>
```

```css
.card { background: var(--card); border: 1px solid var(--bd); border-radius: 14px; padding: clamp(22px,2.5vw,44px); }
```

---

## 5. 비교 카드

좌우 카드로 비효율/효율, 좋은 예/나쁜 예를 비교.

**절대 규칙:** 좌우 카드 flex:1 동일 너비, 카드 간 gap 2vw, 내부 패딩 동일.

```html
<div class="clbl"><span class="bad">✗ 비효율</span><span class="good">✓ 효율</span></div>
<div class="cards">
  <div class="card bad">
    <p class="cex">"나쁜 예시 텍스트"</p>
    <p class="cdesc">→ 설명. <strong>강조 키워드</strong></p>
  </div>
  <div class="card good">
    <p class="cex">"좋은 예시 텍스트"</p>
    <p class="cdesc">→ 설명. <strong>강조 키워드</strong></p>
  </div>
</div>
<p class="csum">요약 텍스트 <strong>강조</strong></p>
```

```css
.clbl { display: flex; gap: 2vw; margin-bottom: 1.8vh; }
.clbl span { flex: 1; font-size: clamp(14px,1.15vw,20px); font-weight: 600; }
.clbl .bad { color: var(--bad-tx); } .clbl .good { color: var(--good-tx); }

.cards { display: flex; gap: 2vw; }
.card { flex: 1; padding: clamp(22px,2.5vw,44px); border-radius: 14px; }
.card.bad { background: var(--bad-bg); border: 1px solid var(--bad-bd); }
.card.good { background: var(--good-bg); border: 1px solid var(--good-bd); }

.cex { font-size: clamp(16px,1.35vw,26px); margin-bottom: 2vh; font-family: Consolas, monospace; }
.cdesc { font-size: clamp(15px,1.25vw,24px); color: var(--t2); line-height: 1.6; }
.cdesc strong { color: var(--orange); font-weight: 700; }
.csum { margin-top: 3.5vh; font-size: clamp(17px,1.45vw,28px); color: var(--t2); line-height: 1.6; }
.csum strong { color: var(--t1); }
```

---

## 6. 상황 A/B 카드

상황별 안내. 좌측=초록(긍정), 우측=빨강(주의).

```html
<div class="cards">
  <div class="card good">
    <span class="slbl good">상황 A</span>
    <p class="sdesc">상황 설명 텍스트</p>
    <p class="scon good">결론/조언 텍스트</p>
  </div>
  <div class="card bad">
    <span class="slbl bad">상황 B</span>
    <p class="sdesc">상황 설명 텍스트</p>
    <p class="scon bad">결론/조언 텍스트</p>
  </div>
</div>
```

```css
.slbl { font-size: clamp(14px,1.15vw,20px); font-weight: 700; display: block; margin-bottom: 2vh; }
.slbl.good { color: var(--good-tx); } .slbl.bad { color: var(--bad-tx); }
.sdesc { font-size: clamp(16px,1.3vw,24px); color: var(--t2); margin-bottom: 2.5vh; line-height: 1.6; }
.scon { font-size: clamp(16px,1.3vw,24px); font-weight: 700; }
.scon.good { color: var(--good-tx); } .scon.bad { color: var(--bad-tx); }
```

---

## 7. 피처 카드

설명 + 회색 예시 박스 + 보충 포인트 구조.

```html
<p class="fdesc">설명 텍스트를 여기에 작성</p>
<div class="ebox">
  <p><span class="k"># 헤딩</span> <span class="c">← 주석</span></p>
  <p>코드/예시 내용</p>
</div>
<ul class="fp">
  <li>포인트 1 <strong>강조</strong></li>
  <li>포인트 2 <strong class="ho">accent 강조</strong></li>
</ul>
```

```css
.fdesc { font-size: clamp(17px,1.45vw,28px); color: var(--t2); margin-bottom: 3vh; line-height: 1.6; }
.ebox { background: var(--card); border: 1px solid var(--bd); border-radius: 10px; padding: clamp(20px,2.2vw,38px); margin-bottom: 3vh; font-family: Consolas, 'Courier New', monospace; }
.ebox p { font-size: clamp(15px,1.2vw,22px); color: var(--t2); line-height: 1.9; }
.ebox .k { color: var(--orange); } .ebox .c { color: var(--t3); }

.fp { list-style: none; padding: 0; }
.fp li { font-size: clamp(17px,1.45vw,28px); padding: clamp(8px,1.2vh,16px) 0 clamp(8px,1.2vh,16px) clamp(18px,1.6vw,32px); position: relative; line-height: 1.55; }
.fp li::before { content: '•'; color: var(--orange); font-weight: 700; position: absolute; left: 0; }
```

---

## 8. 플랜 비교 테이블

여러 플랜/옵션을 표로 비교. 셀별 색상 강조 지원. 3번 테이블 CSS를 그대로 사용하되 추가 클래스:

```css
.accent { color: var(--orange); font-weight: 600; }
.danger { color: var(--bad-tx); font-weight: 600; }
.success { color: var(--good-tx); font-weight: 600; }
.strategy { font-weight: 700; }
```
