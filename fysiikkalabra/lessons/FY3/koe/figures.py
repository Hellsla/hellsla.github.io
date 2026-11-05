"""Figures of the FY3 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY3/koe` writes the model graphs into
solutions.md, and the task figures fy3-k1-work and fy3-k1-heating are shown in the statements by their ids (fy3-koe/<name>)."""
from figlib import Fig, Axes, INK, MUTED, COLD, HEAT

dec = lambda d: (lambda v: f"{v:.{d}f}".replace(".", "{,}"))


def work():
    """Osa 1 item b: the pushing force F against the distance s, 40 N for 0-3 m, then falling linearly to zero at 5 m (no area drawn)."""
    f = Fig("fy3-k1-work", 360, "Kuvaaja: työntövoima F newtoneina matkan s funktiona metreinä. Voima on 40 newtonia matkalla 0–3,0 m "
            "ja pienenee sen jälkeen tasaisesti nollaan matkan ollessa 5,0 m.")
    ax = Axes(f, (80, 310), (500, 60), x=(0, 6), y=(0, 50), xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[0, 10, 20, 30, 40, 50],
              xlabel=r"s\ (\text{m})", ylabel=r"F\ (\text{N})")
    ax.line([(0, 40), (3, 40), (5, 0)], INK, 3.5)
    return f.svg()


def heating():
    """Osa 1 item g: ice from -20 degC heated at constant power: rise, plateau at 0 degC, rise, a much longer plateau at 100 degC.
    Times from c_ice 2,09, s 333, c_water 4,19 and r 2260 kJ/kg with 100 kJ per kg and minute."""
    t1 = 2.09 * 20 / 100; t2 = t1 + 333 / 100; t3 = t2 + 4.19 * 100 / 100; t4 = t3 + 2260 / 100
    f = Fig("fy3-k1-heating", 380, "Kuvaaja: lämpötila T celsiusasteina ajan t funktiona minuutteina. Lämpötila nousee nopeasti "
            "−20 asteesta 0 asteeseen, pysyy 0 asteessa noin kolme minuuttia, nousee 100 asteeseen noin neljässä minuutissa "
            "ja pysyy sitten 100 asteessa noin 23 minuuttia.")
    ax = Axes(f, (90, 320), (480, 60), x=(0, 35), y=(-30, 120), xticks=[0, 5, 10, 15, 20, 25, 30, 35], yticks=[-20, 0, 20, 40, 60, 80, 100, 120],
              xlabel=r"t\ (\text{min})", ylabel=r"T\ ({}^\circ\text{C})", yfmt=dec(0))
    f.tex(ax.X(0), ax.Y(-30) + 24, "0", "middle")
    ax.line([(0, -20), (t1, 0), (t2, 0), (t3, 100), (t4, 100)], INK, 3.5)
    return f.svg()


TH2 = [5, 20, 35, 50, 65, 80]; L2 = [59.0, 62.5, 65.5, 68.5, 72.0, 75.0]


def zero():
    f = Fig("fy3-k2-graph", 420, "Kuvaaja: ilmapatsaan pituus L millimetreinä lämpötilan θ funktiona celsiusasteina. Kuusi mittauspistettä "
            "5 asteesta 80 asteeseen ovat nousevalla suoralla. Suora on jatkettu katkoviivana vasemmalle, ja se leikkaa vaaka-akselin "
            "noin kohdassa −273 astetta. Suoralta on luettu pisteet (0 °C; 58,0 mm) ja (80 °C; 75,0 mm).")
    ax = Axes(f, (80, 370), (480, 70), x=(-300, 100), y=(0, 80), xticks=[-300, -200, -100, 0, 100], yticks=[0, 20, 40, 60, 80],
              xlabel=r"\theta\ ({}^\circ\text{C})", ylabel=r"L\ (\text{mm})", xfmt=dec(0))
    k = 17.0 / 80; x0 = -58.0 / k
    f.tex(ax.X(-300), ax.Y(0) + 24, r"-300", "middle")
    ax.line([(x0, 0), (0, 58.0)], INK, 3, dash="9 6")
    ax.line([(0, 58.0), (95, 58.0 + k * 95)], INK, 3)
    ax.guide(80, 75.0); ax.point(0, 58.0, MUTED, 5)
    for th, L in zip(TH2, L2): ax.point(th, L)
    ax.point(x0, 0, HEAT, 7)
    f.tex(ax.X(-295), ax.Y(30), r"\theta_0 \approx -273\,{}^\circ\text{C}", "start", HEAT, bg=True)
    f.tex(ax.X(-295), ax.Y(55), r"k = \dfrac{75{,}0\,\text{mm} - 58{,}0\,\text{mm}}{80\,{}^\circ\text{C}}", "start", bg=True)
    return f.svg()


T6 = list(range(0, 14)); TH6 = [0.1, 0.1, 0.2, 0.2, 0.2, 0.3, 0.3, 0.6, 3.4, 11.2, 19.1, 27.3, 35.0, 42.9]


def melt():
    k = (42.9 - 11.2) / 4.0; tm = 9.0 - (11.2 - 0.2) / k
    f = Fig("fy3-k6-graph", 420, "Kuvaaja: seoksen lämpötila T celsiusasteina ajan t funktiona minuutteina. Pisteet ovat alussa vaakasuoralla "
            "suoralla lähellä nollaa noin seitsemän minuuttia, ja kahdeksannesta minuutista alkaen ne ovat nousevalla suoralla. "
            "Suorat leikkaavat noin hetkellä 7,6 min. Nousevalta suoralta on luettu pisteet (9,0 min; 11,2 °C) ja (13,0 min; 42,9 °C).")
    ax = Axes(f, (80, 370), (480, 70), x=(0, 14), y=(0, 50), xticks=[0, 2, 4, 6, 8, 10, 12, 14], yticks=[0, 10, 20, 30, 40, 50],
              xlabel=r"t\ (\text{min})", ylabel=r"T\ ({}^\circ\text{C})")
    ax.line([(0, 0.2), (tm + 0.4, 0.2)], COLD, 3)
    ax.line([(tm, 0.2), (13.6, 42.9 + k * 0.6)], INK, 3)
    ax.guide(13.0, 42.9); ax.guide(9.0, 11.2)
    for t, T in zip(T6, TH6): ax.point(t, T)
    f.tex(ax.X(5.6), ax.Y(6), r"t \approx 7{,}6\,\text{min}", "end", INK, bg=True)
    f.arrow(ax.X(5.7), ax.Y(5.2), ax.X(tm) - 4, ax.Y(0.2) - 6, MUTED, 2, 11)
    f.tex(ax.X(0.4), ax.Y(30), r"k = \dfrac{42{,}9\,{}^\circ\text{C} - 11{,}2\,{}^\circ\text{C}}{4{,}0\,\text{min}}", "start", bg=True)
    return f.svg()


FIGURES = {"fy3-k1-work": work, "fy3-k1-heating": heating, "fy3-k2-graph": zero, "fy3-k6-graph": melt}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy3-k1-work": "safe",
    "fy3-k1-heating": "safe",
    "fy3-k2-graph": "reveals: the model graph of exam task fy3-k2 (its solution)",
    "fy3-k6-graph": "reveals: the model graph of exam task fy3-k6 (its solution)",
}
