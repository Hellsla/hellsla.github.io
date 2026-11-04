"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-15` writes them into lesson.md.
FY7 light chapters (course brief): rays #e64980, normals dashed grey; the electric field #8a5f22 (as in FY6 and the
chapter *Sähkömagneettinen säteily ja mustan kappaleen spektri*); polariser film grey with lines along its
transmission axis. An oscillation perpendicular to the page is a dot, one in the page a short double arrow."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    GRAIN, HEAT_LIGHT, HEAT, COLD, COLD_LIGHT, IRON, GOOD, GOOD_LIGHT, PAPER, ALUMINIUM, n)
import herolib as H

RAY = "#e64980"          # light rays in FY7 (chapters 10–15)
EF = "#8a5f22"           # electric field
FILM = "#9aa0a6"         # polariser film


def ray(f, pts, w=3, opacity=1.0, arrow_at=None):
    """A light ray along the points; a small filled arrowhead in the middle of segment arrow_at shows its direction."""
    d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)
    op = f' stroke-opacity="{opacity:g}"' if opacity < 1 else ""
    f.add(f'<path d="{d}" fill="none" stroke="{RAY}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{op}/>')
    for k in ([arrow_at] if isinstance(arrow_at, int) else (arrow_at or [])):
        (x1, y1), (x2, y2) = pts[k], pts[k + 1]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        mx, my = (x1 + x2) / 2 + ux * 6, (y1 + y2) / 2 + uy * 6
        h, hw = 13, 6
        fo = f' fill-opacity="{opacity:g}"' if opacity < 1 else ""
        f.add(f'<path d="M{n(mx)},{n(my)} L{n(mx - ux * h - uy * hw)},{n(my - uy * h + ux * hw)} '
              f'L{n(mx - ux * h + uy * hw)},{n(my - uy * h - ux * hw)} Z" fill="{RAY}"{fo}/>')


def dbl(f, x, y, dx, dy, L, color=EF, w=2.5, head=9):
    """A double arrow through (x, y) along (dx, dy) with half-length L: an oscillation in that direction."""
    m = math.hypot(dx, dy); dx, dy = dx / m, dy / m
    f.line(x - dx * (L - head + 1), y - dy * (L - head + 1), x + dx * (L - head + 1), y + dy * (L - head + 1), color, w)
    for s in (1, -1):
        tx, ty = x + s * dx * L, y + s * dy * L
        bx, by = tx - s * dx * head, ty - s * dy * head
        hw = head * 0.5
        f.path(f"M{n(tx)},{n(ty)} L{n(bx - dy * hw)},{n(by + dx * hw)} L{n(bx + dy * hw)},{n(by - dx * hw)} Z", fill=color)


def dot(f, x, y, color=EF):
    """An oscillation perpendicular to the page."""
    f.circle(x, y, 5.5, color)


def normal(f, x1, y1, x2, y2):
    f.line(x1, y1, x2, y2, MUTED, 1.5, "6 5")


def arc(f, cx, cy, r, a1, a2, color=INK, w=1.5):
    """An angle arc around (cx, cy) from direction a1 to a2 (degrees, 0 = right, 90 = down, SVG y down)."""
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 1 if a2 > a1 else 0
    f.path(f"M{n(p1[0])},{n(p1[1])} A{r},{r} 0 {large},{sweep} {n(p2[0])},{n(p2[1])}", stroke=color, w=w)


SQ = 0.34                # oblique view: a disc across the beam is drawn 0,34 times as wide as it is tall


