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


# --- the opening illustration: a painter on a plank over two trestles, a paint tin out on the overhang --------------
def _trestle(f, x, ytop, yg, gid):
    """A painter's trestle seen end-on: the beam's end under the plank and two legs splayed into an A, with a brace."""
    for dx in (-1, 1):
        f.path(f"M{n(x + dx * 8)},{n(ytop + 10)} L{n(x + dx * 58)},{n(yg)}", stroke=INK, w=17, extra='stroke-linecap="round"')
        f.path(f"M{n(x + dx * 8)},{n(ytop + 10)} L{n(x + dx * 58)},{n(yg)}", stroke=WOOD, w=12, extra='stroke-linecap="round"')
    f.rect(x - 38, ytop + 74, 76, 12, WOOD, WOOD_EDGE, 2, 3)            # the brace between the legs
    f.rect(x - 16, ytop, 32, 22, H.grad(f, gid, SAND_DARK, GRAIN), INK, 2.5, 3)   # the beam end the plank rests on


def _painter(f, x, yf, brush):
    """A painter in white overalls seen from behind, facing the wall: feet at (x, yf), the right hand up at brush."""
    s = 333 / 420                                                     # 1,75 m at 190 units per metre
    for dx in (-1, 1):                                                # legs
        f.path(f"M{n(x + dx * 8 * s)},{n(yf - 190 * s)} L{n(x + dx * 24 * s)},{n(yf - 14 * s)}", stroke=INK, w=40 * s, extra='stroke-linecap="round"')
        f.path(f"M{n(x + dx * 8 * s)},{n(yf - 190 * s)} L{n(x + dx * 24 * s)},{n(yf - 14 * s)}", stroke=WHITE, w=34 * s, extra='stroke-linecap="round"')
        f.path(f"M{n(x + dx * 24 * s - 16 * s)},{n(yf - 6 * s)} h{n(32 * s)}", stroke=INK, w=16 * s, extra='stroke-linecap="round"')
    sh = (x, yf - 330 * s)
    f.path(f"M{n(sh[0] - 42 * s)},{n(sh[1] + 16 * s)} L{n(x - 48 * s)},{n(yf - 196 * s)}", stroke=INK, w=27 * s, extra='stroke-linecap="round"')   # left arm down
    f.path(f"M{n(sh[0] - 42 * s)},{n(sh[1] + 16 * s)} L{n(x - 48 * s)},{n(yf - 196 * s)}", stroke=WHITE, w=21 * s, extra='stroke-linecap="round"')
    f.circle(x - 49 * s, yf - 186 * s, 11 * s, SAND_LIGHT)
    f.path(f"M{n(x - 46 * s)},{n(yf - 312 * s)} Q{n(x - 50 * s)},{n(yf - 342 * s)} {n(x)},{n(yf - 344 * s)} Q{n(x + 50 * s)},{n(yf - 342 * s)} {n(x + 46 * s)},{n(yf - 312 * s)} "
           f"L{n(x + 40 * s)},{n(yf - 176 * s)} H{n(x - 40 * s)} Z", WHITE, INK, 3)                      # the overalls' back
    f.path(f"M{n(x - 22 * s)},{n(yf - 340 * s)} L{n(x - 26 * s)},{n(yf - 230 * s)} M{n(x + 22 * s)},{n(yf - 340 * s)} L{n(x + 26 * s)},{n(yf - 230 * s)}", stroke=RULE, w=4)
    f.rect(x - 30 * s, yf - 228 * s, 60 * s, 34 * s, RULE_LIGHT, INK, 2, 4)                            # the back pocket
    f.path(f"M{n(x + 40 * s)},{n(sh[1] + 14 * s)} L{n(brush[0] - 6)},{n(brush[1] + 14)}", stroke=INK, w=27 * s, extra='stroke-linecap="round"')   # right arm up
    f.path(f"M{n(x + 40 * s)},{n(sh[1] + 14 * s)} L{n(brush[0] - 6)},{n(brush[1] + 14)}", stroke=WHITE, w=21 * s, extra='stroke-linecap="round"')
    f.circle(brush[0] - 4, brush[1] + 10, 11 * s, SAND_LIGHT)
    f.rect(x - 10 * s, yf - 368 * s, 20 * s, 28 * s, SAND_LIGHT)                                        # neck
    hc = (x, yf - 394 * s)
    f.circle(hc[0], hc[1], 32 * s, GRAIN)                                                                # hair, from behind
    f.path(f"M{n(hc[0] - 34 * s)},{n(hc[1] - 4 * s)} Q{n(hc[0] - 32 * s)},{n(hc[1] - 40 * s)} {n(hc[0])},{n(hc[1] - 40 * s)} Q{n(hc[0] + 32 * s)},{n(hc[1] - 40 * s)} "
           f"{n(hc[0] + 34 * s)},{n(hc[1] - 4 * s)} Z", WHITE, INK, 2.5)                                 # painter's cap
    f.rect(hc[0] - 36 * s, hc[1] - 10 * s, 72 * s, 10 * s, WHITE, INK, 2, 3)


