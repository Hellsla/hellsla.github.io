"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-11` writes them into lesson.md.
FY7 optics colours (course brief): a single-colour ray #e64980, normals dashed grey. Light of one colour is drawn in
its own colour (red #c92a2a, orange #e8590c, yellow #f59f00, green #2b8a3e, blue #1971c2, violet #7048e8); white
light is a white line with an ink outline. Every colour is also named in a label, never carried by colour alone.
Ray paths are computed with Snell's law in vector form (refract, reflect); where the colours are spread more than
in reality the description says so."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    HEAT_LIGHT, HEAT, HOT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, PAPER, ICE, SAND_DARK, n)
import herolib as H

RAY = "#e64980"
RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET = HOT, HEAT, "#f59f00", GOOD, COLD, "#7048e8"
SPECTRUM = [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]
# measured data (lesson text): crown glass N-BK7, SCHOTT optical glass catalogue 2017
BK7 = [(404.7, 1.53024), (435.8, 1.52668), (486.1, 1.52238), (546.1, 1.51872), (589.3, 1.51673), (656.3, 1.51432)]
CAUCHY = {"bk7": (1.50411, 0.00446253, -3.09312e-05), "water": (1.32289, 0.00395357, -0.000105379),
          "flint": (1.59582, 0.00791448, 0.000154174)}      # n = A + B / λ² + C / λ⁴, λ in µm (sim.js has the same)


def n_of(mat, lam_nm):
    a, b, c = CAUCHY[mat]; x = (lam_nm / 1000) ** -2
    return a + b * x + c * x * x


# --- vector optics in figure coordinates (y down) ---
def unit(x, y):
    L = math.hypot(x, y); return (x / L, y / L)


def refract(d, nrm, eta):
    """d: unit direction; nrm: unit normal on the side the ray comes from; eta = n1 / n2. None: total reflection."""
    ci = -(d[0] * nrm[0] + d[1] * nrm[1])
    k = 1 - eta * eta * (1 - ci * ci)
    if k < 0: return None
    f = eta * ci - math.sqrt(k)
    return unit(eta * d[0] + f * nrm[0], eta * d[1] + f * nrm[1])


def reflect(d, nrm):
    k = 2 * (d[0] * nrm[0] + d[1] * nrm[1]); return (d[0] - k * nrm[0], d[1] - k * nrm[1])


def hit_line(p, d, a, b):
    """Where the ray p + t d meets the line a–b: (t, point)."""
    ex, ey = b[0] - a[0], b[1] - a[1]
    den = d[0] * ey - d[1] * ex
    t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
    return t, (p[0] + t * d[0], p[1] + t * d[1])


def hit_circle(p, d, c, r):
    """The far intersection of the ray p + t d (p on or in the circle) with the circle."""
    fx, fy = p[0] - c[0], p[1] - c[1]
    b = fx * d[0] + fy * d[1]; cc = fx * fx + fy * fy - r * r
    t = -b + math.sqrt(max(0.0, b * b - cc))
    return (p[0] + t * d[0], p[1] + t * d[1])


def white_ray(f, a, b, w=7):
    f.line(a[0], a[1], b[0], b[1], INK, w + 3, cap="round")
    f.line(a[0], a[1], b[0], b[1], WHITE, w, cap="round")


def arrowhead(f, p, d, colour, size=13):
    """A filled arrowhead with its tip at p pointing along d."""
    bx, by = p[0] - d[0] * size, p[1] - d[1] * size; hw = size * 0.45
    f.path(f"M{n(p[0])},{n(p[1])} L{n(bx - d[1] * hw)},{n(by + d[0] * hw)} L{n(bx + d[1] * hw)},{n(by - d[0] * hw)} Z", colour)


def arc(f, c, r, a0, a1, colour=INK, w=2):
    """A circular arc around c from angle a0 to a1 (degrees, SVG angles: 0 = right, 90 = down)."""
    x0, y0 = c[0] + r * math.cos(math.radians(a0)), c[1] + r * math.sin(math.radians(a0))
    x1, y1 = c[0] + r * math.cos(math.radians(a1)), c[1] + r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0; sweep = 1 if a1 > a0 else 0   # SVG sweep 1: increasing angle
    f.path(f"M{n(x0)},{n(y0)} A{r:g},{r:g} 0 {large} {sweep} {n(x1)},{n(y1)}", stroke=colour, w=w)


def ang(d): return math.degrees(math.atan2(d[1], d[0]))


def angle_arc(f, c, r, da, db, label=None, lr=None, colour=INK, w=2, dx=0, dy=0):
    """The smaller arc around c between the directions da and db, and its label on the bisector at radius lr."""
    a0 = ang(da); diff = (ang(db) - a0 + 180) % 360 - 180
    arc(f, c, r, a0, a0 + diff, colour, w)
    if label:
        m = math.radians(a0 + diff / 2); R = lr or r + 22
        f.tex(c[0] + R * math.cos(m) + dx, c[1] + R * math.sin(m) + dy, label, "middle", colour)


def glass_defs(f, gid):
    f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{COLD_LIGHT}"/></linearGradient>')
    return f"url(#{gid})"


# --- Ydinajatus: white light through a prism ---
def prism():
    f = Fig("fy711-prism", 340, "Periaatekuva, ei mittakaavassa: valkoisen valon kapea kimppu tulee vasemmalta "
            "alhaalta lasiprisman vasempaan sivuun. Prismassa valo hajoaa väreiksi, ja toisesta sivusta lähtee "
            "viuhka: punainen poikkeaa alkuperäisestä suunnastaan vähiten ja violetti eniten, ja niiden välissä ovat "
            "oranssi, keltainen, vihreä ja sininen. Värit osuvat oikealla olevaan valkoiseen varjostimeen "
            "allekkain, punainen ylimpänä. Värien erkaantuminen on piirretty todellista suuremmaksi.")
    T, A, L = (290, 34), 60, 262
    h = math.radians(A / 2)
    B1, B2 = (T[0] - L * math.sin(h), T[1] + L * math.cos(h)), (T[0] + L * math.sin(h), T[1] + L * math.cos(h))
    f.path(f"M{n(T[0])},{n(T[1])} L{n(B2[0])},{n(B2[1])} L{n(B1[0])},{n(B1[1])} Z", glass_defs(f, "fy711-glass1"), INK, 2.5)
    s = 0.55
    P = (T[0] + s * (B1[0] - T[0]), T[1] + s * (B1[1] - T[1]))
    out_l = (-math.cos(h), -math.sin(h))                  # outward normal of the left face
    out_r = (math.cos(h), -math.sin(h))
    d0 = (math.cos(math.radians(-20)), math.sin(math.radians(-20)))   # 50° from the normal for A = 60°
    S = (P[0] - d0[0] * 210, P[1] - d0[1] * 210)
    xs = 520                                              # the screen
    ends = []
    for k, col in enumerate(SPECTRUM):
        nn = 1.47 + 0.032 * k                             # spread exaggerated (description says so)
        d1 = refract(d0, out_l, 1 / nn)
        _, Q = hit_line(P, d1, T, B2)
        d2 = refract(d1, (-out_r[0], -out_r[1]), nn)
        d2 = d2 if (d2[0] * out_r[0] + d2[1] * out_r[1]) > 0 else d2
        t = (xs - Q[0]) / d2[0]
        E = (Q[0] + t * d2[0], Q[1] + t * d2[1])
        f.line(P[0], P[1], Q[0], Q[1], col, 2.5)
        f.line(Q[0], Q[1], E[0], E[1], col, 3)
        ends.append(E)
    # screen with the spectrum on it
    y0, y1 = ends[0][1] - 26, ends[-1][1] + 26
    f.rect(xs, y0, 14, y1 - y0, WHITE, INK, 2, 2)
    for E, col in zip(ends, SPECTRUM):
        f.rect(xs + 1.5, E[1] - 3, 11, 6, col)
    white_ray(f, S, P)
    arrowhead(f, (S[0] + d0[0] * 120, S[1] + d0[1] * 120), d0, INK, 15)
    f.tex(16, 128, r"\text{valkoinen valo}", "start")
    f.tex(min(xs + 7, 588 - 56), y0 - 20, r"\text{punainen}", "middle", RED)
    f.tex(min(xs + 7, 588 - 50), y1 + 20, r"\text{violetti}", "middle", VIOLET)
    f.tex(T[0], B1[1] + 30, r"\text{lasiprisma}", "middle")
    return f.svg()


# --- Ydinajatus: one ray through a raindrop ---
def drop_path(C, R, alpha, nn, d0=(1.0, 0.0)):
    """Entry point, back point, exit point and exit direction of a ray hitting the drop at incidence alpha."""
    a = math.radians(alpha)
    P1 = (C[0] - R * math.cos(a), C[1] - R * math.sin(a))     # upper left, normal at angle alpha from the ray
    nrm = unit(P1[0] - C[0], P1[1] - C[1])
    d1 = refract(d0, nrm, 1 / nn)
    P2 = hit_circle(P1, d1, C, R)
    d2 = reflect(d1, unit(C[0] - P2[0], C[1] - P2[1]))
    P3 = hit_circle(P2, d2, C, R)
    d3 = refract(d2, unit(C[0] - P3[0], C[1] - P3[1]), nn)
    return P1, P2, P3, d3


def drop():
    f = Fig("fy711-drop", 372, "Periaatekuva, ei mittakaavassa: suuri vesipisara. Vasemmalta tulee vaakasuora "
            "valkoisen auringonvalon säde pisaran yläosaan. Tulokohdassa on katkoviivalla piirretty normaali, ja "
            "tulokulma alfa ja taitekulma beeta on merkitty. Pisarassa valo hajoaa: punainen ja violetti säde "
            "kulkevat pisaran takaseinään, heijastuvat siitä ja taittuvat ulos pisaran alaosasta vasemmalle alaspäin. "
            "Violetti lähtee loivemmassa kulmassa kuin punainen. Värien ero on piirretty todellista suuremmaksi.")
    C, R = (392, 160), 118
    f.defs_add(f'<radialGradient id="fy711-drop-g" cx="0.38" cy="0.35" r="0.75"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{WATER_LIGHT}"/></radialGradient>')
    f.circle(C[0], C[1], R, "url(#fy711-drop-g)", WATER, 2.5)
    alpha = 59.5
    paths = [(RED, 1.3315), (VIOLET, 1.40)]                    # violet exaggerated (description says so)
    P1 = None
    for col, nn in paths:
        P1, P2, P3, d3 = drop_path(C, R, alpha, nn)
        f.line(P1[0], P1[1], P2[0], P2[1], col, 2.5)
        f.line(P2[0], P2[1], P3[0], P3[1], col, 2.5)
        E = (P3[0] + d3[0] * 120, P3[1] + d3[1] * 120)
        f.line(P3[0], P3[1], E[0], E[1], col, 3)
        arrowhead(f, E, d3, col, 15)
        if col == RED: Ered, d3r = E, d3
        else: Evio, d3v = E, d3
    white_ray(f, (20, P1[1]), P1, 6)
    arrowhead(f, (130, P1[1]), (1, 0), INK, 15)
    # the normal at the entry point and the angles alpha (outside) and beta (inside)
    nrm = unit(P1[0] - C[0], P1[1] - C[1])
    f.line(P1[0] + nrm[0] * 70, P1[1] + nrm[1] * 70, P1[0] - nrm[0] * 90, P1[1] - nrm[1] * 90, MUTED, 1.5, "6 5")
    a_out = ang(nrm)                                           # direction of the outward normal
    arc(f, P1, 44, 180, a_out + 360 if a_out < 0 else a_out, INK, 2)
    f.tex(P1[0] - 70, P1[1] - 24, r"\alpha", "middle")
    d1 = refract((1.0, 0.0), nrm, 1 / 1.3315)
    arc(f, P1, 52, ang((-nrm[0], -nrm[1])), ang(d1), INK, 2)
    f.tex(P1[0] + 58, P1[1] + 34, r"\beta", "middle")
    f.tex(20, P1[1] - 32, r"\text{auringonvalo}", "start")
    f.tex(588, 58, r"\text{heijastuu}", "end")
    f.tex(Ered[0] + 22, Ered[1] - 12, r"\text{punainen}", "start", RED)
    f.tex(Evio[0] - 16, Evio[1] - 18, r"\text{violetti}", "end", VIOLET)
    return f.svg()


# --- Ydinajatus: the observer, the Sun behind, two drops ---
def observer():
    f = Fig("fy711-observer", 372, "Periaatekuva sivulta, kulmat eivät ole mittakaavassa: tarkkailija seisoo oikealla "
            "selkä aurinkoon päin, ja auringonsäteet tulevat oikealta ylhäältä vinosti alas. Silmästä lähtee "
            "katkoviiva auringonsäteiden suuntaan alas vasemmalle kohti vastapistettä, joka on tarkkailijan pään "
            "varjon kohdalla horisontin alapuolella. Ylempi pisara on 42 asteen kulmassa tästä suunnasta, ja siitä "
            "silmään tulee punainen valo; sen violetti valo kulkee silmän yläpuolelta ohi. Alempi pisara on noin 40,6 "
            "asteen kulmassa, ja siitä silmään tulee violetti valo; sen punainen valo osuu maahan tarkkailijan eteen.")
    ground = 300
    f.rect(12, ground, 576, 46, SAND_LIGHT)
    f.line(12, ground, 588, ground, INK, 2.5)
    eye = (500, 232)
    # the observer, facing left: head, body, legs
    f.circle(eye[0] + 8, eye[1], 15, SAND, INK, 2)
    f.path(f"M{eye[0] - 6},{eye[1] + 17} h28 l4,40 h-36 Z", COLD, INK, 2)
    f.path(f"M{eye[0] + 2},{eye[1] + 57} V{ground} M{eye[0] + 16},{eye[1] + 57} V{ground}", stroke=INK, w=4)
    # sunlight from the upper right, 20° above the horizon (SVG angle 160°: to the left and down)
    sun = 160
    ds = (math.cos(math.radians(sun)), math.sin(math.radians(sun)))
    for x, y in ((582, 34), (582, 92)):
        f.line(x, y, x + ds[0] * 84, y + ds[1] * 84, HEAT, 3)
        arrowhead(f, (x + ds[0] * 92, y + ds[1] * 92), ds, HEAT, 14)
    f.tex(588, 140, r"\text{auringonvalo}", "end")
    # the antisolar direction from the eye, dashed, down to the shadow of the head below the horizon
    t = (ground + 20 - eye[1]) / ds[1]
    f.line(eye[0], eye[1], eye[0] + ds[0] * t, eye[1] + ds[1] * t, MUTED, 2, "7 6")
    # two drops drawn 42° and 33° above that direction (the real difference, 1,7°, is too small to see)
    drops = []
    for deg, r_arc in ((42, 168), (33, 118)):
        a = sun + deg
        u = (math.cos(math.radians(a)), math.sin(math.radians(a)))
        drops.append(((eye[0] + u[0] * 330, eye[1] + u[1] * 330), a, r_arc))
    (Du, au, ru), (Dl, al, rl) = drops
    # the light that reaches the eye: red from the upper drop, violet from the lower drop
    for D, col in ((Du, RED), (Dl, VIOLET)):
        L = math.hypot(eye[0] - D[0], eye[1] - D[1]); u = ((eye[0] - D[0]) / L, (eye[1] - D[1]) / L)
        tip = (eye[0] - u[0] * 22, eye[1] - u[1] * 22)
        f.line(D[0] + u[0] * 14, D[1] + u[1] * 14, tip[0], tip[1], col, 3)
        arrowhead(f, tip, u, col, 14)
    # the other colour of each drop misses the eye: violet from the upper drop passes above, red from the lower hits the ground
    for D, col, rot, length in ((Du, VIOLET, -9, 300), (Dl, RED, 9, None)):
        L = math.hypot(eye[0] - D[0], eye[1] - D[1]); u = ((eye[0] - D[0]) / L, (eye[1] - D[1]) / L)
        c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        v = (u[0] * c - u[1] * s, u[0] * s + u[1] * c)
        tt = length or (ground - D[1]) / v[1]
        f.line(D[0] + v[0] * 14, D[1] + v[1] * 14, D[0] + v[0] * tt, D[1] + v[1] * tt, col, 2, "8 6")
    for D, a, r_arc in drops:
        f.circle(D[0], D[1], 13, WATER_LIGHT, WATER, 2)
    # the angles at the eye, from the antisolar direction up to each drop
    arc(f, eye, ru, sun, au, RED, 2)
    arc(f, eye, rl, sun, al, VIOLET, 2)
    mu, ml = math.radians(sun + 21), math.radians(sun + 16.5)
    f.tex(eye[0] + (ru + 30) * math.cos(mu), eye[1] + (ru + 30) * math.sin(mu), r"42^\circ", "middle", RED)
    f.tex(eye[0] + (rl - 40) * math.cos(ml), eye[1] + (rl - 40) * math.sin(ml) - 4, r"40{,}6^\circ", "middle", VIOLET)
    f.tex(Du[0] + 22, Du[1] - 4, r"\text{punainen}", "start", RED)
    f.tex(Dl[0] - 20, Dl[1] + 2, r"\text{violetti}", "end", VIOLET)
    f.tex(eye[0] + ds[0] * t - 14, ground + 26, r"\text{vastapiste}", "end")
    return f.svg()


# --- Kaava: n(λ) of crown glass ---
def spectrum_band(f, gid, x0, x1, lam0, lam1):
    stops = [(400, VIOLET), (460, BLUE), (520, GREEN), (575, YELLOW), (610, ORANGE), (660, RED)]
    s = "".join(f'<stop offset="{(l - lam0) / (lam1 - lam0):.3f}" stop-color="{c}"/>' for l, c in stops)
    f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{x1}" y2="0">{s}</linearGradient>')
    return f"url(#{gid})"


def n_graph():
    f = Fig("fy711-n-graph", 372, "Kuvaaja mittakaavassa: kruunulasin N-BK7 taitekerroin n tyhjiöaallonpituuden "
            "lambda funktiona välillä 400–700 nm. Kuusi mittauspistettä valmistajan taulukosta: 405 nm 1,5302; 436 nm "
            "1,5267; 486 nm 1,5224; 546 nm 1,5187; 589 nm 1,5167 ja 656 nm 1,5143. Käyrä laskee: lyhyillä "
            "aallonpituuksilla taitekerroin on suurin, ja käyrä loivenee punaista kohti. Vaaka-akselin alla on "
            "näkyvän valon värijana violetista punaiseen.")
    ax = Axes(f, (110, 290), (470, 50), x=(375, 700), y=(1.510, 1.535), xticks=[400, 450, 500, 550, 600, 650, 700],
              yticks=[1.510, 1.515, 1.520, 1.525, 1.530, 1.535], xlabel=r"\lambda\ (\text{nm})", ylabel=r"n",
              xfmt=lambda v: fi(v) if v % 100 == 0 else "", yfmt=lambda v: fi(v, 3), origin_label=False)
    ax.curve(lambda l: n_of("bk7", l), 400, 700, INK, 3)
    for lam, nn in BK7:
        ax.point(lam, nn, INK)
    f.rect(ax.X(400), 336, ax.X(700) - ax.X(400), 12, spectrum_band(f, "fy711-band1", ax.X(400), ax.X(700), 400, 700), INK, 1.5, 2)
    f.tex(ax.X(405) + 16, ax.Y(1.53024), r"\text{violetti}", "start", VIOLET, bg=True)
    f.tex(ax.X(656.3), ax.Y(1.51432) - 30, r"\text{punainen}", "middle", RED, bg=True)
    return f.svg()


def flint_points():
    """Task figure (fy7-11-L2-03): flint glass n at 450–700 nm, seven points on the fitted curve; no answer drawn."""
    f = Fig("fy711-flint-points", 384, "Kuvaaja mittakaavassa: erään flinttilasin taitekerroin n "
            "tyhjiöaallonpituuden lambda funktiona välillä 400–700 nm. Seitsemän pistettä aallonpituuksilla 400, "
            "450, 500, 550, 600, 650 ja 700 nm sekä niiden kautta kulkeva laskeva käyrä. Pystyakselin ruudukon väli "
            "on 0,002 ja vaaka-akselin 50 nm.")
    ax = Axes(f, (110, 300), (470, 64), x=(375, 700), y=(1.610, 1.652),
              xticks=[400, 450, 500, 550, 600, 650, 700], yticks=[1.610 + 0.002 * k for k in range(1, 22)],
              xlabel=r"\lambda\ (\text{nm})", ylabel=r"n", xfmt=lambda v: fi(v) if v % 100 == 0 else "",
              yfmt=lambda v: fi(v, 2) if abs(v * 100 - round(v * 100)) < 1e-6 else "", origin_label=False)
    ax.curve(lambda l: n_of("flint", l), 400, 700, INK, 3)
    for lam in (400, 450, 500, 550, 600, 650, 700):
        ax.point(lam, n_of("flint", lam), INK)
    f.rect(ax.X(400), 346, ax.X(700) - ax.X(400), 12, spectrum_band(f, "fy711-band2", ax.X(400), ax.X(700), 400, 700), INK, 1.5, 2)
    return f.svg()


# --- Kaava: the angles of a prism ---
def prism_angles():
    f = Fig("fy711-prism-angles", 336, "Kaavakuva prismasta: yksivärinen säde tulee vasemmalta prisman vasempaan "
            "sivuun tulokulmassa alfa 1 normaaliin nähden ja taittuu lasissa kulmaan alfa 2. Säde osuu oikeaan "
            "sivuun tulokulmassa alfa 3 ja lähtee prismasta taitekulmassa alfa 4. Molempien pintojen normaalit on "
            "piirretty katkoviivoin. Prisman huipussa on huippukulma A. Tulevan säteen jatke on piirretty "
            "katkoviivana, ja sen ja lähtevän säteen välinen kulma on poikkeamakulma delta.")
    T, A, L = (290, 24), 60, 330
    h = math.radians(A / 2)
    B1, B2 = (T[0] - L * math.sin(h), T[1] + L * math.cos(h)), (T[0] + L * math.sin(h), T[1] + L * math.cos(h))
    f.path(f"M{n(T[0])},{n(T[1])} L{n(B2[0])},{n(B2[1])} L{n(B1[0])},{n(B1[1])} Z", glass_defs(f, "fy711-glass2"), INK, 2.5)
    nn = 1.52
    P = (T[0] + 0.62 * (B1[0] - T[0]), T[1] + 0.62 * (B1[1] - T[1]))
    out_l, out_r = (-math.cos(h), -math.sin(h)), (math.cos(h), -math.sin(h))
    in_l, in_r = (-out_l[0], -out_l[1]), (-out_r[0], -out_r[1])
    d0 = (math.cos(math.radians(-24)), math.sin(math.radians(-24)))     # α1 = 54°
    d1 = refract(d0, out_l, 1 / nn)
    _, Q = hit_line(P, d1, T, B2)
    d2 = refract(d1, in_r, nn)
    S = (P[0] - d0[0] * 180, P[1] - d0[1] * 180)
    E = (Q[0] + d2[0] * 200, Q[1] + d2[1] * 200)
    for X, o in ((P, out_l), (Q, out_r)):                       # the normals
        f.line(X[0] + o[0] * 92, X[1] + o[1] * 92, X[0] - o[0] * 80, X[1] - o[1] * 80, MUTED, 1.5, "6 5")
    f.line(P[0], P[1], P[0] + d0[0] * 330, P[1] + d0[1] * 330, MUTED, 1.5, "4 5")   # the incident ray continued
    f.line(S[0], S[1], P[0], P[1], RAY, 3); arrowhead(f, (S[0] + d0[0] * 90, S[1] + d0[1] * 90), d0, RAY, 14)
    f.line(P[0], P[1], Q[0], Q[1], RAY, 3)
    f.line(Q[0], Q[1], E[0], E[1], RAY, 3); arrowhead(f, E, d2, RAY, 14)
    angle_arc(f, P, 44, (-d0[0], -d0[1]), out_l, r"\alpha_1", 72)
    angle_arc(f, P, 40, d1, in_l, r"\alpha_2", 76, dy=4)
    angle_arc(f, Q, 40, (-d1[0], -d1[1]), in_r, r"\alpha_3", 76, dy=4)
    angle_arc(f, Q, 44, d2, out_r, r"\alpha_4", 72)
    angle_arc(f, T, 40, unit(B1[0] - T[0], B1[1] - T[1]), unit(B2[0] - T[0], B2[1] - T[1]), r"A", 62)
    _, X = hit_line(Q, d2, P, (P[0] + d0[0], P[1] + d0[1]))   # where the exit ray meets the continued incident ray
    angle_arc(f, X, 150, d0, d2, r"\delta", 178, dx=14, dy=-4)
    return f.svg()


# --- Kaava: the exit angle of a ray from a drop against the angle of incidence ---
def theta_graph():
    f = Fig("fy711-theta-graph", 350, "Kuvaaja mittakaavassa: punaisen valon (n = 1,332) säde lähtee vesipisarasta "
            "kulmassa theeta vastapisteen suuntaan nähden. Vaaka-akselilla on tulokulma alfa 0–90 astetta ja "
            "pystyakselilla theeta 0–45 astetta. Käyrä nousee origosta, saavuttaa suurimman arvonsa 42,3 astetta, "
            "kun tulokulma on noin 59,5 astetta, ja laskee sitten noin 15 asteeseen. Huipun lähellä käyrä on "
            "lähes vaakasuora: laajalta tulokulmien väliltä säteet lähtevät lähes samaan suuntaan.")
    ax = Axes(f, (96, 290), (470, 50), x=(0, 90), y=(0, 45), xticks=[10 * k for k in range(1, 10)],
              yticks=[5 * k for k in range(1, 10)], xlabel=r"\alpha\ (^\circ)", ylabel=r"\theta\ (^\circ)",
              xfmt=lambda v: fi(v) if v % 30 == 0 else "", yfmt=lambda v: fi(v) if v % 10 == 0 else "")
    nn = 1.3315
    th = lambda a: 4 * math.degrees(math.asin(math.sin(math.radians(a)) / nn)) - 2 * a
    ax.area([(50, 0), (50, 45), (70, 45), (70, 0)], GOOD_LIGHT, 0.45)
    ax.curve(th, 0, 90, RED, 3)
    amax = math.degrees(math.acos(math.sqrt((nn * nn - 1) / 3)))
    ax.guide(amax, th(amax))
    ax.point(amax, th(amax), RED)
    f.tex(ax.X(amax), ax.Y(th(amax)) - 26, r"42{,}3^\circ", "middle", RED, bg=True)
    f.tex(ax.X(60), ax.Y(8), r"\text{kirkas kaari}", "middle", INK, bg=True)
    return f.svg()


# --- the opening illustration: a rainbow after a summer shower, the Sun behind the viewer ---
def bow_arcs(f, cx, cy, r, w, colours, opacity=1.0):
    for k, col in enumerate(colours):
        rr = r - k * w
        f.add(f'<path d="M{n(cx - rr)},{n(cy)} A{rr:g},{rr:g} 0 0 1 {n(cx + rr)},{n(cy)}" fill="none" stroke="{col}" '
              f'stroke-width="{w + 0.5:g}" stroke-opacity="{opacity:g}"/>')


def hero():
    f = H.hero("fy711-hero", "Kuvitus: kesäsateen jälkeen pellon ja metsän yllä on kirkas sateenkaari, jonka "
               "ulkoreunalla on punainen ja sisäreunalla violetti. Sen ulkopuolella näkyy himmeämpi toinen "
               "sateenkaari, jossa värit ovat päinvastaisessa järjestyksessä, ja kaarten välissä taivas on tummempi. "
               "Taustalla on harmaita sadepilviä. Etualalla ihminen seisoo selin katsojaan ja katsoo kaarta.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy711h-sky", "#8a96a3", "#c4ccd4"))
    cx, cy = 600, 660
    # brighter sky inside the primary bow, darker band between the bows
    f.add(f'<circle cx="{cx}" cy="{cy}" r="470" fill="{GLASS}" fill-opacity="0.55"/>')
    for x, y, sc in ((150, 90, 1.4), (420, 60, 1.1), (900, 80, 1.5), (1110, 150, 1.0)):
        H.cloud(f, x, y, sc, "#6b7480", extra='fill-opacity="0.55"')
    bow_arcs(f, cx, cy, 640, 11, SPECTRUM[::-1], 0.45)      # secondary bow: violet outside, red inside
    bow_arcs(f, cx, cy, 540, 13, SPECTRUM, 0.9)              # primary bow: red outside
    H.hills(f, "fy711h-hill", 410, [COLD_LIGHT, GOOD_LIGHT], amp=26, seed=5)
    H.forest(f, 418, 46, 24, GOOD, seed=7, x0=0, x1=1200, depth=12)
    f.rect(0, 440, 1200, 160, H.grad(f, "fy711h-field", GOOD_LIGHT, SAND_DARK))
    H.red_house(f, 190, 448, 120, 70)
    H.birch(f, 980, 470, 150)
    # the viewer seen from behind (hair covers the whole head)
    H.person(f, 594, 588, shirt=HOT, sc=0.55)
    f.circle(594, 588 - 298 * 0.55, 31 * 0.55, INK)
    return f.svg()


