"""Figures of fy4-16 (scripts/figlib.py, scripts/fbd.py, scripts/herolib.py); `python scripts/figures.py fy4-16` writes them into
lesson.md. Every force diagram is an FBD: the object alone as a plain rectangle (rotated with its surface on a slope), its arrows
drawn to scale and its physics checked as it is drawn; the situation is a separate pictorial situation picture (tilannekuva)
apart from the diagram by a dashed divider; no point-particle diagrams. Velocity is blue, acceleration orange and forces red
(FBD.motion, FBD.force). The sled model: straight slopes, the same friction coefficient on the slope and on the flat, air
resistance neglected; the numbers are those of lesson-answers.py and answers.py."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ICE, ICE_EDGE,
                    GLASS, COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, n)
from fbd import FBD, ground, open_head, _dir
import herolib as H
from herolib import grad, rnd

g = 9.81
SUIT, RIG, SKIN = GOOD, IRON, SAND_LIGHT
CANOPY, CANOPY2 = SAND_DARK, SAND
FAR = 'stroke-linecap="round" stroke-opacity="0.6"'


# ---------------------------------------------------------------- drawing helpers
def slope_frame(cx, cy, w, h, deg):
    """Points of a rectangle (cx, cy, w, h) rotated deg anticlockwise (a slope rising to the right), in figure coordinates
    (y down): the middle of its bottom face and its uphill and downhill bottom corners; t up the slope, nrm out of it (y up)."""
    t = _dir(deg); nrm = (-t[1], t[0])
    bx, by = cx - h / 2 * nrm[0], cy + h / 2 * nrm[1]
    up = (bx + w / 2 * t[0], by - w / 2 * t[1]); down = (bx - w / 2 * t[0], by + w / 2 * t[1])
    return t, nrm, (bx, by), up, down


def angle_arc(f, x, y, r, a0, a1, label, lab_r=None, color=INK):
    """An arc at (x, y) from the direction a0 to a1 (degrees anticlockwise, y up) with its label."""
    p0 = (x + r * math.cos(math.radians(a0)), y - r * math.sin(math.radians(a0)))
    p1 = (x + r * math.cos(math.radians(a1)), y - r * math.sin(math.radians(a1)))
    f.path(f"M{n(p0[0])},{n(p0[1])} A{r},{r} 0 0 0 {n(p1[0])},{n(p1[1])}", "none", color, 2)
    am = math.radians((a0 + a1) / 2); R = lab_r or r + 18
    f.tex(x + R * math.cos(am), y - R * math.sin(am), label, "middle", color)


def axes_slope(f, x, y, deg, L=44):
    """Small axes on a slope rising to the right: x down the slope, y out of the surface."""
    t = _dir(deg); nrm = (-t[1], t[0])
    f.arrow(x, y, x - L * t[0], y + L * t[1], MUTED, 2, 10); f.arrow(x, y, x + L * nrm[0], y - L * nrm[1], MUTED, 2, 10)
    f.tex(x - (L + 14) * t[0], y + (L + 14) * t[1], r"x", "middle", MUTED); f.tex(x + (L + 14) * nrm[0], y - (L + 14) * nrm[1], r"y", "middle", MUTED)


def vline(f, x1, y1, x2, y2, col=COLD, sym=r"\overline{v}", lab=(18, 0)):
    """A thin velocity (blue) or acceleration (orange) arrow with an open head in a situation picture: not a force."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.line(x1, y1, x2 - ux * 2, y2 - uy * 2, col, 2.5); open_head(f, x2, y2, ux, uy, col, 2.5)
    f.tex((x1 + x2) / 2 + lab[0], (y1 + y2) / 2 + lab[1], sym, "middle", col)


