"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-2` writes them into lesson.md.
Colours (FY7 brief): force #c92a2a, velocity #1971c2, magnetic field #2b8a3e (• out of the page, × into it), electric
field #8a5f22, an ion beam (a current of ions) #7048e8. Positive particles #f2a69c, negative #d0e6fb, the sign drawn."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GOOD, GOOD_LIGHT, GLASS, WATER, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, PAPER, SAND, SAND_LIGHT, SAND_DARK, n)
import herolib as H

FORCE, VEL, FIELD, EFIELD, BEAM = HOT, COLD, GOOD, "#8a5f22", "#7048e8"
e, mp, md, u = 1.602e-19, 1.673e-27, 3.344e-27, 1.661e-27


def out_mark(f, x, y, r=8):
    """Magnetic field out of the page: a dot in a circle."""
    f.circle(x, y, r, "none", FIELD, 2)
    f.circle(x, y, 2.6, FIELD)


def in_mark(f, x, y, a=6):
    """Magnetic field into the page: a cross."""
    f.line(x - a, y - a, x + a, y + a, FIELD, 2.2)
    f.line(x - a, y + a, x + a, y - a, FIELD, 2.2)


def seg_dist(px, py, x1, y1, x2, y2):
    """Distance from a point to a segment (figure units)."""
    dx, dy = x2 - x1, y2 - y1
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy or 1)))
    return math.hypot(px - x1 - t * dx, py - y1 - t * dy)


def charge(f, x, y, positive=True, r=13):
    f.circle(x, y, r, HOT_LIGHT if positive else COLD_LIGHT, INK, 2)
    f.line(x - r * 0.5, y, x + r * 0.5, y, INK, 2.5)
    if positive: f.line(x, y - r * 0.5, x, y + r * 0.5, INK, 2.5)


def force_dir():
    f = Fig("fy72-dir", 340, "Kaavakuva: kaksi paneelia, joissa magneettikenttä osoittaa paperiin sisään, mitä kuvaavat vihreät ristit. "
            "Vasemmalla positiivinen hiukkanen liikkuu oikealle, ja magneettinen voima osoittaa ylöspäin. Oikealla negatiivinen "
            "hiukkanen liikkuu samoin oikealle, ja voima osoittaa alaspäin. Voima on kohtisuorassa sekä nopeutta että kenttää vastaan.")
    f.line(300, 16, 300, 324, RULE, 2, "6 6")
    for cx, pos in ((150, True), (450, False)):
        for i in range(4):
            for j in range(4):
                x, y = cx - 105 + 70 * i, 56 + 70 * j
                if abs(x - cx) < 60 and abs(y - 196) < 40: continue
                if x == cx - 35 and y == (126 if pos else 266): continue   # room for the force's label
                in_mark(f, x, y)
        y0 = 196
        f.arrow(cx - 70, y0, cx + 40, y0, VEL, 3.5, 16)
        f.tex(cx + 48, y0, r"\overline{v}", "start", VEL)
        dy = -1 if pos else 1
        f.arrow(cx - 70, y0, cx - 70, y0 + dy * 88, FORCE, 3.5, 16)
        f.tex(cx - 60, y0 + dy * 78, r"\overline{F}_\text{m}", "start", FORCE)
        charge(f, cx - 70, y0, pos)
        f.tex(cx, 316, r"\text{positiivinen } q" if pos else r"\text{negatiivinen } q", "middle", w=220)
    f.tex(16, 24, r"\overline{B}\ \text{paperiin}", "start", FIELD, w=170)
    return f.svg()


