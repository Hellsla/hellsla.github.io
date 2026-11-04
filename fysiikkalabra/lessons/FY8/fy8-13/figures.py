"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-13` writes them into lesson.md.
Gamma photons and the dose rate are orange (HEAT, as in the simulation), lead iron grey, tissue light red; alpha
radiation dark red. The numbers come from lesson-answers.py (imported, one source)."""
import importlib.util, math, pathlib
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, IRON,
                    METAL_EDGE, ALUMINIUM, COLD, COLD_LIGHT, ICE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GOOD, PAPER)
import herolib as H

_spec = importlib.util.spec_from_file_location("fy813_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)


def lahteet():
    """Ydinajatus: the Finnish average effective dose 5,9 mSv a year by source (STUK-A263, 2020, rounded), bars to scale."""
    rows = [("sisäilman radon", LA.SOURCES["radon"], 0), ("muu luonnon säteily", LA.SOURCES["luonto"], 1),
            ("terveydenhuolto", LA.SOURCES["terveydenhuolto"], 1)]
    f = Fig("fy813-lahteet", 360, "Vaakapylväskuvio mittakaavassa: suomalaisen keskimääräinen efektiivinen annos vuodessa "
            "lähteittäin, STUKin arvio vuoden 2018 tilanteesta, yhteensä noin 5,9 millisievertiä. Sisäilman radon noin 4, "
            "muu luonnon säteily eli maaperä, rakennukset, avaruus ja elimistön omat aineet yhteensä noin 1,1 ja "
            "terveydenhuolto noin 0,8 millisievertiä vuodessa. Radonin pylväs on selvästi pisin, yli kolme kertaa niin "
            "pitkä kuin seuraavan.")
    x0, x1, vmax = 262, 548, 4.5
    X = lambda v: x0 + v / vmax * (x1 - x0)
    for v in (1, 2, 3, 4):
        f.line(X(v), 34, X(v), 286, RULE_LIGHT, 1.5)
        f.line(X(v), 286, X(v), 293, INK, 2); f.tex(X(v), 310, fi(v), "middle")
    f.tex(x0 - 10, 310, "0", "end")
    for k, (name, v, light) in enumerate(rows):
        y = 74 + k * 76
        f.rect(x0, y - 18, X(v) - x0, 36, HEAT_LIGHT if light else HEAT, INK, 2)
        f.tex(x0 - 12, y, r"\text{" + name + "}", "end")
        f.tex(X(v) + 10, y, fi(v, 1), "start", INK)
    f.arrow(x0, 287, x1 + 26, 287, INK, 2.5, 13)
    f.line(x0, 287, x0, 32, INK, 2.5)
    f.tex(300, 340, r"H_\text{E}\ (\text{mSv/vuosi})", "middle")
    return f.svg()


def painotus():
    """Kaava: the same absorbed dose 1 mGy from gamma and from alpha radiation; the equivalent doses 1 mSv and 20 mSv."""
    f = Fig("fy813-painotus", 360, "Kaavakuva, ei mittakaavassa: kaksi samanlaista kudospalaa. Vasempaan tulee gammasäteilyä: "
            "aaltoviiva kulkee palan läpi, ja sen varrella on harvassa muutama ionisaatiokohta. Oikeaan osuu alfahiukkanen, "
            "jonka lyhyt paksu jälki pysähtyy palan sisään, ja jäljen varrella ionisaatiot ovat tiheässä. Molemmissa "
            "absorboitunut annos on D = 1 milligray. Gammasäteilyn painotuskerroin on 1, joten ekvivalenttiannos on "
            "1 millisievert; alfasäteilyn painotuskerroin on 20, joten ekvivalenttiannos on 20 millisievertiä.")
    for k, (title, wr, Hs) in enumerate(((r"\text{gammasäteily}", "1", "1"), (r"\text{alfasäteily}", "20", "20"))):
        x0 = 40 + k * 290
        f.tex(x0 + 115, 26, title, "middle")
        f.rect(x0 + 20, 54, 190, 140, HOT_LIGHT, INK, 2.5, 14)
        for i in range(8):                         # cells with their nuclei, above and below the track
            cx, cy = x0 + 48 + (i % 4) * 45, 80 if i < 4 else 168
            f.circle(cx, cy, 15, "none", WHITE, 2); f.circle(cx, cy, 5, HOT, None)
        if k == 0:
            d = f"M{x0 - 4},124"
            for j in range(16): d += f" q7,{-12 if j % 2 == 0 else 12} 14,0"
            f.path(d, "none", HEAT, 3)
            f.arrow(x0 + 220, 124, x0 + 236, 124, HEAT, 3, 12)
            for xx in (x0 + 64, x0 + 128, x0 + 184): f.circle(xx, 124, 5, INK)
        else:
            f.line(x0 - 4, 124, x0 + 132, 124, HOT, 9, cap="round")
            for j in range(13): f.circle(x0 + 32 + j * 8, 124 + (7 if j % 2 else -7), 4, INK)
        f.tex(x0 + 115, 222, r"D = 1\,\text{mGy}", "middle")
        f.tex(x0 + 115, 262, r"w_\text{R} = " + wr, "middle", INK)
        f.arrow(x0 + 115, 280, x0 + 115, 304, INK, 2.5, 11)
        f.tex(x0 + 115, 330, r"H_\text{T} = " + Hs + r"\,\text{mSv}", "middle", HOT if k else INK)
    f.line(300, 20, 300, 340, RULE, 2, "6 6")
    return f.svg()


def etaisyys():
    """Kaava, the inverse-square law: rays from a point source through 1, 4 and 9 squares at r, 2r and 3r."""
    f = Fig("fy813-etaisyys", 384, "Kaavakuva etäisyyden neliölaista. Vasemmalla pistemäinen säteilylähde, josta neljä "
            "säderajaa leviää oikealle. Etäisyydellä r säteet kulkevat yhden ruudun läpi, etäisyydellä 2 r saman "
            "säteilyn on jakauduttava 2 kertaa 2 eli neljälle samankokoiselle ruudulle ja etäisyydellä 3 r 3 kertaa 3 eli "
            "yhdeksälle ruudulle. Yhden ruudun läpi kulkee siis 2 r:n etäisyydellä neljäsosa ja 3 r:n etäisyydellä "
            "yhdeksäsosa säteilystä, joten suhteellinen annosnopeus on näillä etäisyyksillä 1, neljäsosa ja yhdeksäsosa.")
    sx, sy, u = 42, 160, 130                       # source, px per r
    s = 22                                          # half side of one square at r, px (vertical; the depth is drawn skewed)
    for k in (1, 2, 3):
        x, h = sx + k * u, s * k
        for i in range(k):
            for j in range(k):
                y = sy - h + 2 * s * i; dx = 0.45 * (2 * s * j - h + s)
                f.path(f"M{n(x + dx - 0.45 * s)},{n(y)} l{n(0.9 * s)},0 l0,{n(2 * s)} l{n(-0.9 * s)},0 Z", HEAT_LIGHT if (i == 0 and j == 0) else GLASS, INK, 1.5)
    for dy in (-1, 1):
        f.line(sx, sy, sx + 3 * u + 0.45 * 3 * s, sy + dy * 3 * s, HEAT, 2, "8 5")
    f.circle(sx, sy, 9, HEAT, INK, 2)
    for k, lab, frac in ((1, "r", "1"), (2, "2r", r"\dfrac{1}{4}"), (3, "3r", r"\dfrac{1}{9}")):
        x = sx + k * u
        f.line(x, 252, x, 268, MUTED, 2)
        f.tex(x, 286, lab, "middle")
        f.tex(x, 344, frac, "middle", HEAT)
    f.tex(sx + 40, 332, r"\dot{H}", "middle", HEAT)
    f.tex(sx + 40, 364, r"\text{suhteellinen}", "middle", HEAT)
    f.line(sx, 260, sx + 3 * u, 260, MUTED, 1.5)
    f.line(sx, 252, sx, 268, MUTED, 2)
    f.tex(sx, 286, "0", "middle")
    f.tex(sx + 4, 214, r"\text{lähde}", "middle")
    return f.svg()


def suoja():
    """Kaava, the puoliintumispaksuus d½ (half-value layer): the sim's dose rate behind 0–30 mm of lead, halving every 6,0 mm."""
    f = Fig("fy813-suoja", 380, "Kuvaaja mittakaavassa: annosnopeus mikrosieverteinä tunnissa lyijylevyn paksuuden funktiona, "
            "paksuus nollasta 30 millimetriin. Ilman lyijyä annosnopeus on 40, ja jokainen 6 millimetrin kerros puolittaa "
            "sen: 6 millimetrin kohdalla 20, 12 millimetrin kohdalla 10, 18 millimetrin kohdalla 5. Käyrä laskee yhä "
            "loivemmin eikä saavuta nollaa. Puoliintumispaksuus on merkitty vaakasuoralla hakasulkeella ensimmäisen kerroksen kohdalle.")
    ax = Axes(f, (100, 312), (484, 58), x=(0, 30), y=(0, 44), xticks=[6, 12, 18, 24, 30], yticks=[10, 20, 30, 40],
              xlabel=r"d\ (\text{mm})", ylabel=r"\dot{H}\ (\mu\text{Sv/h})")
    ax.curve(lambda x: LA.hdot(1.0, x), 0, 30, HEAT, 3)
    for x in (6, 12, 18):
        ax.guide(x, LA.hdot(1.0, x)); ax.point(x, LA.hdot(1.0, x), HEAT)
    ax.point(0, 40, HEAT)
    yb = ax.Y(43.5)
    f.line(ax.X(0), yb, ax.X(6), yb, INK, 2)
    f.line(ax.X(0), yb, ax.X(0), yb + 8, INK, 2); f.line(ax.X(6), yb, ax.X(6), yb + 8, INK, 2)
    f.tex(ax.X(6) + 12, yb, r"d_{1/2} = 6{,}0\,\text{mm}", "start", INK, bg=True)
    f.tex(ax.X(14), ax.Y(24), r"\dot{H} = \dot{H}_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}", "start", HEAT, bg=True)
    return f.svg()


