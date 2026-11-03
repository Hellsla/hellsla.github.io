"""Figures of this lesson (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy5-2` writes them into lesson.md.
Force diagrams are drawn with fbd.py: the body a plain rectangle, every force from its point of application, lengths to
one scale per figure (docs/force-diagrams.md). Numbers come from lesson-answers.py (g = 9,81 m/s²)."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN,
                    WATER, WATER_LIGHT, GLASS, ICE, IRON, ALUMINIUM, METAL_EDGE, COLD, COLD_LIGHT, HEAT, HEAT_LIGHT, n)
from fbd import FBD, ground
import herolib as H

g = 9.81
WOOD, WOOD_EDGE = SAND_DARK, GRAIN


def dim(f, x1, x2, y, tex, above=True, color=INK):
    """A dimension line from x1 to x2 at height y with end ticks and its label above (or below) the middle."""
    f.line(x1, y, x2, y, color, 1.5)
    for x in (x1, x2): f.line(x, y - 7, x, y + 7, color, 1.5)
    f.tex((x1 + x2) / 2, y - 18 if above else y + 20, tex, "middle", color)


def cmark(f, x, y, r=7):
    """The centre-of-mass symbol: a disc in quarters."""
    f.circle(x, y, r, WHITE, INK, 1.5)
    f.path(f"M{n(x)},{n(y)} V{n(y - r)} A{r},{r} 0 0 1 {n(x + r)},{n(y)} Z", INK)
    f.path(f"M{n(x)},{n(y)} V{n(y + r)} A{r},{r} 0 0 1 {n(x - r)},{n(y)} Z", INK)


def turn_arrow(f, cx, cy, r, a0, a1, color=INK, w=2.5):
    """A circular arc from angle a0 to a1 (degrees, anticlockwise on the page when a1 > a0) with a filled head at a1."""
    p = lambda a: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1 - (6 if a1 > a0 else -6))
    big = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    f.path(f"M{n(x0)},{n(y0)} A{r},{r} 0 {big} {sweep} {n(x1)},{n(y1)}", stroke=color, w=w)
    tx, ty = p(a1)
    d = 1 if a1 > a0 else -1                                   # tangent direction at a1 on the page
    ux, uy = -math.sin(math.radians(a1)) * d, -math.cos(math.radians(a1)) * d
    hx, hy = tx - ux * 12, ty - uy * 12
    f.path(f"M{n(tx)},{n(ty)} L{n(hx - uy * 6)},{n(hy + ux * 6)} L{n(hx + uy * 6)},{n(hy - ux * 6)} Z", color)


# --- the opening illustration: a painter's plank on two trestles, a paint tin on the overhang --------------------------
def hero():
    f = H.hero("fy52-hero", "Kuvitus: talon seinän edessä on kaksi maalauspukkia ja niiden päällä pitkä lankku. Lankun oikea pää "
               "ulottuu reilusti oikeanpuoleisen pukin yli, ja ulokkeen päällä on maalipurkki ja sivellin. Maalari seisoo "
               "maassa lankun vieressä. Kuvasta herää kysymys, kuinka kauas ulokkeelle kuormaa voi viedä ennen kuin lankku kaatuu.")
    H.sky(f, "fy52h", 470)
    H.cloud(f, 230, 110, 0.9); H.cloud(f, 1010, 80, 0.7)
    # the house wall: yellow boards with a window, under construction
    f.rect(120, 120, 960, 350, SAND_LIGHT)
    for x in range(120, 1080, 32): f.line(x, 120, x, 470, SAND, 2)
    f.path("M100,128 L600,40 L1100,128 Z", HOT)
    f.rect(470, 190, 170, 150, GLASS, INK, 3); f.line(555, 190, 555, 340, INK, 3); f.line(470, 265, 640, 265, INK, 3)
    f.rect(458, 340, 194, 14, WHITE, INK, 2)
    # the half-painted part of the wall
    f.rect(120, 120, 300, 350, HOT_LIGHT, extra='fill-opacity="0.55"')
    # grass
    f.rect(0, 470, 1200, 130, H.grad(f, "fy52h-grass", GOOD_LIGHT, GOOD))
    for k in range(40): f.line(20 + k * 30, 480 + 40 * H.rnd(k), 26 + k * 30, 470 + 40 * H.rnd(k), GOOD, 2)
    # two trestles (A-frames) and the plank
    yt = 392
    for cx in (440, 780):
        for dx in (-46, 46): f.path(f"M{cx},{yt} L{cx + dx},{530}", stroke=WOOD_EDGE, w=12, extra='stroke-linecap="round"')
        f.rect(cx - 40, yt - 4, 80, 14, WOOD, WOOD_EDGE, 2.5, 3)
        f.line(cx - 30, 470, cx + 30, 470, WOOD_EDGE, 6)
    f.rect(320, yt - 22, 680, 18, H.grad(f, "fy52h-plank", SAND_DARK, SAND), WOOD_EDGE, 2.5, 3)
    for x in range(350, 980, 70): f.line(x, yt - 13, x + 34, yt - 13, WOOD_EDGE, 1.5)
    # paint tin and brush on the overhang
    f.rect(918, yt - 84, 56, 62, ALUMINIUM, METAL_EDGE, 3, 4)
    f.rect(918, yt - 66, 56, 22, COLD); f.rect(912, yt - 90, 68, 10, METAL_EDGE, INK, 2, 3)
    f.path(f"M926,{yt - 90} Q946,{yt - 136} 966,{yt - 90}", stroke=INK, w=3)
    f.path(f"M860,{yt - 30} L900,{yt - 26}", stroke=WOOD_EDGE, w=8, extra='stroke-linecap="round"')
    f.rect(838, yt - 34, 26, 12, COLD, INK, 1.5, 2)
    # the painter on the ground beside the plank
    H.person(f, 230, 560, shirt=COLD, trousers=INK, sc=1.05)
    return f.svg()


# --- Ydinajatus: forces that cancel do not always keep a body still ------------------------------------------------------
def couple():
    f = Fig("fy52-pari", 330, "Kaavakuva, viivain pöydällä ylhäältä katsottuna, kaksi tapausta. Vasemmalla yhtä suuret ja "
            "vastakkaiset voimat F1 ja F2 vetävät viivaimen päistä viivaimen suuntaisesti samalla suoralla: voimien summa ja "
            "momenttien summa ovat nolla, eikä viivain kierry. Oikealla yhtä suuret ja vastakkaiset voimat vaikuttavat "
            "viivaimen päihin kohtisuoraan sitä vastaan eri suorilla: voimien summa on nolla, mutta momenttien summa ei, ja "
            "viivain alkaa kiertyä, mitä kuvaa kaareva nuoli.")
    f.line(300, 20, 300, 316, RULE, 2, "6 6")
    f.tex(150, 26, r"\text{ei kierry}", "middle")
    f.tex(450, 26, r"\text{kiertyy}", "middle")
    for cx in (150, 450):
        f.rect(cx - 80, 158, 160, 24, ALUMINIUM, METAL_EDGE, 1.5)
        for k in range(1, 16): f.line(cx - 80 + k * 10, 158, cx - 80 + k * 10, 158 + (8 if k % 5 else 13), INK, 1)
    d = FBD(f, 1.0, body=(150, 170, 160, 24), a_dir=(0, 0), draw_body=False)
    d.force("F_1", (-52, 0), (70, 170), kind="applied", lab=(10, -26))
    d.force("F_2", (52, 0), (230, 170), kind="applied", lab=(4, -26))
    d.draw()
    d = FBD(f, 1.0, body=(450, 170, 160, 24), a_dir=(0, 0), draw_body=False)
    d.force("F_1", (0, 70), (372, 158), kind="applied", lab=(-26, 6))
    d.force("F_2", (0, -70), (528, 182), kind="applied", lab=(26, -6))
    d.draw()
    turn_arrow(f, 450, 170, 50, 150, 30)            # F1 up at the left end, F2 down at the right: clockwise
    f.tex(150, 268, r"\Sigma\overline{F} = \overline{0}", "middle")
    f.tex(150, 304, r"\Sigma M = 0", "middle")
    f.tex(450, 268, r"\Sigma\overline{F} = \overline{0}", "middle")
    f.tex(450, 304, r"\Sigma M \neq 0", "middle", HOT)
    return f.svg()


# --- Ydinajatus: a low and a tall box on the same 30° slope, to scale -------------------------------------------------
def tipping():
    f = Fig("fy52-kaatuu", 372, "Kaavakuva mittakaavassa: kaksi laatikkoa samalla 30 asteen kaltevalla tasolla, kitka estää "
            "liukumisen. Matala laatikko on 0,60 m leveä ja 0,60 m korkea, korkea laatikko 0,30 m leveä ja 0,80 m korkea. "
            "Kummankin painopisteestä lähtee pystysuora katkoviiva alas tasoon. Matalan laatikon viiva osuu laatikon "
            "pohjan kohdalle, joten se pysyy pystyssä. Korkean laatikon viiva osuu tasoon pohjan alemman reunan "
            "ulkopuolelle, joten se kaatuu, mitä kuvaa kaareva nuoli.")
    x0, y0, ang, px = 40, 340, 30, 150                          # slope foot, angle, px per metre
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    ground(f, x0, 560, y0, angle=ang)
    f.line(x0, y0, x0 + 120, y0, MUTED, 1.5, "5 4")
    f.path(f"M{x0 + 80},{y0} A80,80 0 0 0 {n(x0 + 80 * c)},{n(y0 - 80 * s)}", stroke=INK, w=1.5)
    f.tex(x0 + 92, y0 - 20, r"30^\circ", "start")
    S = lambda d: (x0 + d * c, y0 - d * s)                       # a point d units up the slope
    for sc, b, h, ok in ((150, 0.60, 0.60, True), (420, 0.30, 0.80, False)):
        bw, bh = b * px, h * px
        bx, by = S(sc)
        cx, cy = bx - (bh / 2) * s, by - (bh / 2) * c            # centre: half the height out of the slope
        f.rect(cx - bw / 2, cy - bh / 2, bw, bh, SAND_LIGHT, GRAIN, 2.5, 2, extra=f'transform="rotate(-{ang} {n(cx)} {n(cy)})"')
        # the base on the slope, and where the plumb line through the centre of mass meets the slope
        p1, p2 = S(sc - bw / 2), S(sc + bw / 2)
        f.line(p1[0], p1[1] + 1, p2[0], p2[1] + 1, GOOD if ok else MUTED, 5, cap="round")
        sp = sc - (bh / 2) * math.tan(math.radians(ang))
        hx, hy = S(sp)
        f.line(cx, cy, hx, hy, INK, 2, "6 5")
        f.circle(hx, hy, 6, GOOD if ok else HOT, WHITE, 2)
        cmark(f, cx, cy)
        if ok: f.tex(cx + 4, cy - bh / 2 - 46, r"\text{pysyy}", "middle", GOOD)
        else:
            turn_arrow(f, p1[0], p1[1], bh * 0.95, 112, 150, HOT)
            f.tex(cx + 58, cy - 30, r"\text{kaatuu}", "start", HOT)
    return f.svg()


# --- Kaava: the plank on two supports, its force diagram and the arms from the centre of mass ----------------------------
def plank_fbd(fid, label, N1, N2, wrong=None, arms=None):
    """Plank 4,0 m (20 kg) on supports at 0,5 m and 3,0 m from its left end: rectangle 440 × 22 units, 110 units per metre."""
    f = Fig(fid, 290, label)
    X = lambda x: 80 + 110 * x
    cy, hh = 130, 11
    d = FBD(f, 0.6, body=(300, cy, 440, 2 * hh), a_dir=None if wrong else (0, 0), wrong=wrong)
    d.force("G", (0, -20 * g), (300, cy), kind="gravity", lab=(26, -6))
    d.force("N_1", (0, N1), (X(0.5), cy + hh), kind="normal", surface=0, push=True, lab=(0, 18))
    d.force("N_2", (0, N2), (X(3.0), cy + hh), kind="normal", surface=0, push=True, lab=(0, 18))
    d.draw()
    cmark(f, 300, cy)
    for x in (X(0.5), X(3.0), 300): f.line(x, cy - hh - 4, x, 64, MUTED, 1.5, "4 4")
    a1, a2 = arms or (r"r_1", r"r_2")
    dim(f, X(0.5), 300, 72, a1)
    dim(f, 300, X(3.0), 72, a2)
    f.tex(470, 92, r"\text{lankku}", "middle")
    return f.svg()


def kaava_plank():
    return plank_fbd("fy52-lankku", "Voimakuvio: tasa-aineinen lankku kahden tuen varassa, suorakulmiona. Paino G lähtee lankun "
                     "keskeltä painopisteestä alas. Tukivoimat N1 ja N2 osoittavat ylös ja päättyvät lankun alapintaan tukien "
                     "kohdalla. Tuki 1 on etäisyydellä r1 painopisteestä ja tuki 2 lyhyemmällä etäisyydellä r2. Nuolten "
                     "pituudet ovat mittakaavassa: N2 on pidempi kuin N1, ja yhdessä ne ovat yhtä pitkät kuin G.",
                     20 * g * 1.0 / 2.5, 20 * g * 1.5 / 2.5)


def error_plank():
    return plank_fbd("fy52-virhe", "Opiskelijan piirtämä voimakuvio: tasa-aineinen lankku kahden tuen varassa suorakulmiona. Tuki 1 "
                     "on 1,5 m ja tuki 2 1,0 m päässä lankun keskikohdasta. Paino G lähtee lankun keskeltä alas. Tukivoimat N1 "
                     "ja N2 osoittavat ylös ja päättyvät lankun alapintaan. Nuolet N1 ja N2 ovat yhtä pitkät, ja yhdessä ne ovat "
                     "yhtä pitkät kuin G.",
                     20 * g / 2, 20 * g / 2, wrong="tukivoimat on piirretty yhtä suuriksi, vaikka tuet ovat eri etäisyydellä painopisteestä",
                     arms=(r"1{,}5\,\text{m}", r"1{,}0\,\text{m}"))


# --- Esimerkki: the log carried by A (front end) and B (1,00 m from the rear end) -------------------------------------
def log_fbd():
    f = Fig("fy52-hirsi", 330, "Voimakuvio: tasa-aineinen hirsi suorakulmiona. Kantaja A on hirren vasemmassa päässä ja kantaja B "
            "1,00 m:n päässä oikeasta päästä. Paino G lähtee hirren keskeltä alas. Kantajien voimat NA ja NB osoittavat ylös ja "
            "päättyvät hirren alapintaan. Etäisyydet: A:sta painopisteeseen 2,00 m, painopisteestä B:hen 1,00 m. "
            "Momenttipisteeksi on merkitty A ja positiiviseksi kiertosuunnaksi vastapäivään. Nuolten pituudet ovat mittakaavassa.")
    X = lambda x: 80 + 110 * x
    cy, hh = 160, 13
    G = 60.0 * g; NB = G * 2.0 / 3.0; NA = G - NB
    f.rect(80, cy - hh, 440, 2 * hh, SAND_LIGHT, GRAIN, 2.5, 6)
    d = FBD(f, 0.2, body=(300, cy, 440, 2 * hh), a_dir=(0, 0), draw_body=False)
    d.force("G", (0, -G), (300, cy), kind="gravity", lab=(26, -4))
    d.force("N_A", (0, NA), (X(0.0) + 1, cy + hh), kind="normal", surface=0, push=True, tex=r"\overline{N}_\text{A}", lab=(8, 18))
    d.force("N_B", (0, NB), (X(3.0), cy + hh), kind="normal", surface=0, push=True, tex=r"\overline{N}_\text{B}", lab=(0, 18))
    d.draw()
    cmark(f, 300, cy)
    for x in (X(0.0), X(2.0), X(3.0), X(4.0)): f.line(x, cy - hh - 4, x, 98, MUTED, 1.5, "4 4")
    dim(f, X(0.0), X(2.0), 106, r"2{,}00\,\text{m}")
    dim(f, X(2.0), X(3.0), 106, r"1{,}00\,\text{m}")
    dim(f, X(3.0), X(4.0), 106, r"1{,}00\,\text{m}")
    f.circle(X(0.0), cy, 5, INK)
    f.tex(X(0.0) - 14, cy, r"\text{A}", "end")
    f.tex(X(3.0) + 30, cy + 40, r"\text{B}", "start")
    turn_arrow(f, X(0.0) + 34, 268, 26, -60, 200)
    f.tex(X(0.0) + 76, 268, r"+", "start")
    return f.svg()


# --- Sovella: the diving board (situation picture and model force diagram) -------------------------------------------
def board_scene():
    f = Fig("fy52-lauta", 360, "Tilannekuva: uima-altaan reunalla on 4,00 m pitkä hyppylauta. Laudan takapää on kiinnitetty "
            "pultilla altaan reunan betoniin, ja 1,50 m:n päässä takapäästä lauta lepää tukipalkin päällä. Laudan etupää "
            "ulottuu veden ylle, ja sen päässä seisoo hyppääjä. Lauta on tasa-aineinen ja vaakasuorassa.")
    X = lambda x: 80 + 110 * x
    yt = 214                                                     # the board's bottom face
    f.rect(0, 0, 600, 360, GLASS)
    f.rect(320, 262, 280, 98, H.grad(f, "fy52l-water", WATER_LIGHT, WATER))
    f.path("M320,262 q20,-6 40,0 t40,0 t40,0 t40,0 t40,0 t40,0 t40,0", stroke=WHITE, w=2.5)
    f.rect(0, 234, 320, 126, RULE_LIGHT, INK, 2.5)               # the concrete pool edge
    for k in range(9): f.circle(20 + k * 34, 280 + 30 * H.rnd(k, 3), 3, RULE)
    f.rect(X(1.5) - 16, yt, 32, 20, IRON, INK, 2, 2)              # the support beam
    f.rect(X(0) - 4, yt - 20, 446, 20, H.grad(f, "fy52l-board", HOT_LIGHT, HOT), INK, 2.5, 4)
    f.rect(X(0) + 6, yt - 28, 12, 50, METAL_EDGE, INK, 2, 2)      # the bolt through the board into the concrete
    f.rect(X(0) + 1, yt - 32, 22, 8, METAL_EDGE, INK, 2, 2)
    H.person(f, X(4.0) - 24, yt - 20, shirt=COLD, trousers=INK, sc=0.44, arms="up")
    dim(f, X(0) + 12, X(1.5), 300, r"1{,}50\,\text{m}", above=False)
    f.line(X(0) + 12, 238, X(0) + 12, 330, MUTED, 1.5, "4 4")
    dim(f, X(0) + 12, X(4.0) - 4, 340, r"4{,}00\,\text{m}", above=True)
    f.tex(X(0) + 12, 58, r"\text{pultti}", "middle")
    f.line(X(0) + 12, 72, X(0) + 12, yt - 36, MUTED, 1.5)
    f.tex(X(1.5), 270, r"\text{tuki}", "middle", bg=True)
    return f.svg()


def board_fbd():
    f = Fig("fy52-lauta-voimat", 400, "Mallivoimakuvio: hyppylauta suorakulmiona. Pultin voima Fp lähtee laudan takapäästä alas. "
            "Tuen voima N osoittaa ylös ja päättyy laudan alapintaan 1,50 m:n päässä takapäästä; se on kuvan pisin nuoli. "
            "Laudan paino G lähtee laudan keskeltä alas, ja hyppääjän voima Fh painaa laudan etupään yläpintaa alas. Nuolten "
            "pituudet ovat mittakaavassa: N on yhtä pitkä kuin muut kolme yhteensä.")
    X = lambda x: 80 + 110 * x
    cy, hh = 150, 9
    Gl, Gh = 30.0 * g, 60.0 * g
    N = (Gl * 2.00 + Gh * 4.00) / 1.50; Fp = N - Gl - Gh
    d = FBD(f, 0.08, body=(300, cy, 440, 2 * hh), a_dir=(0, 0))
    d.force("F_p", (0, -Fp), (X(0) + 8, cy + hh), kind="other", tex=r"\overline{F}_\text{p}", lab=(30, -10))
    d.force("N", (0, N), (X(1.5), cy + hh), kind="normal", surface=0, push=True, lab=(0, 18))
    d.force("G", (0, -Gl), (300, cy), kind="gravity", lab=(24, 2))
    d.force("F_h", (0, -Gh), (X(4.0) - 8, cy - hh), kind="normal", surface=0, outward=(0, -1), push=True, tex=r"\overline{F}_\text{h}", lab=(-30, 0))
    d.draw()
    cmark(f, 300, cy)
    f.tex(470, 30, r"\text{hyppylauta}", "middle")
    # the axes and the positive turning direction chosen for the equations
    f.arrow(530, 300, 530, 248, INK, 2, 11); f.tex(540, 244, "y", "start")
    turn_arrow(f, 500, 352, 22, -60, 200)
    f.tex(532, 352, "+", "start")
    return f.svg()


# --- Tiivistelmä: a tower crane balanced by its counterweight --------------------------------------------------------
def scene():
    f = H.scene("fy52-scene", "Kuvitus: rakennustyömaan torninosturi. Pystysuoran tornin päällä on pitkä vaakapuomi, jonka toisessa "
                "päässä riippuu kuorma ja lyhyemmässä vastapuomissa on raskaat betoniset vastapainot. Nosturin alla on "
                "keskeneräinen talo.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy52s-sky", ICE, GLASS))
    H.cloud(f, 345, 128, 0.5)
    f.rect(0, 318, 600, 42, SAND)
    # the building under construction
    f.rect(330, 220, 190, 98, RULE_LIGHT, INK, 2)
    for x in (360, 410, 460): f.rect(x, 240, 30, 30, GLASS, INK, 1.5)
    f.rect(330, 206, 190, 14, IRON)
    # the tower: a lattice mast
    x0, x1, top = 196, 226, 74
    f.rect(x0 - 16, 306, 62, 14, IRON)
    f.line(x0, 306, x0, top, HEAT, 4); f.line(x1, 306, x1, top, HEAT, 4)
    for y in range(306, top, -22): f.line(x0, y, x1, y - 22, HEAT, 2); f.line(x0, y - 22, x1, y - 22, HEAT, 2)
    # the jib and the counter-jib
    f.rect(70, top - 14, 490, 14, HEAT, INK, 2)
    for x in range(80, 560, 24): f.line(x, top - 14, x + 12, top, INK, 1)
    f.path(f"M{x0},{top - 14} L{(x0 + x1) / 2},{top - 54} L{x1},{top - 14} Z", HEAT, INK, 2)
    f.line((x0 + x1) / 2, top - 54, 540, top - 14, INK, 1.5); f.line((x0 + x1) / 2, top - 54, 80, top - 14, INK, 1.5)
    f.rect(78, top, 64, 40, RULE, INK, 2, 2); f.line(78, top + 20, 142, top + 20, INK, 1.5)   # counterweight blocks
    f.rect(x1 + 2, top, 30, 26, GLASS, INK, 2, 3)                                          # the cab
    # the trolley, the hook and the load
    f.rect(452, top, 28, 10, IRON)
    f.line(466, top + 10, 466, 168, INK, 1.5)
    f.path("M460,168 h12 v8 q-6,10 -12,0 Z", IRON)
    f.line(466, 178, 432, 204, INK, 1.5); f.line(466, 178, 500, 204, INK, 1.5)
    f.rect(420, 204, 92, 14, METAL_EDGE, INK, 2)
    return f.svg()


FIGURES = {"hero": hero, "pari": couple, "kaatuu": tipping, "lankku": kaava_plank, "hirsi": log_fbd, "scene": scene,
           "virhe": error_plank, "lauta": board_scene, "lauta-voimat": board_fbd}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pari": "reveals: a couple turns a body although the forces cancel",
    "kaatuu": "reveals: the tall box tips because its plumb line misses the base",
    "lankku": "reveals: the support nearer the centre of mass carries more",
    "hirsi": "reveals: the force diagram of the worked example",
    "virhe": "safe: a deliberately wrong diagram (equal support forces), for an error-spotting task",
    "lauta": "safe: situation picture of a diving board, data only",
    "lauta-voimat": "reveals: the model force diagram of the diving board",
}
