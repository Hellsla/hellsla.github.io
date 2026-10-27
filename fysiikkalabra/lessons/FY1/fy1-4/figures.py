"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-4` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, COLD, HEAT, GOOD, RULE

# the cart data of the lesson's first simulation case (t in s, s in m) and the line fitted to it
CART = [(1, 0.6), (2, 0.8), (3, 1.6), (4, 2.1), (5, 2.4), (6, 2.9)]
# the kettle example: water temperature T (°C) every minute
KETTLE = [(0, 20.8), (1, 27.9), (2, 36.5), (3, 43.8), (4, 52.4), (5, 59.6)]


def scatter():
    f = Fig("fy14-scatter", 350, "Kuvaaja mittakaavassa: kärryn kulkema matka s ajan t funktiona. Kuusi mittauspistettä (t = 1…6 s) on "
            "hajallaan suoran s = 0,5 m/s · t ympärillä. Pisteitä on suoran molemmin puolin: kolme yläpuolella ja kolme alapuolella, ja "
            "pystysuorat katkoviivat näyttävät kunkin pisteen poikkeaman suorasta. Suora ei kulje jokaisen pisteen kautta.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 7), y=(0, 3.5), xticks=[1, 2, 3, 4, 5, 6], yticks=[1, 2, 3],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    ax.line([(0, 0), (7, 3.5)], INK, 3)
    for t, s in CART:
        f.line(ax.X(t), ax.Y(s), ax.X(t), ax.Y(0.5 * t), MUTED, 1.5, "5 4")
    for t, s in CART:
        ax.point(t, s, COLD)
    # legend in the empty top-left corner
    f.circle(ax.X(0.35), ax.Y(3.25), 6.5, COLD, WHITE, 2)
    f.tex(ax.X(0.35) + 18, ax.Y(3.25), r"\text{mittauspisteet}", "start", COLD, w=190)
    f.line(ax.X(0.35) - 12, ax.Y(2.75), ax.X(0.35) + 12, ax.Y(2.75), INK, 3, cap="round")
    f.tex(ax.X(0.35) + 18, ax.Y(2.75), r"\text{sovitettu suora}", "start", INK, w=190)
    f.tex(ax.X(5.7) + 14, ax.Y(1.6), r"\text{poikkeama}", "start", MUTED, w=150)
    f.line(ax.X(5.7) + 10, ax.Y(1.6), ax.X(5.05), ax.Y(2.45), MUTED, 1.5)
    return f.svg()


def slope():
    f = Fig("fy14-slope", 350, "Kaavakuva mittakaavassa: suora y = kx + b, jonka kulmakerroin on 0,5 ja vakiotermi 1. Suora leikkaa y-akselin "
            "kohdassa y = b = 1. Suoralta on valittu kaksi kaukana toisistaan olevaa pistettä P₁ = (2, 2) ja P₂ = (8, 5). Kulmakolmion "
            "vaakasivu on Δx = x₂ − x₁ = 6 ja pystysivu Δy = y₂ − y₁ = 3, joten kulmakerroin on k = Δy/Δx = 0,5.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 9), y=(0, 6), xticks=[2, 4, 6, 8], yticks=[1, 2, 3, 4, 5], xlabel=r"x", ylabel=r"y")
    ax.line([(0, 1), (9, 5.5)], INK, 3)
    f.line(ax.X(2), ax.Y(2), ax.X(8), ax.Y(2), MUTED, 1.5, "6 5")
    f.line(ax.X(8), ax.Y(2), ax.X(8), ax.Y(5), MUTED, 1.5, "6 5")
    ax.point(0, 1, HEAT)
    ax.point(2, 2, COLD); ax.point(8, 5, COLD)
    f.tex(ax.X(5), ax.Y(2) + 26, r"\Delta x", "middle", w=70)
    f.tex(ax.X(7.7), ax.Y(0.95), r"k = \dfrac{\Delta y}{\Delta x}", "middle", w=150, bg=True)
    f.tex(ax.X(8) + 14, ax.Y(3.5), r"\Delta y", "start", w=70)
    f.tex(ax.X(0) + 14, ax.Y(1) - 24, r"b", "start", HEAT, w=30)
    f.tex(ax.X(2) - 8, ax.Y(2) - 30, r"P_1", "end", COLD, w=50)
    f.tex(ax.X(8) - 14, ax.Y(5) - 26, r"P_2", "end", COLD, w=50)
    f.tex(ax.X(3.4), ax.Y(4.5), r"y = kx + b", "middle", INK, w=140, bg=True)
    return f.svg()


def kettle():
    f = Fig("fy14-kettle", 350, "Kuvaaja mittakaavassa: vedenkeittimen veden lämpötila T ajan t funktiona. Kuusi mittauspistettä minuutin "
            "välein on suoran T = 8,0 °C/min · t + 20 °C ympärillä. Suoralta on luettu kaksi kaukana toisistaan olevaa pistettä, (0 min; 20 °C) "
            "ja (5,0 min; 60 °C). Katkoviiva näyttää, että suora saavuttaa 40 °C:n lämpötilan ajassa 2,5 min.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 6), y=(0, 70), xticks=[1, 2, 3, 4, 5, 6], yticks=[20, 40, 60],
              xlabel=r"t\ (\text{min})", ylabel=r"T\ ({}^\circ\text{C})")
    ax.line([(0, 20), (6, 68)], INK, 3)
    ax.guide(2.5, 40, GOOD)
    for t, T in KETTLE:
        ax.point(t, T, COLD)
    f.circle(ax.X(0), ax.Y(20), 11, "none", HEAT, 2.5)
    f.circle(ax.X(5), ax.Y(60), 11, "none", HEAT, 2.5)
    f.tex(ax.X(0) + 20, ax.Y(20) + 30, r"A", "start", HEAT, w=30)
    f.tex(ax.X(5) + 4, ax.Y(60) + 34, r"B", "start", HEAT, w=30)
    f.line(ax.X(2.5), ax.Y(0), ax.X(2.5), ax.Y(0) + 7, GOOD, 2)
    f.tex(ax.X(2.5), ax.Y(0) + 24, r"2{,}5", "middle", GOOD, w=34, bg=True)
    return f.svg()


FIGURES = {"scatter": scatter, "slope": slope, "kettle": kettle}
