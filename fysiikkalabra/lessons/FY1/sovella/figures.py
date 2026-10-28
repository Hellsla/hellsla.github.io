"""Figures of FY1 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY1` writes them into solutions.md."""
from figlib import Fig, Axes, INK, MUTED, COLD, HOT

T = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
S = [0.0, 38.9, 157.9, 320.9, 477.4, 640.2, 799.2, 957.3, 1120.0, 1277.2, 1439.6]


def graph():
    """The model graph of fy1-s1: the ramp points apart, the line fitted to the floor points and the two points read off it."""
    f = Fig("fy1-s1-graph", 420, "Kuvaaja: pallon paikka s metreinä ajan t funktiona. Kolme ensimmäistä pistettä ovat rampilta ja kaartuvat "
            "ylöspäin. Lattialla otetut pisteet ovat suoralla, jonka kulmakerroin on 0,80 m/s. Suoralta on luettu pisteet (0,6 s; 0,32 m) ja (2,0 s; 1,44 m).")
    ax = Axes(f, (80, 370), (500, 70), x=(0, 2.2), y=(0, 1.6), xticks=[0, 0.4, 0.8, 1.2, 1.6, 2.0], yticks=[0, 0.4, 0.8, 1.2, 1.6],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})", xfmt=lambda v: f"{v:.1f}".replace(".", "{,}"))
    ax.line([(0.2, 0.0), (0.4, 0.16)], INK, 2, dash="8 6")              # the fitted line below the floor points, not a measurement
    ax.line([(0.4, 0.16), (2.15, 1.56)], INK, 3)
    for p in [(0.6, 0.32), (2.0, 1.44)]: ax.guide(*p)
    for t, s in zip(T, S):
        ax.point(t, s / 1000, COLD if t < 0.3 else INK)
    f.tex(ax.X(0.65), ax.Y(0.10), r"\text{ramppi}", "start", COLD)
    f.tex(ax.X(0.08), ax.Y(1.0), r"v = \dfrac{1{,}12\,\text{m}}{1{,}4\,\text{s}} = 0{,}80\,\tfrac{\text{m}}{\text{s}}", "start")
    return f.svg()


FIGURES = {"fy1-s1-graph": graph}
