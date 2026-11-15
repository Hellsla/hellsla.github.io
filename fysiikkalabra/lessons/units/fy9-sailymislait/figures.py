"""Figures of the FY9 unit fy9-sailymislait (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-sailymislait`
writes them into content/fi/units/fy9-sailymislait/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a winter railway yard, a freight wagon rolls towards a standing, identical wagon to couple
            with it (no text, no people)
kartta      the concept map of the review: two conservation laws (energy, momentum), each with its laws, and the
            applications that combine them
tormays     the hook's coupling to scale: two 32 t wagons before and after, the velocity arrows, and bars of the total
            momentum (the same) and of the kinetic energy (half of it becomes internal energy)
pysahtyminen the stopping distance for "Johda itse": a schematic (t, v) graph, the speed v_0 constant for the reaction
            time t_r, then falling linearly to zero during the braking time t_j; the rectangle s_r and the triangle s_j
tuuli       the wind power for "Johda itse": the air cylinder of base area A and length v dt that passes through the
            rotor of a wind turbine in the time dt (side view, schematic)
"""
import math
import figlib
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT,
                    COLD, COLD_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, COPPER, GOOD, n, fi)
import herolib as H

figlib.set_language({}, ",")
LOST = "#dee2e6"            # the lost kinetic energy: a neutral grey, not the acceleration orange

# the hook (computed here and quoted in unit.md and inquiry.json)
M_WAGON = 32000.0           # kg, each wagon
V0 = 1.6                    # m/s, the rolling wagon
V1 = M_WAGON * V0 / (2 * M_WAGON)                 # 0,80 m/s, the coupled pair
EK0 = 0.5 * M_WAGON * V0 ** 2                     # 40 960 J
EK1 = 0.5 * 2 * M_WAGON * V1 ** 2                 # 20 480 J
P0 = M_WAGON * V0                                 # 51 200 kg m/s


def _wagon(f, x, yr, L, body, sc=1.0, snow=True):
    """A covered freight wagon in side view standing on the rail top yr, from x to x + L: underframe, two bogies,
    sliding doors with ribs, a curved roof, buffers and a screw coupling at both ends."""
    h = 118 * sc
    top = yr - 34 * sc - h
    f.rect(x, top, L, h, body, INK, 3, 4)                                 # the body
    for k in range(1, int(L / (26 * sc))):
        f.line(x + k * 26 * sc, top + 6, x + k * 26 * sc, top + h - 6, INK, 1.2)
    for dx in (0.3, 0.52):                                                # two sliding doors
        f.rect(x + L * dx, top + 10 * sc, L * 0.18, h - 20 * sc, body, INK, 2.5)
        f.line(x + L * (dx + 0.09), top + 10 * sc, x + L * (dx + 0.09), top + h - 10 * sc, INK, 1.5)
        f.rect(x + L * (dx + 0.15), top + h * 0.45, 8 * sc, 14 * sc, ALUMINIUM, INK, 1.5)
    f.path(f"M{n(x - 4)},{n(top)} Q{n(x + L / 2)},{n(top - 22 * sc)} {n(x + L + 4)},{n(top)} Z", IRON, INK, 2.5)   # roof
    if snow: f.path(f"M{n(x + 6)},{n(top - 4 * sc)} Q{n(x + L / 2)},{n(top - 24 * sc)} {n(x + L - 6)},{n(top - 4 * sc)} "
                    f"Q{n(x + L / 2)},{n(top - 14 * sc)} {n(x + 6)},{n(top - 4 * sc)} Z", WHITE)
    f.rect(x - 6, yr - 34 * sc, L + 12, 10 * sc, INK)                     # underframe
    for bx in (x + L * 0.16, x + L * 0.84):                               # bogies with two wheels each
        f.rect(bx - 44 * sc, yr - 28 * sc, 88 * sc, 10 * sc, IRON, INK, 2)
        for wx in (bx - 24 * sc, bx + 24 * sc):
            f.circle(wx, yr - 14 * sc, 14 * sc, INK)
            f.circle(wx, yr - 14 * sc, 5 * sc, ALUMINIUM)
    for ex, s in ((x - 6, -1), (x + L + 6, 1)):                          # buffers and the coupling hook
        f.rect(min(ex, ex + s * 14 * sc), yr - 33 * sc, 14 * sc, 6 * sc, IRON)
        f.rect(ex + (s * 14 * sc if s > 0 else -18 * sc), yr - 40 * sc, 4 * sc, 20 * sc, METAL_EDGE, INK, 1.5)
        f.line(ex, yr - 26 * sc, ex + s * 22 * sc, yr - 22 * sc, INK, 3, cap="round")