def disc(f, x, y, R, a, gid):
    """A polariser across a horizontal beam in oblique view: an ellipse of film with lines along its transmission axis
    (a degrees from the vertical) and the axis itself drawn darker."""
    f.defs_add(f'<clipPath id="{gid}"><ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(R * SQ - 1.5)}" ry="{n(R - 1.5)}"/></clipPath>')
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(R * SQ)}" ry="{n(R)}" fill="{FILM}" fill-opacity="0.45"/>')
    ux, uy = math.sin(math.radians(a)), math.cos(math.radians(a))
    vx, vy = uy, -ux
    f.add(f'<g clip-path="url(#{gid})">')
    for k in range(-6, 7):
        d = k * R / 7
        f.line(x + (d * vx - R * ux) * SQ, y - (d * vy - R * uy), x + (d * vx + R * ux) * SQ, y - (d * vy + R * uy), MUTED, 1.5)
    f.add("</g>")
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(R * SQ)}" ry="{n(R)}" fill="none" stroke="{INK}" stroke-width="2.5"/>')


def wave(f, xa, xb, y, A, a, L=46):
    """The electric field of polarised light along a horizontal beam in oblique view: a sine curve in the plane of the
    oscillation (a degrees from the vertical), with thin lines from the beam to the curve."""
    ux, uy = math.sin(math.radians(a)) * SQ, -math.cos(math.radians(a))
    pts, x = [], xa
    while x <= xb + 0.01:
        pts.append((x, math.sin(2 * math.pi * (x - xa) / L))); x += 2
    for j in range(0, len(pts), 3):
        x, v = pts[j]
        f.line(x, y, x + A * v * ux, y + A * v * uy, EF, 1.2)
    f.path("M" + " L".join(f"{n(x + A * v * ux)},{n(y + A * v * uy)}" for x, v in pts), stroke=EF, w=2.5)


def star(f, x, y, L):
    """Unpolarised light in oblique view: oscillations in many directions across the beam."""
    for a in (0, 45, 90, 135):
        dx, dy = math.sin(math.radians(a)) * SQ * 1.6, -math.cos(math.radians(a))
        dbl(f, x, y, dx, dy, L, w=2, head=7)


def lamp(f, x, y):
    f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="30" fill="{HEAT_LIGHT}" fill-opacity="0.45"/>')
    f.circle(x, y, 18, HEAT_LIGHT, INK, 2)
    f.rect(x - 10, y + 17, 20, 16, IRON, INK, 2, 3)


def view(f, x, y, r, dirs, L=24):
    """A view along the beam: a circle with the oscillation directions (degrees from the vertical) as double arrows."""
    f.circle(x, y, r, GLASS, INK, 2)
    for a in dirs:
        dbl(f, x, y, math.sin(math.radians(a)), -math.cos(math.radians(a)), L, w=2.5, head=8)


def polariser():
    f = Fig("fy715-polariser", 360, "Periaatekuva vinosti sivulta, ei mittakaavassa: vasemmalla lamppu, josta lähtee "
            "polarisoimatonta valoa oikealle. Valon sähkökenttä värähtelee kohtisuorassa etenemissuuntaa vastaan moneen "
            "eri suuntaan, mitä kuvaavat ruskeat kaksoisnuolet eri asennoissa. Valo kulkee polarisaattorikalvon läpi, "
            "jonka viivoitus ja tumma viiva näyttävät pystysuoran läpäisysuunnan. Kalvon jälkeen sähkökenttä "
            "värähtelee vain pystysuunnassa, mikä näkyy pystytasossa kulkevana ruskeana aaltona, ja intensiteetti on "
            "puolet alkuperäisestä. Alhaalla pienet ympyrät näyttävät värähtelysuunnat säteen suunnasta katsottuna: "
            "ennen kalvoa monta suuntaa, kalvon jälkeen vain pystysuunta.")
    yb = 140
    lamp(f, 46, yb)
    f.line(78, yb, 580, yb, RAY, 2.5)
    for x in (118, 178):
        star(f, x, yb, 34)
    disc(f, 262, yb, 78, 0, "fy715p-clip")
    wave(f, 300, 566, yb, 52, 0)
    f.path(f"M{n(580)},{n(yb)} L{n(567)},{n(yb - 6)} L{n(567)},{n(yb + 6)} Z", fill=RAY)
    f.tex(20, 36, r"\text{polarisoimaton valo}", "start")
    f.tex(580, 36, r"\text{polarisoitunut valo}", "end")
    f.tex(262, 244, r"\text{polarisaattori}", "middle")
    view(f, 120, 304, 30, (0, 45, 90, 135))
    f.tex(164, 304, r"I_0", "start")
    view(f, 430, 304, 30, (0,))
    f.tex(474, 304, r"\tfrac{1}{2} I_0", "start", w=70)
    return f.svg()