def hero():
    f = H.hero("fy52-hero", "Kuvitus: maalari maalaa talon seinää punaiseksi. Seinän edessä on kaksi maalauspukkia ja niiden päällä "
               "pitkä lankku. Maalari seisoo lankulla pukkien välissä ja ulottuu siveltimellä räystään alle. Lankun oikea pää "
               "ulottuu pitkälle oikeanpuoleisen pukin yli, ja tämän ulokkeen päällä on iso maalipurkki. Ulokkeen alla on tyhjää, "
               "joten herää kysymys, kuinka kauas ulokkeelle purkin voi viedä ennen kuin lankku kaatuu.")
    s = 190                                                            # figure units per metre: trestles, plank, bucket and painter to one scale
    yg = 560                                                           # the trestles' feet on the lawn
    ytop = yg - round(0.8 * s)                                         # the trestles' tops, 0,8 m
    # beyond the house corner: sky, a far forest and a birch
    H.sky(f, "fy52h", 480)
    H.cloud(f, 1110, 120, 0.6)
    H.forest(f, 430, 60, 28, GOOD, seed=2, x0=1000, depth=80)
    # the house wall: vertical boards, the left part freshly painted red, the right part still old and faded
    xc = 1010                                                          # the house corner
    f.rect(-10, 40, xc + 10, 452, HOT_LIGHT)
    f.path("M-10,40 H600 L594,96 L606,150 L590,214 L604,290 L592,360 L604,430 L596,492 H-10 Z", HOT)
    for x in range(14, xc, 34):
        f.line(x, 44, x, 490, INK, 1.5)
        f.add(f'<line x1="{x}" y1="44" x2="{x}" y2="490" stroke="{WHITE}" stroke-width="3" stroke-opacity="0.18" transform="translate(3 0)"/>')
    for k in range(14):                                                # flakes of old paint on the unpainted part
        px, py = 630 + 360 * H.rnd(k, 8), 70 + 400 * H.rnd(k, 9)
        f.add(f'<path d="M{n(px)},{n(py)} l14,-3 l6,9 l-10,8 l-12,-4 Z" fill="{SAND_LIGHT}" fill-opacity="0.8"/>')
    for wx, wy in ((90, 96), (720, 96)):                             # two windows with white frames
        f.rect(wx, wy, 150, 170, WHITE, INK, 3, 2)
        f.rect(wx + 14, wy + 14, 122, 142, H.grad(f, f"fy52h-win{wx}", GLASS, ICE), INK, 2)
        f.line(wx + 75, wy + 14, wx + 75, wy + 156, WHITE, 8); f.line(wx + 14, wy + 85, wx + 136, wy + 85, WHITE, 8)
        f.rect(wx - 10, wy + 170, 170, 14, WHITE, INK, 2, 2)
    f.rect(xc - 16, 40, 22, 452, WHITE, INK, 2)                        # the white corner board
    f.rect(-10, 22, xc + 40, 22, WHITE, INK, 2.5)                      # the fascia under the eaves
    f.path(f"M-10,0 H{xc + 50} L{xc + 34},24 H-10 Z", IRON, INK, 2.5)  # the roof's edge
    f.rect(-10, 488, xc + 10, 20, IRON, INK, 2)                        # the plinth
    # the lawn in front of the wall, the shadow of the plank on it
    f.rect(0, 506, 1200, 94, H.grad(f, "fy52h-grass", GOOD_LIGHT, GOOD, y1=506, y2=600))
    for k in range(46): f.line(10 + k * 26, 590 - 60 * H.rnd(k, 2), 16 + k * 26, 578 - 60 * H.rnd(k, 2), GOOD, 2)
    f.add(f'<ellipse cx="560" cy="{yg + 2}" rx="430" ry="10" fill="{INK}" fill-opacity="0.18"/>')
    # the plank, 4 m, on trestles 2 m apart: 0,6 m over the left one, 1,4 m out over the right one
    x1, x2, xa, xb = 170, 170 + 4 * s, 290, 290 + 2 * s
    for x, k in ((xa, 1), (xb, 2)): _trestle(f, x, ytop, yg, f"fy52h-beam{k}")
    f.rect(x1, ytop - 18, x2 - x1, 18, H.grad(f, "fy52h-plank", SAND_DARK, GRAIN), INK, 2.5, 2)
    for gx in range(x1 + 30, x2 - 40, 90): f.path(f"M{gx},{ytop - 9} q30,-3 60,0", stroke=SAND_LIGHT, w=1.5)
    # the painter between the trestles, reaching up to the eaves with the brush where the red ends
    brush = (574, 58)
    _painter(f, 476, ytop - 18, brush)
    f.path(f"M{brush[0] - 10},{brush[1] + 18} L{brush[0] + 2},{brush[1] - 2}", stroke=GRAIN, w=7, extra='stroke-linecap="round"')
    f.rect(brush[0] - 2, brush[1] - 26, 16, 26, INK, extra=f'transform="rotate(28 {brush[0]} {brush[1]})"')
    f.rect(brush[0] + 1, brush[1] - 40, 10, 16, HOT, extra=f'transform="rotate(28 {brush[0]} {brush[1]})"')
    # the paint tin (a 10-litre bucket) out on the overhang, 0,9 m beyond the right trestle
    bx, bw, bh = xb + round(0.9 * s), 52, 58
    f.path(f"M{bx - bw / 2},{ytop - 18 - bh} L{bx - bw / 2 + 4},{ytop - 18} H{bx + bw / 2 - 4} L{bx + bw / 2},{ytop - 18 - bh} Z", WHITE, INK, 2.5)
    f.rect(bx - bw / 2 + 3, ytop - 18 - bh * 0.62, bw - 6, bh * 0.34, HOT)
    f.rect(bx - bw / 2 - 3, ytop - 22 - bh, bw + 6, 9, RULE, INK, 2, 3)
    f.path(f"M{bx - bw / 2 + 2},{ytop - 18 - bh + 4} Q{bx},{ytop - 18 - bh - 44} {bx + bw / 2 - 2},{ytop - 18 - bh + 4}", stroke=INK, w=2.5)
    f.add(f'<path d="M{bx - 6},{ytop - 18 - bh - 4} q6,10 12,0" fill="{HOT}"/>')
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
    turn_arrow(f, X(0.0) + 34, 284, 26, -60, 200)
    f.tex(X(0.0) + 76, 284, r"+", "start")
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
    f.line(X(0) + 12, 238, X(0) + 12, 342, MUTED, 1.5, "4 4")
    for x in (X(0) + 12, X(4.0) - 4): f.line(x, 335, x, 349, INK, 1.5)
    f.line(X(0) + 12, 342, X(4.0) - 4, 342, INK, 1.5)               # the label sits in the water, clear of the concrete edge
    f.tex(440, 322, r"4{,}00\,\text{m}", "middle")
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


