"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-4` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, WATER, WATER_LIGHT, GLASS, HEAT, HEAT_LIGHT, COPPER, SAND, SAND_LIGHT, GRAIN, fi


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


FIGURES = {"pressure-area": pressure_area, "water-column": water_column, "pressure-depth": pressure_depth}
