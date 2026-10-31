"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-9` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GOOD, GOOD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND_LIGHT, SAND, GLASS, ICE, PAPER, n)
import herolib as H

RED = HOT              # forces and impulse (#c92a2a)
BLUE = COLD            # velocity (#1971c2)
PURPLE = "#7048e8"     # momentum: its own colour, apart from velocity, force and acceleration


def pent(cx, cy, R, rot):
    """The path of a regular pentagon of circumradius R centred at (cx, cy), turned by rot degrees."""
    pts = [(cx + R * math.cos(math.radians(rot + 72 * k - 90)), cy + R * math.sin(math.radians(rot + 72 * k - 90))) for k in range(5)]
    return "M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z"


def ball(f, x, y, r, kind):
    """A football (white with a dark centre pentagon and five dark patches cut by the rim) or a bowling ball (finger holes)."""
    if kind == "jalka":
        cid = f"{f.fid}-c{len(f.defs)}"
        f.defs_add(f'<clipPath id="{cid}"><circle cx="{n(x)}" cy="{n(y)}" r="{r:g}"/></clipPath>')
        f.circle(x, y, r, WHITE)
        f.path(pent(x, y, r * 0.34, 0), INK)
        for k in range(5):
            a = math.radians(72 * k + 90)
            ex, ey = x + math.cos(a) * r * 1.0, y + math.sin(a) * r * 1.0
            f.path(pent(ex, ey, r * 0.36, 36), INK, extra=f'clip-path="url(#{cid})"')
        for k in range(5):                                   # seams from the centre pentagon's corners to the rim patches
            a = math.radians(72 * k - 90)
            f.line(x + math.cos(a) * r * 0.34, y + math.sin(a) * r * 0.34, x + math.cos(a) * r * 0.7, y + math.sin(a) * r * 0.7, INK, 1.5)
        f.circle(x, y, r, "none", INK, 2.5)
    else:
        f.circle(x, y, r, IRON, INK, 2.5)
        for dx, dy in ((-0.25, -0.35), (0.12, -0.42), (-0.02, -0.05)):
            f.circle(x + dx * r, y + dy * r, r * 0.11, INK)


def liikemaara():
    """Ydinajatus: equal momenta of a fast football and a slow bowling ball, and a football moving the other way."""
    f = Fig("fy49-liikemaara", 370, "Kaavakuva, nuolet mittakaavassa: kolme palloa x-akselilla, jonka positiivinen suunta on oikealle. "
            "Ylhäällä 0,45 kilogramman jalkapallo liikkuu oikealle nopeudella 20 metriä sekunnissa: pitkä sininen nopeusnuoli ja "
            "violetti liikemääränuoli, liikemäärä 9,0 kilogrammametriä sekunnissa. Keskellä 6,0 kilogramman keilapallo liikkuu oikealle "
            "nopeudella 1,5 metriä sekunnissa: hyvin lyhyt nopeusnuoli mutta yhtä pitkä liikemääränuoli kuin jalkapallolla, sillä "
            "liikemäärä on sama 9,0. Alhaalla jalkapallo liikkuu vasemmalle nopeudella 10 metriä sekunnissa: nuolet osoittavat vasemmalle, "
            "ja liikemäärä on miinus 4,5 kilogrammametriä sekunnissa.")
    kv, kp = 12, 16                                        # px per m/s and px per kg·m/s
    rows = [(62, 70, "jalka", 22, 20, 0.45, r"0{,}45\,\text{kg}", r"v = 20\,\text{m/s}", r"p = 9{,}0\,\text{kg}\cdot\text{m/s}"),
            (168, 70, "keila", 30, 1.5, 6.0, r"6{,}0\,\text{kg}", r"v = 1{,}5\,\text{m/s}", r"p = 9{,}0\,\text{kg}\cdot\text{m/s}"),
            (274, 336, "jalka", 22, -10, 0.45, r"0{,}45\,\text{kg}", r"v = -10\,\text{m/s}", r"p = -4{,}5\,\text{kg}\cdot\text{m/s}")]
    for k, (y, bx, kind, r, v, m, ml, vl, pl) in enumerate(rows):
        if k: f.line(20, y - 46, 580, y - 46, RULE, 1.5, "6 6")
        ball(f, bx, y, r, kind)
        f.tex(bx, y + r + (12 if r > 25 else 18), ml, "middle")
        x0 = bx + r + 16 if v > 0 else bx - r - 16
        f.arrow(x0, y - 16, x0 + v * kv, y - 16, BLUE, 3.5, 13 if abs(v * kv) > 20 else 10)
        f.arrow(x0, y + 16, x0 + m * v * kp, y + 16, PURPLE, 5, 15)
        f.tex(388, y - 16, vl, "start", BLUE)
        f.tex(388, y + 16, pl, "start", PURPLE)
    f.arrow(40, 352, 360, 352, INK, 2, 12)
    f.tex(368, 352, r"x", "start")
    return f.svg()


