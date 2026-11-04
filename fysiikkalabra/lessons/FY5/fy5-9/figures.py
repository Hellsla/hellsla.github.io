"""Figures of this lesson (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy5-9` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND, SAND_LIGHT, SAND_DARK, GRAIN, ALUMINIUM,
                    METAL_EDGE, IRON, COPPER, GOOD, GOOD_LIGHT, COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, ICE, PAPER, n)
from fbd import FBD, FORCE, VELOCITY, ACCEL, open_head
import herolib as H

EK, EP = "#2b8a3e", "#7048e8"          # kinetic energy green, potential energy violet (as in the simulation)


def thin(f, x1, y1, x2, y2, col):
    """A velocity or acceleration arrow: thin, open head (fbd.py convention)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.line(x1, y1, x2 - ux * 2, y2 - uy * 2, col, 2.5)
    open_head(f, x2, y2, ux, uy, col, 2.5)


def spring_row(f, y, xb, xeq, s_px, wall=40):
    """A wall, a zigzag spring and a block whose centre is at xb, on a frictionless track at height y (bottom of block)."""
    f.rect(wall - 16, y - 70, 16, 70, IRON, INK, 2)
    f.line(wall - 20, y, 576, y, INK, 2.5)
    f.rect(wall, y, 536, 6, ALUMINIUM)
    bw, bh = 52, 44
    left = xb - bw / 2
    y0 = y - bh / 2
    pts = [(wall, y0), (wall + 8, y0)]
    L = left - wall - 16
    for i in range(14):
        pts.append((wall + 8 + L * (i + 0.5) / 14, y0 + (-10 if i % 2 == 0 else 10)))
    pts += [(left - 8, y0), (left, y0)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=MUTED, w=2.5)
    f.rect(left, y - bh, bw, bh, "url(#fy59-wood)", INK, 2.5, 4)
    return left, y - bh, bw


