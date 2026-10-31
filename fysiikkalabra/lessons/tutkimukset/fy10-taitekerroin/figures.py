"""Figures of the investigation Taitekertoimen määrittäminen (scripts/figlib.py); `python scripts/investigations.py figures
fy10-taitekerroin` writes them into investigation.md. Light rays are green (GOOD): no force, velocity or acceleration
appears in these figures, and red stays reserved for forces. The graph shows the model only, never invented measurements.
The schematic is drawn to scale for n = 1,5 (alpha = 25 degrees, beta from n sin alpha = sin beta)."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, ICE, ICE_EDGE, GOOD, GOOD_LIGHT, COLD, n
import herolib as H
from herolib import grad

RAY = GOOD


def scale_disc(f, cx, cy, r, minor=5, major=30, width=2):
    """A protractor disc: white face, rim, ticks every `minor` degrees, longer ones every `major` degrees, no numerals."""
    f.circle(cx, cy, r, WHITE, METAL_EDGE, 3)
    for d in range(0, 360, minor):
        a = math.radians(d); c, s = math.cos(a), math.sin(a)
        L = 22 if d % major == 0 else 14 if d % 10 == 0 else 8
        f.line(cx + c * (r - L), cy + s * (r - L), cx + c * (r - 2), cy + s * (r - 2), MUTED, width)


def half_disc(f, cx, cy, r, fill=ICE, edge=ICE_EDGE, w=3, opacity=0.55):
    """The half-cylinder seen from above: flat face vertical through (cx, cy), curved side to the left."""
    f.path(f"M{n(cx)},{n(cy - r)} A{n(r)},{n(r)} 0 0 0 {n(cx)},{n(cy + r)} Z", fill, edge, w, extra=f'fill-opacity="{opacity:g}"')


def laser_box(f, x_tip, y_tip, ux, uy, length=120, half=20):
    """A laser seen from above, its aperture at (x_tip, y_tip) and the beam leaving along (ux, uy)."""
    px, py = -uy, ux
    bx, by = x_tip - ux * length, y_tip - uy * length
    pts = [(x_tip + px * half, y_tip + py * half), (x_tip - px * half, y_tip - py * half),
           (bx - px * half, by - py * half), (bx + px * half, by + py * half)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", IRON, INK, 2.5)
    f.circle(x_tip - ux * 6, y_tip - uy * 6, 6, INK)


def hero():
    """The opening illustration: a lab bench seen from above, a protractor disc with a transparent half-cylinder on it, a
    laser whose beam runs along the zero line straight through the block's centre, a paper screen, a notebook and pencil."""
    f = H.hero("fy10t-hero", "Kuvitus: laboratorion työpöytä ylhäältä päin. Pöydällä on pyöreä kulma-asteikko, jonka päällä on "
               "puoliympyrän muotoinen läpinäkyvä kappale. Pöydän vasemmassa reunassa on laser, jonka säde kulkee asteikon "
               "nollasuuntaa pitkin kappaleen kaarevan pinnan läpi sen tasaisen pinnan keskipisteeseen ja siitä suoraan "
               "eteenpäin pieneen paperivarjostimeen. Oikealla on vihko ja lyijykynä.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10th-desk", SAND_LIGHT, SAND_DARK, horizontal=True))
    for k in range(9):
        y = 30 + 68 * k
        f.path(f"M0,{y} C300,{y + 14} 700,{y - 14} 1200,{y + 6}", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.45"')
    cx, cy, R = 560, 300, 230
    f.add(f'<circle cx="{cx + 8}" cy="{cy + 10}" r="{R}" fill="{INK}" fill-opacity="0.12"/>')     # shadow of the disc
    scale_disc(f, cx, cy, R)
    f.line(cx - R + 24, cy, cx + R - 24, cy, RULE, 2, "8 6")                                         # zero line
    f.line(cx, cy - R + 24, cx, cy + R - 24, RULE, 2, "8 6")
    half_disc(f, cx, cy, 150)
    # the beam: from the laser along the zero line, through the block's centre and on to the screen
    laser_box(f, 210, cy, 1, 0, 150, 24)
    f.add(f'<line x1="210" y1="{cy}" x2="955" y2="{cy}" stroke="{GOOD_LIGHT}" stroke-width="12" stroke-opacity="0.55"/>')
    f.line(210, cy, 955, cy, RAY, 4)
    f.rect(955, cy - 70, 16, 140, WHITE, INK, 2.5, rx=3)                                             # paper screen
    f.circle(955, cy, 10, GOOD_LIGHT); f.circle(955, cy, 5, RAY)
    # notebook and pencil
    f.add('<g transform="translate(1040,470) rotate(-8)">'
          f'<rect x="-90" y="-80" width="180" height="150" rx="5" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-56 + 18 * k}" x2="74" y2="{-56 + 18 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(7))
          + "</g>")
    f.add(f'<g transform="translate(1030,130) rotate(35)"><rect x="-80" y="-7" width="150" height="14" fill="{SAND}" stroke="{INK}" stroke-width="2"/>'
          f'<path d="M70,-7 L92,0 L70,7 Z" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="2"/><path d="M86,-2 L92,0 L86,2 Z" fill="{INK}"/></g>')
    return f.svg()


def ray(f, x1, y1, x2, y2, w=3.5, dash=None):
    """A light ray with an arrowhead at its middle."""
    f.line(x1, y1, x2, y2, RAY, w, dash)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.path(f"M{n(mx + ux * 9)},{n(my + uy * 9)} L{n(mx - ux * 9 - uy * 7)},{n(my - uy * 9 + ux * 7)} "
           f"L{n(mx - ux * 9 + uy * 7)},{n(my - uy * 9 - ux * 7)} Z", RAY)


def arc(f, cx, cy, r, a1, a2, color=INK):
    """An angle arc around (cx, cy) from screen angle a1 to a2 (degrees, measured clockwise from +x as SVG does)."""
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    sweep = 1 if a2 > a1 else 0
    f.path(f"M{n(p1[0])},{n(p1[1])} A{n(r)},{n(r)} 0 0 {sweep} {n(p2[0])},{n(p2[1])}", stroke=color, w=2)


def setup():
    """Top view of the measurement: the beam enters the curved side along a radius, refracts at the centre of the flat face;
    the normal, the angle of incidence alpha (in the block) and the angle of refraction beta (in air); a weak reflected ray."""
    f = Fig("fy10t-setup", 440, "Kaaviokuva ylhäältä päin. Puoliympyrän muotoisen kappaleen tasainen pinta on pystysuorassa kuvan "
            "keskellä, ja kaareva pinta on vasemmalla. Tasaisen pinnan keskipisteen kautta kulkee vaakasuora katkoviiva, pinnan "
            "normaali. Laserin säde tulee vasemmalta alhaalta kaarevan pinnan läpi säteen suuntaisesti tasaisen pinnan "
            "keskipisteeseen. Tulokulma alfa on kappaleen sisällä säteen ja normaalin välinen kulma. Ilmaan tullut säde jatkaa "
            "oikealle ylös, ja taitekulma beeta on sen ja normaalin välinen kulma. Osa valosta heijastuu tasaisesta pinnasta "
            "takaisin kappaleeseen ohuena katkoviivana. Kuva on piirretty mittakaavassa taitekertoimella 1,5.")
    cx, cy, R = 300, 220, 150
    al = 25; be = math.degrees(math.asin(1.5 * math.sin(math.radians(al))))
    scale_disc(f, cx, cy, 195, minor=10, major=30, width=1.5)
    half_disc(f, cx, cy, R, opacity=0.6)
    f.line(cx - 185, cy, cx + 185, cy, MUTED, 2, "7 5")                                    # the normal
    f.line(cx, cy - 185, cx, cy + 185, ICE_EDGE, 1.5)
    ua = (-math.cos(math.radians(al)), math.sin(math.radians(al)))                         # from the centre towards the laser
    # incident ray: from outside the disc, along a radius to the centre
    sx, sy = cx + ua[0] * 245, cy + ua[1] * 245
    laser_box(f, sx, sy, -ua[0], -ua[1], 60, 13)
    ray(f, sx, sy, cx + ua[0] * R, cy + ua[1] * R)
    ray(f, cx + ua[0] * R, cy + ua[1] * R, cx, cy)
    # refracted ray in air
    ub = (math.cos(math.radians(be)), -math.sin(math.radians(be)))
    ray(f, cx, cy, cx + ub[0] * 190, cy + ub[1] * 190)
    # weak reflected ray inside the block
    ur = (-math.cos(math.radians(al)), -math.sin(math.radians(al)))
    ray(f, cx, cy, cx + ur[0] * (R - 4), cy + ur[1] * (R - 4), w=2, dash="6 5")
    f.circle(cx, cy, 4.5, INK)
    # angles
    arc(f, cx, cy, 62, 180 - al, 180)
    f.tex(cx - 92, cy + 16, r"\alpha", "middle")
    arc(f, cx, cy, 62, -be, 0)
    f.tex(cx + 92, cy - 28, r"\beta", "middle")
    # labels
    f.tex(cx - 72, cy + 100, r"\text{kappale}", "middle", MUTED)
    f.tex(cx + 110, cy + 90, r"\text{ilma}", "middle", MUTED)
    f.tex(cx + 30, cy + 22, r"\text{normaali}", "start", MUTED, size=20)
    f.tex(sx - 20, sy + 42, r"\text{laser}", "middle", MUTED, size=20)
    return f.svg()


def model():
    """The linearised model: sin beta against sin alpha is a line through the origin with slope n, up to sin beta = 1."""
    f = Fig("fy10t-model", 340, "Kuvaaja: taitekulman sini tulokulman sinin funktiona taittumislain mallin mukaan, kun valo tulee "
            "aineesta ilmaan. Kuvaaja on origon kautta kulkeva suora, joka päättyy, kun taitekulman sini on yksi. Suoralle on "
            "merkitty kaksi pistettä ja niiden välinen muutos vaaka- ja pystysuunnassa. Kulmakerroin on taitekerroin n. "
            "Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (100, 290), (450, 50), x=(0, 1), y=(0, 1.1), xticks=[], yticks=[1], xlabel=r"\sin\alpha",
              ylabel=r"\sin\beta", grid=False)
    nn = 1.5
    ax.line([(0, 0), (1 / nn, 1)], INK)
    f.line(ax.X(0), ax.Y(1), ax.X(0.95), ax.Y(1), MUTED, 1.5, "6 5")
    a, b = (0.2, 0.3), (0.55, 0.825)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) + 20, r"\Delta(\sin\alpha)", "middle", MUTED, size=20)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta(\sin\beta)", "start", MUTED, size=20)
    f.tex(ax.X(0.86), ax.Y(0.22), r"n = \dfrac{\Delta(\sin\beta)}{\Delta(\sin\alpha)}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model}
