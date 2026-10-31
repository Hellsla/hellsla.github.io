"""Figures of the investigation Umpinaisen sylinterin hitausmomentti (scripts/figlib.py); `python scripts/investigations.py
figures fy10-hitausmomentti` writes them into investigation.md. No forces are drawn. The only motion arrow is the
velocity of the cylinder's centre, in the velocity colour (teacher's rule: force, velocity and acceleration always in
different colours); the angular velocity is a curved ink arrow. The graph shows models only, never invented measurements."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, HEAT_LIGHT, COLD, n
import herolib as H
from herolib import grad

VELOCITY = "#1971c2"
WOOD, WOOD_EDGE = "#e0b878", "#8a5a1f"


def incline(f, a, b, thick, fill, gid):
    """A straight board whose upper surface runs from a to b; returns the unit vectors downhill d and outward normal nrm."""
    L = math.hypot(b[0] - a[0], b[1] - a[1]); d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    nrm = (d[1], -d[0])                                   # up and out of the surface (SVG y grows downwards)
    pts = [a, b, (b[0] - nrm[0] * thick, b[1] - nrm[1] * thick), (a[0] - nrm[0] * thick, a[1] - nrm[1] * thick)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", fill=fill, stroke=INK, w=2.5)
    return d, nrm


def on_surface(a, d, nrm, s, r):
    """The centre of a circle of radius r touching the surface at distance s from a."""
    return a[0] + d[0] * s + nrm[0] * r, a[1] + d[1] * s + nrm[1] * r


def cylinder_end(f, gid, cx, cy, r, solid=True):
    """A cylinder seen end-on: a solid disc with a radial gradient, or a thin-walled tube (a ring)."""
    if solid:
        f.defs_add(f'<radialGradient id="{gid}" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#e9edf1"/>'
                   f'<stop offset="1" stop-color="{ALUMINIUM}"/></radialGradient>')
        f.circle(cx, cy, r, f"url(#{gid})", INK, 2.5)
    else:
        f.circle(cx, cy, r, "none", METAL_EDGE, max(5, r * 0.12))
        f.circle(cx, cy, r + max(5, r * 0.12) / 2, "none", INK, 2)
        f.circle(cx, cy, r - max(5, r * 0.12) / 2, "none", INK, 2)
    f.circle(cx, cy, 3.5, INK)


def wheel(f, cx, cy, r):
    """A bicycle wheel with its spokes, hub and an axle with two handles, standing on its tyre."""
    f.circle(cx, cy, r, "none", INK, max(8, r * 0.12))
    f.circle(cx, cy, r * 0.9, "none", METAL_EDGE, 3)
    for k in range(18):
        a = k * math.pi / 9
        f.line(cx + r * 0.08 * math.cos(a + 0.4), cy + r * 0.08 * math.sin(a + 0.4), cx + r * 0.88 * math.cos(a), cy + r * 0.88 * math.sin(a), METAL_EDGE, 1.5)
    f.circle(cx, cy, r * 0.1, ALUMINIUM, INK, 2.5)
    f.rect(cx - 6, cy - 6, 12, 12, IRON, INK, 2, rx=3)


def hero():
    """The opening illustration: a board resting on a stack of books, a solid metal cylinder at rest at the top of the
    slope and a stopper at its foot; a thin-walled tube lies on the bench, and a bicycle wheel stands at the right.
    No motion and no timing equipment is shown: how to measure is the student's design."""
    f = H.hero("fy10h-hero", "Kuvitus: työpöydällä on kirjapinon varaan nojaava lauta, joka muodostaa kaltevan tason. Tason "
               "yläpäässä on levossa umpinainen metallisylinteri päästä katsottuna, ja tason poikki pystytetty viivain pitää "
               "sitä paikallaan. Tason alapäässä on pehmeä pysäytin. "
               "Pöydällä on lisäksi ohutseinäinen putki ja oikealla pystyssä polkupyörän rengas akseleineen.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10hh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10hh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # books under the upper end of the board
    for k, c in enumerate(["#4c6ef5", "#e8590c", "#2b8a3e", "#f08c00"]):
        y = 470 - 41.25 * (k + 1)
        f.rect(96 + 4 * (k % 2), y, 134, 41.25, c, INK, 2.5, rx=4)
        f.line(108 + 4 * (k % 2), y + 20, 218 + 4 * (k % 2), y + 20, WHITE, 2)
    a, b = (110, 254), (820, 452)
    d, nrm = incline(f, a, b, 18, grad(f, "fy10hh-board", WOOD, "#c99a55", horizontal=True), "board")
    # the stopper at the foot of the slope
    f.rect(830, 420, 46, 50, "#495057", INK, 2.5, rx=10)
    cx, cy = on_surface(a, d, nrm, 120, 52)
    cylinder_end(f, "fy10hh-cyl", cx, cy, 52)
    # a ruler standing across the slope just below the cylinder holds it at rest until it is lifted away
    s_r, w_r, h_r = 120 + 52, 8, 130
    base = (a[0] + d[0] * s_r, a[1] + d[1] * s_r)
    pts = [base, (base[0] + d[0] * w_r, base[1] + d[1] * w_r),
           (base[0] + d[0] * w_r + nrm[0] * h_r, base[1] + d[1] * w_r + nrm[1] * h_r), (base[0] + nrm[0] * h_r, base[1] + nrm[1] * h_r)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", fill="#ffe8a3", stroke=INK, w=2.5)
    # a thin-walled tube on the bench and the bicycle wheel
    cylinder_end(f, "fy10hh-tube", 960, 470 - 44, 40, solid=False)
    wheel(f, 1100, 470 - 92, 88)
    return f.svg()


def setup():
    """What is measured: the cylinder released from rest rolls down; its centre drops h while it travels s along the
    slope; at the end its centre moves with speed v and the cylinder turns with angular velocity omega; radius r."""
    f = Fig("fy10h-setup", 400, "Kaaviokuva. Umpinainen sylinteri lähtee levosta kaltevan tason yläosasta ja vierii alas. "
            "Matka tason suuntaisesti lähtökohdasta loppukohtaan on s. Sylinterin keskipisteen korkeus laskee matkalla "
            "h:n verran. Loppukohdassa sylinterin keskipisteen nopeus v osoittaa tason suuntaisesti alas, ja sylinteri "
            "pyörii myötäpäivään kulmanopeudella omega. Sylinterin säde on r.")
    a, b = (40, 120), (560, 330)
    d, nrm = incline(f, a, b, 16, SAND_LIGHT, "board")
    f.line(a[0], b[1] - nrm[1] * 16 + 2, 590, b[1] - nrm[1] * 16 + 2, INK, 2)       # the bench
    r = 34; s0, s1 = 50, 410
    c0 = on_surface(a, d, nrm, s0, r); c1 = on_surface(a, d, nrm, s1, r)
    cylinder_end(f, "fy10hs-c0", *c0, r); cylinder_end(f, "fy10hs-c1", *c1, r)
    f.tex(c0[0], c0[1] - r - 20, r"\text{lähtö levosta}", "middle", MUTED)
    # s along the slope, offset below the board
    off = 46
    p0 = (a[0] + d[0] * s0 - nrm[0] * off, a[1] + d[1] * s0 - nrm[1] * off)
    p1 = (a[0] + d[0] * s1 - nrm[0] * off, a[1] + d[1] * s1 - nrm[1] * off)
    f.line(*p0, *p1, INK, 2)
    for p in (p0, p1): f.line(p[0] - nrm[0] * 9, p[1] - nrm[1] * 9, p[0] + nrm[0] * 9, p[1] + nrm[1] * 9, INK, 2)
    for s in (s0, s1):
        q = (a[0] + d[0] * s, a[1] + d[1] * s)
        f.line(q[0] - nrm[0] * 18, q[1] - nrm[1] * 18, q[0] - nrm[0] * (off - 6), q[1] - nrm[1] * (off - 6), MUTED, 1.5, "4 4")
    mid = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    f.tex(mid[0] - 14, mid[1] + 24, r"s", "middle")
    # h: the drop of the centre, measured at the right
    xh = 585
    f.line(c0[0] + r + 6, c0[1], xh + 8, c0[1], MUTED, 1.5, "4 4"); f.line(c1[0] + r + 6, c1[1], xh + 8, c1[1], MUTED, 1.5, "4 4")
    f.line(xh, c0[1], xh, c1[1], INK, 2); f.line(xh - 8, c0[1], xh + 8, c0[1], INK, 2); f.line(xh - 8, c1[1], xh + 8, c1[1], INK, 2)
    f.tex(xh - 8, (c0[1] + c1[1]) / 2, r"h", "end")
    # radius, velocity and angular velocity at the end
    ang = math.radians(-25)
    f.line(c1[0], c1[1], c1[0] + r * math.cos(ang), c1[1] + r * math.sin(ang), INK, 2)
    f.tex(c1[0] + r + 6, c1[1] - 30, r"r", "start")
    tip = (c1[0] + d[0] * 82, c1[1] + d[1] * 82)
    f.arrow(c1[0], c1[1], *tip, VELOCITY, 4, 15)
    f.tex(tip[0] + 8, tip[1] - 4, r"\overline{v}", "start", VELOCITY)
    R = r + 16; t0, t1 = math.radians(-150), math.radians(-60)
    x0, y0 = c1[0] + R * math.cos(t0), c1[1] + R * math.sin(t0); x1, y1 = c1[0] + R * math.cos(t1), c1[1] + R * math.sin(t1)
    f.path(f"M{n(x0)},{n(y0)} A{n(R)},{n(R)} 0 0 1 {n(x1)},{n(y1)}", stroke=INK, w=2.5)
    tx, ty = -math.sin(t1), math.cos(t1)                    # clockwise tangent on screen
    px, py = -ty, tx
    f.path(f"M{n(x1 + tx * 12)},{n(y1 + ty * 12)} L{n(x1 + px * 6)},{n(y1 + py * 6)} L{n(x1 - px * 6)},{n(y1 - py * 6)} Z", fill=INK)
    f.tex(c1[0] - 20, c1[1] - R - 22, r"\omega", "middle")
    return f.svg()


def concept():
    """Mass distribution: a solid cylinder and a thin-walled tube of the same mass and radius, seen end-on."""
    f = Fig("fy10h-concept", 330, "Kaaviokuva: vasemmalla umpinainen tasa-aineinen sylinteri ja oikealla ohutseinäinen putki "
            "päästä katsottuna. Kummallakin on sama massa m ja sama säde r, ja pyörimisakseli kulkee keskipisteen kautta "
            "kohtisuoraan kuvan tasoa vastaan. Sylinterin massa on jakautunut koko poikkileikkaukselle, putken massa on "
            "lähes kokonaan etäisyydellä r akselista. Sylinterin hitausmomentti on puolet m r toiseen, putken likimain "
            "m r toiseen.")
    for cx, solid in ((160, True), (440, False)):
        cylinder_end(f, f"fy10hc-{cx}", cx, 125, 80, solid)
        f.line(cx, 125, cx + 80 * math.cos(math.radians(-35)), 125 + 80 * math.sin(math.radians(-35)), INK, 2)
        f.tex(cx + 26, 92, r"r", "start")
    f.tex(160, 235, r"\text{umpinainen sylinteri}", "middle", MUTED)
    f.tex(440, 235, r"\text{ohutseinäinen putki}", "middle", MUTED)
    f.tex(160, 285, r"I = \tfrac{1}{2}\, m r^2", "middle")
    f.tex(440, 285, r"I \approx m r^2", "middle")
    return f.svg()


def model():
    """The model graph: v squared against h, a line through the origin; sliding without friction (slope 2g) dashed for
    comparison and the rolling body solid (slope a < 2g). No measured points."""
    f = Fig("fy10h-model", 360, "Kuvaaja: nopeuden neliö v toiseen tason alapäässä korkeuden h funktiona mallin mukaan. "
            "Katkoviivalla on suora, jonka kulmakerroin on 2 g; se vastaisi kitkatta liukuvaa kappaletta. Yhtenäinen "
            "suora on vierivän kappaleen malli: suora origon kautta, jonka kulmakerroin a on pienempi kuin 2 g. "
            "Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 310), (470, 60), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"h", ylabel=r"v^2", grid=False)
    ax.line([(0, 0), (8.6, 9.5)], MUTED, 2, "6 5")
    ax.line([(0, 0), (9.6, 7.0)], INK)
    f.tex(ax.X(6.4), ax.Y(8.9), r"\text{kulmakerroin } 2g", "end", MUTED)
    f.tex(ax.X(9.7), ax.Y(3.4), r"\text{kulmakerroin } a", "end")
    return f.svg()


FIGURES = {"hero": hero, "concept": concept, "setup": setup, "model": model}
