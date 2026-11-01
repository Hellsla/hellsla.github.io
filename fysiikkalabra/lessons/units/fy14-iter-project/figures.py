"""Figures of the unit fy14-iter-project (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-iter-project` writes them into content/en/units/fy14-iter-project/unit.md. English: the decimal sign is a point.
The schedule figure draws the milestones of ITER's 2016 and 2024 baselines (ITER baseline press conference summary,
3 July 2024) on one year axis, to scale."""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GOOD, GOOD_LIGHT, n)
import herolib as H

figlib.set_language({}, ".")

OLIVE, OLIVE_DARK, LAVENDER, LAVENDER_DARK = "#8f9d5a", "#5f6b3a", "#b197fc", "#7048e8"


def cypress(f, x, ybase, h):
    """A tall, narrow Provençal cypress."""
    f.path(f"M{n(x)},{n(ybase - h)} Q{n(x + h * 0.16)},{n(ybase - h * 0.55)} {n(x + h * 0.09)},{n(ybase)} "
           f"H{n(x - h * 0.09)} Q{n(x - h * 0.16)},{n(ybase - h * 0.55)} {n(x)},{n(ybase - h)} Z", OLIVE_DARK, INK, 2)
    f.add(f'<path d="M{n(x)},{n(ybase - h)} Q{n(x + h * 0.16)},{n(ybase - h * 0.55)} {n(x + h * 0.09)},{n(ybase)} H{n(x)} Z" fill="{INK}" fill-opacity="0.18"/>')


