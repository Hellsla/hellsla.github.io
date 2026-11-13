"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-6` writes them into lesson.md.
FY7 colours (course brief): force #c92a2a, velocity #1971c2, current #7048e8, magnetic field #2b8a3e, N pole #f2a69c,
S pole #d0e6fb; into the page a cross, out of the page a dot in a circle. Energy: the loss of potential energy muted,
kinetic energy #1971c2, internal energy (heat) #e8590c."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD, IRON,
                    COPPER, ALUMINIUM, METAL_EDGE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GLASS, PAPER, HEAT, HEAT_LIGHT,
                    WATER, WATER_LIGHT, n)
import herolib as H

FORCE, VEL, CURRENT, FIELD, NPOLE, SPOLE = HOT, COLD, "#7048e8", GOOD, HOT_LIGHT, COLD_LIGHT


def into(f, x, y, r=12, colour=CURRENT):
    """Into the page: a cross in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    d = r * 0.55
    f.line(x - d, y - d, x + d, y + d, colour, 2.5); f.line(x + d, y - d, x - d, y + d, colour, 2.5)


def out(f, x, y, r=12, colour=CURRENT):
    """Out of the page: a dot in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    f.circle(x, y, r * 0.32, colour)


def magnet_h(f, x, y, w, h, n_right=True):
    """A bar magnet lying horizontally, its N half on the right (or on the left)."""
    left, right = (SPOLE, NPOLE) if n_right else (NPOLE, SPOLE)
    f.rect(x, y, w / 2, h, left, INK, 2.5, 3)
    f.rect(x + w / 2, y, w / 2, h, right, INK, 2.5, 3)
    f.tex(x + w / 4, y + h / 2, r"\text{S}" if n_right else r"\text{N}", "middle")
    f.tex(x + 3 * w / 4, y + h / 2, r"\text{N}" if n_right else r"\text{S}", "middle")


def lenz_ring():
    f = Fig("fy76-ring", 360, "Kaksi periaatekuvaa, ei mittakaavassa. Kuparirengas on leikattu paperin tasossa, joten "
            "siitä näkyvät ylä- ja alareunan poikkileikkaukset. Vasemmalla magneetti liikkuu N-napa edellä kohti rengasta. "
            "Renkaan induktiovirta kulkee yläreunassa paperiin päin ja alareunassa paperista ulos, ja sen magneettikenttä "
            "osoittaa renkaan keskellä vasemmalle, kohti magneettia: renkaan magneetin puoleinen sivu on N-napa, ja rengas "
            "hylkii magneettia. Voima magneettiin osoittaa vasemmalle, liikettä vastaan. Oikealla magneetti loittonee "
            "renkaasta. Virta on vastakkaissuuntainen, renkaan kenttä osoittaa oikealle, magneetin puoleinen sivu on S-napa, "
            "ja rengas vetää magneettia takaisin. Voima osoittaa oikealle, taas liikettä vastaan.")
    f.tex(150, 28, r"\text{magneetti lähestyy}", "middle", w=240)
    f.tex(450, 28, r"\text{magneetti loittonee}", "middle", w=240)
    f.line(300, 20, 300, 340, RULE, 2, "6 6")
    for x0, approach in ((0, True), (300, False)):
        mx, my, mw, mh = x0 + 26, 162, 112, 40
        magnet_h(f, mx, my, mw, mh)
        rx, ry = x0 + 222, 182
        # the ring cut by the page: its outline behind (thin) and its two cross-sections, top and bottom
        f.add(f'<ellipse cx="{rx}" cy="{ry}" rx="16" ry="70" fill="none" stroke="{COPPER}" stroke-width="5"/>')
        (into if approach else out)(f, rx, ry - 70, 12)
        (out if approach else into)(f, rx, ry + 70, 12)
        f.tex(rx + 18, ry - 96, "I", "start", CURRENT)
        # the ring's own field at its centre: towards the magnet when it approaches, away when it recedes
        if approach: f.arrow(rx + 28, ry, rx - 34, ry, FIELD, 3, 13)
        else: f.arrow(rx - 34, ry, rx + 28, ry, FIELD, 3, 13)
        f.tex(rx - 48, ry + 30, r"\overline{B}_\text{ind}", "middle", FIELD, w=58)
        # the pole of the ring's face towards the magnet
        f.tex(rx - 40, ry - 30, r"\text{N}" if approach else r"\text{S}", "middle")
        # the velocity of the magnet and the force on it
        if approach:
            f.arrow(mx + 30, my - 22, mx + 92, my - 22, VEL, 3.5, 13); f.tex(mx + 98, my - 22, r"\overline{v}", "start", VEL)
            f.arrow(mx + 50, my + mh + 24, mx - 6, my + mh + 24, FORCE, 3.5, 13); f.tex(mx + 56, my + mh + 24, r"\overline{F}", "start", FORCE)
        else:
            f.arrow(mx + 82, my - 22, mx + 20, my - 22, VEL, 3.5, 13); f.tex(mx + 88, my - 22, r"\overline{v}", "start", VEL)
            f.arrow(mx + 56, my + mh + 24, mx + 112, my + mh + 24, FORCE, 3.5, 13); f.tex(mx + 50, my + mh + 24, r"\overline{F}", "end", FORCE)
        f.tex(x0 + 150, 330, r"\text{rengas hylkii}" if approach else r"\text{rengas vetää}", "middle", w=170)
    return f.svg()


