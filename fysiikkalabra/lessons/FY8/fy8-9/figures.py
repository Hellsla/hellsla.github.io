"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-9` writes them into lesson.md.
An undecayed nucleus is a filled orange disc, a decayed one a grey ring (the same as in the simulation); a fresh decay
sends out a short ray. The fitting data are the simulated example data of lesson-answers.py (imported, one source)."""
import importlib.util, math, pathlib
from figlib import Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT, HEAT_LIGHT, IRON, METAL_EDGE, ALUMINIUM, COLD, PAPER
import herolib as H

_spec = importlib.util.spec_from_file_location("fy89_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)
LN2 = math.log(2)


def nucleus(f, x, y, r, alive=True):
    if alive:
        f.circle(x, y, r, HEAT, WHITE, 1.5)
    else:
        f.circle(x, y, r * 0.72, "none", MUTED, 2)


def ydin():
    """Ydinajatus: the same 100 nuclei at t = 0, T½ and 2 T½; which ones decay is random, about half are left each time."""
    life = LA.lifetimes(6, 1.0)[:100]                      # one random sample, T½ = 1
    counts = [sum(1 for x in life if x > k) for k in (0, 1, 2)]
    f = Fig("fy89-ydin", 330, "Kolme ruudukkoa vierekkäin: samat 100 radioaktiivista ydintä kolmella hetkellä. Hajoamaton ydin on "
            f"oranssi täysi ympyrä, hajonnut ydin harmaa rengas. Hetkellä t = 0 kaikki 100 ovat hajoamattomia. Yhden "
            f"puoliintumisajan kuluttua hajoamattomia on {counts[1]} ja kahden puoliintumisajan kuluttua {counts[2]}. Hajonneet "
            "ytimet ovat sattumanvaraisissa kohdissa ruudukkoa, eikä ytimen paikka tai ikä ennusta sen hajoamista.")
    cell, side = 15, 150
    for p, (k, title) in enumerate(((0, "t = 0"), (1, "t = T_{1/2}"), (2, "t = 2T_{1/2}"))):
        x0 = 30 + p * 190
        f.rect(x0 - 6, 58, side + 12, side + 12, PAPER, RULE, 1.5, 6)
        for i in range(100):
            cx, cy = x0 + (i % 10 + 0.5) * cell, 64 + (i // 10 + 0.5) * cell
            nucleus(f, cx, cy, 5.5, life[i] > k)
        f.tex(x0 + side / 2, 30, title, "middle")
        f.tex(x0 + side / 2, 252, "N = " + str(counts[p]), "middle", HEAT)
        if p < 2: f.line(x0 + side + 25, 62, x0 + side + 25, 222, RULE, 2, "6 6")
    f.tex(300, 300, r"\text{oranssi: hajoamaton,\ harmaa: hajonnut}", "middle", MUTED)
    return f.svg()


def kuvaaja():
    """Kaava: N against t in half-lives: N0, N0/2, N0/4, N0/8 at 0, 1, 2, 3 half-lives, guides at each."""
    f = Fig("fy89-kuvaaja", 380, "Kuvaaja mittakaavassa: hajoamattomien ytimien määrä N ajan funktiona. Vaaka-akselilla aika "
            "puoliintumisaikoina nollasta viiteen, pystyakselilla N, asteikko nollasta alkumäärään N nolla neljäsosin. Käyrä "
            "alkaa arvosta N nolla ja laskee yhä loivemmin. Katkoviivat näyttävät, että yhden puoliintumisajan kohdalla "
            "jäljellä on puolet, kahden kohdalla neljäsosa ja kolmen kohdalla kahdeksasosa alkumäärästä. Käyrä ei koskaan "
            "saavuta nollaa.")
    yl = {0.25: r"\tfrac{1}{4}N_0", 0.5: r"\tfrac{1}{2}N_0", 0.75: r"\tfrac{3}{4}N_0", 1: "N_0"}
    xl = {1: "T_{1/2}", 2: "2T_{1/2}", 3: "3T_{1/2}", 4: "4T_{1/2}", 5: "5T_{1/2}"}
    ax = Axes(f, (100, 312), (530, 58), x=(0, 5.5), y=(0, 1.08), xticks=[1, 2, 3, 4, 5], yticks=[0.25, 0.5, 0.75, 1],
              xlabel="t", ylabel="N", xfmt=lambda v: xl[v], yfmt=lambda v: yl[v])
    ax.curve(lambda v: 0.5 ** v, 0, 5.5, HEAT, 3)
    for k in (1, 2, 3):
        ax.guide(k, 0.5 ** k); ax.point(k, 0.5 ** k, HEAT)
    ax.point(0, 1, HEAT)
    f.tex(ax.X(3) + 22, ax.Y(0.125) - 32, r"\tfrac{1}{8}N_0", "start", MUTED)
    f.tex(ax.X(1.45), ax.Y(0.9), r"N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}", "start", HEAT, bg=True)
    return f.svg()


def sovitus():
    """Kaava, fitting: simulated Ba-137m counts per 10 s, the fitted A e^(-Ct) + B and the background B dashed."""
    a = LA.a
    C, A, B = a["ba-C"], a["ba-A"], a["ba-B"]
    f = Fig("fy89-sovitus", 380, "Kuvaaja mittakaavassa, simuloitu esimerkkiaineisto: barium-137m-näytteen pulssimäärä 10 sekunnin "
            "jaksoissa ajan funktiona, aika nollasta 900 sekuntiin, 16 mittauspistettä 60 sekunnin välein. Ensimmäisessä "
            "jaksossa on 249 pulssia, ja määrä pienenee eksponentiaalisesti kohti taustasäteilyn tasoa, noin 5 pulssia 10 "
            "sekunnissa. Pisteiden läpi on piirretty sovitettu käyrä A kertaa e potenssiin miinus C t plus B, ja "
            "taustasäteilyn taso B on vaakasuora katkoviiva. Pisteet ovat käyrän molemmin puolin.")
    ax = Axes(f, (100, 312), (476, 58), x=(0, 900), y=(0, 260), xticks=[150, 300, 450, 600, 750, 900], yticks=[50, 100, 150, 200, 250],
              xlabel=r"t\ (\text{s})", ylabel=r"\text{pulssia}\ /\ 10\,\text{s}")
    ax.line([(0, B), (900, B)], MUTED, 2, "8 6")
    f.tex(ax.X(15), ax.Y(B) - 18, r"B", "start", MUTED)
    ax.curve(lambda t: A * math.exp(-C * t) + B, 0, 900, COLD, 3)
    for t, y in zip(LA.BA_TS, LA.BA_Y): ax.point(t, y, HEAT)
    f.tex(ax.X(280), ax.Y(205), r"y = A\,e^{-Ct} + B", "start", COLD, bg=True)
    return f.svg()


def pa_points():
    """Task figure (Sovella, fitting): the simulated Pa-234m counts per 10 s as points, no fit."""
    f = Fig("fy89-pa", 380, "Kuvaaja mittakaavassa, simuloitu esimerkkiaineisto: protaktinium-234m-näytteen pulssimäärä 10 sekunnin "
            "jaksoissa ajan funktiona, aika nollasta 400 sekuntiin, 21 mittauspistettä 20 sekunnin välein. Pisteet ovat "
            "samat kuin tehtävän taulukossa: alussa 380 pulssia, lopussa noin 10 pulssia. Kuvaan ei ole piirretty sovitusta.")
    ax = Axes(f, (100, 312), (476, 58), x=(0, 400), y=(0, 400), xticks=[50, 100, 150, 200, 250, 300, 350, 400], yticks=[100, 200, 300, 400],
              xlabel=r"t\ (\text{s})", ylabel=r"\text{pulssia}\ /\ 10\,\text{s}",
              xfmt=lambda v: fi(v) if v % 100 == 0 else "")
    for t, y in zip(LA.PA_TS, LA.PA_Y): ax.point(t, y, HEAT)
    return f.svg()


def aktiivisuus():
    """Tarkista 2: the activity of an unknown sample, 720 kBq at t = 0, half-life 5,0 h (read off), 0–20 h."""
    A0, T = LA.CHK_A0, LA.CHK_T
    f = Fig("fy89-akt", 380, "Kuvaaja mittakaavassa: tuntemattoman radioaktiivisen näytteen aktiivisuus kilobecquereleinä ajan "
            "funktiona, aika nollasta 20 tuntiin, ruudukon väli 1 tunti ja 50 kilobecquerelia. Aktiivisuus on alussa 720 "
            "kilobecquerelia ja pienenee yhä loivemmin.")
    ax = Axes(f, (100, 312), (476, 58), x=(0, 20), y=(0, 800), xticks=list(range(1, 21)), yticks=list(range(50, 801, 50)),
              xlabel=r"t\ (\text{h})", ylabel=r"A\ (\text{kBq})",
              xfmt=lambda v: fi(v) if v % 4 == 0 else "", yfmt=lambda v: fi(v) if v % 200 == 0 else "")
    ax.curve(lambda t: A0 * 0.5 ** (t / T), 0, 20, HEAT, 3)
    ax.point(0, A0, HEAT)
    return f.svg()


def hero():
    """The chapter's opening illustration: a hospital isotope lab: a lead pot with a vial, a Geiger counter, a wall clock;
    above the vial a cluster of nuclei, some decayed, two decaying now."""
    f = H.hero("fy89-hero", "Kuvitus: sairaalan isotooppilaboratorio. Puupöydällä on paksuseinäinen lyijysuoja, jonka sisällä on "
               "pieni lasipullo radioaktiivista lääkettä. Pullon yllä leijuu suurennettuna joukko ytimiä: osa on oransseja "
               "hajoamattomia, osa harmaita renkaita eli jo hajonneita, ja kahdesta lähtee juuri säde. Vieressä on "
               "säteilymittari, jonka anturi osoittaa pulloa ja jonka viisari värähtää. Seinällä on kello.")
    H.tiles(f, 470, 75, RULE_LIGHT, PAPER)
    H.wood(f, 40, 470, 1120, 40, "fy89h-table")
    f.rect(80, 510, 30, 76, IRON, INK, 3); f.rect(1090, 510, 30, 76, IRON, INK, 3)
    # wall clock (left)
    H.stopwatch(f, 190, 170, 86, 0.35)
    # lead pot with an open lid and a vial
    f.rect(470, 330, 260, 140, IRON, INK, 3, 10)
    f.rect(450, 316, 300, 24, METAL_EDGE, INK, 3, 6)
    f.rect(560, 250, 80, 86, GLASS, INK, 3, 8)
    f.rect(574, 290, 52, 44, HEAT_LIGHT, None, 0, 4)
    f.rect(572, 232, 56, 22, ALUMINIUM, INK, 3, 4)
    # the lid leaning beside the pot
    f.path("M770,470 L800,330 L860,330 L840,470 Z", METAL_EDGE, INK, 3)
    # nuclei above the vial
    import random
    R = random.Random(4)
    pts = []
    while len(pts) < 26:
        x, y = 600 + R.uniform(-170, 170), 120 + R.uniform(-80, 80)
        if (x - 600) ** 2 / 170 ** 2 + (y - 120) ** 2 / 80 ** 2 < 1 and all((x - a) ** 2 + (y - b) ** 2 > 34 ** 2 for a, b in pts): pts.append((x, y))
    for k, (x, y) in enumerate(pts):
        if k % 3 == 0: f.circle(x, y, 11, "none", MUTED, 3)
        else: f.circle(x, y, 13, HEAT, WHITE, 2.5)
    for k in (1, 4):
        x, y = pts[k]
        f.circle(x, y, 22, "none", HEAT_LIGHT, 4)
        ang = -0.6 if k == 1 else 2.4
        f.arrow(x + 26 * math.cos(ang), y + 26 * math.sin(ang), x + 78 * math.cos(ang), y + 78 * math.sin(ang), HEAT, 5, 20)
    # Geiger counter (right) with a probe on a cable
    f.rect(900, 330, 200, 140, ALUMINIUM, INK, 3, 12)
    f.rect(924, 350, 152, 70, WHITE, INK, 2.5, 6)
    f.path("M940,410 A60,60 0 0 1 1060,410", "none", MUTED, 3)
    f.line(1000, 410, 1036, 366, HEAT, 4, cap="round"); f.circle(1000, 410, 6, INK)
    f.circle(940, 446, 10, INK); f.circle(1060, 446, 10, HEAT)
    f.path("M900,400 C860,400 840,300 800,280", "none", INK, 4)
    f.path("M800,280 L700,262 L696,284 L796,302 Z", IRON, INK, 3)
    f.rect(684, 258, 14, 30, INK, None, 0, 3)
    return f.svg()


# Graph choice of task fy8-9-L1-09: four (t, A) graphs on the same axes, A0 = 800 kBq and T½ = 2,0 h given; only
# "pick-puolittuu" is right (400, 200, 100, 50 kBq at 2, 4, 6, 8 h). The names say the drawn curve, not the answer.
PICK_A0, PICK_T = 800, 2.0
PICK_DESC = ("(t,A)-kuvaaja mittakaavassa: vaaka-akselilla aika t tunteina nollasta kahdeksaan tuntiin, apuviivat tunnin "
             "välein ja lukuarvot kahden tunnin välein; pystyakselilla aktiivisuus A kilobecquereleinä nollasta 900 "
             "kilobecquereliin, apuviivat 50 kilobecquerelin välein ja lukuarvot 200 kilobecquerelin välein. ")


def pick_graph(fid, label, fn):
    """One option: the same axes and the same curve colour and weight for every option."""
    f = Fig(fid, 360, PICK_DESC + label)
    ax = Axes(f, (100, 312), (476, 58), x=(0, 8), y=(0, 900), xticks=list(range(1, 9)), yticks=list(range(50, 901, 50)),
              xlabel=r"t\ (\text{h})", ylabel=r"A\ (\text{kBq})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v) if v % 200 == 0 else "")
    ax.curve(fn, 0, 8, HEAT, 3)
    return f.svg()


def pick_puolittuu():
    return pick_graph("fy89-pick-puolittuu", "Käyrä alkaa arvosta 800 kBq ja laskee yhä loivemmin: se kulkee pisteiden "
                      "(2 h; 400 kBq), (4 h; 200 kBq) ja (6 h; 100 kBq) kautta ja on hetkellä 8 h arvossa 50 kBq.",
                      lambda t: PICK_A0 * 0.5 ** (t / PICK_T))


def pick_suora():
    """The lesson's misconception: the decay goes on at a constant rate, so the rest decays in the second half-life."""
    return pick_graph("fy89-pick-suora", "Laskeva suora alkaa arvosta 800 kBq, kulkee pisteen (2 h; 400 kBq) kautta ja "
                      "osuu nollaan hetkellä 4 h. Sen jälkeen viiva kulkee vaaka-akselia pitkin arvossa nolla.",
                      lambda t: max(0.0, PICK_A0 * (1 - t / (2 * PICK_T))))