def hero():
    """A clear winter day at a small railway yard in the forest: a red-brown covered wagon rolls from the left towards an
    identical standing wagon (motion lines behind it); overhead line masts, spruces, snow banks, a signal."""
    f = H.hero("fy9sl-hero", "Kuvitus: talvinen ratapiha metsän keskellä kirkkaana päivänä. Vasemmalla punaruskea katettu "
               "tavaravaunu rullaa oikealle, ja sen takana on liikeviivoja. Oikealla seisoo samanlainen vaunu, johon rullaava "
               "vaunu on kohta kytkeytymässä. Raiteiden yllä on sähköradan pylväitä ja ajojohdin, taustalla kuusimetsää ja lumipenkkoja.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9sl-sky", "#9cc4e4", "#eef5f9"))
    H.sun(f, "fy9sl", 1050, 96, 40, rays=False)
    H.cloud(f, 260, 92, 0.9); H.cloud(f, 700, 70, 0.7)
    H.forest(f, 330, 46, 34, "#3b6b4f", seed=6, depth=24)
    H.forest(f, 352, 40, 30, "#2f5a41", seed=9, depth=20)
    f.path("M0,350 Q300,334 600,346 T1200,342 V600 H0 Z", "#f8fbfd")      # snow field
    f.path("M0,560 Q360,548 700,560 T1200,556 V600 H0 Z", "#e6eff5")
    # the far track (empty) and the near track the wagons stand on
    for yr, sl, col in ((392, 0.55, "#8a8172"), (500, 1.0, "#6f6556")):
        f.rect(0, yr, 1200, 12 * sl, col)                                 # ballast band
        for k in range(0, 1200, int(34 * sl) + 8):
            f.rect(k, yr + 2 * sl, 18 * sl, 9 * sl, "#5a4a3a")             # sleepers
        f.rect(0, yr - 4 * sl, 1200, 4 * sl, IRON)                        # rail
    # overhead line masts and the contact wire
    for x in (120, 520, 920):
        f.rect(x, 170, 10, 330, IRON, INK, 1.5)
        f.line(x + 5, 190, x + 130, 190, IRON, 4)
        f.line(x + 5, 214, x + 110, 190, IRON, 2)
    f.line(0, 206, 1200, 206, INK, 2)
    f.line(0, 190, 1200, 190, INK, 1.2)
    # a signal on the right
    f.rect(1150, 300, 8, 200, IRON, INK, 1.5)
    f.rect(1136, 280, 36, 60, INK, None, 0, 6)
    f.circle(1154, 296, 9, GOOD); f.circle(1154, 324, 9, "#4b5560")
    # the standing wagon (right) and the rolling one (left), with motion lines
    _wagon(f, 690, 496, 420, "#9c3b2a")
    _wagon(f, 150, 496, 420, "#9c3b2a")
    for k, (y, L) in enumerate(((380, 90), (412, 120), (444, 70))):
        f.line(130 - L, y, 136, y, WHITE, 9, cap="round")
        f.line(130 - L, y, 136, y, COLD, 4, cap="round")
    # snow banks and spruces in front
    f.path("M0,528 Q80,506 170,526 Q260,544 360,562 Q430,576 480,600 H0 Z", WHITE)
    for x, h in ((36, 170), (1182, 150)):
        H.spruce(f, x, 560, h, "#2b6a3e")
    return f.svg()


ACCENT = "#1a4d2e"                                        # the site's own dark green (site.css --accent, the buttons)


