"""Figures of the FY9 unit fy9-kaasut (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-kaasut`
writes them into content/fi/units/fy9-kaasut/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a frosty winter morning; a car has stood outside all night beside a lit, warm garage where
            its tyres were last pumped; a frosted thermometer on the wall (no text, no people)
kartta      the concept map of the review: pressure p = F/A at the top, three branches (liquid, gas, heat engine)
rengas      the hook's answer to scale: the tyre's total pressure = air pressure + gauge reading, at +20 °C and -20 °C
kone        the energy flows of a heat engine to scale: Q1 = 1000 J in, W = 350 J out as work, Q2 = 650 J to the cold
"""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT,
                    COLD, COLD_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, GOOD, GOOD_LIGHT, n, fi)
import herolib as H

figlib.set_language({}, ",")

# rengas: the hook (numbers quoted in unit.md and inquiry.json; p0 = 101 kPa, the tyre's volume taken as constant)
P0 = 101.0                                   # kPa, air pressure
GAUGE_WARM = 230.0                           # kPa, the gauge reading in the warm garage
T_WARM, T_COLD = 20 + 273.15, -20 + 273.15   # K
P_WARM = P0 + GAUGE_WARM                     # 331 kPa total
P_COLD = P_WARM * T_COLD / T_WARM            # 285,8 kPa total
GAUGE_COLD = P_COLD - P0                     # 184,8 kPa: the gauge drops by about 45 kPa

# kone: the example heat engine of the theory summary
Q1, W = 1000.0, 350.0
Q2 = Q1 - W                                  # 650 J; eta = W / Q1 = 0,35


