"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-3` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, COLD, HOT, HEAT, WATER, ALUMINIUM, METAL_EDGE, IRON, fi)
import herolib as H


def system():
    f = Fig("fy33-system", 340, "Periaatekuva, ei mittakaavassa: kaasua sylinterissä, jonka yläpäätä sulkee liikkuva mäntä. "
            "Kaasu on termodynaaminen systeemi; sen rajapinta on piirretty katkoviivalla kaasun ympärille. Sylinterin "
            "seinät, mäntä ja koko muu maailma ovat ympäristöä. Systeemin tilaa kuvaavat tilanmuuttujat: paine p, "
            "tilavuus V ja lämpötila T.")
    # cylinder (aluminium), gas, piston
    f.rect(138, 150, 204, 140, GLASS)
    f.path("M126,110 V302 H354 V110 H342 V290 H138 V110 Z", ALUMINIUM, INK, 2.5)
    f.rect(138, 128, 204, 22, IRON, INK, 2.5)
    f.rect(234, 74, 12, 54, IRON, INK, 2.5)
    f.rect(206, 60, 68, 14, IRON, INK, 2.5, 3)
    # gas particles
    for x, y in [(226, 212), (282, 184), (322, 200), (256, 232), (306, 238), (212, 262), (270, 268), (322, 270),
                 (300, 208)]:
        f.circle(x, y, 5.5, WATER, WHITE, 1.5)
    # the boundary of the system
    f.rect(143, 155, 194, 130, "none", INK, 2.5, 4, 'stroke-dasharray="10 6"')
    # thermometer in the gas
    f.rect(158, 168, 8, 90, WHITE, INK, 2, 4)
    f.rect(160, 206, 4, 54, HOT)
    f.circle(162, 268, 9, HOT, INK, 2)
    f.tex(180, 190, "T", "start")
    # pressure: the gas pushes up on the piston
    for x in (262, 302):
        f.arrow(x, 176, x, 158, INK, 2.5, 11)
    f.tex(244, 169, "p", "end")
    # volume bracket
    f.line(104, 150, 142, 150, MUTED, 1.5, "5 4")
    f.line(104, 290, 142, 290, MUTED, 1.5, "5 4")
    f.arrow(110, 220, 110, 151, INK, 2, 11)
    f.arrow(110, 220, 110, 289, INK, 2, 11)
    f.tex(92, 220, "V", "end")
    # words with leaders
    for y, x1, word in ((235, 318, r"\text{systeemi}"), (190, 338, r"\text{rajapinta}")):
        f.line(402, y, x1, y, MUTED, 1.5)
        f.circle(x1, y, 3, MUTED)
        f.tex(412, y, word, "start")
    f.line(402, 120, 350, 120, MUTED, 1.5)
    f.circle(350, 120, 3, MUTED)
    f.tex(412, 120, r"\text{ympäristö}", "start")
    return f.svg()


def micro_model():
    f = Fig("fy33-micro", 300, "Kaaviokuva kaasun mikromallista: kaksi samankokoista suljettua astiaa, joissa on yhtä monta "
            "hiukkasta. Kylmässä kaasussa nopeutta kuvaavat nuolet ovat lyhyitä, kuumassa pitkiä, ja kuuman kaasun paine "
            "p2 on suurempi kuin kylmän kaasun paine p1.")
    cold = [(95, 105, 111, 121), (210, 100, 191, 111), (155, 155, 177, 155), (85, 190, 101, 174), (215, 200, 194, 192),
            (140, 215, 162, 219)]
    hot = [(385, 105, 416, 136), (500, 100, 462, 122), (445, 155, 489, 155), (375, 190, 406, 159), (505, 200, 464, 185),
           (430, 215, 473, 223)]
    for x, title in ((40, r"\text{kylmä kaasu}"), (330, r"\text{kuuma kaasu}")):
        f.tex(x + 115, 40, title, "middle")
        f.rect(x, 62, 230, 180, GLASS, INK, 3, 6)
    for pts, col in ((cold, COLD), (hot, HOT)):
        for x, y, x2, y2 in pts:
            f.arrow(x, y, x2, y2, INK, 2.5, 10)
            f.circle(x, y, 7, col, WHITE, 1.5)
    f.tex(155, 272, "p_1", "middle")
    f.tex(445, 272, r"p_2 \gt p_1", "middle", w=130)
    return f.svg()


