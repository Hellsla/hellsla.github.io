"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-7` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT, GRAIN,
                    ALUMINIUM, METAL_EDGE, IRON, HEAT, n)

# densities in g/cm3 (the lesson's table) and the cube of 10 cm3 (edge about 2,15 cm)
RHO = {"mänty": 0.50, "alumiini": 2.70, "rauta": 7.87}


def cubes():
    f = Fig("fy17-cubes", 372, "Kaavakuva: kolme yhtä suurta kuutiota, joiden tilavuus on kullakin 10 cm³, ovat mäntyä, alumiinia ja "
            "rautaa. Kuutiot ovat samankokoiset, mutta niiden massat ovat 5,0 g, 27 g ja 79 g. Massaa kuvaavien "
            "vaakapylväiden pituudet ovat mittakaavassa: rautakuution pylväs on yli kymmenen kertaa mäntykuution "
            "pylvään pituinen.")
    f.defs_add(f'<pattern id="fy17-grain" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.3" fill="{GRAIN}"/><circle cx="10" cy="8" r="1" fill="{GRAIN}"/></pattern>')
    f.defs_add(f'<linearGradient id="fy17-pine" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    f.tex(300, 20, r"\text{sama tilavuus } V = 10\,\text{cm}^3", "middle", w=400)
    per = 150 / 78.7                      # bar length per gram: iron 78,7 g -> 150 units
    for cx, name, fill in ((110, "mänty", "url(#fy17-pine)"), (300, "alumiini", ALUMINIUM), (490, "rauta", IRON)):
        m = RHO[name] * 10
        s, d = 84, 22                     # front face 84 units, depth 22
        x0, y0 = cx - s / 2 - d / 2, 100
        # right side and top face first, then the front face
        f.path(f"M{n(x0 + s)},{n(y0)} L{n(x0 + s + d)},{n(y0 - d)} V{n(y0 - d + s)} L{n(x0 + s)},{n(y0 + s)} Z", fill)
        f.path(f"M{n(x0 + s)},{n(y0)} L{n(x0 + s + d)},{n(y0 - d)} V{n(y0 - d + s)} L{n(x0 + s)},{n(y0 + s)} Z", INK, extra='fill-opacity="0.2"')
        f.path(f"M{n(x0)},{n(y0)} L{n(x0 + d)},{n(y0 - d)} H{n(x0 + s + d)} L{n(x0 + s)},{n(y0)} Z", fill)
        f.path(f"M{n(x0)},{n(y0)} L{n(x0 + d)},{n(y0 - d)} H{n(x0 + s + d)} L{n(x0 + s)},{n(y0)} Z", WHITE, extra='fill-opacity="0.4"')
        f.rect(x0, y0, s, s, fill)
        if name == "mänty":
            f.rect(x0, y0, s, s, "url(#fy17-grain)", extra='fill-opacity="0.6"')
        f.path(f"M{n(x0)},{n(y0)} L{n(x0 + d)},{n(y0 - d)} H{n(x0 + s + d)} V{n(y0 - d + s)} L{n(x0 + s)},{n(y0 + s)} H{n(x0)} Z", stroke=INK, w=2.5)
        f.path(f"M{n(x0)},{n(y0)} H{n(x0 + s)} L{n(x0 + s + d)},{n(y0 - d)} M{n(x0 + s)},{n(y0)} V{n(y0 + s)}", stroke=INK, w=2.5)
        f.tex(cx, 238, r"\text{" + name + "}", "middle", w=140)
        # the mass as a bar to scale, left-aligned under the cube
        bx = cx - 75
        f.rect(bx, 268, m * per, 24, MUTED, INK, 1.5, 2)
        f.tex(cx, 316, "m = " + (f"{m:.1f}".replace(".", "{,}") if m < 10 else f"{m:.0f}") + r"\,\text{g}", "middle", w=150)
        f.tex(cx, 350, r"\rho = " + f"{RHO[name]:.2f}".replace(".", "{,}") + r"\,\tfrac{\text{g}}{\text{cm}^3}", "middle", w=170)
    f.line(205, 56, 205, 366, RULE, 2, "6 6")
    f.line(395, 56, 395, 366, RULE, 2, "6 6")
    return f.svg()


def m_v_graph():
    f = Fig("fy17-graph", 372, "Kuvaaja mittakaavassa: massa tilavuuden funktiona kolmelle aineelle. Jokainen aine antaa origon "
            "kautta kulkevan suoran: veden tiheys on 1,00 g/cm³, alumiinin 2,70 g/cm³ ja raudan 7,87 g/cm³. Mitä "
            "suurempi tiheys, sitä jyrkempi suora. Raudan suoralle on piirretty kulmakerrointa osoittava kolmio, "
            "jossa tilavuus kasvaa 20 cm³ ja massa noin 157 g.")
    ax = Axes(f, (96, 316), (440, 72), x=(0, 50), y=(0, 420), xticks=[10, 20, 30, 40, 50], yticks=[100, 200, 300, 400],
              xlabel=r"V\ (\text{cm}^3)", ylabel=r"m\ (\text{g})")
    for name, rho, col in (("vesi", 1.00, WATER), ("alumiini", 2.70, METAL_EDGE), ("rauta", 7.87, IRON)):
        ax.line([(0, 0), (50, rho * 50)], col, 3)
        for v in (10, 20, 30, 40, 50):
            ax.point(v, rho * v, col)
        f.tex(448, ax.Y(rho * 50), r"\text{" + name + "}", "start", col, w=120)
    # slope triangle on the iron line, 20 cm3 -> 40 cm3
    a, b = (20, 7.87 * 20), (40, 7.87 * 40)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 1.5, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 1.5, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) - 20, r"\Delta V", "middle", w=50)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta m", "start", w=50)
    f.tex(ax.X(a[0]) - 8, ax.Y(b[1]), r"\rho = \dfrac{\Delta m}{\Delta V}", "end", w=110)
    return f.svg()