def tube():
    f = Fig("fy76-tube", 380, "Periaatekuva, ei mittakaavassa. Vasemmalla pystysuora kupariputki pituussuunnassa "
            "leikattuna, ja sen sisällä putoava magneetti, jonka N-napa on alaspäin. Magneetin alapuolella putken seinässä "
            "kiertää pyörrevirta, joka kulkee oikeassa seinässä paperiin päin ja vasemmassa paperista ulos; sen kenttä "
            "osoittaa ylöspäin, kohti magneettia. Magneetin yläpuolella pyörrevirta kiertää vastakkaiseen suuntaan, ja sen "
            "kenttä osoittaa alaspäin. Magneettiin vaikuttavat alaspäin paino ja ylöspäin yhtä pitkä jarruttava voima, ja "
            "sen nopeus osoittaa alaspäin. Oikealla alempi pyörrevirtarengas ylhäältä katsottuna: virta kiertää "
            "vastapäivään, ja kenttä osoittaa renkaan keskellä kohti katsojaa eli ylöspäin.")
    cx, top, bot, ro, wall = 150, 24, 356, 46, 10
    # the tube in section: the back wall faint, the two walls copper
    f.rect(cx - ro + wall, top, 2 * (ro - wall), bot - top, H.grad(f, "fy76t-back", COPPER, "#8a5f22", horizontal=True), extra='fill-opacity="0.3"')
    f.rect(cx - ro, top, wall, bot - top, COPPER, INK, 2, 2)
    f.rect(cx + ro - wall, top, wall, bot - top, COPPER, INK, 2, 2)
    # the magnet, N down
    my, mw, mh = 190, 46, 76
    f.rect(cx - mw / 2, my - mh / 2, mw, mh / 2, SPOLE, INK, 2.5, 3)
    f.rect(cx - mw / 2, my, mw, mh / 2, NPOLE, INK, 2.5, 3)
    f.tex(cx, my - mh / 4, r"\text{S}", "middle"); f.tex(cx, my + mh / 4, r"\text{N}", "middle")
    # the eddy currents below (anticlockwise from above: right wall into the page) and above (clockwise)
    yb, ya = my + mh / 2 + 44, my - mh / 2 - 44
    into(f, cx + ro - wall / 2, yb, 11); out(f, cx - ro + wall / 2, yb, 11)
    out(f, cx + ro - wall / 2, ya, 11); into(f, cx - ro + wall / 2, ya, 11)
    f.arrow(cx, yb + 22, cx, yb - 20, FIELD, 3, 12)
    f.arrow(cx, ya - 22, cx, ya + 20, FIELD, 3, 12)
    f.tex(cx - ro - 14, yb, r"I", "end", CURRENT); f.tex(cx - ro - 14, ya, r"I", "end", CURRENT)
    f.tex(cx - ro - 34, yb + 30, r"\overline{B}_\text{ind}", "end", FIELD, w=58)
    f.line(cx - ro - 34, yb + 22, cx - 8, yb + 4, MUTED, 1.5)
    # the forces on the magnet and its velocity, beside the tube
    xa = cx + ro + 26
    f.arrow(xa, my, xa, my + 78, FORCE, 3.5, 13); f.tex(xa + 10, my + 66, r"\overline{G}", "start", FORCE)
    f.arrow(xa, my, xa, my - 78, FORCE, 3.5, 13); f.tex(xa + 10, my - 66, r"\overline{F}_\text{j}", "start", FORCE)
    f.arrow(xa + 64, my - 30, xa + 64, my + 30, VEL, 3.5, 13); f.tex(xa + 74, my + 22, r"\overline{v}", "start", VEL)
    f.line(330, 24, 330, 356, RULE, 2, "6 6")
    # right: the lower ring seen from above, the current anticlockwise, the field out of the page (up)
    rx, ry, rr = 466, 196, 74
    f.circle(rx, ry, rr, "none", COPPER, 9)
    a0, a1 = math.radians(-60), math.radians(200)
    rc = rr + 20
    f.path(f"M{n(rx + rc * math.cos(a0))},{n(ry - rc * math.sin(a0))} A{rc},{rc} 0 1 0 {n(rx + rc * math.cos(a1))},{n(ry - rc * math.sin(a1))}", stroke=CURRENT, w=3)
    tx_, ty_ = rx + rc * math.cos(a1), ry - rc * math.sin(a1)
    ux, uy = math.sin(a1), math.cos(a1)                  # anticlockwise on the screen at the arc's end
    f.path(f"M{n(tx_ + 13 * ux)},{n(ty_ + 13 * uy)} L{n(tx_ - 4 * ux - 7 * uy)},{n(ty_ - 4 * uy + 7 * ux)} L{n(tx_ - 4 * ux + 7 * uy)},{n(ty_ - 4 * uy - 7 * ux)} Z", CURRENT)
    f.tex(rx + 78, ry + 84, "I", "start", CURRENT)
    out(f, rx, ry, 15, FIELD)
    f.tex(rx, ry + 36, r"\overline{B}_\text{ind}", "middle", FIELD, w=60)
    f.tex(rx, 46, r"\text{alempi rengas ylhäältä}", "middle", w=250)
    return f.svg()


