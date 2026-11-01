"""Figures of the unit fy14-fr-nombres (scripts/figlib.py, scripts/herolib.py); `python3 scripts/units.py figures
fy14-fr-nombres` writes them into unit.md."""
from figlib import Fig, INK, MUTED, WHITE, GLASS, ICE, SAND_LIGHT, SAND, SAND_DARK, HOT, HEAT, HEAT_LIGHT, IRON, COLD, GOOD, n
import herolib as H

OCHRE, OCHRE_DARK, SHUTTER = "#e7c27d", "#c99a4b", "#4f7f6a"
LEMON, APRICOT, TOMATO, MELON, MELON_DARK = "#f4d03f", "#f0a04b", "#d9480f", "#8fbf6a", "#5c8a3c"
CRATE, CRATE_DARK, PLANE_BARK, LEAF, LEAF_DARK = "#c8955a", "#9a6a35", "#b9ad8f", "#7aa05a", "#56783c"


def facade(f, x, w, top, base, wall, shutters=True):
    """A Provençal town house: an ochre wall, a tiled roof edge and windows with green shutters."""
    f.rect(x, top, w, base - top, wall, INK, 2)
    f.rect(x - 6, top - 14, w + 12, 16, "#b5543a", INK, 2)
    for i in range(int((w - 30) // 70)):
        wx = x + 26 + i * 70
        for wy in range(int(top + 30), int(base - 70), 90):
            f.rect(wx, wy, 26, 44, "#3d4f5c")
            if shutters:
                f.rect(wx - 12, wy, 11, 44, SHUTTER); f.rect(wx + 27, wy, 11, 44, SHUTTER)


def crate(f, x, y, w, h, fruit, r, shade):
    """A wooden crate seen from the front, heaped with fruit."""
    for i in range(int(w // (2 * r))):
        for j in range(2):
            cx = x + r + 2 * r * i + (r if j else 0)
            if cx + r > x + w: continue
            f.circle(cx, y - r * (0.6 + 1.3 * j), r, fruit, shade, 1.5)
    f.rect(x, y - 4, w, h, CRATE, INK, 2.5)
    f.line(x, y + h / 2 - 2, x + w, y + h / 2 - 2, CRATE_DARK, 3)


def tag(f, x, y):
    """An empty price tag on a stick: a white card without writing (the opening illustration has no text)."""
    f.line(x, y + 22, x, y + 64, IRON, 3)
    f.rect(x - 34, y - 22, 68, 44, WHITE, INK, 2.5, 6)


def plane_tree(f, x, ybase, h):
    """A plane tree of a Provençal square: a pale mottled trunk and a broad crown."""
    f.path(f"M{n(x - 22)},{n(ybase)} L{n(x - 14)},{n(ybase - h * 0.55)} L{n(x + 14)},{n(ybase - h * 0.55)} L{n(x + 22)},{n(ybase)} Z", PLANE_BARK, INK, 2)
    for dx, dy, r in ((-14, -0.25, 8), (8, -0.38, 10), (-6, -0.5, 6)):
        f.circle(x + dx, ybase + dy * h, r, "#e6ddc6")
    for dx, dy, r, c in ((-90, -0.62, 80, LEAF_DARK), (60, -0.66, 90, LEAF_DARK), (-20, -0.8, 100, LEAF), (80, -0.82, 70, LEAF), (-110, -0.78, 60, LEAF)):
        f.circle(x + dx, ybase + dy * h, r, c)


def hero():
    f = H.hero("fy14frn-hero", "Illustration: a sunny morning market on a square in a Provençal town. Ochre houses with green "
               "shutters stand behind a plane tree. In front of them is a market stall under a red and white striped awning, "
               "with wooden crates of lemons, apricots, tomatoes and melons. Each crate has a blank price tag on a stick. "
               "A seller in a green shirt stands behind the stall, and a student in a blue shirt with a shopping bag stands in "
               "front of it with a coin in one hand. The figures have no faces.")
    H.sky(f, "frn", 600, ICE, GLASS)
    H.sun(f, "frn", 1080, 92, 46)
    H.cloud(f, 300, 80, 0.55)
    # houses of the old town behind the square
    facade(f, 0, 300, 150, 420, OCHRE)
    facade(f, 300, 260, 110, 420, "#efd7a6")
    facade(f, 560, 330, 170, 420, OCHRE_DARK)
    facade(f, 890, 310, 130, 420, OCHRE)
    # the paved square
    f.path("M0,420 H1200 V600 H0 Z", H.grad(f, "frn-square", SAND_LIGHT, SAND_DARK))
    for k in range(9):
        f.line(150 * k - 60, 600, 150 * k + 20, 420, SAND, 2)
    plane_tree(f, 1060, 450, 360)
    # the stall: awning on poles, a table with a cloth, crates of fruit
    for x in (190, 830):
        f.rect(x - 6, 200, 12, 300, IRON, INK, 1.5)
    stripes = 10
    for i in range(stripes):
        x0 = 160 + i * 70
        f.path(f"M{n(x0)},190 L{n(x0 + 70)},190 L{n(x0 + 70)},236 Q{n(x0 + 35)},262 {n(x0)},236 Z", HOT if i % 2 == 0 else WHITE, INK, 2)
    f.rect(152, 176, 716, 18, "#a61e1e", INK, 2)
    # the seller behind the table (only the upper body shows above the table)
    H.person(f, 540, 560, shirt=GOOD, trousers=IRON, sc=0.95)
    f.rect(170, 390, 680, 40, "#f8f3e6", INK, 2.5)            # the table top
    f.path("M170,430 H850 L846,566 H174 Z", "#dbe7f2", INK, 2.5)  # the cloth, down to the ground
    for x in range(200, 840, 60):
        f.line(x, 430, x - 2, 566, "#b9cde0", 3)
    crate(f, 190, 392, 150, 34, LEMON, 17, "#c9a227")
    crate(f, 360, 392, 150, 34, APRICOT, 16, "#c77a2a")
    crate(f, 530, 392, 150, 34, TOMATO, 18, "#a5370b")
    # melons: larger fruit in the last crate
    for cx, cy in ((722, 352), (782, 352), (752, 318)):
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="24" fill="{MELON}" stroke="{MELON_DARK}" stroke-width="2"/>')
        f.path(f"M{cx - 22},{cy} Q{cx},{cy - 14} {cx + 22},{cy}", stroke=MELON_DARK, w=2)
    f.rect(700, 388, 150, 34, CRATE, INK, 2.5)
    f.line(700, 405, 850, 405, CRATE_DARK, 3)
    for x in (265, 435, 605, 775):
        tag(f, x, 300 if x != 775 else 268)
    # the student in front of the stall, holding out a coin, with a shopping bag
    H.person(f, 960, 590, shirt=COLD, trousers=INK, sc=0.95)
    f.path("M992,450 L1000,470 H1040 L1048,450 Z", SAND_DARK, INK, 2)
    f.rect(996, 468, 48, 56, "#f1dfb5", INK, 2, 4)              # the shopping bag
    f.circle(916, 452, 10, "#d4a017", INK, 1.5)                 # the coin in the student's hand
    return f.svg()


FIGURES = {"hero": hero}