def kartta():
    """The recognition chart (teacher 2026-11-15, replaces the concept map): "Mistä tunnistan, mitä lakia käytän?". One
    card per sign in the task's own words: the sign on top, the choice it leads to and, as the result in a pill in the
    site's dark green, the law or method; no list of formulas. Stacked for a phone: a spine down the left from the start box."""
    rows = [
        (r"\text{ei kitkaa, vain painovoima}", r"\to\ \text{mekaaninen energia säilyy}", r"E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}", 230, True),
        (r"\text{kitka tai moottori tekee työtä}", r"\to\ \text{energiaperiaate}", r"E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}", 290, True),
        (r"\text{kappale liikkuu}", r"\to\ \text{liike-energia}", r"E_\text{k} = \tfrac12 mv^2", 124, False),
        (r"\text{korkeus muuttuu}", r"\to\ \text{potentiaalienergia}", r"E_\text{p} = mgh", 106, False),
        (r"\text{törmäys tai räjähdys}", r"\to\ \text{liikemäärä säilyy}", r"\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}", 210, True),
        (r"\text{kimmoisa törmäys}", r"\to\ \text{liike-energia säilyy}", r"\Delta E_\text{k} = 0", 100, False),
        (r"\text{voima vaikuttaa tietyn ajan}", r"\to\ \text{impulssi}", r"\overline{I} = \Delta\overline{p}", 116, False),
        (r"\text{teho tai hyötysuhde kysytään}", r"\to\ \text{hyötysuhde}", r"\eta = P_\text{a}/P_\text{o}", 124, False),
    ]
    hub_h, x0, x1, ch, gap, top = 72, 30, 372, 72, 14, 98
    heights = [ch + (30 if r[4] else 0) for r in rows]
    ys = [top + sum(heights[:k]) + gap * k for k in range(len(rows))]
    height = ys[-1] + heights[-1] + 8
    f = Fig("fy9sl-kartta", height, ARIA_KARTTA, width=380, size=21)
    f.line(14, hub_h + 8, 14, ys[-1] + heights[-1] / 2, RULE, 3)
    f.rect(8, 8, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, 8 + 26, r"\textbf{mistä tunnistan lain?}", "middle", INK, w=330)
    f.tex(190, 8 + 54, r"\text{ensin tunnusmerkki, sitten laki}", "middle", INK, size=17, w=340)
    for (sign, choice, law, pw, tall), y, ch_ in zip(rows, ys, heights):
        f.line(14, y + ch_ / 2, x0, y + ch_ / 2, RULE, 3)
        f.rect(x0, y, x1 - x0, ch_, WHITE, MUTED, 2, 10)
        f.tex(x0 + 14, y + 22, sign, "start", INK, size=19, w=x1 - x0 - 28)
        f.line(x0 + 10, y + 40, x1 - 10, y + 40, RULE_LIGHT, 1.5)
        yy = y + 55
        f.tex(x0 + 14, yy, choice, "start", MUTED, size=17, w=x1 - x0 - 38 - (0 if tall else pw))
        if tall:                                               # a long result on a line of its own
            yy += 30
            f.rect(x1 - 10 - pw, yy - 12, pw, 26, ACCENT, ACCENT, 2, 8)
        else:
            f.rect(x1 - 10 - pw, yy - 11, pw, 24, ACCENT, ACCENT, 2, 8)
        f.tex(x1 - 10 - pw / 2, yy + 1, law, "middle", WHITE, size=17, w=pw - 8)
    return f.svg()


ARIA_KARTTA = ("Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Katso ensin tehtävän tunnusmerkki. Ei kitkaa, vain "
               "painovoima: mekaaninen energia säilyy, eli alun potentiaali- ja liike-energian summa on yhtä suuri kuin lopun. "
               "Kitka tai moottori tekee työtä: energiaperiaate, jossa alun mekaaniseen energiaan lisätään muiden voimien työ. "
               "Kappale liikkuu: liike-energia on puolet m v toiseen. Korkeus muuttuu: potentiaalienergia on m g h. Törmäys "
               "tai räjähdys: liikemäärä säilyy, ennen on yhtä suuri kuin jälkeen. Kimmoisa törmäys: myös liike-energia "
               "säilyy, sen muutos on nolla. Voima vaikuttaa tietyn ajan: impulssi on liikemäärän muutos. Teho tai hyötysuhde "
               "kysytään: hyötysuhde on antoteho jaettuna ottotehoon.")