def energy():
    """Energies when the body has fallen the 1,00 m tube in the simulation (m = 20 g): plastic E_k = 196,2 mJ, Q = 0;
    copper E_k = 0,225 mJ, Q = 195,98 mJ (lesson-answers.py fig-*)."""
    f = Fig("fy76-energy", 360, "Pylväskuvaaja mittakaavassa: energiat, kun 20 gramman magneetti on pudonnut metrin "
            "pituisen putken läpi. Muoviputkessa potentiaalienergian väheneminen 196 millijoulea on kokonaan muuttunut "
            "liike-energiaksi, eikä sisäenergiaa synny. Kupariputkessa potentiaalienergia vähenee yhtä paljon, mutta "
            "liike-energiaa on vain 0,2 millijoulea, niin vähän ettei pylväs näy, ja lähes kaikki, 196 millijoulea, on "
            "muuttunut putken sisäenergiaksi.")
    ax = Axes(f, (100, 280), (560, 70), x=(0, 7), y=(0, 200), xticks=[], yticks=[50, 100, 150, 200],
              xlabel=None, ylabel=r"E\ (\text{mJ})", origin_label=True)
    groups = (("muovi", 196.2, 196.2, 0.0), ("kupari", 196.2, 0.225, 195.975))
    for gi, (name, ep, ek, q) in enumerate(groups):
        for bi, (val, col, lab) in enumerate(((ep, MUTED, r"\Delta E_\text{p}"), (ek, COLD, r"E_\text{k}"), (q, HEAT, r"Q"))):
            x = 0.6 + gi * 3.4 + bi * 0.9
            x0, x1 = ax.X(x), ax.X(x + 0.7)
            if val > 0.5: f.rect(x0, ax.Y(val), x1 - x0, ax.Y(0) - ax.Y(val), col)
            f.tex((x0 + x1) / 2, 302, lab, "middle", COLD if col == COLD else HEAT if col == HEAT else INK)
        f.tex(ax.X(0.6 + gi * 3.4 + 1.25), 342, r"\text{" + name + r"putki}", "middle", w=150)
    # the copper tube's kinetic energy: too small to see, said in words
    xk = ax.X(0.6 + 3.4 + 0.9 + 0.35)
    f.line(xk, ax.Y(0) - 4, xk, ax.Y(60), MUTED, 1.5, "5 4")
    f.tex(xk, ax.Y(70), r"0{,}2\,\text{mJ}", "middle", COLD, bg=True)
    return f.svg()