def kelvin_scale():
    f = Fig("fy33-scale", 250, "Kelvinasteikko ja celsiusasteikko rinnakkain mittakaavassa: 0 K on −273,15 °C "
            "(absoluuttinen nollapiste), 273,15 K on 0 °C (vesi jäätyy) ja 373,15 K on 100 °C (vesi kiehuu). Asteikkojen "
            "välit ovat yhtä suuret, ja kelvinlukema saadaan lisäämällä celsiuslukemaan 273,15.")
    x0, s = 70, 1.2
    X = lambda K: x0 + s * K
    yk, yc = 112, 182
    for y in (yk, yc):
        f.arrow(x0 - 12, y, 545, y, INK, 2.5, 13)
    pts = [(0, "0\\,\\text{K}", "-273{,}15\\,{}^\\circ\\text{C}", COLD), (273.15, "273{,}15\\,\\text{K}", "0\\,{}^\\circ\\text{C}", COLD),
           (373.15, "373{,}15\\,\\text{K}", "100\\,{}^\\circ\\text{C}", HOT)]
    for K, kt, ct, col in pts:
        f.line(X(K), yk, X(K), yc, col, 3)
        f.line(X(K), yk - 8, X(K), yk + 8, INK, 2.5)
        f.line(X(K), yc - 8, X(K), yc + 8, INK, 2.5)
    f.tex(X(0) - 8, 76, pts[0][1], "start", w=70)
    f.tex(X(273.15), 76, pts[1][1], "middle", w=104)
    f.tex(X(373.15), 76, pts[2][1], "middle", w=104)
    f.tex(X(0) - 8, 218, pts[0][2], "start", w=130)
    f.tex(X(273.15), 218, pts[1][2], "middle", w=80)
    f.tex(X(373.15), 218, pts[2][2], "middle", w=90)
    f.tex(X(0) - 8, 30, r"\text{absoluuttinen nollapiste}", "start", w=250)
    f.tex(450, 30, r"\text{vesi jäätyy}", "end", w=118)
    f.tex(590, 30, r"\text{vesi kiehuu}", "end", w=118)
    f.tex(222, 147, r"T = \theta + 273{,}15", "middle", w=230, bg=True)
    f.tex(553, yk, r"T", "start", w=30)
    f.tex(553, yc, r"\theta", "start", w=30)
    return f.svg()


def extrapolation():
    f = Fig("fy33-extrap", 350, "Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella "
            "0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C. "
            "Pystyakseli on kuvan vasemmassa reunassa kohdassa −300 °C.")
    ax = Axes(f, (92, 290), (470, 84), x=(-300, 100), y=(0, 150), xticks=[-270, -200, -100, 0, 100],
              yticks=[25, 50, 75, 100, 125],
              xlabel=r"\theta\ (^\circ\text{C})", ylabel=r"p\ (\text{kPa})",
              xfmt=lambda v: ("-" if v < 0 else "") + fi(abs(v)), origin_label=False)
    f.tex(ax.x0 - 12, ax.y0, "0", "end")
    p0, k = 100, 0.37
    th0 = -p0 / k
    ax.line([(th0, 0), (0, p0)], MUTED, 3, "9 7")
    ax.line([(0, p0), (100, p0 + 100 * k)], INK, 3.5)
    for th, p in [(0, 100), (20, 107), (40, 115), (60, 122), (80, 129), (100, 137)]:
        ax.point(th, p)
    f.circle(ax.X(th0), ax.Y(0), 7, WHITE, COLD, 3)
    f.tex(ax.X(th0) + 4, ax.Y(0) - 40, r"p = 0", "start", COLD)
    f.tex(ax.X(-160), ax.Y(18), r"\text{ekstrapolointi}", "start", MUTED, bg=True)
    f.tex(ax.X(40), ax.Y(90), r"\text{mittaukset}", "start", INK, bg=True)
    return f.svg()


def hero():
    """The chapter's opening illustration: a bicycle on a hot summer street, heat shimmering above the asphalt."""
    f = H.hero("fy33-hero", "Kuvitus: polkupyörä seisoo kuumalla asfaltilla kesähelteellä. Aurinko paistaa, asfaltin yllä väreilee "
               "kuumuus ja tolpan lämpömittarin punainen pylväs on korkealla.")
    H.sky(f, "fy33h", 430)
    H.sun(f, "fy33h", 1020, 110)
    H.cloud(f, 300, 90, 0.9)
    for x, w, h in ((40, 220, 220), (280, 180, 170), (480, 240, 250), (740, 200, 190)):
        f.rect(x, 430 - h, w, h, H.WHITE, H.RULE, 3)
        for wx in range(x + 24, x + w - 40, 60):
            for wy in range(430 - h + 26, 400, 64):
                f.rect(wx, wy, 34, 40, H.GLASS, H.RULE, 2)
    f.rect(0, 430, 1200, 20, H.RULE_LIGHT, H.RULE, 2)
    f.rect(0, 450, 1200, 150, H.grad(f, "fy33h-road", H.IRON, H.INK))
    for x in range(40, 1200, 220): f.rect(x, 528, 110, 10, H.WHITE, rx=3)
    H.shimmer(f, (160, 240, 920, 1000, 1080), 520, 90)
    # bicycle
    for cx in (480, 760):
        f.circle(cx, 446, 82, "none", H.INK, 12)
        f.circle(cx, 446, 74, "none", H.METAL_EDGE, 2)
        for k in range(12):
            a = k * H.math.pi / 6
            f.line(cx, 446, cx + 70 * H.math.cos(a), 446 + 70 * H.math.sin(a), H.METAL_EDGE, 1.5)
        f.circle(cx, 446, 7, H.INK)
    for d in ("M480,446 L580,446 L700,330 L560,330 Z", "M580,446 L540,300", "M700,330 L760,446", "M700,330 L690,300"):
        f.path(d, stroke=H.COLD, w=10, extra='stroke-linecap="round"')
    f.path("M512,292 H572", stroke=H.INK, w=12, extra='stroke-linecap="round"')
    f.path("M670,296 Q690,286 716,298", stroke=H.INK, w=8, extra='stroke-linecap="round"')
    f.circle(580, 446, 16, H.ALUMINIUM, H.INK, 3)
    H.thermometer(f, 1120, 400, 160, H.HOT, 190)
    f.rect(1114, 400, 12, 50, H.IRON)
    return f.svg()