def sled(f, x, y, deg=0.0, sc=1.0, gid="s", rider=True, coat=COLD, face_left=True):
    """A red plastic sled (pulkka) with a child sitting in it, its bottom centre at (x, y), tilted by deg (anticlockwise, a
    slope rising to the right), the front towards the lower end (face_left: front to the left)."""
    k = -1 if face_left else 1
    f.add(f'<g transform="translate({n(x)},{n(y)}) rotate({n(-deg)}) scale({k * sc:g},{sc:g})">')
    f.path("M-46,-4 Q-48,0 -40,0 H34 Q52,0 56,-22 L48,-24 Q44,-10 30,-10 H-38 Z", grad(f, gid, HOT_LIGHT, HOT), INK, 2.5)
    f.path("M-40,-6 H28", stroke=HOT_LIGHT, w=3, extra='stroke-linecap="round" stroke-opacity="0.8"')
    if rider:
        f.path("M6,-14 Q26,-16 40,-20", stroke=INK, w=9, extra='stroke-linecap="round"')                     # legs forward
        f.path("M-22,-12 Q-26,-46 -6,-50 Q8,-50 10,-14 Z", coat, INK, 2.5)                                    # body
        f.path("M2,-40 L22,-24", stroke=coat, w=8, extra='stroke-linecap="round"')                            # arm to the sled's edge
        f.circle(-8, -62, 11, SKIN, INK, 2)
        f.path("M-20,-62 Q-20,-78 -8,-78 Q4,-78 4,-62 Z", HOT, INK, 2)                                          # cap
        f.circle(-8, -80, 4, WHITE, INK, 1.5)
    f.add("</g>")


def person(f, cx, yfoot, h=110, fill=COLD_LIGHT):
    """A simple standing person (fy4-5's), seen from the front: body, head, legs."""
    f.rect(cx - 17, yfoot - h * 0.72, 34, h * 0.48, fill, INK, 2.5, rx=10)
    f.circle(cx, yfoot - h * 0.84, h * 0.11, SKIN, INK, 2.5)
    f.line(cx - 8, yfoot - h * 0.26, cx - 8, yfoot, INK, 4, cap="round"); f.line(cx + 8, yfoot - h * 0.26, cx + 8, yfoot, INK, 4, cap="round")


def cabin(f, x, y, w, h):
    """A lift car: the cable from above, the walls, a handrail and the floor (its top at y + h - 12)."""
    f.line(x + w / 2, y - 10, x + w / 2, y, IRON, 3)
    f.rect(x, y, w, h, GLASS, INK, 3, rx=4)
    f.rect(x + 6, y + h - 12, w - 12, 8, ALUMINIUM, METAL_EDGE, 1.5)
    f.line(x + w - 14, y + h * 0.45, x + w - 14, y + h * 0.62, METAL_EDGE, 3)
    return y + h - 12


def skydiver_hang(f, x, y, sc=1.0):
    """A skydiver hanging upright under a canopy (fy4-14's), centred at (x, y)."""
    f.add(f'<g transform="translate({n(x)},{n(y)}) scale({sc:g})">')
    f.path("M-5,12 L-7,40", stroke=SUIT, w=9, extra='stroke-linecap="round"'); f.path("M5,12 L7,40", stroke=SUIT, w=9, extra=FAR)
    f.rect(-11, -18, 22, 34, SUIT, INK, 2.5, 7)
    f.rect(-8, -16, 16, 14, RIG, INK, 2, 2)
    f.path("M-11,-12 L-18,-34", stroke=SUIT, w=7, extra='stroke-linecap="round"'); f.path("M11,-12 L18,-34", stroke=SUIT, w=7, extra='stroke-linecap="round"')
    f.circle(0, -28, 10, SKIN, INK, 2); f.path("M-10,-28 A10,10 0 0 1 10,-28 Z", INK)
    f.add("</g>")


def canopy(f, x, y, sc=1.0, w=150, gid="c"):
    """A ram-air canopy over a hanging skydiver at (x, y): the lines from the shoulders to the canopy's lower edge."""
    hw, top, bot = w / 2 * sc, y - 120 * sc, y - 88 * sc
    for k in (-0.5, -0.2, 0.2, 0.5):
        f.line(x + k * 20 * sc, y - 30 * sc, x + k * w * 0.9 * sc, bot, MUTED, 1.5)
    f.path(f"M{n(x - hw)},{n(bot)} Q{n(x - hw)},{n(top)} {n(x)},{n(top)} Q{n(x + hw)},{n(top)} {n(x + hw)},{n(bot)} Z",
           grad(f, gid, CANOPY, CANOPY2), INK, 2.5)
    for k in range(1, 6):
        xx = x - hw + k * 2 * hw / 6
        f.line(xx, bot, xx, bot - (bot - top) * 0.8 * math.sin(math.pi * k / 6), GRAIN, 1.5)