def sheets():
    f = Fig("fy715-sheets", 320, "Periaatekuva: kaksi paria pyöreitä polarisaattorikalvoja valopöydän päällä. Kalvojen "
            "viivoitus näyttää läpäisysuunnan. Vasemmalla kalvojen läpäisysuunnat ovat samat, kulma on 0 astetta, ja "
            "päällekkäinen osa on vain vähän tummempi kuin yksi kalvo. Oikealla toisen kalvon läpäisysuunta on "
            "pystysuora ja toisen vaakasuora, kulma on 90 astetta, ja päällekkäinen osa on lähes musta.")
    f.rect(14, 14, 572, 236, WHITE, RULE, 2, 10)
    f.line(300, 24, 300, 300, RULE, 1.5, "6 5")
    r = 74
    for (cx, a), gid in zip(((112, 0), (190, 0), (410, 0), (488, 90)), ("a", "b", "c", "d")):
        f.defs_add(f'<clipPath id="fy715s-{gid}"><circle cx="{cx}" cy="132" r="{r - 1.5}"/></clipPath>')
    for (cx, a), gid in zip(((112, 0), (190, 0), (410, 0), (488, 90)), ("a", "b", "c", "d")):
        f.add(f'<circle cx="{cx}" cy="132" r="{r}" fill="{FILM}" fill-opacity="0.42"/>')
    # the crossed pair's overlap: almost no light through
    f.add(f'<g clip-path="url(#fy715s-c)"><circle cx="488" cy="132" r="{r}" fill="{INK}" fill-opacity="0.88"/></g>')
    for (cx, a), gid in zip(((112, 0), (190, 0), (410, 0), (488, 90)), ("a", "b", "c", "d")):
        f.add(f'<g clip-path="url(#fy715s-{gid})">')
        for k in range(-8, 9):
            d = k * 9
            if a == 0: f.line(cx + d, 132 - r, cx + d, 132 + r, MUTED, 1.2)
            else: f.line(cx - r, 132 + d, cx + r, 132 + d, MUTED, 1.2)
        f.add("</g>")
        f.circle(cx, 132, r, "none", INK, 2.5)
    f.tex(151, 280, r"\theta = 0^\circ", "middle")
    f.tex(449, 280, r"\theta = 90^\circ", "middle")
    return f.svg()


