"""Figures of fy4-7 (scripts/figlib.py); `python scripts/figures.py fy4-7` writes them into lesson.md.
Colours carry the quantity in every figure: velocity blue (COLD #1971c2), kinetic energy orange (HEAT #e8590c),
potential energy green (GOOD #2b8a3e), mechanical energy ink. Heights and speeds are drawn to scale where a figure says so."""
import math
from figlib import (Fig, Axes, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK,
                    GRAIN, HEAT_LIGHT, HEAT, HOT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE,
                    GOOD, GOOD_LIGHT, fi, n)
import herolib as H
from herolib import grad, rnd

V_COL, EK_COL, EP_COL = COLD, HEAT, GOOD


# ---------------------------------------------------------------- opening illustration
def _skater(f, x, yf, sc, op, coat, board_angle=0.0):
    """A skateboarder standing upright on a board whose middle is at (x, yf); the board tilts with the ramp."""
    f.add(f'<g opacity="{op:g}">')
    H.walker(f, x, yf - 16 * sc, coat, INK, sc, lean=6, stride=0.45)
    f.add(f'<g transform="rotate({board_angle:g} {n(x)} {n(yf)})">')
    f.rect(x - 70 * sc, yf - 16 * sc, 140 * sc, 12 * sc, COPPER, INK, 2, 6 * sc)
    for wx in (x - 44 * sc, x + 44 * sc):
        f.circle(wx, yf + 3 * sc, 9 * sc, SAND_LIGHT, INK, 2)
    f.add("</g></g>")


def _speed(f, x1, y1, x2, y2):
    """A velocity arrow (blue) with a white halo, so it reads on any background."""
    f.arrow(x1, y1, x2, y2, WHITE, 15, 32)
    f.arrow(x1, y1, x2, y2, V_COL, 8, 26)