def circle_path():
    f = Fig("fy72-circle", 360, "Kaavakuva: positiivinen hiukkanen kiertää ympyrärataa myötäpäivään magneettikentässä, joka osoittaa "
            "paperista ulos (vihreät pisteympyrät). Radan neljässä kohdassa sininen nopeusnuoli on radan tangentin suuntainen ja "
            "punainen magneettisen voiman nuoli osoittaa kohti ympyrän keskipistettä. Nuolet ovat joka kohdassa yhtä pitkät, "
            "koska vauhti ei muutu. Keskipisteestä rataan on piirretty säde r.")
    cx, cy, R = 300, 180, 120
    segs = []                                      # the arrows and labels: no field mark under them
    for ang in (90, 0, 270, 180):
        a = math.radians(ang); x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        segs += [(x, y, x + 62 * math.sin(a), y + 62 * math.cos(a)), (x, y, x + (cx - x) * 0.46, y + (cy - y) * 0.46)]
    segs += [(370, 56, 400, 56), (314, 136, 360, 136), (cx - 70, cy + 22, cx - 34, cy + 22)]
    for i in range(-3, 4):
        for j in range(-2, 3):
            x, y = cx + 76 * i, cy + 66 * j
            if abs(math.hypot(x - cx, y - cy) - R) < 26 or (i == 0 and j == 0): continue
            if x < 40 or x > 560: continue
            if any(seg_dist(x, y, *sg) < 22 for sg in segs): continue
            out_mark(f, x, y)
    f.circle(cx, cy, R, "none", INK, 2.5)
    f.line(cx, cy, cx + R * math.cos(math.radians(225)), cy - R * math.sin(math.radians(225)), MUTED, 2, "7 5")
    f.circle(cx, cy, 4, INK)
    f.tex(cx - 52, cy + 22, "r", "middle")
    for ang in (90, 0, 270, 180):                 # positions on the circle (degrees, counterclockwise from +x)
        a = math.radians(ang)
        x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        tx, ty = math.sin(a), math.cos(a)          # clockwise tangent in screen coordinates
        f.arrow(x, y, x + 62 * tx, y + 62 * ty, VEL, 3.5, 15)
        f.arrow(x, y, x + (cx - x) * 0.46, y + (cy - y) * 0.46, FORCE, 3.5, 15)
        charge(f, x, y, True, 11)
        if ang == 90:
            f.tex(x + 70, y - 4, r"\overline{v}", "start", VEL)
            f.tex(x + 14, y + 44, r"\overline{F}_\text{m}", "start", FORCE)
    f.tex(584, 24, r"\overline{B}\ \text{paperista ulos}", "end", FIELD, w=230)
    f.tex(584, 336, r"\text{myötäpäivään}", "end", w=170)
    return f.svg()


def r_graph():
    f = Fig("fy72-rv", 340, "Kuvaaja mittakaavassa: ympyräradan säde r senttimetreinä hiukkasen vauhdin v funktiona, kun magneettikenttä "
            "on 0,20 teslaa. Protonin suora nousee origosta arvoon 10,4 cm vauhdilla 2,0 miljoonaa metriä sekunnissa, deuteronin "
            "suora kaksi kertaa jyrkemmin arvoon 20,9 cm. Säde on suoraan verrannollinen vauhtiin ja massaan. Kuvaaja näyttää säteen r, ei halkaisijaa 2r.")
    ax = Axes(f, (96, 286), (424, 52), x=(0, 2.0), y=(0, 22), xticks=[0.5, 1.0, 1.5, 2.0], yticks=[5, 10, 15, 20],
              xlabel=r"v\ (10^6\,\text{m/s})", ylabel=r"r\ (\text{cm})", xfmt=lambda v: fi(v, 1))
    rp = lambda v: mp * v * 1e6 / (e * 0.20) * 100
    rd = lambda v: md * v * 1e6 / (e * 0.20) * 100
    ax.line([(0, 0), (2.0, rp(2.0))], INK, 3)
    ax.line([(0, 0), (2.0, rd(2.0))], WATER, 3)
    for v in (1.0, 2.0):
        ax.point(v, rp(v), INK); ax.point(v, rd(v), WATER)
    f.tex(ax.X(1.5), ax.Y(rp(1.5)) + 48, r"\text{protoni}", "middle", INK, w=110)
    f.tex(ax.X(2.0) - 16, ax.Y(rd(2.0)) - 2, r"\text{deuteroni}", "end", WATER, w=130)
    f.tex(ax.X(0.08), 40, r"B = 0{,}20\,\text{T}", "start", w=130)
    return f.svg()


