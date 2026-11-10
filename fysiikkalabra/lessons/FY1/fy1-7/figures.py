"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-7` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT, GRAIN,
                    ALUMINIUM, METAL_EDGE, IRON, HEAT, n)
import math
from figlib import PAPER
import herolib as H
from figlib import COLD_LIGHT, GOOD_LIGHT, HEAT_LIGHT
from herolib import grad, steel
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S

# densities in g/cm3 (the lesson's table) and the cube of 10 cm3 (edge about 2,15 cm)
RHO = {"mänty": 0.50, "alumiini": 2.70, "rauta": 7.87}


def hero():
    """The chapter's opening illustration: two cubes of the same size tip a balance, a measuring cylinder waits beside them."""
    f = S.hero("fy17-hero", "Kuvitus: laboratorion pöydällä vaaka, jonka kupeissa on kaksi samankokoista metallikuutiota, vaalea ja tumma. "
               "Vaaka kallistuu tumman kuution puolelle. Vieressä mittalasi, jossa on vettä.")
    H.tiles(f, 430)
    H.window(f, 60, 50, 220, 230, "fy17h-win")
    f.rect(820, 120, 340, 14, RULE, INK, 3, 3)                               # a shelf with bottles
    for k, (x, h, c) in enumerate(((850, 70, COLD_LIGHT), (910, 90, GOOD_LIGHT), (980, 60, HEAT_LIGHT), (1040, 84, GLASS), (1100, 66, COLD_LIGHT))):
        f.rect(x, 120 - h, 40, h, c, INK, 2.5, 6); f.rect(x + 12, 120 - h - 14, 16, 16, IRON, INK, 2)
    f.rect(0, 430, 1200, 26, RULE, INK, 3); f.rect(0, 456, 1200, 144, RULE_LIGHT)
    for x in (300, 900): f.line(x, 456, x, 600, INK, 2)
    for x in (270, 330, 870, 930): f.rect(x - 4, 480, 8, 44, METAL_EDGE, rx=4)
    # the balance: a heavy foot, a pillar, the beam tilted towards the iron cube
    cx, top = 540, 170; t = math.radians(9)
    f.path(f"M{cx - 120},430 L{cx - 90},398 H{cx + 90} L{cx + 120},430 Z", grad(f, "fy17h-foot", IRON, INK), INK, 3)
    f.rect(cx - 14, top, 28, 230, steel(f, "fy17h-pillar"), INK, 3, 4)
    L = 280
    lx, ly = cx - L * math.cos(t), top - L * math.sin(t); rx, ry = cx + L * math.cos(t), top + L * math.sin(t)
    f.line(lx, ly, rx, ry, INK, 16, cap="round"); f.line(lx, ly, rx, ry, ALUMINIUM, 10, cap="round")
    f.circle(cx, top, 14, IRON, INK, 3)
    f.add(f'<g transform="rotate(9 {cx} {top})">')                       # the pointer is fixed to the beam and turns with it
    f.path(f"M{cx - 10},{top + 6} L{cx},{top + 124} L{cx + 10},{top + 6} Z", IRON, INK, 2)
    f.add("</g>"); f.circle(cx, top, 14, IRON, INK, 3)
    f.path(f"M{cx - 50},{top + 128} A60,60 0 0 0 {cx + 50},{top + 128}", stroke=INK, w=3)
    for k in range(-2, 3): f.line(cx + 12 * k, top + 132 + abs(k) * 2, cx + 12 * k, top + 142 + abs(k) * 2, INK, 2)
    for x, y, cube, side, lit in ((lx, ly, ALUMINIUM, METAL_EDGE, WHITE), (rx, ry, IRON, INK, METAL_EDGE)):
        pan = y + 150
        f.line(x, y, x - 80, pan, MUTED, 2.5); f.line(x, y, x + 80, pan, MUTED, 2.5)
        f.path(f"M{n(x - 100)},{n(pan)} Q{n(x)},{n(pan + 40)} {n(x + 100)},{n(pan)} Z", steel(f, f"fy17h-pan{int(x)}"), INK, 3)
        s = 90; bx, by = x - s / 2 - 10, pan - s
        f.rect(bx, by, s, s, cube, INK, 3)
        f.path(f"M{n(bx)},{n(by)} l24,-20 h{s} l-24,20 Z", lit, INK, 3)
        f.path(f"M{n(bx + s)},{n(by)} l24,-20 v{s} l-24,20 Z", side, INK, 3)
    # measuring cylinder with water and its meniscus
    x0, w = 960, 104
    f.rect(x0 - 24, 410, w + 48, 20, GLASS, INK, 3, 4)
    f.rect(x0, 250, w, 160, grad(f, "fy17h-water", WATER_LIGHT, WATER))
    f.add(f'<rect x="{x0}" y="130" width="{w}" height="280" fill="{GLASS}" fill-opacity="0.35" stroke="{INK}" stroke-width="3"/>')
    f.path(f"M{x0 - 8},130 H{x0 + w + 8} l-6,10 H{x0 - 2} Z", GLASS, INK, 2)
    f.path(f"M{x0},250 Q{x0 + w / 2},262 {x0 + w},250", stroke=WATER, w=3)
    for k in range(14): f.line(x0, 396 - k * 20, x0 + (30 if k % 2 == 0 else 16), 396 - k * 20, INK, 2)
    f.add(f'<rect x="{x0 + 8}" y="140" width="10" height="266" fill="{WHITE}" fill-opacity="0.6"/>')
    return f.svg()


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
    # slope triangle on the iron line, 20 cm3 -> 40 cm3
    a, b = (20, 7.87 * 20), (40, 7.87 * 40)
    f.path(f"M{n(ax.X(a[0]))},{n(ax.Y(a[1]))} L{n(ax.X(b[0]))},{n(ax.Y(a[1]))} L{n(ax.X(b[0]))},{n(ax.Y(b[1]))} Z", fill=S.light(IRON, 0.85))
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), IRON, 1.5)
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), IRON, 1.5)
    for name, rho, col in (("vesi", 1.00, WATER), ("alumiini", 2.70, METAL_EDGE), ("rauta", 7.87, IRON)):
        ax.line([(0, 0), (50, rho * 50)], col, 3)
        for v in (10, 20, 30, 40, 50):
            ax.point(v, rho * v, col)
        f.tex(448, ax.Y(rho * 50), r"\text{" + name + "}", "start", col, w=120)
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) - 20, r"\Delta V", "middle", w=50)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta m", "start", w=50)
    f.tex(ax.X(a[0]) - 8, ax.Y(b[1]), r"\rho = \dfrac{\Delta m}{\Delta V}", "end", w=110)
    return f.svg()