# --- Tarkista osaamisesi 2: the seesaw (model force diagram of the solution) ----------------------------------------
def seesaw_fbd():
    f = Fig("fy52-keinu-voimat", 400, "Mallivoimakuvio: keinulauta suorakulmiona, tukipiste laudan keskellä. Lapsen voima Fl "
            "painaa laudan vasemman pään yläpintaa alas 1,50 m:n päässä tukipisteestä. Aikuisen voima F painaa laudan "
            "yläpintaa alas tukipisteen oikealla puolella 1,20 m:n päässä siitä. Laudan paino G lähtee laudan keskeltä alas, "
            "ja tuen voima N osoittaa ylös ja päättyy laudan alapintaan tukipisteessä; G ja N on piirretty vierekkäin, jotta "
            "ne erottuvat. Positiivinen kiertosuunta on myötäpäivään. Nuolten pituudet ovat mittakaavassa: F on 1,25 kertaa "
            "Fl:n pituinen, ja N on yhtä pitkä kuin muut kolme yhteensä. Laudan massaa ei ole annettu, joten G:n pituus on "
            "valittu.")
    X = lambda x: 300 + 130 * x                                  # x in metres from the pivot
    cy, hh = 130, 9
    Fl = 24.0 * g; F = Fl * 1.50 / 1.20; G = 15.0 * g            # the board's mass is not given: G is drawn at 15 kg
    d = FBD(f, 0.26, body=(300, cy, 390, 2 * hh), a_dir=(0, 0))
    d.force("F_l", (0, -Fl), (X(-1.5) + 8, cy - hh), kind="normal", surface=0, outward=(0, -1), push=True,
            tex=r"\overline{F}_\text{l}", lab=(30, 0))
    d.force("F", (0, -F), (X(1.2), cy - hh), kind="normal", surface=0, outward=(0, -1), push=True, lab=(-24, 0))
    d.force("G", (0, -G), (300, cy), kind="gravity", lab=(-24, 4))
    d.force("N", (0, G + Fl + F), (X(0) + 16, cy + hh), kind="normal", surface=0, push=True, lab=(24, 6))
    d.draw()
    cmark(f, 300, cy)
    for x in (X(-1.5) + 8, X(1.2)): f.line(x, cy + hh + 4, x, 337, MUTED, 1.5, "4 4")
    f.line(300, cy + hh + 60, 300, 337, MUTED, 1.5, "4 4")
    dim(f, X(-1.5) + 8, 300, 345, r"1{,}50\,\text{m}", above=False)
    dim(f, 300, X(1.2), 345, r"1{,}20\,\text{m}", above=False)
    f.tex(300, 50, r"\text{keinulauta}", "middle")
    turn_arrow(f, 545, 240, 22, 200, -60)
    f.tex(577, 240, "+", "start")
    return f.svg()


