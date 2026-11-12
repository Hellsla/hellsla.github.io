"""Figures of the unit fy14-fr-cadarache (scripts/figlib.py, scripts/herolib.py); `python3 scripts/units.py figures
fy14-fr-cadarache` writes them into unit.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, GLASS, ICE, SAND_LIGHT, SAND, SAND_DARK, HOT, IRON, COLD, GOOD, METAL_EDGE,
                    ALUMINIUM, WATER, WATER_LIGHT, RULE, RULE_LIGHT, n)
import herolib as H

OLIVE, OLIVE_DARK, OAK, STONE_LIGHT, STONE = "#9aa86a", "#6f7f45", "#55703a", "#e9e2cf", "#d6ccb2"
LAND, SEA, ROAD = "#efe6cf", "#cfe4f5", "#b8a57a"


def oak(f, x, ybase, r):
    """A round holm oak of the garrigue."""
    f.rect(x - 5, ybase - r * 0.9, 10, r * 0.9, "#6b5232")
    f.circle(x, ybase - r * 1.2, r, OAK)
    f.circle(x - r * 0.35, ybase - r * 1.45, r * 0.5, OLIVE_DARK)


def hero():
    f = H.hero("fy14frca-hero", "Illustration: a sunny morning among dry limestone hills and dark green oak trees in Provence. "
               "A long, low, modern research building with a glass front stands at the end of a road. In front of it a "
               "signpost with four blank arrow-shaped boards points in different directions. Two simple figures without "
               "faces stand by the signpost: a student with a blue shirt and a backpack, and a researcher with a green "
               "shirt and a badge.")
    H.sky(f, "frca", 600, ICE, GLASS)
    H.sun(f, "frca", 1060, 96, 48)
    H.cloud(f, 260, 74, 0.6)
    H.hills(f, "frca", 270, [STONE_LIGHT, STONE], amp=50, seed=11)
    H.hills(f, "frca2", 330, [OLIVE, OLIVE_DARK], amp=26, seed=5)
    for x, r in ((60, 34), (130, 26), (980, 30), (1050, 38), (1140, 28), (700, 22)):
        oak(f, x, 352 + (x % 7), r)
    # the research building: long and low, with a glass band and a flat roof
    f.rect(420, 240, 700, 140, WHITE, INK, 3)
    f.rect(440, 262, 660, 70, H.grad(f, "frca-glass", "#cfe4f5", "#7fb0d8"), INK, 2.5)
    for x in range(440 + 60, 1100, 60):
        f.line(x, 262, x, 332, METAL_EDGE, 3)
    f.rect(400, 226, 740, 18, ALUMINIUM, INK, 3)
    f.rect(740, 332, 80, 48, H.grad(f, "frca-door", "#a7c8e6", WATER), INK, 2.5)
    # the ground and the road leading to the entrance
    f.path("M0,380 H1200 V600 H0 Z", H.grad(f, "frca-ground", SAND_LIGHT, SAND_DARK))
    f.path("M700,380 H860 L1060,600 H420 Z", "#c9c2b2", INK, 2)
    f.line(780, 384, 740, 600, WHITE, 4, dash="26 22")
    # the signpost with blank boards (the opening illustration has no text)
    f.rect(296, 210, 12, 360, IRON, INK, 1.5)
    for y, d, w in ((236, 1, 170), (290, -1, 150), (344, 1, 140), (398, -1, 160)):
        x0 = 302
        tip = x0 + d * w
        f.path(f"M{n(x0)},{n(y - 20)} L{n(tip - d * 24)},{n(y - 20)} L{n(tip)},{n(y)} L{n(tip - d * 24)},{n(y + 20)} L{n(x0)},{n(y + 20)} Z",
               [GOOD, COLD, "#e8590c", "#6c4fa8"][(y - 236) // 54], INK, 2)
    # the student (blue, with a backpack) and the researcher (green, with a badge)
    f.rect(152, 396, 28, 74, IRON, INK, 2, 8)
    H.person(f, 210, 590, shirt=COLD, trousers=INK, sc=0.8)
    H.person(f, 440, 590, shirt=GOOD, trousers=IRON, sc=0.8)
    f.rect(450, 430, 18, 22, WHITE, INK, 1.5, 2)
    return f.svg()


# --------------------------------------------------------------------------------------------- the regional map
LON0, LON1, LAT0, LAT1 = 4.75, 6.05, 43.05, 44.0
KX = 111.32 * math.cos(math.radians(43.6))        # km per degree of longitude at 43.6° N
KY = 111.13                                       # km per degree of latitude
PX = 7.0                                          # pixels per km
W = round((LON1 - LON0) * KX * PX)
HGT = round((LAT1 - LAT0) * KY * PX)


def P(lon, lat):
    return (lon - LON0) * KX * PX, (LAT1 - lat) * KY * PX


def poly(pts):
    return " L".join(f"{n(a)},{n(b)}" for a, b in (P(*p) for p in pts))


COAST = [(4.75, 43.43), (4.88, 43.40), (4.97, 43.37), (5.05, 43.33), (5.17, 43.33), (5.30, 43.36), (5.36, 43.30),
         (5.37, 43.21), (5.45, 43.21), (5.54, 43.21), (5.61, 43.17), (5.70, 43.14), (5.80, 43.08), (5.93, 43.10), (6.05, 43.08)]
DURANCE = [(5.96, 44.0), (5.90, 43.93), (5.84, 43.86), (5.80, 43.78), (5.79, 43.72), (5.70, 43.70), (5.62, 43.70),
           (5.50, 43.68), (5.35, 43.72), (5.20, 43.75), (5.05, 43.83), (4.90, 43.90), (4.81, 43.935)]
RHONE = [(4.83, 44.0), (4.81, 43.935), (4.78, 43.86), (4.75, 43.80)]
PLACES = [  # name, lon, lat, label anchor, dx, dy
    ("Marseille", 5.370, 43.296, "start", 16, -26),
    ("Aix-en-Provence", 5.447, 43.530, "start", 16, 0),
    ("Manosque", 5.791, 43.836, "end", -16, 0),
    ("Avignon", 4.806, 43.949, "start", 16, 6),
    ("Toulon", 5.928, 43.124, "end", -14, -26),
]
ITER = (5.765, 43.704)


def map_():
    f = Fig("fy14frca-map", HGT, "Simplified map of the region around ITER, drawn to scale (scale bar 20 km). The Mediterranean "
            "Sea is at the bottom, with Marseille on the coast and Toulon further east. Aix-en-Provence lies about 25 km north of "
            "Marseille. The river Durance flows from the north-east past Manosque, then past the ITER and Cadarache site, and "
            "then west to Avignon, where it joins the Rhône. A lagoon, the Étang de Berre, lies north-west of Marseille. The ITER and Cadarache site is marked with a red star, about 35 km "
            "north of Aix-en-Provence and about 15 km south of Manosque.", width=W, size=30)
    f.rect(0, 0, W, HGT, LAND)
    f.path("M" + poly(COAST) + f" L{W},{HGT} L0,{HGT} Z", SEA, WATER, 2)
    cx, cy = P(5.10, 43.47)
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(0.08 * KX * PX)}" ry="{n(0.07 * KY * PX)}" fill="{SEA}" stroke="{WATER}" stroke-width="2"/>')
    f.path("M" + poly(DURANCE), stroke=WATER, w=6)
    f.path("M" + poly(RHONE), stroke=WATER, w=8)
    for name, lon, lat, anchor, dx, dy in PLACES:
        x, y = P(lon, lat)
        f.circle(x, y, 9, INK)
        f.tex(x + dx, y + dy, r"\text{" + name + "}", anchor)
    x, y = P(*ITER)
    pts = []
    for k in range(10):
        r = 22 if k % 2 == 0 else 9
        a = -math.pi / 2 + k * math.pi / 5
        pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", HOT, INK, 1.5)
    f.tex(x + 10, y + 40, r"\text{ITER et Cadarache}", "end", color=HOT)
    f.tex(*P(5.30, 43.12), r"\text{mer Méditerranée}", "middle", color=WATER)
    lx, ly = P(5.24, 43.90)
    f.tex(lx, ly + 34, r"\text{la Durance}", "middle", color=WATER)
    f.tex(22, 148, r"\text{le Rhône}", "start", color=WATER)
    # light correction (teacher 2026-11-11, illustration audit): the name clear of the lagoon's outline, not on it
    f.tex(cx, cy - 0.07 * KY * PX - 30, r"\text{l'étang de Berre}", "middle", color=WATER)
    # scale bar and north arrow
    x0, y0 = 40, HGT - 70
    f.rect(x0, y0, 20 * PX, 10, INK)
    f.tex(x0 + 10 * PX, y0 + 36, r"20\ \text{km}", "middle")
    f.arrow(W - 190, HGT - 40, W - 190, HGT - 130, INK, 4, 20)
    f.tex(W - 190, HGT - 158, r"\text{N}", "middle")
    return f.svg()


# --------------------------------------------------------------------------------------------- the building plan
def plan():
    f = Fig("fy14frca-plan", 940, "Plan of the ground floor of an invented research building. The entrance is at the bottom "
            "in the middle. Just inside is the reception desk with a star: you are here, facing a long corridor that runs "
            "straight up. On the left of the corridor, first comes the cafeteria and then the library. On the right, first "
            "comes the lift and then the toilets, opposite the library. At the end of the corridor is the conference room. "
            "A separate strip below the plan shows the first floor, one level up by the lift, where the laboratory is.",
            width=800, size=32)
    wall, room, corr = INK, "#fbf8f1", "#eee6d3"
    f.rect(20, 20, 760, 660, room, wall, 4)
    f.rect(300, 140, 200, 540, corr)                                  # the corridor
    f.rect(20, 20, 760, 120, "#e3eef8", wall, 3)                      # conference room
    f.tex(400, 80, r"\text{la salle de conférence}", "middle")
    f.rect(20, 140, 280, 230, "#e6f2e1", wall, 3)                      # library (left, far)
    f.tex(160, 255, r"\text{la bibliothèque}", "middle")
    f.rect(20, 370, 280, 210, "#fdebd3", wall, 3)                      # cafeteria (left, near)
    f.tex(160, 475, r"\text{la cafétéria}", "middle")
    f.rect(500, 140, 280, 260, "#eef0f3", wall, 3)                     # toilets (right, far)
    f.tex(640, 270, r"\text{les toilettes}", "middle")
    f.rect(500, 400, 280, 180, "#e9e4f4", wall, 3)                     # lift (right, near)
    f.tex(640, 460, r"\text{l'ascenseur}", "middle")
    f.arrow(640, 548, 640, 500, INK, 4, 16)                            # the lift goes up
    # doors: gaps in the corridor walls
    for x, y in ((300, 520), (300, 300), (500, 500), (500, 300)):
        f.line(x, y - 30, x, y + 30, corr, 8)
    f.line(370, 140, 430, 140, corr, 8)
    # reception desk, star and entrance
    f.rect(330, 600, 140, 34, "#d9b26a", INK, 2)
    f.tex(400, 576, r"\text{l'accueil}", "middle")
    xs, ys = 400, 660
    pts = []
    for k in range(10):
        r = 16 if k % 2 == 0 else 7
        a = -math.pi / 2 + k * math.pi / 5
        pts.append((xs + r * math.cos(a), ys + r * math.sin(a)))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", HOT, INK, 1.5)
    f.line(350, 680, 450, 680, room, 10)
    f.tex(400, 712, r"\text{l'entrée}", "middle")
    f.tex(400, 330, r"\text{le couloir}", "middle")
    # the first floor, one level up
    f.rect(20, 770, 760, 150, "#f4f0fa", wall, 3)
    f.tex(40, 800, r"\text{au premier étage}", "start", color=MUTED)
    f.rect(500, 770, 280, 150, "#e9e4f4", wall, 3)
    f.tex(640, 845, r"\text{l'ascenseur}", "middle")
    f.rect(40, 826, 420, 80, "#e1f0f5", wall, 2.5)
    f.tex(250, 866, r"\text{le laboratoire}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "map": map_, "plan": plan}
