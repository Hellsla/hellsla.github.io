"""Figures of the FY7 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY7/koe` writes the model
figures into solutions.md. The task figures fy7-k1-flux (item d) and fy7-k4-sin (task k4, part a) are shown in the
statement by their id (fy7-koe/<name>). Graphs to scale from the task data; every label is LaTeX."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, COLD, HEAT, HOT, n, fi

# ---- k1 item d: magnetic flux through a coil
def flux():
    f = Fig("fy7-k1-flux", 400, "Kuvaaja: käämin läpi kulkeva magneettivuo $\\Phi$ milliweberinä ajan $t$ funktiona sekunteina. "
            "Vuo kasvaa tasaisesti nollasta arvoon 0,6 mWb kahdessa sekunnissa, pysyy 0,6 mWb:ssä hetkestä 2,0 s hetkeen 4,0 s ja pienenee tasaisesti nollaan hetkeen 5,5 s mennessä.")
    ax = Axes(f, (100, 340), (470, 60), x=(0, 6), y=(0, 0.8), xticks=[1, 2, 3, 4, 5, 6], yticks=[0.2, 0.4, 0.6, 0.8],
              xlabel=r"t\ (\text{s})", ylabel=r"\Phi\ (\text{mWb})")
    ax.line([(0, 0), (2, 0.6), (4, 0.6), (5.5, 0)], INK, 3)
    for x, y in [(0, 0), (2, 0.6), (4, 0.6), (5.5, 0)]: ax.point(x, y, COLD)
    return f.svg()


# ---- k2: electron beam, r^2 against U
U2 = [80, 120, 160, 200, 240]
R2 = [0.038, 0.046, 0.054, 0.059, 0.066]
Q2 = [r * r * 1e3 for r in R2]                               # 1e-3 m^2
DQ2 = [2 * r * 0.001 * 1e3 for r in R2]
_n = 5; _mx = sum(U2) / _n; _my = sum(Q2) / _n
S2 = sum((a - _mx) * (b - _my) for a, b in zip(U2, Q2)) / sum((a - _mx) ** 2 for a in U2); B2 = _my - S2 * _mx


def beam():
    f = Fig("fy7-k2-graph", 420, "Kuvaaja: elektronin ratasäteen neliö $r^2$ yksikössä $10^{-3}$ neliömetriä kiihdytysjännitteen $U$ funktiona. "
            "Viisi mittauspistettä jännitteillä 80, 120, 160, 200 ja 240 volttia, kullakin pystysuora virhepalkki. Pisteet ovat nousevalla suoralla, jonka kulmakerroin "
            "luetaan pisteistä 80 V ja 1,4 sekä 240 V ja 4,3 kymmenen potenssiin miinus 3 neliömetriä.")
    ax = Axes(f, (100, 370), (470, 70), x=(0, 250), y=(0, 5), xticks=[50, 100, 150, 200, 250], yticks=[1, 2, 3, 4, 5],
              xlabel=r"U\ (\text{V})", ylabel=r"r^2\ (10^{-3}\,\text{m}^2)")
    ax.line([(0, B2), (250, B2 + S2 * 250)], INK, 3)
    for u, q, d in zip(U2, Q2, DQ2):
        ax.line([(u, q - d), (u, q + d)], COLD, 2.5)
        for yy in (q - d, q + d): f.line(ax.X(u) - 7, ax.Y(yy), ax.X(u) + 7, ax.Y(yy), COLD, 2.5)
        ax.point(u, q, COLD, 3.5)
    ax.guide(80, B2 + S2 * 80); ax.guide(240, B2 + S2 * 240)
    f.tex(ax.X(80) + 10, ax.Y(B2 + S2 * 80) - 24, r"(80;\ 1{,}4)", "start", INK, bg=True)
    f.tex(ax.X(240) - 10, ax.Y(B2 + S2 * 240) + 28, r"(240;\ 4{,}3)", "end", INK, bg=True)
    return f.svg()


# ---- k4: alternating voltage of a generator coil
E0 = 17.5; T4 = 25.0


def sine():
    f = Fig("fy7-k4-sin", 450, "Kuvaaja: generaattorin käämin jännite $e$ voltteina ajan $t$ funktiona millisekunteina. "
            "Jännite on sinimuotoinen, huippuarvo on 17,5 volttia ja jakso 25 millisekuntia. Kuvassa on kaksi jaksoa ajanhetkestä nolla hetkeen 50 millisekuntia.")
    ax = Axes(f, (100, 400), (470, 40), x=(0, 55), y=(-20, 20), xticks=[5 * i for i in range(1, 12)], yticks=[-20, -15, -10, -5, 5, 10, 15, 20],
              xlabel=r"t\ (\text{ms})", ylabel=r"e\ (\text{V})", x_at=0, origin_label=False, ticks_below=True)
    ax.curve(lambda t: E0 * math.sin(2 * math.pi * t / T4), 0, 50, INK, 3)
    return f.svg()


# ---- k7: peak wavelength of a lamp against 1/T
T7 = [2200, 2400, 2600, 2800, 3000]
L7 = [1262, 1139, 1070, 975, 921]
INV7 = [1e4 / t for t in T7]
S7 = sum(a * b for a, b in zip(INV7, L7)) / sum(a * a for a in INV7)


def lamp():
    f = Fig("fy7-k7-graph", 420, "Kuvaaja: hehkulampun spektrin huipun aallonpituus $\\lambda_\\text{max}$ nanometreinä lämpötilan käänteisluvun $1/T$ funktiona, yksikössä $10^{-4}$ per kelvin. "
            "Viisi mittauspistettä välillä 3,3–4,5 on suoralla, joka kulkee origon kautta; suoran kulmakerroin luetaan pisteistä 2,0 ja 550 nm sekä 4,0 ja 1100 nm.")
    ax = Axes(f, (100, 370), (400, 70), x=(0, 5), y=(0, 1400), xticks=[1, 2, 3, 4, 5], yticks=[200, 400, 600, 800, 1000, 1200, 1400],
              xlabel=r"1/T\ (10^{-4}\,\text{K}^{-1})", ylabel=r"\lambda_\text{max}\ (\text{nm})")
    ax.line([(0, 0), (5, S7 * 5)], INK, 3)
    ax.guide(2.0, S7 * 2.0); ax.guide(4.0, S7 * 4.0)
    f.tex(ax.X(2.0) + 10, ax.Y(S7 * 2.0) - 22, r"(2{,}0;\ 550)", "start", INK, bg=True)
    f.tex(ax.X(4.0) + 12, ax.Y(S7 * 4.0) + 30, r"(4{,}0;\ 1100)", "start", INK, bg=True)
    for a, b in zip(INV7, L7): ax.point(a, b, COLD, 7.5)      # the markers on top of the line and the labels
    return f.svg()


FIGURES = {"fy7-k1-flux": flux, "fy7-k2-graph": beam, "fy7-k4-sin": sine, "fy7-k7-graph": lamp}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy7-k1-flux": "safe: the flux data of Osa 1 item d; the answer needs the slope of the last section",
    "fy7-k2-graph": "reveals: the model graph of exam task fy7-k2 (its solution)",
    "fy7-k4-sin": "safe: the data of exam task fy7-k4 part a; the peak value and the period are read from it",
    "fy7-k7-graph": "reveals: the model graph of exam task fy7-k7 (its solution)",
}
