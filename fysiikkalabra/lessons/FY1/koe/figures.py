"""Figures of the FY1 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY1/koe` writes the model graphs into
solutions.md, and the task figure fy1-k1-walk is shown in the statement by its id (fy1-koe/fy1-k1-walk)."""
import math
from figlib import Fig, Axes, INK, MUTED, COLD

dec = lambda d: (lambda v: f"{v:.{d}f}".replace(".", "{,}"))


def walk():
    """Osa 1 item h: a walker's (t, s) graph, rising 0-4 s, flat 4-7 s, falling 7-9 s (no answer drawn in)."""
    f = Fig("fy1-k1-walk", 360, "Kuvaaja: kävelijän paikka s metreinä ajan t funktiona. Paikka kasvaa tasaisesti nollasta kuuteen metriin "
            "aikavälillä 0–4 s, pysyy kuudessa metrissä aikavälillä 4–7 s ja pienenee tasaisesti kahteen metriin aikavälillä 7–9 s.")
    ax = Axes(f, (80, 310), (500, 60), x=(0, 10), y=(0, 8), xticks=list(range(0, 11)), yticks=[0, 2, 4, 6, 8],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    ax.line([(0, 0), (4, 6), (7, 6), (9, 2)], INK, 3.5)
    return f.svg()


T2 = [0, 10, 20, 30, 40, 50]; L2 = [15.0, 13.9, 12.6, 11.5, 10.4, 9.1]


def candle():
    f = Fig("fy1-k2-graph", 420, "Kuvaaja: kynttilän pituus L senttimetreinä ajan t funktiona minuutteina. Kuusi mittauspistettä 15,0 senttimetristä "
            "9,1 senttimetriin asettuu laskevalle suoralle. Suoralta on luettu pisteet (0 min; 15,0 cm) ja (51 min; 9,0 cm).")
    ax = Axes(f, (80, 370), (470, 70), x=(0, 60), y=(0, 16), xticks=[0, 10, 20, 30, 40, 50, 60], yticks=[0, 4, 8, 12, 16],
              xlabel=r"t\ (\text{min})", ylabel=r"L\ (\text{cm})")
    ax.line([(0, 15.0), (58, 15.0 - 6.0 / 51 * 58)], INK, 3)
    ax.guide(51, 9.0)
    for t, L in zip(T2, L2): ax.point(t, L)
    f.tex(ax.X(3), ax.Y(3.2), r"k = \dfrac{-6{,}0\,\text{cm}}{51\,\text{min}} \approx -0{,}12\,\tfrac{\text{cm}}{\text{min}}", "start")
    return f.svg()


def chase():
    f = Fig("fy1-k3-graph", 420, "Kuvaaja: Elinan ja Aaron paikka s kilometreinä ajan t funktiona minuutteina Elinan lähdöstä. Elinan suora alkaa origosta "
            "ja nousee 2,3 kilometriin 12 minuutissa. Aaron jyrkempi suora alkaa kohdasta 5,0 minuuttia ja leikkaa Elinan suoran "
            "noin kohdassa (10,7 min; 2,1 km).")
    ax = Axes(f, (80, 370), (470, 70), x=(0, 13), y=(0, 3.0), xticks=[0, 2, 4, 6, 8, 10, 12], yticks=[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
              xlabel=r"t\ (\text{min})", ylabel=r"s\ (\text{km})", yfmt=dec(1))
    ax.line([(0, 0), (12, 3.2 * 720 / 1000)], COLD, 3)
    ax.line([(5, 0), (12, 6.0 * 420 / 1000)], INK, 3)
    tm = 642.9 / 60; sm = 3.2 * 642.9 / 1000
    ax.guide(tm, sm); ax.point(tm, sm)
    f.tex(ax.X(1.0), ax.Y(0.75), r"\text{Elina}", "start", COLD)
    f.tex(ax.X(8.2), ax.Y(0.55), r"\text{Aaro}", "start", INK)
    return f.svg()


T6 = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
V6 = [0.47, 0.99, 1.45, 1.95, 2.44, 2.90, 3.41, 3.87]
VL6 = [0.47, 0.86, 1.13, 1.30, 1.39, 1.44, 1.47, 1.48]


def fall():
    f = Fig("fy1-k6-graph", 420, "Kuvaaja: nopeus v ajan t funktiona. Pallon pisteet ovat origon kautta kulkevalla suoralla, joka nousee 3,87 metriin "
            "sekunnissa hetkellä 0,40 s. Kahvinsuodattimen pisteet ovat alussa lähellä pallon pisteitä, kaartuvat alaspäin ja "
            "tasaantuvat noin 1,5 metriin sekunnissa.")
    ax = Axes(f, (80, 370), (500, 70), x=(0, 0.45), y=(0, 5.0), xticks=[0, 0.1, 0.2, 0.3, 0.4], yticks=[0, 1, 2, 3, 4, 5],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\tfrac{\text{m}}{\text{s}})", xfmt=dec(1))
    ax.line([(0, 0), (0.43, 3.87 / 0.40 * 0.43)], INK, 3)
    ax.curve(lambda t: 1.5 * math.tanh(9.81 * t / 1.5), 0, 0.43, COLD, 3, dash="9 6")
    ax.guide(0.40, 3.87)
    for t, v in zip(T6, V6): ax.point(t, v)
    for t, v in zip(T6, VL6): ax.point(t, v, COLD)
    f.tex(ax.X(0.355), ax.Y(2.55), r"\text{pallo}", "end", INK)
    f.tex(ax.X(0.22), ax.Y(0.8), r"\text{suodatin}", "start", COLD)
    f.tex(ax.X(0.02), ax.Y(4.65), r"g = \dfrac{3{,}87\,\tfrac{\text{m}}{\text{s}}}{0{,}40\,\text{s}} \approx 9{,}7\,\tfrac{\text{m}}{\text{s}^2}", "start")
    return f.svg()


N7 = [100, 200, 300, 400, 500]; D7 = [10, 21, 30, 41, 51]


def paper():
    f = Fig("fy1-k7-graph", 420, "Kuvaaja: arkkipinon paksuus d millimetreinä arkkimäärän N funktiona. Viisi pistettä sadasta viiteensataan arkkiin "
            "on origon kautta kulkevalla suoralla; suoralta on luettu piste (500; 51 mm).")
    ax = Axes(f, (80, 370), (500, 70), x=(0, 550), y=(0, 70), xticks=[0, 100, 200, 300, 400, 500], yticks=[0, 10, 20, 30, 40, 50, 60, 70],
              xlabel=r"N", ylabel=r"d\ (\text{mm})")
    ax.line([(0, 0), (540, 51 / 500 * 540)], INK, 3)
    ax.guide(500, 51)
    for N, d in zip(N7, D7): ax.point(N, d)
    f.tex(ax.X(20), ax.Y(63), r"d_1 = \dfrac{51\,\text{mm}}{500} = 0{,}102\,\text{mm}", "start")
    return f.svg()


FIGURES = {"fy1-k1-walk": walk, "fy1-k2-graph": candle, "fy1-k3-graph": chase, "fy1-k6-graph": fall, "fy1-k7-graph": paper}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy1-k1-walk": "safe",
    "fy1-k2-graph": "reveals: the model graph of exam task fy1-k2 (its solution)",
    "fy1-k3-graph": "reveals: the model graph of exam task fy1-k3 (its solution)",
    "fy1-k6-graph": "reveals: the model graph of exam task fy1-k6 (its solution)",
    "fy1-k7-graph": "reveals: the model graph of exam task fy1-k7 (its solution)",
}