def pysaytys():
    """Ydinajatus: the force F_x on a 1,0 kg cart stopped from 2,0 m/s by a hard and a soft bumper (the sim's model), below the
    axis as in the sim: equal areas, I = -2,0 N·s."""
    f = Fig("fy49-pysaytys", 340, "Kuvaaja mittakaavassa, simulaation mallin arvoja: puskurin kärryyn kohdistaman voiman x-komponentti F_x newtoneina aja"
            "n funktiona, kun 1,0 kilogramman kärry pysähtyy nopeudesta 2,0 metriä sekunnissa. Kärry liikkuu positiiviseen suuntaan"
            " ja voima osoittaa negatiiviseen suuntaan, joten käyrät ovat vaaka-akselin alapuolella. Kova puskuri: voima on suurimm"
            "illaan miinus 80 newtonia ja törmäys kestää 0,039 sekuntia, kapea ja syvä käyrä. Pehmeä puskuri: voima on suurimmillaa"
            "n vain miinus 20 newtonia, mutta törmäys kestää 0,157 sekuntia, matala ja leveä käyrä. Käyrien ja vaaka-akselin välise"
            "t alueet on varjostettu, ja ne ovat yhtä suuret: kummankin impulssi on miinus 2,0 newtonsekuntia.")
    ax = Axes(f, (92, 300), (478, 72), x=(0, 0.2), y=(-100, 0), xticks=[0, 0.05, 0.1, 0.15, 0.2], yticks=[-100, -80, -60, -40, -20, 0],
              xlabel=r"t\ (\text{s})", ylabel=r"F_x\ (\text{N})", x_at=0)   # signed, like the sim: the time axis at F_x = 0, the curves below it
    for Fm, T, dash, lx, ly, name in ((-80, 0.03927, None, 0.048, -80, r"\text{kova}"), (-20, 0.15708, "9 6", 0.162, -30, r"\text{pehmeä}")):
        w = math.pi / 2 / T
        pts = [(T * i / 60, Fm * math.sin(w * T * i / 60)) for i in range(61)] + [(T, 0)]
        ax.area([(0, 0)] + pts, HOT_LIGHT, 0.45)
        ax.line(pts, RED, 3, dash)
        f.tex(ax.X(lx), ax.Y(ly), name, "start", RED, bg=True)
    f.tex(ax.X(0.128), ax.Y(-52), r"\text{yhtä suuret pinta-alat}", "middle", INK, bg=True)
    return f.svg()