def tormays():
    """The hook to scale: before, a wagon at 1,6 m/s and one at rest; after, the pair at 0,80 m/s (blue velocity arrows,
    100 px per m/s). Under them two bars, before and after: the total momentum (the same) and the kinetic energy
    (half of it remains; the other half, shaded, has become internal energy of the buffers and couplings)."""
    f = Fig("fy9sl-tormays", 560, "Kaavakuva, nopeudet ja palkit mittakaavassa. Ylhäällä ennen törmäystä: vasen vaunu liikkuu "
            "oikealle nopeudella 1,6 m/s, sininen nuoli, ja oikea vaunu on levossa. Sen alla törmäyksen jälkeen: vaunut ovat "
            "kiinni toisissaan ja liikkuvat yhdessä nopeudella 0,80 m/s, puolet lyhyempi nuoli. Alhaalla palkit. "
            "Kokonaisliikemäärä on ennen ja jälkeen sama, 51 200 kilogrammametriä sekunnissa. Liike-energia on ennen 41 kJ ja "
            "jälkeen 20 kJ; puuttuva puolikas on muuttunut puskurien ja kytkimien sisäenergiaksi.", width=420, size=20)
    def wag(x, y, w=110, h=46):
        f.rect(x, y, w, h, "#c8735f", INK, 2.5, 4)
        for wx in (x + 22, x + w - 22): f.circle(wx, y + h + 8, 9, INK)
    f.tex(8, 22, r"\text{ennen}", "start", INK)
    f.line(0, 130, 420, 130, INK, 1.5)
    wag(20, 60); wag(290, 60)
    f.arrow(75, 44, 75 + 160, 44, COLD, 4, 14)
    f.tex(160, 20, r"1{,}6\,\text{m/s}", "middle", COLD)
    f.tex(345, 40, r"v = 0", "middle", INK, size=18)
    f.tex(8, 160, r"\text{jälkeen}", "start", INK)
    f.line(0, 260, 420, 260, INK, 1.5)
    wag(100, 190); wag(214, 190)
    f.rect(208, 206, 8, 10, INK)
    f.arrow(155, 176, 155 + 80, 176, COLD, 4, 14)
    f.tex(290, 164, r"0{,}80\,\text{m/s}", "start", COLD)
    # bars: 160 px for the momentum and for 41 kJ
    y0 = 500
    f.line(10, y0, 410, y0, INK, 2)
    hp = 160
    he0, he1 = 160, 160 * EK1 / EK0
    bars = ((40, hp, IRON, None), (110, hp, IRON, None), (230, he0, SAND, None), (300, he1, SAND, LOST))
    for x, h, col, lost in bars:
        f.rect(x, y0 - h, 52, h, col, INK, 2)
        if lost:
            f.rect(x, y0 - he0, 52, he0 - h, lost, INK, 1.5, extra='stroke-dasharray="6 4"')
    f.tex(101, 292, r"p_\text{kok}", "middle")
    f.tex(256, 292, r"E_\text{k}", "middle")
    for x, t in ((40, "ennen"), (110, "jälkeen"), (230, "ennen"), (300, "jälkeen")):
        f.tex(x + 26, y0 + 22, r"\text{" + t + "}", "middle", INK, size=17)
    f.tex(326, y0 - he0 - 18, r"\text{sisäenergiaksi}", "middle", MUTED, size=17)
    f.tex(101, 318, r"51\,200\,\text{kg} \cdot \text{m/s}", "middle", INK, size=17)   # the same before and after
    f.tex(256, y0 - he0 / 2, r"41\,\text{kJ}", "middle", INK, size=17)
    f.tex(326, y0 - he1 / 2, r"20\,\text{kJ}", "middle", INK, size=17)
    return f.svg()


def pysahtyminen():
    """The stopping distance as a (t, v) graph, schematic: the speed v_0 stays constant for the reaction time t_r (the
    blue rectangle, the reaction distance s_r) and then falls linearly to zero during the braking time t_j (the sand
    triangle, the braking distance s_j). No numbers on the axes."""
    f = Fig("fy9sl-pysahtyminen", 360, "Kaavakuva, ei lukuarvoja: auton nopeus v ajan t funktiona. Reaktioajan t r nopeus "
            "pysyy lähtönopeutena v 0, joten kuvaaja on vaakasuora, ja sen alla on sininen suorakulmio, reaktiomatka s r. "
            "Sitten jarrutuksen aikana t j nopeus pienenee tasaisesti nollaan, joten kuvaaja on laskeva suora, ja sen alla "
            "on hiekanvärinen kolmio, jarrutusmatka s j. Auto pysähtyy hetkellä t r + t j.", size=24)
    ax = Axes(f, (90, 300), (470, 70), x=(0, 10), y=(0, 6), xticks=[], yticks=[], xlabel=r"t", ylabel=r"v", grid=False)
    v0, tr, ts = 4.5, 2.5, 8.0
    ax.area([(0, 0), (0, v0), (tr, v0), (tr, 0)], COLD_LIGHT, 0.9)
    ax.area([(tr, 0), (tr, v0), (ts, 0)], SAND_LIGHT, 0.9)
    ax.line([(tr, 0), (tr, v0)], MUTED, 1.5, "6 5")
    ax.line([(0, v0), (tr, v0), (ts, 0)], INK, 3.5)
    f.tex(ax.X(0) - 12, ax.Y(v0), r"v_0", "end", INK)
    f.tex(ax.X(tr), ax.Y(0) + 26, r"t_\text{r}", "middle", INK)
    f.tex(ax.X(ts), ax.Y(0) + 26, r"t_\text{r} + t_\text{j}", "middle", INK)
    f.tex(ax.X(tr / 2), ax.Y(v0 / 2), r"s_\text{r}", "middle", COLD)
    f.tex(ax.X(tr + (ts - tr) / 3), ax.Y(v0 / 3), r"s_\text{j}", "middle", INK)
    f.tex(ax.X(tr / 2), ax.Y(v0) - 22, r"\text{reaktio}", "middle", MUTED, size=20)
    f.tex(ax.X(5.7), ax.Y(3.3), r"\text{jarrutus}", "start", MUTED, size=20)
    return f.svg()