def suitcase(f, cx, top, w=56, h=70):
    """A suitcase hanging from its handle at (cx, top)."""
    f.path(f"M{n(cx - 12)},{n(top + 12)} V{n(top + 2)} Q{n(cx)},{n(top - 6)} {n(cx + 12)},{n(top + 2)} V{n(top + 12)}", stroke=INK, w=3)
    f.rect(cx - w / 2, top + 12, w, h, grad(f, "fy416-case", COPPER, "#8f4a22"), INK, 2.5, rx=7)
    for dx in (-w / 4, w / 4): f.line(cx + dx, top + 16, cx + dx, top + 8 + h, INK, 1.5)


def spring_scale(f, cx, y1, y2):
    """A spring balance hanging from (cx, y1) with its hook at (cx, y2)."""
    f.line(cx, y1, cx, y1 + 10, INK, 2.5)
    f.rect(cx - 9, y1 + 10, 18, y2 - y1 - 26, ALUMINIUM, INK, 2, rx=4)
    for k in range(5): f.line(cx - 5, y1 + 16 + k * (y2 - y1 - 38) / 4, cx + 5, y1 + 16 + k * (y2 - y1 - 38) / 4, MUTED, 1.5)
    f.path(f"M{n(cx)},{n(y2 - 16)} V{n(y2 - 4)} Q{n(cx)},{n(y2 + 4)} {n(cx - 7)},{n(y2)}", stroke=INK, w=2.5)


# ---------------------------------------------------------------- opening illustration
# The hero hill: summit 13 m above the flat, the steep side at 35°, the gentle side at 16°, friction coefficient 0,25 on the
# slopes and the flat: both sleds stop h/μ = 52 m (520 px) from the summit, measured horizontally (10 px per metre; the
# children and sleds are drawn larger than the scale so that they read).
HERO = dict(top=(600, 336), h=130, steep=35.0, gentle=16.0, mu=0.25)


def flag(f, x, yb, col=HOT):
    """A thin marker pole with a small pennant, its foot at (x, yb)."""
    f.line(x, yb, x, yb - 62, IRON, 3, cap="round")
    f.path(f"M{n(x)},{n(yb - 62)} L{n(x + 26)},{n(yb - 53)} L{n(x)},{n(yb - 44)} Z", col, INK, 1.5)


