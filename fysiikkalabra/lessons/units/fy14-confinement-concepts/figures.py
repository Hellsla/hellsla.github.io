"""Figures of the unit fy14-confinement-concepts (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-confinement-concepts` writes them into content/en/units/fy14-confinement-concepts/unit.md. English, decimal point.
Colours: magnetic field green #2b8a3e (⊙ out of / ⊗ into the page), force red #c92a2a, electric current violet #7048e8
(as in the course's reactors explorer). NIF energies from LLNL (5 Dec 2022: 2.05 MJ laser, 3.15 MJ fusion) and the
electricity drawn for that shot, about 300 MJ (Wikipedia, National Ignition Facility), checked 2026-11-01."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, PAPER, SAND, SAND_LIGHT, COPPER, n)
import herolib as H

figlib.set_language({}, ".")

F_COL, B_COL, I_COL = "#c92a2a", "#2b8a3e", "#7048e8"
PLASMA, PLASMA_LIGHT = "#e64980", "#fcc2d7"
LASER = "#2f9e44"
E_GRID, E_LASER, E_FUSION = 300.0, 2.05, 3.15


def odot(f, x, y, r=9):
    f.circle(x, y, r, WHITE, B_COL, 2.2); f.circle(x, y, 2.6, B_COL)


def otimes(f, x, y, r=9):
    f.circle(x, y, r, WHITE, B_COL, 2.2)
    d = r * 0.68
    f.line(x - d, y - d, x + d, y + d, B_COL, 2.2); f.line(x - d, y + d, x + d, y - d, B_COL, 2.2)


def hero():
    """Opening illustration: a path that splits into three, each leading to a different kind of fusion machine: a
    spherical target chamber with converging laser beams, a compact spherical tokamak, and a long straight tube with
    ring coils. No words."""
    f = H.hero("fy14cc-hero", "Illustration: a road on warm paper splits into three paths. The left path leads to a large "
               "metal sphere into which many thin green laser beams converge on a tiny bright point in its centre. The middle "
               "path leads to a compact, almost round machine shaped like a cored apple, with a pink glow inside. The right "
               "path leads to a long straight glass tube wrapped in copper-coloured ring coils. Small signposts stand at the fork, "
               "without any words.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 430, 1200, 170, SAND_LIGHT)
    # the road and the fork
    f.path("M520,600 L680,600 L640,470 L560,470 Z", SAND)
    for path in ("M560,470 Q470,420 250,400 L230,420 Q470,440 575,490 Z", "M585,470 L590,410 L610,410 L615,470 Z", "M640,470 Q730,420 950,400 L970,420 Q730,440 625,490 Z"):
        f.path(path, SAND)
    f.rect(596, 470, 8, 70, COPPER)
    for k, (x1, y1, a) in enumerate(((596, 478, -1), (604, 494, 1), (596, 510, -1))):
        f.path(f"M{x1},{y1} l{a * 46},0 l{a * 10},8 l{-a * 10},8 l{-a * 46},0 Z", WHITE, INK, 2)
    # left: laser target chamber
    cx, cy = 210, 260
    for k in range(10):
        a = math.radians(-160 + 140 * k / 9)
        f.line(cx + 250 * math.cos(a), cy + 250 * math.sin(a) * 0.9, cx, cy, LASER, 3)
    f.circle(cx, cy, 120, ALUMINIUM, INK, 4)
    f.circle(cx, cy, 96, "#dde2e6", METAL_EDGE, 2)
    for k in range(12):
        a = 2 * math.pi * k / 12
        f.circle(cx + 108 * math.cos(a), cy + 108 * math.sin(a), 9, IRON, INK, 1.5)
    for k in range(10):
        a = math.radians(-160 + 140 * k / 9)
        f.line(cx + 96 * math.cos(a), cy + 96 * math.sin(a), cx, cy, LASER, 2)
    f.add(f'<circle cx="{cx}" cy="{cy}" r="22" fill="{HEAT_LIGHT}" fill-opacity="0.6"/>')
    f.circle(cx, cy, 8, WHITE)
    f.rect(cx - 60, cy + 120, 120, 50, IRON, INK, 2, 4)
    # middle: spherical tokamak (cored apple)
    mx, my = 600, 250
    f.add(f'<ellipse cx="{mx}" cy="{my}" rx="128" ry="136" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="4"/>')
    f.add(f'<ellipse cx="{mx}" cy="{my}" rx="104" ry="112" fill="#3d4852"/>')
    f.add(f'<ellipse cx="{mx}" cy="{my}" rx="86" ry="96" fill="{PLASMA}" fill-opacity="0.45"/>')
    f.add(f'<ellipse cx="{mx}" cy="{my}" rx="62" ry="78" fill="{PLASMA_LIGHT}" fill-opacity="0.55"/>')
    f.rect(mx - 16, my - 150, 32, 300, COPPER, INK, 3, 6)
    for dy in (-118, 118):
        f.add(f'<ellipse cx="{mx}" cy="{my + dy}" rx="150" ry="16" fill="none" stroke="{HEAT}" stroke-width="10"/>')
    f.rect(mx - 70, my + 140, 140, 40, IRON, INK, 2, 4)
    # right: long tube with ring coils
    tx, ty = 990, 260
    f.add(f'<rect x="{tx - 170}" y="{ty - 46}" width="340" height="92" rx="46" fill="{GLASS}" fill-opacity="0.6" stroke="{METAL_EDGE}" stroke-width="4"/>')
    f.rect(tx - 160, ty - 14, 320, 28, PLASMA_LIGHT, rx=14)
    for k in range(9):
        x = tx - 140 + k * 35
        f.add(f'<ellipse cx="{x}" cy="{ty}" rx="11" ry="64" fill="none" stroke="{COPPER}" stroke-width="10"/>')
    for x in (tx - 130, tx + 130):
        f.rect(x - 10, ty + 64, 20, 90, IRON)
    return f.svg()


def pinches():
    """Z-pinch and theta-pinch: where the current flows, where its magnetic field points, and the inward force."""
    f = Fig("fy14cc-pinch", 400, "Two diagrams, one above the other. Top, Z-pinch: a horizontal column of plasma carries a "
            "violet current I to the right. Above the column its magnetic field points out of the page (green dotted circles), "
            "below it into the page (green crossed circles): the field circles the column. Red force arrows on the top and bottom "
            "surfaces point inward, squeezing the column. Bottom, theta-pinch: a coil wound around a tube carries a current around "
            "it; inside, a green magnetic field arrow points along the axis, and red arrows squeeze the plasma inward from all sides.")
    f.tex(14, 22, r"\text{Z-pinch}", "start")
    y0 = 110
    f.rect(70, y0 - 28, 460, 56, PLASMA_LIGHT, PLASMA, 2.5, 28)
    f.arrow(110, y0, 500, y0, I_COL, 4, 16); f.tex(300, y0 + 4, r"I", "middle", color=I_COL, bg=True)
    for x in range(100, 520, 70):
        odot(f, x, y0 - 52); otimes(f, x, y0 + 52)
    for x in (135, 275, 415):
        f.arrow(x, y0 - 82, x, y0 - 32, F_COL, 4, 14)
        f.arrow(x, y0 + 82, x, y0 + 32, F_COL, 4, 14)
    f.tex(548, y0 - 52, r"\overline{B}", "start", color=B_COL)
    f.tex(423, y0 - 70, r"\overline{F}", "start", color=F_COL, bg=True)
    f.tex(14, 222, r"\text{theta-pinch}", "start")
    y1 = 310
    f.add(f'<rect x="60" y="{y1 - 44}" width="480" height="88" rx="44" fill="{GLASS}" stroke="{METAL_EDGE}" stroke-width="3"/>')
    f.rect(100, y1 - 18, 400, 36, PLASMA_LIGHT, PLASMA, 2.5, 18)
    for k in range(10):
        x = 92 + k * 46
        f.add(f'<ellipse cx="{x}" cy="{y1}" rx="9" ry="56" fill="none" stroke="{I_COL}" stroke-width="5"/>')
    f.arrow(196, y1 - 70, 236, y1 - 62, I_COL, 3, 12)
    f.tex(244, y1 - 82, r"I\ \text{around the tube}", "start", color=I_COL)
    f.arrow(180, y1, 420, y1, B_COL, 4, 16); f.tex(430, y1 + 2, r"\overline{B}", "start", color=B_COL, bg=True)
    for x in (207, 345):
        f.arrow(x, y1 - 66, x, y1 - 22, F_COL, 4, 14)
        f.arrow(x, y1 + 66, x, y1 + 22, F_COL, 4, 14)
    return f.svg()


def icf():
    """Inertial confinement with indirect drive in four steps."""
    f = Fig("fy14cc-icf", 300, "Four panels in a row. One: laser beams, green, enter a small gold cylinder, the hohlraum, through "
            "its two ends; a tiny fuel capsule sits in its centre. Two: the hot inner wall of the cylinder gives off X-rays, drawn "
            "as orange wavy arrows towards the capsule. Three: the outer layer of the capsule boils away outward and pushes the "
            "rest inward: red arrows point to the centre. Four: the compressed fuel in the centre ignites, a bright spot, before "
            "it can fly apart.")
    xs = [75, 225, 375, 525]
    titles = [r"\text{1. lasers}", r"\text{2. X-rays}", r"\text{3. implosion}", r"\text{4. ignition}"]
    for k, (x, t) in enumerate(zip(xs, titles)):
        f.tex(x, 26, t, "middle")
        f.rect(x - 70, 50, 140, 190, "#fbfaf6", RULE, 2, 10)
    cy = 145
    for x in xs[:2]:
        f.rect(x - 34, cy - 56, 68, 112, SAND_LIGHT, "#b08900", 3, 6)
        f.rect(x - 28, cy - 50, 56, 100, "#fff9db")
        f.circle(x, cy, 12, COLD_LIGHT, COLD, 2)
    for dy in (-30, 30):
        for s in (-1, 1):
            f.line(xs[0] + s * 66, cy - s * 0 + dy * 2.2, xs[0] + s * 20, cy + dy * 0.6, LASER, 3)
    for a in range(8):
        ang = 2 * math.pi * a / 8
        x0, y0 = xs[1] + 26 * math.cos(ang), cy + 44 * math.sin(ang)
        x1, y1 = xs[1] + 16 * math.cos(ang), cy + 16 * math.sin(ang)
        f.line(x0, y0, x1, y1, HEAT, 2.5)
    f.circle(xs[2], cy, 34, COLD_LIGHT, COLD, 2.5)
    for a in range(8):
        ang = 2 * math.pi * a / 8
        f.arrow(xs[2] + 34 * math.cos(ang), cy + 34 * math.sin(ang), xs[2] + 14 * math.cos(ang), cy + 14 * math.sin(ang), F_COL, 3, 10)
        f.line(xs[2] + 40 * math.cos(ang), cy + 40 * math.sin(ang), xs[2] + 56 * math.cos(ang), cy + 56 * math.sin(ang), MUTED, 2, "4 4")
    f.add(f'<circle cx="{xs[3]}" cy="{cy}" r="40" fill="{HEAT_LIGHT}" fill-opacity="0.45"/>')
    f.circle(xs[3], cy, 18, HEAT_LIGHT, HEAT, 2.5)
    f.circle(xs[3], cy, 7, WHITE)
    f.tex(300, 274, r"\text{a few billionths of a second}", "middle", color=MUTED)
    return f.svg()


def energy():
    """The energy of NIF's first ignition shot, to scale: electricity drawn, laser energy on target, fusion energy."""
    f = Fig("fy14cc-energy", 270, "Horizontal bar chart to scale, in megajoules, for NIF's shot of 5 December 2022. Electricity "
            "drawn from the grid to fire the lasers: about 300 MJ, a bar across almost the whole width. Laser energy delivered to "
            "the target: 2.05 MJ, a sliver less than one percent as long. Fusion energy released: 3.15 MJ, a slightly longer "
            "sliver. The target gain is 3.15 MJ divided by 2.05 MJ, about 1.5.")
    x0, x1 = 220, 560
    X = lambda e: x0 + e / E_GRID * (x1 - x0)
    for e in (0, 100, 200, 300):
        f.line(X(e), 30, X(e), 196, RULE_LIGHT, 1.5)
        f.tex(X(e), 214, f"{e}", "middle")
    f.tex(x1 + 20, 244, r"E\ (\text{MJ})", "end")
    rows = ((r"\text{electricity}", E_GRID, IRON, r"\approx 300\ \text{MJ}"), (r"\text{laser on target}", E_LASER, LASER, r"2.05\ \text{MJ}"),
            (r"\text{fusion energy}", E_FUSION, HEAT, r"3.15\ \text{MJ}"))
    for k, (name, e, col, val) in enumerate(rows):
        y = 54 + k * 56
        f.tex(x0 - 10, y, name, "end")
        f.rect(x0, y - 16, max(6, X(e) - x0), 32, col, rx=2)
        if e > 100: f.tex(X(e) - 10, y, val, "end", color=WHITE)
        else: f.tex(X(e) + 10, y, val, "start", bg=True)
    return f.svg()


