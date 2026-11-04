"""Figures of FY8 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY8` writes them into
solutions.md. One task figure (the oxygen atom's three lowest levels for the aurora task, no transitions drawn) and the
two model graphs of the GM tube task (data as in answers.py)."""
import math
from figlib import Fig, Axes, INK, MUTED, COLD, fi

# fy8-s3 data (answers.py): distances (cm), pulses in 1,0 min, background 112 pulses in 5,0 min
RS = [2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 14.0, 20.0]
NS = [3048, 1806, 1172, 790, 617, 405, 256, 152, 94]
RB = 112 / 5.0


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def oxygen_levels():
    """fy8-s1 task figure: the three lowest energy levels of the oxygen atom, energy axis to scale, no transitions."""
    f = Fig("fy8-s1-levels", 340, "Happiatomin energiatasokaavio, energia-akseli mittakaavassa. Alimpana perustila energialla 0 "
            "elektronivolttia. Sen yläpuolella alempi viritystila energialla 1,97 elektronivolttia ja ylimpänä ylempi "
            "viritystila energialla 4,19 elektronivolttia. Siirtymiä ei ole piirretty.")
    Y = lambda E: 290 - E * 56
    xl, xr = 150, 400
    f.tex(20, 22, r"E\ (\text{eV})", "start")
    f.arrow(110, Y(0) + 10, 110, Y(4.6), INK, 2.5, 13)
    for E, name in ((0, r"\text{perustila}"), (1.97, r"\text{alempi viritystila}"), (4.19, r"\text{ylempi viritystila}")):
        f.line(xl, Y(E), xr, Y(E), INK, 3)
        f.line(104, Y(E), 116, Y(E), INK, 2)
        f.tex(96, Y(E), "0" if E == 0 else fi(E), "end")
        f.tex(xr + 12, Y(E), name, "start", w=170)
    f.tex((xl + xr) / 2, 322, r"\text{happiatomi}", "middle", MUTED)
    return f.svg()


def inverse_square():
    """fy8-s3 a: the net count rate against 1/r², and the line through the origin and the farthest point (the
    assumption R ∝ 1/r² tested): the near points fall far below it."""
    xs = [1 / r ** 2 for r in RS]; ys = [n - RB for n in NS]
    k0 = ys[-1] / xs[-1]                                         # through the origin and the 20 cm point
    f = Fig("fy8-s3-inv", 420, "Kuvaaja: nettopulssitaajuus R pulsseina minuutissa etäisyyden neliön käänteisarvon 1 per r toiseen "
            "funktiona, vaaka-akseli nollasta 0,26:een per neliösenttimetri ja pystyakseli nollasta 3500:aan per minuutti. Yhdeksän "
            "mustaa pistettä: (0,0025; 72), (0,0051; 130), (0,0100; 234), (0,0156; 383), (0,0278; 595), (0,0400; 768), "
            "(0,0625; 1150), (0,111; 1784) ja (0,250; 3026). Origosta lähtee katkoviivana suora, joka kulkee kaukaisimman "
            "pisteen kautta. Lähimmät pisteet ovat selvästi suoran alapuolella, ja pisteet muodostavat alaspäin kaartuvan "
            "käyrän eivätkä suoraa.")
    ax = Axes(f, (100, 370), (420, 60), x=(0, 0.26), y=(0, 3500), xticks=[0.05, 0.10, 0.15, 0.20, 0.25],
              yticks=[500, 1000, 1500, 2000, 2500, 3000, 3500],
              xlabel=r"1/r^2\ (1/\text{cm}^2)", ylabel=r"R\ (1/\text{min})",
              xfmt=lambda v: "0{,}" + f"{round(v * 100):02d}", yfmt=lambda v: str(round(v)) if v % 1000 == 0 else "")
    ax.line([(0, 0), (3500 / k0, 3500)], MUTED, 2.5, dash="9 6")
    f.tex(ax.X(3500 / k0) + 10, ax.Y(3300), r"R \sim 1/r^2", "start", MUTED)
    for x, y in zip(xs, ys): ax.point(x, y)
    return f.svg()


def linearised():
    """fy8-s3 b: 1/sqrt(R) against r with the fitted line, extended dashed to the r axis at r = -d, and the points it is read at."""
    ys = [100 / math.sqrt(n - RB) for n in NS]                  # 10^-2 sqrt(min)
    k, b = _fit(RS, ys)
    r0 = -b / k
    f = Fig("fy8-s3-lin", 450, "Kuvaaja: nettopulssitaajuuden neliöjuuren käänteisarvo, R potenssiin miinus yksi kahdesosa, yksikössä 10 potenssiin "
            "miinus 2 minuutti potenssiin yksi kahdesosa etäisyyden r funktiona, r miinus kahdesta 22 senttimetriin. Yhdeksän mustaa pistettä: "
            "(2,0; 1,82), (3,0; 2,37), (4,0; 2,95), (5,0; 3,61), (6,0; 4,10), (8,0; 5,11), (10,0; 6,54), (14,0; 8,78) ja "
            "(20,0; 11,82). Pisteisiin on sovitettu suora, ja sitä on jatkettu katkoviivana r-akselille, jonka se leikkaa "
            "kohdassa r = −1,3 cm. Suoralta on merkitty piste (20,0; 12,0) ja leikkauskohta (−1,3; 0).")
    ax = Axes(f, (90, 396), (480, 84), x=(-2, 22), y=(0, 13), xticks=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
              yticks=list(range(1, 14)), xlabel=r"r\ (\text{cm})",
              ylabel=r"R^{-1/2}\ (10^{-2}\,\text{min}^{1/2})",
              xfmt=lambda v: str(v) if v % 4 == 0 else "", yfmt=lambda v: str(v) if v % 2 == 0 else "", origin_label=False)
    f.line(ax.X(0), ax.y0, ax.X(0), ax.y1, MUTED, 1.5)
    ax.line([(r0, 0), (2.0, b + 2.0 * k)], INK, 2.5, dash="8 6")
    ax.line([(2.0, b + 2.0 * k), (21.5, b + 21.5 * k)], INK, 2.5)
    for r, y in zip(RS, ys): ax.point(r, y)
    for r, y in ((-1.3, 0.0), (20.0, 12.0)):
        f.circle(ax.X(r), ax.Y(y), 11, "none", INK, 1.5)
    ax.guide(20.0, 12.0)
    f.tex(ax.X(20.0) - 18, ax.Y(12.0) - 24, r"(20{,}0;\ 12{,}0)", "end", INK, bg=True)
    f.tex(ax.X(2.6), ax.Y(0.7), r"(-1{,}3;\ 0)", "start", COLD, bg=True)
    return f.svg()


FIGURES = {"fy8-s1-levels": oxygen_levels, "fy8-s3-inv": inverse_square, "fy8-s3-lin": linearised}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy8-s1-levels": "safe: the oxygen atom's levels 0, 1,97 and 4,19 eV without transitions (task fy8-s1)",
    "fy8-s3-inv": "reveals: the model graph of task fy8-s3 a (R against 1/r² bends below the origin line)",
    "fy8-s3-lin": "reveals: the model graph of task fy8-s3 b (the linearised fit and d = 1,3 cm)",
}