def keskivoima():
    """Kaava: a varying force during Δt and the constant mean force with the same area (schematic)."""
    f = Fig("fy49-keskivoima", 330, "Kaavakuva, ei lukuarvoja: törmäyksen aikana voima F kasvaa nollasta suurimpaan arvoonsa ja "
            "pienenee takaisin nollaan aikavälin Delta t aikana. Käyrän alle jäävä pinta-ala on impulssi I. Katkoviivoin piirretty "
            "suorakulmio, jonka korkeus on keskimääräinen voima F_ka ja leveys Delta t, on pinta-alaltaan yhtä suuri kuin käyrän alle "
            "jäävä alue.")
    ax = Axes(f, (80, 262), (470, 52), x=(0, 1.25), y=(0, 1.1), xticks=[0], yticks=[0], xlabel=r"t", ylabel=r"F")
    t0, t1, Fm = 0.15, 1.05, 1.0
    pts = [(t0 + (t1 - t0) * i / 80, Fm * math.sin(math.pi * i / 80)) for i in range(81)]
    ax.area([(t0, 0)] + pts + [(t1, 0)], HOT_LIGHT, 0.45)
    Fka = 2 / math.pi * Fm
    f.rect(ax.X(t0), ax.Y(Fka), ax.X(t1) - ax.X(t0), ax.Y(0) - ax.Y(Fka), "none", INK, 2, extra='stroke-dasharray="7 5"')
    ax.line(pts, RED, 3)
    f.tex(ax.X(t1) + 10, ax.Y(Fka), r"F_\text{ka}", "start")
    f.tex(ax.X(0.6), ax.Y(0.3), r"I", "middle", RED, bg=True)
    y = ax.Y(0) + 32
    f.line(ax.X(t0), y - 10, ax.X(t0), y + 10, INK, 2); f.line(ax.X(t1), y - 10, ax.X(t1), y + 10, INK, 2)
    xm = ax.X(0.6); f.line(ax.X(t0), y, xm - 30, y, INK, 2); f.line(xm + 30, y, ax.X(t1), y, INK, 2)
    f.tex(ax.X(0.6), y, r"\Delta t", "middle")
    return f.svg()


def kimpoaminen():
    """Kaava: a ball bounces straight back from a wall; Δp = p − p0 is twice as long as p0 and points like the wall's force."""
    f = Fig("fy49-kimpoaminen", 330, "Kaavakuva, nuolet mittakaavassa. Vasemmalla pallo ennen törmäystä ja sen jälkeen: ennen törmäystä "
            "pallo liikkuu oikealle kohti seinää ja sen liikemäärä p0 osoittaa oikealle, jälkeen pallo liikkuu yhtä nopeasti vasemmalle ja "
            "sen liikemäärä p osoittaa vasemmalle. Oikealla liikemäärän muutos: p ja miinus p0 peräkkäin muodostavat nuolen Delta p, "
            "joka on kaksi kertaa niin pitkä kuin p0 ja osoittaa vasemmalle. Alimpana seinän voiman impulssi I, yhtä pitkä kuin Delta p "
            "ja samaan suuntaan.")
    L = 80
    # the wall and the ball before and after
    f.rect(272, 28, 34, 260, RULE)
    f.line(272, 28, 272, 288, INK, 2.5)
    for y in range(40, 288, 18): f.line(276, y + 14, 300, y, MUTED, 1.5)
    f.tex(40, 50, r"\text{ennen}", "start")
    ball(f, 246, 96, 22, "jalka")
    f.arrow(120, 96, 120 + L, 96, PURPLE, 5, 15); f.tex(160, 64, r"\overline{p}_0", "middle", PURPLE)
    f.tex(40, 180, r"\text{jälkeen}", "start")
    ball(f, 246, 226, 22, "jalka")
    f.arrow(204, 226, 204 - L, 226, PURPLE, 5, 15); f.tex(164, 194, r"\overline{p}", "middle", PURPLE)
    f.line(330, 20, 330, 310, RULE, 2, "6 6")
    # the vector difference: p followed by −p0
    xr = 560
    f.arrow(xr, 70, xr - L, 70, PURPLE, 5, 15); f.tex(xr - L / 2, 40, r"\overline{p}", "middle", PURPLE)
    f.arrow(xr - L, 70, xr - 2 * L, 70, PURPLE, 3, 13); f.tex(xr - 1.5 * L, 40, r"-\overline{p}_0", "middle", PURPLE)
    f.line(xr - L, 60, xr - L, 80, PURPLE, 2)
    f.arrow(xr, 160, xr - 2 * L, 160, PURPLE, 6, 16); f.tex(xr - L, 130, r"\Delta\overline{p}", "middle", PURPLE)
    f.arrow(xr, 250, xr - 2 * L, 250, RED, 6, 16); f.tex(xr - L, 220, r"\overline{I}", "middle", RED)
    f.tex(xr - L, 292, r"\overline{I} = \Delta\overline{p}", "middle")
    return f.svg()