def hero():
    """The chapter's opening illustration: a sledding hill with a steep and a gentle side of the same height; two sleds have
    slid down the two sides and stopped equally far from the summit, measured horizontally, each beside a marker flag."""
    (tx, ty), h, mu = HERO["top"], HERO["h"], HERO["mu"]
    yb = ty + h
    xl = tx - h / math.tan(math.radians(HERO["steep"])); xr = tx + h / math.tan(math.radians(HERO["gentle"]))
    stop_l, stop_r = tx - h / mu, tx + h / mu
    f = H.hero("fy416-hero", "Kuvitus: talvinen pulkkamäki. Mäen huipulla seisoo kaksi lasta, ja toisen pulkka odottaa lähtöä. Mäen "
               "vasen rinne on jyrkkä ja lyhyt, oikea rinne loiva ja pitkä, ja kummankin rinteen juurelta jatkuu tasainen lumikenttä. "
               "Kummallakin puolella pulkan jäljet kulkevat rinnettä alas ja tasaista pitkin pulkkaan, joka on pysähtynyt lapsi "
               "kyydissään punaisen merkkilipun kohdalle. Vasemmalla jyrkältä puolelta laskenut pulkka on liukunut tasaisella pitkälle, "
               "oikealla loivalta puolelta laskenut vain vähän, ja molemmat liput ovat yhtä kaukana mäen huipusta vaakasuunnassa "
               "mitattuna. Taustalla metsää, punainen mökki ja lumisia kumpuja. Mäen korkeus ja matkat ovat mittakaavassa, lapset ja "
               "pulkat sitä suurempina.")
    H.sky(f, "fy416h", 470, ICE, GLASS)
    H.sun(f, "fy416h", 1080, 96, 44, rays=False)
    H.cloud(f, 230, 96, 1.1); H.cloud(f, 820, 70, 0.8); H.cloud(f, 520, 150, 0.55, extra='fill-opacity="0.85"')
    H.hills(f, "fy416h", 370, [WHITE, GLASS], amp=34, seed=7)
    H.forest(f, 452, 70, 30, GOOD, seed=5, depth=40)
    H.red_house(f, 120, 458, 170, 92, snow=True)
    for k in range(10): f.path(f"M{n(rnd(k, 4) * 1200)},{n(404 - 30 * rnd(k, 6))} l8,-14 l8,14 Z", WHITE)
    # the hill and the flat: snow
    snow = grad(f, "fy416h-snow", WHITE, COLD_LIGHT, y1=ty, y2=600)
    outline = (f"M0,{yb} H{n(xl - 16)} Q{n(xl)},{yb} {n(xl + 10)},{n(yb - 7)} L{n(tx - 9)},{n(ty + 6)} Q{n(tx)},{n(ty - 2)} {n(tx + 9)},{n(ty + 3)} "
               f"L{n(xr - 20)},{n(yb - 5)} Q{n(xr)},{yb} {n(xr + 20)},{yb} H1200")
    f.path(outline + " V600 H0 Z", snow)
    f.path(outline, stroke=ICE_EDGE, w=2.5)
    for k in range(22): f.path(f"M{n(rnd(k, 9) * 1200)},{n(yb + 26 + rnd(k, 3) * 100)} q14,-4 28,0", stroke=ICE, w=2, extra='stroke-linecap="round"')
    # the tracks: down each side and along the flat to the stopped sled
    for dy in (3, 10):
        f.path(f"M{n(tx - 12)},{n(ty + 8 + dy)} L{n(xl + 8)},{n(yb - 3 + dy)} Q{n(xl - 6)},{n(yb + dy)} {n(xl - 30)},{n(yb + dy)} H{n(stop_l + 50)}",
               stroke=ICE_EDGE, w=2.5, extra='stroke-opacity="0.75"')
        f.path(f"M{n(tx + 12)},{n(ty + 7 + dy)} L{n(xr - 16)},{n(yb - 3 + dy)} Q{n(xr)},{n(yb + dy)} {n(xr + 22)},{n(yb + dy)} H{n(stop_r - 50)}",
               stroke=ICE_EDGE, w=2.5, extra='stroke-opacity="0.75"')
    # the marker flags at the stops, equally far from the summit, and the stopped sleds beside them
    flag(f, stop_l, yb + 14); flag(f, stop_r, yb + 14)
    sled(f, stop_l + 62, yb + 16, 0, 1.25, "fy416h-s1", coat=COLD, face_left=True)       # its front at the flag
    sled(f, stop_r - 62, yb + 16, 0, 1.25, "fy416h-s2", coat=GOOD, face_left=False)
    # the children on the summit with a sled ready to go down the steep side
    sled(f, tx - 40, ty + 26, 22, 1.0, "fy416h-s3", rider=False)
    H.walker(f, tx + 26, ty + 8, HEAT, INK, 0.25, winter=True)
    H.walker(f, tx - 4, ty + 6, COLD, INK, 0.23, winter=True, hand=(tx - 30, ty - 20))
    # foreground: snow drifts
    for x, w in ((260, 150), (760, 190), (1010, 120)):
        f.path(f"M{x - w / 2},{yb + 120} Q{x},{yb + 84} {x + w / 2},{yb + 120} Z", WHITE, ICE, 2)
    return f.svg()


# ---------------------------------------------------------------- Ydinajatus: three situations, three force diagrams
KELKKA = dict(m=32.0, deg=20.0, mu=0.200, L=25.0)     # the worked example's sled (lesson-answers.py computes the same)


