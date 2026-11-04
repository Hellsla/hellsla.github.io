"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-6` writes them into lesson.md.
Force red, velocity blue, acceleration orange (FY4/FY5). The orbits of the cannon figure are integrated with the same
velocity Verlet step as the simulation, so the drawn paths are the computed ones."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, COLD_LIGHT, GLASS,
                    WATER, WATER_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ALUMINIUM, METAL_EDGE, IRON, ICE, GOOD, n)
from fbd import FBD, FORCE, VELOCITY, ACCEL, open_head
import herolib as H

GM = 6.674e-11 * 5.97e24          # γM of the Earth, m³/s²


def vec(f, x1, y1, x2, y2, col):
    """A velocity or acceleration arrow: thin, open head (fbd.py style), never a force."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.line(x1, y1, x2 - ux * 2, y2 - uy * 2, col, 2.5)
    open_head(f, x2, y2, ux, uy, col, 2.5)


def satellite(f, x, y, s=1.0):
    """A small satellite: a box with two solar panels."""
    f.rect(x - 34 * s, y - 7 * s, 22 * s, 14 * s, COLD_LIGHT, COLD, 1.5, 2)
    f.rect(x + 12 * s, y - 7 * s, 22 * s, 14 * s, COLD_LIGHT, COLD, 1.5, 2)
    f.line(x - 12 * s, y, x + 12 * s, y, INK, 2)
    f.rect(x - 9 * s, y - 9 * s, 18 * s, 18 * s, ALUMINIUM, INK, 2, 3)


def earth_disc(f, pre, cx, cy, r):
    f.defs_add(f'<radialGradient id="{pre}-earth" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></radialGradient>')
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r * 1.06)}" fill="{ICE}" fill-opacity="0.45"/>')
    f.circle(cx, cy, r, f"url(#{pre}-earth)", INK, 2)
    f.add(f'<ellipse cx="{n(cx - r * 0.3)}" cy="{n(cy - r * 0.2)}" rx="{n(r * 0.32)}" ry="{n(r * 0.22)}" fill="{SAND_DARK}"/>')
    f.add(f'<ellipse cx="{n(cx + r * 0.3)}" cy="{n(cy + r * 0.32)}" rx="{n(r * 0.2)}" ry="{n(r * 0.26)}" fill="{SAND_DARK}"/>')


def orbit():
    """Ydinajatus: gravity is the only force on the satellite, so it is the net force; it points to the Earth's centre
    and gives the normal acceleration that bends the path into a circle."""
    f = Fig("fy56-orbit", 360, "Kaavakuva, ei mittakaavassa: satelliitti kiertää Maata ympyrärataa, joka on piirretty "
            "katkoviivalla. Satelliitti on radan ylimmässä kohdassa. Sininen nopeusnuoli v osoittaa radan tangentin suuntaan "
            "oikealle. Punainen gravitaatiovoiman nuoli F osoittaa kohti Maan keskipistettä, ja sen vieressä oranssi "
            "normaalikiihtyvyyden nuoli a n osoittaa samaan suuntaan. Ohut katkoviiva jatkaa suoraan oikealle: sitä pitkin "
            "satelliitti liikkuisi ilman gravitaatiota.")
    cx, cy, R = 200, 214, 128
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="7 6"/>')
    earth_disc(f, "fy56o", cx, cy, 52)
    f.tex(cx, cy + 26, r"\text{Maa}", "middle")
    f.circle(cx, cy, 3.5, INK)
    sy = cy - R
    f.line(cx + 50, sy, 572, sy, MUTED, 1.5, "4 6")
    f.tex(572, sy - 24, r"\text{ilman gravitaatiota}", "end", MUTED)
    satellite(f, cx, sy)
    vec(f, cx + 40, sy + 22, cx + 150, sy + 22, VELOCITY)
    f.tex(cx + 166, sy + 44, r"\overline{v}", "middle", VELOCITY)
    f.arrow(cx, sy + 14, cx, sy + 76, FORCE, 4, 18)
    f.tex(cx + 24, sy + 64, r"\overline{F}", "middle", FORCE)
    vec(f, cx - 26, sy + 18, cx - 26, sy + 66, ACCEL)
    f.tex(cx - 52, sy + 56, r"\overline{a}_\text{n}", "middle", ACCEL)
    f.tex(cx + 78, cy - 66, "r", "middle")
    f.line(cx, cy, cx + R * math.cos(math.radians(-50)), cy + R * math.sin(math.radians(-50)), INK, 1.5, "4 4")
    f.line(398, 128, 398, 340, RULE, 2, "6 6")
    f.tex(412, 156, r"\text{ainoa voima}", "start")
    f.tex(412, 192, r"\overline{F}", "start", FORCE)
    f.tex(412, 228, r"\text{kohti Maan}", "start")
    f.tex(412, 262, r"\text{keskipistettä}", "start")
    f.tex(412, 312, r"\overline{F} = m\,\overline{a}_\text{n}", "start", w=150)
    return f.svg()


def path(k, r0, steps=6000):
    """The path of a satellite launched horizontally at radius r0 (m) with k times the circular speed: velocity Verlet
    as in the simulation, until it hits a sphere of radius 0.62 r0 (the drawn Earth) or completes one revolution."""
    mu = GM; v = k * math.sqrt(mu / r0)
    eps = v * v / 2 - mu / r0; a = -mu / (2 * eps); T = 2 * math.pi * math.sqrt(a ** 3 / mu)
    x, y, vx, vy = 0.0, r0, v, 0.0
    def acc(x, y):
        r2 = x * x + y * y; q = -mu / (r2 * math.sqrt(r2)); return q * x, q * y
    ax, ay = acc(x, y); pts = [(x, y)]; ang, sw = math.pi / 2, 0.0
    h = T / steps
    for _ in range(steps + 10):
        vx += 0.5 * h * ax; vy += 0.5 * h * ay; x += h * vx; y += h * vy
        ax, ay = acc(x, y); vx += 0.5 * h * ax; vy += 0.5 * h * ay
        pts.append((x, y))
        if math.hypot(x, y) <= 0.62 * r0: break
        a2 = math.atan2(y, x); d = (a2 - ang + math.pi) % (2 * math.pi) - math.pi; sw += abs(d); ang = a2
        if sw >= 2 * math.pi: break
    return pts


def cannon():
    """Newton's cannon: launched horizontally from the same point with three speeds."""
    f = Fig("fy56-cannon", 380, "Kaavakuva, ei mittakaavassa: kappale lähtee vaakasuoraan samasta pisteestä Maan "
            "yläpuolelta kolmella nopeudella. Radat on laskettu gravitaatiolaista. Liian pienellä nopeudella rata kaartuu "
            "jyrkemmin kuin ympyrä ja osuu Maahan. Ympyräradan nopeudella kappale kiertää lähtöpisteen etäisyydellä "
            "pysyvää ympyrää. Suuremmalla nopeudella rata kaartuu loivemmin, ja kappale loittonee kauemmas ja palaa "
            "lähtöpisteeseen.")
    cx, cy, R0 = 236, 186, 116           # the Earth's centre and the launch radius in the figure
    r0 = 1.0e7; sc = R0 / r0
    earth_disc(f, "fy56c", cx, cy, 0.62 * R0)
    f.tex(cx, cy, r"\text{Maa}", "middle")
    styles = ((0.82, MUTED, "8 6"), (1.0, INK, None), (1.07, GOOD, "2 5"))
    for k, col, dash in styles:
        pts = path(k, r0)
        d = " ".join(f"{n(cx + x * sc)},{n(cy - y * sc)}" for x, y in pts[::10] + [pts[-1]])
        f.add(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
              + (f' stroke-dasharray="{dash}"' if dash else "") + "/>")
    sy = cy - R0
    f.circle(cx, sy, 7, INK)
    vec(f, cx + 12, sy - 18, cx + 88, sy - 18, VELOCITY)
    f.tex(cx + 104, sy - 34, r"\overline{v}", "middle", VELOCITY)
    for k, (lab, col, dash) in enumerate(((r"\text{liian hidas}", MUTED, "8 6"), (r"\text{ympyrärata}", INK, None), (r"\text{liian nopea}", GOOD, "2 5"))):
        y = 150 + 44 * k
        f.line(408, y, 436, y, col, 3, dash, cap="round")
        f.tex(444, y, lab, "start", col)
    return f.svg()