def spectrometer():
    f = Fig("fy72-ms", 410, "Periaatekuva, ei mittakaavassa: massaspektrometri. Vasemmalla ionilähde. Ionit kulkevat ensin "
            "nopeusvalitsimen läpi: levyjen välillä sähkökenttä osoittaa ylöspäin ja magneettikenttä paperista ulos, ja "
            "suoraan kulkevaan ioniin vaikuttavat yhtä suuret vastakkaiset voimat, sähköinen ylös ja magneettinen alas. Raon "
            "jälkeen ionit kaartuvat toisessa magneettikentässä puoliympyrän ja osuvat ilmaisimeen. Raskaampien ionien "
            "puoliympyrä on suurempi, joten ne osuvat kauemmas raosta. Osumakohdan etäisyys raosta on radan halkaisija 2r.")
    yb = 78                                        # the beam line
    # ion source
    f.rect(14, yb - 18, 46, 36, ALUMINIUM, INK, 2, 5)
    f.tex(37, yb + 42, r"\text{lähde}", "middle", w=80)
    # velocity selector: plates, E arrows, B marks, forces on an ion
    f.rect(84, yb - 46, 190, 10, METAL_EDGE, INK, 1.5, 2)
    f.rect(84, yb + 36, 190, 10, METAL_EDGE, INK, 1.5, 2)
    for x in (104, 254):
        f.line(x, yb + 34, x, yb - 32, EFIELD, 2)
        f.path(f"M{x},{yb - 34} L{x - 6},{yb - 20} L{x + 6},{yb - 20} Z", EFIELD)
    for x in (124, 232):
        out_mark(f, x, yb - 20, 7); out_mark(f, x, yb + 20, 7)
    f.tex(179, 16, r"\text{nopeusvalitsin}", "middle", w=200)
    # the deflection chamber: B2 out of the page, two semicircles back to the detector on its left wall
    wall = 330
    r1, r2 = 106, 126                              # a lighter and a heavier ion; schematic, not to scale (the ratio is exaggerated)
    f.rect(wall, yb - 30, 250, 2 * r2 + 70, GLASS, None)
    f.rect(wall, yb - 30, 250, 2 * r2 + 70, "none", INK, 2.5, 6)
    for i in range(3):
        for j in range(4):
            x, y = wall + 70 + 66 * i, yb + 30 + 62 * j
            out_mark(f, x, y, 7)
    f.tex(574, yb - 12, r"\overline{B}_2", "end", FIELD)
    f.line(60, yb, wall, yb, BEAM, 3)
    for r, w in ((r1, 3), (r2, 3)):
        f.path(f"M{wall},{yb} A{r},{r} 0 0 1 {wall},{yb + 2 * r}", stroke=BEAM, w=w)
    # detector on the left wall below the slit
    f.rect(wall - 10, yb + 20, 10, 2 * r2 + 14, INK)
    for r in (r1, r2): f.circle(wall - 5, yb + 2 * r, 5, HEAT_LIGHT, INK, 1.5)
    f.tex(wall - 18, yb + 2 * r2 + 50, r"\text{ilmaisin}", "end", w=110)
    f.tex(wall - 56, yb + 2 * r1, r"\text{kevyempi}", "end", BEAM, w=130)
    f.tex(wall - 22, yb + 2 * r2 + 2, r"\text{raskaampi}", "end", BEAM, w=130)
    # 2r of the lighter ion
    xd = wall - 34
    f.line(xd, yb, xd, yb + 2 * r1, INK, 1.5)
    for y in (yb, yb + 2 * r1): f.line(xd - 6, y, xd + 6, y, INK, 1.5)
    f.tex(xd - 10, yb + r1 + 16, "2r", "end")
    # forces on an ion in the selector, drawn on its own row under the plates
    ix = 160
    f.arrow(ix, yb, ix, yb - 28, FORCE, 3, 11)
    f.arrow(ix, yb, ix, yb + 28, FORCE, 3, 11)
    charge(f, ix, yb, True, 8)
    f.tex(ix + 14, yb - 22, r"\overline{F}_\text{s}", "start", FORCE)
    f.tex(ix + 14, yb + 22, r"\overline{F}_\text{m}", "start", FORCE)
    f.tex(104, yb + 80, r"\overline{E}", "middle", EFIELD)
    f.tex(232, yb + 80, r"\overline{B}_1", "middle", FIELD)
    return f.svg()


def track_sign():
    """Task figure: a track in a field into the page that bends down. The sign of the charge is not given."""
    f = Fig("fy72-track", 330, "Kaavakuva: tyhjiökammiossa magneettikenttä osoittaa paperiin sisään (vihreät ristit). Hiukkanen "
            "tulee vasemmalta vaakasuoraan oikealle, ja sen rata kaartuu ympyränkaarena alaspäin. Hiukkasen varauksen merkkiä "
            "ei ole merkitty.")
    f.rect(40, 30, 520, 270, GLASS, None)
    f.rect(40, 30, 520, 270, "none", INK, 2.5, 6)
    R = 190
    ang = math.radians(62); px, py = 40 + R * math.sin(ang), 100 + R - R * math.cos(ang)
    for i in range(7):
        for j in range(4):
            x, y = 80 + 74 * i, 62 + 70 * j
            th = math.atan2(x - 40, 100 + R - y)           # a cross keeps clear of the dashed track and the particle
            d_track = abs(math.hypot(x - 40, y - 100 - R) - R) if 0 <= th <= ang else 1e9
            if d_track < 22 or math.hypot(x - px, y - py) < 36: continue
            in_mark(f, x, y)
    f.line(14, 100, 40, 100, INK, 2.5, "6 4")
    f.path(f"M40,100 A{R},{R} 0 0 1 {n(40 + R * math.sin(math.radians(62)))},{n(100 + R - R * math.cos(math.radians(62)))}", stroke=INK, w=2.5, extra='stroke-dasharray="6 4"')
    a = math.radians(62); x, y = 40 + R * math.sin(a), 100 + R - R * math.cos(a)
    f.circle(x, y, 11, ALUMINIUM, INK, 2)
    f.tex(552, 270, r"\overline{B}\ \text{paperiin}", "end", FIELD, w=170, bg=True)
    return f.svg()