def kolme():
    """Ydinajatus: the three situations of the chapter, each with its situation picture above the dashed divider and the force
    diagram of the chosen body below it, forces to scale within each diagram: a 60,0 kg person in a lift speeding up upward at
    1,0 m/s² (N > G), a jumper under the canopy at the terminal speed (F_v = G), a sled sliding down a 20° slope with μ = 0,20."""
    f = Fig("fy416-kolme", 460, "Kolme tilannetta. Ylhäällä tilannekuvat ja katkoviivan alla voimakuviot, joissa valittu kappale on "
            "suorakulmio ja voimat ovat kunkin kuvion sisällä mittakaavassa. Vasemmalla hissi lähtee ylös: ihminen seisoo hissikorin "
            "lattialla, ja sininen nopeusnuoli osoittaa ylös. Ihmisen voimakuviossa paino G keskipisteestä alas ja lattian tukivoima N "
            "alapinnasta ylös, painoa pidempänä, ja oranssi kiihtyvyysnuoli ylös. Keskellä laskuvarjohyppääjä "
            "laskeutuu varjon varassa tasaisella nopeudella: nopeusnuoli alas. Voimakuviossa paino G alas ja ilmanvastus F_v "
            "yläpinnasta ylös, yhtä pitkinä, kiihtyvyys nolla. Oikealla pulkka liukuu rinnettä alas vasemmalle: nopeusnuoli rinnettä "
            "alas. Voimakuviossa pulkka on rinteen suuntaisesti kallistettu suorakulmio: paino G keskipisteestä suoraan alas, "
            "tukivoima N alapinnasta kohtisuoraan rinteestä ulos ja liikekitka F_mu alapinnan ylemmästä kulmasta rinnettä ylös, "
            "lyhyenä. Kiihtyvyysnuoli rinnettä alas.", size=26)
    f.line(14, 196, 586, 196, RULE, 1.5, "6 6")
    f.line(200, 36, 200, 446, RULE_LIGHT, 1.5, "4 6"); f.line(400, 36, 400, 446, RULE_LIGHT, 1.5, "4 6")
    for x, t in ((100, r"\text{hissi}"), (300, r"\text{laskuvarjo}"), (500, r"\text{kelkkamäki}")): f.tex(x, 22, t, "middle", MUTED)
    # the lift: 60,0 kg, a = 1,0 m/s² up
    m, a = 60.0, 1.0; G = m * g; N = m * (g + a)
    floor = cabin(f, 40, 48, 104, 138)
    person(f, 86, floor, 104)
    vline(f, 170, 150, 170, 100, lab=(18, 0))
    cx, cy, w, h = 90, 292, 44, 76
    d = FBD(f, 0.12, body=(cx, cy, w, h), m=m, a=(0, a))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -4))
    d.force("N", (0, N), (cx - 12, cy + h / 2), "normal", surface=0, lab=(-24, 6))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (160, 300), 46, lab=(18, 8))
    # the canopy: terminal speed, F_v = G
    m = 80.0; G = m * g
    canopy(f, 286, 160, 0.95, 110, "fy416-k-c")
    skydiver_hang(f, 286, 160, 0.95)
    vline(f, 360, 110, 360, 150, lab=(18, 0))
    cx, cy, w, h = 286, 316, 56, 44
    d = FBD(f, 0.085, body=(cx, cy, w, h), m=m, a=(0, 0))
    d.force("F_v", (0, G), (cx - 14, cy - h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-30, 14))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -4))
    d.draw()
    f.tex(366, 300, r"a = 0", "middle", MUTED)
    # the sled: slope rising to the right at 20°, sliding down (to the left), μ = 0,20
    m, deg, mu = KELKKA["m"], KELKKA["deg"], KELKKA["mu"]
    th = math.radians(deg); G = m * g; N = G * math.cos(th); Fmu = mu * N; acc = g * (math.sin(th) - mu * math.cos(th))
    x0, y0 = 418, 176
    t = _dir(deg)
    f.path(f"M{x0},{y0} L{n(x0 + 168 * t[0])},{n(y0 - 168 * t[1])} V{y0} Z", grad(f, "fy416-k-snow", WHITE, COLD_LIGHT), ICE_EDGE, 2.5)
    sled(f, x0 + 104 * t[0], y0 - 104 * t[1], deg, 0.62, "fy416-k-s")
    vline(f, x0 + 70 * t[0] - 12, y0 - 70 * t[1] - 48, x0 + 30 * t[0] - 12, y0 - 30 * t[1] - 48, lab=(-6, -16))
    cx, cy, w, h = 498, 318, 66, 30
    t, nrm, bc, up, down = slope_frame(cx, cy, w, h, deg)
    d = FBD(f, 0.28, body=(cx, cy, w, h, deg), m=m, a=(-acc * t[0], -acc * t[1]))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-16, 14))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 16 * t[0], bc[1] - 16 * t[1]), "normal", surface=deg, lab=(-14, -12))
    d.force("F_mu", (Fmu * t[0], Fmu * t[1]), up, "friction", surface=deg, lab=(10, 18))
    d.draw()
    d.motion(r"\overline{a}", (-t[0], -t[1]), (446, 252), 40, lab=(-4, -18))
    return f.svg()