def scene():
    f = H.scene("fy711-scene", "Kuvitus: puutarhassa nurmikkoa kastellaan letkulla. Vesisuihkun pisaroissa näkyy "
                "pieni sateenkaari, kun aurinko paistaa kastelijan selän takaa.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy711s-sky", ICE, GLASS))
    f.rect(0, 250, 600, 110, GOOD_LIGHT)
    # the water jet from the hose and its spray of drops
    f.path("M168,232 C250,150 360,130 470,190", stroke=WATER_LIGHT, w=5, extra='stroke-linecap="round"')
    for k in range(90):
        x = 300 + 260 * H.rnd(k, 3); y = 150 + 150 * H.rnd(k + 300, 3)
        f.circle(x, y, 2 + 1.5 * H.rnd(k + 600, 3), WATER_LIGHT)
    bow_arcs(f, 430, 300, 118, 7, SPECTRUM, 0.8)
    f.rect(0, 296, 600, 64, H.grad(f, "fy711s-lawn2", GOOD_LIGHT, GOOD))
    # the person with the hose, the Sun behind them (to the left, outside the picture)
    H.person(f, 120, 330, shirt=COLD, sc=0.62)
    f.path("M145,248 C155,240 162,236 168,232", stroke=GOOD, w=6, extra='stroke-linecap="round"')
    f.path("M100,330 C80,345 50,345 24,338", stroke=GOOD, w=6, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero, "prism": prism, "drop": drop, "observer": observer, "n-graph": n_graph,
           "prism-angles": prism_angles, "theta-graph": theta_graph, "scene": scene, "flint-points": flint_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "prism": "reveals: a prism spreads white light, violet deviates most and red least",
    "drop": "reveals: in a drop light refracts, reflects once at the back and refracts out; violet leaves at a smaller angle",
    "observer": "reveals: red reaches the eye from drops at 42° and violet from drops at 40,6° from the antisolar point",
    "n-graph": "reveals: crown glass N-BK7 n against λ (1,5302 at 405 nm … 1,5143 at 656 nm), n falls with λ",
    "prism-angles": "safe: prism geometry with α1–α4, the apex angle A and the deviation δ labelled, no values",
    "theta-graph": "reveals: θ(α) of red light in a drop peaks at 42,3° near α = 59,5°",
    "flint-points": "safe: flint glass n against λ at 400–700 nm (seven points on a curve), grid 0,002; no answer",
}