def glare():
    f = Fig("fy715-glare", 360, "Periaatekuva sivulta, ei mittakaavassa: auringonvalo tulee vasemmalta ylhäältä "
            "järven pintaan. Tulevassa säteessä on sekä pisteitä, jotka tarkoittavat paperin tasoa vastaan kohtisuoraa "
            "eli vedenpinnan suuntaista värähtelyä, että paperin tasossa olevia kaksoisnuolia: valo on "
            "polarisoimatonta. Pinnasta heijastuneessa säteessä on enimmäkseen pisteitä: häikäisy on osittain "
            "polarisoitunut vaakasuunnassa. Heijastunut valo osuu oikealla polaroituihin aurinkolaseihin, joiden "
            "läpäisysuunta on pystysuora, joten lasien jälkeen jatkuu vain heikko säde silmään. Osa valosta taittuu "
            "veteen.")
    ys, hx = 236, 262
    f.rect(12, ys, 576, 336 - ys, H.grad(f, "fy715g-water", WATER_LIGHT, WATER))
    f.line(12, ys, 588, ys, INK, 2)
    H.sun(f, "fy715g", 62, 70, r=30, rays=False)
    a = math.radians(55)                                  # angle of incidence in the schematic picture
    x0, y0 = hx - 196 * math.sin(a), ys - 196 * math.cos(a)
    ray(f, [(x0, y0), (hx, ys)], arrow_at=0)
    L2 = 190
    x2, y2 = hx + L2 * math.sin(a), ys - L2 * math.cos(a)
    ray(f, [(hx, ys), (x2, y2)], arrow_at=0)
    b = math.asin(math.sin(a) / 1.33)
    ray(f, [(hx, ys), (hx + 86 * math.sin(b), ys + 86 * math.cos(b))], w=2.5, opacity=0.6)
    normal(f, hx, ys - 120, hx, ys + 40)
    # marks on the incoming ray: dots and double arrows perpendicular to the ray in the page
    ux, uy = math.sin(a), math.cos(a)                    # along the incoming ray (down-right)
    for k, t in enumerate((0.22, 0.4, 0.58, 0.76)):
        px, py = x0 + (hx - x0) * t, y0 + (ys - y0) * t
        if k % 2: dot(f, px, py)
        else: dbl(f, px, py, uy, -ux, 18, w=2, head=7)
    # the reflected ray: mostly dots
    for t in (0.2, 0.36, 0.52, 0.68):
        dot(f, hx + (x2 - hx) * t, ys + (y2 - ys) * t)
    rx, ry = hx + (x2 - hx) * 0.84, ys + (y2 - ys) * 0.84
    dbl(f, rx, ry, math.cos(a), math.sin(a), 9, w=1.8, head=5)
    # the sunglasses' lens across the reflected ray, its transmission axis in the page and vertical
    lx, ly = x2 + 18 * math.sin(a), y2 - 18 * math.cos(a)
    f.add(f'<g transform="rotate({n(math.degrees(a) - 90)} {n(lx)} {n(ly)})">')
    f.add(f'<ellipse cx="{n(lx)}" cy="{n(ly)}" rx="12" ry="52" fill="{FILM}" fill-opacity="0.55" stroke="{INK}" stroke-width="2.5"/>')
    for d in (-6, 0, 6):
        f.line(lx + d, ly - 44 + 2 * abs(d), lx + d, ly + 44 - 2 * abs(d), MUTED, 1.5)
    f.add("</g>")
    dx, dy = math.sin(a), -math.cos(a)
    ray(f, [(lx + 14 * dx, ly + 14 * dy), (lx + 56 * dx, ly + 56 * dy)], w=2, opacity=0.35)
    # the eye
    ex, ey = lx + 72 * dx, ly + 72 * dy
    f.path(f"M{n(ex - 22)},{n(ey)} Q{n(ex)},{n(ey - 16)} {n(ex + 22)},{n(ey)} Q{n(ex)},{n(ey + 16)} {n(ex - 22)},{n(ey)} Z", WHITE, INK, 2)
    f.circle(ex - 4, ey, 6, INK)
    f.tex(hx - 150, 196, r"\text{ilma}", "middle")
    f.tex(584, 306, r"\text{vesi}", "end", color=WHITE)
    f.tex(360, 206, r"\text{häikäisy}", "start")
    f.tex(584, 34, r"\text{polaroidut lasit}", "end")
    f.line(462, 50, 444, 82, MUTED, 1.5)
    return f.svg()


