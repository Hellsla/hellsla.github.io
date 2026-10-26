"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-6` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, GOOD, ALUMINIUM, METAL_EDGE,
                    IRON, COPPER, ICE, ICE_EDGE, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT, SAND_DARK, GRAIN, HOT_LIGHT, n)


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


FIGURES = {"water-sand": water_sand, "c-bars": c_bars, "calorimeter": calorimeter}
