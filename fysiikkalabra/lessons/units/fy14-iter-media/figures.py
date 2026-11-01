"""Figures of the unit fy14-iter-media (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-iter-media` writes them into content/en/units/fy14-iter-media/unit.md. The opening illustration is original:
an old printed newspaper page and a tablet with a newer article, both with a drawing of a tokamak, under a
magnifying glass; the text lines are grey bars, so nothing is readable."""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")
PLASMA, OLD_PAPER = "#e64980", "#f3e5c0"


def tokamak_sketch(f, x, y, w, h, bg):
    """A small cross-section of a tokamak in a picture box: two D shapes with a glowing plasma and a central stack."""
    f.rect(x, y, w, h, bg, INK, 2)
    cx, cy = x + w / 2, y + h / 2
    f.rect(cx - w * 0.04, y + h * 0.15, w * 0.08, h * 0.7, METAL_EDGE, INK, 1.5)
    for s in (-1, 1):
        ex = cx + s * w * 0.24
        f.add(f'<ellipse cx="{n(ex)}" cy="{n(cy)}" rx="{n(w * 0.17)}" ry="{n(h * 0.36)}" fill="#495057" stroke="{INK}" stroke-width="2"/>')
        f.add(f'<ellipse cx="{n(ex)}" cy="{n(cy)}" rx="{n(w * 0.1)}" ry="{n(h * 0.24)}" fill="{PLASMA}" fill-opacity="0.85"/>')
        f.add(f'<ellipse cx="{n(ex)}" cy="{n(cy)}" rx="{n(w * 0.05)}" ry="{n(h * 0.12)}" fill="#fff0f6"/>')


def lines(f, x, y, w, count, step, colour, short_last=True):
    for k in range(count):
        ww = w * (0.6 if short_last and k == count - 1 else 1)
        f.rect(x, y + k * step, ww, 8, colour, None, 0, 4)


def hero():
    f = H.hero("fy14im-hero", "Illustration: on a wooden table lie an old, slightly yellowed newspaper page and a modern tablet. "
               "Both show a picture of a doughnut-shaped fusion machine with a glowing pink plasma, and columns of text drawn as grey "
               "lines. A large magnifying glass rests over the tablet's picture, and a pencil lies beside the newspaper, as if "
               "someone is comparing the two articles.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy14im-table", "#c69c6d", "#9c6b3e"))
    for k in range(7):
        f.line(0, 40 + k * 90, 1200, 30 + k * 92, "#b08354", 3)
    # old newspaper, slightly rotated
    f.add('<g transform="rotate(-4 330 300)">')
    f.rect(90, 70, 480, 470, OLD_PAPER, INK, 2.5)
    f.rect(120, 96, 420, 26, "#8d7a55", None, 0, 4)
    f.line(120, 138, 540, 138, "#8d7a55", 2)
    tokamak_sketch(f, 120, 156, 240, 170, "#e9dcb4")
    lines(f, 380, 160, 160, 9, 19, "#b8a77f")
    lines(f, 120, 350, 200, 9, 19, "#b8a77f")
    lines(f, 340, 350, 200, 9, 19, "#b8a77f")
    f.add('</g>')
    # tablet
    f.add('<g transform="rotate(5 860 320)">')
    f.rect(640, 80, 440, 470, INK, INK, 3, 26)
    f.rect(662, 104, 396, 422, WHITE)
    f.rect(684, 122, 300, 22, COLD, None, 0, 4)
    tokamak_sketch(f, 684, 160, 352, 170, "#e7f5ff")
    lines(f, 684, 350, 352, 7, 22, "#ced4da")
    f.add('</g>')
    # pencil
    f.path("M120,560 L380,520 L386,534 L126,574 Z", HEAT_LIGHT, INK, 2)
    f.path("M380,520 L404,524 L386,534 Z", INK)
    # magnifying glass over the tablet picture
    f.circle(900, 260, 92, "none", INK, 10)
    f.add('<circle cx="900" cy="260" r="84" fill="#a5d8ff" fill-opacity="0.18"/>')
    f.path("M966,326 L1060,420", stroke=INK, w=24, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero}