def vr_graph():
    """Kaava: v = sqrt(γM/r) against r, with the real ISS, GPS and geostationary orbits (data of the inquiry table)."""
    f = Fig("fy56-vr", 360, "Kuvaaja mittakaavassa: ympyräradan ratanopeus v kilometreinä sekunnissa etäisyyden r funktiona, "
            "kun r on Maan keskipisteestä mitattu etäisyys tuhansina kilometreinä. Käyrä alkaa Maan pinnalta, r on 6 371 km ja v "
            "noin 7,9 km/s, ja laskee loivenevasti: kaukana kiertävä satelliitti liikkuu hitaammin. Käyrälle on merkitty "
            "pisteinä ISS (r 6 790 km, v 7,65 km/s), GPS-satelliitti (r 26 560 km, v 3,87 km/s) ja geostationaarinen "
            "satelliitti (r 42 164 km, v 3,07 km/s), jotka on laskettu todellisista kiertoajoista.")
    ax = Axes(f, (90, 300), (420, 60), x=(0, 45), y=(0, 9), xticks=[5, 10, 15, 20, 25, 30, 35, 40, 45],
              yticks=[1, 2, 3, 4, 5, 6, 7, 8, 9], xlabel=r"r\ (1000\,\text{km})", ylabel=r"v\ (\text{km/s})",
              xfmt=lambda v: fi(v) if v % 10 == 0 else "", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.curve(lambda r: math.sqrt(GM / (r * 1e6)) / 1e3, 6.371, 45, COLD, 3)
    pts = [(6.79, 2 * math.pi * 6.79e6 / (92.9 * 60) / 1e3, r"\text{ISS}", (16, -22)),
           (26.56, 2 * math.pi * 26.56e6 / (718 * 60) / 1e3, r"\text{GPS}", (0, -30)),
           (42.164, 2 * math.pi * 42.164e6 / 86164 / 1e3, r"\text{geostationaarinen}", (24, 30))]
    for r, v, name, (dx, dy) in pts:
        ax.point(r, v, COLD)
        f.tex(ax.X(r) + dx, ax.Y(v) + dy, name, "end" if dx > 20 else "start" if dx else "middle", bg=True)
    f.tex(ax.X(30), ax.Y(6.6), r"v = \sqrt{\dfrac{\gamma M}{r}}", "middle", COLD, w=150)
    return f.svg()


def weightless():
    """Painottomuus: the same astronaut standing on a scale on the Earth and floating in the ISS. Force diagrams to one
    scale (0,13 units per newton): on the ground F and N cancel; in orbit only F = m g_h acts and gives a = g_h."""
    f = Fig("fy56-paino", 380, "Kaksi voimakuviota samassa mittakaavassa. Vasemmalla astronautti seisoo vaa'alla Maan "
            "pinnalla, ja hänet on piirretty suorakulmiona: gravitaatiovoima F (paino) osoittaa keskipisteestä alas ja vaa'an tukivoima N "
            "alapinnasta ylös, yhtä pitkinä, joten kiihtyvyys on nolla. Oikealla sama astronautti avaruusasemalla: "
            "ainoa voima on noin 12 prosenttia lyhyempi gravitaatiovoima F, tukivoimaa ei ole, ja oranssi kiihtyvyysnuoli a osoittaa "
            "alas kohti Maata kappaleen vieressä. Asema putoaa samalla kiihtyvyydellä, joten lattia ei paina astronauttia.")
    m, g0, gh = 70.0, 9.81, GM / (6.371e6 + 420e3) ** 2
    s = 0.13
    f.tex(150, 26, r"\text{Maan pinnalla}", "middle")
    f.tex(450, 26, r"\text{avaruusasemalla}", "middle")
    f.line(300, 14, 300, 366, RULE, 2, "6 6")
    # left: on the ground, at rest on the scale
    cx, cy, w, h = 150, 186, 56, 96
    bot = cy + h / 2
    f.rect(cx - 62, bot, 124, 14, ALUMINIUM, INK, 2, 3)
    d = FBD(f, s, body=(cx, cy, w, h), m=m, a=(0, 0))
    d.force("F", (0, -m * g0), (cx, cy), kind="gravity", lab=(-22, 6))
    d.force("N", (0, m * g0), (cx + 18, bot), kind="normal", surface=0, lab=(24, 10))
    d.draw()
    f.tex(cx, 356, r"\overline{a} = \overline{0}", "middle")
    # right: in orbit, only the weight
    cx = 450
    d = FBD(f, s, body=(cx, cy, w, h), m=m, a=(0, -gh))
    d.force("F", (0, -m * gh), (cx, cy), kind="gravity", lab=(-22, 6))
    d.draw()
    d.motion(r"\overline{a}", (0, -1), (cx + 56, cy - 30), length=70, lab=(22, -8))
    f.tex(cx, 356, r"N = 0", "middle")
    return f.svg()


def orbits():
    """Milloin malli pätee: the Earth's orbit round the Sun (nearly a circle) and Halley's comet (very elongated),
    each to its own scale, the Sun at a focus."""
    f = Fig("fy56-radat", 360, "Kaksi rataa, kumpikin omassa mittakaavassaan, Aurinko radan polttopisteessä. Vasemmalla Maan "
            "rata: pienin etäisyys Auringosta 147,1 miljoonaa kilometriä ja suurin 152,1 miljoonaa kilometriä. Rata on "
            "piirretty yhtenäisellä viivalla ja sen päälle katkoviivalla ympyrä, eikä niitä erota toisistaan. Oikealla "
            "Halleyn komeetan rata: pienin etäisyys 88 miljoonaa kilometriä ja suurin noin 5 250 miljoonaa kilometriä, "
            "erittäin pitkänomainen ellipsi.")
    f.tex(150, 26, r"\text{Maan rata}", "middle")
    f.tex(450, 26, r"\text{Halleyn komeetan rata}", "middle")
    f.line(300, 14, 300, 346, RULE, 2, "6 6")
    # Earth: r_min 147,1 and r_max 152,1 million km; the ellipse's half axes and the Sun's offset to scale
    rp, ra = 147.1, 152.1; a = (rp + ra) / 2; c = a - rp; b = math.sqrt(rp * ra); k = 112 / a
    ex, ey = 150, 182
    f.add(f'<ellipse cx="{n(ex)}" cy="{n(ey)}" rx="{n(a * k)}" ry="{n(b * k)}" fill="none" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<circle cx="{n(ex)}" cy="{n(ey)}" r="{n(a * k)}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="5 7"/>')
    H.sun(f, "fy56r", ex + c * k, ey, r=14, rays=False)
    f.circle(ex - a * k, ey, 7, WATER, INK, 1.5)
    f.tex(ex - a * k + 14, ey - 26, r"\text{Maa}", "start")
    f.tex(ex, 324, r"147{,}1\text{–}152{,}1\ \text{milj. km}", "middle", w=272)
    # Halley: r_min 88 and r_max about 5250 million km
    rp, ra = 88.0, 5250.0; a = (rp + ra) / 2; c = a - rp; b = math.sqrt(rp * ra); k = 128 / a
    hx, hy = 450, 182
    f.add(f'<ellipse cx="{n(hx)}" cy="{n(hy)}" rx="{n(a * k)}" ry="{n(b * k)}" fill="none" stroke="{INK}" stroke-width="3"/>')
    H.sun(f, "fy56h", hx + c * k, hy, r=8, rays=False)
    f.circle(hx - a * k, hy, 6, ICE, INK, 1.5)
    f.tex(hx - a * k + 6, hy - 44, r"\text{komeetta}", "start")
    f.tex(hx + c * k + 4, hy + 40, r"\text{Aurinko}", "end")
    f.tex(hx, 324, r"88\text{–}5250\ \text{milj. km}", "middle", w=250)
    return f.svg()


def model_fbd():
    """The model answer of the drawing task: a satellite at the top of its circular orbit, only the gravitational force."""
    f = Fig("fy56-malli", 344, "Mallivoimakuvio: satelliitti radan ylimmässä kohdassa suorakulmiona. Ainoa voima on Maan "
            "gravitaatiovoima F, joka lähtee suorakulmion keskipisteestä alas kohti Maan keskipistettä. Kappaleen vieressä "
            "ohut sininen nopeusnuoli v osoittaa vaakasuoraan radan tangentin suuntaan ja oranssi kiihtyvyysnuoli a n alas "
            "kohti Maan keskipistettä. Kuvan alareunassa nuoli osoittaa Maan keskipisteen suunnan.")
    cx, cy, w, h = 270, 120, 90, 54
    d = FBD(f, 0.11, body=(cx, cy, w, h), a_dir=(0, -1))
    d.force("F", (0, -1200), (cx, cy), kind="gravity", lab=(-24, 4))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (cx + 60, cy - 6), length=96, lab=(18, -20))
    d.motion(r"\overline{a}_\text{n}", (0, -1), (cx + 80, cy + 28), length=80, lab=(30, -6))
    f.arrow(110, 292, 110, 330, MUTED, 2, 10)
    f.tex(124, 312, r"\text{kohti Maan keskipistettä}", "start", MUTED)
    return f.svg()