def crane(f, x, ybase, h, jib_left, jib_right, hook_x, hook_y):
    """A tower crane: a lattice mast, a jib, a counter-jib with its weight and a hook on a cable."""
    top = ybase - h
    f.rect(x - 10, top, 20, h, "none", HEAT, 4)
    for k in range(int(h // 30)):
        y = top + k * 30
        f.line(x - 10, y, x + 10, y + 30, HEAT, 2.5)
    f.rect(x - jib_left, top - 14, jib_left + jib_right, 14, HEAT, INK, 2)
    f.rect(x - jib_left + 6, top, 40, 26, IRON, INK, 2)
    f.path(f"M{n(x)},{n(top - 14)} L{n(x)},{n(top - 52)} L{n(x + jib_right * 0.8)},{n(top - 14)} M{n(x)},{n(top - 52)} L{n(x - jib_left * 0.7)},{n(top - 14)}", stroke=INK, w=2)
    f.line(hook_x, top, hook_x, hook_y, INK, 2)
    f.path(f"M{n(hook_x - 6)},{n(hook_y)} h12 v8 q-6,10 -12,0 Z", INK)


def hero():
    """Opening illustration: the ITER construction site in the hills of Provence: the tall concrete building with
    cranes over it, the assembly hall beside it, lavender and olive trees, cypresses, and one road with a heavy
    convoy carrying a large crate towards the site. No text."""
    f = H.hero("fy14ip-hero", "Illustration: a sunny landscape of low, dry hills with cypress trees, olive trees and rows of "
               "lavender. On a flat platform in the middle stands a very large grey concrete building, taller than all the "
               "trees, with a lower assembly hall beside it. Two orange tower cranes reach over the roofs. In front, a road "
               "winds out of the hills, and a long, slow transport vehicle on many wheels carries a huge covered crate "
               "towards the site.")
    H.sky(f, "fy14ip", 600, "#a5d8ff", "#eef5f9")
    H.sun(f, "fy14ip", 1080, 92, 46)
    H.cloud(f, 250, 110, 0.9)
    H.cloud(f, 760, 70, 0.6)
    H.hills(f, "fy14ip", 330, ["#c9c7a3", "#b5b98a", "#a3ac77"], amp=46, seed=3)
    # the platform
    f.path("M300,420 L980,420 L1040,462 L250,462 Z", SAND_LIGHT, INK, 2)
    # the tokamak building: tall block, the assembly hall to its left
    f.rect(330, 300, 240, 130, ALUMINIUM, INK, 2.5)
    for k in range(5):
        f.line(330 + 48 * (k + 1), 300, 330 + 48 * (k + 1), 430, METAL_EDGE, 2)
    f.rect(590, 196, 280, 234, "#d6dbe0", INK, 2.5)
    f.rect(590, 196, 280, 26, METAL_EDGE, INK, 2.5)
    for k in range(6):
        f.line(590 + 40 * (k + 1), 222, 590 + 40 * (k + 1), 430, "#b9c1c9", 2)
    f.rect(890, 336, 110, 94, "#e9ecef", INK, 2.5)
    # cranes over the buildings
    crane(f, 720, 196, 110, 160, 260, 860, 150)
    crane(f, 470, 300, 170, 120, 220, 610, 180)
    # lavender rows and olive trees in the foreground fields
    f.path("M0,470 Q300,450 600,470 T1200,466 V600 H0 Z", "#b7c27a")
    for r in range(4):
        y = 500 + r * 26
        for k in range(10):
            x0 = 30 + k * 34 + r * 10
            f.add(f'<ellipse cx="{n(x0)}" cy="{n(y)}" rx="14" ry="7" fill="{LAVENDER if (k + r) % 3 else LAVENDER_DARK}"/>')
    for x, y, s in ((520, 540, 1.0), (640, 556, 0.8), (1110, 520, 1.1)):
        f.rect(x - 5 * s, y - 34 * s, 10 * s, 34 * s, "#7a5a3a")
        f.add(f'<ellipse cx="{n(x)}" cy="{n(y - 50 * s)}" rx="{n(46 * s)}" ry="{n(26 * s)}" fill="{OLIVE}" stroke="{INK}" stroke-width="2"/>')
    for x, h in ((200, 160), (232, 130), (1010, 170), (1044, 140), (150, 110)):
        cypress(f, x, 470, h)
    # the road and the convoy
    f.path("M1200,600 C1000,560 900,520 780,500 S560,470 470,462", stroke="#8a8f99", w=34, extra='stroke-linecap="round"')
    f.path("M1200,600 C1000,560 900,520 780,500 S560,470 470,462", stroke=WHITE, w=2, extra='stroke-dasharray="14 14"')
    f.rect(820, 470, 210, 26, IRON, INK, 2, 4)
    for k in range(9):
        f.circle(836 + k * 22, 500, 9, INK)
    f.rect(850, 412, 150, 58, SAND, INK, 2.5, 3)
    f.line(850, 432, 1000, 432, "#a97a35", 2)
    f.rect(772, 474, 48, 26, HOT, INK, 2, 4)
    f.rect(776, 478, 24, 12, GLASS, INK, 1.5, 2)
    f.circle(786, 502, 9, INK)
    f.circle(806, 502, 9, INK)
    return f.svg()


def schedule():
    """The 2016 and the 2024 baseline on one year axis (to scale): when plasma experiments start and when D–T
    operation begins, with a mark for November 2026."""
    f = Fig("fy14ip-schedule", 360, "Timeline to scale from 2024 to 2040 with two rows. Upper row, the 2016 plan: first plasma in "
            "2025 and deuterium–tritium operation in 2035. Lower row, the 2024 plan: start of research operation in 2034 and "
            "deuterium–tritium operation in 2039. Circles mark the start of plasma experiments, diamonds the start of "
            "deuterium–tritium operation. A dashed vertical line marks November 2026. An arrow shows that deuterium–tritium "
            "operation moved four years later.", size=26)
    x0, x1, y0, y1 = 170, 560, 2024, 2040
    X = lambda y: x0 + (y - y0) / (y1 - y0) * (x1 - x0)
    ya, r1, r2 = 300, 116, 226
    xn = X(2026 + 10 / 12)
    f.line(xn, 44, xn, ya, MUTED, 2.5, "8 6")
    f.arrow(x0 - 4, ya, x1 + 24, ya, INK, 2.5, 13)
    for y in range(2024, 2041):
        f.line(X(y), ya, X(y), ya + (9 if y % 5 == 0 else 5), INK, 2 if y % 5 == 0 else 1.5)
    for y in (2025, 2030, 2035, 2040):
        f.tex(X(y), ya + 30, str(y), "middle")
    for yrow, label, start, dt in ((r1, r"\text{2016 plan}", 2025, 2035), (r2, r"\text{2024 plan}", 2034, 2039)):
        f.line(x0, yrow, x1, yrow, RULE_LIGHT, 2)
        f.tex(8, yrow, label, "start")
        for yr in (start, dt):
            f.line(X(yr), yrow, X(yr), ya, RULE_LIGHT, 1.5, "4 5")
        f.circle(X(start), yrow, 11, COLD, WHITE, 2.5)
        x = X(dt)
        f.path(f"M{n(x)},{n(yrow - 14)} L{n(x + 14)},{n(yrow)} L{n(x)},{n(yrow + 14)} L{n(x - 14)},{n(yrow)} Z", HOT, WHITE, 2.5)
        f.tex(x, yrow - 34, r"\text{D–T}", "middle", color=HOT, bg=True)
    f.tex(X(2025) + 6, r1 - 34, r"\text{first plasma}", "start", color=COLD, bg=True)
    f.tex(X(2034), r2 + 36, r"\text{research starts}", "middle", color=COLD, bg=True)
    f.arrow(X(2035) + 8, r1 + 16, X(2039) - 10, r2 - 16, HOT, 2.5, 12)
    f.tex(X(2037) - 22, (r1 + r2) / 2 + 4, r"+4\ \text{years}", "end", color=HOT, bg=True)
    f.tex(xn, 26, r"\text{Nov. 2026}", "middle", color=MUTED, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "schedule": schedule}