def components():
    f = Fig("fy715-components", 360, "Kaavakuva säteen suunnasta katsottuna: polarisoituneen valon sähkökentän "
            "amplitudi E0 osoittaa pystysuoraan ylöspäin, eli valo on polarisoitunut pystysuunnassa. Analysaattorin "
            "läpäisysuunta on kulmassa theeta pystysuunnasta. Sähkökentän läpäisysuuntainen komponentti E0 cos theeta "
            "pääsee läpi, ja sitä vastaan kohtisuora komponentti E0 sin theeta absorboituu. Kulma theeta on kuvassa "
            "35 astetta.")
    ox, oy, E = 240, 300, 220
    th = math.radians(35)
    ux, uy = math.sin(th), -math.cos(th)                 # analyser axis direction (up-right)
    f.line(ox, oy + 24, ox, oy - E - 30, MUTED, 1.5, "6 5")
    f.line(ox - ux * 30, oy - uy * 30, ox + ux * (E + 34), oy + uy * (E + 34), INK, 3)
    # E0 and its components
    tipx, tipy = ox, oy - E
    c = E * math.cos(th)
    px, py = ox + ux * c, oy + uy * c
    f.line(tipx, tipy, px, py, MUTED, 1.5, "5 4")
    f.arrow(ox, oy, tipx, tipy, EF, 3.5, 16)
    f.arrow(ox, oy, px, py, EF, 3.5, 16)
    perp = (-uy, ux)                                      # perpendicular to the axis (pointing up-left)
    s = E * math.sin(th)
    qx, qy = ox - perp[0] * s, oy - perp[1] * s
    f.line(ox, oy, qx + perp[0] * 14, qy + perp[1] * 14, EF, 2.5, "7 5")
    f.path(f"M{n(qx)},{n(qy)} L{n(qx + perp[0] * 14 - ux * 6)},{n(qy + perp[1] * 14 - uy * 6)} "
           f"L{n(qx + perp[0] * 14 + ux * 6)},{n(qy + perp[1] * 14 + uy * 6)} Z", fill=EF)
    arc(f, ox, oy, 64, -90, -90 + 35)
    f.circle(ox, oy, 4, INK)
    f.tex(262, 212, r"\theta", "start", w=30)
    f.tex(ox - 14, tipy + 8, r"E_0", "end", w=50)
    f.tex(px + 16, py + 22, r"E_0 \cos\theta", "start")
    f.tex(qx - 6, qy + 22, r"E_0 \sin\theta", "end")
    f.tex(ox + ux * (E + 34) + 8, oy + uy * (E + 34) - 4, r"\text{läpäisysuunta}", "start")
    f.tex(ox + 12, oy + 30, r"\text{polarisaatiosuunta}", "start")
    return f.svg()


def malus_graph():
    f = Fig("fy715-graph", 340, "Kuvaaja mittakaavassa: polarisoituneen valon intensiteetin osuus I per I0, joka "
            "pääsee polarisaattorin läpi, kulman theeta funktiona nollasta 180 asteeseen. Käyrä cos toiseen theeta "
            "alkaa arvosta 1, laskee ensin loivasti, on 45 asteessa 0,50 ja 90 asteessa nolla, ja nousee sitten "
            "symmetrisesti takaisin arvoon 1 kulmassa 180 astetta. Merkityt pisteet: 30 astetta 0,75; 45 astetta "
            "0,50; 60 astetta 0,25.")
    ax = Axes(f, (92, 290), (504, 60), x=(0, 180), y=(0, 1), xticks=[30 * k for k in range(1, 7)],
              yticks=[0.25 * k for k in range(1, 5)], xlabel=r"\theta\ (^\circ)", ylabel=r"I : I_0",
              yfmt=lambda v: fi(round(v, 2), 2))
    ax.curve(lambda t: math.cos(math.radians(t)) ** 2, 0, 180, RAY, 3)
    for t in (30, 45, 60):
        v = math.cos(math.radians(t)) ** 2
        ax.guide(t, v); ax.point(t, v, INK)
    return f.svg()


