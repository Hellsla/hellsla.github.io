"""Figures of the unit fy14-fr-bonjour (scripts/figlib.py, scripts/herolib.py); `python3 scripts/units.py figures
fy14-fr-bonjour` writes them into unit.md."""
from figlib import (Fig, INK, MUTED, WHITE, GLASS, ICE, SAND_LIGHT, SAND, SAND_DARK, ALUMINIUM, METAL_EDGE, IRON, COLD, GOOD,
                    WATER, n)
import herolib as H

LAVENDER, LAVENDER_DARK, LAVENDER_LIGHT = "#9775d6", "#6c4fa8", "#c9b6ee"
OLIVE, OLIVE_DARK, CYPRESS = "#9aa86a", "#6f7f45", "#2f4f2a"
STONE_LIGHT, STONE = "#e9e2cf", "#d6ccb2"


def cypress(f, x, ybase, h, w):
    """A Provençal cypress: a tall narrow flame of dark green with a shaded right half."""
    f.path(f"M{n(x)},{n(ybase - h)} C{n(x + w * 0.6)},{n(ybase - h * 0.7)} {n(x + w * 0.62)},{n(ybase - h * 0.2)} {n(x + w * 0.2)},{n(ybase)} "
           f"H{n(x - w * 0.2)} C{n(x - w * 0.62)},{n(ybase - h * 0.2)} {n(x - w * 0.6)},{n(ybase - h * 0.7)} {n(x)},{n(ybase - h)} Z", CYPRESS)
    f.add(f'<path d="M{n(x)},{n(ybase - h)} C{n(x + w * 0.6)},{n(ybase - h * 0.7)} {n(x + w * 0.62)},{n(ybase - h * 0.2)} {n(x + w * 0.2)},{n(ybase)} H{n(x)} Z" fill="{INK}" fill-opacity="0.25"/>')


def bubble(f, x0, y0, w, h, tail):
    """An empty speech bubble: a rounded box with a tail ending at tail = (x, y). The opening illustration has no text
    (NOTES §3); three dots inside say that someone speaks without saying what."""
    tx, ty = tail
    bx = min(max(tx, x0 + 40), x0 + w - 40)
    f.path(f"M{n(x0 + 18)},{n(y0)} H{n(x0 + w - 18)} Q{n(x0 + w)},{n(y0)} {n(x0 + w)},{n(y0 + 18)} V{n(y0 + h - 18)} "
           f"Q{n(x0 + w)},{n(y0 + h)} {n(x0 + w - 18)},{n(y0 + h)} H{n(bx + 18)} L{n(tx)},{n(ty)} L{n(bx - 14)},{n(y0 + h)} "
           f"H{n(x0 + 18)} Q{n(x0)},{n(y0 + h)} {n(x0)},{n(y0 + h - 18)} V{n(y0 + 18)} Q{n(x0)},{n(y0)} {n(x0 + 18)},{n(y0)} Z", WHITE, INK, 3)
    for k in (-1, 0, 1):
        f.circle(x0 + w / 2 + 34 * k, y0 + h / 2, 9, MUTED)


def hero():
    f = H.hero("fy14frb-hero", "Illustration: a sunny morning in Provence. Behind low limestone hills and dark cypress trees "
               "stands a modern visitor centre with a glass front and a flat roof. In front of its entrance two simple figures "
               "without faces meet: a student with a blue shirt and a backpack, and an engineer with a green shirt and a staff badge. "
               "Two speech bubbles without words show that they greet each other. In the foreground rows of lavender lead towards the building.")
    H.sky(f, "frb", 600, ICE, GLASS)
    H.sun(f, "frb", 140, 96, 50)
    H.cloud(f, 420, 70, 0.6)
    # limestone hills and the green garrigue below them
    H.hills(f, "frb", 286, [STONE_LIGHT, STONE], amp=46, seed=4)
    H.hills(f, "frb2", 346, [OLIVE, OLIVE_DARK], amp=30, seed=7)
    # the visitor centre: flat roof, glass front with mullions, entrance doors (no sign, no logo)
    f.rect(560, 250, 600, 262, WHITE, INK, 3)
    f.rect(586, 280, 548, 196, H.grad(f, "frb-glass", "#cfe4f5", "#7fb0d8"), INK, 2.5)
    for x in range(586 + 68, 1134, 68):
        f.line(x, 280, x, 476, METAL_EDGE, 3)
    f.line(586, 380, 1134, 380, METAL_EDGE, 3)
    for x, y, w in ((610, 300, 40), (746, 300, 50), (1020, 300, 46)):
        f.line(x, y + 40, x + w, y, WHITE, 3)          # reflections on the glass
    f.rect(926, 380, 136, 132, H.grad(f, "frb-door", "#a7c8e6", WATER), INK, 2.5)
    f.line(994, 380, 994, 512, INK, 2.5)
    f.rect(980, 432, 6, 34, IRON); f.rect(1002, 432, 6, 34, IRON)
    f.rect(536, 228, 648, 24, ALUMINIUM, INK, 3)        # the roof slab, overhanging
    # cypresses beside the building
    cypress(f, 468, 520, 260, 54)
    cypress(f, 520, 516, 200, 44)
    cypress(f, 70, 420, 170, 40)
    # the paved square in front of the entrance
    f.path("M440,512 H1200 V600 H330 Z", H.grad(f, "frb-square", SAND_LIGHT, SAND_DARK))
    for k in range(6):
        f.line(470 + 140 * k, 512, 380 + 160 * k, 600, SAND, 2)
    # the lavender field in the foreground, rows converging towards the building
    f.path("M0,420 C140,430 300,470 440,512 L330,600 H0 Z", OLIVE_DARK)
    vx, vy = 470, 404                                   # the rows run towards this point behind the field
    for k in range(6):
        bx = -150 + 92 * k                              # where the row meets the bottom edge
        t1 = 0.58                                       # how far towards the vanishing point the row is drawn
        ex, ey = bx + (vx - bx) * t1, 600 + (vy - 600) * t1
        hw0, hw1 = 30, 30 * (1 - t1)
        f.path(f"M{n(bx - hw0)},600 L{n(ex - hw1)},{n(ey)} L{n(ex + hw1)},{n(ey)} L{n(bx + hw0)},600 Z", LAVENDER_DARK)
        for j in range(12):                             # flowering bushes along the row, smaller with distance
            t = j / 12 * t1
            r = 22 * (1 - t) * 0.9
            f.circle(bx + (vx - bx) * t, 600 + (vy - 600) * t - r * 0.4, round(r, 1), LAVENDER)
            f.circle(bx + (vx - bx) * t - r * 0.3, 600 + (vy - 600) * t - r * 0.8, round(r * 0.35, 1), LAVENDER_LIGHT)
    # two people meet: the student (blue, with a backpack) and the engineer (green, with a badge)
    f.rect(592, 342, 30, 80, IRON, INK, 2, 8)          # backpack behind the student
    H.person(f, 650, 568, shirt=COLD, trousers=INK, sc=0.86)
    H.person(f, 846, 568, shirt=GOOD, trousers=IRON, sc=0.86)
    f.rect(858, 398, 20, 26, WHITE, INK, 1.5, 2)       # the staff badge on the engineer's shirt
    bubble(f, 820, 70, 220, 82, (850, 262))
    bubble(f, 470, 138, 220, 82, (630, 262))
    return f.svg()


FIGURES = {"hero": hero}
