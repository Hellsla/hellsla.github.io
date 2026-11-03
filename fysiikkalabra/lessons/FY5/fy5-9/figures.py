"""Figures of this lesson (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy5-9` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND, SAND_LIGHT, SAND_DARK, GRAIN, ALUMINIUM,
                    METAL_EDGE, IRON, GOOD, GOOD_LIGHT, COLD, COLD_LIGHT, HOT, HEAT, HEAT_LIGHT, ICE, n)
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
    """The chapter's opening illustration: a playground swing set; one swing at the end of its swing, one hanging still."""
    f = H.hero("fy59-hero", "Kuvitus: leikkipuiston keinuteline nurmikolla puiden edessä. Kahdesta samanpituisesta keinusta "
               "toisessa istuu lapsi keinun ollessa heilahduksensa ääriasennossa, toinen keinu riippuu tyhjänä paikallaan. "
               "Katkoviivainen kaari näyttää keinun radan.")
    H.sky(f, "fy59h")
    H.cloud(f, 860, 110, 1.0); H.cloud(f, 300, 80, 0.7)
    H.forest(f, 400, 70, 30, "#2b8a3e", seed=2)
    f.rect(0, 420, 1200, 180, GOOD_LIGHT)
    for k in range(40):
        x = H.rnd(k, 7) * 1200; y = 440 + H.rnd(k + 50, 7) * 150
        f.path(f"M{n(x)},{n(y)} l4,-12 M{n(x + 6)},{n(y)} l-2,-10", stroke="#2b8a3e", w=2)
    # sandy patch under the swings
    f.add(f'<ellipse cx="600" cy="520" rx="330" ry="46" fill="{SAND_LIGHT}"/>')
    # the frame: two A-legs and a top bar
    top, foot = 120, 530
    for cx in (330, 870):
        f.path(f"M{cx - 70},{foot} L{cx},{top} L{cx + 70},{foot}", stroke=METAL_EDGE, w=16, extra='stroke-linecap="round"')
    f.line(320, top, 880, top, METAL_EDGE, 20, cap="round")
    # the empty swing hanging still on the right
    for x in (720, 780):
        f.line(x, top + 8, x, 438, METAL_EDGE, 4)
    f.rect(706, 436, 88, 14, SAND, INK, 2.5, 4)
    # the child's swing at its extreme position on the left (pivot at y = top, angle 30°)
    a = math.radians(26); L = 330
    for x in (520, 580):
        ex, ey = x - L * math.sin(a), top + L * math.cos(a)
        f.line(x, top + 8, ex, ey, METAL_EDGE, 4)
    cx, cy = 550 - L * math.sin(a), top + L * math.cos(a)
    f.path(f"M{n(550 - 352 * math.sin(math.radians(32)))},{n(top + 352 * math.cos(math.radians(32)))} A352,352 0 0 0 {n(550 + 352 * math.sin(math.radians(32)))},{n(top + 352 * math.cos(math.radians(32)))}",
           stroke=MUTED, w=3, extra='stroke-dasharray="10 9"')
    f.add(f'<g transform="rotate(26 {n(cx)} {n(cy)})">')
    f.rect(cx - 44, cy - 7, 88, 14, SAND, INK, 2.5, 4)
    # the child sitting: trousers (thighs forward, shins down), body, arms to the ropes, head
    f.path(f"M{n(cx - 20)},{n(cy - 8)} H{n(cx + 46)} V{n(cy + 52)} H{n(cx + 30)} V{n(cy + 10)} H{n(cx - 20)} Z", INK)
    f.path(f"M{n(cx - 26)},{n(cy - 6)} Q{n(cx - 30)},{n(cy - 92)} {n(cx - 4)},{n(cy - 96)} Q{n(cx + 22)},{n(cy - 92)} {n(cx + 18)},{n(cy - 6)} Z", HEAT)
    f.path(f"M{n(cx + 8)},{n(cy - 74)} L{n(cx + 30)},{n(cy - 104)}", stroke=HEAT, w=14, extra='stroke-linecap="round"')
    f.circle(cx + 30, cy - 106, 8, SAND_LIGHT)
    f.circle(cx - 4, cy - 118, 24, SAND_LIGHT)
    f.path(f"M{n(cx - 28)},{n(cy - 120)} Q{n(cx - 26)},{n(cy - 148)} {n(cx - 2)},{n(cy - 146)} Q{n(cx + 24)},{n(cy - 146)} {n(cx + 22)},{n(cy - 122)} Q{n(cx)},{n(cy - 132)} {n(cx - 28)},{n(cy - 120)} Z", INK)
    f.add('</g>')
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