def tuuli():
    """The wind power, schematic side view: the wind blows from the left at the speed v; the air that passes through
    the rotor in the time dt fills a cylinder (light blue) whose base is the rotor's swept area A (an ellipse in
    perspective) and whose length is v dt; the turbine's tower, nacelle and three blades on the right. No numbers."""
    f = Fig("fy9sl-tuuli", 420, "Kaavakuva sivulta, ei lukuarvoja. Oikealla tuulivoimala: torni, konehuone ja kolme lapaa. "
            "Roottorin pyyhkäisemä pinta-ala A on piirretty soikiona. Tuuli puhaltaa vasemmalta nopeudella v, siniset nuolet. "
            "Roottorin vasemmalla puolella on vaaleansininen ilmalieriö, jonka pohja on ala A ja pituus v kertaa delta t: "
            "se ilma, joka kulkee roottorin läpi ajassa delta t.", size=24)
    cy, ry, rx, xl, xr = 190, 110, 26, 150, 420
    # the ground and the tower behind everything
    f.line(20, 400, 580, 400, INK, 2.5)
    f.path(f"M{xr + 44},{cy + 14} L{xr + 36},400 L{xr + 64},400 L{xr + 56},{cy + 14} Z", ALUMINIUM, INK, 2)
    # the air cylinder: the far ellipse at the left, the sides, the rotor's ellipse on the right
    f.path(f"M{xl},{cy - ry} L{xr},{cy - ry} A{rx},{ry} 0 0 1 {xr},{cy + ry} L{xl},{cy + ry} "
           f"A{rx},{ry} 0 0 1 {xl},{cy - ry} Z", COLD_LIGHT, None, 0, extra='fill-opacity="0.75"')
    f.line(xl, cy - ry, xr, cy - ry, COLD, 2, "8 6")
    f.line(xl, cy + ry, xr, cy + ry, COLD, 2, "8 6")
    f.path(f"M{xl},{cy - ry} A{rx},{ry} 0 1 0 {xl},{cy + ry} A{rx},{ry} 0 1 0 {xl},{cy - ry} Z", "none", COLD, 2,
           extra='stroke-dasharray="8 6"')
    for y in (cy - 60, cy, cy + 60):
        f.arrow(xl + 40, y, xl + 150, y, COLD, 3.5, 14)
    f.tex(xl + 95, cy - 60 - 22, r"v", "middle", COLD)
    # the rotor: its swept area as an ellipse, the nacelle and three blades
    f.path(f"M{xr},{cy - ry} A{rx},{ry} 0 1 0 {xr},{cy + ry} A{rx},{ry} 0 1 0 {xr},{cy - ry} Z", "none", INK, 2.5)
    f.rect(xr + 6, cy - 14, 76, 28, WHITE, INK, 2.5, 8)
    for deg in (90, 210, 330):
        bx = xr + 0.94 * rx * math.cos(math.radians(deg)); by = cy - 0.94 * ry * math.sin(math.radians(deg))
        f.line(xr, cy, bx, by, INK, 7, cap="round")
        f.line(xr, cy, bx, by, WHITE, 3, cap="round")
    f.circle(xr, cy, 10, INK)
    f.tex(xr + 38, cy - ry + 8, r"A", "start", INK)
    # the length of the cylinder
    yb = cy + ry + 26
    f.line(xl, yb - 8, xl, yb + 8, INK, 2); f.line(xr, yb - 8, xr, yb + 8, INK, 2)
    f.line(xl, yb, xr, yb, INK, 2)
    f.tex((xl + xr) / 2, yb + 24, r"v\,\Delta t", "middle", INK)
    f.tex(xl - 4, cy - ry - 24, r"\text{ilmaa ajassa } \Delta t", "start", MUTED, size=20)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "tormays": tormays, "pysahtyminen": pysahtyminen, "tuuli": tuuli}
REUSE = {"kartta": "reveals: the key laws of FY4 mechanical energy and momentum",
         "tormays": "reveals: the coupled wagons keep the momentum and lose half of the kinetic energy",
         "pysahtyminen": "safe: the (t, v) graph of a stop, reaction then braking, no numbers",
         "tuuli": "safe: the air cylinder A by v dt through a wind turbine's rotor, no numbers"}