def scene():
    """A second everyday scene: the same bicycle on a frosty winter morning."""
    f = H.scene("fy33-scene", "Kuvitus: sama polkupyörä lumisena pakkasaamuna. Lunta on maassa ja satulalla, ja tolpan lämpömittarin "
                "pylväs on matalalla.")
    H.sky(f, "fy33s", 360, H.COLD_LIGHT, H.WHITE)
    H.forest(f, 240, 50, 26, H.ALUMINIUM, seed=7, depth=30)
    f.path("M0,250 Q300,236 600,252 V360 H0 Z", H.WHITE)
    for k in range(40): f.circle(H.rnd(k, 3) * 600, H.rnd(k + 70, 3) * 230, 2 + 2 * H.rnd(k + 9, 3), H.WHITE, H.ICE_EDGE, 1)
    for cx in (220, 400):
        f.circle(cx, 270, 52, "none", H.INK, 9)
        for k in range(12):
            a = k * H.math.pi / 6
            f.line(cx, 270, cx + 46 * H.math.cos(a), 270 + 46 * H.math.sin(a), H.METAL_EDGE, 1.2)
        f.circle(cx, 270, 5, H.INK)
    for d in ("M220,270 L284,270 L360,196 L270,196 Z", "M284,270 L258,178", "M360,196 L400,270", "M360,196 L354,176"):
        f.path(d, stroke=H.COLD, w=7, extra='stroke-linecap="round"')
    f.path("M240,172 H280", stroke=H.INK, w=9, extra='stroke-linecap="round"')
    f.path("M238,166 Q260,156 282,166", stroke=H.WHITE, w=7, extra='stroke-linecap="round"')
    f.path("M340,174 Q354,166 370,176", stroke=H.INK, w=6, extra='stroke-linecap="round"')
    f.path("M150,322 Q300,316 470,322", stroke=H.ICE_EDGE, w=2, extra='stroke-opacity="0.6"')
    H.thermometer(f, 520, 230, 30, H.COLD, 150)
    f.rect(514, 230, 12, 40, H.IRON)
    return f.svg()


def extrapolation_points():
    """Measurements of a gas at constant volume, for a task (scripts/figcat.py variant): the points without the
    fitted line or its extension, on axes reaching below 0 °C; the description lists the points, not the extrapolated value."""
    f = Fig("fy33-extrap-points", 330, "Kaasun paine lämpötilan funktiona suljetussa jäykässä astiassa: viisi mittauspistettä "
            "ilman piirrettyä suoraa. Pisteet ovat (0 °C; 75 kPa), (25 °C; 82 kPa), (50 °C; 89 kPa), (75 °C; 96 kPa) ja "
            "(100 °C; 102,5 kPa). Vaaka-akseli ulottuu −150 °C:een; ruudukon väli on 25 °C ja 25 kPa.")
    ax = Axes(f, (92, 290), (500, 56), x=(-150, 110), y=(0, 125), xticks=list(range(-125, 101, 25)),
              yticks=[25, 50, 75, 100], xlabel=r"\theta\ (^\circ\text{C})", ylabel=r"p\ (\text{kPa})",
              xfmt=lambda v: (("-" if v < 0 else "") + fi(abs(v))) if v % 50 == 0 else "", origin_label=False)
    for th, pr in [(0, 75), (25, 82), (50, 89), (75, 96), (100, 102.5)]:
        ax.point(th, pr, WATER)
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "system": system, "micro-model": micro_model, "kelvin-scale": kelvin_scale, "extrapolation": extrapolation, "extrapolation-points": extrapolation_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "system": "safe: a gas as a system and its state variables",
    "micro-model": "reveals: the hot gas has the higher pressure",
    "kelvin-scale": "reveals: the K–°C conversions",
    "extrapolation": "reveals: the zero-pressure temperature about −270 °C",
    "extrapolation-points": "safe: five (θ, p) points of a gas at constant volume without the line or its extension; the description lists the points",
}