# ---------------------------------------------------------------- Kaava: friction work on a slope depends on the horizontal distance
def kitkatyo():
    """Kaava: a slope of length L and height h at angle α followed by a flat run-out: the horizontal run of the slope is
    x_1 = L cos α, so the friction work on the slope −μ mg cos α · L equals −μ mg x_1, and on the flat −μ mg x_2."""
    f = Fig("fy416-kitkatyo", 330, "Kaavakuva, ei mittakaavassa: pulkka lähtee levosta mäen huipulta, liukuu suoraa rinnettä alas ja "
            "jatkaa tasaista pitkin, kunnes pysähtyy. Rinteen pituus on L ja korkeus h, ja rinne on kulmassa alfa vaakatasoon nähden. "
            "Rinteen vaakasuora pituus on x 1 eli L kertaa kosini alfa, ja tasaisella pulkka liukuu matkan x 2. Kummallakin "
            "pulkka on piirretty paikallaan, nopeus nolla.")
    deg = 30.0; th = math.radians(deg)
    tx, ty, h = 84, 70, 140
    fx = tx + h / math.tan(th); fy = ty + h
    stop = 520
    f.path(f"M24,{ty} H{tx} L{n(fx)},{fy} H{574} V{fy + 30} H24 Z", grad(f, "fy416-kt-snow", WHITE, COLD_LIGHT), None)
    f.path(f"M24,{ty} H{tx} L{n(fx)},{fy} H{574}", stroke=INK, w=3)
    # the sled at the start and where it stops (no rider in the schematic)
    sled(f, tx - 26, ty, 0, 0.5, "fy416-kt-s1", rider=False, face_left=False)
    sled(f, stop, fy, 0, 0.5, "fy416-kt-s2", rider=False, face_left=False)
    f.tex(tx - 30, ty - 26, r"v_1 = 0", "middle", MUTED)
    f.tex(stop, fy - 32, r"v_2 = 0", "middle", MUTED)
    # L along the slope, h dashed down from the summit, the angle at the foot
    mx, my = (tx + fx) / 2, (ty + fy) / 2
    f.tex(mx + 22, my - 22, r"L", "middle")
    f.line(tx, ty, tx, fy, MUTED, 1.5, "6 5")
    f.tex(tx + 18, (ty + fy) / 2 + 20, r"h", "middle")
    angle_arc(f, fx, fy, 48, 180 - deg, 180, r"\alpha", lab_r=66)
    # the horizontal distances under the ground
    yb = fy + 54
    for x1, x2, lab in ((tx, fx, r"x_1 = L\cos\alpha"), (fx, stop, r"x_2")):
        f.line(x1, yb - 8, x1, yb + 8, INK, 2); f.line(x2, yb - 8, x2, yb + 8, INK, 2); f.line(x1, yb, x2, yb, INK, 2)
        f.tex((x1 + x2) / 2, yb + 24, lab, "middle")
    f.line(stop, fy, stop, yb - 8, MUTED, 1.5, "4 4"); f.line(fx, fy + 30, fx, yb - 8, MUTED, 1.5, "4 4"); f.line(tx, fy + 30, tx, yb - 8, MUTED, 1.5, "4 4")
    return f.svg()