def ex_potku():
    """Exercise L3-01: a trapezoidal push on a sled (the area is not shaded)."""
    f = Fig("fy49-ex-potku", 340, "Kuvaaja mittakaavassa: vaakasuora voima, jolla pulkkaa työnnetään, ajan funktiona. Voima kasvaa "
            "tasaisesti nollasta 60 newtoniin 0,20 sekunnissa, pysyy 60 newtonissa hetkeen 0,80 sekuntia ja pienenee tasaisesti nollaan "
            "hetkellä 1,00 sekuntia. Vaaka-akselilla aika 0–1,2 sekuntia 0,2 sekunnin välein, pystyakselilla voima 0–80 newtonia "
            "20 newtonin välein.")
    ax = Axes(f, (92, 286), (478, 52), x=(0, 1.2), y=(0, 80), xticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], yticks=[0, 20, 40, 60, 80],
              xlabel=r"t\ (\text{s})", ylabel=r"F\ (\text{N})")
    ax.line([(0, 0), (0.2, 60), (0.8, 60), (1.0, 0)], RED, 3)
    return f.svg()


def tarkistus_kolmio():
    """Check 2: a kick's force on a football as a triangle (the area is not shaded)."""
    f = Fig("fy49-tarkistus-kolmio", 340, "Kuvaaja mittakaavassa: voima, jolla jalka potkaisee palloa, ajan funktiona millisekunteina. "
            "Voima kasvaa tasaisesti nollasta 900 newtoniin 6 millisekunnissa ja pienenee tasaisesti nollaan hetkellä 12 millisekuntia. "
            "Vaaka-akselilla aika 0–14 millisekuntia 2 millisekunnin välein, pystyakselilla voima 0–1000 newtonia 100 newtonin "
            "ruuduin, luvut 200 newtonin välein.")
    ax = Axes(f, (100, 286), (478, 52), x=(0, 14), y=(0, 1000), xticks=[0, 2, 4, 6, 8, 10, 12, 14], yticks=list(range(0, 1001, 100)),
              xlabel=r"t\ (\text{ms})", ylabel=r"F\ (\text{N})", yfmt=lambda v: str(v) if v % 200 == 0 else "")
    ax.line([(0, 0), (6, 900), (12, 0)], RED, 3)
    return f.svg()


def jumper(f, hx, hy, sc=1.0):
    """A high jumper arching backwards over the bar (flop), seen from the side: hips at (hx, hy), moving to the right."""
    s = sc
    knee, foot = (hx - 70 * s, hy + 18 * s), (hx - 120 * s, hy - 26 * s)
    sh, head = (hx + 92 * s, hy + 22 * s), (hx + 126 * s, hy + 40 * s)
    f.path(f"M{n(hx)},{n(hy)} L{n(knee[0])},{n(knee[1])} L{n(foot[0])},{n(foot[1])}", stroke=SAND_LIGHT, w=24 * s, extra='stroke-linecap="round"')
    f.path(f"M{n(hx + 8 * s)},{n(hy - 6 * s)} L{n(knee[0] + 4 * s)},{n(knee[1] - 4 * s)}", stroke=INK, w=34 * s, extra='stroke-linecap="round"')
    f.path(f"M{n(foot[0] - 10 * s)},{n(foot[1] + 4 * s)} l{n(-14 * s)},{n(-10 * s)}", stroke=WHITE, w=16 * s, extra='stroke-linecap="round"')
    f.path(f"M{n(hx)},{n(hy)} Q{n(hx + 50 * s)},{n(hy - 4 * s)} {n(sh[0])},{n(sh[1])}", stroke=HOT, w=46 * s, extra='stroke-linecap="round"')
    f.path(f"M{n(sh[0] - 6 * s)},{n(sh[1] + 10 * s)} L{n(hx + 30 * s)},{n(hy + 50 * s)}", stroke=SAND_LIGHT, w=16 * s, extra='stroke-linecap="round"')
    f.circle(head[0], head[1], 26 * s, SAND_LIGHT)
    f.path(f"M{n(head[0] - 4 * s)},{n(head[1] - 26 * s)} Q{n(head[0] + 30 * s)},{n(head[1] - 22 * s)} {n(head[0] + 26 * s)},{n(head[1] + 8 * s)} "
           f"Q{n(head[0] + 10 * s)},{n(head[1] - 4 * s)} {n(head[0] - 4 * s)},{n(head[1] - 26 * s)} Z", COPPER)