def spring():
    """Ydinajatus: the block at +A, at the equilibrium and at −A, with the spring force, the acceleration and the velocity."""
    f = Fig("fy59-jousi", 400, "Kaavakuva, ei mittakaavassa: kitkattomalla vaakasuoralla alustalla oleva kappale on kiinnitetty jousella "
            "seinään. Kolme hetkeä allekkain. Ylhäällä kappale on ääriasennossa x = A tasapainoaseman oikealla puolella: "
            "jousivoima ja kiihtyvyys osoittavat vasemmalle kohti tasapainoasemaa, nopeus on nolla. Keskellä kappale ohittaa "
            "tasapainoaseman x = 0 vasemmalle: voima ja kiihtyvyys ovat nolla ja nopeus on suurimmillaan. Alhaalla kappale on "
            "ääriasennossa x = −A: voima ja kiihtyvyys osoittavat oikealle, nopeus on nolla.")
    f.defs_add(f'<linearGradient id="fy59-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_DARK}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    xeq, A = 300, 110
    f.line(xeq, 14, xeq, 364, MUTED, 1.5, "6 5")
    f.tex(xeq, 382, "x = 0", "middle", MUTED)
    rows = [(118, xeq + A, r"x = A", "ääri"), (234, xeq, r"x = 0", "tasa"), (350, xeq - A, r"x = -A", "ääri2")]
    for y, xb, name, kind in rows:
        left, top, bw = spring_row(f, y, xb, xeq, A)
        if kind != "tasa":
            f.tex(xb, y + 26, name, "middle")
        if kind == "ääri":
            f.arrow(xb, top - 14, xb - 92, top - 14, FORCE, 4, 16)
            f.tex(xb - 100, top - 14, r"\overline{F}", "end", FORCE)
            thin(f, xb, top - 44, xb - 92, top - 44, ACCEL)
            f.tex(xb - 100, top - 44, r"\overline{a}", "end", ACCEL)
            f.tex(xb + 34, y - 22, r"v = 0", "start")
        elif kind == "tasa":
            thin(f, xb, top - 14, xb - 110, top - 14, VELOCITY)
            f.tex(xb - 118, top - 14, r"\overline{v}", "end", VELOCITY)
            f.tex(xb + 34, y - 22, r"F = 0,\ a = 0", "start")
        else:
            f.arrow(xb, top - 14, xb + 92, top - 14, FORCE, 4, 16)
            f.tex(xb + 100, top - 14, r"\overline{F}", "start", FORCE)
            thin(f, xb, top - 44, xb + 92, top - 44, ACCEL)
            f.tex(xb + 100, top - 44, r"\overline{a}", "start", ACCEL)
            f.tex(xb - 40, top - 14, r"v = 0", "end")
    return f.svg()


def xt():
    """Ydinajatus: a schematic x(t) graph of harmonic oscillation with the amplitude and the period marked."""
    f = Fig("fy59-xt", 350, "Kaavakuva: harmonisen värähtelyn paikka x ajan t funktiona on siniaallon muotoinen käyrä. Käyrä "
            "alkaa ääriasennosta x = A, käy ääriasennossa x = −A ja palaa ääriasentoon A. Amplitudi A on merkitty "
            "tasapainoasemasta x = 0 käyrän huippuun, ja jaksonaika T kahden peräkkäisen huipun väliin. Kuvaajassa on kaksi "
            "ja puoli jaksoa.")
    ax = Axes(f, (80, 310), (470, 72), x=(0, 2.6), y=(-1.25, 1.25), xticks=[], yticks=[], xlabel=r"t", ylabel=r"x",
              grid=False, origin_label=False, x_at=0)
    for yy in (-1, 1):
        f.line(80, ax.Y(yy), 470, ax.Y(yy), RULE_LIGHT, 1.5)
    ax.curve(lambda t: math.cos(2 * math.pi * t), 0, 2.5, INK, 3)
    f.tex(72, ax.Y(1), "A", "end"); f.tex(72, ax.Y(-1), "-A", "end")
    # amplitude bracket at t = 1 (a crest)
    xa = ax.X(2.0)
    f.arrow(xa, ax.Y(0) - 2, xa, ax.Y(1) + 2, INK, 2, 11)
    f.tex(xa + 12, (ax.Y(0) + ax.Y(1)) / 2, "A", "start")
    # period between the crests at t = 0 and t = 1
    y = ax.Y(1) - 18
    f.line(ax.X(0) + 2, y, ax.X(1), y, INK, 2)
    for t in (0, 1): f.line(ax.X(t) + (2 if t == 0 else 0), y - 8, ax.X(t) + (2 if t == 0 else 0), y + 8, INK, 2)
    f.tex((ax.X(0) + ax.X(1)) / 2, y - 18, "T", "middle")
    for t in (0, 1, 2): f.line(ax.X(t), ax.Y(1), ax.X(t), ax.Y(1) + 0.1, MUTED, 1.5)
    return f.svg()


def pendulum():
    """Kaava: the force diagram of a pendulum bob at its extreme position α: weight, string tension, and the weight's
    components along the path and along the string. G = 1 unit, α = 35°, v = 0, so the net force is mg sin α along the path."""
    al = math.radians(35)
    f = Fig("fy59-heiluri", 410, "Voimakuvio, heilurin punnus ääriasennossaan, kun lanka on kulmassa α pystysuoraan nähden ja nopeus "
            "on nolla. Lanka lähtee ylhäällä olevasta kiinnityskohdasta, ja punnus on piirretty langan suuntaisena "
            "suorakulmiona. Paino G osoittaa keskipisteestä suoraan alas. Langan jännitysvoima S vaikuttaa punnuksen "
            "yläpinnasta langan suuntaisesti kohti kiinnityskohtaa. Katkoviivoin on piirretty painon komponentit: G n langan "
            "suuntaisesti poispäin kiinnityskohdasta ja G t radan tangentin suuntaisesti kohti tasapainoasemaa. Jännitysvoima on "
            "yhtä suuri kuin G n, joten jäljelle jää palauttava komponentti G t, jonka suuruus on G sin α.")
    px, py, L = 230, 40, 230
    bx, by = px + L * math.sin(al), py + L * math.cos(al)
    f.rect(px - 70, py - 16, 140, 16, IRON, INK, 2)
    f.line(px, py, px, py + L + 50, MUTED, 1.5, "6 5")
    # the path arc and the angle
    a0 = math.radians(40)
    f.path(f"M{n(px - L * math.sin(a0))},{n(py + L * math.cos(a0))} A{L},{L} 0 0 0 {n(px + L * math.sin(a0))},{n(py + L * math.cos(a0))}",
           stroke=MUTED, w=1.5, extra='stroke-dasharray="6 5"')
    r = 62
    f.path(f"M{px},{py + r} A{r},{r} 0 0 0 {n(px + r * math.sin(al))},{n(py + r * math.cos(al))}", stroke=INK, w=2)
    f.tex(px + 18, py + r + 16, r"\alpha", "middle")
    h = 44
    tx, ty = bx - (h / 2) * math.sin(al), by - (h / 2) * math.cos(al)        # top face centre, where the string pulls
    f.line(px, py, tx, ty, INK, 2.5)
    f.circle(px, py, 4, INK)
    f.tex(px + 75 * math.sin(al) + 14, py + 75 * math.cos(al), "l", "start")
    G, sc = 1.0, 120
    d = FBD(f, scale=sc, body=(bx, by, 40, h, 35), a_dir=(-math.cos(al), -math.sin(al)))
    d.force("G", (0, -G), (bx, by), kind="gravity", lab=(22, -6))
    d.force("S", (-G * math.cos(al) * math.sin(al), G * math.cos(al) * math.cos(al)), (tx, ty), kind="tension",
            rope=(-math.sin(al), math.cos(al)), lab=(26, 2))
    d.component("G_t", "G", (-math.cos(al), -math.sin(al)), lab=(-28, 8), tex=r"\overline{G}_\text{t}")
    d.component("G_n", "G", (math.sin(al), -math.cos(al)), lab=(28, 4), tex=r"\overline{G}_\text{n}")
    d.draw()
    f.tex(450, 392, r"G_\text{t} = G \sin\alpha", "middle", FORCE)
    return f.svg()


def energy_graph():
    """Kaava: E_p = ½kx² and the constant E = ½kA² for k = 20 N/m, A = 0,10 m; at x = 5 cm E_p = 0,025 J and E_k = 0,075 J."""
    f = Fig("fy59-energia", 360, "Kuvaaja mittakaavassa, kun jousivakio on 20 N/m ja amplitudi 10 cm: jousen potentiaalienergia E p on "
            "paraabeli, joka on nolla tasapainoasemassa x = 0 ja kasvaa arvoon 0,10 J ääriasennoissa x = −10 cm ja x = 10 cm. "
            "Vaakasuora viiva korkeudella 0,10 J on värähtelyn kokonaisenergia E. Kohdassa x = 5 cm on pystysuora jana, jonka "
            "alaosa nollasta 0,025 J:een on potentiaalienergia ja yläosa 0,025 J:sta 0,10 J:een liike-energia E k.")
    x0, x1, y0, y1 = 60, 440, 300, 60                     # plot area: x from −10 to 10 cm, E from 0 to 0,12 J
    X = lambda v: x0 + (v + 10) / 20 * (x1 - x0)
    Y = lambda e: y0 - e / 0.12 * (y0 - y1)
    for e in (0.02, 0.04, 0.06, 0.08, 0.10, 0.12):
        f.line(x0, Y(e), x1, Y(e), RULE_LIGHT, 1.5)
    for v in (-10, -5, 5, 10):
        f.line(X(v), y0, X(v), y1, RULE_LIGHT, 1.5)
    f.arrow(x0 - 1, y0, x1 + 26, y0, INK, 2.5, 13)
    f.arrow(X(0), y0 + 1, X(0), y1 - 26, INK, 2.5, 13)
    for v in (-10, -5, 5, 10):
        f.line(X(v), y0, X(v), y0 + 7, INK, 2)
        f.tex(X(v), y0 + 24, fi(v), "middle")
    f.tex(X(0), y0 + 24, "0", "middle")
    for e in (0.04, 0.08, 0.12):
        f.line(X(0) - 7, Y(e), X(0), Y(e), INK, 2)
        f.tex(X(0) - 12, Y(e), fi(e, 2), "end", bg=True)
    f.tex(x1 + 32, y0, r"x\ (\text{cm})", "start")
    f.tex(X(0) + 12, y1 - 32, r"E\ (\text{J})", "start")
    pts = [(-10 + 20 * i / 120, 0.5 * 20 * ((-10 + 20 * i / 120) / 100) ** 2) for i in range(121)]
    f.add('<polyline points="' + " ".join(f"{n(X(a))},{n(Y(b))}" for a, b in pts) + f'" fill="none" stroke="{EP}" stroke-width="3" stroke-linejoin="round"/>')
    f.line(X(-10), Y(0.10), X(10), Y(0.10), INK, 3)
    f.tex(X(-10) - 8, Y(0.10), "E", "end")
    f.tex(X(-5), Y(0.062), r"E_\text{p}", "middle", EP)
    # the split at x = 5 cm
    xs = X(5)
    f.line(xs, y0, xs, Y(0.025), EP, 6)
    f.line(xs, Y(0.025), xs, Y(0.10), EK, 6)
    f.circle(xs, Y(0.025), 6.5, EP, WHITE, 2)
    f.tex(xs + 14, Y(0.0125) - 2, r"E_\text{p}", "start", EP)
    f.tex(xs + 14, Y(0.0625), r"E_\text{k}", "start", EK)
    return f.svg()


def damped():
    """Vaimeneminen: a schematic damped x(t) curve inside its shrinking envelope."""
    f = Fig("fy59-vaimeneva", 320, "Kaavakuva: vaimenevan värähtelyn paikka x ajan t funktiona. Käyrä heilahtelee tasapainoaseman "
            "molemmin puolin, ja sen huiput pienenevät tasaisesti. Katkoviivat huippujen kautta näyttävät, miten amplitudi "
            "pienenee. Peräkkäisten huippujen väli eli jaksonaika pysyy lähes samana.")
    ax = Axes(f, (80, 290), (470, 72), x=(0, 5.2), y=(-1.2, 1.2), xticks=[], yticks=[], xlabel="t", ylabel="x",
              grid=False, origin_label=False, x_at=0)
    b = 0.35
    ax.curve(lambda t: math.exp(-b * t), 0, 5, MUTED, 1.5, dash="6 5")
    ax.curve(lambda t: -math.exp(-b * t), 0, 5, MUTED, 1.5, dash="6 5")
    ax.curve(lambda t: math.exp(-b * t) * math.cos(2 * math.pi * t), 0, 5, INK, 3, steps=240)
    return f.svg()


def graph_task():
    """Task figure (Tarkista osaamisesi): x(t) of a spring oscillator, maxima at 0, 0,40 and 0,80 s, amplitude 3,0 cm."""
    f = Fig("fy59-kuvaaja-k", 350, "Kuvaaja mittakaavassa: jousen varassa värähtelevän kappaleen paikka x senttimetreinä ajan t funktiona "
            "sekunteina nollasta 1,0 sekuntiin. Käyrä on siniaallon muotoinen, ja sen huiput ovat kohdassa x = 3,0 cm hetkillä "
            "0 s, 0,40 s ja 0,80 s ja pohjat kohdassa x = −3,0 cm hetkillä 0,20 s ja 0,60 s. Ruudukon väli on 0,1 s ja 1 cm.")
    ax = Axes(f, (90, 310), (470, 72), x=(0, 1.0), y=(-4, 4), xticks=[0.1 * i for i in range(1, 11)], yticks=[-4, -3, -2, -1, 1, 2, 3, 4],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{cm})", xfmt=lambda v: fi(v, 1) if round(v * 10) % 2 == 0 else "",
              yfmt=lambda v: fi(v) if v % 2 == 1 or v % 2 == -1 else "", origin_label=False, x_at=0)
    ax.curve(lambda t: 3 * math.cos(2 * math.pi * t / 0.40), 0, 1.0, INK, 3, steps=240)
    return f.svg()