# ---------------------------------------------------------------- Esimerkki: the sled on the slope
def esimerkki():
    """The worked example: a 32,0 kg sled with its rider slides down a 25,0 m slope at 20,0°, μ = 0,200. Situation picture left,
    the force diagram right (the sled a rectangle along the slope), axes x down the slope and y out of it, G's components dashed."""
    m, deg, mu = KELKKA["m"], KELKKA["deg"], KELKKA["mu"]
    th = math.radians(deg); G = m * g; N = G * math.cos(th); Fmu = mu * N; acc = g * (math.sin(th) - mu * math.cos(th))
    f = Fig("fy416-esimerkki", 400, "Vasemmalla tilannekuva: pulkka ja lapsi liukuvat lumista rinnettä alas vasemmalle, ja pulkan yllä "
            "sininen nopeusnuoli osoittaa rinnettä alas. Rinne nousee oikealle kulmassa 20 astetta. Oikealla pulkan voimakuvio, pulkka "
            "suorakulmiona rinteen suuntaisesti kallistettuna, voimat mittakaavassa. Paino G keskipisteestä suoraan alas. Tukivoima N "
            "alapinnasta kohtisuoraan rinteestä ulos, vähän painoa lyhyempänä. Liikekitka F_mu alapinnan ylemmästä kulmasta rinnettä "
            "ylös, lyhyenä. Painon komponentit katkoviivoin keskipisteestä: G x rinnettä alas, kitkaa pidempänä, ja G y kohtisuoraan "
            "rinnettä kohti. Erillään oranssi kiihtyvyysnuoli rinnettä alas. Nurkassa akselit: x rinnettä alas ja y kohtisuoraan "
            "rinteestä ulos.")
    f.tex(110, 22, r"\text{tilannekuva}", "middle", MUTED); f.tex(400, 22, r"\text{voimakuvio}", "middle", MUTED)
    x0, y0 = 18, 300
    t = _dir(deg)
    f.path(f"M{x0},{y0} L{n(x0 + 210 * t[0])},{n(y0 - 210 * t[1])} V{y0} Z", grad(f, "fy416-ex-snow", WHITE, COLD_LIGHT), ICE_EDGE, 2.5)
    sled(f, x0 + 128 * t[0], y0 - 128 * t[1], deg, 0.8, "fy416-ex-s")
    vline(f, x0 + 110 * t[0] - 14, y0 - 110 * t[1] - 92, x0 + 50 * t[0] - 14, y0 - 50 * t[1] - 92, lab=(-4, -18))
    angle_arc(f, x0, y0, 70, 0, deg, r"20^\circ", lab_r=96)
    f.line(234, 36, 234, 388, RULE, 1.5, "6 6")
    cx, cy, w, h = 410, 176, 104, 44
    t, nrm, bc, up, down = slope_frame(cx, cy, w, h, deg)
    d = FBD(f, 0.42, body=(cx, cy, w, h, deg), m=m, a=(-acc * t[0], -acc * t[1]))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-18, 18))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 20 * t[0], bc[1] - 20 * t[1]), "normal", surface=deg, lab=(-14, -12))
    d.force("F_mu", (Fmu * t[0], Fmu * t[1]), up, "friction", surface=deg, lab=(10, 20))
    d.component("G_x", "G", (-t[0], -t[1]), lab=(-22, 12))
    d.component("G_y", "G", (t[1], -t[0]), lab=(28, 2))
    d.draw()
    d.motion(r"\overline{a}", (-t[0], -t[1]), (300, 120), 56, lab=(-4, -18))
    axes_slope(f, 540, 330, deg)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
def malli_laukku():
    """Model diagram for the drawing task: an 18,0 kg suitcase hangs from a spring balance on the ceiling of a lift that has
    started downward and speeds up at 1,5 m/s²: the balance's pull T = m(g − a) is smaller than the weight."""
    m, a = 18.0, 1.5
    G = m * g; T = m * (g - a)
    f = Fig("fy416-malli-laukku", 360, "Mallikuvio. Vasemmalla tilannekuva: hissikori, jonka katosta riippuu jousivaaka, ja vaa'an koukussa "
            "matkalaukku. Hissi liikkuu alas ja kiihtyy. Oikealla laukun voimakuvio, laukku suorakulmiona: paino G keskipisteestä "
            "alas ja vaa'an jännitysvoima T yläpinnasta ylös, painoa lyhyempänä. Erillään sininen nopeusnuoli alas ja oranssi "
            "kiihtyvyysnuoli alas. Ne eivät ole voimia.")
    f.line(80, 14, 80, 40, IRON, 3)
    f.rect(20, 40, 120, 290, GLASS, INK, 3, rx=4)
    f.rect(26, 312, 108, 10, ALUMINIUM, METAL_EDGE, 1.5)
    spring_scale(f, 80, 43, 128)
    suitcase(f, 80, 128)
    vline(f, 162, 120, 162, 190, lab=(16, 0))
    f.line(200, 20, 200, 340, RULE, 1.5, "6 6")
    cx, cy, w, h = 340, 170, 80, 96
    d = FBD(f, 0.42, body=(cx, cy, w, h), m=m, a=(0, -a))
    d.force("T", (0, T), (cx, cy - h / 2), "tension", rope=(0, 1), lab=(22, 6))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -4))
    d.draw()
    d.motion(r"\overline{v}", (0, -1), (480, 110), 70)
    d.motion(r"\overline{a}", (0, -1), (540, 140), 44)
    return f.svg()