# --- Momenttipisteen valinta: a force along and across a rod ----------------------------------------------------------
from fbd import FORCE, dashed_arrow


def wall(f, x, y0, y1, w=56):
    """A wall on the left of x, hatched, from y0 to y1."""
    f.rect(x - w, y0, w, y1 - y0, RULE_LIGHT, INK, 2.5)
    for y in range(int(y0) + 14, int(y1), 22): f.line(x - w, y + 10, x - w + 18, y - 4, MUTED, 1.5)


def components():
    f = Fig("fy52-komponentit", 290, "Kaavakuva: vaakasuora tanko on saranalla seinässä. Tangon uloimpaan päähän vaikuttaa voima F, joka "
            "osoittaa vinosti ylös kohti seinää ja muodostaa kulman alfa tangon kanssa. Voima on jaettu katkoviivanuolilla "
            "tangon suuntaiseen komponenttiin, joka kulkee saranan kautta eikä kierrä tankoa, ja tankoa vastaan kohtisuoraan "
            "komponenttiin F sin alfa, joka antaa momentin saranan suhteen. Momentin varsi on tangon pituus r.")
    hx, hy, L, a = 90, 190, 340, 35                                       # hinge, rod length in px, angle
    ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
    ex = hx + L
    wall(f, hx, 40, 250)
    f.rect(hx, hy - 8, L, 16, SAND_LIGHT, GRAIN, 2.5, 3)
    tx, ty = ex - 150 * ca, hy - 150 * sa
    f.line(tx, ty, ex, ty, MUTED, 1.5, "5 4"); f.line(tx, ty, tx, hy, MUTED, 1.5, "5 4")
    dashed_arrow(f, ex, hy - 8, ex, ty, FORCE)                            # the component across the rod
    dashed_arrow(f, ex - 6, hy - 14, tx + 2, hy - 14, FORCE)              # the component along the rod
    f.arrow(ex, hy, tx, ty, FORCE, 4, 18)
    f.circle(hx, hy, 7, WHITE, INK, 2.5)
    f.path(f"M{n(ex - 66)},{n(hy)} A66,66 0 0 1 {n(ex - 66 * ca)},{n(hy - 66 * sa)}", stroke=INK, w=1.5)
    f.tex(ex - 92, hy - 38, r"\alpha", "middle")
    f.tex(tx - 12, ty - 8, r"\overline{F}", "end", FORCE)
    f.tex(ex + 14, (hy + ty) / 2, r"F\sin\alpha", "start", FORCE)
    f.tex((tx + ex) / 2 - 20, hy + 40, r"F\cos\alpha", "middle", FORCE)
    dim(f, hx, ex, 262, r"r", above=False)
    f.tex(hx + 6, hy + 34, r"\text{sarana}", "start")
    return f.svg()