def displacement():
    f = Fig("fy17-disp", 372, "Periaatekuva tilavuuden mittaamisesta vedensiirtymällä. Vasemmassa mittalasissa vesi yltää merkkiin "
            "40 ml. Kun kivi upotetaan, vesi nousee oikeassa mittalasissa merkkiin 70 ml. Kiven tilavuus on "
            "tilavuuksien erotus, 30 ml eli 30 cm³.")
    f.defs_add(f'<linearGradient id="fy17-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    top, bot, w = 44, 324, 70            # cylinder from 0 ml (bottom) to 100 ml (top)
    per = (bot - top) / 100
    def cyl(cx, ml, stone):
        x0, x1 = cx - w / 2, cx + w / 2
        y = bot - ml * per
        f.rect(x0, top - 10, w, bot - top + 10, GLASS)
        f.rect(x0 + 2, y, w - 4, bot - y - 2, "url(#fy17-water)")
        f.line(x0 + 2, y, x1 - 2, y, WHITE, 2.5)
        if stone:
            f.path(f"M{cx - 20},{bot - 6} Q{cx - 26},{bot - 30} {cx - 6},{bot - 38} Q{cx + 14},{bot - 46} {cx + 24},{bot - 24} Q{cx + 28},{bot - 6} {cx + 6},{bot - 4} Z", IRON, INK, 2.5)
        f.path(f"M{x0},{top - 10} V{bot} H{x1} V{top - 10}", stroke=INK, w=3)
        for k in range(0, 101, 10):
            yy = bot - k * per
            f.line(x0 - 9 if k % 20 == 0 else x0 - 5, yy, x0, yy, INK, 2 if k % 20 == 0 else 1.5)
        for k in (20, 60, 100):
            f.tex(x0 - 14, bot - k * per, str(k), "end", MUTED, w=48)
    cyl(120, 40, False)
    cyl(380, 70, True)
    y1, y2 = bot - 40 * per, bot - 70 * per
    f.line(155, y1, 440, y1, MUTED, 1.5, "6 5")
    f.line(415, y2, 440, y2, MUTED, 1.5, "6 5")
    f.path(f"M448,{n(y2)} H456 V{n(y1)} H448", stroke=HEAT, w=2.5)
    f.tex(466, (y1 + y2) / 2 - 16, r"\Delta V", "start", HEAT, w=60)
    f.tex(466, (y1 + y2) / 2 + 16, r"= 30\,\text{ml}", "start", HEAT, w=120)
    f.tex(120, 346, r"V_1 = 40\,\text{ml}", "middle", w=170)
    f.tex(380, 346, r"V_2 = 70\,\text{ml}", "middle", w=170)
    return f.svg()


FIGURES = {"cubes": cubes, "graph": m_v_graph, "displacement": displacement}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "cubes": "reveals: the masses 5,0 g, 27 g and 79 g of 10 cm³ cubes",
    "graph": "reveals: the densities of water, aluminium and iron",
    "displacement": "reveals: the volume 30 ml",
}