def displacement():
    f = Fig("fy17-disp", 372, "Periaatekuva tilavuuden mittaamisesta vedensiirtymällä. Vasemmassa mittalasissa vesi yltää merkkiin "
            "40 ml. Kun kivi upotetaan, vesi nousee oikeassa mittalasissa merkkiin 70 ml. Kiven tilavuus on "
            "lukemien erotus, 30 ml eli 30 cm³.")
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
    cyl(110, 40, False)
    cyl(330, 70, True)
    y1, y2 = bot - 40 * per, bot - 70 * per
    f.line(145, y1, 384, y1, MUTED, 1.5, "6 5")
    f.line(365, y2, 384, y2, MUTED, 1.5, "6 5")
    f.dim_v(392, y2, y1, r"V = V_2 - V_1", HEAT)
    f.tex(404, (y1 + y2) / 2 + 30, r"= 30\,\text{ml}", "start", HEAT)
    f.tex(110, 346, r"V_1 = 40\,\text{ml}", "middle", w=170)
    f.tex(330, 346, r"V_2 = 70\,\text{ml}", "middle", w=170)
    return f.svg()


def cylinders_read():
    """A task-only variant of `displacement`: two measuring cylinders with a fine scale and no values written; the student reads both levels."""
    f = Fig("fy17-cyl", 404, "Kuva mittalasista ennen ja jälkeen metallikappaleen upottamisen. Asteikko on 0–100 ml, numerot joka 20 ml:n kohdalla ja "
            "pienet viivat joka 2 ml:n kohdalla. Vasemmassa mittalasissa vesi yltää merkkiin 40 ml. Kun kappale on upotettu, vesi yltää oikeassa mittalasissa merkkiin 50 ml.")
    f.defs_add(f'<linearGradient id="fy17-water2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    top, bot, w = 50, 360, 80            # cylinder from 0 ml (bottom) to 100 ml (top)
    per = (bot - top) / 100
    def cyl(cx, ml, piece):
        x0, x1 = cx - w / 2, cx + w / 2
        y = bot - ml * per
        f.rect(x0, top - 10, w, bot - top + 10, GLASS)
        f.rect(x0 + 2, y, w - 4, bot - y - 2, "url(#fy17-water2)")
        f.line(x0 + 2, y, x1 - 2, y, WHITE, 2.5)
        if piece:
            f.rect(cx - 16, bot - 40, 32, 36, IRON, INK, 2.5, 3)
        f.path(f"M{x0},{top - 10} V{bot} H{x1} V{top - 10}", stroke=INK, w=3)
        for k in range(0, 101, 2):
            yy = bot - k * per
            f.line(x0 - (10 if k % 10 == 0 else 5), yy, x0, yy, INK, 2 if k % 10 == 0 else 1.2)
        for k in range(20, 101, 20):
            f.tex(x0 - 16, bot - k * per, str(k), "end", MUTED, w=48)
        f.tex(x0 - 16, top - 30, r"\text{ml}", "end", MUTED, w=48)
    cyl(150, 40, False)
    cyl(400, 50, True)
    f.tex(150, 388, r"\text{ennen}", "middle", w=100)
    f.tex(400, 388, r"\text{jälkeen}", "middle", w=100)
    return f.svg()


def gold_bar():
    """Task illustration (fy1-7-L2-01): a gold bar with its three edges dimensioned; no mass or density."""
    f = Fig("fy17-gold", 330, "Kuvitus: kultaharkko pöydällä, harkon mitat 10,0 cm, 5,0 cm ja 2,0 cm on merkitty mittaviivoin.")
    gold, side, top_ = "#e2b23c", "#b9861c", "#f3d27a"
    x0, y0, L, D, H_ = 120, 150, 300, 110, 60          # front face width L, depth drawn at 30° as D·(cos, sin)
    dx, dy = D * 0.82, -D * 0.5
    f.add(f'<ellipse cx="{x0 + L / 2 + dx / 2}" cy="{y0 + H_ + 8}" rx="{L / 2 + 70}" ry="12" fill="#d9d2c3" opacity="0.7"/>')
    f.path(f"M{x0},{y0} L{x0 + dx},{y0 + dy} H{x0 + L + dx} L{x0 + L},{y0} Z", top_, S.dark(gold, 0.45), S.W_OBJ)
    f.path(f"M{x0 + L},{y0} L{x0 + L + dx},{y0 + dy} V{y0 + dy + H_} L{x0 + L},{y0 + H_} Z", side, S.dark(gold, 0.45), S.W_OBJ)
    f.rect(x0, y0, L, H_, gold, S.dark(gold, 0.45), S.W_OBJ)
    f.path(f"M{x0 + 24},{y0 + 14} H{x0 + 120}", stroke="#fff3c4", w=4, extra='stroke-linecap="round" opacity="0.8"')
    f.dim_h(x0, x0 + L, y0 + H_ + 34, r"10{,}0\,\text{cm}")
    f.dim_v(x0 - 22, y0, y0 + H_, r"2{,}0\,\text{cm}", side="left")
    f.line(x0 + L + 18, y0 + H_ + 4, x0 + L + dx + 18, y0 + H_ + dy + 4, INK, 1.25)
    for t in (0, 1): f.line(x0 + L + 18 + dx * t - 5, y0 + H_ + dy * t + 4 - 5, x0 + L + 18 + dx * t + 5, y0 + H_ + dy * t + 4 + 5, INK, 1.25)
    f.tex(x0 + L + dx / 2 + 34, y0 + H_ + dy / 2 + 14, r"5{,}0\,\text{cm}", "start")
    return f.svg()


def sinker():
    """Task illustration (fy1-7-L1-08): a fishing line with a float and a lead sinker under the water surface; no numbers."""
    f = S.scene("fy17-sinker", "Kuvitus: onkisiima järvessä. Pinnalla kelluu koho, jonka punainen yläosa on veden yläpuolella ja valkoinen alaosa veden alla, ja siiman alapäässä veden alla on harmaa "
                "pisaranmuotoinen lyijypaino ja koukku.")
    f.rect(0, 0, 600, 120, "#e3eef6")
    f.path("M0,104 C120,96 200,100 300,96 C420,92 520,98 600,96 V120 H0 Z", "#9db8a4")
    f.rect(0, 120, 600, 240, S.light(WATER, 0.45))
    f.rect(0, 250, 600, 110, S.light(WATER, 0.2), extra='opacity="0.5"')
    f.path("M0,120 H600", stroke=S.light(WATER, 0.7), w=3)
    for x in (60, 180, 420, 520): f.path(f"M{x},{126} q14,-5 28,0", stroke="#ffffff", w=2, extra='opacity="0.7"')
    f.path("M190,0 C230,40 290,80 300,90", stroke=S.SOFT_INK, w=1.25)            # line from the rod above
    # the float: red top above the surface, white bottom under it (the water drawn over it, see-through)
    body = "M300,102 C290,102 286,112 286,120 C286,132 300,142 300,142 C300,142 314,132 314,120 C314,112 310,102 300,102 Z"
    f.path(body, "#ffffff", S.SOFT_INK, 1.5)
    f.path("M300,102 C290,102 286,112 286,120 H314 C314,112 310,102 300,102 Z", "#d6402f", S.dark("#d6402f", 0.4), 1.5)
    f.line(300, 88, 300, 102, "#d6402f", 3, cap="round")
    f.path(body.replace("M300,102", "M286,120").split(" C286,132")[0] + " C286,132 300,142 300,142 C300,142 314,132 314,120 Z",
           S.light(WATER, 0.45), extra='opacity="0.45"')
    f.line(300, 142, 300, 222, S.SOFT_INK, 1.25)
    f.path("M300,222 C290,224 286,238 290,248 C294,258 306,258 310,248 C314,238 310,224 300,222 Z", "#7d8590", S.dark("#7d8590", 0.4), S.W_OBJ)
    f.path("M295,232 q-2,8 1,14", stroke="#c4ccd4", w=2.5, extra='stroke-linecap="round"')
    f.line(300, 258, 300, 284, S.SOFT_INK, 1.25)
    f.path("M300,284 v16 a8,8 0 0 1 -16,0 l4,-4", stroke="#5b636d", w=2.5, extra='stroke-linecap="round"')
    for x, y, r in ((120, 220, 4), (128, 206, 3), (470, 300, 5), (478, 284, 3)): f.circle(x, y, r, "none", "#ffffff", 1.5)
    f.path("M0,330 C150,320 300,336 600,326 V360 H0 Z", "#c9b48a")
    return f.svg()


FIGURES = {"hero": hero, "cubes": cubes, "graph": m_v_graph, "displacement": displacement, "cylinders-read": cylinders_read,
           "gold-bar": gold_bar, "sinker": sinker}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "cubes": "reveals: the masses 5,0 g, 27 g and 79 g of 10 cm³ cubes",
    "graph": "reveals: the densities of water, aluminium and iron",
    "displacement": "reveals: the volume 30 ml",
    "gold-bar": "safe: the bar's edges 10,0 cm, 5,0 cm and 2,0 cm (given in the task), no mass",
    "sinker": "safe: the situation only, a lead sinker on a fishing line under water; no numbers",
    "cylinders-read": "safe: two measuring cylinders before and after, levels to be read from a fine scale (displacement is the lesson figure)",
}
