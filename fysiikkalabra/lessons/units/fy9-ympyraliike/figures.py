"""Figures of the FY9 unit fy9-ympyraliike (scripts/figlib.py, fbd.py, herolib.py); `python3 scripts/units.py figures
fy9-ympyraliike` writes them into content/fi/units/fy9-ympyraliike/unit.md. The unit is Finnish, so the decimal sign is
a comma.

hero        the Why scene: a winter twilight, a red wooden house with a satellite dish on its gable pointing low into the
            sky at a television satellite on the geostationary arc (no text, no people)
kartta      the concept map of the review: the force diagram and Newton's second law first, then three branches
            (equilibrium, circular motion, gravitation and satellites), each with its three laws
geo         the hook answered to scale, seen from above the North Pole: the Earth and the geostationary orbit (radii in
            the ratio 6,6), the satellite with its velocity and the gravitational force, the dish's line of sight, and the
            same line 6 h later turned with the Earth
tilanteet   three force diagrams for the Kaava section: a plank on two supports (at rest), a car at the top of a bump
            and a satellite (only gravity), each with what the forces add up to
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, HEAT_LIGHT, HEAT, HOT,
                    COLD, COLD_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, COPPER, n)
from fbd import FBD
import herolib as H

figlib.set_language({}, ",")

# the hook (computed here and quoted in unit.md and inquiry.json)
GM = 6.674e-11 * 5.97e24                 # m^3/s^2, the Earth
R_E = 6371e3                             # m
T_GEO = 23 * 3600 + 56 * 60              # s, one turn of the Earth (23 h 56 min)
R_GEO = (GM * T_GEO ** 2 / (4 * math.pi ** 2)) ** (1 / 3)   # 42 157 km
V_GEO = 2 * math.pi * R_GEO / T_GEO                          # 3074 m/s


def _satellite(f, cx, cy, s=1.0, panel=COLD, body=SAND_DARK):
    """A small communications satellite: a box body with a dish, two long solar panels with cell lines."""
    for sgn in (-1, 1):
        x0 = cx + sgn * 16 * s
        x1 = cx + sgn * 92 * s
        f.line(x0, cy, x0 + sgn * 10 * s, cy, METAL_EDGE, 3 * s)
        f.rect(min(x0 + sgn * 10 * s, x1), cy - 13 * s, 66 * s, 26 * s, panel, INK, 2 * s)
        for k in range(1, 4):
            xx = min(x0 + sgn * 10 * s, x1) + k * 16.5 * s
            f.line(xx, cy - 13 * s, xx, cy + 13 * s, COLD_LIGHT, 1.2 * s)
        f.line(min(x0 + sgn * 10 * s, x1), cy, max(x0 + sgn * 10 * s, x1), cy, COLD_LIGHT, 1.2 * s)
    f.rect(cx - 16 * s, cy - 18 * s, 32 * s, 36 * s, body, INK, 2 * s, 3 * s)
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy + 26 * s)}" rx="{n(14 * s)}" ry="{n(6 * s)}" fill="{WHITE}" stroke="{INK}" stroke-width="{n(1.5 * s)}"/>')
    f.line(cx, cy + 18 * s, cx, cy + 22 * s, INK, 1.5 * s)


def hero():
    """Winter twilight in the Finnish countryside: a red wooden house with snow on its roof, a satellite dish on the
    gable aimed low up to the left, its faint dashed line of sight reaching a satellite on a dashed arc across the
    sky (the geostationary belt); stars, a dark forest edge, snow banks and spruces."""
    f = H.hero("fy9yl-hero", "Kuvitus: talvinen iltahämärä maaseudulla. Keskellä on punainen puutalo, jonka katolla on lunta ja "
               "ikkunoissa valoa. Talon päätyseinässä on lautasantenni, joka on suunnattu matalalle vasemmalle taivaalle. Antennista "
               "lähtee himmeä katkoviiva taivaalla olevaan televisiosatelliittiin, jolla on kaksi aurinkopaneelia. Satelliitti on "
               "taivaan poikki kulkevalla katkoviivakaarella. Taivaalla on tähtiä, taustalla metsän reuna ja edessä lumipenkkoja ja kuusia.")
    f.defs_add('<linearGradient id="fy9yl-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22406a"/>'
               '<stop offset="0.62" stop-color="#6f93bb"/><stop offset="1" stop-color="#f3d7b4"/></linearGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy9yl-sky)")
    for k in range(60):
        x, y = H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 250
        f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(1 + 1.4 * H.rnd(k + 700, 3))}" fill="{WHITE}" fill-opacity="{0.45 + 0.5 * H.rnd(k + 90, 3):.2f}"/>')
    # the geostationary belt as an arc across the sky, the satellite on it
    f.path("M40,300 Q600,40 1160,300", "none", WHITE, 2, extra='stroke-dasharray="3 10" stroke-opacity="0.55" stroke-linecap="round"')
    sx, sy = 430, 196
    _satellite(f, sx, sy, 1.0)
    # forest edge and snow
    H.forest(f, 430, 60, 36, "#24394e", seed=4, depth=30)
    H.forest(f, 446, 46, 30, "#2c4a5f", seed=8, depth=24)
    f.path("M0,452 Q300,440 600,450 T1200,446 V600 H0 Z", "#eef3f8")
    f.path("M0,540 Q360,526 720,540 T1200,534 V600 H0 Z", "#dfe8f0")
    # the house
    hx, hb, hw, hh = 560, 506, 300, 150
    H.red_house(f, hx, hb, hw, hh, snow=True)
    for k in range(int((hw - 40) / 70)):                                  # warm light in the windows
        wx = hx + 30 + k * 70
        f.rect(wx + 3, hb - hh * 0.72 + 3, 34, hh * 0.4 - 6, HEAT_LIGHT)
        f.line(wx + 20, hb - hh * 0.72, wx + 20, hb - hh * 0.32, WHITE, 3)
        f.rect(wx, hb - hh * 0.72, 40, hh * 0.4, "none", INK, 2)
    f.rect(hx + hw - 66, hb - 92, 40, 92, "#7a2a20", INK, 2.5)             # the door
    f.rect(hx + hw - 66, hb - 8, 40, 8, WHITE)
    # the dish on the left gable wall, pointing up-left at the satellite
    mx, my = hx + 40, hb - hh + 26                                         # the wall mount
    f.rect(mx - 6, my - 6, 12, 26, IRON, INK, 2)
    f.line(mx, my, mx - 34, my - 18, IRON, 5, cap="round")                 # the arm
    dx, dy = mx - 46, my - 30                                              # the dish centre
    ang = math.degrees(math.atan2(sy - dy, sx - dx))                       # the aim
    f.line(dx, dy, sx + 4, sy + 30, WHITE, 2, dash="4 10")
    f.add(f'<ellipse cx="{n(dx)}" cy="{n(dy)}" rx="{n(13)}" ry="{n(34)}" fill="{WHITE}" stroke="{INK}" stroke-width="2.5" '
          f'transform="rotate({n(ang)} {n(dx)} {n(dy)})"/>')
    ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    f.line(dx - 20 * uy, dy + 20 * ux, dx + 44 * ux, dy + 44 * uy, INK, 2.5)   # the feed arm
    f.rect(dx + 44 * ux - 6, dy + 44 * uy - 6, 12, 12, ALUMINIUM, INK, 2, 2)   # the LNB
    # snow banks and spruces in front
    f.path("M0,560 Q120,520 260,548 Q360,568 430,600 H0 Z", WHITE)
    f.path("M900,600 Q980,552 1080,560 Q1150,566 1200,548 V600 Z", WHITE)
    for x, h, c in ((110, 230, "#2b6a3e"), (220, 170, "#2f5a41"), (1000, 200, "#2b6a3e"), (1110, 250, "#2f5a41")):
        H.spruce(f, x, 556, h, c)
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: the method at the top, a spine down the left and three boxes (equilibrium,
    circular motion, gravitation), each with three laws and a grey word beside each."""
    f = Fig("fy9yl-kartta", 620, "Käsitekartta. Ylhäällä solmu: voimakuvio ensin, sitten Newtonin toinen laki summa F = m a. "
            "Siitä lähtee alas kolme haaraa. Tasapaino: momentti M = F r, voimien summa on nolla, joten kappale ei etene, ja "
            "momenttien summa on nolla, joten se ei kierry. Ympyräliike: ratanopeus v = 2 pii r jaettuna T:llä, normaalikiihtyvyys "
            "a n = v toiseen jaettuna r:llä osoittaa keskipisteeseen, ja liikeyhtälö summa F = m v toiseen jaettuna r:llä. "
            "Gravitaatio: vetovoima F = gamma m 1 m 2 jaettuna r toiseen, kentän voimakkuus g = gamma M jaettuna r toiseen ja "
            "satelliitin ratanopeus v = neliöjuuri gamma M jaettuna r:llä.", width=380, size=20)
    groups = [
        ("tasapaino", [(r"M = Fr", "momentti"), (r"\Sigma\overline{F} = \overline{0}", "ei etene"),
                       (r"\Sigma M = 0", "ei kierry")]),
        ("ympyräliike", [(r"v = 2\pi r/T", "ratanopeus"), (r"a_\text{n} = v^2/r", "keskipisteeseen"),
                         (r"\Sigma F = mv^2/r", "liikeyhtälö")]),
        ("gravitaatio", [(r"F = \gamma m_1 m_2/r^2", "vetovoima"), (r"g = \gamma M/r^2", "kenttä"),
                         (r"v = \sqrt{\gamma M/r}", "satelliitti")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 156, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{voimakuvio ensin}", "middle", INK)
    f.tex(190, hub_y + 51, r"\Sigma\overline{F} = m\overline{a}", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 66 + j * 37
            f.tex(x_box + 14, yy, law, "start", INK)
            if word: f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


def geo():
    """The hook to scale, seen from above the North Pole: the Earth (radius 35 units) and the geostationary orbit
    (radius 6,62 times as large, dashed). Both turn anticlockwise in 23 h 56 min. The satellite now, with its velocity
    (blue, along the tangent) and the Earth's gravitational force on it (red, to the centre); the dish's place on the
    Earth and the dashed line of sight to the satellite; 6 h later (a quarter turn) both the dish and the satellite
    have turned by 90°, drawn faint, and the line of sight is the same line turned with them."""
    f = Fig("fy9yl-geo", 600, "Kaavakuva pohjoisnavan suunnasta, säteet mittakaavassa. Keskellä Maa, jonka ympäri kulkee katkoviivalla "
            "geostationaarinen rata. Radan säde r on noin 42 200 km eli noin 6,6 Maan sädettä. Maa pyörii ja satelliitti kiertää "
            "samaan suuntaan, vastapäivään, ja kumpikin tekee kierroksen ajassa T = 23 h 56 min. Satelliitin sininen nopeusnuoli on "
            "radan tangentin suuntainen ja punainen gravitaatiovoiman nuoli osoittaa Maan keskipisteeseen. Maan pinnalla on antennin "
            "paikka, josta katkoviiva kulkee satelliittiin. Kuuden tunnin kuluttua antenni ja satelliitti ovat kumpikin kiertyneet "
            "neljänneskierroksen: himmeästi piirretty uusi näkösuora on sama viiva kiertyneenä.", size=26)
    cx, cy, Rg = 300, 318, 232
    Re = Rg * R_E / R_GEO                                                  # 35 units
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{Rg}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 7"/>')
    H.earth(f, "fy9yl-geo", cx, cy, Re)
    # the Earth's rotation: a curved arrow outside it
    ra = Re + 18
    a0, a1 = math.radians(200), math.radians(320)
    f.path(f"M{n(cx + ra * math.cos(a0))},{n(cy - ra * math.sin(a0))} A{n(ra)},{n(ra)} 0 0 0 {n(cx + ra * math.cos(a1))},{n(cy - ra * math.sin(a1))}",
           "none", INK, 2.5)
    ex, ey = cx + ra * math.cos(a1), cy - ra * math.sin(a1)
    tx, ty = -math.sin(a1), -math.cos(a1)                                  # anticlockwise tangent in figure coordinates
    f.path(f"M{n(ex + 12 * tx)},{n(ey + 12 * ty)} L{n(ex - 6 * ty)},{n(ey + 6 * tx)} L{n(ex + 6 * ty)},{n(ey - 6 * tx)} Z", INK)

    def place(th, faint=False):
        """The dish (on the Earth at angle th) and the satellite above it (on the orbit, 25° ahead) with their line."""
        op = ' stroke-opacity="0.35"' if faint else ""
        ax, ay = cx + Re * math.cos(th), cy - Re * math.sin(th)
        ph = th + math.radians(25)
        sx, sy = cx + Rg * math.cos(ph), cy - Rg * math.sin(ph)
        f.add(f'<line x1="{n(ax)}" y1="{n(ay)}" x2="{n(sx)}" y2="{n(sy)}" stroke="{INK}" stroke-width="2" stroke-dasharray="5 6"{op}/>')
        f.add(f'<circle cx="{n(ax)}" cy="{n(ay)}" r="6" fill="{HOT}" stroke="{WHITE}" stroke-width="2"{" fill-opacity=\"0.4\"" if faint else ""}/>')
        f.add(f'<rect x="{n(sx - 10)}" y="{n(sy - 10)}" width="20" height="20" rx="3" fill="{SAND_DARK}" stroke="{INK}" stroke-width="2"'
              f'{" fill-opacity=\"0.4\" stroke-opacity=\"0.4\"" if faint else ""}/>')
        return (ax, ay), (sx, sy), ph

    place(math.radians(160), faint=True)
    (ax, ay), (sx, sy), ph = place(math.radians(70))
    # velocity along the tangent (anticlockwise) and the force to the centre
    tx, ty = -math.sin(ph), -math.cos(ph)
    f.arrow(sx + 14 * tx, sy + 14 * ty, sx + 92 * tx, sy + 92 * ty, COLD, 3, 14)
    f.tex(sx + 92 * tx - 4, sy + 92 * ty - 22, r"\overline{v}", "middle", COLD)
    ux, uy = (cx - sx) / Rg, (cy - sy) / Rg
    f.arrow(sx + 14 * ux, sy + 14 * uy, sx + 84 * ux, sy + 84 * uy, HOT, 4, 18)
    f.tex(sx + 84 * ux + 28, sy + 84 * uy, r"\overline{F}", "middle", HOT)
    # labels
    f.tex(ax + 14, ay - 26, r"\text{antenni}", "start", INK)
    f.tex(cx - Rg + 10, cy - 40, r"\text{6 h myöhemmin}", "start", MUTED, bg=True)
    f.line(cx, cy, cx + Rg * math.cos(math.radians(-35)), cy - Rg * math.sin(math.radians(-35)), MUTED, 1.5)
    f.tex(cx + 116, cy + 112, r"r \approx 6{,}6\,R", "start", INK, bg=True)
    f.tex(cx, 26, r"T = 23\,\text{h}\;56\,\text{min}", "middle", INK)
    f.tex(cx, cy + Rg + 30, r"\text{radan säde } r \approx 42\,200\,\text{km}", "middle", MUTED)
    return f.svg()


def tilanteet():
    """Three force diagrams stacked for a phone, each object a plain rectangle with the forces from their points of
    application, lengths in one panel to scale: a uniform plank at rest on two supports 80 and 40 units from its centre
    (N2 = 2 N1, N1 + N2 = G); a car at the top of a bump (N shorter than G, acceleration down to the centre of the arc
    below); a satellite (only the gravitational force, acceleration to the Earth's centre)."""
    f = Fig("fy9yl-tilanteet", 690, "Kolme voimakuviota allekkain. Ylimpänä tasa-aineinen lankku levossa kahden tuen varassa "
            "suorakulmiona: paino G lähtee keskipisteestä alas, ja tukivoimat N 1 ja N 2 alapinnasta ylös. Tuki 2 on lähempänä "
            "keskipistettä, ja sen tukivoima on kaksi kertaa niin pitkä kuin N 1; yhdessä ne ovat painon pituiset. Ehdot: voimien "
            "summa ja momenttien summa ovat nolla. Keskellä auto nyppylän huipulla suorakulmiona: paino G alas ja tukivoima N "
            "ylös, painoa lyhyempänä. Auton vieressä sininen nopeusnuoli eteenpäin ja oranssi kiihtyvyysnuoli alas kohti kaaren "
            "keskipistettä. Ehto: G miinus N on m v toiseen jaettuna r:llä. Alimpana satelliitti suorakulmiona: ainoa voima on "
            "Maan gravitaatiovoima F alas kohti Maan keskipistettä. Vieressä nopeusnuoli eteenpäin ja kiihtyvyysnuoli alas. "
            "Ehto: gravitaatiovoima on m v toiseen jaettuna r:llä.", width=380, size=20)
    # 1. the plank
    f.tex(12, 20, r"\text{lankku levossa: } \Sigma\overline{F} = \overline{0},\ \Sigma M = 0", "start", INK)
    cx, cy = 190, 112
    d = FBD(f, 1.0, body=(cx, cy, 250, 22), a_dir=(0, 0))
    d.force("G", (0, -84), (cx, cy), "gravity", lab=(-18, 10))
    d.force("N_1", (0, 28), (cx - 80, cy + 11), "normal", surface=0, lab=(0, -18))
    d.force("N_2", (0, 56), (cx + 40, cy + 11), "normal", surface=0, lab=(24, -10))
    d.draw()
    f.line(10, 226, 370, 226, RULE, 1.5, "6 6")
    # 2. the car at the top of a bump
    f.tex(12, 256, r"\text{nyppylän huippu: } G - N = m\dfrac{v^2}{r}", "start", INK)
    cx, cy = 150, 358
    f.path(f"M40,{cy + 64} Q{cx},{cy + 34} 260,{cy + 64}", "none", MUTED, 2, extra='stroke-dasharray="6 6"')
    d = FBD(f, 1.0, body=(cx, cy, 110, 44), a_dir=(0, -1))
    d.force("G", (0, -78), (cx, cy), "gravity", lab=(-20, 6))
    d.force("N", (0, 46), (cx + 26, cy + 22), "normal", surface=0, lab=(0, -18))
    d.motion(r"\overline{v}", (1, 0), (cx + 70, cy - 12), length=64)
    d.motion(r"\overline{a}", (0, -1), (cx + 112, cy + 2), length=56, lab=(22, -6))
    d.draw()
    f.line(10, 458, 370, 458, RULE, 1.5, "6 6")
    # 3. the satellite
    f.tex(12, 490, r"\text{satelliitti: } \gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}", "start", INK)
    cx, cy = 150, 572
    f.path(f"M20,676 Q{cx},646 300,676", "none", MUTED, 3)
    d = FBD(f, 1.0, body=(cx, cy, 60, 36), a_dir=(0, -1))
    d.force("F", (0, -56), (cx, cy), "gravity", lab=(-20, 4))
    d.motion(r"\overline{v}", (1, 0), (cx + 44, cy - 6), length=64)
    d.motion(r"\overline{a}", (0, -1), (cx + 86, cy + 2), length=56, lab=(22, -6))
    d.draw()
    f.tex(328, 646, r"\text{Maa}", "middle", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "geo": geo, "tilanteet": tilanteet}
REUSE = {"kartta": "reveals: the key laws of FY5 equilibrium, circular motion and gravitation",
         "geo": "reveals: the geostationary orbit to scale (r ≈ 6,6 R) and why the dish keeps pointing at the satellite",
         "tilanteet": "reveals: model force diagrams of a plank on two supports, a car at the top of a bump and a satellite"}
