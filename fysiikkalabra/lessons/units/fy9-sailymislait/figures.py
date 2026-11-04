"""Figures of the FY9 unit fy9-sailymislait (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-sailymislait`
writes them into content/fi/units/fy9-sailymislait/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a winter railway yard, a freight wagon rolls towards a standing, identical wagon to couple
            with it (no text, no people)
kartta      the concept map of the review: two conservation laws (energy, momentum), each with its laws, and the
            applications that combine them
tormays     the hook's coupling to scale: two 32 t wagons before and after, the velocity arrows, and bars of the total
            momentum (the same) and of the kinetic energy (half of it becomes internal energy)
"""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT,
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


def kartta():
    """The concept map, stacked for a phone: two conservation laws at the top, a spine down the left and three boxes
    (energy, momentum, the applications), each with three laws and a grey word beside each."""
    f = Fig("fy9sl-kartta", 604, "Käsitekartta. Ylhäällä solmu säilymislait: energia ja liikemäärä. Siitä lähtee alas kolme "
            "haaraa. Energia: liike-energia E k = puolet m v toiseen, potentiaalienergia E p = m g h ja energiaperiaate, jossa "
            "alun mekaaninen energia ja muiden voimien työ on yhtä suuri kuin lopun mekaaninen energia. Liikemäärä: p = m v vektoreina, "
            "impulssiperiaate summa F kertaa delta t = delta p ja liikemäärän säilyminen törmäyksessä. Sovellukset: törmäyksessä liikemäärä "
            "säilyy mutta liike-energia vain kimmoisassa, pysähtymismatka on reaktiomatka ja jarrutusmatka, ja vesivoimalan teho "
            "on eeta rho Q g h.", width=380, size=20)
    groups = [
        ("energia", [(r"E_\text{k} = \tfrac12 mv^2", "liike-energia"), (r"E_\text{p} = mgh", "potentiaalienergia"),
                     (r"E_\text{mek,1} + W_\text{muut} = E_\text{mek,2}", "")]),
        ("liikemäärä", [(r"\overline{p} = m\overline{v}", "määritelmä"), (r"\Sigma\overline{F}\,\Delta t = \Delta\overline{p}", "impulssi"),
                        (r"\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}", "säilyminen")]),
        ("sovellukset", [(r"\text{törmäys: } p \text{ säilyy, } E_\text{k} \text{ ei aina}", ""),
                      (r"s_\text{p} = v_0 t_\text{r} + v_0^2/(2a)", "pysähtyminen"), (r"P = \eta\rho Qgh", "vesivoima")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 150, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{säilymislait}", "middle", INK)
    f.tex(190, hub_y + 51, r"\text{energia ja liikemäärä}", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 66 + j * 34
            f.tex(x_box + 14, yy, law, "start", INK, size=18 if len(law) > 34 else None)
            if word: f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


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


FIGURES = {"hero": hero, "kartta": kartta, "tormays": tormays}
REUSE = {"kartta": "reveals: the key laws of FY4 mechanical energy and momentum",
         "tormays": "reveals: the coupled wagons keep the momentum and lose half of the kinetic energy"}