def core():
    f = Fig("fy76-core", 340, "Kaksi periaatekuvaa muuntajan rautasydämen poikkileikkauksesta, ei mittakaavassa. "
            "Vaihtuva magneettikenttä osoittaa sydämen pituussuunnassa paperiin päin, mitä kuvaavat vihreät ristit. "
            "Vasemmalla umpinainen rautasydän: siinä kiertää yksi suuri pyörrevirtasilmukka koko poikkileikkauksen "
            "ympäri. Oikealla sydän on koottu ohuista levyistä, joiden välissä on eristekerros: pyörrevirrat kiertävät "
            "vain kunkin kapean levyn sisällä pieninä ja heikkoina silmukoina.")
    f.tex(150, 28, r"\text{umpinainen sydän}", "middle", w=220)
    f.tex(450, 28, r"\text{levyistä koottu sydän}", "middle", w=250)
    f.line(300, 20, 300, 330, RULE, 2, "6 6")
    def crosses(x0, y0, w, h):
        for i in range(3):
            for j in range(3):
                cx, cy = x0 + w * (i + 1) / 4, y0 + h * (j + 1) / 4
                f.line(cx - 7, cy - 7, cx + 7, cy + 7, FIELD, 2.5); f.line(cx + 7, cy - 7, cx - 7, cy + 7, FIELD, 2.5)
    # solid core: one big loop
    x0, y0, w, h = 50, 86, 200, 194
    f.rect(x0, y0, w, h, H.grad(f, "fy76c-iron", METAL_EDGE, IRON), INK, 2.5, 4)
    crosses(x0, y0, w, h)
    f.rect(x0 + 18, y0 + 18, w - 36, h - 36, "none", CURRENT, 3.5, 22)
    f.path(f"M{x0 + 94},{y0 + 18} l14,-7 v14 Z", CURRENT)                   # anticlockwise: on the top side to the left
    f.tex(x0 + 100, y0 + h + 30, r"\text{suuri pyörrevirta}", "middle", w=200)
    # laminated core: five sheets with insulation between them, a thin loop in each
    x0 = 350
    sw = 32
    for k in range(5):
        xs = x0 + k * (sw + 10)
        f.rect(xs, y0, sw, h, H.grad(f, f"fy76c-sheet{k}", METAL_EDGE, IRON), INK, 2, 2)
        f.rect(xs + 7, y0 + 16, sw - 14, h - 32, "none", CURRENT, 2, 8)
        if k < 4: f.rect(xs + sw, y0, 10, h, SAND_LIGHT, INK, 1, 0)
    for i in range(5):
        for j in range(3):
            cx, cy = x0 + (sw + 10) * i + sw / 2, y0 + h * (j + 1) / 4
            f.line(cx - 4, cy - 4, cx + 4, cy + 4, FIELD, 2); f.line(cx + 4, cy - 4, cx - 4, cy + 4, FIELD, 2)
    f.tex(x0 + 100, y0 + h + 30, r"\text{eristetyt levyt}", "middle", w=190)
    f.tex(x0 + 100, y0 - 22, r"\overline{B}\ \text{paperiin}", "middle", FIELD, w=170)
    return f.svg()