def aspect():
    """Cross-sections of a conventional and a spherical tokamak with the same plasma minor radius a: aspect ratio R/a."""
    f = Fig("fy14cc-aspect", 300, "Two cross-sections side by side, each showing the central column on the left and the D-shaped "
            "plasma on the right. Left, conventional tokamak: the plasma's centre is far from the machine's axis, major radius R "
            "about three times the minor radius a, so the ring is like a doughnut. Right, spherical tokamak: the plasma's centre "
            "is close to the axis, R less than twice a, so the ring is like a cored apple, with a narrow central column.")
    def section(ox, R, a, k, label):
        f.line(ox, 40, ox, 250, MUTED, 2, "8 6")
        f.rect(ox - 10, 50, 20, 190, COPPER, INK, 2, 4)
        for s in (-1, 1):
            pts = [(ox + R + a * math.cos(t + 0.35 * math.sin(t)), 150 - k * a * math.sin(t)) for t in [2 * math.pi * i / 80 for i in range(81)]]
            f.path("M" + " L".join(f"{n(px)},{n(py)}" for px, py in pts) + " Z", PLASMA_LIGHT, PLASMA, 2.5)
            break
        f.circle(ox + R, 150, 4, INK)
        f.line(ox, 262, ox + R, 262, INK, 2); f.line(ox, 256, ox, 268, INK, 2); f.line(ox + R, 256, ox + R, 268, INK, 2)
        f.tex(ox + R / 2, 284, "R", "middle", bg=True)
        f.line(ox + R, 150, ox + R + a, 150, INK, 2)
        f.tex(ox + R + a / 2, 128, "a", "middle", bg=True)
        f.tex(ox + (R + a) / 2, 22, label, "middle")
    section(40, 150, 46, 1.7, r"\text{conventional}")
    section(370, 100, 58, 1.75, r"\text{spherical}")
    return f.svg()


FIGURES = {"hero": hero, "pinch": pinches, "icf": icf, "energy": energy, "aspect": aspect}
