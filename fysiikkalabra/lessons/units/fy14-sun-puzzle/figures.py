"""Figures of the unit fy14-sun-puzzle (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-sun-puzzle` writes them into content/en/units/fy14-sun-puzzle/unit.md. English: the decimal sign is a point.
The three lifetime estimates are computed here with the same rounded values as the text: M = 1.99e30 kg,
L = 3.83e26 W, R = 6.96e8 m, G = 6.674e-11, c = 3.00e8 m/s, anthracite 32.5 MJ/kg (Wikipedia, Heat of combustion),
0.71 % of the fused mass (AME2020) and 10 % of the Sun's mass fused."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, GOOD, SAND, SAND_LIGHT,
                    SAND_DARK, GRAIN, IRON, n)
import herolib as H

figlib.set_language({}, ".")

M, L, R, G, C, YR = 1.99e30, 3.83e26, 6.96e8, 6.674e-11, 3.00e8, 3.156e7
T_CHEM = M * 3.25e7 / L / YR            # 5.35e3 a
T_GRAV = G * M * M / (R * L) / YR       # 3.14e7 a
T_NUC = 0.0071 * 0.10 * M * C * C / L / YR   # 1.05e10 a
AGE = 4.6e9


def hero():
    """The Why question: the Sun above a cliff of many rock layers, with a fossil shell in an old layer: the rocks record
    a very long time of sunshine. No words."""
    f = H.hero("fy14sp-hero", "Illustration: a bright Sun in a pale sky above the sea. In front, a tall cliff shows many horizontal "
               "rock layers in sand, brown and grey colours, stacked one on top of another. In one of the lower layers lies a "
               "spiral fossil shell. Small waves break at the foot of the cliff.")
    H.sky(f, "fy14sp-h", 600, "#cfe6f7", "#fdf3dc")
    H.sun(f, "fy14sp-h", 900, 130, 70)
    f.rect(0, 430, 1200, 170, "#7fb3d5")
    for k in range(9):
        y = 450 + k * 16
        f.path(f"M0,{y} " + " ".join(f"Q{60 * i + 30},{y - 6} {60 * i + 60},{y}" for i in range(20)), stroke=WHITE, w=2, extra='stroke-opacity="0.5"')
    # cliff with layers
    cols = ["#e9c98a", "#c99a5b", "#a97a35", "#d9b26a", "#8a6a45", "#b9a07a", "#7a6a5a", "#d6bf94", "#9c7b52", "#6c5a48"]
    top = 150
    ys = [top + i * 34 for i in range(len(cols) + 1)]
    face = lambda y: 560 + (y - top) * 125 / 340      # the cliff face: every layer ends on this one line
    for c, y0, y1 in zip(cols, ys, ys[1:]):
        f.path(f"M0,{y0} L{face(y0):.0f},{y0} L{face(y1):.0f},{y1} L0,{y1} Z", c)
    f.path(f"M0,{top} L560,{top} L{face(ys[-1]):.0f},{ys[-1]}", stroke=INK, w=2.5)
    f.rect(0, ys[-1], 720, 600 - ys[-1], "#5f4f40")
    # grass on top
    f.path(f"M0,{top} L560,{top} L556,{top - 14} L0,{top - 14} Z", "#7aa35a")
    # fossil spiral in a lower layer
    cx, cy = 300, ys[7] + 17
    pts = []
    for i in range(160):
        a = i * 0.12; r = 1.2 * math.exp(0.17 * a)
        pts.append((cx + r * math.cos(a), cy + 0.62 * r * math.sin(a)))
    f.path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), stroke="#f6f1e6", w=3)
    for k in range(10):
        f.circle(80 + H.rnd(k, 4) * 460, ys[2] + H.rnd(k + 50, 4) * 30, 2.5, "#f6f1e6")
    return f.svg()


def estimates():
    """The three lifetime estimates on a logarithmic time axis, with the age of the Sun."""
    f = Fig("fy14sp-estimates", 360, size=26, label=f"Horizontal bar chart on a logarithmic axis of time in years, from 10 to the power 3 "
            f"to 10 to the power 11. Chemical burning: about {round(T_CHEM, -3):.0f} years. Gravitational contraction: about {T_GRAV / 1e6:.0f} million "
            f"years. Hydrogen fusion: about {round(T_NUC / 1e10) * 10:.0f} billion years. A dashed vertical line marks the age of the Sun, "
            f"4.6 billion years: only the fusion bar reaches past it.")
    X0, X1 = 30, 560
    X = lambda t: X0 + (X1 - X0) * (math.log10(t) - 3) / 8
    base = 286
    f.arrow(X0, base, X1 + 22, base, INK, 2.5, 13)
    for e in range(3, 12):
        f.line(X(10 ** e), base, X(10 ** e), base + 8, INK, 2)
        if e % 2 == 1: f.tex(X(10 ** e), base + 30, rf"10^{{{e}}}", "middle")
        f.line(X(10 ** e), 40, X(10 ** e), base, RULE_LIGHT, 1.5)
    f.tex(X1 - 4, base - 22, r"t\ (\text{a})", "end", bg=True)
    rows = ((T_CHEM, HOT, r"\text{chemical}", 56), (T_GRAV, HEAT, r"\text{contraction}", 128), (T_NUC, COLD, r"\text{fusion}", 200))
    for t, col, lab, y in rows:
        f.rect(X0, y - 18, X(t) - X0, 36, col, INK, 1.5)
    f.line(X(AGE), 30, X(AGE), base, INK, 2.5, "8 6")
    f.tex(X(AGE) - 8, 248, r"\text{age of the Sun}", "end", bg=True)
    for t, col, lab, y in rows:
        f.tex(X(t) + 10, y, lab, "start", bg=True)
    return f.svg()


FIGURES = {"hero": hero, "estimates": estimates}