def brewster():
    f = Fig("fy715-brewster", 360, "Kaavakuva, kulmat mittakaavassa: valo tulee ilmasta vedenpintaan Brewsterin "
            "kulmassa alfa B = 53,1 astetta pinnan normaaliin nähden. Tulevassa säteessä on sekä pisteitä eli paperin "
            "tasoa vastaan kohtisuoraa värähtelyä että paperin tasossa olevia kaksoisnuolia. Heijastunut säde lähtee "
            "samassa kulmassa ja on täysin polarisoitunut: siinä on vain pisteitä, eli sähkökenttä värähtelee "
            "vedenpinnan suuntaisesti. Taittunut säde jatkaa veteen kulmassa alfa 2 = 36,9 astetta, ja siinä on "
            "enimmäkseen kaksoisnuolia. Heijastuneen ja taittuneen säteen välissä on suora kulma.")
    ys, hx = 172, 300
    aB = math.atan(1.33); a2 = math.pi / 2 - aB
    f.rect(12, ys, 576, 336 - ys, H.grad(f, "fy715b-water", WATER_LIGHT, WATER))
    f.line(12, ys, 588, ys, INK, 2)
    normal(f, hx, 30, hx, 330)
    L = 186
    x0, y0 = hx - L * math.sin(aB), ys - L * math.cos(aB)
    x1, y1 = hx + L * math.sin(aB), ys - L * math.cos(aB)
    x2, y2 = hx + 170 * math.sin(a2), ys + 170 * math.cos(a2)
    ray(f, [(x0, y0), (hx, ys)], arrow_at=0)
    ray(f, [(hx, ys), (x1, y1)], arrow_at=0)
    ray(f, [(hx, ys), (x2, y2)], arrow_at=0)
    ux, uy = math.sin(aB), math.cos(aB)
    for k, t in enumerate((0.18, 0.34, 0.66, 0.8)):
        px, py = x0 + (hx - x0) * t, y0 + (ys - y0) * t
        if k % 2: dot(f, px, py)
        else: dbl(f, px, py, uy, -ux, 17, w=2, head=7)
    for t in (0.3, 0.48, 0.66, 0.84):
        dot(f, hx + (x1 - hx) * t, ys + (y1 - ys) * t)
    vx, vy = math.sin(a2), math.cos(a2)
    for k, t in enumerate((0.36, 0.56, 0.78)):
        px, py = hx + (x2 - hx) * t, ys + (y2 - ys) * t
        if k == 1: dot(f, px, py)
        else: dbl(f, px, py, vy, -vx, 16, w=2, head=7)
    # angles: incidence and reflection from the normal (up), refraction from the normal (down)
    arc(f, hx, ys, 48, -90 - math.degrees(aB), -90)
    arc(f, hx, ys, 56, -90, -90 + math.degrees(aB))
    arc(f, hx, ys, 52, 90 - math.degrees(a2), 90)
    # the right angle between the reflected and the refracted ray
    r1 = (math.sin(aB), -math.cos(aB)); r2 = (math.sin(a2), math.cos(a2)); s = 20
    f.path(f"M{n(hx + r1[0] * s)},{n(ys + r1[1] * s)} L{n(hx + (r1[0] + r2[0]) * s)},{n(ys + (r1[1] + r2[1]) * s)} "
           f"L{n(hx + r2[0] * s)},{n(ys + r2[1] * s)}", stroke=INK, w=1.5)
    f.tex(hx - 38, ys - 82, r"\alpha_\text{B}", "end", w=50)
    f.tex(hx + 40, ys - 90, r"\alpha_\text{B}", "start", w=50)
    f.tex(hx + 12, ys + 82, r"\alpha_2", "start", w=40)
    f.tex(hx + 46, ys + 2 + 20, r"90^\circ", "start", w=50)
    f.tex(24, 140, r"\text{ilma},\ n_1 = 1{,}00", "start")
    f.tex(24, 316, r"\text{vesi},\ n_2 = 1{,}33", "start", color=WHITE)
    f.tex(584, 30, r"\text{täysin polarisoitunut}", "end")
    return f.svg()


FIT_TH = [0, 15, 30, 45, 60, 75, 90]
FIT_E = [374, 354, 283, 197, 102, 40, 15]          # light sensor readings, lx (lesson-answers.py fits them)


