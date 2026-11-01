"""Figures of the unit fy14-big-machines (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-big-machines` writes them into content/en/units/fy14-big-machines/unit.md. English: decimal point.
The hero has no text and shows only the size of a 1980s tokamak hall (prediction 1 is about ohmic heating, prediction 2
about the budget: neither is drawn). The budget chart uses the Fusion Power Associates figures (then-year US dollars):
FY1973 40, FY1978 332, FY1984 469 million; one series, so one colour, direct value labels and no legend."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, COLD, COLD_LIGHT,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")
BUDGET = [("1973", 40), ("1978", 332), ("1984", 469)]


def hero():
    """A huge tokamak in a high hall: a D-shaped torus with large coils and a neutral-beam box beside it, a crane above,
    and five small faceless people on the floor for scale."""
    f = H.hero("fy14bm-hero", "Illustration: a vast, brightly lit experimental hall with a travelling crane under the roof. In "
               "the middle stands a huge ring-shaped machine as tall as a three-storey house: a grey vacuum vessel inside "
               "large D-shaped blue coils, surrounded by pipes. To its right, a big box on legs points a tube into the ring. "
               "Five small people in different coloured shirts stand on the floor in front of it and look tiny next to the machine.")
    f.rect(0, 0, 1200, 600, H.grad(f, "bm-wall", "#e8edf1", "#c9d3db"))
    for x in range(0, 1201, 150):                       # wall panels
        f.line(x, 0, x, 470, "#b7c2cc", 3)
    # crane rails and crane
    f.rect(0, 40, 1200, 16, IRON)
    f.rect(330, 56, 560, 28, HEAT, INK, 2)
    f.line(610, 84, 610, 140, INK, 3)
    f.path("M596,140 h28 l-6,16 h-16 Z", IRON)
    # floor
    f.rect(0, 470, 1200, 130, H.grad(f, "bm-floor", "#9aa6b0", "#7a8792"))
    for x in range(-300, 1500, 120):
        f.line(x, 470, x - 220, 600, "#8a96a1", 2)
    # the machine: back coils, vessel, front coils (D-shaped, seen from the side, offset in depth)
    cx, base = 560, 470
    def dcoil(x, w, top, col, edge):
        f.path(f"M{x},{base - 10} V{top + 60} Q{x},{top} {x + w * 0.5},{top} Q{x + w},{top} {x + w},{top + 90} "
               f"V{base - 90} Q{x + w},{base - 10} {x + w * 0.5},{base - 10} Z", "none", col, 26)
    for k in range(7):                                  # back row, paler
        dcoil(250 + 90 * k, 110, 130, "#8fb3d9", None)
    f.rect(240, 230, 690, 160, H.grad(f, "bm-vessel", ALUMINIUM, METAL_EDGE), INK, 3, 70)
    for k in range(6):                                  # front row
        dcoil(290 + 105 * k, 120, 110, COLD, None)
    for y in (300, 330):                                # pipes
        f.line(160, y, 250, y, IRON, 8)
    f.rect(120, 260, 60, 210, IRON, INK, 2, 6)
    # neutral beam box on legs, pointing into the ring
    f.rect(960, 230, 190, 120, H.grad(f, "bm-nbi", SAND_LIGHT, SAND), INK, 3, 8)
    f.rect(900, 280, 70, 26, METAL_EDGE, INK, 2)
    f.rect(975, 350, 16, 120, IRON); f.rect(1120, 350, 16, 120, IRON)
    # people for scale
    for x, shirt in ((300, HOT), (360, GOOD), (700, COLD), (760, HEAT), (1040, "#7e22ce")):
        H.person(f, x, 560, shirt=shirt, trousers=INK, sc=0.36)
    return f.svg()


def heating():
    """A tokamak cross-section and the three ways to heat its plasma: the current (ohmic), a neutral beam, radio waves."""
    f = Fig("fy14bm-heating", 560, "Diagram of three ways to heat a tokamak plasma, drawn on a cross-section of the plasma ring "
            "seen from above. In the middle, an orange ring of plasma. A dark arrow along the ring shows the plasma current: "
            "ohmic heating. From the right, outside the ring, a box labelled neutral beam sends a short arrow and a row of dark dots, fast neutral "
            "atoms, into the plasma band, where the dots fade out: the atoms are caught in the plasma. From the lower left, an antenna sends curved wave lines into the plasma: radio waves.",
            width=600, size=28)
    f.rect(0, 0, 600, 560, WHITE)
    cx, cy, rx, ry = 260, 290, 180, 150                 # the plasma band reaches from rx - 32 to rx + 32 (x 408-472 at the right)
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{HEAT_LIGHT}" stroke-width="64"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{HEAT}" stroke-width="6" stroke-opacity="0.5"/>')
    # current arrow along the ring (ohmic heating)
    pts = [(cx + rx * math.cos(a), cy + ry * math.sin(a)) for a in [math.pi * (1.1 + 0.02 * k) for k in range(31)]]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=5)
    x2, y2 = pts[-1]; x1, y1 = pts[-3]
    f.arrow(x1, y1, x2 + (x2 - x1) * 0.8, y2 + (y2 - y1) * 0.8, INK, 5, 20)
    f.tex(cx, cy - 210, r"\text{current: ohmic heating}", "middle", size=28, w=420)
    # neutral beam from the right
    # neutral beam: the injector box stands outside the ring; the fast atoms fly into the plasma band and are caught there
    f.rect(500, 255, 90, 70, IRON, INK, 2, 6)
    f.tex(545, 196, r"\text{neutral}", "middle", size=28, w=110)
    f.tex(545, 230, r"\text{beam}", "middle", size=28, w=110)
    f.arrow(500, 290, 478, 290, INK, 4, 14)
    for k, x in enumerate((462, 446, 430, 414)):     # inside the band (x 408-472); fading: ionised and caught
        f.add(f'<circle cx="{x}" cy="290" r="8" fill="{INK}" fill-opacity="{1 - 0.22 * k:.2f}"/>')
    # radio waves from the lower left
    f.rect(20, 470, 90, 34, COPPER, INK, 2, 4)
    for k in range(3):
        r = 50 + 34 * k
        f.add(f'<path d="M{n(65 + r * 0.30)},{n(470 - r * 0.95)} A{r},{r} 0 0,1 {n(65 + r * 0.95)},{n(470 - r * 0.30)}" fill="none" stroke="{COPPER}" stroke-width="4"/>')
    f.tex(130, 534, r"\text{radio waves}", size=28, w=220)
    return f.svg()


def budget():
    """The US fusion budget in three years (millions of then-year dollars), a bar chart drawn to scale."""
    f = Fig("fy14bm-budget", 420, "Bar chart of the yearly US government budget for fusion research, in millions of dollars of "
            "the time: 40 in 1973, 332 in 1978 and 469 in 1984. The 1978 bar is about eight times as tall as the 1973 bar.",
            width=600, size=28)
    f.rect(0, 0, 600, 420, WHITE)
    x0, yb, top, vmax = 110, 350, 104, 500
    Y = lambda v: yb - (yb - top) * v / vmax
    for v in (0, 100, 200, 300, 400, 500):
        f.line(x0, Y(v), 580, Y(v), RULE_LIGHT if v else INK, 1.5 if v else 2.5)
        f.tex(x0 - 12, Y(v), str(v), "end", size=26, w=70)
    for i, (yr, v) in enumerate(BUDGET):
        x = x0 + 40 + 150 * i
        f.path(f"M{x},{yb} V{n(Y(v) + 4)} Q{x},{n(Y(v))} {x + 4},{n(Y(v))} H{x + 86} Q{x + 90},{n(Y(v))} {x + 90},{n(Y(v) + 4)} V{yb} Z", COLD)
        f.tex(x + 45, Y(v) - 22, str(v), "middle", size=28, w=90)
        f.tex(x + 45, yb + 28, yr, "middle", size=28, w=90)
    f.tex(10, 24, r"\text{US fusion budget, million dollars a year}", size=28, w=580)
    f.tex(10, 58, r"\text{(dollars of the time)}", size=26, w=580, color=INK)
    return f.svg()


FIGURES = {"hero": hero, "heating": heating, "budget": budget}