def pick_e():
    """λ taken as 1/T½ without ln 2: A = A0 e^(-t/T½), about 294 kBq at 2 h."""
    return pick_graph("fy89-pick-e", "Käyrä alkaa arvosta 800 kBq ja laskee yhä loivemmin: se kulkee noin pisteiden "
                      "(2 h; 290 kBq) ja (4 h; 110 kBq) kautta ja on hetkellä 8 h noin arvossa 15 kBq.",
                      lambda t: PICK_A0 * math.exp(-t / PICK_T))


def pick_kiihtyy():
    """The nuclei taken to have a memory: the decay speeds up, A = A0 (1 - t²/8 h²), zero at about 2,8 h."""
    return pick_graph("fy89-pick-kiihtyy", "Käyrä alkaa arvosta 800 kBq ja laskee yhä jyrkemmin: se kulkee pisteen "
                      "(2 h; 400 kBq) kautta ja osuu nollaan noin hetkellä 2,8 h. Sen jälkeen viiva kulkee vaaka-akselia "
                      "pitkin arvossa nolla.",
                      lambda t: max(0.0, PICK_A0 * (1 - t * t / (2 * PICK_T ** 2))))


FIGURES = {"hero": hero, "ydin": ydin, "kuvaaja": kuvaaja, "sovitus": sovitus, "pa-points": pa_points, "aktiivisuus": aktiivisuus,
           "pick-puolittuu": pick_puolittuu, "pick-suora": pick_suora, "pick-e": pick_e, "pick-kiihtyy": pick_kiihtyy}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "ydin": "reveals: about half of 100 nuclei left after T½ and a quarter after 2 T½, at random places",
    "kuvaaja": "reveals: N = N0/2, N0/4, N0/8 at 1, 2, 3 half-lives",
    "sovitus": "reveals: Ba-137m counts with the fitted A e^(-Ct) + B and the background level B",
    "pa-points": "safe: simulated Pa-234m counts per 10 s, 0–400 s, points only, no fit",
    "aktiivisuus": "safe: activity curve of an unknown sample from 720 kBq over 0–20 h on a 1 h grid; the half-life is to be read off",
    "pick-puolittuu": "reveals: the right option of task fy8-9-L1-09 (800 kBq halving every 2,0 h)",
    "pick-suora": "safe: a wrong option of task fy8-9-L1-09 (a straight line from 800 kBq to zero at 4 h, decay at a constant rate)",
    "pick-e": "safe: a wrong option of task fy8-9-L1-09 (A0 e^(-t/T½), the decay constant taken as 1/T½)",
    "pick-kiihtyy": "safe: a wrong option of task fy8-9-L1-09 (the decay speeding up to zero at 2,8 h, as if nuclei aged)",
}
