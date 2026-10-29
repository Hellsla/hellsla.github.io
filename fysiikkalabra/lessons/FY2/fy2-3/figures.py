"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-3` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, HEAT, HEAT_LIGHT, COLD, WHITE
import math
from figlib import ALUMINIUM, GOOD_LIGHT, HOT, IRON, PAPER, RULE, RULE_LIGHT, SAND, SAND_LIGHT, n
import herolib as H


def hero():
    """The chapter's opening illustration: a powerful kettle on for minutes, a small lamp on all evening, and the electricity meter between them."""
    f = H.hero("fy23-hero", "Kuvitus: keittiössä vasemmalla höyryävä vedenkeitin, jonka vieressä kello näyttää lyhyttä aikaa, ja oikealla pieni "
               "pöytävalaisin, jonka vieressä kello näyttää pitkää aikaa. Keskellä seinällä sähkömittari.")
    f.rect(0, 0, 1200, 600, PAPER)
    for k in range(1, 6): f.line(0, k * 70, 1200, k * 70, RULE_LIGHT, 2)
    f.rect(0, 400, 1200, 200, SAND_LIGHT); f.rect(0, 400, 1200, 22, SAND, INK, 2)
    # kettle
    x = 230
    f.path(f"M{x - 80},400 L{x - 64},250 Q{x},230 {x + 64},250 L{x + 80},400 Z", ALUMINIUM, INK, 3)
    f.path(f"M{x + 64},270 Q{x + 130},280 {x + 80},370", stroke=INK, w=12, extra='stroke-linecap="round"')
    f.path(f"M{x - 64},280 L{x - 110},248 L{x - 72},318 Z", ALUMINIUM, INK, 3)
    f.rect(x - 90, 392, 180, 12, INK, None, 0, 3)
    f.circle(x + 40, 370, 8, HOT)
    for k in range(3):
        f.path(f"M{x - 112 + k * 16},236 q-14,-24 0,-48 t0,-48", stroke=WHITE, w=10, extra='stroke-linecap="round"')
        f.path(f"M{x - 112 + k * 16},236 q-14,-24 0,-48 t0,-48", stroke=RULE, w=2, extra='stroke-linecap="round" stroke-opacity="0.6"')
    # lamp
    x = 960
    f.path(f"M{x - 70},400 h140 l-30,-20 h-80 Z", IRON, INK, 3)
    f.line(x, 380, x, 230, INK, 6)
    f.add(f'<path d="M{x - 160},420 L{x - 46},230 H{x + 46} L{x + 160},420 Z" fill="{HEAT_LIGHT}" fill-opacity="0.35"/>')
    f.path(f"M{x - 70},240 L{x - 40},150 H{x + 40} L{x + 70},240 Z", HEAT, INK, 3)
    f.circle(x, 238, 14, HEAT_LIGHT, INK, 2)
    # clocks: a short time (a quarter of a turn) and a long time (an almost full turn)
    for cx, t1 in ((420, 0.08), (780, 0.92)):
        f.circle(cx, 140, 56, WHITE, INK, 3)
        a = t1 * 2 * math.pi
        if t1 > 0.5:
            d = f"M{cx},140 L{cx},84 A56,56 0 1 1 {n(cx + 56 * math.sin(a))},{n(140 - 56 * math.cos(a))} Z"
        else:
            d = f"M{cx},140 L{cx},84 A56,56 0 0 1 {n(cx + 56 * math.sin(a))},{n(140 - 56 * math.cos(a))} Z"
        f.add(f'<path d="{d}" fill="{COLD}" fill-opacity="0.3"/>')
        for k in range(12):
            b = k * math.pi / 6; f.line(cx + 46 * math.sin(b), 140 - 46 * math.cos(b), cx + 52 * math.sin(b), 140 - 52 * math.cos(b), MUTED, 2)
        f.line(cx, 140, cx + 40 * math.sin(a), 140 - 40 * math.cos(a), INK, 4, cap="round"); f.circle(cx, 140, 5, INK)
    # electricity meter
    f.rect(540, 190, 120, 170, WHITE, INK, 3, 8)
    f.rect(560, 214, 80, 34, INK, None, 0, 3)
    for k in range(4): f.rect(566 + k * 18, 220, 14, 22, GOOD_LIGHT if k < 3 else HEAT_LIGHT, None, 0, 2)
    f.circle(600, 300, 26, ALUMINIUM, INK, 2); f.line(600, 300, 618, 284, HOT, 3, cap="round")
    f.path("M600,360 V400", stroke=INK, w=4)
    return f.svg()


