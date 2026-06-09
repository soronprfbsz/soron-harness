# HTML 보일러플레이트

## 핵심 구조

- 슬라이드는 `position: fixed; inset: 0`으로 뷰포트 전체를 채움
- `justify-content: center` + `align-items: center`로 콘텐츠 수직+가로 중앙
- `.slide > * { max-width: 1100px }`로 콘텐츠 폭 제한 (가로로 퍼지는 것 방지)
- 패딩/폰트는 `vh`, `vw`, `clamp()` 단위로 모든 화면에 비례
- 전체화면 시 `body.fs` 클래스 추가 → 네비바 자동 숨김
- **상단 프로그레스바** — 화면 최상단 3px 두께. 슬라이드 진행에 따라 좌→우로 채워짐. 모든 모드에서 표시

## 전체 코드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>프레젠테이션 제목</title>
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root {
  --bg:#0a0a0a; --card:#1a1a1a;
  --orange:#ff6b35; --green:#00d084; --purple:#a855f7; --blue:#3b82f6;
  --good-bg:#0d2a15; --good-bd:#166534; --good-tx:#4ade80;
  --bad-bg:#2a0f0f; --bad-bd:#7f1d1d; --bad-tx:#f87171;
  --t1:#fff; --t2:#aaa; --t3:#666; --bd:#2a2a2a;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Pretendard',-apple-system,sans-serif;background:var(--bg);color:var(--t1);overflow:hidden;height:100vh}

/* ★ 슬라이드: 뷰포트 전체 + 수직/가로 중앙 + 폭 제한 */
.slide{position:fixed;inset:0;display:none;flex-direction:column;justify-content:center;align-items:center;padding:6vh 7vw;background:var(--bg)}
.slide.active{display:flex;animation:fi .3s ease}
.slide>*{width:100%;max-width:1100px}
.slide.cover{justify-content:center}
.pg{width:auto!important;max-width:none!important}
@keyframes fi{from{opacity:0}to{opacity:1}}

/* 타이포: clamp 반응형 (세로로 넉넉하게) */
.lbl{color:var(--orange);font-size:clamp(14px,1.3vw,22px);font-weight:500;letter-spacing:3px;text-transform:uppercase;margin-bottom:2.5vh}
.ttl{font-size:clamp(40px,4.5vw,84px);font-weight:800;line-height:1.2}
.desc{font-size:clamp(18px,1.6vw,30px);color:var(--t2);margin-top:3.5vh;line-height:1.6}
.ho{color:var(--orange)}.hg{color:var(--green)}.hp{color:var(--purple)}

.badge{width:clamp(36px,3.2vw,58px);height:clamp(36px,3.2vw,58px);border-radius:50%;background:var(--orange);color:#fff;font-weight:700;font-size:clamp(16px,1.5vw,26px);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.badge.sm{width:clamp(32px,2.8vw,50px);height:clamp(32px,2.8vw,50px);font-size:clamp(14px,1.3vw,22px)}
.ct{font-size:clamp(30px,3.3vw,62px);font-weight:800;line-height:1.25;margin:2vh 0 4vh}

.li{display:flex;align-items:center;gap:clamp(14px,1.4vw,28px);margin-bottom:clamp(18px,2.8vh,40px)}
.li p{font-size:clamp(18px,1.55vw,30px);line-height:1.55}
.li strong{color:var(--orange)}

.pg{position:absolute;bottom:3vh;right:4vw;color:var(--t3);font-size:clamp(12px,1vw,18px)}

/* 네비바 */
.nav{position:fixed;bottom:0;left:0;right:0;height:56px;background:rgba(10,10,10,.95);border-top:1px solid var(--bd);display:flex;align-items:center;justify-content:center;gap:24px;z-index:200;transition:opacity .3s}
.nb{background:0 0;border:1px solid var(--bd);color:var(--t1);padding:8px 20px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:14px}
.nb:hover{background:var(--card);border-color:var(--orange)}
.cnt{color:var(--t2);font-size:14px;min-width:80px;text-align:center}
body.fs .nav{opacity:0;pointer-events:none} /* ★ 전체화면 시 네비바 숨김 */

/* ★ 상단 프로그레스바 — 발표 진행률 (전체화면에서도 유지) */
.prog{position:fixed;top:0;left:0;right:0;height:3px;background:rgba(255,255,255,.05);z-index:150}
.prog-fill{height:100%;background:var(--orange);transition:width .3s ease;width:0}

/* ★ 장점/한계 색상 코드 (불릿 리스트) */
.hr{color:var(--bad-tx)}                              /* 라벨용 빨강 */
.fp li.good::before{color:var(--good-tx)}             /* 장점 불릿 = 초록 */
.fp li.bad::before{color:var(--bad-tx)}               /* 한계 불릿 = 빨강 */
.card.good .fp li::before{color:var(--good-tx)}       /* 비교 카드 내부 불릿 자동 동기화 */
.card.bad .fp li::before{color:var(--bad-tx)}

/* === 여기에 컴포넌트 CSS 추가 (components.md 참조) === */
</style>
</head>
<body>

<!-- 표지 (cover 클래스) -->
<div class="slide cover active">
  <div class="lbl">시리즈명</div>
  <h1 class="ttl">메인 <span class="ho">제목</span></h1>
  <p class="desc">설명 텍스트</p>
  <span class="pg">1</span>
</div>

<!-- 콘텐츠 슬라이드 (상단 배지는 기본 미사용 — "번호 뱃지 리스트" 컴포넌트에서만) -->
<div class="slide">
  <h2 class="ct">타이틀 <span class="ho">강조</span> 나머지</h2>
  <!-- 컴포넌트 HTML -->
  <span class="pg">2</span>
</div>

<!-- 상단 프로그레스바 (모든 슬라이드 공통) -->
<div class="prog"><div class="prog-fill" id="pf"></div></div>

<!-- 네비바 -->
<div class="nav">
  <button class="nb" onclick="go(cur-1)">← 이전</button>
  <span class="cnt" id="c">1 / 1</span>
  <button class="nb" onclick="go(cur+1)">다음 →</button>
  <button class="nb" onclick="tf()">전체화면 [F]</button>
</div>

<script>
let cur=0;const S=document.querySelectorAll('.slide');
function uc(){
  document.getElementById('c').textContent=`${cur+1} / ${S.length}`;
  document.getElementById('pf').style.width=`${(cur+1)/S.length*100}%`;
}
function go(n){S[cur].classList.remove('active');cur=((n%S.length)+S.length)%S.length;S[cur].classList.add('active');uc()}
function tf(){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
document.addEventListener('fullscreenchange',()=>{document.body.classList.toggle('fs',!!document.fullscreenElement)});
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();go(cur+1)}if(e.key==='ArrowLeft')go(cur-1);if(e.key==='f'||e.key==='F')tf()});
uc();
</script>
</body>
</html>
```
