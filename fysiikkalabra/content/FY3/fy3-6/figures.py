"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-6` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, GOOD, ALUMINIUM, METAL_EDGE,
                    IRON, COPPER, ICE, ICE_EDGE, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT, SAND_DARK, GRAIN, HOT_LIGHT, COLD_LIGHT, n)


def defs(f):
    f.defs_add(f'<linearGradient id="fy36-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy36-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    f.defs_add(f'<pattern id="fy36-grain" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" fill="{GRAIN}"/><circle cx="10" cy="8" r="1.1" fill="{GRAIN}"/><circle cx="8" cy="2" r="0.8" fill="#8a5f22"/></pattern>')
    f.defs_add(f'<linearGradient id="fy36-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')


def water_sand():
    f = Fig("fy36-ws", 384, "Kaavakuva: yhtä suuriin massoihin vettä ja hiekkaa siirtyy sama lämpömäärä Q, mitä kuvaavat yhtä pitkät "
            "nuolet. Veden lämpömittarin lukema nousee vähän, hiekan noin viisi kertaa enemmän, koska hiekan "
            "ominaislämpökapasiteetti 800 J/(kg·K) on noin viidesosa veden arvosta 4190 J/(kg·K). Lämpötilan nousut on "
            "piirretty mittakaavassa ja korostettu punaisella. Hiekkaa on astiassa tilavuutena vähemmän, koska se on "
            "tiheämpää kuin vesi.")
    defs(f)
    f.tex(300, 24, r"\text{sama } Q \text{ ja sama } m", "middle")
    f.line(300, 56, 300, 372, RULE, 2, "6 6")
    for cx, kind in ((192, "water"), (512, "sand")):
        x0, x1 = cx - 77, cx + 78            # vessel outer edges
        f.path(f"M{x0},140 V250 Q{x0},262 {x0 + 12},262 H{x1 - 12} Q{x1},262 {x1},250 V140 Z", GLASS)
        if kind == "water":
            f.path(f"M{x0 + 2},172 Q{x0 + 21},165 {x0 + 40},172 T{x0 + 78},172 T{x0 + 116},172 T{x1 - 2},172 V250 Q{x1 - 2},260 {x1 - 12},260 H{x0 + 12} Q{x0 + 2},260 {x0 + 2},250 Z", "url(#fy36-water)")
            f.path(f"M{x0 + 5},172 Q{x0 + 21},166 {x0 + 40},172 T{x0 + 78},172 T{x0 + 116},172 T{x1 - 5},172", stroke=WHITE, w=2.5, extra='stroke-opacity="0.8"')
        else:
            top = f"M{x0 + 2},218 L{x0 + 20},213 L{x0 + 38},217 L{x0 + 57},212 L{x0 + 76},216 L{x0 + 96},211 L{x0 + 116},215 L{x1 - 2},212 V250 Q{x1 - 2},260 {x1 - 12},260 H{x0 + 12} Q{x0 + 2},260 {x0 + 2},250 Z"
            f.path(top, "url(#fy36-sand)")
            f.path(top, "url(#fy36-grain)", extra='fill-opacity="0.6"')
        f.path(f"M{x0},140 V250 Q{x0},262 {x0 + 12},262 H{x1 - 12} Q{x1},262 {x1},250 V140", stroke=INK, w=3)
        # equal heat arrows
        f.path(f"M{cx - 8},56 H{cx + 8} V112 H{cx + 20} L{cx},140 L{cx - 20},112 H{cx - 8} Z", "url(#fy36-heat)")
        f.tex(cx + 24, 80, "Q", "start")
        # thermometer, rise to scale: water 20, sand 105
        tx = cx - 107
        f.rect(tx, 64, 14, 206, WHITE, INK, 2, 7)
        for y in range(86, 252, 15):
            f.line(tx + 14, y, tx + 20, y, MUTED, 1.5)
        f.rect(tx + 4, 236, 6, 36, HOT_LIGHT)
        f.circle(tx + 7, 276, 13, HOT_LIGHT, INK, 2)
        rise = 20 if kind == "water" else 105
        f.rect(tx + 4, 236 - rise, 6, rise, HOT)
        f.line(tx - 8, 236, tx + 22, 236, INK, 2, "4 3")
        f.path(f"M{tx - 16},{236 - rise} H{tx - 22} V236 H{tx - 16}", stroke=HOT, w=2.5)
        if kind == "water":
            f.tex(tx - 28, 226, r"\Delta T", "end")
        else:
            f.tex(tx - 28, 183, r"\approx 5\,\Delta T", "end")
        f.tex(cx, 294, r"\text{vesi}" if kind == "water" else r"\text{hiekka}", "middle")
        f.tex(cx, 346, (r"c = 4190\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}" if kind == "water"
                        else r"c = 800\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}"), "middle", w=170)
    return f.svg()


def c_bars():
    f = Fig("fy36-cb", 350, "Vaakapylväskaavio ominaislämpökapasiteeteista yksikössä J/(kg·K): vesi 4190, jää 2100, alumiini 900, "
            "hiekka 800, rauta 450 ja kupari 385. Pylväiden pituudet ovat mittakaavassa: veden pylväs on noin viisi kertaa "
            "hiekan pylvään pituinen.")
    f.defs_add(f'<linearGradient id="fy36-sandbar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{SAND}"/><stop offset="1" stop-color="{SAND_DARK}"/></linearGradient>')
    f.tex(130, 24, r"c\ \left(\text{J/(kg}\cdot\text{K)}\right)", "start", w=230)
    x0, per = 130, 391.1 / 4190          # 1000 J/(kg K) = 93.3 units
    for t in (1000, 2000, 3000, 4000):
        f.line(x0 + t * per, 50, x0 + t * per, 304, RULE_LIGHT, 1.5)
    rows = [("vesi", 4190, WATER, None), ("jää", 2100, ICE, ICE_EDGE), ("alumiini", 900, ALUMINIUM, METAL_EDGE),
            ("hiekka", 800, "url(#fy36-sandbar)", GRAIN), ("rauta", 450, IRON, None), ("kupari", 385, COPPER, None)]
    for i, (name, c, fill, edge) in enumerate(rows):
        y = 52 + 42 * i
        w = c * per
        f.rect(x0, y, w, 28, fill, edge, 1.5, 3)
        f.tex(x0 - 10, y + 14, r"\text{" + name + "}", "end")
        f.tex(x0 + w + 8, y + 14, str(c), "start")
    f.arrow(x0, 304, x0 + 4 * 93.3 + 26, 304, INK, 2.5, 13)
    f.line(x0, 46, x0, 306, INK, 2.5)
    for t in (0, 1000, 2000, 3000, 4000):
        if t: f.line(x0 + t * per, 304, x0 + t * per, 311, INK, 2)
        f.tex(x0 + t * per, 330, str(t), "middle", MUTED)
    return f.svg()


def calorimeter():
    f = Fig("fy36-cal", 432, "Kalorimetri ennen ja jälkeen lämpötasapainon, periaatekuva, ei mittakaavassa. Ennen: eristetyssä astiassa "
            "on 0,300 kg vettä 20,0 °C:ssa ja sen yläpuolella langasta roikkuu 0,200 kg:n metallikappale 100,0 °C:ssa. "
            "Jälkeen: kappale on vedessä, ja sekä vesi että kappale ovat lämpötilassa 24,5 °C. Metallin luovuttama "
            "lämpömäärä on yhtä suuri kuin veden vastaanottama.")
    defs(f)
    f.defs_add(f'<pattern id="fy36-insul" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="{MUTED}" stroke-width="2"/></pattern>')
    f.tex(150, 22, r"\text{ennen}", "middle")
    f.tex(450, 22, r"\text{jälkeen}", "middle")
    f.line(300, 12, 300, 316, RULE, 2, "6 6")
    top, bot, wall = 168, 312, 14
    for cx, after in ((150, False), (450, True)):
        x0, x1 = cx - 92, cx + 92
        level = 204
        f.path(f"M{x0},{top} V{bot - 12} Q{x0},{bot} {x0 + 12},{bot} H{x1 - 12} Q{x1},{bot} {x1},{bot - 12} V{top} Z", GLASS)
        ib = bot - wall
        f.path(f"M{x0 + wall},{level} Q{x0 + 40},{level - 6} {cx - 24},{level} T{cx + 24},{level} T{x1 - wall},{level} V{ib} H{x0 + wall} Z", "url(#fy36-water)")
        f.path(f"M{x0 + wall + 2},{level} Q{x0 + 40},{level - 6} {cx - 24},{level} T{cx + 24},{level} T{x1 - wall - 2},{level}", stroke=WHITE, w=2.5, extra='stroke-opacity="0.8"')
        # insulating wall: hatched
        f.path(f"M{x0},{top} V{bot - 12} Q{x0},{bot} {x0 + 12},{bot} H{x1 - 12} Q{x1},{bot} {x1},{bot - 12} V{top} H{x1 - wall} V{ib} H{x0 + wall} V{top} Z",
               "url(#fy36-insul)", INK, 3)
        f.path(f"M{x0 + wall},{top} V{ib} H{x1 - wall} V{top}", stroke=INK, w=2)
        if not after:
            mx, my = cx - 45, 84
            f.line(mx, 48, mx, my, INK, 2)
            f.circle(mx, 48, 3, INK)
            f.rect(mx - 22, my, 44, 46, COPPER, INK, 2.5, 5)
            f.tex(mx + 32, my + 8, r"T_\text{m} = 100{,}0\,{}^\circ\text{C}", "start", HOT, w=160)
            f.tex(mx + 32, my + 38, r"m_\text{m} = 0{,}200\,\text{kg}", "start", w=160)
            f.tex(cx, 332, r"T_\text{v} = 20{,}0\,{}^\circ\text{C}", "middle", COLD, w=200)
            f.tex(cx, 366, r"m_\text{v} = 0{,}300\,\text{kg}", "middle", w=200)
        else:
            mx, my = cx - 40, 246
            f.rect(mx - 22, my, 44, 46, COPPER, INK, 2.5, 5)
            f.block_arrow(mx + 28, my + 23, mx + 84, my + 23, "url(#fy36-heat)", 14, 30, 24)
            f.tex(mx + 56, my - 10, "Q", "middle", bg=True)
            f.tex(cx, 332, r"T = 24{,}5\,{}^\circ\text{C}", "middle", w=200)
            f.tex(cx, 366, r"\text{sama } T \text{ kaikkialla}", "middle", w=220)
    f.line(12, 394, 588, 394, RULE_LIGHT, 1.5)
    f.tex(300, 414, r"Q_\text{luovutettu} = Q_\text{vastaanotettu}", "middle", w=340)
    return f.svg()


def hero():
    """The chapter's opening illustration: a lake beach in the morning sun, the sand already hot, the water still cool."""
    f = Fig("fy36-hero", 600, "Kuvitus: järven uimaranta aamupäivällä. Aurinko paistaa sekä hiekkaan että veteen. Hiekan yllä "
            "väreilee kuumuus, ja hiekkaan pistetyn lämpömittarin punainen pylväs on korkealla. Rantaveteen pistetyn "
            "lämpömittarin pylväs on matalalla, koska vesi on vielä viileää.", width=1200, hero=True)
    f.defs_add(f'<linearGradient id="fy36h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ICE}"/><stop offset="1" stop-color="{GLASS}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy36h-lake" gradientUnits="userSpaceOnUse" x1="0" y1="300" x2="0" y2="600"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy36h-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy36h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.defs_add(f'<pattern id="fy36h-grain" width="22" height="16" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.8" fill="{GRAIN}"/><circle cx="15" cy="11" r="1.4" fill="{GRAIN}"/><circle cx="12" cy="3" r="1" fill="#8a5f22"/></pattern>')
    # sky, sun and its halo, clouds
    f.rect(0, 0, 1200, 600, "url(#fy36h-sky)")
    f.add(f'<circle cx="250" cy="118" r="96" fill="{WHITE}" fill-opacity="0.5"/>')
    for k in range(12):
        a = k * math.pi / 6 + math.pi / 12
        c, s_ = math.cos(a), math.sin(a)
        r0, r1, hw = 74, 104, 7
        f.path(f"M{n(250 + c * r0 - s_ * hw)},{n(118 + s_ * r0 + c * hw)} L{n(250 + c * r1)},{n(118 + s_ * r1)} "
               f"L{n(250 + c * r0 + s_ * hw)},{n(118 + s_ * r0 - c * hw)} Z", HEAT_LIGHT)
    f.circle(250, 118, 60, "url(#fy36h-sun)")
    for cx, cy, sc in ((760, 92, 1.0), (1010, 150, 0.7)):
        f.path(f"M{n(cx - 90 * sc)},{n(cy + 20 * sc)} Q{n(cx - 92 * sc)},{n(cy - 14 * sc)} {n(cx - 52 * sc)},{n(cy - 10 * sc)} "
               f"Q{n(cx - 36 * sc)},{n(cy - 46 * sc)} {n(cx + 4 * sc)},{n(cy - 34 * sc)} Q{n(cx + 40 * sc)},{n(cy - 54 * sc)} {n(cx + 60 * sc)},{n(cy - 16 * sc)} "
               f"Q{n(cx + 96 * sc)},{n(cy - 12 * sc)} {n(cx + 92 * sc)},{n(cy + 20 * sc)} Z", WHITE)
    # far shore: two layers of spruce forest on the horizon
    def forest(y0, h, step, colour, seed):
        d, x = f"M0,{y0}", 0
        while x < 1200:
            r = (math.sin(x * 12.9898 + seed * 78.233) * 43758.5453) % 1      # a fixed pseudo-random tree height
            w = step * (0.7 + 0.6 * r)
            d += f" L{n(x + w / 2)},{n(y0 - h * (0.45 + 0.55 * r))} L{n(x + w)},{y0}"
            x += w
        f.path(d + f" V{y0 + 30} H0 Z", colour)
    forest(292, 46, 26, ALUMINIUM, 3)
    forest(306, 34, 20, METAL_EDGE, 5)
    # the lake, with light on its ripples
    f.rect(0, 300, 1200, 300, "url(#fy36h-lake)")
    for x, y, w in ((640, 340, 90), (860, 330, 120), (1040, 362, 80), (760, 392, 140), (980, 428, 110), (900, 500, 150), (1080, 540, 90)):
        f.path(f"M{x},{y} q{n(w / 4)},-6 {n(w / 2)},0 t{n(w / 2)},0", stroke=WHITE, w=3, extra='stroke-opacity="0.7" stroke-linecap="round"')
    # the sand: wet strip, foam line, dry sand with grains
    shore = "M0,330 C260,336 470,402 610,470 C700,514 760,560 790,600"
    f.path(shore + " H0 Z", SAND)
    dry = "M0,340 C250,348 450,410 585,474 C670,516 726,562 752,600"
    f.path(dry + " H0 Z", "url(#fy36h-sand)")
    f.path(dry + " H0 Z", "url(#fy36h-grain)", extra='fill-opacity="0.55"')
    f.path(shore, stroke=WHITE, w=4, extra='stroke-linecap="round" stroke-opacity="0.85"')
    # footprints towards the water
    for k, (x, y) in enumerate(((330, 590), (380, 560), (432, 532), (484, 506), (536, 484))):
        dx = 12 if k % 2 else -12
        f.add(f'<ellipse cx="{x + dx}" cy="{y}" rx="13" ry="7" transform="rotate(-22 {x + dx} {y})" fill="{GRAIN}" fill-opacity="0.45"/>')
    # towel
    f.path("M40,486 L220,470 L262,540 L70,562 Z", WHITE, INK, 3)
    for t in (0.2, 0.45, 0.7):
        f.path(f"M{n(40 + 30 * t)},{n(486 + 76 * t)} L{n(220 + 42 * t)},{n(470 + 70 * t)} L{n(220 + 42 * (t + 0.12))},{n(470 + 70 * (t + 0.12))} "
               f"L{n(40 + 30 * (t + 0.12))},{n(486 + 76 * (t + 0.12))} Z", COLD_LIGHT)
    f.path("M40,486 L220,470 L262,540 L70,562 Z", stroke=INK, w=3)
    # heat shimmering above the hot sand
    for x in (230, 300, 370):
        f.path(f"M{x},446 q-12,-16 0,-32 t0,-32 t0,-32", stroke=HEAT, w=4, extra='stroke-linecap="round" stroke-opacity="0.75"')

    def thermometer(x, ybot, level, colour):
        f.rect(x - 9, ybot - 150, 18, 150, WHITE, INK, 3, 9)
        f.circle(x, ybot, 16, colour, INK, 3)
        f.rect(x - 4, ybot - level, 8, level, colour)
        for k in range(1, 7):
            f.line(x + 9, ybot - 20 * k, x + 17, ybot - 20 * k, MUTED, 2)
    # a thermometer stuck in the sand reads high, one in the shallow water reads low
    thermometer(450, 500, 128, HOT)
    f.add(f'<ellipse cx="450" cy="504" rx="40" ry="12" fill="{SAND}"/>')          # the bulb is buried in the sand
    f.add(f'<ellipse cx="450" cy="500" rx="30" ry="8" fill="url(#fy36h-grain)"/>')
    thermometer(880, 520, 66, HOT_LIGHT)
    f.rect(840, 482, 80, 118, "url(#fy36h-lake)", extra='fill-opacity="0.8"')    # the bulb is under the water
    f.add(f'<ellipse cx="880" cy="482" rx="30" ry="6" fill="none" stroke="{WHITE}" stroke-width="3"/>')
    return f.svg()


FIGURES = {"hero": hero, "water-sand": water_sand, "c-bars": c_bars, "calorimeter": calorimeter}