def brake_task():
    """Task figure: measured braking force of the eddy currents on a magnet in an aluminium tube against its speed; six
    points, fitted line F = 1,6 N·s/m · v (v 0,05–0,30 m/s). No power, no terminal speed drawn or written."""
    f = Fig("fy76-brake-task", 340, "Kuvaaja mittakaavassa: alumiiniputkessa liikkuvaan magneettiin kohdistuva pyörrevirtojen "
            "jarruttava voima newtoneina vauhdin funktiona metreinä sekunnissa. Kuusi mittauspistettä on origon kautta "
            "kulkevan nousevan suoran lähellä, ja suora on piirretty pisteiden lomitse. Ruudukon väli on 0,05 m/s ja 0,1 N.")
    ax = Axes(f, (96, 290), (480, 64), x=(0, 0.30), y=(0, 0.5), xticks=[0.05 * k for k in range(1, 7)],
              yticks=[0.1 * k for k in range(1, 6)], xlabel=r"v\ (\text{m/s})", ylabel=r"F\ (\text{N})",
              xfmt=lambda v: fi(round(v, 2), 2), yfmt=lambda v: fi(round(v, 1), 1))
    ax.line([(0, 0), (0.30, 0.48)], FORCE, 3)
    for v_, F_ in ((0.05, 0.081), (0.10, 0.158), (0.15, 0.243), (0.20, 0.319), (0.25, 0.402), (0.30, 0.478)):
        ax.point(v_, F_, INK)
    return f.svg()


