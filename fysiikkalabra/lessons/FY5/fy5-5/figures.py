"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-5` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, GOOD,
                    GOOD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT,
                    SAND_DARK, GRAIN, PAPER, n)
import herolib as H

FORCE = HOT          # forces red (FY4/FY5 convention)
ACC = HEAT           # accelerations and the field strength orange
GAMMA = 6.674e-11


def hero():
    f = H.hero("fy55-hero", "Kuvitus: omenapuu kesäillan hämärässä niityllä. Yksi omena on irronnut oksasta ja on puolivälissä "
               "matkalla maahan; sen perässä on liikeviivoja. Taivaalla, puun oikealla puolella, paistaa täysikuu.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy55h-sky", INK, "#4f8fbf"))
    for k in range(40):
        f.circle(H.rnd(k, 3) * 1200, H.rnd(k + 200, 3) * 230, 1 + 1.4 * H.rnd(k + 400, 3), WHITE)
    # the full Moon, upper right, with maria
    f.add(f'<circle cx="930" cy="140" r="92" fill="{WHITE}" fill-opacity="0.18"/>')
    f.circle(930, 140, 66, PAPER)
    for dx, dy, r in ((-22, -14, 16), (14, 8, 21), (-6, 30, 10), (26, -26, 9)):
        f.add(f'<circle cx="{930 + dx}" cy="{140 + dy}" r="{r}" fill="{ALUMINIUM}" fill-opacity="0.75"/>')
    H.hills(f, "fy55h", 400, ["#8a96a3", "#6c757d"], amp=36, seed=4)
    f.rect(0, 470, 1200, 130, H.grad(f, "fy55h-grass", GOOD_LIGHT, GOOD))
    for k in range(60):
        x = H.rnd(k, 7) * 1200; y = 480 + H.rnd(k + 90, 7) * 110
        f.path(f"M{n(x)},{n(y)} l-4,-14 M{n(x)},{n(y)} l4,-12", stroke=GOOD, w=2)
    # the apple tree in the middle third
    f.path("M578,470 C584,420 584,360 574,300 L604,300 C598,360 602,420 616,470 Z", COPPER, INK, 3)
    f.path("M584,330 C560,300 530,290 500,282", stroke=COPPER, w=12, extra='stroke-linecap="round"')
    f.path("M598,320 C626,296 660,286 696,280", stroke=COPPER, w=12, extra='stroke-linecap="round"')
    for k, (cx, cy, r) in enumerate(((590, 200, 120), (480, 250, 84), (700, 246, 88), (540, 150, 80), (650, 150, 82), (596, 280, 70))):
        f.circle(cx, cy, r, GOOD)
        f.add(f'<circle cx="{cx - r * 0.3:g}" cy="{cy - r * 0.3:g}" r="{r * 0.55:g}" fill="{GOOD_LIGHT}" fill-opacity="0.3"/>')
    for k, (cx, cy) in enumerate(((470, 280), (520, 214), (640, 196), (708, 274), (566, 132), (668, 128), (610, 248), (430, 236))):
        f.circle(cx, cy, 13, HOT, INK, 2)
        f.path(f"M{cx},{cy - 13} l3,-8", stroke=INK, w=2)
    # the falling apple and its motion lines
    for k in range(3):
        f.line(760 + 9 * k, 300 + 12 * k, 760 + 9 * k, 348 + 6 * k, WHITE, 3, cap="round")
    f.circle(774, 386, 16, HOT, INK, 2.5)
    f.path("M774,370 l4,-10", stroke=INK, w=2.5)
    f.add('<path d="M778,362 q12,-8 18,2 q-10,6 -18,-2 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>')
    for k, (x, y) in enumerate(((520, 500), (650, 510), (700, 492))):
        f.add(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="9" fill="{HOT}" stroke="{INK}" stroke-width="2"/>')
    return f.svg()


def vuorovaikutus():
    f = Fig("fy55-vv", 360, "Kaavakuva, ei mittakaavassa: vasemmalla Maa, oikealla omena. Maa vetää omenaa voimalla F1, joka "
            "osoittaa omenasta kohti Maata, ja omena vetää Maata yhtä suurella voimalla F2, joka osoittaa Maan keskipisteestä "
            "kohti omenaa. Nuolet ovat yhtä pitkät. Omenan kiihtyvyys on 9,8 metriä sekunnissa toiseen, Maan kiihtyvyys "
            "noin 3 kertaa 10 potenssiin miinus 25 metriä sekunnissa toiseen.")
    H.earth(f, "fy55-vv", 150, 170, 118)
    f.circle(150, 170, 5, INK)
    f.arrow(150, 170, 270, 170, FORCE, 4, 18)
    f.tex(210, 140, r"\overline{F}_2", "middle", color=FORCE, bg=True)
    f.circle(500, 170, 18, HOT, INK, 2.5)
    f.path("M500,152 l4,-10", stroke=INK, w=2.5)
    f.add('<path d="M504,146 q12,-8 18,2 q-10,6 -18,-2 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>')
    f.arrow(500, 170, 380, 170, FORCE, 4, 18)
    f.tex(440, 140, r"\overline{F}_1", "middle", color=FORCE)
    f.tex(176, 330, r"\text{Maa: } a \approx 3 \cdot 10^{-25}\,\text{m/s}^2", "middle", color=ACC)
    f.tex(500, 220, r"\text{omena}", "middle")
    f.tex(500, 330, r"a = 9{,}8\,\text{m/s}^2", "middle", color=ACC)
    f.tex(300, 24, r"F_1 = F_2", "middle")
    return f.svg()


def kaava():
    f = Fig("fy55-kaava", 300, "Kaavakuva: kaksi palloa, vasemmalla suurempi massa m1 ja oikealla pienempi massa m2. Pallojen "
            "keskipisteiden välinen etäisyys r on merkitty mittajanalla pallojen alle. Kumpaankin palloon vaikuttaa yhtä suuri "
            "gravitaatiovoima kohti toista palloa: F1 vasemmasta pallosta oikealle ja F2 oikeasta pallosta vasemmalle.")
    f.defs_add(f'<radialGradient id="fy55-rock" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#6c757d"/></radialGradient>')
    for cx, r, lab in ((150, 70, "m_1"), (470, 42, "m_2")):
        f.circle(cx, 130, r, "url(#fy55-rock)", INK, 2.5)
        f.circle(cx, 130, 4.5, INK)
        f.line(cx, 130 + r + 6, cx, 248, MUTED, 1.5, "5 4")
    f.tex(150, 36, "m_1", "middle")
    f.tex(470, 64, "m_2", "middle")
    f.arrow(150, 130, 262, 130, FORCE, 4, 18)
    f.arrow(470, 130, 358, 130, FORCE, 4, 18)
    f.tex(244, 100, r"\overline{F}_1", "middle", color=FORCE)
    f.tex(376, 100, r"\overline{F}_2", "middle", color=FORCE)
    f.arrow(300, 240, 150, 240, INK, 2, 12)
    f.arrow(300, 240, 470, 240, INK, 2, 12)
    f.tex(300, 268, "r", "middle", bg=True)
    return f.svg()


def kuvaaja(points=True):
    f = Fig("fy55-graph", 360, "Kuvaaja mittakaavassa: vaaka-akselilla kappaleiden keskipisteiden etäisyys r metreinä nollasta "
            "kymmeneen, pystyakselilla gravitaatiovoima F mikronewtoneina nollasta 1800:aan, kun kummankin kappaleen massa on "
            "10 tonnia. Laskevan käyrän pisteet ovat r = 2 m, F = 1670 µN; r = 4 m, F = 417 µN; r = 6 m, F = 185 µN; "
            "r = 8 m, F = 104 µN ja r = 10 m, F = 66,7 µN. Katkoviivat näyttävät, että kun etäisyys kaksinkertaistuu kahdesta "
            "neljään metriin, voima pienenee neljäsosaan.")
    F = lambda r: GAMMA * 1e4 * 1e4 / r ** 2 * 1e6
    ax = Axes(f, (96, 306), (480, 72), x=(0, 10), y=(0, 1800), xticks=[2, 4, 6, 8, 10], yticks=[600, 1200, 1800],
              xlabel=r"r\ (\text{m})", ylabel=r"F\ (\mu\text{N})")
    ax.curve(F, 2, 10, FORCE, 3)
    for r in (2, 4): ax.guide(r, F(r))
    for r in (2, 4, 6, 8, 10): ax.point(r, F(r))
    f.tex(ax.X(2) + 14, ax.Y(F(2)) + 2, r"F", "start", color=FORCE)
    f.tex(ax.X(4) + 12, ax.Y(F(4)) - 26, r"\tfrac{F}{4}", "start", color=FORCE)
    f.tex(ax.X(7.2), 92, r"m_1 = m_2 = 10\,\text{t}", "middle", bg=True)
    f.tex(ax.X(7.2), 130, r"2r \;\Rightarrow\; \tfrac{1}{4}F", "middle", bg=True)
    return f.svg()


def kentta():
    f = Fig("fy55-kentta", 380, "Kaavakuva, ei mittakaavassa: Maa keskellä. Kahden Maan säteen etäisyydellä keskipisteestä on "
            "katkoviivalla piirretty ympyrä, jonka seitsemästä pisteestä lähtee yhtä pitkä oranssi nuoli g kohti Maan "
            "keskipistettä. Ympyrän oikeassa reunassa on pieni kappale, johon vaikuttaa punainen voima F = mg kohti Maan keskipistettä.")
    cx, cy, R = 250, 200, 78
    H.earth(f, "fy55-ke", cx, cy, R)
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{2 * R}" fill="none" stroke="{RULE}" stroke-width="1.5" stroke-dasharray="6 6"/>')
    for k in range(1, 8):
        a = k * math.pi / 4
        x0, y0 = cx + 2 * R * math.cos(a), cy + 2 * R * math.sin(a)
        x1, y1 = cx + (2 * R - 46) * math.cos(a), cy + (2 * R - 46) * math.sin(a)
        f.circle(x0, y0, 3.5, INK)
        f.arrow(x0, y0, x1, y1, ACC, 3, 13)
    f.tex(cx + 2 * R * math.cos(-math.pi / 4) + 14, cy - 2 * R * math.sin(math.pi / 4) - 14, r"\overline{g}", "start", color=ACC)
    bx = cx + 2 * R                                   # a small body on the circle: the force on it F = mg, towards the centre
    f.arrow(bx, cy, bx - 58, cy, FORCE, 4, 15)
    f.rect(bx - 12, cy - 12, 24, 24, SAND_LIGHT, INK, 2, 3)
    f.tex(bx + 20, cy, r"m", "start")
    f.tex(bx - 30, cy + 40, r"\overline{F} = m\overline{g}", "start", color=FORCE)
    f.tex(cx, cy - 2 * R - 20, r"r = 2R", "middle", bg=True)
    return f.svg()


def planeetat():
    data = (("Kuu", 1.62, "1{,}62"), ("Mars", 3.71, "3{,}71"), ("Maa", 9.80, "9{,}80"), ("Jupiter", 24.8, "24{,}8"))
    f = Fig("fy55-planeetat", 360, "Kuva, nuolten pituudet mittakaavassa: neljä pintaa vierekkäin, Kuu, Mars, Maa ja Jupiter. "
            "Kunkin pinnan yllä on pieni pallo ja siitä alaspäin oranssi nuoli, jonka pituus on gravitaatiokentän voimakkuus "
            "eli putoamiskiihtyvyys pinnalla: Kuu 1,62, Mars 3,71, Maa 9,80 ja Jupiter 24,8 metriä sekunnissa toiseen.")
    colours = (("#c4ccd4", "#8a96a3"), ("#f2a69c", "#b8622d"), ("#a9d1f0", "#2f74b5"), ("#f1dfb5", "#d9b26a"))
    for k, ((name, g, gs), (c1, c2)) in enumerate(zip(data, colours)):
        x = 84 + 144 * k
        f.defs_add(f'<linearGradient id="fy55-pl{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')
        f.path(f"M{x - 62},268 Q{x},250 {x + 62},268 V300 H{x - 62} Z", f"url(#fy55-pl{k})", INK, 2)
        y0 = 70
        f.circle(x, y0 - 12, 11, WHITE, INK, 2)
        L = g * 7.0
        f.arrow(x, y0, x, y0 + L, ACC, 3.5, 14)
        f.tex(x, 326, r"\text{" + name + "}", "middle")
        f.tex(x, 26, gs + r"\,\text{m/s}^2", "middle", color=ACC)
    f.tex(84 + 3 * 144 + 14, 150, r"\overline{g}", "start", color=ACC)
    return f.svg()


def rakenteet():
    f = Fig("fy55-rak", 330, "Kaavakuva kolmessa vaiheessa vasemmalta oikealle, ei mittakaavassa. Ensin lähes tasainen kaasu- ja "
            "pölypilvi, jossa on hieman tiheämpi kohta. Sitten tiheämmät kohdat ovat kasvaneet, ja nuolet näyttävät ympäröivän "
            "aineen virtaavan niitä kohti. Lopuksi tiheimpään kohtaan on syntynyt tähti, jonka ympärillä kiertää litteä kiekko ja "
            "pieniä planeettoja. Vaiheiden välillä on aikaa kuvaavat nuolet.")
    for k, cx in enumerate((100, 300, 500)):
        if k < 2: f.line(200 + 200 * k, 40, 200 + 200 * k, 250, RULE, 2, "6 6")
    for i in range(110):                                  # 1: almost even cloud, a slightly denser spot
        x = 22 + H.rnd(i, 11) * 156; y = 64 + H.rnd(i + 300, 11) * 170
        if i % 5 == 0: x, y = 112 + (x - 100) * 0.25, 140 + (y - 150) * 0.25
        f.circle(x, y, 3, MUTED)
    for i in range(110):                                  # 2: clumps have grown, matter flows in
        cxs = ((262, 118), (330, 182)); c = cxs[i % 2]
        rr = 4 + 34 * H.rnd(i, 12) ** 2; a = H.rnd(i + 500, 12) * 6.283
        f.circle(c[0] + rr * math.cos(a), c[1] + rr * math.sin(a), 3, MUTED)
    for c in ((262, 118), (330, 182)):
        for a in (0.4, 2.2, 4.0, 5.6):
            f.arrow(c[0] + 62 * math.cos(a), c[1] + 62 * math.sin(a), c[0] + 40 * math.cos(a), c[1] + 40 * math.sin(a), FORCE, 2.5, 10)
    f.add(f'<ellipse cx="500" cy="150" rx="86" ry="22" fill="{HEAT_LIGHT}" fill-opacity="0.45" stroke="{HEAT}" stroke-width="1.5"/>')
    f.defs_add(f'<radialGradient id="fy55-star" cx="0.45" cy="0.45" r="0.6"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.circle(500, 150, 26, "url(#fy55-star)")
    for x, y, r in ((430, 146, 5), (566, 156, 6), (548, 136, 4)): f.circle(x, y, r, COPPER, INK, 1.5)
    f.tex(100, 290, r"\text{kaasupilvi}", "middle")
    f.tex(300, 290, r"\text{tihentymiä}", "middle")
    f.tex(500, 290, r"\text{tähti}", "middle")
    for x in (200, 400): f.arrow(x - 22, 22, x + 22, 22, INK, 2.5, 12)
    return f.svg()


FIGURES = {"hero": hero, "vuorovaikutus": vuorovaikutus, "kaava": kaava, "kuvaaja": kuvaaja, "kentta": kentta,
           "planeetat": planeetat, "rakenteet": rakenteet}
