"""Figures of the unit fy14-fr-cafe (scripts/figlib.py, scripts/herolib.py); `python3 scripts/units.py figures
fy14-fr-cafe` writes them into unit.md."""
from figlib import Fig, INK, MUTED, WHITE, GLASS, ICE, SAND_LIGHT, SAND, SAND_DARK, HOT, IRON, COLD, GOOD, METAL_EDGE, n
import herolib as H

OCHRE, OCHRE_LIGHT, SHUTTER, AWNING = "#e7c27d", "#efd7a6", "#4f7f6a", "#2f6f8f"
PLANE_BARK, LEAF, LEAF_DARK, CHAIR, CROISSANT, COFFEE = "#b9ad8f", "#7aa05a", "#56783c", "#8a5a2b", "#d8933a", "#5a3a1e"


def plane_tree(f, x, ybase, h):
    f.path(f"M{n(x - 20)},{n(ybase)} L{n(x - 12)},{n(ybase - h * 0.55)} L{n(x + 12)},{n(ybase - h * 0.55)} L{n(x + 20)},{n(ybase)} Z", PLANE_BARK, INK, 2)
    for dx, dy, r in ((-10, -0.22, 8), (6, -0.36, 9), (-4, -0.48, 6)):
        f.circle(x + dx, ybase + dy * h, r, "#e6ddc6")
    for dx, dy, r, c in ((-80, -0.62, 76, LEAF_DARK), (60, -0.66, 84, LEAF_DARK), (-20, -0.82, 96, LEAF), (70, -0.84, 66, LEAF), (-100, -0.78, 56, LEAF)):
        f.circle(x + dx, ybase + dy * h, r, c)


def chair(f, x, y, facing):
    """A bistro chair seen from the side: a curved back towards `facing` (-1 left, 1 right)."""
    bx = x - 26 * facing
    f.line(bx, y - 120, bx, y, CHAIR, 6, cap="round")
    f.line(x + 26 * facing, y - 60, x + 26 * facing, y, CHAIR, 6, cap="round")
    f.line(bx, y - 60, x + 30 * facing, y - 60, CHAIR, 8, cap="round")
    f.path(f"M{n(bx)},{n(y - 120)} Q{n(bx - 12 * facing)},{n(y - 90)} {n(bx)},{n(y - 64)}", stroke=CHAIR, w=5)


def table(f, x, y):
    """A round bistro table: a marble top seen at a slant, one leg and a cast-iron foot."""
    f.line(x, y, x, y + 112, IRON, 7)
    f.path(f"M{n(x - 40)},{n(y + 116)} Q{n(x)},{n(y + 98)} {n(x + 40)},{n(y + 116)}", IRON, INK, 2)
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="92" ry="20" fill="#f4f1ea" stroke="{INK}" stroke-width="2.5"/>')


def cup(f, x, y):
    """A small coffee cup on a saucer."""
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="22" ry="6" fill="{WHITE}" stroke="{INK}" stroke-width="1.5"/>')
    f.path(f"M{n(x - 13)},{n(y - 22)} H{n(x + 13)} L{n(x + 10)},{n(y - 3)} H{n(x - 10)} Z", WHITE, INK, 1.5)
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y - 22)}" rx="13" ry="3.5" fill="{COFFEE}"/>')
    f.path(f"M{n(x + 12)},{n(y - 18)} q10,2 0,10", stroke=INK, w=1.5)


def croissant(f, x, y):
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="26" ry="6" fill="{WHITE}" stroke="{INK}" stroke-width="1.5"/>')
    f.path(f"M{n(x - 22)},{n(y - 4)} Q{n(x)},{n(y - 30)} {n(x + 22)},{n(y - 4)} Q{n(x)},{n(y - 12)} {n(x - 22)},{n(y - 4)} Z", CROISSANT, "#9a5a1a", 1.5)
    for dx in (-8, 0, 8):
        f.line(x + dx, y - 20 + abs(dx) * 0.6, x + dx * 1.2, y - 8, "#9a5a1a", 1.5)


def hero():
    f = H.hero("fy14frc-hero", "Illustration: a café terrace in a Provençal town at midday. Under a blue awning and the shade of a "
               "plane tree stand round marble tables and wooden bistro chairs. Two students without faces sit at one table with a long tablecloth with "
               "small cups of coffee, a glass of orange juice and a croissant. A waiter in a white shirt and a long dark apron "
               "comes towards them carrying a round tray above his shoulder. Behind them is an ochre house with green shutters "
               "and a glass shop front.")
    H.sky(f, "frc", 600, ICE, GLASS)
    H.cloud(f, 1040, 70, 0.6)
    # the café building: ochre wall, upper windows with shutters, glass front at street level, awning
    f.rect(140, 40, 1000, 420, OCHRE, INK, 2.5)
    for wx in range(220, 1100, 160):
        f.rect(wx, 80, 44, 70, "#3d4f5c")
        f.rect(wx - 18, 80, 17, 70, SHUTTER); f.rect(wx + 45, 80, 17, 70, SHUTTER)
    f.rect(180, 250, 920, 210, H.grad(f, "frc-glass", "#cfe4f5", "#7fb0d8"), INK, 2.5)
    for x in range(180 + 115, 1100, 115):
        f.line(x, 250, x, 460, METAL_EDGE, 3)
    f.line(740, 300, 790, 260, WHITE, 3); f.line(410, 300, 450, 266, WHITE, 3)
    f.path("M150,196 H1130 L1170,262 H110 Z", AWNING, INK, 2.5)
    for k in range(13):
        x0 = 110 + k * 820 / 9.1
        f.path(f"M{n(x0)},262 h{n(1060 / 13)} l-{n(530 / 13)},20 Z", AWNING if k % 2 else "#24566f", INK, 1.5)
    # the terrace floor
    f.path("M0,460 H1200 V600 H0 Z", H.grad(f, "frc-floor", SAND_LIGHT, SAND_DARK))
    for k in range(10):
        f.line(-100 + 150 * k, 600, 40 + 130 * k, 460, SAND, 2)
    plane_tree(f, 90, 520, 470)
    # a second, empty table at the back
    chair(f, 930, 540, -1); table(f, 1030, 440); chair(f, 1130, 540, 1)
    # the students' table: chairs, the two students, then the table in front of them
    chair(f, 360, 586, -1); chair(f, 660, 586, 1)
    H.person(f, 400, 640, shirt=COLD, trousers=INK, sc=0.82)
    H.person(f, 620, 640, shirt=HOT, trousers=IRON, sc=0.82)
    table(f, 510, 470)
    f.path("M420,474 L392,600 H628 L600,474 Z", "#f4f1ea", INK, 2)     # a long tablecloth hides the legs: they sit
    for x in (450, 490, 530, 570):
        f.line(x, 480, x - 12 + (x - 510) * 0.25, 600, "#dcd6c8", 2)
    cup(f, 450, 468); cup(f, 556, 470)
    f.path("M500,470 L496,436 H520 L516,470 Z", "#ffb347", INK, 1.5)   # a glass of orange juice
    croissant(f, 600, 474)
    # the waiter with a tray held up
    H.person(f, 830, 590, shirt=WHITE, trousers=INK, sc=0.95, arms="up")
    f.path("M800,440 H860 L856,590 H804 Z", INK)                       # the long apron
    f.add(f'<ellipse cx="{n(830)}" cy="{n(270)}" rx="70" ry="10" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="2"/>')
    cup(f, 806, 266); cup(f, 852, 266)
    return f.svg()


FIGURES = {"hero": hero}