def hero():
    """The opening illustration: a copper tube held upright in a lab stand, a magnet just leaving its lower end above
    a soft pad, a plastic tube beside it and a stopwatch on the bench."""
    f = H.hero("fy76-hero", "Kuvitus: laboratorion pöydällä seisoo telineessä pystysuora kupariputki ja sen vieressä "
               "läpinäkyvä muoviputki. Kupariputken alapäästä on juuri tulossa ulos pieni magneetti pehmeän alustan "
               "yläpuolella. Pöydällä on sekuntikello, joka näyttää kuluneen useita sekunteja.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 470, 1200, 130, H.grad(f, "fy76h-desk", SAND_LIGHT, SAND))
    f.line(0, 470, 1200, 470, GRAIN, 3)
    # a window on the wall
    f.rect(90, 70, 220, 250, H.grad(f, "fy76h-sky", H.ICE, GLASS), INK, 3, 6)
    f.line(200, 70, 200, 320, INK, 3); f.line(90, 195, 310, 195, INK, 3)
    # lab stand: base, rod, two clamps
    f.rect(470, 448, 200, 22, IRON, INK, 3, 4)
    f.rect(500, 50, 16, 400, H.grad(f, "fy76h-rod", ALUMINIUM, METAL_EDGE, horizontal=True), INK, 3, 3)
    for y in (90, 330):
        f.rect(508, y, 110, 14, METAL_EDGE, INK, 3, 3)
        f.rect(612, y - 8, 30, 30, IRON, INK, 3, 4)
    # the copper tube in the clamps
    f.rect(600, 40, 56, 350, H.grad(f, "fy76h-cu", COPPER, "#8a5f22", horizontal=True), INK, 3, 4)
    f.add('<ellipse cx="628" cy="40" rx="28" ry="8" fill="#8a5f22" stroke="#1f2933" stroke-width="3"/>')
    # the magnet just leaving the lower end, slow-motion lines above it
    f.rect(611, 392, 34, 30, NPOLE, INK, 3, 4)
    f.rect(611, 372, 34, 22, SPOLE, INK, 3, 4)
    f.rect(586, 452, 84, 18, HOT_LIGHT, INK, 3, 8)
    for dx in (-14, 0, 14):
        f.line(628 + dx, 432, 628 + dx, 444, MUTED, 3, cap="round")
    # the plastic tube beside, transparent
    f.rect(760, 120, 44, 350, H.grad(f, "fy76h-pl", GLASS, COLD_LIGHT, horizontal=True), INK, 3, 4, extra='fill-opacity="0.75"')
    f.add('<ellipse cx="782" cy="120" rx="22" ry="7" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>')
    # stopwatch on the bench
    H.stopwatch(f, 960, 400, 62, 0.62)
    # eddy-current glow hints: faint violet rings on the copper tube near the magnet
    for y in (352, 382):
        f.add(f'<ellipse cx="628" cy="{y}" rx="32" ry="7" fill="none" stroke="#7048e8" stroke-width="3" stroke-opacity="0.55"/>')
    return f.svg()


def scene():
    """A second everyday scene: an induction hob heating a steel pot; the glass top stays cool beside the pot."""
    f = H.scene("fy76-scene", "Kuvitus: induktioliesi, jonka lasipinnalla on teräskattila. Kattilassa vesi kiehuu ja "
                "siitä nousee höyryä. Lasipinnan alla näkyy leikkauskuvana kuparinen kela. Liekkiä tai hehkuvaa levyä "
                "ei ole.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 250, 600, 110, H.grad(f, "fy76s-bench", SAND_LIGHT, SAND))
    # the hob: dark glass top and the coil under it (cut away)
    f.rect(70, 226, 460, 26, INK, rx=6)
    f.rect(70, 252, 460, 60, IRON, INK, 2, 4)
    for k in range(7):
        x = 210 + k * 26
        f.rect(x, 262, 18, 12, COPPER, INK, 1.5, 3)
    f.circle(480, 239, 6, HEAT)
    # the steel pot with water and steam
    f.path("M190,226 L196,130 L404,130 L410,226 Z", H.grad(f, "fy76s-pot", ALUMINIUM, METAL_EDGE, horizontal=True), INK, 3)
    f.rect(184, 122, 232, 12, METAL_EDGE, INK, 3, 4)
    f.rect(150, 140, 40, 12, IRON, INK, 2.5, 5); f.rect(410, 140, 40, 12, IRON, INK, 2.5, 5)
    f.add(f'<ellipse cx="300" cy="134" rx="104" ry="9" fill="{WATER_LIGHT}" stroke="{INK}" stroke-width="2"/>')
    for x, ph in ((250, 0), (300, 1), (350, 2)):
        f.path(f"M{x},112 c-14,-16 14,-30 0,-46 c-14,-16 14,-30 0,-46", stroke=MUTED, w=4, extra='stroke-linecap="round" stroke-opacity="0.6"')
    # faint violet eddy currents in the pot's base
    f.add(f'<ellipse cx="300" cy="219" rx="80" ry="5" fill="none" stroke="{CURRENT}" stroke-width="3" stroke-opacity="0.6"/>')
    return f.svg()


FIGURES = {"hero": hero, "ring": lenz_ring, "tube": tube, "energy": energy, "core": core, "scene": scene, "brake-task": brake_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "ring": "reveals: an approaching N pole is repelled (the ring's face is N), a receding one attracted",
    "tube": "reveals: the eddy currents below and above a falling magnet and the braking force equal to the weight",
    "energy": "reveals: in the copper tube nearly all of the potential energy becomes internal energy",
    "brake-task": "safe: measured F(v) of an eddy-current brake, six points and a line through the origin, no power or terminal speed",
    "core": "reveals: a laminated core cuts the eddy currents into small loops",
}
