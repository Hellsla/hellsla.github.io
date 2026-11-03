"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-6` writes them into lesson.md.
Force red, velocity blue, acceleration orange (FY4/FY5). The orbits of the cannon figure are integrated with the same
velocity Verlet step as the simulation, so the drawn paths are the computed ones."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, COLD_LIGHT, GLASS,
                    WATER, WATER_LIGHT, SAND_DARK, ALUMINIUM, METAL_EDGE, IRON, ICE, GOOD, n)
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


def hero():
    """The chapter's opening illustration: the space station above the Earth's limb, an astronaut floating at a window."""
    f = H.hero("fy56-hero", "Kuvitus: avaruusasema kiertää Maata. Alhaalla näkyy Maan kaareutuva pinta, jossa on merta, "
               "maata ja pilviä, ja ohut ilmakehä. Asemalla on pitkä ristikkorunko, suuret aurinkopaneelit ja asuinmoduulit. "
               "Moduulin ikkunassa näkyy astronautti leijumassa.")
    H.space(f, seed=6, count=90)
    # the Earth's limb: a large disc whose top shows at the bottom
    f.defs_add(f'<radialGradient id="fy56h-ocean" cx="0.4" cy="0.1" r="0.9"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></radialGradient>')
    f.add(f'<circle cx="600" cy="1580" r="1150" fill="{ICE}" fill-opacity="0.35"/>')
    f.circle(600, 1580, 1110, "url(#fy56h-ocean)")
    for x, y, rx, ry in ((260, 520, 170, 50), (720, 486, 220, 44), (1040, 560, 130, 40)):
        f.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{SAND_DARK}"/>')
    for x, y, w in ((140, 480, 160), (470, 455, 200), (880, 470, 180), (600, 540, 240), (1080, 505, 120)):
        f.path(f"M{x},{y} q{n(w / 4)},-14 {n(w / 2)},0 t{n(w / 2)},0", stroke=WHITE, w=12, extra='stroke-linecap="round" stroke-opacity="0.85"')
    # the station: truss, solar arrays, radiators and modules
    cx, cy = 600, 230
    f.rect(cx - 330, cy - 9, 660, 18, ALUMINIUM, INK, 2.5, 3)
    for k in range(-15, 16):
        f.line(cx + k * 22, cy - 9, cx + k * 22 + 11, cy + 9, METAL_EDGE, 2)
    f.defs_add(f'<linearGradient id="fy56h-panel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{COLD}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    for side in (-1, 1):
        for dx in (250, 330):
            x = cx + side * dx - 30
            for y0 in (cy - 170, cy + 22):
                f.rect(x, y0, 60, 148, "url(#fy56h-panel)", INK, 2.5, 2)
                for j in range(1, 6):
                    f.line(x, y0 + j * 148 / 6, x + 60, y0 + j * 148 / 6, ICE, 1.5)
            f.line(x + 30, cy - 22, x + 30, cy + 22, INK, 3)
    for dx in (-150, 150):
        f.rect(cx + dx - 20, cy + 14, 40, 80, WHITE, INK, 2.5, 2)
    f.rect(cx - 110, cy - 46, 220, 70, WHITE, INK, 3, 30)
    f.rect(cx - 30, cy - 86, 60, 172, WHITE, INK, 3, 26)
    for x in (cx - 80, cx + 50):
        f.line(x, cy - 46, x, cy + 24, RULE, 2)
    # a round window with a floating astronaut
    f.circle(cx + 76, cy - 11, 22, GLASS, INK, 3)
    f.add(f'<g transform="rotate(-28 {cx + 76} {cy - 11})">')
    f.circle(cx + 76, cy - 22, 7, WHITE, INK, 2)
    f.rect(cx + 70, cy - 15, 12, 18, WHITE, INK, 2, 4)
    f.add("</g>")
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
