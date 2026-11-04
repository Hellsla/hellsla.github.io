"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-13` writes them into lesson.md.
A plate capacitor seen from the side: metal plates in aluminium grey, positive charges red (#c92a2a), negative ones
(electrons) blue (#1971c2) as in the other FY6 chapters, field lines green (#2b8a3e, as in the chapter on the
uniform field) with filled heads and the label $\\overline{E}$, energy orange. Circuit symbols IEC (a source as a long + plate and a short − plate). Every label LaTeX.
The numbers are those of lesson-answers.py and answers.py."""
import math
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    GLASS, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN, PAPER, ICE, n
import herolib as H

PLUS, MINUS, FIELD = HOT, COLD, GOOD


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')


def source(f, x, y, gap=16):
    """A source on a vertical wire at x, centred on y: the long thin plate (+) above, the short thick plate (−) below."""
    f.rect(x - 28, y - gap / 2 - 3, 56, gap + 6, WHITE)
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def charge(f, x, y, sign, r=8):
    """A charge as a small filled circle with a white + or − drawn in lines (no text)."""
    f.circle(x, y, r, PLUS if sign > 0 else MINUS, WHITE, 1.5)
    f.line(x - r * 0.55, y, x + r * 0.55, y, WHITE, 2.2)
    if sign > 0: f.line(x, y - r * 0.55, x, y + r * 0.55, WHITE, 2.2)


def plate(f, x, y0, y1, w=12):
    f.rect(x - w / 2, y0, w, y1 - y0, ALUMINIUM, INK, 2.5)


def dipole(f, x, y, rx=15, ry=7.5):
    """A polarised molecule of the dielectric: its negative side (blue) toward the + plate on the left."""
    f.path(f"M{n(x)},{n(y - ry)} A{rx},{ry} 0 0 0 {n(x)},{n(y + ry)} Z", COLD_LIGHT, MINUS, 1.5)
    f.path(f"M{n(x)},{n(y - ry)} A{rx},{ry} 0 0 1 {n(x)},{n(y + ry)} Z", HOT_LIGHT, PLUS, 1.5)


def dim(f, x1, x2, y, label):
    """A dimension line with arrowheads at both ends and its label under it."""
    f.arrow((x1 + x2) / 2, y, x1, y, INK, 2, 10); f.arrow((x1 + x2) / 2, y, x2, y, INK, 2, 10)
    f.line(x1, y - 9, x1, y + 9, INK, 2); f.line(x2, y - 9, x2, y + 9, INK, 2)
    f.tex((x1 + x2) / 2, y + 24, label, "middle", w=40)


# --- Ydinajatus: the plate capacitor charged by a source --------------------------------------------------------
def structure():
    f = new("fy613-rakenne", 350, "Kaavakuva, ei mittakaavassa: levykondensaattori kytkettynä jännitelähteeseen. "
            "Vasemmalla jännitelähde, jonka jännite on U ja plusnapa ylhäällä. Plusnavasta johto kulkee vasempaan "
            "metallilevyyn ja miinusnavasta oikeaan. Levyt ovat pystyssä vastakkain, ja niiden välinen etäisyys on d. "
            "Vasemman levyn sisäpinnalla on viisi punaista positiivista varausta, yhteensä +Q, ja oikean levyn "
            "sisäpinnalla viisi sinistä negatiivista varausta, yhteensä −Q. Levyjen välissä on eristettä, tässä ilmaa, "
            "ja siinä tasavälisiä vaakasuoria vihreitä kenttäviivoja, joiden nuolet osoittavat positiivisesta levystä "
            "negatiiviseen: homogeeninen sähkökenttä E.")
    xs, xl, xr, top, bot = 92, 262, 382, 104, 264
    wire(f, (xs, 177 - 8), (xs, 52), (xl, 52), (xl, top))
    wire(f, (xs, 177 + 8), (xs, 324), (xr, 324), (xr, bot))
    source(f, xs, 177)
    f.tex(xs - 36, 177, r"U", "end", w=30)
    f.tex(xs + 36, 164, r"+", "start", w=24)
    plate(f, xl, top, bot); plate(f, xr, top, bot)
    ys = [120 + 32 * k for k in range(5)]
    for y in ys:
        charge(f, xl + 16, y, +1); charge(f, xr - 16, y, -1)
    for k in range(4):
        y = (ys[k] + ys[k + 1]) / 2
        f.arrow(xl + 22, y, xr - 22, y, FIELD, 2.5, 13)
    f.tex((xl + xr) / 2, 84, r"\overline{E}", "middle", FIELD, w=40)
    f.tex(xl - 22, 184, r"+Q", "end", PLUS, w=60)
    f.tex(xr + 22, 184, r"-Q", "start", MINUS, w=60)
    dim(f, xl + 6, xr - 6, 284, r"d")
    f.tex(452, 112, r"\text{metallilevy}", "start", w=136)
    f.line(447, 112, xr + 9, 118, MUTED, 1.5)
    f.tex(452, 294, r"\text{eriste}", "start", w=90)
    f.line(447, 294, xr - 36, 262, MUTED, 1.5)
    return f.svg()


# --- Ydinajatus: charging and discharging through a resistor (schematic) ----------------------------------------
def charging():
    f = new("fy613-lataus", 420, "Kaavakuva, ei mittakaavassa: kaksi kuvaajaa yhteisellä aika-akselilla. Ylempi: "
            "kondensaattorin jännite U_C ajan t funktiona. Latauksessa jännite nousee aluksi jyrkästi ja sitten yhä "
            "loivemmin kohti lähteen jännitettä U_0, joka on merkitty katkoviivalla. Purkautumisessa jännite laskee "
            "aluksi jyrkästi ja sitten yhä loivemmin kohti nollaa. Alempi: virta I. Latauksen alussa virta on suurin ja "
            "pienenee vähitellen nollaan. Purkautumisen alussa virta on suurin mutta vastakkaissuuntainen eli negatiivinen, "
            "ja sen suuruus pienenee vähitellen nollaan. Pystysuora katkoviiva erottaa latauksen ja purkautumisen.")
    T, t1, k = 10.0, 5.0, 1.0
    up = Axes(f, (92, 182), (470, 72), x=(0, T), y=(0, 1.25), xticks=[], yticks=[1], yfmt=lambda v: "",
              xlabel=r"t", ylabel=r"U_C", origin_label=False)
    lo = Axes(f, (92, 404), (470, 276), x=(0, T), y=(-1.15, 1.15), xticks=[], yticks=[], xlabel=r"t", ylabel=r"I",
              origin_label=False, x_at=0)
    f.line(92, up.Y(1), 470, up.Y(1), MUTED, 1.5, "6 5")
    f.tex(80, up.Y(1), r"U_0", "end", w=40)
    uc = lambda t: 1 - math.exp(-t / k) if t <= t1 else (1 - math.exp(-t1 / k)) * math.exp(-(t - t1) / k)
    up.curve(uc, 0, T * 0.97, COLD, 3, steps=200)
    lo.curve(lambda t: 0.95 * math.exp(-t / k), 0, t1, HOT, 3, steps=100)
    lo.curve(lambda t: -0.95 * (1 - math.exp(-t1 / k)) * math.exp(-(t - t1) / k), t1, T * 0.97, HOT, 3, steps=100)
    lo.line([(t1, 0.95 * math.exp(-t1 / k)), (t1, -0.95 * (1 - math.exp(-t1 / k)))], HOT, 3)
    f.line(up.X(t1), 72, up.X(t1), 404, MUTED, 1.5, "6 5")
    f.tex(up.X(t1 / 2), 220, r"\text{lataus}", "middle", w=100)
    f.tex(up.X((t1 + T) / 2), 220, r"\text{purkautuminen}", "middle", w=180)
    return f.svg()


# --- Ydinajatus: the dielectric weakens the field (the same charge) ---------------------------------------------
def dielectric_panel(f, x0, with_dielectric):
    xl, xr, top, bot = x0 + 52, x0 + 232, 76, 256
    if with_dielectric:
        f.rect(xl + 6, top, xr - xl - 12, bot - top, GLASS)
    plate(f, xl, top, bot); plate(f, xr, top, bot)
    ys = [92 + 37 * k for k in range(5)]
    for y in ys:
        charge(f, xl + 16, y, +1); charge(f, xr - 16, y, -1)
    if with_dielectric:
        for r in range(3):
            for c in range(3):
                dipole(f, xl + 47 + 43 * c, 110 + 56 * r)
        for y in (138, 194):
            f.arrow(xl + 28, y, xr - 28, y, FIELD, 2.5, 13)
    else:
        for k in range(4):
            y = (ys[k] + ys[k + 1]) / 2
            f.arrow(xl + 22, y, xr - 22, y, FIELD, 2.5, 13)
    f.tex((xl + xr) / 2, 36, r"\text{eriste}" if with_dielectric else r"\text{ilma}", "middle", w=110)
    f.tex((xl + xr) / 2, 290, r"\text{sama } Q", "middle", w=130)
    f.tex((xl + xr) / 2, 324, r"\text{pienempi } U" if with_dielectric else r"\text{suurempi } U", "middle", w=200)


def dielectric():
    f = new("fy613-eriste", 350, "Kaavakuva, ei mittakaavassa: kaksi samanlaista levykondensaattoria, joissa on sama "
            "varaus Q: vasemmalla levyssä viisi positiivista ja oikealla viisi negatiivista varausta. Vasemmanpuoleisen "
            "kondensaattorin levyjen välissä on ilmaa ja neljä kenttäviivaa. Oikeanpuoleisen levyjen välissä on eristettä, "
            "jonka yhdeksän molekyyliä kolmessa rivissä ovat polarisoituneet: kunkin molekyylin negatiivinen puoli on kääntynyt kohti positiivista "
            "levyä ja positiivinen puoli kohti negatiivista levyä. Eristeessä kenttäviivoja on vain kaksi, joten kenttä "
            "on heikompi. Ilmaa sisältävän kondensaattorin jännite U on suurempi, eristettä sisältävän pienempi.")
    dielectric_panel(f, 0, False)
    f.line(300, 20, 300, 336, RULE, 1.5, "6 6")
    dielectric_panel(f, 300, True)
    return f.svg()


# --- Kaava: the energy as the area under the (Q, U) graph -------------------------------------------------------
def energy():
    f = new("fy613-energia", 350, "Kaavakuva: kondensaattorin jännite U varauksen Q funktiona latauksen aikana. Kuvaaja "
            "on origon kautta kulkeva suora, koska jännite kasvaa samassa suhteessa kuin varaus. Suoran alle on piirretty "
            "kapeita pylväitä: kukin kuvaa pientä varausta, joka siirretään senhetkisen jännitteen yli, ja pylvään "
            "pinta-ala on sen saama energia. Pylväät ovat alussa matalia ja lopussa korkeita. Suoran ja Q-akselin väliin "
            "jäävä kolmio on sävytetty oranssiksi; sen pinta-ala on kondensaattorin energia W = ½QU. Vaakasuora "
            "katkoviiva kulkee keskimääräisen jännitteen U/2 kohdalla, ja sen alle jäävä suorakulmio on yhtä suuri "
            "kuin kolmio.")
    ax = Axes(f, (96, 290), (440, 70), x=(0, 1.15), y=(0, 1.2), xticks=[1], yticks=[0.5, 1],
              xfmt=lambda v: "Q", yfmt=lambda v: {0.5: r"\tfrac{U}{2}", 1: "U"}[v],
              xlabel=r"\text{varaus}", ylabel=r"\text{jännite}", origin_label=False)
    ax.area([(0, 0), (1, 1), (1, 0)], HEAT_LIGHT, 0.55)
    N = 8
    for i in range(N):
        q0, q1 = i / N, (i + 1) / N
        f.rect(ax.X(q0) + 1, ax.Y(q0), ax.X(q1) - ax.X(q0) - 2, ax.Y(0) - ax.Y(q0), HEAT_LIGHT, HEAT, 1.5)
    ax.line([(0, 0), (1, 1)], INK, 3)
    ax.line([(0, 0.5), (1, 0.5)], MUTED, 1.5, "6 5")
    ax.line([(1, 0), (1, 1)], MUTED, 1.5, "6 5")
    ax.point(1, 1, INK, 6)
    f.tex(ax.X(0.66), ax.Y(0.2), r"W = \tfrac{1}{2} Q U", "middle", w=170, bg=True)
    f.tex(ax.X(0.86), ax.Y(1.06), r"U = \tfrac{Q}{C}", "end", w=120)
    return f.svg()


# --- a task figure: U as a function of Q for one capacitor ------------------------------------------------------
def ex_qu():
    f = new("fy613-exqu", 340, "Kuvaaja mittakaavassa: kondensaattorin jännite U voltteina sen varauksen Q funktiona "
            "mikrocoulombeina, ruudukon välit 10 µC ja 2 V. Kuvaaja on suora, joka alkaa origosta ja päättyy pisteeseen "
            "(70 µC; 14 V).")
    ax = Axes(f, (92, 284), (476, 56), x=(0, 70), y=(0, 14), xticks=[10, 20, 30, 40, 50, 60, 70],
              yticks=[2, 4, 6, 8, 10, 12, 14], xlabel=r"Q\ (\mu\text{C})", ylabel=r"U\ (\text{V})")
    ax.line([(0, 0), (70, 14)], COLD, 3)
    return f.svg()


# --- opening illustration: a camera flash going off in a dim room ------------------------------------------------
def hero():
    f = H.hero("fy613-hero", "Kuvitus: hämärässä huoneessa pöydällä on kolmijalan päällä kamera, jonka salamavalo "
               "välähtää kirkkaasti. Salaman valo leviää viuhkana oikealle kohti pöydän päässä olevaa kukkamaljakkoa. "
               "Kameran vieressä pöydällä on kaksi AA-paristoa, jotka lataavat salaman kondensaattorin.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 400, H.grad(f, "fy613h-wall", "#6c757d", "#8a96a3"))
    # the flash's light: a wide fan of warm light to the right
    f.defs_add(f'<radialGradient id="fy613h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{WHITE}" '
               f'stop-opacity="0.95"/><stop offset="0.35" stop-color="{HEAT_LIGHT}" stop-opacity="0.55"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<linearGradient id="fy613h-fan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{WHITE}" '
               f'stop-opacity="0.85"/><stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></linearGradient>')
    f.path("M612,214 L1180,40 L1180,470 Z", "url(#fy613h-fan)")
    f.circle(612, 214, 190, "url(#fy613h-glow)")
    # the table
    f.rect(0, 400, 1200, 200, H.grad(f, "fy613h-table", SAND, SAND_DARK))
    f.rect(0, 392, 1200, 16, GRAIN)
    for k in range(5):
        y = 436 + 34 * k
        f.path(f"M0,{y} C320,{y - 6} 760,{y + 8} 1200,{y - 2}", stroke=GRAIN, w=2, extra='stroke-opacity="0.4"')
    # the tripod
    for x2 in (440, 530, 620):
        f.line(530, 330, x2, 452, INK, 7, cap="round")
    f.rect(518, 296, 24, 40, IRON, INK, 3, rx=4)
    # the camera body, lens and flash
    f.rect(400, 196, 260, 110, INK, None, 0, rx=18)
    f.rect(410, 206, 240, 90, IRON, None, 0, rx=12)
    f.rect(430, 176, 80, 26, INK, None, 0, rx=6)
    f.circle(500, 252, 52, INK)
    f.circle(500, 252, 40, METAL_EDGE)
    f.circle(500, 252, 28, "#2f74b5")
    f.circle(490, 242, 9, ICE)
    f.rect(584, 200, 56, 28, WHITE, INK, 3, rx=6)                   # the flash window, lit
    f.rect(592, 206, 40, 16, HEAT_LIGHT, None, 0, rx=4)
    f.circle(632, 270, 9, HOT)                                      # the ready light
    # two AA cells on the table
    for i, x in enumerate((300, 340)):
        f.rect(x, 440 - 6 * i, 30, 92, GOOD, INK, 3, rx=6)
        f.rect(x + 9, 432 - 6 * i, 12, 10, ALUMINIUM, INK, 2, rx=2)
    # a vase with flowers in the light
    f.path("M960,420 Q936,360 962,320 L1018,320 Q1044,360 1020,420 Z", COLD_LIGHT, INK, 3)
    for dx, h, col in ((-26, 120, HOT), (0, 150, HEAT), (24, 110, HOT_LIGHT)):
        f.line(990 + dx * 0.3, 322, 990 + dx, 322 - h, GOOD, 4, cap="round")
        f.circle(990 + dx, 322 - h, 18, col, INK, 2.5)
        f.circle(990 + dx, 322 - h, 6, HEAT_LIGHT)
    return f.svg()


FIGURES = {"hero": hero, "rakenne": structure, "lataus": charging, "eriste": dielectric, "energia": energy,
           "ex-qu": ex_qu}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "rakenne": "reveals: a source charges the plates to +Q and -Q with a uniform field from + to - between them",
    "lataus": "reveals: the charging and discharging curves (U_C rises/falls gradually, the current is largest at first)",
    "eriste": "reveals: with the same Q a dielectric weakens the field and lowers U (polarised molecules)",
    "energia": "reveals: W = 1/2 Q U as the area under the (Q, U) line, the mean voltage U/2",
    "ex-qu": "safe: a capacitor's (Q, U) line from the origin to (70 µC; 14 V), no energy or capacitance written",
}
