"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-4` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, WATER, WATER_LIGHT, GLASS, HEAT, HEAT_LIGHT, COPPER, SAND, SAND_LIGHT, GRAIN, fi
import herolib as H


def pressure_area():
    f = Fig("fy34-pa", 380, "Sama voima F kohdistuu samanlaiseen tiiliskiveen kahdella tavalla. Vasemmalla tiili on pystyssä "
            "ja koskettaa alustaa pienellä alalla A1, jolloin paine p1 = F/A1 on suuri. Oikealla tiili on kyljellään "
            "ja koskettaa alustaa kolme kertaa suuremmalla alalla A2 = 3 A1, jolloin paine p2 = F/A2 on kolmasosa "
            "vasemman paineesta. Voimanuolet ovat yhtä pitkät. Kontaktialat ovat mittakaavassa, kaaviokuva muuten.")
    f.defs_add(f'<pattern id="fy34-snow" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="{GLASS}"/>'
               f'<circle cx="3" cy="4" r="1.3" fill="{WATER_LIGHT}"/><circle cx="10" cy="10" r="1.3" fill="{WATER_LIGHT}"/></pattern>')
    ground = 240
    f.rect(12, ground, 576, 22, "url(#fy34-snow)", INK, 2)
    f.line(300, 30, 300, 330, RULE, 1.5, "7 6")
    # (centre x, brick width, brick height, subscript, title)
    for cx, bw, bh, k, title in ((150, 40, 120, "1", r"\text{pystyssä}"), (450, 120, 40, "2", r"\text{kyljellään}")):
        top = ground - bh
        f.tex(cx, 24, title, "middle")
        f.rect(cx - bw / 2, top, bw, bh, COPPER, INK, 2.5, 3)
        f.arrow(cx, top - 62, cx, top - 3, INK, 4, 18)                  # equal force arrows, equal length
        f.tex(cx + 14, top - 34, "F", "start")
        f.line(cx - bw / 2, ground + 1, cx + bw / 2, ground + 1, HEAT, 6)  # the contact area
        by = ground + 36                                                # bracket marking the area A
        f.path(f"M{n_(cx - bw / 2)},{by - 6} V{by + 6} M{n_(cx - bw / 2)},{by} H{n_(cx + bw / 2)} M{n_(cx + bw / 2)},{by - 6} V{by + 6}", stroke=INK, w=2)
        f.tex(cx, by + 24, f"A_{k}" if k == "1" else r"A_2 = 3A_1", "middle")
        f.tex(cx, 346, rf"p_{k} = \dfrac{{F}}{{A_{k}}}", "middle")
    return f.svg()


def n_(v):
    return str(int(v)) if v == int(v) else f"{v:.1f}"


def water_column():
    f = Fig("fy34-col", 300, "Vesipatsas, jonka pohjan pinta-ala on A ja korkeus syvyys h. Patsaan paino G = ρAhg painaa "
            "pohjaa alaspäin, ja paine on paino jaettuna alalla, p = G/A = ρgh: pinta-ala supistuu pois. Kaaviokuva, "
            "ei mittakaavassa.")
    f.defs_add('<linearGradient id="fy34-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/>'
               '<stop offset="1" stop-color="#2f74b5"/></linearGradient>')
    f.rect(30, 50, 340, 230, "url(#fy34-water)", extra='fill-opacity="0.55"')
    f.line(30, 50, 370, 50, WATER, 3)
    f.path("M30,22 V280 H370 V22", stroke=INK, w=3)
    f.tex(44, 34, r"\text{vesipinta}", "start")
    f.rect(170, 50, 80, 170, WATER, INK, 2, extra='fill-opacity="0.3" stroke-dasharray="7 5"')
    f.line(170, 220, 250, 220, INK, 6)
    f.arrow(210, 80, 210, 214, INK, 4, 26)
    f.tex(160, 135, "G", "end", size=30)
    f.tex(210, 252, "A", "middle", size=30)
    f.line(275, 50, 275, 220, INK, 2)
    f.line(267, 50, 283, 50, INK, 2)
    f.line(267, 220, 283, 220, INK, 2)
    f.tex(290, 135, "h", "start", size=30)
    f.tex(392, 40, r"\text{patsaan paino}", "start")
    f.tex(392, 76, r"G = \rho A h g", "start", size=28)
    f.tex(392, 130, r"\text{paine pohjalla}", "start")
    f.tex(392, 188, r"p = \dfrac{G}{A} = \rho g h", "start", size=28)
    return f.svg()


