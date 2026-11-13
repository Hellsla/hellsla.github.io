"""Figures of the FY8 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY8/koe` writes the model
figures into solutions.md. The task figure fy8-k1-stop is shown in the statement of item b by its id (fy8-koe/fy8-k1-stop).
Graphs to scale from the task data; every label is LaTeX."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, COLD, HEAT, HOT, n, fi

h, c, e = 6.626e-34, 2.998e8, 1.602e-19

# ---- k1 item b: stopping voltage of a metal
W_J = 2.32 * e
F1 = [6.5, 7.5, 8.5, 9.5]                                 # 1e14 Hz
US1 = [round((h * f * 1e14 - W_J) / e, 2) for f in F1]


def stop():
    f = Fig("fy8-k1-stop", 420, "Kuvaaja: pysäytysjännite $U_\\text{s}$ voltteina valon taajuuden $f$ funktiona, taajuus yksikössä $10^{14}$ hertsiä. "
            "Neljä mittauspistettä taajuuksilla 6,5, 7,5, 8,5 ja 9,5 kymmenen potenssiin 14 hertsiä on suoralla, joka nousee vasemmalta oikealle. "
            "Suora on piirretty vain mittausalueelle, ja se päättyy vasemmalla noin 0,24 voltin korkeudelle taajuudella 6,2 kymmenen potenssiin 14 hertsiä.")
    ax = Axes(f, (90, 360), (430, 70), x=(0, 10), y=(0, 2), xticks=list(range(1, 11)), yticks=[0.5, 1.0, 1.5, 2.0],
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{s}\ (\text{V})")
    k = h / e * 1e14
    ax.line([(6.2, k * 6.2 - 2.32), (9.8, k * 9.8 - 2.32)], INK, 3)
    for x, y in zip(F1, US1): ax.point(x, y, COLD)
    return f.svg()


# ---- k2: LED thresholds
LAM2 = [625, 590, 525, 470, 430]
UK2 = [1.91, 2.07, 2.31, 2.62, 2.84]
F2 = [c / (l * 1e-9) / 1e14 for l in LAM2]                # 1e14 Hz
n2 = len(F2); mx, my = sum(F2) / n2, sum(UK2) / n2
S2 = sum((a - mx) * (b - my) for a, b in zip(F2, UK2)) / sum((a - mx) ** 2 for a in F2); B2 = my - S2 * mx
dU2 = 0.05


def leds():
    f = Fig("fy8-k2-graph", 440, "Kuvaaja: LEDin kynnysjännite $U_\\text{k}$ voltteina valon taajuuden $f$ funktiona, taajuus yksikössä $10^{14}$ hertsiä. "
            "Viisi mittauspistettä taajuuksilla 4,8, 5,1, 5,7, 6,4 ja 7,0 kymmenen potenssiin 14 hertsiä, kullakin pystysuora virhepalkki plus miinus 0,05 volttia. "
            "Pisteet ovat nousevalla suoralla, joka jatkuu katkoviivana alaspäin ja leikkaa vaaka-akselin noin taajuudella 2,6 kymmenen potenssiin 14 hertsiä. "
            "Suoran kulmakerroin luetaan pisteistä 4,0 ja 1,59 volttia sekä 7,0 ja 2,87 volttia.")
    ax = Axes(f, (90, 390), (430, 70), x=(0, 8), y=(0, 3.5), xticks=list(range(1, 9)), yticks=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5],
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{k}\ (\text{V})")
    x0 = -B2 / S2
    ax.line([(x0, 0), (4.5, S2 * 4.5 + B2)], MUTED, 2.5, dash="8 6")
    ax.line([(4.5, S2 * 4.5 + B2), (7.3, S2 * 7.3 + B2)], INK, 3)
    for a, b in zip(F2, UK2):
        ax.line([(a, b - dU2), (a, b + dU2)], COLD, 2)
        ax.point(a, b, COLD, 5.5)
    ax.guide(4.0, S2 * 4.0 + B2); ax.guide(7.0, S2 * 7.0 + B2)
    f.tex(ax.X(2.6) + 4, ax.Y(0.45), r"\text{ekstrapolointi}", "start", MUTED, size=20, bg=True)
    f.tex(ax.X(7.0) + 8, ax.Y(S2 * 7.0 + B2) + 26, r"(7{,}0;\ 2{,}87)", "start", INK, size=20, bg=True)
    f.tex(ax.X(4.0) + 10, ax.Y(S2 * 4.0 + B2) + 26, r"(4{,}0;\ 1{,}59)", "start", INK, size=20, bg=True)
    return f.svg()


# ---- k3: decay counts
T3 = [0, 1, 2, 3, 4, 6, 8, 10]
N3 = [803, 631, 535, 409, 345, 205, 150, 88]
_s = sum((t - sum(T3) / 8) * (math.log(m) - sum(math.log(v) for v in N3) / 8) for t, m in zip(T3, N3)) / sum((t - sum(T3) / 8) ** 2 for t in T3)
LAM3 = -_s
N0_3 = math.exp(sum(math.log(v) for v in N3) / 8 - _s * sum(T3) / 8)


def decay():
    f = Fig("fy8-k3-graph", 420, "Kuvaaja: laskettu hajoamisten lukumäärä $N$ 30 sekunnin aikana ajan $t$ funktiona minuutteina. Kahdeksan mittauspistettä "
            "pienenee 803:sta arvoon 88 ajanhetkillä 0–10 minuuttia ja ne ovat laskevalla, alaspäin kuperalla eksponenttikäyrällä. Katkoviivat osoittavat, "
            "että käyrä on puolittunut alkuarvostaan 401 noin 3,2 minuutin kohdalla.")
    ax = Axes(f, (90, 380), (470, 70), x=(0, 10), y=(0, 900), xticks=list(range(1, 11)), yticks=[100 * i for i in range(1, 10)],
              xlabel=r"t\ (\text{min})", ylabel=r"N")
    ax.curve(lambda t: N0_3 * math.exp(-LAM3 * t), 0, 10.2, INK, 3)
    for t, m in zip(T3, N3): ax.point(t, m, COLD)
    th = math.log(2) / LAM3
    ax.guide(th, N0_3 / 2)
    f.tex(ax.X(th) + 8, ax.Y(0) - 22, r"3{,}2\,\text{min}", "start", MUTED, size=20, bg=True)
    f.tex(ax.X(0) + 10, ax.Y(N0_3 / 2) - 18, r"N = 401", "start", MUTED, size=20, bg=True)
    return f.svg()


# ---- k6: shielding
D6 = [0, 3, 6, 9, 12, 18, 24]
R6 = [120.9, 85.7, 61.3, 43.2, 31.4, 16.0, 8.7]
RN = [round(r - 0.8, 1) for r in R6]
_x = sum(D6) / 7; _y = sum(math.log(r) for r in RN) / 7
S6 = sum((a - _x) * (math.log(b) - _y) for a, b in zip(D6, RN)) / sum((a - _x) ** 2 for a in D6); B6 = _y - S6 * _x


def shield():
    f = Fig("fy8-k6-graph", 420, "Kuvaaja: nettolaskentanopeuden luonnollinen logaritmi $\\ln R$ lyijykerroksen paksuuden $d$ funktiona millimetreinä. "
            "Seitsemän mittauspistettä paksuuksilla 0–24 mm asettuu laskevalle suoralle, jonka kulmakerroin on noin −0,114 per millimetri. "
            "Suoran pisteet 0 mm ja 4,78 sekä 24 mm ja 2,05 on merkitty katkoviivoin.")
    ax = Axes(f, (112, 370), (470, 70), x=(0, 26), y=(0, 5), xticks=[3 * i for i in range(1, 9)], yticks=[1, 2, 3, 4, 5],
              xlabel=r"d\ (\text{mm})", ylabel=r"\ln(R / \text{s}^{-1})")
    ax.line([(0, B6), (26, B6 + S6 * 26)], INK, 3)
    for d, r in zip(D6, RN): ax.point(d, math.log(r), COLD)
    ax.guide(24, B6 + S6 * 24)
    f.line(ax.x0, ax.Y(B6), ax.X(0) + 0.1, ax.Y(B6), MUTED, 1.5)
    f.tex(ax.X(24) + 8, ax.Y(B6 + S6 * 24) - 22, r"(24;\ 2{,}05)", "start", INK, size=20, bg=True)
    f.tex(ax.X(0) + 14, ax.Y(B6) - 22, r"(0;\ 4{,}78)", "start", INK, size=20, bg=True)
    return f.svg()


FIGURES = {"fy8-k1-stop": stop, "fy8-k2-graph": leds, "fy8-k3-graph": decay, "fy8-k6-graph": shield}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy8-k1-stop": "reveals: the work function of the metal is read from the intercept (Osa 1 item b of the exam)",
    "fy8-k2-graph": "reveals: the model graph of exam task fy8-k2 (its solution)",
    "fy8-k3-graph": "reveals: the model graph of exam task fy8-k3 (its solution)",
    "fy8-k6-graph": "reveals: the model graph of exam task fy8-k6 (its solution)",
}