def bars():
    f = Fig("fy23-bars", 330, "Kuvaaja mittakaavassa: vaakapylväät näyttävät, kuinka paljon energiaa laite muuntaa yhdessä sekunnissa. "
            "Vedenkeitin, jonka teho on 2000 W, muuntaa 2000 J, tosteri 1000 W 1000 J ja televisio 80 W vain 80 J. "
            "Pylvään pituus on suoraan verrannollinen tehoon.")
    f.defs_add(f'<linearGradient id="fy23-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    f.tex(300, 26, r"\text{energiaa muuntuu yhdessä sekunnissa}", "middle")
    scale = 0.2
    for i, (name, p) in enumerate((("vedenkeitin", 2000), ("tosteri", 1000), ("televisio", 80))):
        y = 90 + i * 84
        f.tex(30, y, rf"\text{{{name}}},\ P = {p}\,\text{{W}}", "start")
        f.rect(30, y + 18, p * scale, 32, "url(#fy23-heat)", INK, 2)
        f.tex(30 + p * scale + 12, y + 34, rf"{p}\,\text{{J}}", "start")
    f.line(30, 306, 570, 306, "#c9c2b2", 1.5, "6 5")
    return f.svg()


def graph():
    f = Fig("fy23-graph", 340, "Kuvaaja: energia ajan funktiona kolmelle laitteelle, jotka muuntavat energiaa tasaisesti. "
            "Vedenkeittimen 2000 W suora nousee jyrkimmin, tosterin 1000 W suora puolet loivemmin ja television 80 W suora lähes vaakasuoraan. "
            "Suoran kulmakerroin on teho: vedenkeittimen suoralla 40 kJ kuluu 20 sekunnissa. Asteikot ovat tasavälisiä ja kuvaaja on mittakaavassa.")
    ax = Axes(f, (84, 290), (470, 70), x=(0, 60), y=(0, 120), xticks=[20, 40, 60], yticks=[40, 80, 120],
              xlabel=r"t\ (\text{s})", ylabel=r"E\ (\text{kJ})")
    ax.line([(0, 0), (60, 120)], HEAT)
    ax.line([(0, 0), (60, 60)], COLD)
    ax.line([(0, 0), (60, 4.8)], MUTED)
    # slope triangle on the 2000 W line: right angle above the line
    f.line(ax.X(20), ax.Y(40), ax.X(20), ax.Y(80), MUTED, 1.5, "6 5")
    f.line(ax.X(20), ax.Y(80), ax.X(40), ax.Y(80), MUTED, 1.5, "6 5")
    ax.point(20, 40, HEAT); ax.point(40, 80, HEAT)
    f.tex(ax.X(20) - 12, ax.Y(60), r"\Delta E", "end", bg=True)
    f.tex(ax.X(30), ax.Y(80) - 22, r"\Delta t", "middle", bg=True)
    f.tex(ax.X(60) + 14, ax.Y(120), r"2000\,\text{W}", "start", HEAT)
    f.tex(ax.X(60) + 14, ax.Y(60), r"1000\,\text{W}", "start", COLD)
    f.tex(ax.X(60) - 6, ax.Y(4.8) - 26, r"80\,\text{W}", "end", MUTED)
    return f.svg()


def graph_ab():
    """A task figure: two devices' energy against time, unnamed, without powers or a slope triangle."""
    f = Fig("fy23-graph-ab", 340, "Kuvaaja: kahden laitteen A ja B muuntama sähköenergia E kilojouleina ajan t funktiona, kun laitteet "
            "muuntavat energiaa tasaisesti. Aika-akselilla on 0–80 s ruudukon välein 10 s, energia-akselilla 0–120 kJ välein 20 kJ. "
            "Suora A alkaa origosta ja kulkee ruudukon pisteiden (40 s; 60 kJ) ja (80 s; 120 kJ) kautta. Suora B alkaa origosta ja "
            "kulkee pisteiden (40 s; 20 kJ) ja (80 s; 40 kJ) kautta. Asteikot ovat tasavälisiä.")
    ax = Axes(f, (84, 290), (470, 66), x=(0, 80), y=(0, 120), xticks=[10, 20, 30, 40, 50, 60, 70, 80], yticks=[20, 40, 60, 80, 100, 120],
              xlabel=r"t\ (\text{s})", ylabel=r"E\ (\text{kJ})", xfmt=lambda v: str(v) if v % 20 == 0 else "")
    ax.line([(0, 0), (80, 120)], HEAT)
    ax.line([(0, 0), (80, 40)], COLD)
    f.tex(ax.X(80) + 14, ax.Y(120), r"\text{A}", "start", HEAT, w=30)
    f.tex(ax.X(80) + 14, ax.Y(40), r"\text{B}", "start", COLD, w=30)
    return f.svg()


FIGURES = {"hero": hero, "bars": bars, "graph": graph, "graph-ab": graph_ab}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "graph": "reveals: the power of each line printed beside it and the slope triangle 40 kJ in 20 s",
    "graph-ab": "safe: two lines through the origin on 10 s and 20 kJ gridlines, no powers, no slope triangle (other data than graph)",
}