def pressure_depth():
    f = Fig("fy34-ph", 340, "Kuvaaja mittakaavassa: veden paine p kilopascaleina syvyyden h funktiona, kun h on 0–10 m. "
            "Paine on nouseva suora: pinnalla paine on ilmanpaine 101 kPa ja 10 metrin syvyydessä noin 199 kPa. "
            "Suoran ja katkoviivan väli on hydrostaattinen paine ρgh.")
    ax = Axes(f, (104, 285), (450, 70), x=(0, 10), y=(0, 240), xticks=[2, 4, 6, 8, 10], yticks=[50, 100, 150, 200],
              xlabel=r"h\ (\text{m})", ylabel=r"p\ (\text{kPa})")
    p0, p10 = 101, 101 + 1000 * 9.81 * 10 / 1000
    ax.line([(0, p0), (10, p10)], WATER, 4)
    ax.line([(0, p0), (10, p0)], MUTED, 2.5, "8 6")
    ax.point(0, p0)
    ax.point(10, p10)
    f.tex(ax.X(0) + 12, ax.Y(p0) + 30, r"\text{ilmanpaine}\ p_0 = 101\,\text{kPa}", "start", bg=True)
    f.tex(ax.X(8.3), ax.Y(222), r"p = p_0 + \rho g h", "end", WATER)
    bx = ax.X(10) + 22                                                  # bracket for the hydrostatic part
    f.path(f"M{bx - 6},{n_(ax.Y(p10))} H{bx} V{n_(ax.Y(p0))} H{bx - 6}", stroke=INK, w=2)
    f.tex(bx + 10, (ax.Y(p0) + ax.Y(p10)) / 2, r"\rho g h", "start")
    return f.svg()


def hero():
    """The chapter's opening illustration: a concrete dam that widens towards its base, a deep reservoir behind it."""
    f = H.hero("fy34-hero", "Kuvitus: betonipato vuoristolaaksossa sivulta nähtynä. Padon takana on syvä tekojärvi, jonka vesi "
               "tummuu syvyyden kasvaessa. Pato on yläreunasta kapea ja levenee alaspäin, pohjalta se on moninkertaisesti paksumpi.")
    H.sky(f, "fy34h", 600)
    H.cloud(f, 900, 100, 0.9)
    f.path("M0,260 L180,120 L330,230 L470,90 L640,250 L800,140 L1000,260 L1200,160 V600 H0 Z", H.ALUMINIUM)
    f.path("M0,300 L160,220 L300,290 L480,200 L620,300 L820,230 L1050,310 L1200,260 V600 H0 Z", H.METAL_EDGE)
    H.forest(f, 330, 40, 24, H.IRON, seed=2, x1=1200, depth=300)
    f.rect(0, 330, 1200, 270, H.RULE)
    f.path("M0,600 V560 Q300,540 600,560 Q900,580 1200,555 V600 Z", H.SAND)
    # reservoir: water darkens with depth
    f.path("M0,250 H560 L620,560 H0 Z", H.grad(f, "fy34h-water", H.WATER_LIGHT, H.WATER))
    for x, y, w in ((80, 280, 120), (300, 300, 90), (150, 340, 100)):
        f.path(f"M{x},{y} q{w / 4},-6 {w / 2},0 t{w / 2},0", stroke=H.WHITE, w=3, extra='stroke-linecap="round" stroke-opacity="0.7"')
    # dam: narrow crest, wide base
    f.path("M540,224 H600 L760,560 H560 Z", H.grad(f, "fy34h-concrete", H.RULE_LIGHT, H.RULE, horizontal=True), H.INK, 3)
    for y in (300, 380, 460):
        x0 = 540 + (y - 224) * 20 / 336; x1 = 600 + (y - 224) * 160 / 336
        f.line(x0 + 4, y, x1 - 4, y, H.RULE, 2)
    f.rect(530, 214, 80, 12, H.IRON, H.INK, 2)
    # river below the dam
    f.path("M760,560 Q900,520 1200,540 V600 H760 Z", H.grad(f, "fy34h-river", H.WATER_LIGHT, H.WATER))
    return f.svg()