def vaimennus():
    """Tarkista 2 (task figure): the dose rate behind 0–25 cm of concrete from 80 µSv/h; the half-value layer 5,0 cm is read off."""
    H0, D = LA.CHK_H0, LA.CHK_D
    f = Fig("fy813-vaimennus", 380, "Kuvaaja mittakaavassa: gammasäteilyn annosnopeus mikrosieverteinä tunnissa betoniseinän "
            "paksuuden funktiona, paksuus nollasta 25 senttimetriin, ruudukon väli 1 senttimetri ja 5 mikrosievertiä tunnissa, "
            "joka viides pystyviiva ja joka toinen vaakaviiva tummempi; vaaka-akselilla numerot 5 senttimetrin ja pystyakselilla "
            "10 mikrosievertin välein. "
            "Ilman betonia annosnopeus on 80, ja käyrä laskee yhä loivemmin.")
    ax = Axes(f, (100, 312), (484, 58), x=(0, 25), y=(0, 85), xticks=list(range(1, 26)), yticks=list(range(5, 86, 5)),
              xlabel=r"d\ (\text{cm})", ylabel=r"\dot{H}\ (\mu\text{Sv/h})",
              xfmt=lambda v: fi(v) if v % 5 == 0 else "", yfmt=lambda v: fi(v) if v % 10 == 0 else "")
    for v in range(5, 26, 5): f.line(ax.X(v), ax.Y(0), ax.X(v), ax.Y(85), RULE, 1.5)     # darker every 5 cm
    for v in range(10, 86, 10): f.line(ax.X(0), ax.Y(v), ax.X(25), ax.Y(v), RULE, 1.5)   # and every 10 µSv/h
    ax.curve(lambda x: H0 * 0.5 ** (x / D), 0, 25, HEAT, 3)
    ax.point(0, H0, HEAT)
    return f.svg()


