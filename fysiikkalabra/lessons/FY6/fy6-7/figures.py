"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-7` writes them into lesson.md.
Energy as the area under a (t, P) graph in the energy colours (#ffc078 -> #e8590c), the kilowatt-hour as a 1 kW heater
running for 1 h, a washing machine's power programme for a task; every label LaTeX. The opening illustration is a
cut-away home on a winter evening: sauna, kitchen and living room with their electrical devices."""
import math
from figlib import Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, \
    COLD_LIGHT, GLASS, ICE, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN, PAPER
import herolib as H

ENERGY = "fy67-energy"


def energy_grad(f, gid=ENERGY, vertical=True):
    x2, y2 = ("0", "1") if vertical else ("1", "0")
    f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{HEAT}"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}"/></linearGradient>')
    return f"url(#{gid})"


# --- Ydinajatus: the same energy from a large power for a short time and a small power for a long time ------------
def power_time():
    f = Fig("fy67-pt", 360, "Kuvaaja mittakaavassa: teho P kilowatteina ajan t funktiona tunteina. Vedenkeittimen teho on 2,0 kW "
            "ajan 0–0,10 h, joten sen alue on kapea ja korkea suorakulmio. Television teho on 0,10 kW ajan 0–2,0 h, joten sen "
            "alue on leveä ja matala suorakulmio. Kummankin suorakulmion pinta-ala on 0,20 kWh: sama energia.")
    fill = energy_grad(f)
    ax = Axes(f, (84, 300), (468, 64), x=(0, 2.5), y=(0, 2.5), xticks=[0.5, 1, 1.5, 2, 2.5], yticks=[0.5, 1, 1.5, 2, 2.5],
              xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: fi(v) if v in (1, 2) else ("" if v == 2.5 else fi(v)),
              yfmt=lambda v: fi(v) if v in (1, 2) else ("" if v == 2.5 else fi(v)))
    # television: 0,10 kW for 2,0 h
    f.rect(ax.X(0), ax.Y(0.10), ax.X(2.0) - ax.X(0), ax.Y(0) - ax.Y(0.10), fill, INK, 2)
    # kettle: 2,0 kW for 0,10 h
    f.rect(ax.X(0), ax.Y(2.0), ax.X(0.10) - ax.X(0), ax.Y(0) - ax.Y(2.0), fill, INK, 2)
    f.tex(ax.X(0.10) + 14, ax.Y(2.0) - 2, r"\text{vedenkeitin}", "start", w=150, bg=True)
    f.tex(ax.X(0.10) + 14, ax.Y(2.0) + 30, r"E = 0{,}20\,\text{kWh}", "start", w=170, bg=True)
    f.tex(ax.X(1.0), ax.Y(0.10) - 50, r"\text{televisio}", "middle", w=130, bg=True)
    f.tex(ax.X(1.0), ax.Y(0.10) - 20, r"E = 0{,}20\,\text{kWh}", "middle", w=170, bg=True)
    return f.svg()


# --- Kaava: one kilowatt-hour -------------------------------------------------------------------------------------
def radiator(f, x, y, w, h):
    """An electric radiator standing on its feet at y (bottom), x left edge."""
    fins = 6
    fw = w / fins
    for k in range(fins):
        f.rect(x + k * fw + 2, y - h, fw - 4, h - 14, H.grad(f, f"fy67-fin{k}", WHITE, ALUMINIUM, horizontal=True), INK, 2.5, 8)
    f.rect(x - 4, y - h + 18, w + 8, 10, ALUMINIUM, INK, 2, 3)
    f.rect(x - 4, y - 38, w + 8, 10, ALUMINIUM, INK, 2, 3)
    f.rect(x + 8, y - 14, 10, 14, IRON, INK, 2, 2)
    f.rect(x + w - 18, y - 14, 10, 14, IRON, INK, 2, 2)
    f.circle(x + w - 14, y - h + 46, 7, HOT, INK, 2)


def clock(f, cx, cy, r):
    f.circle(cx, cy, r, WHITE, INK, 3)
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r - 8:g}" fill="{COLD}" fill-opacity="0.18"/>')
    for k in range(12):
        b = k * math.pi / 6
        f.line(cx + (r - 12) * math.sin(b), cy - (r - 12) * math.cos(b), cx + (r - 4) * math.sin(b), cy - (r - 4) * math.cos(b),
               INK if k % 3 == 0 else MUTED, 3 if k % 3 == 0 else 2)
    f.line(cx, cy, cx, cy - (r - 18), INK, 4, cap="round")
    f.line(cx, cy, cx + (r - 30) * math.sin(math.pi / 3), cy - (r - 30) * math.cos(math.pi / 3), INK, 5, cap="round")
    f.circle(cx, cy, 5, INK)
    # a curved arrow: one full turn of the minute hand
    a0, a1 = -math.pi / 2 + 0.35, -math.pi / 2 + 2 * math.pi - 0.55
    R = r + 12
    pts = [(cx + R * math.cos(a0 + (a1 - a0) * i / 40), cy + R * math.sin(a0 + (a1 - a0) * i / 40)) for i in range(41)]
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{COLD}" stroke-width="3"/>')
    tx, ty = cx + R * math.cos(a1 + 0.3), cy + R * math.sin(a1 + 0.3)
    bx1, by1 = cx + (R - 9) * math.cos(a1), cy + (R - 9) * math.sin(a1)
    bx2, by2 = cx + (R + 9) * math.cos(a1), cy + (R + 9) * math.sin(a1)
    f.path(f"M{n(tx)},{n(ty)} L{n(bx1)},{n(by1)} L{n(bx2)},{n(by2)} Z", COLD)


def meter(f, x, y, w, h):
    """An electricity meter: a grey box with a black counter window."""
    f.rect(x, y, w, h, H.grad(f, "fy67-meter", WHITE, ALUMINIUM), INK, 3, 10)
    f.rect(x + 14, y + 22, w - 28, 40, INK, None, 0, 4)
    for k in range(5):
        f.rect(x + 20 + k * (w - 40) / 5, y + 28, (w - 40) / 5 - 4, 28, GOOD_LIGHT if k < 4 else HEAT_LIGHT, None, 0, 2)
    f.circle(x + w / 2, y + 92, 8, HOT, INK, 2)
    f.rect(x + 22, y + h - 26, w - 44, 10, IRON, INK, 1.5, 3)


def kwh():
    f = Fig("fy67-kwh", 360, "Kaavakuva, ei mittakaavassa: vasemmalla sähköpatteri, jonka teho on 1 kW, ja sen yläpuolella oransseja "
            "lämpönuolia. Keskellä kello, jonka minuuttiosoitin kiertää kerran ympäri eli 1 tunnin. Oikealla sähkömittari, jonka "
            "lukema kasvaa 1 kilowattitunnin. Kuvan alla: 1 kWh = 1000 W · 3600 s = 3,6 MJ.")
    fill = energy_grad(f, "fy67-heatup")
    radiator(f, 40, 250, 132, 150)
    for k, x in enumerate((60, 106, 152)):
        f.block_arrow(x, 92, x, 34, fill, 12, 26, 18)
    f.tex(106, 280, r"P = 1\,\text{kW}", "middle", w=150)
    f.tex(214, 166, r"\cdot", "middle", w=30, size=40)
    clock(f, 302, 166, 62)
    f.tex(302, 280, r"t = 1\,\text{h}", "middle", w=130)
    f.tex(400, 166, r"=", "middle", w=30, size=34)
    meter(f, 440, 82, 132, 168)
    f.tex(506, 280, r"E = 1\,\text{kWh}", "middle", w=160)
    f.line(30, 308, 570, 308, RULE, 1.5, "6 5")
    f.tex(300, 334, r"1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}", "middle", w=520)
    return f.svg()


# --- task figure: a washing machine's power during one programme ----------------------------------------------
def washer():
    f = Fig("fy67-washer", 350, "Kuvaaja mittakaavassa: pesukoneen teho P kilowatteina ajan t funktiona tunteina yhden pesuohjelman "
            "aikana. Pystyakselin ruudukon väli on 0,2 kW ja vaaka-akselin 0,25 h. Teho on ensin 2,0 kW ajan 0–0,25 h, sitten "
            "0,2 kW ajan 0,25–1,25 h ja lopuksi 0,4 kW ajan 1,25–1,5 h, minkä jälkeen kone sammuu.")
    yt = [0.2 * k for k in range(1, 13)]
    ax = Axes(f, (84, 296), (470, 66), x=(0, 1.75), y=(0, 2.4), xticks=[0.25 * k for k in range(1, 8)], yticks=yt,
              xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: fi(v) if abs(v * 2 - round(v * 2)) < 1e-9 and v < 1.7 else "",
              yfmt=lambda v: fi(round(v, 1)) if abs(v / 0.4 - round(v / 0.4)) < 1e-9 and v < 2.3 else "")
    ax.line([(0, 2.0), (0.25, 2.0), (0.25, 0.2), (1.25, 0.2), (1.25, 0.4), (1.5, 0.4), (1.5, 0)], HEAT, 3)
    f.tex(ax.X(0.25) + 12, ax.Y(2.0), r"\text{lämmitys}", "start", w=130)
    f.tex(ax.X(0.75), ax.Y(0.2) - 26, r"\text{pesu}", "middle", w=80)
    f.tex(ax.X(1.375), ax.Y(0.4) - 26, r"\text{linkous}", "middle", w=110)
    return f.svg()


# --- task figure: a tumble dryer's power during one programme (variant of the washer figure) -------------------
def dryer():
    f = Fig("fy67-dryer", 350, "Kuvaaja mittakaavassa: kuivausrummun teho P kilowatteina ajan t funktiona tunteina yhden kuivausohjelman "
            "aikana. Pystyakselin ruudukon väli on 0,4 kW ja vaaka-akselin 0,25 h. Teho on ensin 2,4 kW ajan 0–0,5 h, sitten "
            "1,2 kW ajan 0,5–1,5 h ja lopuksi 0,2 kW ajan 1,5–2,0 h, minkä jälkeen kone sammuu.")
    yt = [0.4 * k for k in range(1, 7)]
    ax = Axes(f, (84, 296), (470, 66), x=(0, 2.25), y=(0, 2.8), xticks=[0.25 * k for k in range(1, 9)], yticks=yt,
              xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: fi(v) if abs(v * 2 - round(v * 2)) < 1e-9 and v < 2.1 else "",
              yfmt=lambda v: fi(round(v, 1)))
    ax.line([(0, 2.4), (0.5, 2.4), (0.5, 1.2), (1.5, 1.2), (1.5, 0.2), (2.0, 0.2), (2.0, 0)], HEAT, 3)
    f.tex(ax.X(0.5) + 12, ax.Y(2.4), r"\text{kuumennus}", "start", w=130)
    f.tex(ax.X(1.0), ax.Y(1.2) - 26, r"\text{kuivaus}", "middle", w=100)
    f.tex(ax.X(1.75), ax.Y(0.2) - 26, r"\text{jäähdytys}", "middle", w=110)
    return f.svg()


# --- opening illustration: a home on a winter evening ---------------------------------------------------------
def hero():
    f = H.hero("fy67-hero", "Kuvitus: talvi-ilta ja leikkauskuva omakotitalosta. Vasemmalla saunassa hehkuu sähkökiuas, keskellä "
               "keittiössä höyryää vedenkeitin jääkaapin vieressä ja kattovalaisin palaa, oikealla olohuoneessa on televisio ja "
               "lattiavalaisin. Talon ulkoseinällä on sähkömittari, ja ulkona on lunta.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy67h-sky", COLD, ICE, y1=0, y2=470))
    for k in range(26):
        x, y = 30 + H.rnd(k, 3) * 1140, 20 + H.rnd(k, 5) * 150
        if 140 < x < 1060 and y > 60: continue
        f.circle(x, y, 2 + H.rnd(k, 7) * 2, WHITE)
    f.circle(1110, 70, 34, WHITE)
    f.circle(1124, 62, 30, H.grad(f, "fy67h-moon", COLD, ICE, y1=30, y2=100))
    # snow
    f.path("M0,470 Q300,450 600,468 T1200,462 V600 H0 Z", WHITE)
    f.path("M0,520 Q380,500 760,526 T1200,516 V600 H0 Z", ICE, extra='fill-opacity="0.45"')
    for x in (60, 1130):
        H.spruce(f, x, 476, 190)
    # house: roof and the cut-away walls
    L, R, T, B = 150, 1050, 200, 484
    f.path(f"M{L - 40},{T + 6} L600,64 L{R + 40},{T + 6} Z", HOT, INK, 3)
    f.path(f"M{L - 40},{T + 6} L600,64 L{R + 40},{T + 6}", stroke=WHITE, w=10, extra='stroke-linecap="round"')
    f.rect(L - 14, T, R - L + 28, B - T + 14, INK)
    rooms = [(L, 420), (436, 776), (790, R)]
    # sauna: wooden boards
    x0, x1 = rooms[0]
    f.rect(x0, T + 14, x1 - x0, B - T - 14, H.grad(f, "fy67h-wood", SAND_LIGHT, SAND_DARK))
    for x in range(x0 + 30, x1, 30): f.line(x, T + 14, x, B, SAND, 2)
    f.rect(x0, 360, 170, 22, SAND, INK, 2.5, 3); f.rect(x0, 300, 110, 20, SAND, INK, 2.5, 3)
    for x in (x0 + 20, x0 + 150): f.rect(x, 382, 12, B - 382, SAND, INK, 2)
    # electric stove with glowing stones
    kx = 344
    f.rect(kx - 52, 344, 104, B - 344, H.grad(f, "fy67h-stove", IRON, INK, horizontal=True), INK, 3, 6)
    f.circle(kx, 344, 62, H.glow(f, "fy67h-stoneglow", HEAT_LIGHT, HEAT))
    for k, (dx, dy, r) in enumerate([(-34, -6, 16), (-6, -14, 18), (24, -8, 16), (-20, -28, 14), (12, -32, 15), (40, -24, 12)]):
        f.circle(kx + dx, 344 + dy, r, IRON if k % 2 else METAL_EDGE, INK, 2)
    f.rect(kx - 40, 400, 80, 8, HOT, None, 0, 3)
    H.shimmer(f, [kx - 30, kx, kx + 30], 282, 70)
    # kitchen: tiles, cupboards, worktop, fridge, kettle, pendant lamp
    x0, x1 = rooms[1]
    f.rect(x0, T + 14, x1 - x0, B - T - 14, WHITE)
    for x in range(x0, x1 + 1, 40): f.line(x, 300, x, 382, RULE_LIGHT, 2)
    for y in range(300, 383, 40): f.line(x0, y, x1, y, RULE_LIGHT, 2)
    f.rect(x0, 382, 250, 14, SAND, INK, 2.5, 2)
    f.rect(x0 + 6, 396, 238, B - 396, WHITE, INK, 2.5, 2)
    for x in (x0 + 125,): f.line(x, 396, x, B, INK, 2)
    for x in (x0 + 105, x0 + 145): f.rect(x - 3, 420, 6, 30, METAL_EDGE, rx=3)
    # kettle on the worktop, steam rising
    ex = 556
    f.rect(ex - 40, 372, 80, 10, INK, None, 0, 3)
    f.path(f"M{ex - 34},372 L{ex - 28},314 Q{ex},304 {ex + 28},314 L{ex + 34},372 Z", H.steel(f, "fy67h-kettle"), INK, 3)
    f.path(f"M{ex + 28},320 Q{ex + 62},326 {ex + 38},366", stroke=INK, w=8, extra='stroke-linecap="round"')
    f.path(f"M{ex - 28},328 L{ex - 52},312 L{ex - 32},350 Z", H.steel(f, "fy67h-spout"), INK, 2.5)
    f.circle(ex + 22, 360, 5, HOT)
    for k in range(2):
        d = f"M{ex - 50 + k * 12},304 c-10,-16 10,-28 0,-44 s10,-28 0,-44"
        f.path(d, stroke=RULE, w=14, extra='stroke-linecap="round" stroke-opacity="0.5"'); f.path(d, stroke=WHITE, w=9, extra='stroke-linecap="round"')
    # fridge
    fx0, fx1 = 690, 770
    f.rect(fx0, 236, fx1 - fx0, B - 236, H.grad(f, "fy67h-fridge", WHITE, ALUMINIUM, horizontal=True), INK, 3, 8)
    f.line(fx0, 318, fx1, 318, INK, 2.5)
    f.rect(fx0 + 8, 256, 6, 44, METAL_EDGE, rx=3); f.rect(fx0 + 8, 336, 6, 70, METAL_EDGE, rx=3)
    # pendant lamp over the kitchen
    f.line(600, T + 14, 600, 236, INK, 3)
    f.add(f'<path d="M560,262 L470,382 H730 L640,262 Z" fill="{HEAT_LIGHT}" fill-opacity="0.28"/>')
    f.path("M572,262 Q600,226 628,262 Z", H.grad(f, "fy67h-shade", HEAT_LIGHT, HEAT), INK, 2.5)
    f.circle(600, 264, 9, H.glow(f, "fy67h-bulb", WHITE, HEAT_LIGHT))
    # living room: wall, sofa, television, floor lamp
    x0, x1 = rooms[2]
    f.rect(x0, T + 14, x1 - x0, B - T - 14, H.grad(f, "fy67h-wall", GLASS, COLD_LIGHT))
    f.rect(x0, B - 14, x1 - x0, 14, SAND, INK, 2)
    f.rect(820, 400, 120, 70, SAND, INK, 2.5, 3)
    f.rect(830, 290, 100, 96, INK, INK, 3, 4)
    f.rect(838, 298, 84, 80, H.grad(f, "fy67h-screen", COLD, COLD_LIGHT), None, 0, 2)
    f.rect(872, 386, 16, 14, INK)
    f.circle(926, 452, 4, HOT)
    f.line(1006, B - 14, 1006, 278, INK, 4); f.rect(986, B - 22, 40, 8, INK, rx=3)
    f.add(f'<path d="M984,276 L944,380 H1068 L1028,276 Z" fill="{HEAT_LIGHT}" fill-opacity="0.25"/>')
    f.path("M982,278 L992,244 H1020 L1030,278 Z", H.grad(f, "fy67h-flamp", HEAT_LIGHT, HEAT), INK, 2.5)
    # room walls between the rooms and the ceiling
    for a, b in ((420, 436), (776, 790)): f.rect(a, T, b - a, B - T, INK)
    # electricity meter on the outside wall
    f.rect(100, 330, 40, 54, H.grad(f, "fy67h-meter", WHITE, ALUMINIUM), INK, 2.5, 4)
    f.rect(106, 338, 28, 12, INK, None, 0, 2)
    f.path("M120,384 V476", stroke=INK, w=3)
    return f.svg()


FIGURES = {"hero": hero, "power-time": power_time, "kwh": kwh, "washer": washer, "dryer": dryer}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "power-time": "reveals: 2,0 kW for 0,10 h and 0,10 kW for 2,0 h are the same 0,20 kWh (energy = area)",
    "kwh": "reveals: 1 kW for 1 h is 1 kWh = 1000 W · 3600 s = 3,6 MJ",
    "washer": "safe: a washing machine's (t, P) graph, 2,0 / 0,2 / 0,4 kW in three stages, no energy written",
    "dryer": "safe: a tumble dryer's (t, P) graph, 2,4 / 1,2 / 0,2 kW in three stages, no energy written",
}
