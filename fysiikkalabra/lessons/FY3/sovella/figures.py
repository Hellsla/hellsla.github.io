"""Figures of FY3 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY3` writes them into solutions.md."""
import math
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD

t = list(range(0, 65, 5))
T = [20.0, 24.1, 28.0, 31.6, 35.0, 38.0, 40.9, 43.8, 46.2, 48.5, 50.7, 52.8, 54.7]
model = lambda x: 20 + 60 * (1 - math.exp(-x / 69.8))   # the curve the data was made from (answers.py)


def graph():
    """The model graph of fy3-s1: the points, a smooth curve, the tangent at the start (b) and the chord 40–60 min (d)."""
    f = Fig("fy3-s1-graph", 420, "Kuvaaja: veden lämpötila T ajan t funktiona. Pisteiden kautta kulkee loiveneva käyrä. Alkuun piirretty tangentti "
            "nousee 0,85 kelviniä minuutissa, ja hetkien 40 min ja 60 min pisteiden kautta kulkeva suora nousee 0,43 kelviniä minuutissa.")
    ax = Axes(f, (80, 370), (470, 70), x=(0, 66), y=(10, 60), xticks=[0, 10, 20, 30, 40, 50, 60], yticks=[10, 20, 30, 40, 50, 60],
              xlabel=r"t\ (\text{min})", ylabel=r"T\ ({}^\circ\text{C})", origin_label=False)
    f.tex(ax.x0 - 12, ax.y0, "10", "end"); f.tex(ax.x0, ax.y0 + 24, "0", "middle")
    ax.curve(model, 0, 64, MUTED, 2.5)
    ax.line([(0, 20.0), (32, 47.2)], HEAT, 2.5, dash="9 6")              # tangent at the start: 0,85 K/min
    ax.line([(34, 43.65), (64, 56.4)], COLD, 2.5, dash="9 6")            # through the points at 40 and 60 min: 0,425 K/min
    for a, b in zip(t, T): ax.point(a, b)
    f.tex(ax.X(2), ax.Y(53), r"\text{tangentti: } 0{,}85\,\tfrac{\text{K}}{\text{min}}", "start", HEAT)
    f.tex(ax.X(64), ax.Y(42), r"0{,}43\,\tfrac{\text{K}}{\text{min}}", "end", COLD)
    return f.svg()


FIGURES = {"fy3-s1-graph": graph}
