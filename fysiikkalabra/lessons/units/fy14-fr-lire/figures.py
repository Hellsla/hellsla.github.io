"""Figures of the unit fy14-fr-lire (scripts/figlib.py, scripts/herolib.py); `python3 scripts/units.py figures
fy14-fr-lire` writes them into unit.md."""
from figlib import Fig, INK, MUTED, WHITE, SAND_LIGHT, SAND, SAND_DARK, IRON, COLD, GOOD, METAL_EDGE, RULE, n
import herolib as H

TABLE, TABLE_DARK, PAPER_C, LINE_C, MARK, COFFEE = "#c99a62", "#9a6a35", "#fbf8f0", "#9aa3ad", "#ffe066", "#5a3a1e"


def text_lines(f, x0, y0, w, rows, gap=22, seed=1, marks=()):
    """Lines of text as grey bars of varying length (no readable words); `marks` are (row, start, length) highlights."""
    for r in range(rows):
        y = y0 + r * gap
        k = (r * 37 + seed * 11) % 9
        lw = w if k < 6 else w * (0.55 + 0.05 * k)
        for (mr, ms, ml) in marks:
            if mr == r:
                f.rect(x0 + ms, y - 9, ml, 18, MARK, rx=3)
        x = x0
        while x < x0 + lw - 10:                                   # words: short bars with gaps
            ww = 24 + ((int(x) * 7 + r * 13 + seed) % 5) * 12
            ww = min(ww, x0 + lw - x)
            f.rect(x, y - 3, ww, 6, LINE_C, rx=3)
            x += ww + 10


def hero():
    f = H.hero("fy14frl-hero", "Illustration: a newspaper lies open on a wooden café table, seen from above. Its columns are "
               "drawn as grey lines without readable words, and a few short pieces of the lines are highlighted in yellow, "
               "like words a reader recognised. A photograph-shaped box on the page shows a simple ring-shaped machine. "
               "A magnifying glass lies on the newspaper, next to a small cup of coffee on a saucer and a pencil.")
    f.rect(0, 0, 1200, 600, H.grad(f, "frl-table", TABLE, TABLE_DARK))
    for y in range(40, 600, 70):
        f.path(f"M0,{y} C300,{y + 14} 700,{y - 12} 1200,{y + 6}", stroke="#b5864f", w=2)
    # the open newspaper: two pages, slightly rotated
    f.add('<g transform="rotate(-4 600 300)">')
    f.rect(170, 50, 860, 520, PAPER_C, INK, 2.5)
    f.line(600, 50, 600, 570, RULE, 2)
    f.rect(200, 80, 380, 26, "#3d4f5c", rx=3)                       # a headline bar (no words)
    f.rect(630, 80, 360, 16, "#6b7480", rx=3)
    # the picture box on the left page: a ring-shaped machine (a torus seen at a slant)
    f.rect(200, 128, 380, 150, "#e3eef8", INK, 1.5)
    f.add(f'<ellipse cx="390" cy="203" rx="120" ry="46" fill="none" stroke="{METAL_EDGE}" stroke-width="26"/>')
    f.add(f'<ellipse cx="390" cy="203" rx="120" ry="46" fill="none" stroke="#e8a3d8" stroke-width="6" opacity="0.8"/>')
    text_lines(f, 200, 300, 380, 12, seed=2, marks=((1, 40, 96), (4, 150, 70), (7, 10, 110), (10, 200, 80)))
    text_lines(f, 630, 120, 360, 19, seed=5, marks=((2, 120, 90), (6, 10, 70), (9, 200, 110), (13, 60, 80), (16, 160, 64)))
    f.add('</g>')
    # the magnifying glass over the right page
    f.line(880, 420, 980, 520, "#3d2b1a", 18, cap="round")
    f.circle(820, 360, 86, "#eef5f9", INK, 6)
    f.add(f'<circle cx="820" cy="360" r="86" fill="{WHITE}" fill-opacity="0.35"/>')
    f.path("M770,320 Q790,292 828,290", stroke=WHITE, w=6)
    # coffee cup on a saucer, and a pencil
    f.circle(1110, 470, 62, WHITE, INK, 2.5)
    f.circle(1110, 470, 40, WHITE, INK, 2)
    f.circle(1110, 470, 32, COFFEE)
    f.path("M1146,452 q34,4 30,30 q-4,18 -28,12", stroke=INK, w=6)
    f.add('<g transform="rotate(28 120 470)">')
    f.rect(40, 458, 170, 22, "#f2c94c", INK, 2)
    f.path("M210,458 L246,469 L210,480 Z", SAND_LIGHT, INK, 2)
    f.path("M236,466 L246,469 L236,472 Z", INK)
    f.rect(26, 458, 16, 22, "#e78f8e", INK, 2)
    f.add('</g>')
    return f.svg()


FIGURES = {"hero": hero}
