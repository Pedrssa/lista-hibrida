"""Tema celestial claro: tokens, partículas CSS e animações acessíveis.

Sem JavaScript, bibliotecas extras ou alterações na lógica dos algoritmos.
"""
import streamlit as st

TOKENS = {
    "white": "#FFFFFF",
    "canvas": "#FAFAF8",
    "ivory": "#F5F2EA",
    "ink": "#172438",
    "ink_soft": "#465365",
    "gold": "#917142",
    "bronze": "#70542E",
    "line": "#D9DDE3",
    "celestial": "#314B69",
}

STYLES = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root {
  --white:#FFFFFF; --paper:#FAFAF8; --ivory:#F5F2EA;
  --ink:#172438; --muted:#465365; --gold:#917142; --bronze:#70542E;
  --line:#D9DDE3; --celestial:#314B69;
  --display:'Cormorant Garamond',Georgia,serif;
  --body:'Inter',system-ui,sans-serif;
  --mono:'IBM Plex Mono',monospace;
  --ease:cubic-bezier(.22,.68,0,1);
}
html { color-scheme:light!important; }
body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
  background:var(--paper)!important; color:var(--ink)!important;
  font-family:var(--body)!important;
}
.stApp { isolation:isolate; }
[data-testid="stHeader"] { background:rgba(250,250,248,.83)!important; }
[data-testid="stMainBlockContainer"] {
  max-width:1240px; padding-top:2rem; padding-bottom:5rem;
  position:relative; z-index:2;
}
[data-testid="stSidebar"], [data-testid="stSidebarContent"] {
  background:#FFFFFF!important; color:var(--ink)!important;
  border-right:1px solid var(--line);
}
[data-testid="stSidebar"] * { color:var(--ink); }
h1,h2,h3 { font-family:var(--display)!important; font-weight:600!important; color:var(--ink)!important; }
h1 { font-size:clamp(2.6rem,5.2vw,4.9rem)!important; letter-spacing:-.03em!important; line-height:1.07!important; }
h2 { font-size:clamp(1.8rem,3vw,2.8rem)!important; }
h3 { font-size:clamp(1.55rem,2.5vw,2.1rem)!important; }
p,li,label,[data-testid="stMarkdownContainer"] { color:var(--ink)!important; }
small,[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] p { color:var(--muted)!important; }
a { color:var(--celestial)!important; text-underline-offset:3px; }
:focus-visible { outline:3px solid var(--celestial)!important; outline-offset:2px!important; }
[data-testid="stMetric"] {
  padding:1.2rem 1.3rem!important; border:1px solid var(--line)!important;
  border-radius:13px; background:#FFFFFF!important;
  min-height:125px; box-shadow:0 8px 28px rgba(23,36,56,.045);
  animation:atlas-rise .55s var(--ease) both;
  transition:transform .24s var(--ease), box-shadow .24s var(--ease),border-color .24s var(--ease);
}
[data-testid="stMetric"]:hover { transform:translateY(-4px); box-shadow:0 17px 36px rgba(23,36,56,.10); border-color:#B3C1D0!important; }
[data-testid="stMetricLabel"] p {
  color:var(--muted)!important; font-size:.77rem!important;
  text-transform:uppercase; letter-spacing:.1em;
}
[data-testid="stMetricValue"] {
  color:var(--ink)!important; font-family:var(--mono)!important;
  font-size:clamp(1.25rem,2vw,2rem)!important; font-variant-numeric:tabular-nums;
}
.stTabs [data-baseweb="tab-list"] {
  gap:.35rem; border-bottom:1px solid var(--line)!important;
  overflow-x:auto; background:transparent!important;
}
.stTabs [data-baseweb="tab"] {
  background:transparent!important; color:var(--muted)!important; font-size:.9rem;
  padding:0 1rem; min-height:51px;
}
.stTabs [aria-selected="true"] { color:var(--ink)!important; font-weight:700; }
.stTabs [data-baseweb="tab-highlight"] { background:var(--celestial)!important; height:3px; }
[data-testid="stForm"] {
  border:1px solid var(--line)!important; background:#FFFFFF!important;
  border-radius:14px!important; padding:1.35rem!important;
  box-shadow:0 10px 30px rgba(23,36,56,.045);
}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="select"] {
  background:#FFFFFF!important; border:1px solid #B9C4CF!important;
  border-radius:9px!important; color:var(--ink)!important;
}
input,textarea { color:var(--ink)!important; font-family:var(--mono)!important; }
input:focus,textarea:focus { box-shadow:0 0 0 2px var(--celestial)!important; }
.stButton button,[data-testid="stFormSubmitButton"] button {
  border:1px solid var(--celestial)!important; border-radius:9px!important;
  color:var(--celestial)!important; background:#FFFFFF!important;
  font-family:var(--body)!important; font-weight:600;
  min-height:43px; transition:transform .18s var(--ease),background .18s var(--ease),box-shadow .18s var(--ease);
}
.stButton button:hover,[data-testid="stFormSubmitButton"] button:hover {
  background:#EDF2F7!important; box-shadow:0 7px 16px rgba(23,36,56,.10);
  transform:translateY(-2px);
}
.stButton button:active,[data-testid="stFormSubmitButton"] button:active { transform:translateY(0); }
.stButton button:disabled { opacity:.55; cursor:not-allowed; }
button[kind="primary"],[data-testid="stFormSubmitButton"] button[kind="primary"] {
  color:#FFFFFF!important; background:var(--ink)!important; border-color:var(--ink)!important;
}
button[kind="primary"]:hover { background:var(--celestial)!important; }
[data-testid="stAlert"] { border-radius:10px!important; }
[data-testid="stDataFrame"],[data-testid="stExpander"] { border:1px solid var(--line)!important; border-radius:10px!important; }
[data-testid="stProgress"] [role="progressbar"] > div { background:var(--celestial)!important; }
[data-testid="stCodeBlock"],code,pre { font-family:var(--mono)!important; }
[data-testid="stCodeBlock"] { border:1px solid var(--line); border-radius:10px; }
/* A decoração pertence ao fundo: não intercepta cliques ou navegação. */
.cosmos-field {
  position:fixed; inset:0; z-index:0; overflow:hidden;
  pointer-events:none; opacity:.8;
  background-image:
    radial-gradient(circle at 15% 25%, rgba(49,75,105,.055) 0 1px,transparent 2px),
    radial-gradient(circle at 78% 48%, rgba(145,113,66,.09) 0 1px,transparent 2px),
    linear-gradient(rgba(49,75,105,.025) 1px,transparent 1px),
    linear-gradient(90deg,rgba(49,75,105,.025) 1px,transparent 1px);
  background-size:140px 170px, 210px 190px, 48px 48px, 48px 48px;
}
.cosmos-particle {
  position:absolute; width:var(--size); height:var(--size);
  top:var(--top); left:var(--left); opacity:.15;
  border-radius:50%; background:var(--celestial);
  box-shadow:0 0 0 3px rgba(49,75,105,.10);
  animation:particle-float var(--duration) ease-in-out var(--delay) infinite alternate,
            particle-pulse 4s ease-in-out var(--delay) infinite;
  will-change:transform,opacity;
}
.cosmos-particle:nth-child(3n) { background:var(--gold); box-shadow:0 0 0 3px rgba(145,113,66,.09); }
.atlas-hero {
  position:relative; overflow:hidden; isolation:isolate;
  padding:clamp(1.5rem,3vw,2.8rem) clamp(1.4rem,4vw,3.3rem);
  background:linear-gradient(110deg,#FFFFFF 0%,#FFFFFF 57%,#EEF2F5 100%);
  border:1px solid #C9D2DA; border-radius:17px;
  box-shadow:0 18px 58px rgba(23,36,56,.075);
  margin:0 0 1.7rem; animation:atlas-rise .75s var(--ease) both;
}
.atlas-hero::before {
  content:""; position:absolute; inset:9px; z-index:-1; pointer-events:none;
  border:1px solid rgba(49,75,105,.12); border-radius:10px;
}
.atlas-hero::after {
  content:""; position:absolute; width:390px; height:390px; top:-168px; right:-75px;
  z-index:-1; pointer-events:none; border-radius:50%;
  border:1.5px solid rgba(49,75,105,.35);
  box-shadow:0 0 0 39px rgba(49,75,105,.035),0 0 0 86px rgba(49,75,105,.03),0 0 0 136px rgba(145,113,66,.025);
  animation:orbit-breathe 8s ease-in-out infinite alternate;
}
.atlas-kicker { color:var(--celestial)!important; font:600 .74rem var(--mono); letter-spacing:.17em; text-transform:uppercase; }
.atlas-hero h1 { margin:.65rem 0 .8rem; max-width:710px; }
.atlas-hero p { max-width:625px; color:var(--muted)!important; line-height:1.75; }
.atlas-mark { color:var(--bronze); font:500 .72rem var(--mono); letter-spacing:.12em; }
.atlas-rule { height:1px; margin:1.2rem 0; background:linear-gradient(90deg,var(--celestial),rgba(49,75,105,.06)); transform-origin:left; animation:rule-reveal 1s .25s var(--ease) both; }
.atlas-section { color:var(--celestial); font:600 .73rem var(--mono); letter-spacing:.14em; text-transform:uppercase; margin:1.2rem 0 .85rem; }
.atlas-grid { display:grid; grid-template-columns:repeat(10,minmax(0,1fr)); gap:.5rem; margin:1rem 0; }
.atlas-slot {
  min-height:49px; display:grid; place-items:center;
  border:1px dashed #C5CFD9; border-radius:8px; background:#FFFFFF;
  color:var(--muted); font:500 .79rem var(--mono);
  transition:transform .25s var(--ease),background .25s var(--ease),border-color .25s var(--ease);
}
.atlas-slot.filled { border:1px solid var(--celestial); background:#E9F0F5; color:var(--ink); animation:slot-arrive .4s var(--ease) both; }
.atlas-slot.filled:hover { transform:translateY(-3px); }
.atlas-footer { color:var(--muted); border-top:1px solid var(--line); margin-top:2.5rem; padding-top:1rem; font:400 .7rem var(--mono); letter-spacing:.06em; }
@keyframes atlas-rise { from{opacity:0; transform:translateY(21px)} to{opacity:1;transform:translateY(0)} }
@keyframes particle-float { from{transform:translate3d(0,13px,0)} to{transform:translate3d(24px,-27px,0)} }
@keyframes particle-pulse { 0%,100%{opacity:.10} 50%{opacity:.54} }
@keyframes orbit-breathe { from{transform:rotate(-9deg) scale(.96);opacity:.55} to{transform:rotate(9deg) scale(1.07);opacity:1} }
@keyframes rule-reveal { from{transform:scaleX(0)} to{transform:scaleX(1)} }
@keyframes slot-arrive { from{opacity:.4;transform:translateY(10px) scale(.93)} to{opacity:1;transform:translateY(0) scale(1)} }
@media(max-width:800px) {
  [data-testid="stMainBlockContainer"] { padding:1.2rem .85rem 3rem; }
  .atlas-grid { grid-template-columns:repeat(5,minmax(0,1fr)); }
  .atlas-hero { padding:1.6rem 1.2rem; }
  .atlas-hero::after { right:-180px; width:320px; height:320px; }
  .stTabs [data-baseweb="tab"] { padding:0 .65rem; }
  [data-testid="stMetric"] { min-height:100px; padding:.8rem!important; }
}
@media(prefers-reduced-motion:reduce) {
  *, *::before, *::after {
    animation:none!important; transition:none!important;
    scroll-behavior:auto!important; will-change:auto!important;
  }
}
</style>
"""

def aplicar_tema() -> None:
    """Renderiza CSS e 24 partículas visuais não interativas."""
    st.markdown(STYLES, unsafe_allow_html=True)
    particles = []
    for i in range(24):
        left = (i * 37 + 11) % 97
        top = (i * 43 + 17) % 95
        size = 3 + i % 4
        duration = 5 + (i % 6)
        delay = -(i % 8)
        particles.append(
            f'<i class="cosmos-particle" aria-hidden="true" '
            f'style="--left:{left}%;--top:{top}%;--size:{size}px;'
            f'--duration:{duration}s;--delay:{delay}s"></i>'
        )
    st.markdown(
        '<div class="cosmos-field" aria-hidden="true">'
        + "".join(particles)
        + "</div>",
        unsafe_allow_html=True,
    )