def hero():
    """Two oscillators of one home, each at its own pace: a pendulum clock (the long pendulum swings slowly behind the
    glass of its door) and a baby bouncing in a door bouncer hanging from a coil spring clamped to the door frame. One
    scale (about 2,1 px per cm): the clock and the door are 2 m tall. No swing: that is fy5-7's picture."""
    f = H.hero("fy59-hero", "Kuvitus: olohuone, jossa on kaksi värähtelijää. Vasemmalla seisoo kaappikello, jonka lasioven "
               "takana pitkä heiluri on heilahtanut sivuun. Oikealla oviaukon yläkarmiin on kiinnitetty kierrejousi, jonka "
               "varassa vauva istuu hyppykiikussa varpaat lattiaa vasten. Taustalla on ikkuna, huonekasvi ja taulu, edessä "
               "oikealla nojatuoli.")
    floor = 506
    # the wall with faint stripes, the skirting board and the wooden floor
    f.rect(0, 0, 1200, floor, H.grad(f, "fy59h-wall", PAPER, SAND_LIGHT, y1=0, y2=floor))
    for x in range(30, 1200, 60):
        f.rect(x, 0, 24, floor, SAND_LIGHT, extra='fill-opacity="0.35"')
    f.rect(0, floor, 1200, 94, H.grad(f, "fy59h-floor", SAND, GRAIN, y1=floor, y2=600))
    for k, y in enumerate((532, 562, 592)):
        f.line(0, y, 1200, y, GRAIN, 1.5)
        for j in range(5):
            x = 80 + j * 260 + (k % 2) * 130
            f.line(x, y - (26 if k else 26), x, y, GRAIN, 1.5)
    f.rect(0, floor - 16, 1200, 16, WHITE, INK, 2)
    # the window on the left and a plant under it
    H.window(f, 64, 120, 190, 220, "fy59h-win")
    f.rect(52, 106, 214, 16, RULE, INK, 2.5, 3)
    f.path(f"M150,{floor - 16} L132,{floor - 96} H208 L190,{floor - 16} Z", COPPER, INK, 2.5)
    for k, (dx, h, s) in enumerate(((-34, 120, -1), (-8, 160, -1), (14, 150, 1), (38, 110, 1))):
        f.path(f"M170,{floor - 96} Q{170 + dx * 0.4},{floor - 96 - h * 0.6} {170 + dx + s * 18},{floor - 96 - h} "
               f"Q{170 + dx * 1.3},{floor - 96 - h * 0.5} 170,{floor - 96} Z", GOOD, INK, 2)
    f.add(f'<ellipse cx="560" cy="{floor + 50}" rx="250" ry="24" fill="{HOT_LIGHT}" fill-opacity="0.55"/>')   # a rug

    # the pendulum clock: plinth, trunk with a glass door, hood with the dial, a pediment on top
    cx, w = 420, 124
    wood_ = H.grad(f, "fy59h-wood", COPPER, GRAIN, horizontal=True)
    f.rect(cx - w / 2 - 10, floor - 64, w + 20, 64, wood_, INK, 3, 3)
    f.rect(cx - w / 2, 220, w, floor - 64 - 220, wood_, INK, 3)
    f.rect(cx - w / 2 - 12, 92, w + 24, 128, wood_, INK, 3, 4)
    f.path(f"M{cx - w / 2 - 16},92 L{cx},50 L{cx + w / 2 + 16},92 Z", wood_, INK, 3)
    f.circle(cx, 72, 7, HEAT_LIGHT, INK, 2)
    # the dial: white face, twelve marks, two hands
    dy = 156
    f.circle(cx, dy, 48, SAND_LIGHT, INK, 2.5)
    f.circle(cx, dy, 40, WHITE, INK, 2)
    for k in range(12):
        a = k * math.pi / 6
        f.line(cx + 32 * math.sin(a), dy - 32 * math.cos(a), cx + 38 * math.sin(a), dy - 38 * math.cos(a), INK, 2.5 if k % 3 == 0 else 1.5)
    f.line(cx, dy, cx + 16, dy - 12, INK, 4, cap="round"); f.line(cx, dy, cx - 6, dy - 30, INK, 3, cap="round")
    f.circle(cx, dy, 4, INK)
    # behind the door's glass: the pendulum swung out to one side, two driving weights on chains
    gx0, gx1, gy0, gy1 = cx - w / 2 + 14, cx + w / 2 - 14, 236, floor - 82
    f.rect(gx0, gy0, gx1 - gx0, gy1 - gy0, IRON)
    f.defs_add(f'<clipPath id="fy59h-glass"><rect x="{n(gx0)}" y="{gy0}" width="{n(gx1 - gx0)}" height="{gy1 - gy0}"/></clipPath>')
    f.add('<g clip-path="url(#fy59h-glass)">')
    for x, wy in ((cx - 28, 300), (cx + 28, 270)):
        f.line(x, gy0, x, wy, METAL_EDGE, 2)
        f.rect(x - 9, wy, 18, 58, H.grad(f, f"fy59h-wt{x}", HEAT_LIGHT, GRAIN, horizontal=True), INK, 2, 3)
    piv, Lp, th = (cx, 228), 168, math.radians(7)
    bx, by = piv[0] + Lp * math.sin(th), piv[1] + Lp * math.cos(th)
    f.line(piv[0], piv[1], bx, by, HEAT_LIGHT, 4)
    f.circle(bx, by, 24, H.grad(f, "fy59h-bob", HEAT_LIGHT, GRAIN), INK, 2.5)
    f.circle(bx - 6, by - 6, 7, WHITE, None, 0)
    f.add('</g>')
    f.add(f'<rect x="{n(gx0)}" y="{gy0}" width="{n(gx1 - gx0)}" height="{gy1 - gy0}" fill="{GLASS}" fill-opacity="0.25" stroke="{INK}" stroke-width="2.5"/>')
    f.add(f'<path d="M{n(gx0 + 10)},{gy1} L{n(gx0 + 40)},{gy0} H{n(gx0 + 58)} L{n(gx0 + 28)},{gy1} Z" fill="{WHITE}" fill-opacity="0.25"/>')

    # a framed picture and, in the foreground on the right, an armchair
    f.rect(970, 140, 150, 110, WHITE, INK, 3, 2)
    f.rect(984, 154, 122, 82, H.grad(f, "fy59h-pic", ICE, GLASS), INK, 2)
    f.path("M984,236 L1030,190 L1060,214 L1080,198 L1106,224 V236 Z", GOOD, INK, 2)
    f.circle(1080, 176, 10, HEAT_LIGHT)
    f.path(f"M1000,{floor + 40} V330 Q1000,300 1040,300 H1200 V{floor + 40} Z", GOOD, INK, 3)               # back
    f.path(f"M972,{floor + 40} V420 Q972,396 1000,396 Q1028,396 1028,420 V{floor + 40} Z", GOOD, INK, 3)  # arm
    f.rect(1028, 430, 180, 60, GOOD_LIGHT, INK, 3, 10)                                                     # cushion
    for x in (990, 1180): f.rect(x - 7, floor + 40, 14, 16, GRAIN, INK, 2)
    # the doorway: the next room beyond it, the frame round it
    d0, d1, dtop = 680, 880, 86
    f.rect(d0, dtop, d1 - d0, floor - dtop, H.grad(f, "fy59h-next", COLD_LIGHT, GLASS, y1=dtop, y2=floor))
    f.rect(d0, floor - 40, d1 - d0, 40, SAND_DARK)
    f.path(f"M{d0 - 18},{floor} V{dtop - 18} H{d1 + 18} V{floor} H{d1} V{dtop} H{d0} V{floor} Z", WHITE, INK, 2.5)
    # the door bouncer: a clamp on the top frame, the coil spring, a ring, four straps and the seat
    mx = (d0 + d1) / 2
    f.rect(mx - 22, dtop - 4, 44, 18, IRON, INK, 2, 3)
    f.line(mx, dtop + 14, mx, dtop + 26, INK, 3)
    top_s, bot_s = dtop + 26, 210
    coils = 14
    pts = [(mx + (-12 if i % 2 else 12), top_s + 8 + (bot_s - top_s - 16) * i / (coils - 1)) for i in range(coils)]
    f.path(f"M{mx},{top_s} L" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + f" L{mx},{bot_s}", stroke=IRON, w=3.5, extra='stroke-linejoin="round"')
    f.circle(mx, bot_s + 8, 8, "none", INK, 3)
    seat_y = 408
    for dx in (-46, 46):
        f.line(mx, bot_s + 14, mx + dx, seat_y - 46, COLD, 5)
    # the baby: legs down to the floor, the seat round the body, arms, head
    for dx, c in ((-12, SAND_LIGHT), (14, SAND_LIGHT)):
        f.path(f"M{mx + dx},{seat_y} L{mx + dx * 1.6},{floor - 30} L{mx + dx * 1.4 + 6},{floor - 6}", stroke=c, w=16, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{mx - 30},{seat_y - 56} Q{mx - 36},{seat_y - 104} {mx - 12},{seat_y - 110} H{mx + 12} Q{mx + 36},{seat_y - 104} {mx + 30},{seat_y - 56} Z", GOOD_LIGHT, INK, 2.5)  # body in a vest
    f.path(f"M{mx - 52},{seat_y - 52} Q{mx},{seat_y - 36} {mx + 52},{seat_y - 52} L{mx + 40},{seat_y + 6} Q{mx},{seat_y + 18} {mx - 40},{seat_y + 6} Z", COLD, INK, 2.5)  # the seat
    f.path(f"M{mx - 52},{seat_y - 52} Q{mx},{seat_y - 36} {mx + 52},{seat_y - 52}", stroke=COLD_LIGHT, w=3)
    for s in (-1, 1):
        f.path(f"M{mx + s * 28},{seat_y - 96} Q{mx + s * 52},{seat_y - 80} {mx + s * 46},{seat_y - 56}", stroke=GOOD_LIGHT, w=14, extra='stroke-linecap="round"')
        f.circle(mx + s * 46, seat_y - 54, 8, SAND_LIGHT)
    f.circle(mx, seat_y - 134, 30, SAND_LIGHT)
    f.path(f"M{mx - 18},{seat_y - 158} Q{mx - 4},{seat_y - 172} {mx + 12},{seat_y - 160} Q{mx + 2},{seat_y - 156} {mx - 2},{seat_y - 150} Z", GRAIN)
    return f.svg()



FIGURES = {"hero": hero, "jousi": spring, "xt": xt, "heiluri": pendulum, "energia": energy_graph, "vaimeneva": damped,
           "kuvaaja-k": graph_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "jousi": "reveals: force and acceleration point to the equilibrium, speed largest at x = 0",
    "xt": "safe: schematic x(t) with A and T marked, no numbers",
    "heiluri": "reveals: the restoring component G sin α of a pendulum's weight",
    "energia": "reveals: E_p + E_k = ½kA² for k = 20 N/m, A = 10 cm, split at x = 5 cm",
    "vaimeneva": "safe: schematic damped oscillation, no numbers",
    "kuvaaja-k": "safe: x(t) of a spring oscillator, maxima at 0, 0,40 and 0,80 s, amplitude 3,0 cm, no k",
}