def hero():
    """The chapter's opening illustration: a high jumper clears the bar above a thick landing mat in a stadium."""
    f = H.hero("fy49-hero", "Kuvitus: korkeushyppy ulkostadionilla kesäpäivänä. Kuvan keskellä hyppääjä kaartuu selällään riman yli, "
               "ja riman alla on paksu sininen alastulopatja. Katkoviiva näyttää hyppääjän radan, joka kaartuu riman yli alas patjalle. "
               "Taustalla on katsomo ja juoksurata, ja patjan vieressä nurmikkoa.")
    H.sky(f, "fy49h", 330)
    H.cloud(f, 200, 90, 0.9); H.cloud(f, 1000, 70, 0.7)
    # the stand: rows of seats with spectators as dots
    f.rect(0, 150, 1200, 180, ALUMINIUM)
    for r in range(5):
        y = 168 + r * 32
        f.rect(0, y + 18, 1200, 8, METAL_EDGE)
        for k in range(40):
            if H.rnd(k + 40 * r, 4) < 0.55:
                c = (COLD, HOT, HEAT, GOOD, SAND, WHITE)[int(H.rnd(k + 9 * r, 7) * 6)]
                x = 14 + k * 30 + 8 * (r % 2)
                f.circle(x, y + 6, 8, c); f.circle(x, y - 6, 5.5, SAND_LIGHT)
    f.rect(0, 322, 1200, 10, INK)
    # the running track and the grass
    f.rect(0, 330, 1200, 70, COPPER)
    for y in (346, 364, 382): f.line(0, y, 1200, y, WHITE, 2)
    f.rect(0, 398, 1200, 202, H.grad(f, "fy49h-grass", GOOD_LIGHT, GOOD, y1=398, y2=800))
    # the landing mat: a thick blue block with a lighter top
    f.path("M380,430 L860,430 L930,388 L450,388 Z", COLD_LIGHT, INK, 3)
    f.rect(380, 430, 480, 92, COLD, INK, 3)
    f.path("M860,430 L930,388 L930,480 L860,522 Z", "#4f8fbf", INK, 3)
    for x in (500, 620, 740): f.line(x, 436, x, 516, COLD_LIGHT, 2)
    f.line(386, 476, 854, 476, COLD_LIGHT, 2)
    # the standards and the bar
    for x, top in ((430, 196), (880, 176)):
        f.rect(x - 7, top, 14, (430 if x < 600 else 400) - top, ALUMINIUM, INK, 2)
        f.rect(x - 16, (430 if x < 600 else 400) - 6, 32, 10, IRON)
    f.line(430, 262, 880, 242, WHITE, 8)
    for k in range(0, 9, 2): f.line(430 + 50 * k, 262 - 20 * k / 9, 430 + 50 * (k + 1), 262 - 20 * (k + 1) / 9, HOT, 8)
    # the path of the jump: up from the left, over the bar, down onto the mat
    f.path("M330,470 Q560,20 760,410", stroke=MUTED, w=3, extra='stroke-dasharray="10 9"')
    jumper(f, 600, 162, 1.0)
    # the jumper's shadow on the mat
    f.add('<ellipse cx="660" cy="412" rx="120" ry="12" fill="#1f2933" fill-opacity="0.18"/>')
    return f.svg()


FIGURES = {"hero": hero, "liikemaara": liikemaara, "pysaytys": pysaytys, "keskivoima": keskivoima, "kimpoaminen": kimpoaminen,
           "ex-potku": ex_potku, "tarkistus-kolmio": tarkistus_kolmio}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "liikemaara": "reveals: p = m v with equal momenta of a fast light and a slow heavy ball, and a negative momentum",
    "pysaytys": "reveals: a hard and a soft stop have equal impulses (areas) but different peak forces and times",
    "keskivoima": "reveals: the impulse as the area under (t, F) and the mean force as the rectangle of equal area",
    "kimpoaminen": "reveals: Δp of a ball bouncing straight back is twice p0 and points like the wall's force",
    "ex-potku": "safe: a trapezoidal (t, F) graph on a grid, the area not shaded",
    "tarkistus-kolmio": "safe: a triangular (t, F) graph on a grid, the area not shaded",
}