def hero():
    """A frosty winter dawn in a Finnish yard: a lit garage with its door open (warm inside, a compressor hose on the
    wall), a car that has stood outside all night with frost on its roof, a thermometer on the wall low in its scale."""
    f = H.hero("fy9ka-hero", "Kuvitus: pakkasaamu pihalla. Vasemmalla autotalli, jonka ovi on auki ja jonka sisällä palaa lämmin "
               "valo; seinällä roikkuu paineilmaletku. Pihalla seisoo auto, joka on ollut ulkona koko yön: sen katolla ja "
               "ikkunoissa on huurretta. Autotallin ulkoseinän lämpömittarin punainen pylväs on matalalla. Taustalla "
               "lumiset kuuset ja vaalea aamutaivas.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9ka-sky", "#9fc3e0", "#f3e3cf"))
    f.add(f'<circle cx="980" cy="300" r="70" fill="{HEAT_LIGHT}" fill-opacity="0.55"/>')     # the low sun at dawn
    f.add(f'<circle cx="980" cy="300" r="44" fill="#ffd8a8"/>')
    H.forest(f, 330, 46, 34, "#3d5a4a", seed=7, depth=26)
    # snow
    f.path("M0,330 Q300,316 600,326 T1200,322 V600 H0 Z", "#f8fbfd")
    f.path("M0,470 Q320,452 640,466 T1200,462 V600 H0 Z", "#e6eff5")
    for k in range(26):                                   # frost sparkle on the snow
        x, y = 40 + H.rnd(k, 5) * 1120, 350 + H.rnd(k + 70, 5) * 230
        f.line(x - 5, y, x + 5, y, WHITE, 2, cap="round"); f.line(x, y - 5, x, y + 5, WHITE, 2, cap="round")
    # spruces
    for x, h in ((700, 190), (770, 150), (1130, 210), (1185, 160)):
        H.spruce(f, x, 400, h, "#2b6a3e")
        f.path(f"M{n(x - h * 0.3)},{n(400 - h * 0.17)} L{n(x)},{n(400 - h * 0.37)} L{n(x + h * 0.3)},{n(400 - h * 0.17)} "
               f"l-{n(h * 0.06)},-{n(h * 0.02)} L{n(x)},{n(400 - h * 0.31)} Z", WHITE)
    # garage: red wooden wall, open door with warm light inside
    gx, gy, gw, gh = 70, 470, 420, 230
    f.rect(gx, gy - gh, gw, gh, HOT, INK, 3)
    for k in range(1, int(gw / 14)): f.line(gx + k * 14, gy - gh + 3, gx + k * 14, gy - 3, HOT_LIGHT, 1)
    f.rect(gx, gy - gh, 10, gh, WHITE, INK, 2); f.rect(gx + gw - 10, gy - gh, 10, gh, WHITE, INK, 2)
    f.path(f"M{gx - 24},{gy - gh} L{gx + gw / 2},{gy - gh - 96} L{gx + gw + 24},{gy - gh} Z", WHITE, INK, 3)
    f.path(f"M{gx - 24},{gy - gh} L{gx + gw / 2},{gy - gh - 96} L{gx + gw + 24},{gy - gh} l-9,9 L{gx + gw / 2},{gy - gh - 84} L{gx - 15},{gy - gh + 9} Z", ICE)
    dx, dw, dh = gx + 40, 250, 180                        # the open door
    f.rect(dx, gy - dh, dw, dh, H.grad(f, "fy9ka-warm", "#ffe8c2", HEAT_LIGHT), INK, 3)
    f.rect(dx + 6, gy - dh, dw - 12, 10, IRON)            # the rolled-up door
    f.add(f'<circle cx="{dx + dw / 2}" cy="{gy - dh + 30}" r="10" fill="#fff4e0" stroke="{INK}" stroke-width="2"/>')
    f.add(f'<path d="M{dx},{gy} L{dx + dw},{gy} L{dx + dw + 70},{gy + 60} L{dx - 50},{gy + 60} Z" fill="{HEAT_LIGHT}" fill-opacity="0.35"/>')
    # compressor and its hose inside the garage
    f.rect(dx + 24, gy - 64, 64, 64, COLD, INK, 2.5, 6)
    f.circle(dx + 56, gy - 40, 13, WHITE, INK, 2); f.line(dx + 56, gy - 40, dx + 63, gy - 47, INK, 2, cap="round")
    f.path(f"M{dx + 88},{gy - 50} Q{dx + 150},{gy - 140} {dx + 190},{gy - 100} Q{dx + 222},{gy - 66} {dx + 200},{gy - 30}",
           stroke=INK, w=4, extra='stroke-linecap="round"')
    f.rect(dx + 192, gy - 34, 16, 22, ALUMINIUM, INK, 2, 3)
    # shelf with a tyre inside
    f.rect(dx + 140, gy - dh + 52, 96, 8, "#b8622d", INK, 1.5)
    f.circle(dx + 210, gy - 30, 28, INK); f.circle(dx + 210, gy - 30, 12, ALUMINIUM, INK, 2)
    # thermometer on the outer wall, low in its scale (cold)
    H.thermometer(f, gx + gw - 40, gy - 40, 30, HOT, 140)
    f.rect(gx + gw - 49, gy - 180, 18, 140, "none", ICE, 2, 9)
    # the car outside, facing left, frost on the roof and windows
    cy = 520
    f.path(f"M640,{cy} L646,{cy - 40} Q654,{cy - 58} 680,{cy - 62} L728,{cy - 86} Q760,{cy - 98} 812,{cy - 98} L874,{cy - 98} "
           f"Q912,{cy - 96} 938,{cy - 66} L980,{cy - 52} Q1002,{cy - 46} 1004,{cy - 22} L1004,{cy} Z", "#5c7c99", INK, 3)
    f.path(f"M694,{cy - 62} L738,{cy - 82} Q766,{cy - 92} 806,{cy - 92} L806,{cy - 62} Z", GLASS, INK, 2)
    f.path(f"M818,{cy - 92} L870,{cy - 92} Q900,{cy - 88} 922,{cy - 62} L818,{cy - 62} Z", GLASS, INK, 2)
    for k in range(9):                                    # frost on the glass
        x = 712 + k * 23 + 6 * H.rnd(k, 3)
        f.line(x, cy - 66, x + 10, cy - 84 + 8 * H.rnd(k + 9, 3), ICE, 2, cap="round")
    f.path(f"M736,{cy - 92} Q790,{cy - 108} 870,{cy - 102} Q912,{cy - 98} 930,{cy - 76} L922,{cy - 72} Q900,{cy - 92} 868,{cy - 94} "
           f"Q800,{cy - 98} 740,{cy - 86} Z", WHITE)       # snow on the roof
    f.rect(652, cy - 34, 14, 12, "#fff4e0", INK, 1.5, 3)
    for cx in (712, 930):
        f.circle(cx, cy + 2, 30, INK); f.circle(cx, cy + 2, 14, ALUMINIUM, INK, 2)
    f.path(f"M618,{cy + 34} Q820,{cy + 46} 1030,{cy + 34}", stroke="#c9d6e0", w=6, extra='stroke-linecap="round"')
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: pressure at the top, a spine down the left and three branches (liquid,
    gas, heat engine), each a box of three laws with a grey word beside each."""
    f = Fig("fy9ka-kartta", 596, "Käsitekartta. Ylhäällä solmu paine: p = F / A. Siitä lähtee alas kolme haaraa. Neste: paine syvyydellä p = p0 "
            "+ ρ g h, ylipaine ρ g h ja kokonaispaine, joka on ilmanpaine ja ylipaine yhteensä. Kaasu: tilanyhtälö p V = n "
            "R T, yhdistetty kaasulaki p V / T = vakio ja kelvinlämpötila T = θ + 273,15 K. Lämpövoimakone: kaasun työ W = "
            "p ΔV, energian säilyminen W = Q1 − Q2 ja hyötysuhde eeta = W / Q1.", width=380, size=21)
    groups = [
        ("neste", [(r"p = p_0 + \rho g h", "syvyydellä"), (r"\Delta p = \rho g h", "ylipaine"),
                   (r"p = p_0 + \Delta p", "kokonaispaine")]),
        ("kaasu", [(r"pV = nRT", "tilanyhtälö"), (r"pV/T = \text{vakio}", "sama kaasu"),
                   (r"T = \theta + 273{,}15\,\text{K}", "kelvinit")]),
        ("lämpövoimakone", [(r"W = p\,\Delta V", "kaasun työ"), (r"W = Q_1 - Q_2", "säilyminen"),
                            (r"\eta = W/Q_1", "hyötysuhde")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 150, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 21, r"\text{paine}", "middle", INK)
    f.tex(190, hub_y + 51, r"p = F/A", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 66 + j * 34
            f.tex(x_box + 14, yy, law, "start", INK)
            f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    # a tall, narrow map: cap its width so that it does not fill a wide screen (labels stay about 24 px)
    return f.svg().replace("max-width:100%", "max-width:min(100%,440px)", 1)


def rengas():
    """Two horizontal bars to scale (1 px = 1 kPa): the tyre's total pressure split into the air pressure 101 kPa and
    the gauge reading, in the warm garage (+20 °C) and after the frosty night (-20 °C)."""
    f = Fig("fy9ka-rengas", 330, f"Pylväskuvio mittakaavassa: renkaan ilman kokonaispaine kahdessa lämpötilassa. Kumpikin vaakapylväs on "
            f"jaettu kahteen osaan: ilmanpaine 101 kPa ja mittarin näyttämä ylipaine. Lämpimässä autotallissa, +20 °C, "
            f"ylipaine on 230 kPa ja kokonaispaine 331 kPa. Pakkasyön jälkeen, −20 °C, kokonaispaine on 286 kPa ja "
            f"ylipaine 185 kPa. Kokonaispaine on pienentynyt kelvinlämpötilan suhteessa, mutta mittarin lukema on "
            f"pienentynyt 45 kPa eli noin viidenneksen.", width=480, size=20)
    s, x0 = 1.0, 40                           # px per kPa
    X = lambda p: x0 + s * p
    rows = [(60, r"+20\,{}^\circ\text{C}", GAUGE_WARM, P_WARM, HOT_LIGHT, HOT), (172, r"-20\,{}^\circ\text{C}", GAUGE_COLD, P_COLD, COLD_LIGHT, COLD)]
    ybase = 268
    for t in (100, 200, 300):
        f.line(X(t), 40, X(t), ybase, RULE_LIGHT, 1.5)
    for y, label, gauge, total, light, dark in rows:
        f.tex(x0 + 10, y - 22, label, "start", dark)
        f.rect(X(0), y, s * P0, 46, SAND_LIGHT, INK, 2)
        f.rect(X(P0), y, s * gauge, 46, light, INK, 2)
        f.tex(X(P0 / 2), y + 23, r"p_0", "middle", INK)
        f.tex(X(P0 + gauge / 2), y + 23, fr"\Delta p = {fi(round(gauge))}", "middle", INK)
        f.tex(X(total) + 8, y + 23, fi(round(total)) + r"\,\text{kPa}", "start", INK)
    f.arrow(x0 - 1, ybase, 404, ybase, INK, 2.5, 13)
    f.line(x0, ybase + 1, x0, 40, INK, 2.5)
    for t in (100, 200, 300):
        f.line(X(t), ybase, X(t), ybase + 7, INK, 2)
        f.tex(X(t), ybase + 24, fi(t), "middle", MUTED)
    f.tex(x0 - 6, ybase + 24, "0", "end", MUTED)
    f.tex(410, ybase, r"p\ (\text{kPa})", "start")
    return f.svg()


def kone():
    """The energy flows of a heat engine, arrow widths to scale (0,1 px per joule): Q1 = 1000 J from the hot source
    into the engine, W = 350 J out to the right as work, Q2 = 650 J down to the colder surroundings."""
    f = Fig("fy9ka-kone", 470, "Lämpövoimakoneen energiavirrat yhden kierroksen aikana, nuolten leveydet mittakaavassa. Ylhäällä "
            "kuuma lähde, jonka lämpötila on T1. Siitä tulee alas koneeseen leveä lämpönuoli Q1 = 1000 J. Koneesta lähtee "
            "oikealle kapea vihreä nuoli, työ W = 350 J, ja alas kylmempään ympäristöön, jonka lämpötila on T2, lämpönuoli "
            "Q2 = 650 J. Lähtevät nuolet ovat yhteensä yhtä leveät kuin tuleva nuoli.", width=420, size=20)
    s = 0.1
    cx = 150
    f.rect(16, 12, 388, 62, HOT_LIGHT, HOT, 2.5, 12)
    f.tex(210, 43, r"\text{kuuma lähde } T_1", "middle", INK)
    ex, ey, ew, eh = cx - 70, 196, 140, 84             # the engine
    f.block_arrow(cx, 74, cx, ey, HEAT_LIGHT, shaft=s * Q1, head=s * Q1 + 26, headlen=24)
    f.tex(cx + s * Q1 / 2 + 22, 132, r"Q_1 = 1000\,\text{J}", "start", HEAT)
    f.rect(ex, ey, ew, eh, ALUMINIUM, INK, 3, 14)
    f.tex(cx, ey + eh / 2, r"\text{kone}", "middle", INK)
    xq2 = cx - s * W / 2                                 # Q2 leaves the left part of the engine's base, W its right side
    f.block_arrow(xq2, ey + eh, xq2, 392, HEAT_LIGHT, shaft=s * Q2, head=s * Q2 + 26, headlen=24)
    f.tex(xq2 + s * Q2 / 2 + 22, 340, r"Q_2 = 650\,\text{J}", "start", HEAT)
    f.block_arrow(ex + ew, ey + eh / 2, 330, ey + eh / 2, GOOD, shaft=s * W, head=s * W + 22, headlen=22)
    f.tex(ex + ew + 10, ey + eh / 2 - 38, r"W = 350\,\text{J}", "start", GOOD)
    f.rect(16, 394, 388, 62, COLD_LIGHT, COLD, 2.5, 12)
    f.tex(210, 425, r"\text{kylmempi ympäristö } T_2", "middle", INK)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "rengas": rengas, "kone": kone}