def _plate(fid, desc, m, phases, tmax, ymax, ylab_every=100):
    """A force plate's reading in a lift: phases [(t_from, t_to, N)], linear ramps of 0,2 s between them (example data)."""
    f = Fig(fid, 360, desc)
    ax = Axes(f, (92, 300), (500, 52), x=(0, tmax), y=(0, ymax), xticks=list(range(1, tmax + 1)), yticks=list(range(50, ymax + 1, 50)),
              xlabel=r"t\ (\text{s})", ylabel=r"N\ (\text{N})", xfmt=lambda v: str(v) if v % 2 == 0 else "",
              yfmt=lambda v: str(v) if v % ylab_every == 0 else "")
    pts = []
    for k, (t0, t1, F) in enumerate(phases):
        a0 = t0 + (0.1 if k else 0); a1 = t1 - (0.1 if k < len(phases) - 1 else 0)
        pts += [(a0, F), (a1, F)]
    ax.line(pts, HOT, 3)
    return f.svg()


def hissi_kuvaaja():
    """Tutki: a 60,0 kg student stands on a force plate in a lift going up: 588,6 N at rest, 650 N while speeding up (1,0–3,0 s),
    588,6 N at constant speed, 550 N while slowing down (9,0–12,2 s), example data (lesson-answers.py)."""
    G = 60.0 * g
    return _plate("fy416-hissi-kuvaaja", "Kuvaaja mittakaavassa, keksitty esimerkkiaineisto: voima-anturilevyn lukema N newtoneina ajan "
                  "funktiona, kun 60,0 kilogramman opiskelija seisoo levyllä ylöspäin liikkuvassa hississä. Vaaka-akselilla aika 0–14 "
                  "sekuntia, pystyakselilla voima 0–700 newtonia 50 newtonin välein. Hetkeen 1,0 s asti lukema on noin 589 newtonia. "
                  "Hetkestä 1,0 s hetkeen 3,0 s lukema on 650 newtonia. Hetkestä 3,0 s hetkeen 9,0 s lukema on taas noin 589 newtonia. "
                  "Hetkestä 9,0 s noin hetkeen 12,2 s lukema on 550 newtonia, ja sen jälkeen taas noin 589 newtonia.",
                  60.0, [(0, 1.0, G), (1.0, 3.0, 650), (3.0, 9.0, G), (9.0, 12.18, 550), (12.18, 14, G)], 14, 700)


def ex_hissi():
    """Exercise L3-02: a 75,0 kg person on a force plate in a lift going down: 650 N while speeding up (1,0–3,0 s), 735,75 N at
    constant speed, 800 N while slowing down (6,0–8,67 s), example data (answers.py)."""
    G = 75.0 * g
    return _plate("fy416-ex-hissi", "Kuvaaja mittakaavassa, keksitty esimerkkiaineisto: voima-anturilevyn lukema N newtoneina ajan "
                  "funktiona, kun 75,0 kilogramman ihminen seisoo levyllä alaspäin liikkuvassa hississä. Vaaka-akselilla aika 0–10 "
                  "sekuntia, pystyakselilla voima 0–900 newtonia 50 newtonin välein. Hetkeen 1,0 s asti lukema on noin 736 newtonia. "
                  "Hetkestä 1,0 s hetkeen 3,0 s lukema on 650 newtonia. Hetkestä 3,0 s hetkeen 6,0 s lukema on taas noin 736 newtonia. "
                  "Hetkestä 6,0 s noin hetkeen 8,7 s lukema on 800 newtonia, ja sen jälkeen taas noin 736 newtonia.",
                  75.0, [(0, 1.0, G), (1.0, 3.0, 650), (3.0, 6.0, G), (6.0, 6.0 + 2.0 * (G - 650) / (800 - G), 800), (6.0 + 2.0 * (G - 650) / (800 - G), 10, G)], 10, 900, 200)


FIGURES = {"hero": hero, "kolme": kolme, "kitkatyo": kitkatyo, "esimerkki": esimerkki, "malli-laukku": malli_laukku,
           "hissi-kuvaaja": hissi_kuvaaja, "ex-hissi": ex_hissi}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "kolme": "reveals: the force diagrams of a person in a lift speeding up upward, a jumper under a canopy at terminal speed and a sled sliding down a slope with friction",
    "kitkatyo": "reveals: the geometry x_1 = L cos α behind the friction work −μ mg x on a slope and the flat",
    "esimerkki": "reveals: the force diagram of the worked example (a sled sliding down a 20° slope, μ = 0,20)",
    "malli-laukku": "reveals: the model diagram of a suitcase on a spring balance in a lift speeding up downward (shown after the attempt)",
    "hissi-kuvaaja": "safe: a force plate's reading in a lift going up (example data); the accelerations are not given",
    "ex-hissi": "safe: a force plate's reading in a lift going down (example data); the accelerations and the speed are not given",
}