def scene():
    """A second everyday scene: a diver deep in a lake with a depth gauge on the wrist."""
    f = H.scene("fy34-scene", "Kuvitus: sukeltaja on syvällä järvessä. Vesi tummuu syvemmälle mentäessä, ilmakuplat nousevat "
                "pintaan, ja sukeltajan ranteessa on syvyys- ja painemittari.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy34s-water", H.WATER_LIGHT, H.WATER))
    f.rect(0, 0, 600, 24, H.grad(f, "fy34s-sky", H.ICE, H.GLASS))
    f.path("M0,24 q25,-6 50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0", stroke=H.WHITE, w=3)
    f.path("M0,360 V320 Q150,300 300,330 T600,316 V360 Z", H.SAND)
    for x, y, r in ((360, 180, 6), (368, 150, 8), (356, 116, 10), (366, 78, 12), (358, 44, 14)): f.circle(x, y, r, "none", H.WHITE, 2.5)
    # diver swimming to the left: fins, legs, body, tank, head with mask, arm with the gauge
    f.add('<g transform="rotate(-8 300 230)">')
    f.path("M430,226 L500,206 L506,230 L436,246 Z", H.INK)
    f.path("M430,246 L500,252 L496,276 L428,262 Z", H.INK)
    f.rect(270, 214, 170, 44, H.INK, rx=22)
    f.rect(300, 192, 110, 26, H.ALUMINIUM, H.INK, 2.5, 13)
    f.circle(250, 230, 26, H.INK)
    f.rect(226, 218, 30, 18, H.GLASS, H.WHITE, 2, 6)
    f.path("M280,252 L216,276", stroke=H.INK, w=18, extra='stroke-linecap="round"')
    f.circle(232, 270, 11, H.WHITE, H.INK, 2.5)
    f.line(232, 270, 237, 263, H.INK, 2)
    f.add('</g>')
    return f.svg()


def two_liquids():
    """The (h, p) lines of two liquids with the same surface pressure, for a task (scripts/figcat.py variant of
    `pressure-depth`): the student reads the slopes off grid crossings; the description lists the points, not the densities."""
    f = Fig("fy34-two-liquids", 340, "Kuvaaja mittakaavassa: kahden nesteen paine p kilopascaleina syvyyden h funktiona, kun h on 0–10 m. "
            "Molemmissa paine pinnalla on 100 kPa. Neste A: suora kulkee pisteiden (0 m; 100 kPa), (5 m; 150 kPa) ja (10 m; 200 kPa) kautta. "
            "Neste B: suora kulkee pisteiden (0 m; 100 kPa), (5 m; 175 kPa) ja (10 m; 250 kPa) kautta. "
            "Ruudukon väli on 1 m ja 25 kPa.")
    ax = Axes(f, (100, 290), (470, 62), x=(0, 11), y=(0, 275), xticks=list(range(1, 11)), yticks=list(range(25, 251, 25)),
              xlabel=r"h\ (\text{m})", ylabel=r"p\ (\text{kPa})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v) if v % 50 == 0 else "")
    for pts, col, name in [([(0, 100), (10, 200)], WATER, "A"), ([(0, 100), (10, 250)], COPPER, "B")]:
        ax.line(pts, col, 3.5)
        f.tex(ax.X(10) + 14, ax.Y(pts[1][1]), r"\text{" + name + "}", "start", col)
    for h, p in [(0, 100), (5, 150), (10, 200)]:
        ax.point(h, p, WATER)
    for h, p in [(5, 175), (10, 250)]:
        ax.point(h, p, COPPER)
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "pressure-area": pressure_area, "water-column": water_column, "pressure-depth": pressure_depth, "two-liquids": two_liquids}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pressure-area": "reveals: p1 = 3 p2 for the same force",
    "water-column": "reveals: the derivation p = ρgh",
    "pressure-depth": "reveals: about 199 kPa at 10 m",
    "two-liquids": "safe: two (h, p) lines with the same surface pressure 100 kPa; the description lists their points, not the densities",
}