def hero():
    """Opening illustration: a radiocarbon laboratory. A piece of old wood is the sample; its ions fly through a vacuum
    tube between the poles of a large electromagnet and split into two beams that hit two spots on a detector."""
    f = H.hero("fy72-hero", "Kuvitus: radiohiililaboratorio. Pöydällä on vanha puunpala näytteenä. Sen hiili-ioneista syntyvä säde "
               "kulkee tyhjiöputkessa suuren sähkömagneetin napojen välistä, kaartuu ja jakautuu kahdeksi säteeksi, jotka osuvat "
               "ilmaisimen kahteen eri kohtaan. Näytöllä näkyy kaksi eri korkuista piikkiä.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 420, H.grad(f, "fy72h-wall", GLASS, "#e3dccb"))
    for x in range(0, 1200, 150): f.line(x, 0, x, 420, WHITE, 3, None)
    # bench
    f.rect(0, 420, 1200, 26, SAND, INK, 3)
    f.rect(0, 446, 1200, 154, SAND_LIGHT)
    for x in (120, 1080): f.rect(x - 14, 446, 28, 154, SAND_DARK)
    # the sample: an old piece of wood on a small stand at the left
    f.rect(70, 380, 120, 40, METAL_EDGE, INK, 3, 6)
    f.path("M86,380 L104,338 L172,330 L182,372 Z", "#a97a35", INK, 3)
    for k in range(3): f.path(f"M{106 + 20 * k},{344 - 2 * k} q8,14 2,32", stroke="#8a5f22", w=2.5)
    # ion source box and the vacuum tube to the magnet, on the beam's height y = 285
    f.rect(220, 230, 130, 110, ALUMINIUM, INK, 3, 10)
    f.circle(285, 285, 18, IRON, INK, 3)
    f.rect(350, 270, 170, 30, GLASS, INK, 3, 6)
    # the electromagnet: an iron yoke behind, pole pieces with copper coils above and below the gap
    f.rect(500, 110, 300, 310, METAL_EDGE, INK, 3, 10)
    f.rect(510, 120, 280, 44, IRON, INK, 3, 6)
    f.rect(510, 376, 280, 34, IRON, INK, 3, 6)
    for y0 in (164, 312):
        f.rect(520, y0, 260, 64, H.grad(f, f"fy72h-coil{y0}", COPPER, "#8a5f22"), INK, 3, 10)
        for x in range(538, 780, 22): f.line(x, y0 + 4, x, y0 + 60, "#8a5f22", 2)
    f.rect(510, 238, 280, 64, GLASS, INK, 3, 10)          # the gap between the poles with the beam tube in it
    f.path("M500,285 C600,285 700,280 760,262", stroke=WHITE, w=22, extra='stroke-linecap="round"')
    f.path("M500,285 C600,285 700,280 760,262", stroke=BEAM, w=8, extra='stroke-linecap="round" stroke-opacity="0.85"')
    # two beams leaving the magnet towards the detector, the lighter one bent more
    f.path("M760,262 C830,232 870,196 905,150", stroke=GLASS, w=40, extra='stroke-linecap="round"')
    f.path("M762,261 C830,230 872,192 905,150", stroke=BEAM, w=7, extra='stroke-linecap="round"')
    f.path("M762,264 C840,240 890,220 925,196", stroke=BEAM, w=4, extra='stroke-linecap="round" stroke-opacity="0.8"')
    # detector plate with two glowing spots
    f.path("M890,110 L960,90 L1010,250 L940,270 Z", METAL_EDGE, INK, 3)
    for x, y, r in ((912, 146, 16), (934, 196, 10)):
        f.circle(x, y, r + 10, HEAT_LIGHT)
        f.circle(x, y, r, HEAT, INK, 2)
    f.rect(960, 250, 30, 170, IRON, INK, 3, 4)
    # a screen with two peaks of different height
    f.rect(1010, 290, 170, 120, INK, None, 0, 10)
    f.rect(1022, 302, 146, 96, INK, MUTED, 2, 6)
    f.path("M1030,388 L1060,388 L1070,316 L1080,388 L1110,388 L1118,372 L1126,388 L1160,388", stroke=GOOD_LIGHT, w=3)
    f.rect(1080, 410, 30, 12, IRON)
    return f.svg()


FIGURES = {"hero": hero, "force-dir": force_dir, "circle-path": circle_path, "r-graph": r_graph, "spectrometer": spectrometer,
           "track-sign": track_sign}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "force-dir": "reveals: the direction of the magnetic force for a positive and a negative charge in a field into the page",
    "circle-path": "reveals: the force points to the centre and the speed stays constant on the circle",
    "r-graph": "reveals: r grows in proportion to v and to m (proton and deuteron at 0,20 T)",
    "spectrometer": "reveals: the heavier ion lands farther from the slit",
    "track-sign": "safe: a track bending down in a field into the page, the sign of the charge not marked",
}
