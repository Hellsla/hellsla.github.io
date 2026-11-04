"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-13` writes them into lesson.md.
FY7 optics colours (course brief): laser light and single-colour rays #e64980, normals and axes dashed grey; light of
one colour in a white-light spectrum in its own colour as in the chapter *Dispersio: prisma ja sateenkaari* (red
#c92a2a, orange #e8590c, yellow #f59f00, green #2b8a3e, blue #1971c2, violet #7048e8), every colour also named in a
label. Angles of the grating figures are computed from d sin θ = k λ (lesson-answers.py)."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, HOT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, GOOD, PAPER, n)
import herolib as H

RAY = "#e64980"          # light rays in FY7 (chapters 10–13)
RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET = HOT, "#e8590c", "#f59f00", GOOD, COLD, "#7048e8"
# the colour of light of wavelength λ (nm) in the spectrum figures: the nearest of the six named colours
BANDS = [(400, VIOLET), (450, BLUE), (500, GREEN), (570, YELLOW), (600, ORANGE), (640, RED)]


def colour(lam):
    return [c for l, c in BANDS if lam >= l][-1]


def dashed(f, x1, y1, x2, y2):
    f.line(x1, y1, x2, y2, MUTED, 1.5, "6 5")


def arc(f, cx, cy, r, a1, a2, color=INK, w=1.5):
    """An angle arc around (cx, cy) from direction a1 to a2 (degrees, 0 = right, 90 = down, SVG y down)."""
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 1 if a2 > a1 else 0
    f.path(f"M{n(p1[0])},{n(p1[1])} A{r},{r} 0 {large},{sweep} {n(p2[0])},{n(p2[1])}", stroke=color, w=w)


def ray(f, x1, y1, x2, y2, color=RAY, w=3, head=True, opacity=1.0):
    """A light ray with a small filled arrowhead in its middle."""
    op = f' stroke-opacity="{opacity:g}"' if opacity < 1 else ""
    f.add(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{color}" stroke-width="{w:g}" stroke-linecap="round"{op}/>')
    if head:
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        mx, my = (x1 + x2) / 2 + ux * 6, (y1 + y2) / 2 + uy * 6
        h, hw = 13, 6
        f.path(f"M{n(mx)},{n(my)} L{n(mx - ux * h - uy * hw)},{n(my - uy * h + ux * hw)} "
               f"L{n(mx - ux * h + uy * hw)},{n(my - uy * h - ux * hw)} Z", fill=color)


def dim(f, x1, y1, x2, y2, color=INK):
    """A dimension line with filled arrowheads at both ends."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    f.arrow(mx, my, x1, y1, color, 1.5, 10); f.arrow(mx, my, x2, y2, color, 1.5, 10)


def laser_body(f, x, y, length=96):
    """A laser pointer lying along the x axis, its aperture at (x, y)."""
    f.rect(x - length, y - 13, length - 6, 26, IRON, INK, 2, 5)
    f.rect(x - 8, y - 9, 8, 18, ALUMINIUM, INK, 2, 2)
    f.rect(x - length + 18, y - 13, 12, 26, METAL_EDGE)


def slit():
    """Diffraction at a wide and at a narrow slit: plane wavefronts from the left, the wavefronts behind the slit."""
    f = Fig("fy713-slit", 360, "Periaatekuva, ei mittakaavassa: kaksi paneelia päällekkäin. Kummassakin vasemmalta tulee "
            "tasaisia aaltorintamia, jotka osuvat seinään, jossa on rako. Ylemmässä paneelissa rako on monta "
            "aallonpituutta leveä: raon takana aaltorintamat jatkuvat lähes suorina, vain reunoilta vähän kaartuen, ja "
            "valo etenee kapeana kimppuna. Alemmassa paneelissa rako on aallonpituuden levyinen: raon takana "
            "aaltorintamat ovat puoliympyröitä, ja valo leviää laajalle alueelle myös seinän taakse.")
    lam = 20
    for k, (y0, a, label) in enumerate(((22, 96, r"\text{leveä rako}"), (196, 16, r"\text{kapea rako}"))):
        h, yc, xs = 150, y0 + 75, 200
        f.defs_add(f'<clipPath id="fy713-slit-c{k}"><rect x="12" y="{y0}" width="576" height="{h}"/></clipPath>')
        f.rect(12, y0, 576, h, GLASS, RULE, 1.5, 6)
        f.add(f'<g clip-path="url(#fy713-slit-c{k})">')
        for j in range(8):                                   # incoming plane wavefronts
            x = xs - 14 - lam * j
            if x > 24: f.line(x, y0 + 8, x, y0 + h - 8, RAY, 2.5)
        top, bot = yc - a / 2, yc + a / 2
        for j in range(1, 20):                               # wavefronts behind the slit
            r = lam * j - 6
            op = max(0.25, 1 - j * 0.035)
            if a > 40:                                       # wide: straight middle, rounded ends around the edges
                e = 14 + 0.9 * j
                p1 = (xs + r * math.cos(math.radians(-e)), top + r * math.sin(math.radians(-e)))
                p2 = (xs + r * math.cos(math.radians(e)), bot + r * math.sin(math.radians(e)))
                d = (f"M{n(p1[0])},{n(p1[1])} A{r},{r} 0 0,1 {n(xs + r)},{n(top)} L{n(xs + r)},{n(bot)} "
                     f"A{r},{r} 0 0,1 {n(p2[0])},{n(p2[1])}")
            else:                                            # narrow: half circles
                p1 = (xs + r * math.cos(math.radians(-80)), yc + r * math.sin(math.radians(-80)))
                p2 = (xs + r * math.cos(math.radians(80)), yc + r * math.sin(math.radians(80)))
                d = f"M{n(p1[0])},{n(p1[1])} A{r},{r} 0 0,1 {n(p2[0])},{n(p2[1])}"
            f.add(f'<path d="{d}" fill="none" stroke="{RAY}" stroke-width="2.5" stroke-opacity="{op:.2f}"/>')
        f.add('</g>')
        f.rect(xs - 10, y0 + 1, 10, top - y0 - 1, IRON, INK, 2)          # the wall with the slit
        f.rect(xs - 10, bot, 10, y0 + h - 1 - bot, IRON, INK, 2)
        f.tex(30, y0 + 22, label, "start", bg=True)
    return f.svg()


def young():
    """Young's double slit: circular wavefronts from two slits overlap; bright and dark fringes on the screen."""
    f = Fig("fy713-young", 360, "Periaatekuva, ei mittakaavassa: Youngin kaksoiskoe ylhäältä nähtynä. Vasemmalta tulee "
            "tasaisia aaltorintamia seinään, jossa on kaksi kapeaa rakoa S1 ja S2. Kummastakin raosta lähtee "
            "ympyränmuotoisia aaltorintamia, jotka menevät päällekkäin. Oikealla varjostimella vuorottelevat kirkkaat "
            "ja tummat juovat; keskellä on kirkas juova. Kohtaan P, joka on ensimmäinen kirkas juova keskijuovan "
            "yläpuolella, on raosta S2 yhden aallonpituuden pidempi matka kuin raosta S1.")
    lam, xs, y1, y2, xr = 24, 150, 130, 210, 480
    yc = (y1 + y2) / 2
    f.defs_add('<clipPath id="fy713-young-c"><rect x="154" y="16" width="322" height="296"/></clipPath>')
    for j in range(4):
        x = xs - 14 - lam * j
        f.line(x, 30, x, 300, RAY, 2.5)
    f.add('<g clip-path="url(#fy713-young-c)">')
    for (sy) in (y1, y2):
        for j in range(1, 15):
            r = lam * j
            p1 = (xs + r * math.cos(math.radians(-86)), sy + r * math.sin(math.radians(-86)))
            p2 = (xs + r * math.cos(math.radians(86)), sy + r * math.sin(math.radians(86)))
            f.add(f'<path d="M{n(p1[0])},{n(p1[1])} A{r},{r} 0 0,1 {n(p2[0])},{n(p2[1])}" fill="none" stroke="{RAY}" '
                  f'stroke-width="2" stroke-opacity="0.55"/>')
    f.add('</g>')
    # the wall with two slits
    f.rect(xs - 4, 16, 10, y1 - 5 - 16, IRON, INK, 2)
    f.rect(xs - 4, y1 + 5, 10, y2 - y1 - 10, IRON, INK, 2)
    f.rect(xs - 4, y2 + 5, 10, 312 - y2 - 5, IRON, INK, 2)
    # the fringes on the screen: I ∝ cos²(π d sin θ / λ), d = 80, λ = 24 (schematic units)
    f.rect(xr, 16, 20, 296, INK)
    for k in range(148):
        y = 16 + 2 * k + 1
        th = math.atan((y - yc) / (xr - xs))
        I = math.cos(math.pi * (y2 - y1) * math.sin(th) / lam) ** 2
        if I > 0.04: f.rect(xr, y - 1, 20, 2, RAY, extra=f'fill-opacity="{I:.2f}"')
    f.rect(xr, 16, 20, 296, "none", INK, 2)
    # the path lengths to the first bright fringe above the centre (Δs = λ)
    th1 = math.asin(lam / (y2 - y1)); yp = yc - (xr - xs) * math.tan(th1)
    f.line(xs + 1, y1, xr, yp, INK, 2); f.line(xs + 1, y2, xr, yp, INK, 2)
    f.circle(xr, yp, 5, WHITE, INK, 2)
    f.tex(xs - 12, y1, r"S_1", "end", bg=True)
    f.tex(xs - 12, y2, r"S_2", "end", bg=True)
    f.tex(xr + 30, yp, r"P", "start")
    f.tex(xr + 30, yc, r"\text{kirkas}", "start")
    yd = yc + (xr - xs) * math.tan(math.asin(lam / 2 / (y2 - y1)))
    f.tex(xr + 30, yd + 4, r"\text{tumma}", "start")
    f.tex(300, 338, r"\text{kohdassa P}\ \ s_2 - s_1 = \lambda", "middle", w=330)
    return f.svg()


def pattern():
    """Graph: the brightness on the screen for a double slit and for a grating of 8 slits with the same d."""
    f = Fig("fy713-pattern", 340, "Kuvaaja mittakaavassa: valon intensiteetti varjostimella suhteessa suurimpaan arvoon "
            "naapurirakojen matkaeron funktiona, kun matkaero on ilmaistu aallonpituuksina nollasta 3,2:een. "
            "Kaksoisraon katkoviivakäyrä vaihtelee tasaisesti: huiput kohdissa 0, 1, 2 ja 3 ja nollakohdat niiden "
            "puolivälissä. Kahdeksan raon hilan käyrä on samoissa kohdissa olevia kapeita ja korkeita huippuja, ja "
            "niiden välissä intensiteetti on lähes nolla. Rakojen leveyden vaikutus on jätetty pois.")
    ax = Axes(f, (96, 290), (480, 70), x=(0, 3.2), y=(0, 1.36), xticks=[0.5 * k for k in range(1, 7)],
              yticks=[0.25, 0.5, 0.75, 1.0], xlabel=r"\tfrac{\Delta s}{\lambda}", ylabel=r"\text{intensiteetti}",
              xfmt=lambda v: fi(v) if v == int(v) else "", yfmt=lambda v: fi(v, 1) if v in (0.5, 1.0) else "")
    ax.curve(lambda u: math.cos(math.pi * u) ** 2, 0, 3.2, INK, 2.5, 320, "7 6")

    def grating(u, N=8):
        s = math.sin(math.pi * u)
        return 1.0 if abs(s) < 1e-9 else (math.sin(N * math.pi * u) / (N * s)) ** 2
    ax.curve(grating, 0, 3.2, RAY, 3, 1280)
    # legend in one row above the curves (they never exceed 1)
    lx1, lx2, ly = ax.X(0.1), ax.X(1.85), ax.Y(1.24)
    f.line(lx1, ly, lx1 + 40, ly, INK, 2.5, "7 6"); f.tex(lx1 + 50, ly, r"\text{kaksoisrako}", "start", bg=True)
    f.line(lx2, ly, lx2 + 40, ly, RAY, 3); f.tex(lx2 + 50, ly, r"\text{hila, 8 rakoa}", "start", color=RAY, bg=True)
    return f.svg()


def white():
    """White light through a grating of 300 lines/mm: the first-order fans (to scale) and the screen seen from the front."""
    f = Fig("fy713-white", 350, "Kaavakuva, kulmat ja varjostimen etäisyydet mittakaavassa hilalle, jossa on 300 viivaa "
            "millimetrillä. Ylhäällä tilanne ylhäältä nähtynä: valkoinen valo tulee vasemmalta hilaan. Suoraan läpi "
            "jatkaa valkoinen keskimaksimi, k = 0. Sen molemmin puolin ensimmäisen kertaluvun valo hajoaa väreiksi: "
            "violetti 400 nm poikkeaa vähiten, 6,9 astetta, ja punainen 700 nm eniten, 12,1 astetta. Alhaalla "
            "varjostin edestä nähtynä metrin etäisyydellä hilasta: keskellä valkoinen täplä ja kummallakin puolella "
            "ensimmäisen ja toisen kertaluvun spektri, violetti sisäreunalla ja punainen ulkoreunalla. Kolmannen "
            "kertaluvun spektri alkaa jo toisen kertaluvun spektrin sisältä, joten ne menevät osittain päällekkäin.")
    d = 1e-3 / 300
    gx, yc, sx = 150, 120, 490                               # grating, axis, screen in the top view
    f.line(24, yc, gx, yc, INK, 7); f.line(24, yc, gx, yc, WHITE, 4)
    for lam in (400, 450, 500, 550, 600, 650, 700):
        th = math.asin(lam * 1e-9 / d)
        for s in (-1, 1):
            ray(f, gx, yc, sx, yc + s * (sx - gx) * math.tan(th), colour(lam), 2.5, head=False)
    f.line(gx, yc, sx, yc, INK, 7); f.line(gx, yc, sx, yc, WHITE, 4)
    f.rect(gx - 4, yc - 52, 8, 104, GLASS, INK, 2, 2)                       # the grating
    for k in range(12): f.line(gx - 4, yc - 46 + 8.4 * k, gx + 4, yc - 46 + 8.4 * k, MUTED, 1)
    f.rect(sx, 20, 10, 200, IRON, INK, 2)                                    # the screen, edge on
    f.tex(24, 40, r"\text{valkoinen valo}", "start")
    f.tex(gx + 14, 196, r"\text{hila}", "start")
    for lam, name in ((700, r"700\,\text{nm}"), (400, r"400\,\text{nm}")):
        y = yc - (sx - gx) * math.tan(math.asin(lam * 1e-9 / d))
        f.tex(sx + 18, y, name, "start", w=82)
    f.tex(sx + 18, yc, r"k = 0", "start")
    # the screen from the front, 1,00 m from the grating, from −47 cm to +47 cm
    x0, x1, ys, hs = 40, 560, 248, 40
    cx, sc = (x0 + x1) / 2, (x1 - x0) / 2 / 47
    f.rect(x0, ys, x1 - x0, hs, INK, INK, 2, 3)
    f.defs_add(f'<clipPath id="fy713-white-c"><rect x="{x0}" y="{ys}" width="{x1 - x0}" height="{hs}"/></clipPath>')
    f.add('<g clip-path="url(#fy713-white-c)">')
    for k in (1, 2, 3):
        for s in (-1, 1):
            for lam in range(400, 701, 4):
                x = 100 * math.tan(math.asin(k * lam * 1e-9 / d))           # cm on the screen
                f.rect(cx + s * x * sc - 1.5, ys + 4, 3.5, hs - 8, colour(lam), extra='fill-opacity="0.75"')
    f.add('</g>')
    f.circle(cx, ys + hs / 2, 9, WHITE)
    f.rect(x0, ys, x1 - x0, hs, "none", INK, 2, 3)
    for k, xcm in ((0, 0), (1, 16.8), (2, 31), (3, 43)):
        f.tex(cx + xcm * sc, ys + hs + 22, fr"k = {k}", "middle")
    return f.svg()


def geometry():
    """The path difference of the rays from two neighbouring slits: Δs = d sin θ."""
    f = Fig("fy713-geometry", 360, "Kaavakuva, ei mittakaavassa: hilan kaksi vierekkäistä rakoa suurennettuna. Rakojen "
            "etäisyys on hilavakio d. Valo tulee vasemmalta kohtisuoraan hilaan. Kummastakin raosta lähtee "
            "yhdensuuntainen säde kulmassa theeta alkuperäiseen suuntaan nähden, jota näyttää vaakasuora katkoviiva. "
            "Alemmasta raosta piirretty kohtisuora jana ylemmän raon säteeseen erottaa ylemmän raon säteestä "
            "ylimääräisen matkan, matkaeron delta s. Suorakulmaisessa kolmiossa, jonka hypotenuusa on d ja kulma "
            "theeta, matkaero on d kertaa sini theeta.")
    xs, ya, yb, th = 190, 70, 210, math.radians(24)
    u = (math.cos(th), math.sin(th))                         # the rays go down to the right at θ
    for y in (40, 120, 200, 280):
        f.arrow(36, y, 168, y, RAY, 3, 13)
    # the grating: a wall with two slits
    f.rect(xs - 5, 24, 10, ya - 7 - 24, IRON, INK, 2)
    f.rect(xs - 5, ya + 7, 10, yb - ya - 14, IRON, INK, 2)
    f.rect(xs - 5, yb + 7, 10, 316 - yb - 7, IRON, INK, 2)
    Lr = 200                                                 # the rays end above and left of the label "kohti varjostinta"
    ray(f, xs, ya, xs + Lr * u[0], ya + Lr * u[1]); ray(f, xs, yb, xs + Lr * u[0], yb + Lr * u[1])
    dashed(f, xs, yb, 430, yb)
    arc(f, xs, yb, 62, 0, 24)
    f.tex(xs + 84, yb + 15, r"\theta", "middle", w=26)
    # the perpendicular from the lower slit to the upper ray, its foot F and the right angle
    t = (yb - ya) * u[1]
    F = (xs + t * u[0], ya + t * u[1])
    dashed(f, xs, yb, F[0], F[1])
    q = 10; nx, ny = -u[1], u[0]                             # the right-angle mark at F
    f.path(f"M{n(F[0] - u[0] * q)},{n(F[1] - u[1] * q)} L{n(F[0] - u[0] * q - nx * q)},{n(F[1] - u[1] * q - ny * q)} "
           f"L{n(F[0] - nx * q)},{n(F[1] - ny * q)}", stroke=INK, w=1.5)
    # θ in the triangle at the lower slit, between the wall (up) and the perpendicular
    a2 = math.degrees(math.atan2(F[1] - yb, F[0] - xs))
    arc(f, xs, yb, 40, -90, a2)
    f.tex(xs + 13, yb - 62, r"\theta", "middle", w=26)
    # the path difference: a bracket beside the upper ray from the slit to F
    o = 16; pnx, pny = u[1], -u[0]
    A1 = (xs + pnx * o, ya + pny * o); F1 = (F[0] + pnx * o, F[1] + pny * o)
    f.line(A1[0], A1[1], F1[0], F1[1], INK, 2)
    f.line(xs + pnx * 8, ya + pny * 8, A1[0], A1[1], INK, 2); f.line(F[0] + pnx * 8, F[1] + pny * 8, F1[0], F1[1], INK, 2)
    f.tex(F1[0] + 14, F1[1] - 26, r"\Delta s = d\sin\theta", "start")
    # d beside the wall
    dim(f, xs - 16, ya, xs - 16, yb)
    f.tex(xs - 26, (ya + yb) / 2, r"d", "end", w=26, bg=True)
    f.tex(xs, 338, r"\text{hila}", "middle")
    f.tex(588, 330, r"\text{kohti varjostinta}", "end")
    return f.svg()


def setup():
    """Measuring the angle on a screen: laser, grating, screen at distance L, tan θ1 = x1 : L (to scale)."""
    f = Fig("fy713-setup", 350, "Kaavakuva mittakaavassa ylhäältä nähtynä: vasemmalla laser, jonka säde osuu "
            "kohtisuoraan hilaan. Hilassa on 600 viivaa millimetrillä, ja laserin aallonpituus on 532 nm. Hilasta "
            "metrin päässä on varjostin. Suoraan läpi menevä valo osuu varjostimelle kohtaan k = 0, ja ensimmäisen "
            "kertaluvun säteet k = 1 ja k = −1 poikkeavat 18,6 asteen kulmassa ja osuvat varjostimelle 33,7 cm "
            "keskimaksimin kummallekin puolelle. Kulma theeta 1 on merkitty hilan kohdalle, etäisyys L hilasta "
            "varjostimelle ja etäisyys x1 keskimaksimista ensimmäiseen maksimiin.")
    sc = 300                                                 # px per metre
    gx, yc, L = 140, 170, 1.00
    sx = gx + sc * L
    th = math.asin(532e-9 / (1e-3 / 600)); x1 = L * math.tan(th)
    laser_body(f, gx - 30, yc, 92)
    ray(f, gx - 30, yc, gx, yc, head=False)
    dashed(f, gx, yc, sx, yc)
    for s in (-1, 0, 1):
        ray(f, gx, yc, sx, yc - s * sc * x1)
    f.rect(gx - 4, yc - 50, 8, 100, GLASS, INK, 2, 2)
    for k in range(11): f.line(gx - 4, yc - 44 + 8.8 * k, gx + 4, yc - 44 + 8.8 * k, MUTED, 1)
    f.rect(sx, 34, 10, 272, WHITE, INK, 2)
    for s in (-1, 0, 1):
        f.circle(sx + 5, yc - s * sc * x1, 6, RAY, INK, 1.5)
    arc(f, gx, yc, 70, -math.degrees(th), 0)
    f.tex(gx + 104, yc - 17, r"\theta_1", "middle", w=36)
    # x1 beside the screen, L under the drawing
    dim(f, sx + 26, yc, sx + 26, yc - sc * x1)
    f.tex(sx + 38, yc - sc * x1 / 2, r"x_1", "start", w=36)
    for s, lab in ((1, r"k = 1"), (0, r"k = 0"), (-1, r"k = -1")):
        f.tex(588, yc - s * sc * x1, lab, "end", w=72)
    dim(f, gx, 326, sx, 326)
    f.tex((gx + sx) / 2, 306, r"L", "middle", w=26, bg=True)
    f.tex(gx - 76, yc + 34, r"\text{laser}", "middle")
    f.tex(gx + 14, yc + 70, r"\text{hila}", "start")
    f.tex(sx - 8, 18, r"\text{varjostin}", "middle")
    return f.svg()


def hero():
    """The opening illustration: in a dark classroom a laser shines through a grating slide; a row of red spots on the wall."""
    f = H.hero("fy713-hero", "Kuvitus: pimeä luokkahuone. Pöydällä vasemmalla on laserosoitin pienellä telineellä, ja sen "
               "edessä diakehykseen kiinnitetty ohut läpinäkyvä kalvo. Laserin säde kulkee kalvon läpi, ja kalvosta "
               "lähtee viuhkana heikkoja säteitä oikealla olevalle valkoiselle seinätaululle. Taululla on vaakasuora "
               "rivi tasavälisiä punaisia valopisteitä; keskimmäinen on kirkkain, ja reunoja kohti pisteet himmenevät.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy713h-wall", INK, IRON))
    f.rect(0, 430, 1200, 170, H.grad(f, "fy713h-table", SAND, GRAIN))
    f.line(0, 430, 1200, 430, INK, 3)
    # the whiteboard on the right, seen at a slant
    bx = [(760, 110), (1150, 60), (1150, 420), (760, 400)]
    f.path("M" + " L".join(f"{x},{y}" for x, y in bx) + " Z", RULE_LIGHT, INK, 4)
    f.path("M772,122 L1138,76 L1138,408 L772,390 Z", WHITE)
    # the laser pointer on a stand and the grating slide
    f.rect(150, 392, 26, 38, IRON, INK, 3, 3)
    f.rect(70, 362, 190, 32, ALUMINIUM, INK, 3, 10)
    f.rect(232, 366, 28, 24, METAL_EDGE, INK, 2, 4)
    f.rect(90, 362, 18, 32, IRON)
    f.rect(392, 420, 56, 12, IRON, INK, 3, 2)
    f.rect(404, 316, 32, 108, WHITE, INK, 3, 4)
    f.rect(412, 334, 16, 72, COLD_LIGHT, INK, 2, 2)
    # the beams: the laser to the slide, then a fan to the spots on the board
    gx, gy = 420, 378
    f.line(260, 378, gx, gy, RAY, 5)
    spots = []
    for k in range(-3, 4):
        x = 955 + 64 * k; y = 238 - 6 * k                     # along the slanted board
        spots.append((k, x, y))
        f.add(f'<line x1="{gx}" y1="{gy}" x2="{x}" y2="{y}" stroke="{RAY}" stroke-width="3" stroke-opacity="{0.5 - 0.1 * abs(k):.2f}"/>')
    f.defs_add(f'<radialGradient id="fy713h-glow"><stop offset="0" stop-color="{WHITE}"/><stop offset="0.3" '
               f'stop-color="{RAY}"/><stop offset="1" stop-color="{RAY}" stop-opacity="0"/></radialGradient>')
    for k, x, y in spots:
        r = 34 - 6 * abs(k)
        f.circle(x, y, r, "url(#fy713h-glow)")
        f.circle(x, y, 7 - abs(k), RAY)
    return f.svg()


def scene():
    """A second everyday scene: a CD on a desk under a lamp shows bands of rainbow colours."""
    f = H.scene("fy713-scene", "Kuvitus: pöydällä on CD-levy, jota valaisee pöytälamppu vasemmalta ylhäältä. Levyn "
                "hopeisella pinnalla näkyy keskiöstä reunalle ulottuvia sateenkaaren värisiä vyöhykkeitä, joissa värit "
                "ovat järjestyksessä violetista punaiseen.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 250, 600, 110, H.grad(f, "fy713s-desk", SAND_LIGHT, SAND))
    f.line(0, 250, 600, 250, INK, 2.5)
    # the desk lamp
    f.rect(40, 236, 90, 16, IRON, INK, 2.5, 4)
    f.path("M84,236 L104,110 L176,70", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M160,52 L222,84 L200,118 L140,88 Z", IRON, INK, 2.5)
    f.path("M200,118 L140,88", stroke=HEAT_LIGHT, w=6, extra='stroke-linecap="round"')
    # the CD lying on the desk (an ellipse in perspective)
    cx, cy, rx, ry = 380, 262, 170, 74
    f.add(f'<ellipse cx="{cx}" cy="{cy + 6}" rx="{rx}" ry="{ry}" fill="{GRAIN}" fill-opacity="0.35"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2.5"/>')
    f.defs_add(f'<clipPath id="fy713s-disc"><ellipse cx="{cx}" cy="{cy}" rx="{rx - 2}" ry="{ry - 2}"/></clipPath>')
    f.add('<g clip-path="url(#fy713s-disc)">')
    cols = [VIOLET, BLUE, GREEN, YELLOW, ORANGE, RED]
    for side, a0 in ((1, -40.0), (-1, 140.0)):               # two bands of colour on opposite sides of the centre
        for j, c in enumerate(cols):
            a1 = math.radians(a0 + 5 * j); a2 = math.radians(a0 + 5 * j + 5)
            p1 = (cx + 2 * rx * math.cos(a1), cy + 2 * ry * math.sin(a1))
            p2 = (cx + 2 * rx * math.cos(a2), cy + 2 * ry * math.sin(a2))
            f.path(f"M{cx},{cy} L{n(p1[0])},{n(p1[1])} L{n(p2[0])},{n(p2[1])} Z", c, extra='fill-opacity="0.75"')
    f.add('</g>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * 0.24:.1f}" ry="{ry * 0.24:.1f}" fill="{GLASS}" stroke="{INK}" stroke-width="2"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * 0.09:.1f}" ry="{ry * 0.09:.1f}" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="2"/>')
    return f.svg()


FIGURES = {"hero": hero, "slit": slit, "young": young, "pattern": pattern, "white": white, "geometry": geometry,
           "setup": setup, "scene": scene}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "slit": "reveals: a narrower slit spreads the light more (diffraction)",
    "young": "reveals: two slits give alternating bright and dark fringes; at the first bright fringe s2 − s1 = λ",
    "pattern": "reveals: a grating's maxima are at the same Δs = kλ as a double slit's but narrow and bright",
    "white": "reveals: in a grating red deviates most (300 lines/mm: 400 nm 6,9°, 700 nm 12,1°), the 2nd and 3rd orders overlap",
    "geometry": "reveals: the path difference of neighbouring slits is Δs = d sin θ",
    "setup": "reveals: 600 lines/mm, 532 nm, L = 1,00 m: θ1 = 18,6°, x1 = 33,7 cm; tan θ1 = x1 : L",
}