# --- L2-03: a shelf tilted on its front edge, at the limit of tipping (to scale: 0,400 m × 1,80 m, 120 px per metre) ---
def shelf():
    f = Fig("fy52-hylly", 350, "Kuva mittakaavassa: kirjahylly, jonka syvyys d on 0,400 m ja korkeus h 1,80 m, on kallistettu eteenpäin "
            "niin, että se nojaa vain etureunaansa P. Hyllyn painopiste on suorakulmion keskellä. Painopisteestä lähtee "
            "pystysuora katkoviiva alas etureunaan P, joten hylly on kaatumisen rajalla. Kulma alfa on pystysuoran ja hyllyn "
            "korkeussuunnan eli etureunan välinen kulma. Hyllyn pohjan puolikas d/2 ja puolet korkeudesta h/2 muodostavat "
            "suorakulmaisen kolmion, jonka hypotenuusa on pystysuora jana painopisteestä reunaan P.")
    px, py, k, a = 330, 272, 120, math.degrees(math.atan(0.4 / 1.8))
    ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
    d, h = 0.400 * k, 1.80 * k
    u = (-ca, -sa)                                                    # the depth direction on the page (backwards, up a little)
    v = (sa, -ca)                                                     # the height direction (up, leaning forward)
    P = lambda s, t: (px + s * u[0] + t * v[0], py + s * u[1] + t * v[1])
    f.line(60, py, 560, py, INK, 3, cap="round")
    for x in range(70, 560, 18): f.line(x, py, x - 10, py + 12, MUTED, 1.5)
    pts = [P(0, 0), P(d, 0), P(d, h), P(0, h)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", SAND_LIGHT, GRAIN, 2.5)
    for j in (0.3, 0.55, 0.8):                                        # shelf boards
        a1, b1 = P(0, j * h), P(d, j * h); f.line(a1[0], a1[1], b1[0], b1[1], GRAIN, 1.5)
    cx, cy = P(d / 2, h / 2)
    mx, my = P(d / 2, 0)
    f.line(px, py, px, py - 178, INK, 2, "6 5")                       # the vertical through P and the centre of mass
    f.line(px, py, mx, my, MUTED, 1.5, "5 4"); f.line(mx, my, cx, cy, MUTED, 1.5, "5 4")
    cmark(f, cx, cy)
    f.circle(px, py, 6, INK, WHITE, 2)
    r = 170
    f.path(f"M{n(px)},{n(py - r)} A{r},{r} 0 0 1 {n(px + r * sa)},{n(py - r * ca)}", stroke=INK, w=1.5)
    f.tex(px + r * sa + 26, py - r * ca - 4, r"\alpha", "middle")
    f.tex(px + 14, py + 36, r"\text{etureuna }P", "start")
    # half the depth, under the floor: from the foot of M to P
    f.line(mx, my + 2, mx, py + 26, MUTED, 1.5, "4 4")
    dim(f, mx, px, py + 26, r"\tfrac{d}{2}", above=False)
    # half the height, beside the front face
    o = (34 * ca, 34 * sa)
    f.line(px + o[0], py + o[1], cx + o[0], cy + o[1], INK, 1.5)
    for q in ((px, py), (cx, cy)):
        f.line(q[0] + o[0] - 7 * u[0], q[1] + o[1] - 7 * u[1], q[0] + o[0] + 7 * u[0], q[1] + o[1] + 7 * u[1], INK, 1.5)
    f.tex((px + cx) / 2 + o[0] + 24, (py + cy) / 2 + o[1], r"\tfrac{h}{2}", "start")
    return f.svg()


# --- L3-02: the sign on a rod, held by a wire above it (to scale: 220 px per metre) -----------------------------------------
def sign():
    f = Fig("fy52-kyltti", 350, "Kuva mittakaavassa: vaakasuora, 1,20 m pitkä tanko on kiinnitetty saranalla seinään. Tangon uloimmasta "
            "päästä riippuu kyltti. Tangon uloimmasta päästä lähtee vaijeri vinosti ylös seinään, saranan yläpuolelle, "
            "niin että vaijerin ja tangon välinen kulma on 30,0 astetta.")
    hx, hy, L = 96, 200, 264
    ex = hx + L
    ay = hy - L * math.tan(math.radians(30))
    wall(f, hx, 20, 300)
    f.line(hx, ay, ex, hy, INK, 3)                                   # the wire
    f.circle(hx, ay, 5, INK)
    f.rect(hx, hy - 9, L, 18, SAND_LIGHT, GRAIN, 2.5, 3)
    f.circle(hx, hy, 7, WHITE, INK, 2.5)
    f.line(ex, hy + 9, ex, 262, INK, 2)
    f.rect(ex - 50, 262, 100, 56, ALUMINIUM, METAL_EDGE, 2.5, 4)
    f.tex(ex, 290, r"\text{kyltti}", "middle")
    r = 100
    f.path(f"M{n(ex - r)},{n(hy)} A{r},{r} 0 0 1 {n(ex - r * math.cos(math.radians(30)))},{n(hy - r * 0.5)}", stroke=INK, w=1.5)
    bx, by = ex - 175 * math.cos(math.radians(15)), hy - 175 * math.sin(math.radians(15))
    f.tex(bx, by, r"30{,}0^\circ", "middle")
    f.tex((hx + ex) / 2, hy + 34, r"\text{tanko }1{,}20\,\text{m}", "middle")
    f.tex(ex - 100, (hy + ay) / 2 - 62, r"\text{vaijeri}", "middle")
    return f.svg()

FIGURES = {"hero": hero, "pari": couple, "kaatuu": tipping, "lankku": kaava_plank, "komponentit": components, "hirsi": log_fbd,
           "virhe": error_plank, "lauta": board_scene, "lauta-voimat": board_fbd, "keinu-voimat": seesaw_fbd,
           "hylly": shelf, "kyltti": sign}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pari": "reveals: a couple turns a body although the forces cancel",
    "kaatuu": "reveals: the tall box tips because its plumb line misses the base",
    "lankku": "reveals: the support nearer the centre of mass carries more",
    "hirsi": "reveals: the force diagram of the worked example",
    "virhe": "safe: a deliberately wrong diagram (equal support forces), for an error-spotting task",
    "lauta": "safe: situation picture of a diving board, data only",
    "lauta-voimat": "reveals: the model force diagram of the diving board",
    "keinu-voimat": "reveals: the model force diagram of the seesaw (the solution of its check)",
    "komponentit": "reveals: only the component across the rod gives a moment about the hinge",
    "hylly": "safe: geometry of the tilted shelf at the limit, symbols d, h and alpha only",
    "kyltti": "safe: situation picture of the sign, rod and wire with the angle and length, no forces",
}