def fit():
    """Task figure (inquiry 'mittaus'): illuminance E against cos² θ with the line Graphical Analysis fitted."""
    X = [math.cos(math.radians(t)) ** 2 for t in FIT_TH]
    nn = len(X); mx = sum(X) / nn; my = sum(FIT_E) / nn
    b = sum((x - mx) * (y - my) for x, y in zip(X, FIT_E)) / sum((x - mx) ** 2 for x in X); a0 = my - b * mx
    f = Fig("fy715-fit", 360, "Kuvaaja mittakaavassa: puhelimen näytön valo polarisaattorikalvon läpi. Vaaka-akselilla "
            "on cos toiseen theeta, missä theeta on kalvon kiertokulma, nollasta yhteen, ruudukon väli 0,1. "
            "Pystyakselilla on valoanturin lukema E luksia nollasta 400:aan, ruudukon väli 25 luksia. Seitsemän "
            "mittauspistettä kulmilla 0, 15, 30, 45, 60, 75 ja 90 astetta: 374, 354, 283, 197, 102, 40 ja 15 luksia. "
            "Pisteisiin on sovitettu suora, joka nousee tasaisesti vasemmasta reunasta, jossa se on noin 15 luksin "
            "kohdalla, oikeaan reunaan, jossa se on noin 375 luksin kohdalla.")
    ax = Axes(f, (96, 300), (500, 52), x=(0, 1), y=(0, 400), xticks=[0.1 * k for k in range(1, 11)],
              yticks=[25 * k for k in range(1, 17)], xlabel=r"\cos^2\theta", ylabel=r"E\ (\text{lx})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 2 == 0 else "",
              yfmt=lambda v: fi(v) if v % 100 == 0 else "")
    ax.line([(0, a0), (1, a0 + b)], RAY, 3)
    for x, y in zip(X, FIT_E):
        ax.point(x, y, INK)
    return f.svg()


def hero():
    """The opening illustration: a sunny lake with bright glare, and polarised sunglasses in front: through the lenses
    the glare is gone and the stones on the bottom show."""
    f = H.hero("fy715-hero", "Kuvitus: aurinkoinen järvi, jonka pinnassa kimaltaa kirkas häikäisy. Taustalla on "
               "metsäinen ranta. Kuvan keskellä ovat aurinkolasit. Linssien läpi katsottuna häikäisy on poissa: "
               "vesi näyttää tummemmalta ja läpinäkyvältä, ja pohjan kivet ja kala näkyvät.")
    H.sky(f, "fy715h", 260)
    H.sun(f, "fy715h", 1010, 92, r=52)
    H.forest(f, 262, 70, 46, GOOD, seed=3)
    water = H.grad(f, "fy715h-lake", WATER_LIGHT, WATER, y1=260, y2=600)
    f.rect(0, 260, 1200, 340, water)

    def glare_marks(k0, x0, x1):
        for k in range(70):
            x = x0 + (x1 - x0) * H.rnd(k + k0, 5); y = 280 + 300 * H.rnd(k + k0 + 300, 5) ** 1.4
            w = 26 + 70 * H.rnd(k + k0 + 600, 5)
            f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(w)}" ry="4" fill="{WHITE}" fill-opacity="0.85"/>')
    glare_marks(0, 0, 1200)
    # the sunglasses: two lenses; inside them the lake without glare
    lenses = [(470, 360), (730, 360)]
    clip = "".join(f'<ellipse cx="{x}" cy="{y}" rx="118" ry="92"/>' for x, y in lenses)
    f.defs_add(f'<clipPath id="fy715h-lens">{clip}</clipPath>')
    deep = H.grad(f, "fy715h-deep", WATER, "#1d4f7c", y1=260, y2=600)
    f.add('<g clip-path="url(#fy715h-lens)">')
    f.rect(330, 260, 540, 200, deep)
    for k in range(26):
        x = 352 + 500 * H.rnd(k, 9); y = 380 + 70 * H.rnd(k + 40, 9); r = 9 + 15 * H.rnd(k + 80, 9)
        f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(r * 1.4)}" ry="{n(r)}" fill="{SAND if k % 3 else SAND_LIGHT}" stroke="{GRAIN}" stroke-width="2"/>')
    f.path("M660,330 Q690,312 724,330 Q690,348 660,330 Z M660,330 L642,318 L642,342 Z", HEAT, INK, 2)
    f.circle(710, 327, 3.5, INK)
    f.add('</g>')
    for x, y in lenses:
        f.add(f'<ellipse cx="{x}" cy="{y}" rx="118" ry="92" fill="{INK}" fill-opacity="0.12" stroke="{INK}" stroke-width="10"/>')
    f.path("M588,344 Q600,326 612,344", stroke=INK, w=10)
    f.path("M352,340 L250,316", stroke=INK, w=10, extra='stroke-linecap="round"')
    f.path("M848,340 L950,316", stroke=INK, w=10, extra='stroke-linecap="round"')
    return f.svg()


