"""Figures of the unit fy14-fusion-debate (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-fusion-debate` writes them into content/en/units/fy14-fusion-debate/unit.md. hero: a school debate seen from the
back of the audience; no text, faceless figures (herolib.person)."""
import figlib
from figlib import INK, WHITE, ALUMINIUM, METAL_EDGE, IRON, COLD, HOT, HEAT, GOOD, SAND_LIGHT, SAND, n
import herolib as H

figlib.set_language({}, ".")
WALL, WALL_DARK, FLOOR, FLOOR_DARK = "#e8e1d2", "#d6ccb6", "#b98b5a", "#9a6f43"
WOOD, WOOD_DARK = "#a0703f", "#7a522b"
SCREEN, VIOLET = "#22313f", "#7048e8"


def lectern(f, x, ybase, colour):
    """A speaker's lectern: a tapered wooden stand with a coloured front panel and a sloping top."""
    f.path(f"M{n(x - 46)},{n(ybase)} L{n(x - 38)},{n(ybase - 120)} H{n(x + 38)} L{n(x + 46)},{n(ybase)} Z", WOOD, INK, 2.5)
    f.rect(x - 30, ybase - 104, 60, 60, colour, INK, 2)
    f.path(f"M{n(x - 50)},{n(ybase - 120)} L{n(x - 44)},{n(ybase - 136)} H{n(x + 44)} L{n(x + 50)},{n(ybase - 120)} Z", WOOD_DARK, INK, 2.5)


def head_back(f, x, y, r, shirt):
    """A member of the audience seen from behind: shoulders and the back of a head (no face)."""
    f.path(f"M{n(x - r * 1.9)},{n(y + r * 2.6)} Q{n(x - r * 1.9)},{n(y + r * 1.0)} {n(x)},{n(y + r * 0.9)} Q{n(x + r * 1.9)},{n(y + r * 1.0)} {n(x + r * 1.9)},{n(y + r * 2.6)} Z", shirt)
    f.circle(x, y, r, INK)


def hero():
    f = H.hero("fy14fd-hero", "Illustration: a school debate seen from the back of the classroom. On the left and on the "
               "right of the room stand two wooden lecterns facing each other, one with a blue front panel and one with an "
               "orange front panel. A speaker in a blue shirt stands behind the left lectern; a speaker in an orange shirt stands "
               "behind the right one. Between them, at a small table, the chair of the debate stands with a timer. Behind them, a "
               "large screen shows a simple bar chart and the outline of a ring-shaped fusion machine. In the foreground, "
               "the backs of the heads and shoulders of the audience fill two rows.")
    f.rect(0, 0, 1200, 600, WALL)
    f.rect(0, 0, 1200, 40, WALL_DARK)
    f.path("M0,400 H1200 V600 H0 Z", FLOOR)
    for k in range(9): f.line(-200 + 180 * k, 600, 120 + 120 * k, 400, FLOOR_DARK, 2)
    f.line(0, 400, 1200, 400, INK, 2)
    # the screen with a bar chart and a torus outline (no words or numbers)
    f.rect(380, 70, 440, 230, SCREEN, INK, 4, 6)
    f.line(420, 270, 600, 270, ALUMINIUM, 3); f.line(420, 270, 420, 110, ALUMINIUM, 3)
    for k, (h, c) in enumerate(((60, METAL_EDGE), (110, COLD), (80, HEAT), (140, GOOD))):
        f.rect(440 + 38 * k, 270 - h, 26, h, c)
    f.add(f'<ellipse cx="710" cy="185" rx="80" ry="52" fill="none" stroke="{VIOLET}" stroke-width="10"/>')
    f.add(f'<ellipse cx="710" cy="185" rx="34" ry="18" fill="{SCREEN}" stroke="{VIOLET}" stroke-width="4"/>')
    for a in (-60, -20, 20, 60):
        f.line(710 + a, 130 + abs(a) * 0.12, 710 + a * 1.1, 240 - abs(a) * 0.12, "#b9a6f7", 3)
    # the chair's table and a timer
    f.rect(540, 380, 120, 16, WOOD_DARK, INK, 2)
    f.line(556, 396, 556, 450, INK, 4); f.line(644, 396, 644, 450, INK, 4)
    H.stopwatch(f, 620, 362, 16, 0.3)
    H.person(f, 586, 450, shirt=GOOD, trousers=IRON, sc=0.55)
    f.rect(540, 380, 120, 16, WOOD_DARK, INK, 2)
    # the two teams' lecterns and speakers
    H.person(f, 250, 470, shirt=COLD, trousers=INK, sc=0.95)
    lectern(f, 250, 480, COLD)
    H.person(f, 950, 470, shirt=HEAT, trousers=INK, sc=0.95)
    lectern(f, 950, 480, HEAT)
    # the audience from behind, two rows
    shirts = [COLD, HOT, GOOD, IRON, HEAT, "#495057", SAND, COLD, GOOD, HOT]
    for k in range(9):
        head_back(f, 70 + 132 * k, 492, 26, shirts[k % len(shirts)])
    for k in range(8):
        head_back(f, 130 + 136 * k, 548, 32, shirts[(k + 3) % len(shirts)])
    return f.svg()


FIGURES = {"hero": hero}