def hero():
    """The chapter's opening illustration: a skateboarder rolls up a straight ramp in a skate park, drawn at three
    places to scale: at the foot with speed v, at three quarters of the height with v/2, and at the top at rest.
    The arrows (2 : 1 : 0) start at the skater; a bracket on the ramp marks 3/4 h and 1/4 h."""
    f = H.hero("fy47-hero", "Kuvitus: rullalautailija skeittiparkissa. Lautailija on piirretty kolmeen kohtaan: "
               "tasaisella maalla rampin edessä hänestä lähtee pitkä sininen nopeusnuoli v, kolmen neljäsosan korkeudella "
               "rampissa nuoli on puolet lyhyempi, v/2, ja ylimpänä hän on hetken paikallaan, v = 0. Rampin kyljessä oleva "
               "mittajana näyttää korkeudet: puolet nopeudesta kuluu kolmen neljäsosan nousuun 3/4 h, toinen puolikas vain "
               "viimeiseen neljäsosaan 1/4 h. Nuolten pituudet (2 : 1 : 0) ja korkeudet ovat mittakaavassa.")
    H.sky(f, "fy47h", 420, ICE, GLASS)
    H.sun(f, "fy47h", 400, 74, 38, rays=False)
    H.cloud(f, 180, 96, 0.75); H.cloud(f, 610, 70, 0.5)
    for k in range(4):                                          # the town far behind the park, kept low
        bx = 20 + k * 150 + 30 * rnd(k, 3); bh = 70 + 50 * rnd(k, 5); bw = 90 + 30 * rnd(k, 7)
        f.rect(bx, 350 - bh, bw, bh + 10, ALUMINIUM if k % 2 else METAL_EDGE, INK, 2)
        for r in range(int(bh // 34)):
            for c in range(int(bw // 34)):
                f.rect(bx + 12 + c * 30, 350 - bh + 14 + r * 32, 16, 18, GLASS, None)
    H.forest(f, 362, 40, 26, GOOD, seed=4, depth=18, x1=640)
    H.spruce(f, 40, 386, 90)
    f.rect(0, 380, 1200, 220, grad(f, "fy47h-ground", GLASS, ALUMINIUM, y1=380, y2=600))   # the concrete of the park
    for k in range(5):
        f.line(k * 150 - 20, 380, k * 170 - 120, 600, METAL_EDGE, 1.5)
    # the ramp: a straight plywood wedge rising at 25° from the foot (260, 540) to a deck at y = 180
    foot, yfl, ang = 260, 540, math.radians(25)
    ytop = 180; xtop = foot + (yfl - ytop) / math.tan(ang)
    f.path(f"M{foot},{yfl} L{n(xtop)},{ytop} H1188 V{yfl} Z", grad(f, "fy47h-ply", SAND_DARK, SAND), INK, 3)
    for xx in (760, 900, 1040, 1150):                           # plywood panels (vertical seams, never mistaken for heights)
        yy = max(ytop, yfl - (xx - foot) * math.tan(ang))
        f.line(xx, yy + 4, xx, yfl, GRAIN, 1.5)
    f.rect(xtop - 4, ytop - 8, 1188 - xtop + 4, 10, H.steel(f, "fy47h-coping"), INK, 2)   # the steel coping
    f.line(foot, yfl, xtop, ytop, INK, 4)
    f.line(12, yfl, foot, yfl, INK, 3)
    # the three places, to scale: v at the foot, v/2 at 3/4 of the rise, rest at the top (v² falls linearly with height)
    rise = 330                                                 # the skater's full rise in figure units
    y34, ytp = yfl - 0.75 * rise, yfl - rise
    x34, xtp = foot + 0.75 * rise / math.tan(ang), foot + rise / math.tan(ang)
    L, sc, coat = 170, 0.34, IRON                              # the arrow of speed v; the skater (grey: blue is velocity)
    hip = lambda yb: yb - 12 - 16 * sc - 160 * sc
    xg = 120
    _skater(f, xg, yfl - 12, sc, 1.0, coat)
    _speed(f, xg, hip(yfl), xg + L, hip(yfl))
    f.tex(xg + L - 14, hip(yfl) - 52, "v", anchor="middle", color=V_COL, size=60)
    ca, sa = math.cos(ang), math.sin(ang)
    _skater(f, x34, y34 - 12, sc, 1.0, coat, -25)
    _speed(f, x34, hip(y34), x34 + L / 2 * ca, hip(y34) - L / 2 * sa)
    f.tex(x34 + L / 2 * ca + 6, hip(y34) - L / 2 * sa - 76, r"\dfrac{v}{2}", anchor="middle", color=V_COL, size=56)
    _skater(f, xtp, ytp - 12, sc, 1.0, coat, -25)
    f.tex(xtp + 40, ytp - 150, "v = 0", anchor="start", color=V_COL, size=60, bg=True)
    # the heights on the ramp itself: a dimension line in quarters, guides from where the wheels touch the ramp
    bx = 1068
    for y, x in ((y34, x34 + 34), (ytp, xtp + 34)):
        f.line(x, y, bx - 10, y, INK, 2, "8 6")
    f.line(bx, ytp, bx, yfl, INK, 3)
    for q in range(5):
        yq = yfl - q * rise / 4
        f.line(bx - (14 if q in (0, 3, 4) else 8), yq, bx + (14 if q in (0, 3, 4) else 8), yq, INK, 3 if q in (0, 3, 4) else 2)
    f.tex(bx + 18, (yfl + y34) / 2, r"\dfrac{3}{4}h", anchor="start", size=56, bg=True)
    f.tex(bx + 18, (y34 + ytp) / 2, r"\dfrac{1}{4}h", anchor="start", size=56, bg=True)
    f.rect(440, 562, 150, 12, COPPER, INK, 2, 3)                  # a bench with a helmet on it
    f.rect(454, 574, 10, 14, IRON); f.rect(566, 574, 10, 14, IRON)
    f.path("M490,562 a22,20 0 0 1 44,0 Z", HEAT, INK, 2)
    return f.svg()


# ---------------------------------------------------------------- theory figures
def _cart(f, cx, cy, ang_deg, body=ALUMINIUM, op=1.0):
    """A small cart whose wheels touch the surface at (cx, cy), tilted by ang_deg (negative: up to the right)."""
    f.add(f'<g opacity="{op:g}" transform="rotate({ang_deg:g} {n(cx)} {n(cy)})">')
    f.rect(cx - 20, cy - 26, 40, 16, body, INK, 2.5, 3)
    for wx in (cx - 11, cx + 11):
        f.circle(wx, cy - 7, 6.5, IRON, INK, 2)
    f.add("</g>")


def ramppi():
    """Ydinajatus: the same cart starts up the same frictionless ramp with speed v and with 2v; it rises to h and 4h."""
    f = Fig("fy47-ramppi", 360, "Kaksi kuvaa samasta rampista, korkeudet ja nopeusnuolet mittakaavassa. Vasemmalla kärry lähtee "
            "rampin juurelta nopeudella v, jota esittää lyhyt sininen nuoli, ja nousee korkeudelle h. Oikealla sama kärry lähtee "
            "kaksinkertaisella nopeudella 2v, nuoli on kaksi kertaa pidempi, ja se nousee korkeudelle 4h eli neljä kertaa "
            "korkeammalle. Kitkaa ei ole.")
    ang = math.radians(50)
    yfl, hpx, rise = 320, 45, 205                              # h = 45 units, 4h = 180
    for x0, k, tag in ((20, 1, r"\overline{v}"), (316, 2, r"2\overline{v}")):
        foot = x0 + 84
        top = foot + rise / math.tan(ang)
        f.path(f"M{foot},{yfl} L{n(top)},{yfl - rise} H{n(top + 26)} V{yfl} Z", grad(f, f"fy47-rp{k}", SAND_DARK, SAND), INK, 2.5)
        f.line(x0 + 4, yfl, x0 + 262, yfl, INK, 2.5)
        hk = hpx * k * k
        xs = foot + hk / math.tan(ang)
        _cart(f, x0 + 56, yfl, 0)
        _cart(f, xs + 4, yfl - hk - 3, -50, op=0.55)
        f.arrow(x0 + 42, yfl - 46, x0 + 42 + 30 * k, yfl - 46, V_COL, 4, 13)
        f.tex(x0 + 42 + 15 * k, yfl - 72, tag, "middle", V_COL)
        f.line(x0 + 24, yfl - hk, xs - 2, yfl - hk, MUTED, 1.5, "7 6")
        f.line(x0 + 24, yfl, x0 + 24, yfl - hk, INK, 2)
        f.line(x0 + 18, yfl - hk, x0 + 30, yfl - hk, INK, 2)
        if k == 1: f.tex(x0 + 16, yfl - hk / 2 - 12, "h", "end")
        else: f.tex(x0 + 32, yfl - hk * 0.72, "4h", "start")
    f.line(300, 24, 300, 336, RULE, 1.5, "6 6")
    return f.svg()


def polut():
    """Ydinajatus: from the same height h, a ball dropped straight down and carts on a steep and a gentle frictionless
    ramp all reach the floor with the same speed (equal blue arrows): gravity's energy depends only on the height."""
    f = Fig("fy47-polut", 350, "Kaavakuva, ei mittakaavassa. Kolme reittiä samalta korkeudelta h lattiaan: vasemmalla pallo putoaa "
            "suoraan alas tornin vierestä, keskellä kärry laskee jyrkkää ramppia ja oikealla loivempaa ramppia. Kitkaa ja "
            "ilmanvastusta ei ole. Alhaalla kaikilla kolmella on yhtä pitkä sininen nopeusnuoli: nopeus on sama, koska painovoiman "
            "potentiaalienergia riippuu vain korkeudesta eikä reitistä.")
    ytop, yfl = 80, 290
    f.rect(20, yfl, 560, 12, SAND_LIGHT); f.line(20, yfl, 580, yfl, INK, 2.5)
    f.line(20, ytop, 550, ytop, MUTED, 1.5, "7 6")
    L = 54
    # the drop: a tower and the ball beside it, at the top and just above the floor
    f.rect(24, ytop, 18, yfl - ytop, SAND_DARK, INK, 2)
    f.circle(58, ytop + 12, 11, HOT, INK, 2)
    f.line(58, ytop + 30, 58, yfl - 50, MUTED, 1.5, "6 6")
    f.circle(58, yfl - 14, 11, HOT, INK, 2)
    f.arrow(86, yfl - 84, 86, yfl - 84 + L, V_COL, 4, 13)
    f.tex(96, yfl - 60, r"\overline{v}", "start", V_COL)
    # the ramps: a tower each, the ramp to the floor, the cart at the foot with its arrow above it
    for tx0, foot, gid in ((120, 200, "fy47-ps"), (296, 470, "fy47-pg")):
        f.rect(tx0, ytop, 18, yfl - ytop, SAND_DARK, INK, 2)
        f.path(f"M{tx0 + 18},{ytop} L{foot},{yfl} H{tx0 + 18} Z", grad(f, gid, SAND_DARK, SAND), INK, 2)
        _cart(f, foot + 30, yfl, 0)
        f.arrow(foot, yfl - 46, foot + L, yfl - 46, V_COL, 4, 13)
        f.tex(foot + L / 2, yfl - 70, r"\overline{v}", "middle", V_COL)
    f.line(556, ytop, 556, yfl, INK, 2); f.line(550, ytop, 562, ytop, INK, 2)
    f.tex(564, (ytop + yfl) / 2, "h", "start")
    f.tex(300, 40, r"\text{sama korkeus, sama nopeus}", "middle")
    return f.svg()


def nollataso():
    """Kaava: a book on a shelf 1,80 m and a table 0,80 m above the floor; E_p with the floor or the table top as the
    zero level. The values differ, the change from the shelf to the table (4,9 J) does not."""
    f = Fig("fy47-nollataso", 400, "Kaavakuva, korkeudet mittakaavassa. Vasemmalla seinähylly 1,80 metrin ja pöytä 0,80 metrin "
            "korkeudella lattiasta, ja hyllyllä on 0,50 kilogramman kirja. Oikealla kaksi pystysuoraa asteikkoa potentiaalienergian "
            "arvoista. Kun nollataso on lattia, kirjan potentiaalienergia on hyllyllä 8,8 joulea, pöydällä 3,9 joulea ja "
            "lattialla nolla. Kun nollataso on pöydän pinta, arvot ovat 4,9 joulea, nolla ja miinus 3,9 joulea. Kummassakin "
            "potentiaalienergia pienenee 4,9 joulea, kun kirja siirretään hyllyltä pöydälle.")
    yfl, k = 322, 150                                          # 150 units per metre
    Y = lambda h: yfl - k * h
    f.rect(20, 18, 240, yfl - 18, GLASS)                       # the wall
    f.rect(20, yfl, 240, 12, SAND_LIGHT); f.line(20, yfl, 260, yfl, INK, 2.5)
    f.rect(36, Y(1.80), 110, 8, SAND_DARK, INK, 2)              # the shelf with its bracket
    f.path(f"M48,{n(Y(1.80) + 8)} l0,24 l18,-24 Z", IRON)
    f.rect(76, Y(1.80) - 34, 46, 34, COLD, INK, 2.5, 2)         # the book
    f.rect(80, Y(1.80) - 30, 4, 26, COLD_LIGHT)
    f.rect(150, Y(0.80), 104, 10, SAND_DARK, INK, 2)            # the table
    f.rect(160, Y(0.80) + 10, 8, k * 0.80 - 10, SAND, INK, 1.5); f.rect(236, Y(0.80) + 10, 8, k * 0.80 - 10, SAND, INK, 1.5)
    f.rect(184, Y(0.80) - 34, 46, 34, COLD, INK, 2.5, 2); f.add(f'<rect x="184" y="{n(Y(0.80) - 34)}" width="46" height="34" fill="{WHITE}" fill-opacity="0.45"/>')
    for h in (1.80, 0.80):
        f.line(256, Y(h), 600 - 24, Y(h), MUTED, 1.5, "7 6")
    # two scales of E_p
    for xs, zero, vals, title in ((350, 0.0, ("8{,}8", "3{,}9", "0"), r"\text{lattia}"),
                                  (500, 0.80, ("4{,}9", "0", "-3{,}9"), r"\text{pöytä}")):
        f.line(xs, Y(1.80) - 6, xs, yfl + 6, INK, 2.5)
        f.line(xs - 12, Y(zero), xs + 12, Y(zero), EP_COL, 4)
        for h, v in zip((1.80, 0.80, 0.0), vals):
            f.circle(xs, Y(h), 6.5, EP_COL, WHITE, 2)
            f.tex(xs + 14, Y(h) - 16, v + r"\,\text{J}", "start", EP_COL)
        f.tex(xs, 354, r"\text{nollataso}", "middle")
        f.tex(xs, 382, title, "middle")
        f.arrow(xs - 20, Y(1.80) + 6, xs - 20, Y(0.80) - 6, EP_COL, 3, 12)
    f.tex(425, (Y(1.80) + Y(0.80)) / 2 - 16, r"\Delta E_\text{p}", "middle", EP_COL)
    f.tex(425, (Y(1.80) + Y(0.80)) / 2 + 16, r"= -4{,}9\,\text{J}", "middle", EP_COL)
    f.tex(152, Y(1.80) + 4, r"1{,}80\,\text{m}", "start", MUTED)
    f.tex(140, Y(0.80), r"0{,}80\,\text{m}", "end", MUTED)
    return f.svg()


def ek_kuvaaja():
    """Kaava: E_k against v for m = 1,0 kg: doubling the speed from 2,0 to 4,0 m/s gives four times the energy."""
    f = Fig("fy47-ekv", 350, "Kuvaaja mittakaavassa: vaaka-akselilla nopeus nollasta 4,5 metriin sekunnissa, pystyakselilla liike-energia "
            "nollasta 9 jouleen kappaleelle, jonka massa on 1,0 kilogrammaa. Kuvaaja on ylöspäin kaartuva paraabeli. Nopeudella "
            "2,0 metriä sekunnissa liike-energia on 2,0 joulea ja nopeudella 4,0 metriä sekunnissa 8,0 joulea: kaksinkertainen "
            "nopeus antaa nelinkertaisen liike-energian. Katkoviivat näyttävät lukemat.")
    ax = Axes(f, (90, 304), (470, 76), x=(0, 4.5), y=(0, 9), xticks=[1, 2, 3, 4], yticks=list(range(1, 10)),
              xlabel=r"v\ (\text{m/s})", ylabel=r"E_\text{k}\ (\text{J})", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.curve(lambda v: 0.5 * v * v, 0, 4.24, EK_COL, 3.5)
    for v in (2, 4):
        ax.guide(v, 0.5 * v * v); ax.point(v, 0.5 * v * v, EK_COL)
    f.tex(ax.X(2) - 12, ax.Y(2) - 22, r"2{,}0\,\text{J}", "end", EK_COL, bg=True)
    f.tex(ax.X(4) - 12, ax.Y(8) - 22, r"8{,}0\,\text{J}", "end", EK_COL, bg=True)
    f.tex(ax.X(4.24) + 10, ax.Y(9) + 10, r"E_\text{k}", "start", EK_COL)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id; no answer drawn)
def pallo_ek():
    f = Fig("fy47-pallo", 360, "Kuvaaja mittakaavassa: vaaka-akselilla pallon nopeus nollasta 6 metriin sekunnissa, pystyakselilla "
            "pallon liike-energia nollasta 10 jouleen yhden joulen välein. Kuvaaja on origosta ylöspäin kaartuva käyrä, joka "
            "kulkee pisteiden (2,0 m/s; 1,0 J), (4,0 m/s; 4,0 J) ja (6,0 m/s; 9,0 J) kautta. Massaa ei ole merkitty.")
    ax = Axes(f, (90, 314), (476, 70), x=(0, 6.5), y=(0, 10), xticks=[1, 2, 3, 4, 5, 6], yticks=list(range(1, 11)),
              xlabel=r"v\ (\text{m/s})", ylabel=r"E_\text{k}\ (\text{J})", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.curve(lambda v: 0.25 * v * v, 0, 6.25, EK_COL, 3.5)
    return f.svg()


FIGURES = {"hero": hero, "ramppi": ramppi, "polut": polut, "nollataso": nollataso, "ek-kuvaaja": ek_kuvaaja,
           "pallo-ek": pallo_ek}

# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "ramppi": "reveals: doubling the speed up a frictionless ramp gives four times the height (a theory figure)",
    "polut": "reveals: the same speed at the bottom of different frictionless paths from one height (a theory figure)",
    "nollataso": "reveals: E_p of a 0,50 kg book from two zero levels and the equal change 4,9 J (a theory figure)",
    "ek-kuvaaja": "reveals: E_k against v for 1,0 kg, 2,0 J at 2,0 m/s and 8,0 J at 4,0 m/s",
    "pallo-ek": "safe: an E_k(v) curve on a grid; the mass is not marked",
}
