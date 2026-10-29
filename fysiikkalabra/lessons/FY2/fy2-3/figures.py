"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-3` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, HEAT, HEAT_LIGHT, COLD, WHITE
import math
from figlib import ALUMINIUM, GOOD_LIGHT, HOT, IRON, PAPER, RULE, RULE_LIGHT, SAND, SAND_LIGHT, n
import herolib as H
from figlib import HOT_LIGHT, METAL_EDGE
from herolib import grad, steel


def hero():
    """The chapter's opening illustration: a powerful kettle on for minutes, a small lamp on all evening, and the electricity meter between them."""
    f = H.hero("fy23-hero", "Kuvitus: keittiössä vasemmalla höyryävä vedenkeitin, jonka yllä kello näyttää lyhyttä aikaa, ja oikealla pieni "
               "pöytävalaisin, jonka yllä kello näyttää pitkää aikaa. Keskellä seinällä sähkömittari, josta johto kulkee laitteille.")
    H.tiles(f, 400)
    f.rect(0, 400, 1200, 26, RULE, INK, 3); f.rect(0, 426, 1200, 174, RULE_LIGHT)
    for x in (300, 600, 900): f.line(x, 426, x, 600, INK, 2)
    for x in (270, 330, 570, 630, 870, 930): f.rect(x - 4, 450, 8, 44, METAL_EDGE, rx=4)
    # wall cable from the meter to the two devices
    f.path("M600,330 V370 H300 V400 M600,370 H930 V400", stroke=INK, w=4, extra='stroke-linejoin="round"')
    # kettle: steel body, black handle and base, glowing switch, steam
    x = 240
    f.add(f'<ellipse cx="{x}" cy="400" rx="110" ry="10" fill="{INK}" fill-opacity="0.2"/>')
    f.rect(x - 100, 384, 200, 16, INK, None, 0, 4)
    f.path(f"M{x - 86},384 L{x - 70},210 Q{x},188 {x + 70},210 L{x + 86},384 Z", steel(f, "fy23h-kettle"), INK, 3)
    f.path(f"M{x + 70},226 Q{x + 150},236 {x + 92},360", stroke=INK, w=16, extra='stroke-linecap="round"')
    f.path(f"M{x - 70},240 L{x - 124},206 L{x - 80},288 Z", steel(f, "fy23h-spout"), INK, 3)
    f.path(f"M{x - 60},196 Q{x},176 {x + 60},196 L{x + 50},206 Q{x},192 {x - 50},206 Z", INK)
    f.rect(x + 56, 330, 22, 14, HOT, INK, 2, 4); f.circle(x + 67, 337, 12, H.glow(f, "fy23h-led", HOT_LIGHT, HOT))
    for k in range(3):
        d = f"M{x - 126 + k * 14},196 c-14,-24 14,-40 0,-64 s14,-40 0,-64"
        f.path(d, stroke=RULE, w=20, extra='stroke-linecap="round" stroke-opacity="0.5"'); f.path(d, stroke=WHITE, w=14, extra='stroke-linecap="round"')
    # table lamp with its warm cone of light
    x = 940
    f.add(f'<path d="M{x - 70},248 L{x - 200},426 H{x + 200} L{x + 70},248 Z" fill="{HEAT_LIGHT}" fill-opacity="0.3"/>')
    f.path(f"M{x - 80},400 h160 l-30,-24 h-100 Z", grad(f, "fy23h-base", IRON, INK), INK, 3)
    f.line(x, 380, x, 250, INK, 7)
    f.path(f"M{x - 86},252 L{x - 50},150 H{x + 50} L{x + 86},252 Z", grad(f, "fy23h-shade", HEAT_LIGHT, HEAT), INK, 3)
    f.circle(x, 250, 16, H.glow(f, "fy23h-bulb", WHITE, HEAT_LIGHT))
    # clocks: a short time and a long time, the elapsed part shaded
    for cx, t1 in ((420, 0.08), (780, 0.92)):
        f.circle(cx, 150, 64, WHITE, INK, 4)
        a = t1 * 2 * math.pi
        d = f"M{cx},150 L{cx},92 A58,58 0 {1 if t1 > 0.5 else 0} 1 {n(cx + 58 * math.sin(a))},{n(150 - 58 * math.cos(a))} Z"
        f.add(f'<path d="{d}" fill="{COLD}" fill-opacity="0.3"/>')
        for k in range(12):
            b = k * math.pi / 6; f.line(cx + 50 * math.sin(b), 150 - 50 * math.cos(b), cx + 58 * math.sin(b), 150 - 58 * math.cos(b), INK if k % 3 == 0 else MUTED, 3 if k % 3 == 0 else 2)
        f.line(cx, 150, cx + 44 * math.sin(a), 150 - 44 * math.cos(a), INK, 5, cap="round"); f.circle(cx, 150, 6, INK)
    # electricity meter with its counter and spinning disc
    f.rect(530, 170, 140, 160, grad(f, "fy23h-meter", WHITE, ALUMINIUM), INK, 3, 10)
    f.rect(550, 192, 100, 36, INK, None, 0, 4)
    for k in range(5): f.rect(556 + k * 18, 198, 14, 24, GOOD_LIGHT if k < 4 else HEAT_LIGHT, None, 0, 2)
    f.add(f'<ellipse cx="600" cy="276" rx="44" ry="12" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2"/>')
    f.rect(592, 266, 16, 20, HOT, None, 0, 2)
    f.rect(560, 304, 80, 12, IRON, INK, 1.5, 3)
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