def _hull(pts):
    """The convex hull of screen points (monotone chain), counterclockwise."""
    pts = sorted(set((round(x, 2), round(y, 2)) for x, y in pts))
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0: h.pop()
            h.append(p)
        return h
    lo, hi = half(pts), half(pts[::-1])
    return lo[:-1] + hi[:-1]


def _poly(pts):
    return "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z"


def _blob(cx, cy, rx, ry, seed, k=26, rough=0.35):
    """An irregular closed outline (a coastline or a cloud bank) around (cx, cy), flattened to ry/rx."""
    pts = []
    for i in range(k):
        a = 2 * math.pi * i / k
        r = 1 + rough * (H.rnd(i, seed) - 0.5) + 0.5 * rough * math.sin(3 * a + seed)
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    d = f"M{n((pts[-1][0] + pts[0][0]) / 2)},{n((pts[-1][1] + pts[0][1]) / 2)}"
    for i, p in enumerate(pts):
        q = pts[(i + 1) % k]
        d += f" Q{n(p[0])},{n(p[1])} {n((p[0] + q[0]) / 2)},{n((p[1] + q[1]) / 2)}"
    return d + " Z"


def hero():
    """The chapter's opening illustration: the ISS in an oblique view above the Earth's limb, drawn from its real layout
    (a 110 m truss, four pairs of solar wings, radiators, the module chain across the truss) in one projection."""
    f = H.hero("fy56-hero", "Kuvitus: Kansainvälinen avaruusasema ISS kiertää Maata mustaa avaruutta vasten. Aseman poikki kulkee pitkä "
               "ristikkorunko, jonka kummassakin päässä on kaksi paria suuria kullanruskeita aurinkopaneelisiipiä. Rungon keskeltä "
               "lähtee sen poikki lieriön muotoisten asuinmoduulien ketju, ja rungosta riippuu valkoisia jäähdytyspaneeleita. "
               "Alhaalla näkyy Maan kaareutuva reuna: sinistä merta, vihreää ja ruskeaa maata, valkoisia pilviä ja ohut sininen ilmakehä.")
    H.space(f, seed=6, count=80)
    # the Earth's limb: ocean, land, clouds, the haze near the edge and the thin blue atmosphere
    ex, ey, er = 600, 2160, 1690
    f.add(f'<circle cx="{ex}" cy="{ey}" r="{er + 26}" fill="{COLD_LIGHT}" fill-opacity="0.18"/>')
    f.add(f'<circle cx="{ex}" cy="{ey}" r="{er + 11}" fill="{ICE}" fill-opacity="0.45"/>')
    f.defs_add(f'<radialGradient id="fy56h-sea" gradientUnits="userSpaceOnUse" cx="{ex}" cy="{ey}" r="{er}"><stop offset="0.9" stop-color="{WATER}"/>'
               f'<stop offset="0.975" stop-color="{COLD}"/><stop offset="1" stop-color="{WATER_LIGHT}"/></radialGradient>')
    f.defs_add(f'<clipPath id="fy56h-clip"><circle cx="{ex}" cy="{ey}" r="{er}"/></clipPath>')
    f.circle(ex, ey, er, "url(#fy56h-sea)")
    f.add('<g clip-path="url(#fy56h-clip)">')
    for cx, cy, rx, ry, sd in ((210, 560, 250, 52, 3), (930, 530, 300, 44, 7), (640, 610, 170, 30, 11)):   # land, foreshortened
        f.path(_blob(cx, cy, rx, ry, sd), GOOD)
        f.path(_blob(cx - rx * 0.2, cy, rx * 0.45, ry * 0.4, sd + 20, rough=0.6), INK, extra='fill-opacity="0.16"')      # darker forest
        f.path(_blob(cx + rx * 0.35, cy + ry * 0.1, rx * 0.22, ry * 0.3, sd + 30, rough=0.6), GRAIN, extra='fill-opacity="0.4"')   # a dry plain
    for k in range(48):                                               # cloud banks in streets along the limb
        cx = 1200 * H.rnd(k, 21); cy = 478 + 120 * H.rnd(k, 22) ** 1.4
        sc = 0.4 + (cy - 470) / 130
        f.path(_blob(cx, cy, 70 * sc * (0.6 + H.rnd(k, 23)), 8 * sc * (0.7 + H.rnd(k, 24)), k + 40, k=16, rough=0.6), WHITE,
               extra=f'fill-opacity="{0.55 + 0.35 * H.rnd(k, 25):.2f}"')
    f.defs_add(f'<radialGradient id="fy56h-haze" gradientUnits="userSpaceOnUse" cx="{ex}" cy="{ey}" r="{er}"><stop offset="0.955" stop-color="{WHITE}" stop-opacity="0"/>'
               f'<stop offset="1" stop-color="{ICE}" stop-opacity="0.8"/></radialGradient>')
    f.circle(ex, ey, er, "url(#fy56h-haze)")
    f.add("</g>")
    f.add(f'<circle cx="{ex}" cy="{ey}" r="{er + 2}" fill="none" stroke="{GLASS}" stroke-width="3" stroke-opacity="0.9"/>')

    # the station, in metres: X along the truss, Y along the module chain (towards the viewer), Z away from the Earth
    O, k = (600, 236), 6.6
    def P(x, y, z): return (O[0] + k * (x - 0.42 * y), O[1] + k * (-0.1 * x + 0.32 * y - 0.95 * z))
    def quad(a, b, c, d, fill, stroke=INK, w=2): f.path(_poly([P(*a), P(*b), P(*c), P(*d)]), fill, stroke, w)
    def cyl(c0, c1, r, axis, fill, cap=True):
        """A cylinder from c0 to c1 along the axis 'x' or 'y'; the near end cap drawn when cap."""
        ring = lambda c: [P(*((c[0], c[1] + r * math.cos(t), c[2] + r * math.sin(t)) if axis == "x" else (c[0] + r * math.cos(t), c[1], c[2] + r * math.sin(t))))
                          for t in (i * math.pi / 24 for i in range(48))]
        f.path(_poly(_hull(ring(c0) + ring(c1))), fill, INK, 2)
        if cap: f.path(_poly(ring(c1)), ALUMINIUM, INK, 1.5)
    steel = H.steel(f, "fy56h-mod", vertical=True)
    gold = H.grad(f, "fy56h-wing", SAND_DARK, COPPER)
    def wing(x0, up, phi):
        """One solar wing on the truss at X = x0: two blankets either side of a mast, 34 m long, tilted by phi."""
        s, c = math.sin(phi), math.cos(phi)
        sg = 1 if up else -1
        y0, z0 = sg * 3 * s, sg * 3 * c
        y1, z1 = sg * 37 * s, sg * 37 * c
        for a, b in ((x0 - 5.8, x0 - 0.5), (x0 + 0.5, x0 + 5.8)):
            quad((a, y0, z0), (b, y0, z0), (b, y1, z1), (a, y1, z1), gold, INK, 2)
            for j in range(1, 9):
                t = j / 9
                p, q = P(a, y0 + (y1 - y0) * t, z0 + (z1 - z0) * t), P(b, y0 + (y1 - y0) * t, z0 + (z1 - z0) * t)
                f.line(p[0], p[1], q[0], q[1], GRAIN, 1.5)
            m0, m1 = P((a + b) / 2, y0, z0), P((a + b) / 2, y1, z1)
            f.line(m0[0], m0[1], m1[0], m1[1], GRAIN, 1)
        p, q = P(x0, 0, 0), P(x0, y1, z1)
        f.line(p[0], p[1], q[0], q[1], INK, 2.5)
    wings = [(-47, 0.5), (-34, 0.5), (34, 0.5), (47, 0.5)]
    # behind the truss: the Russian segment (Zvezda with its own small wings, Zarya) and the lower solar wings
    cyl((0, -36, -4), (0, -27, -4), 1.6, "y", ALUMINIUM, cap=False)                                 # a Progress ship at the back
    for sg in (-1, 1):
        quad((sg * 3, -22, -4), (sg * 14, -22, -4), (sg * 14, -19, -4), (sg * 3, -22 + 3, -4), COLD, INK, 1.5)
    cyl((0, -27, -4), (0, -13, -4), 2.1, "y", steel, cap=False)                                    # Zvezda
    cyl((0, -13, -4), (0, 0, -4), 2.1, "y", steel, cap=False)                                      # Zarya
    for x0, phi in wings: wing(x0, False, phi)
    # the radiators hanging below the truss, near its middle
    for sg in (-1, 1):
        for j in range(3):
            a = sg * (12 + 3.6 * j); b = a + sg * 3.2
            quad((a, -1, -3), (b, -1, -3), (b, -8, -24), (a, -8, -24), WHITE, INK, 1.5)
            for t in (0.25, 0.5, 0.75):
                p, q = P(a, -1 - 7 * t, -3 - 21 * t), P(b, -1 - 7 * t, -3 - 21 * t)
                f.line(p[0], p[1], q[0], q[1], RULE, 1.5)
    # the truss: top and front faces with its lattice, rotary joints between the wing pairs
    L, h = 55, 2.4
    quad((-L, -h, h), (L, -h, h), (L, h, h), (-L, h, h), ALUMINIUM, INK, 2)
    quad((-L, h, h), (L, h, h), (L, h, -h), (-L, h, -h), METAL_EDGE, INK, 2)
    for j in range(44):
        x = -L + j * 2.5
        p, q = P(x, h, h), P(x + 2.5, h, -h); f.line(p[0], p[1], q[0], q[1], IRON, 1.5)
        p, q = P(x, h, -h), P(x, h, h); f.line(p[0], p[1], q[0], q[1], ALUMINIUM, 1)
    for x in (-40, 40):
        cyl((x - 1.5, 0, 0), (x + 1.5, 0, 0), 3.4, "x", WHITE)
    for x0, phi in wings: wing(x0, True, phi)
    # the US segment in front: Unity, Destiny, Harmony with Columbus and Kibo across it, a docked crew capsule
    cyl((0, 0, -4), (0, 5, -4), 2.3, "y", steel)                                                  # Unity
    cyl((0, 3, -6), (0, 3, -6.5), 1.6, "y", WHITE, cap=False)
    cyl((-15, 21, -4), (-2, 21, -4), 2.2, "x", steel)                                            # Kibo (port)
    cyl((0, 5, -4), (0, 18, -4), 2.2, "y", steel)                                                 # Destiny
    cyl((2, 21, -4), (9, 21, -4), 2.2, "x", steel)                                               # Columbus (starboard)
    cyl((0, 18, -4), (0, 25, -4), 2.3, "y", steel)                                                # Harmony
    cyl((0, 25, -4), (0, 27, -4), 1.2, "y", ALUMINIUM)                                           # the docking adapter
    cyl((0, 27, -4), (0, 31, -4), 1.9, "y", WHITE)                                                # a crew capsule
    p = P(0, 31, -4); f.circle(p[0], p[1], 6, IRON, INK, 1.5)
    return f.svg()


FIGURES = {"hero": hero, "orbit": orbit, "cannon": cannon, "vr": vr_graph, "paino": weightless, "radat": orbits,
           "malli": model_fbd}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "orbit": "reveals: gravity is the only force and points to the centre, F = m a_n",
    "cannon": "reveals: too slow hits the Earth, faster rises higher",
    "vr": "reveals: v = sqrt(γM/r) and the speeds of ISS, GPS and geostationary orbits",
    "paino": "reveals: in orbit only G acts, N = 0 (weightlessness is free fall)",
    "radat": "safe: the Earth's and Halley's orbits to scale with their distances from the Sun",
    "malli": "reveals: the model force diagram of a satellite (only the gravitational force)",
}
