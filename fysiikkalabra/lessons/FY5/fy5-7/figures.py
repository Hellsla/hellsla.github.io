"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-7` writes them into lesson.md.
The motion itself (a curve x(t) the text describes) is ink, a fitted model is blue as in the simulation, simulated
measurement points are ink circles with a white ring; every arrow is a filled path. The graphs of the tasks are
model curves drawn from x = A sin(2πt/T) (no measured data)."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, COLD_LIGHT, GLASS, IRON, METAL_EDGE, ALUMINIUM,
                    GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, HEAT, n, fi)
import herolib as H

PI = math.pi
# the simulated measurement of the fitting figure: the same Park–Miller noise of ±0,25 cm as the simulation
M, NOISE = 2147483647, 0.25


def simulated(A, T, tmax, seed, step=0.1):
    s, pts = seed, []
    for i in range(int(round(tmax / step)) + 1):
        s = (s * 16807) % M; t = i * step
        pts.append((t, A * math.sin(2 * PI * t / T) + (s / M - 0.5) * 2 * NOISE))
    return pts


def darrow(f, x1, y1, x2, y2, color=INK, w=2, head=11):
    """A double-headed dimension arrow between two points (filled heads)."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    f.arrow(mx, my, x1, y1, color, w, head)
    f.arrow(mx, my, x2, y2, color, w, head)


def spring(f, x, y0, y1, turns=9, width=26, color=IRON, w=3):
    """A coil spring drawn as a zigzag from (x, y0) down to (x, y1), with short straight ends."""
    end = 8
    pts = [(x, y0), (x, y0 + end)]
    L = (y1 - y0) - 2 * end
    for k in range(2 * turns):
        pts.append((x + (width / 2 if k % 2 == 0 else -width / 2), y0 + end + L * (k + 0.5) / (2 * turns)))
    pts += [(x, y1 - end), (x, y1)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=color, w=w, extra='stroke-linecap="round"')


def weight(f, x, yc, ghost=False, wd=56, ht=40):
    """An iron weight with a hook, centred at (x, yc); a ghost is a dashed outline of an earlier or later position."""
    if ghost:
        f.rect(x - wd / 2, yc - ht / 2, wd, ht, WHITE, MUTED, 2, 5, extra='stroke-dasharray="6 5" fill-opacity="0.6"')
        return
    f.rect(x - wd / 2, yc - ht / 2, wd, ht, IRON, INK, 2.5, 5)
    f.rect(x - wd / 2 + 6, yc - ht / 2 + 6, wd - 12, 6, METAL_EDGE, None, 0, 3)


def hero():
    f = H.hero("fy57-hero", "Kuvitus: lapsi seisoo keinulla puistossa kesäpäivänä ja keinuu edestakaisin. Keinun kaksi "
               "ääriasentoa näkyvät haaleina katkoviivoina keinun molemmin puolin, ja keskimmäinen, alin asento on piirretty "
               "täytenä. Keinutelineen takana on koivuja ja kumpuilevia mäkiä.")
    H.sky(f, "fy57h", bottom=600)
    H.sun(f, "fy57h", 1050, 110, r=48)
    H.cloud(f, 230, 100, 1.0); H.cloud(f, 820, 70, 0.8)
    H.hills(f, "fy57h", 340, [GOOD_LIGHT], amp=34, seed=5)
    f.rect(0, 400, 1200, 200, H.grad(f, "fy57h-grass", GOOD_LIGHT, GOOD, y1=400, y2=600))
    for x, h in ((90, 240), (180, 180), (1100, 250), (1020, 175)):
        H.birch(f, x, 440, h)
    # worn sand under the swing
    f.add(f'<ellipse cx="600" cy="520" rx="330" ry="46" fill="{SAND_LIGHT}"/>')
    # the frame: two A-shaped legs and the top bar
    top_y, px = 96, 600
    for lx in (360, 840):
        f.line(lx, top_y, lx - 70, 520, IRON, 12, cap="round"); f.line(lx, top_y, lx + 70, 520, IRON, 12, cap="round")
    f.line(340, top_y, 860, top_y, IRON, 16, cap="round")
    f.line(340, top_y - 8, 860, top_y - 8, METAL_EDGE, 3, cap="round")
    L = 360

    def swing(deg, ghost):
        a = math.radians(deg)
        sx, sy = px + L * math.sin(a), top_y + L * math.cos(a)
        col = MUTED if ghost else INK
        extra = 'stroke-dasharray="12 10"' if ghost else ""
        for dx in (-44, 44):
            f.path(f"M{n(px + dx)},{top_y} L{n(sx + dx * math.cos(a))},{n(sy - dx * math.sin(a))}", stroke=col, w=4, extra=extra)
        # the seat, tilted with the ropes
        c, s = math.cos(a), math.sin(a)
        pts = [(-56, -6), (56, -6), (56, 10), (-56, 10)]
        d = "M" + " L".join(f"{n(sx + u * c + v * s)},{n(sy - u * s + v * c)}" for u, v in pts) + " Z"
        if ghost: f.path(d, WHITE, MUTED, 3, extra='stroke-dasharray="10 8" fill-opacity="0.5"')
        else: f.path(d, SAND_DARK, INK, 3)
        return sx, sy
    swing(-34, True); swing(34, True)
    sx, sy = swing(0, False)
    H.person(f, sx, sy - 6, shirt=COLD, sc=0.62, arms="down")
    # light swooshes along the path of the seat
    for d0, d1 in ((-30, -8), (8, 30)):
        pts = [(px + (L + 34) * math.sin(math.radians(d)), top_y + (L + 34) * math.cos(math.radians(d))) for d in range(d0, d1 + 1, 2)]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=WHITE, w=6, extra='stroke-linecap="round" stroke-opacity="0.85"')
    return f.svg()


def osat():
    f = Fig("fy57-osat", 360, "Kaavakuva kahdesta värähtelijästä. Vasemmalla punnus riippuu jousesta. Täytenä piirretty punnus "
            "on tasapainoasemassa, jonka kohdalla on vaakasuora katkoviiva x = 0, ja katkoviivoin piirretyt punnukset ovat "
            "ylimmässä ja alimmassa asemassa. Tasapainoasemasta kumpaankin ääriasemaan on yhtä pitkä nuoli, jonka merkintä on A. "
            "Pystysuora akseli x osoittaa ylöspäin. Oikealla heiluri: punnus riippuu langasta, ja tasapainoasemassa lanka on "
            "pystysuorassa katkoviivan x = 0 kohdalla. Katkoviivoin piirretyt punnukset ovat ääriasemissa vasemmalla ja oikealla, "
            "ja tasapainoasemasta kumpaankin on vaakasuora nuoli A.")
    # left: a weight on a spring, x up
    cx, yeq, amp = 120, 190, 80
    f.rect(52, 18, 136, 12, METAL_EDGE, INK, 2, 2)
    for k in range(8): f.line(58 + 16 * k, 18, 50 + 16 * k, 8, INK, 1.5)
    spring(f, cx, 30, yeq - 20)
    weight(f, cx, yeq - amp, ghost=True); weight(f, cx, yeq + amp, ghost=True)
    weight(f, cx, yeq)
    f.line(30, yeq, 240, yeq, MUTED, 1.5, "7 6")
    f.tex(244, yeq, r"x = 0", "start")
    for y2 in (yeq - amp, yeq + amp):
        f.line(152, y2, 196, y2, MUTED, 1.5)
        darrow(f, 184, yeq, 184, y2)
    f.tex(196, yeq - amp / 2, "A", "start"); f.tex(196, yeq + amp / 2, "A", "start")
    f.arrow(40, 300, 40, 60, INK, 2.5, 13)
    f.tex(52, 64, "x", "start")
    f.line(316, 30, 316, 340, RULE, 2, "6 6")
    # right: a pendulum, x horizontal
    pvx, pvy, Lp, th = 452, 40, 210, math.radians(21)
    f.rect(pvx - 46, pvy - 14, 92, 12, METAL_EDGE, INK, 2, 2)
    f.line(pvx, pvy, pvx, 300, MUTED, 1.5, "7 6")
    for sgn in (-1, 1):
        bx, by = pvx + sgn * Lp * math.sin(th), pvy + Lp * math.cos(th)
        f.line(pvx, pvy, bx, by, MUTED, 2, "6 5")
        f.add(f'<circle cx="{n(bx)}" cy="{n(by)}" r="17" fill="{WHITE}" fill-opacity="0.6" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 5"/>')
    f.line(pvx, pvy, pvx, pvy + Lp, INK, 2.5)
    f.circle(pvx, pvy + Lp, 18, IRON, INK, 2.5)
    f.circle(pvx, pvy, 5, INK)
    dx = Lp * math.sin(th); yb = 290
    for sgn in (-1, 1):
        f.line(pvx + sgn * dx, pvy + Lp * math.cos(th) + 20, pvx + sgn * dx, yb + 8, MUTED, 1.5)
        darrow(f, pvx, yb, pvx + sgn * dx, yb)
        f.tex(pvx + sgn * dx / 2, yb + 22, "A", "middle")
    f.tex(pvx, 334, r"x = 0", "middle")
    return f.svg()


def sine_graph(fid, label, A, T, tmax, tstep, tlabel, ymax, ystep, ylabel_step, x_off=0, points=None, color=INK,
               height=330, marks=None, tend=None):
    """A (t, x) graph with the time axis at the bottom and the equilibrium x = 0 as a dashed rule; ticks every tstep
    (numbers every tlabel) and every ystep (numbers every ylabel_step). The curve is x = A sin(2πt/T)."""
    f = Fig(fid, height, label)
    xt = [round(k * tstep, 6) for k in range(1, int(round(tmax / tstep)) + 1)]
    yt = [round(-ymax + k * ystep, 6) for k in range(int(round(2 * ymax / ystep)) + 1)]
    lab = lambda v: fi(v) if abs(v / tlabel - round(v / tlabel)) < 1e-6 else ""
    ylab = lambda v: fi(v) if abs(v / ylabel_step - round(v / ylabel_step)) < 1e-6 else ""
    ax = Axes(f, (86 + x_off, height - 52), (486, 62), x=(0, tmax), y=(-ymax, ymax), xticks=xt, yticks=yt,
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{cm})", xfmt=lab, yfmt=ylab, origin_label=False)
    f.tex(ax.X(0), height - 52 + 24, "0", "middle")
    f.line(ax.X(0), ax.Y(0), ax.X(tmax), ax.Y(0), MUTED, 1.5, "7 6")
    if points:
        if A: ax.curve(lambda t: A * math.sin(2 * PI * t / T), 0, tmax, COLD, 3, steps=240)
        for t, x in points: ax.point(t, x, INK, 5)
    else:
        ax.curve(lambda t: A * math.sin(2 * PI * t / T), 0, tend or tmax, color, 3, steps=240)
    if marks: marks(f, ax)
    return f.svg()


def kuvaaja():
    def marks(f, ax):
        A, T = 4.0, 0.80
        # T between two successive maxima, and between two successive upward crossings of x = 0
        y_top = ax.Y(A) - 16
        f.line(ax.X(0.2), ax.Y(A) - 4, ax.X(0.2), y_top - 8, MUTED, 1.5); f.line(ax.X(1.0), ax.Y(A) - 4, ax.X(1.0), y_top - 8, MUTED, 1.5)
        darrow(f, ax.X(0.2), y_top, ax.X(1.0), y_top)
        f.tex(ax.X(0.6), y_top - 2, "T", "middle", bg=True)
        y_bot = ax.Y(-A) + 14
        f.line(ax.X(0.8), ax.Y(0), ax.X(0.8), y_bot + 8, MUTED, 1.5); f.line(ax.X(1.6), ax.Y(0), ax.X(1.6), y_bot + 8, MUTED, 1.5)
        darrow(f, ax.X(0.8), y_bot, ax.X(1.6), y_bot)
        f.tex(ax.X(1.2), y_bot + 2, "T", "middle", bg=True)
        # the amplitude from the equilibrium to the maximum at t = 1,8 s
        xa = ax.X(1.8)
        darrow(f, xa, ax.Y(0), xa, ax.Y(A))
        f.tex(xa + 14, ax.Y(A / 5), "A", "start", bg=True)
    return sine_graph("fy57-kuv", "Kuvaaja mittakaavassa: punnuksen poikkeama x senttimetreinä ajan t funktiona nollasta "
                      "kahteen sekuntiin. Käyrä on sinikäyrä, joka nousee nollasta ylimpään arvoon 4 cm hetkellä 0,2 s, laskee "
                      "alimpaan arvoon miinus 4 cm hetkellä 0,6 s ja toistuu samanlaisena. Ylhäällä kaksipäinen nuoli T kahden "
                      "peräkkäisen huipun välillä 0,2 s:sta 1,0 s:iin, alhaalla toinen nuoli T kahden peräkkäisen ylöspäin "
                      "tapahtuvan tasapainoaseman ohituksen välillä 0,8 s:sta 1,6 s:iin. Oikealla pystysuora nuoli A "
                      "tasapainoasemasta huippuun.", 4.0, 0.80, 2.0, 0.2, 0.4, 6.0, 1.0, 2.0, marks=marks, height=360, tend=1.98)


def ympyra():
    f = Fig("fy57-ymp", 350, "Kaavakuva: vasemmalla piste kiertää vastapäivään ympyrää, jonka säde on A. Piste on kiertynyt "
            "vaakasuorasta säteestä kulman 2 pii t per T. Pisteen korkeus ympyrän keskipisteen tasosta on x. Vaakasuora "
            "katkoviiva vie saman korkeuden oikealle kuvaajaan, jossa x on piirretty ajan t funktiona yhden kierrosajan T "
            "ajalta: sinikäyrä saa arvon A hetkellä neljäsosa T, arvon nolla hetkellä puoli T, arvon miinus A hetkellä kolme "
            "neljäsosaa T ja taas nollan hetkellä T.")
    cx, cy, R, deg = 136, 176, 108, 125
    f.circle(cx, cy, R, "none", INK, 2.5)
    f.line(cx - R - 10, cy, cx + R + 10, cy, MUTED, 1.5, "6 5")
    a = math.radians(deg); px, py = cx + R * math.cos(a), cy - R * math.sin(a)
    f.line(cx, cy, px, py, INK, 2)
    f.circle(cx, cy, 4, INK)
    # the turned angle (from the horizontal radius) and its label inside the circle, clear of the outline and the arc
    arc = [(cx + 26 * math.cos(math.radians(d)), cy - 26 * math.sin(math.radians(d))) for d in range(0, deg + 1, 5)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in arc), stroke=INK, w=2)
    f.tex(cx + 58 * math.cos(math.radians(34)), cy - 58 * math.sin(math.radians(34)), r"2\pi t/T", "middle", w=70)
    # A beside the radius (on the side of the turned angle), 24 units from its midpoint
    f.tex(cx + 0.5 * R * math.cos(a) + 24 * math.sin(a), cy - 0.5 * R * math.sin(a) + 24 * math.cos(a), "A", "middle")
    # the height x of the point; x stands right of the vertical segment
    f.line(px, cy, px, py, INK, 4)
    f.tex(px + 12, cy - 34, "x", "start")
    f.circle(px, py, 8, INK)
    # the turning direction
    ar = [(cx + (R + 12) * math.cos(math.radians(d)), cy - (R + 12) * math.sin(math.radians(d))) for d in range(138, 173, 4)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in ar), stroke=MUTED, w=2.5)
    ex, ey = ar[-1]; b = math.radians(170); ux, uy = -math.sin(b), -math.cos(b)
    f.path(f"M{n(ex + 12 * ux)},{n(ey + 12 * uy)} L{n(ex - 6 * uy - 2 * ux)},{n(ey + 6 * ux - 2 * uy)} L{n(ex + 6 * uy - 2 * ux)},{n(ey - 6 * ux - 2 * uy)} Z", MUTED)
    # the graph of x against t over one period, at the same height scale
    gx0, gx1 = 286, 516
    X = lambda u: gx0 + u * (gx1 - gx0)
    Y = lambda v: cy - v * R
    for u in (0.25, 0.5, 0.75, 1.0):
        f.line(X(u), cy - R - 14, X(u), cy + R + 14, RULE_LIGHT, 1.5)
    for v in (1, -1):
        f.line(gx0, Y(v), gx1, Y(v), RULE_LIGHT, 1.5)
        f.line(gx0 - 7, Y(v), gx0, Y(v), INK, 2)
    f.tex(gx0 - 12, Y(1), "A", "end"); f.tex(gx0 - 12, Y(-1), "-A", "end")
    f.arrow(gx0 - 1, cy, gx1 + 30, cy, INK, 2.5, 13)
    f.arrow(gx0, cy + R + 26, gx0, cy - R - 34, INK, 2.5, 13)
    f.tex(gx1 + 36, cy, "t", "start")
    f.tex(gx0 + 10, cy - R - 38, "x", "start")
    for u, s in ((0.25, r"\tfrac{T}{4}"), (0.5, r"\tfrac{T}{2}"), (0.75, r"\tfrac{3T}{4}"), (1.0, "T")):
        f.tex(X(u), cy + R + 40, s, "middle")
    pts = [(X(k / 120), Y(math.sin(2 * PI * k / 120))) for k in range(121)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=3)
    u0 = deg / 360
    f.line(px + 10, py, X(u0) - 8, py, MUTED, 1.5, "6 5")
    f.circle(X(u0), py, 7, INK, WHITE, 2)
    return f.svg()


def sovitus():
    pts = simulated(3.0, 1.20, 4.0, seed=53)

    def marks(f, ax):
        y = ax.Y(-4.2)
        for t in (0, 3.6): f.line(ax.X(t), ax.Y(0), ax.X(t), y - 8, MUTED, 1.5)
        darrow(f, ax.X(0), y, ax.X(3.6), y)
        f.tex(ax.X(1.8), y, r"3T = 3{,}6\,\text{s}", "middle", bg=True)
        xa = ax.X(3.9) + 20
        f.line(ax.X(3.3), ax.Y(3.0), xa + 8, ax.Y(3.0), MUTED, 1.5, "6 5")
        darrow(f, xa, ax.Y(0), xa, ax.Y(3.0))
        f.tex(xa + 10, ax.Y(1.5), "A", "start")
    return sine_graph("fy57-sov", "Kuvaaja mittakaavassa: simuloidut mittauspisteet, punnuksen poikkeama x senttimetreinä ajan t "
                      "funktiona nollasta neljään sekuntiin kymmenesosasekunnin välein. Pisteet vaihtelevat noin plus ja miinus "
                      "kolmen senttimetrin välillä, ja niiden läpi on piirretty sininen sinikäyrä. Alhaalla kaksipäinen nuoli "
                      "kolmen täyden värähdyksen ajalle nollasta 3,6 sekuntiin, merkintä 3T on 3,6 s. Oikealla pystysuora nuoli "
                      "A tasapainoasemasta käyrän huipun tasolle 3 cm.", 3.0, 1.20, 4.0, 0.4, 1.2, 5.0, 1.0, 2.0,
                      points=pts, height=360, marks=marks)


# Task figures: model curves without marks; the description lists what is drawn, not the answer of the task
def l1_kuvaaja():
    return sine_graph("fy57-l1", "Kuvaaja: punnuksen poikkeama x senttimetreinä ajan t funktiona nollasta kolmeen sekuntiin. "
                      "Pystyakselilla on apuviivat puolen senttimetrin välein ja lukuarvot kokonaisina senttimetreinä miinus "
                      "kolmesta kolmeen, aika-akselilla apuviivat 0,2 sekunnin välein. Käyrä on sinikäyrä, joka lähtee nollasta "
                      "ylöspäin ja värähtelee tasapainoaseman molemmin puolin. Ensimmäinen huippu on hetkellä 0,3 s ja se osuu "
                      "apuviivalle, joka on kahden ja kolmen senttimetrin puolivälissä; pohjat ovat samalla etäisyydellä "
                      "tasapainoaseman alapuolella.", 2.5, 1.2, 3.0, 0.2, 0.6, 3.0, 0.5,
                      1.0)


def l2_kuvaaja():
    return sine_graph("fy57-l2", "Kuvaaja: ilmatyynyradan vaunun poikkeama x senttimetreinä ajan t funktiona nollasta kolmeen sekuntiin, "
                      "aika-akselilla apuviivat 0,25 sekunnin välein ja lukuarvot puolen sekunnin välein. Käyrä on sinikäyrä, joka "
                      "lähtee nollasta ylöspäin ja värähtelee koko ajan samanlaisena tasapainoaseman molemmin puolin. Huiput osuvat "
                      "apuviivalle 3 cm ja pohjat apuviivalle miinus 3 cm, ja käyrä leikkaa tasapainoaseman katkoviivan "
                      "jokaisella aika-akselin apuviivalla.",
                      3.0, 0.50, 3.0, 0.25, 0.5, 4.0, 1.0, 2.0)


def tarkistus_kuvaaja():
    return sine_graph("fy57-tk", "Kuvaaja: heilurin punnuksen vaakasuora poikkeama x senttimetreinä ajan t funktiona nollasta "
                      "5,4 sekuntiin, aika-akselilla apuviivat ja lukuarvot 0,9 sekunnin välein. Käyrä on sinikäyrä, joka lähtee "
                      "nollasta ylöspäin, saa suurimman arvonsa 5 cm ja pienimmän arvonsa miinus 5 cm ja leikkaa tasapainoaseman "
                      "katkoviivan jokaisella aika-akselin apuviivalla.", 5.0, 1.8, 5.4, 0.9, 0.9, 6.0, 1.0, 2.0)


FIGURES = {"hero": hero, "osat": osat, "kuvaaja": kuvaaja, "ympyra": ympyra, "sovitus": sovitus,
           "l1-kuvaaja": l1_kuvaaja, "l2-kuvaaja": l2_kuvaaja, "tarkistus-kuvaaja": tarkistus_kuvaaja}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "osat": "reveals: the amplitude is measured from the equilibrium to one extreme, for a spring and a pendulum",
    "kuvaaja": "reveals: T between successive maxima or upward crossings and A from x = 0 to a peak (A = 4,0 cm, T = 0,80 s)",
    "ympyra": "reveals: x = A sin(2πt/T) as the height of a point in uniform circular motion, values at T/4, T/2, 3T/4, T",
    "sovitus": "reveals: reading 3T and A off simulated points with a fitted sine (A = 3,0 cm, T = 1,20 s)",
    "l1-kuvaaja": "safe: a model sine x(t), 0–3 s, half-centimetre gridlines, no marks (A and T are to be read)",
    "l2-kuvaaja": "safe: a model sine x(t), 0–3 s, several periods, no marks (A and T are to be read)",
    "tarkistus-kuvaaja": "safe: a model sine x(t) of a pendulum, 0–5,4 s, gridlines every 0,9 s, no marks (T to be read)",
}
