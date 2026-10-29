"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-3` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, HEAT, HEAT_LIGHT, COLD, WHITE


def bars():
    f = Fig("fy23-bars", 330, "Kuvaaja mittakaavassa: vaakapylväät näyttävät, kuinka paljon energiaa laite muuntaa yhdessä sekunnissa. "
            "Vedenkeitin, jonka teho on 2000 W, muuntaa 2000 J, tosteri 1000 W 1000 J ja televisio 100 W vain 100 J. "
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


FIGURES = {"bars": bars, "graph": graph, "graph-ab": graph_ab}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "graph": "reveals: the power of each line printed beside it and the slope triangle 40 kJ in 20 s",
    "graph-ab": "safe: two lines through the origin on 10 s and 20 kJ gridlines, no powers, no slope triangle (other data than graph)",
}