def scene():
    """A second everyday scene: a phone screen with a polariser film laid over part of it: the covered part is dark."""
    f = H.scene("fy715-scene", "Kuvitus: pöydällä on puhelin, jonka näyttö loistaa kirkkaana. Näytön päälle on "
                "asetettu vinosti neliön muotoinen harmaa polarisaattorikalvo. Kalvon alle jäävä osa näytöstä näyttää "
                "lähes mustalta, ja kalvon kulma, joka on näytön ulkopuolella, näyttää vain vähän harmaalta.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 250, 600, 110, H.grad(f, "fy715s-table", SAND_LIGHT, SAND))
    f.line(0, 250, 600, 250, INK, 2.5)
    # the phone lying at a slant on the table
    f.add('<g transform="rotate(-8 300 200)">')
    f.rect(200, 40, 200, 300, INK, INK, 3, 26)
    f.rect(214, 64, 172, 252, H.grad(f, "fy715s-screen", COLD_LIGHT, WHITE), None, 0, 8)
    for k in range(5):
        f.rect(232, 88 + 42 * k, 136, 22, COLD, None, 0, 5, 'fill-opacity="0.35"')
    f.add('</g>')
    # the polariser film over the lower right part, crossed with the screen's polarisation
    f.defs_add('<clipPath id="fy715s-film"><path d="M300,170 L470,140 L500,320 L330,350 Z"/></clipPath>')
    f.path("M300,170 L470,140 L500,320 L330,350 Z", FILM, INK, 2, 'fill-opacity="0.35"')
    f.add('<g clip-path="url(#fy715s-film)"><g transform="rotate(-8 300 200)">'
          f'<rect x="214" y="64" width="172" height="252" rx="8" fill="{INK}" fill-opacity="0.9"/></g></g>')
    return f.svg()


FIGURES = {"hero": hero, "polariser": polariser, "sheets": sheets, "glare": glare, "components": components,
           "graph": malus_graph, "brewster": brewster, "scene": scene, "fit": fit}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "polariser": "reveals: a polariser passes half of unpolarised light, polarised along its transmission axis",
    "sheets": "reveals: crossed polarisers (90°) let almost no light through, parallel ones most of it",
    "glare": "reveals: glare from water is partly polarised parallel to the surface and polarised sunglasses block it",
    "components": "reveals: the component E0 cos θ along the analyser axis passes (Malus's law)",
    "graph": "reveals: I/I0 = cos² θ, 0,75 at 30°, 0,50 at 45°, 0,25 at 60°, 0 at 90°",
    "brewster": "reveals: at the Brewster angle (water 53,1°) the reflected light is fully polarised and the reflected and refracted rays are perpendicular",
    "fit": "safe: example data E (lx) against cos² θ for a phone screen through a polariser, with a fitted line, no slope written",
}