def hero():
    """Opening illustration, neutral until the prediction about the largest source: a Finnish red house in winter on soil
    and granite bedrock, a passenger plane in the sky and a nuclear power plant far behind the forest; nothing marks a
    source (no radon is drawn: ennuste 3 asks for it)."""
    f = H.hero("fy813-hero", "Kuvitus: talvinen suomalainen maisema. Punainen omakotitalo on piirretty poikkileikkauksena: "
               "katolla on lunta, savupiipusta nousee savua ja talon alla on kellari. Maan alla on hiekkainen maakerros ja "
               "syvemmällä harmaa graniittikallio. Taivaalla lentää matkustajakone, ja kaukana metsän takana näkyy "
               "ydinvoimalaitoksen reaktorirakennus.")
    H.sky(f, "fy813h", 330, ICE, GLASS)
    H.sun(f, "fy813h-sun", 1000, 78, 42, rays=False)
    # a nuclear power plant far away: a boxy reactor building with a domed top and a turbine hall
    f.rect(20, 290, 70, 40, RULE_LIGHT, INK, 2); f.rect(60, 262, 46, 68, WHITE, INK, 2)
    f.path("M60,262 Q83,236 106,262 Z", WHITE, INK, 2); f.rect(112, 220, 8, 110, RULE_LIGHT, INK, 2)
    # a passenger plane high in the sky
    f.path("M300,96 L420,90 Q440,92 432,100 L300,104 Q292,100 300,96 Z", WHITE, INK, 2)
    f.path("M360,98 L336,128 L352,128 L392,99 Z", RULE_LIGHT, INK, 2)
    f.path("M304,97 L292,76 L304,76 L322,96 Z", RULE_LIGHT, INK, 2)
    # ground: snow, sandy soil, granite bedrock
    f.rect(0, 318, 1200, 20, WHITE)
    f.rect(0, 336, 1200, 124, H.grad(f, "fy813h-soil", SAND_LIGHT, SAND))
    for k in range(70):
        f.circle(20 + k * 17 + 8 * H.rnd(k), 352 + 96 * H.rnd(k, 3), 2.5, GRAIN)
    f.path("M0,460 Q150,440 300,462 T600,458 T900,464 T1200,452 V600 H0 Z", ALUMINIUM, INK, 2)
    for k in range(120):
        x, y = 10 + 1180 * H.rnd(k, 5), 476 + 116 * H.rnd(k, 6)
        f.circle(x, y, 3 + 3 * H.rnd(k, 7), IRON if k % 3 else HOT_LIGHT)
    # basement in the soil
    f.rect(430, 330, 340, 110, RULE_LIGHT, INK, 3)
    f.rect(444, 344, 312, 82, WHITE, INK, 2)
    # the house
    H.red_house(f, 420, 330, 360, 170, snow=True)
    f.rect(690, 156, 34, 70, IRON, INK, 3)
    H.smoke(f, 707, 140, 0.8, MUTED, 0.45)
    # trees
    H.spruce(f, 170, 330, 200); H.spruce(f, 300, 330, 150); H.spruce(f, 960, 330, 180); H.birch(f, 1112, 330, 170, leaves=False)
    return f.svg()


FIGURES = {"hero": hero, "lahteet": lahteet, "painotus": painotus, "etaisyys": etaisyys, "suoja": suoja, "vaimennus": vaimennus}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "lahteet": "reveals: the Finnish average dose by source (STUK-A263, 2020): radon about 4 of 5,9 mSv/a",
    "painotus": "reveals: the same 1 mGy gives 1 mSv from gamma and 20 mSv from alpha (w_R)",
    "etaisyys": "reveals: 1, 4 and 9 squares at r, 2r, 3r: the dose rate 1, 1/4, 1/9",
    "suoja": "reveals: 40 µSv/h halving every d½ = 6,0 mm of lead: 20, 10, 5 at 6, 12, 18 mm",
    "vaimennus": "safe: dose rate behind 0–25 cm of concrete from 80 µSv/h on a 1 cm grid; the half-value layer is to be read off",
}
