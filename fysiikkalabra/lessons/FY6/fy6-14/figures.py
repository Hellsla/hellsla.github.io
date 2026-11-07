"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-14` writes them into lesson.md.
Circuit diagrams with IEC symbols: a resistor is a rectangle, a source a long thin (+) and a short thick (−) plate, a
diode a triangle pointing the way the current can pass with a bar (the cathode), an LED the same with two light arrows.
Conventional current from + to −, violet (#7048e8) as in the other FY6 chapters; every label LaTeX. Graphs to scale,
computed with the models of lesson-answers.py (the same as the simulation's)."""
from math import exp, log
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GLASS, ICE, ALUMINIUM, METAL_EDGE, IRON, COPPER, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN,
                    PAPER, WATER, n)
import herolib as H

CUR = "#7048e8"     # conventional current (FY6)
RED_LED, BLUE_LED = HOT, COLD
COMP = {"pii": (0.70, 0.040), "punainen": (1.90, 0.050), "sininen": (2.90, 0.060), "vihrea": (2.20, 0.050)}
M_PV, ISC, UOC = 0.40, 0.200, 6.0
I0 = ISC / (exp(UOC / M_PV) - 1)


def i_led(c, u):
    """mA at U_D = u (V): I = I_s (exp(u / m) - 1), 10 mA at U_ref."""
    ur, m = COMP[c]
    return 0.0 if u <= 0 else 10 * (exp(u / m) - 1) / (exp(ur / m) - 1)


def u_led(c, i):
    ur, m = COMP[c]
    return m * log(i / 10 * (exp(ur / m) - 1) + 1)


def i_pv(G, u): return max(0.0, (ISC * G / 1000 - I0 * (exp(u / M_PV) - 1)) * 1000)     # mA
def u_open(G): return M_PV * log(ISC * G / 1000 / I0 + 1)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- circuit pieces -------------------------------------------------------------------------------------------
def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False):
    w, h = (24, 60) if vertical else (60, 24)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def cell(f, x, y, gap=14, half=24):
    """A source on a vertical wire at x, centred on y: the long thin plate (+) above, the short thick (−) below."""
    f.line(x - half, y - gap / 2, x + half, y - gap / 2, INK, 3)
    f.line(x - half / 2, y + gap / 2, x + half / 2, y + gap / 2, INK, 7)


def head(f, x, y, d, colour=CUR):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", colour)


def diode(f, x, y, down=True, led=None, lit=False, gid=None):
    """A diode on a vertical wire at x, centred on y, 32 units tall. down: the triangle points down (the current can
    pass downward). led: the LED's colour (two light arrows); lit: a glow behind it."""
    if led and lit:
        f.defs_add(f'<radialGradient id="{gid}" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{led}" stop-opacity="0.55"/>'
                   f'<stop offset="1" stop-color="{led}" stop-opacity="0"/></radialGradient>')
        f.circle(x, y, 46, f"url(#{gid})")
    t, b = (y - 14, y + 14) if down else (y + 14, y - 14)
    fill = led if (led and lit) else WHITE
    f.path(f"M{n(x - 16)},{n(t)} L{n(x + 16)},{n(t)} L{n(x)},{n(b)} Z", fill, INK, 2.5)
    f.line(x - 17, b, x + 17, b, INK, 3)
    if led:
        for dy in (-9, 3):
            f.arrow(x + 22, y + dy, x + 40, y + dy - 15, INK, 2, 9)


# --- Ydinajatus: forward and reverse ----------------------------------------------------------------------------
def suunnat_panel(f, x0, forward):
    xs, xd, top, bot, yd = x0 + 52, x0 + 230, 70, 286, 178
    wire(f, (xs, 171), (xs, top), (xd, top), (xd, yd - 15))
    wire(f, (xd, yd + 15), (xd, bot), (xs, bot), (xs, 185))
    cell(f, xs, 178)
    f.tex(xs - 32, 178, "U", "end", w=30)
    f.tex(xs + 30, 156, "+", "start", w=24)
    resistor(f, (xs + xd) / 2, top)
    f.tex((xs + xd) / 2, top - 30, "R", "middle", w=30)
    diode(f, xd, yd, down=forward, led=RED_LED, lit=forward, gid=f"fy614-glow{int(forward)}")
    if forward:
        head(f, xs + 44, top, "r"); f.tex(xs + 44, top - 28, "I", "middle", CUR, w=24)
        head(f, xd, 240, "d"); head(f, (xs + xd) / 2, bot, "l")
        f.tex(xd - 26, yd - 22, r"\text{anodi}", "end", w=84)
        f.tex(xd - 26, yd + 24, r"\text{katodi}", "end", w=90)
        f.tex(x0 + 141, 330, r"\text{päästösuunta}", "middle", w=190)
    else:
        f.tex(x0 + 141, 178, r"I = 0", "middle", w=70)
        f.tex(x0 + 141, 330, r"\text{estosuunta}", "middle", w=160)


def suunnat():
    f = new("fy614-suunnat", 352, "Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Kummassakin jännitelähde U, "
            "etuvastus R ja punainen LED ovat sarjassa, ja lähteen plusnapa on ylhäällä. Vasemmalla LEDin kolmio osoittaa "
            "alaspäin eli virran kulkusuuntaan: LEDin anodi on yläpuolella kohti lähteen plusnapaa ja katodi eli poikkiviiva "
            "alapuolella. LED palaa, ja violetit nuolet näyttävät virran I kulkevan plusnavalta vastuksen ja LEDin kautta "
            "miinusnavalle. Tämä on päästösuunta. Oikealla sama LED on käännetty toisin päin, kolmio osoittaa ylöspäin. "
            "LED ei pala, eikä piirissä kulje virtaa: I = 0. Tämä on estosuunta.")
    suunnat_panel(f, 8, True)
    f.line(300, 24, 300, 340, RULE, 1.5, "6 6")
    suunnat_panel(f, 308, False)
    return f.svg()


# --- Ydinajatus: the (U, I) characteristics -----------------------------------------------------------------------
def ominaiskayra():
    f = new("fy614-ominaiskayra", 360, "Kuvaaja mittakaavassa, laskettu luvun diodimallilla: diodin virta I milliampeereina "
            "sen jännitteen U_D funktiona voltteina, jännite välillä −2 V … 4 V ja virta 0–30 mA. Negatiivisilla jännitteillä "
            "eli estosuunnassa virta on nolla kaikilla kolmella komponentilla. Päästösuunnassa piidiodin virta pysyy lähes "
            "nollana noin 0,6 volttiin asti ja kasvaa sitten jyrkästi, ja 10 milliampeerin virta saavutetaan 0,70 voltissa. "
            "Punaisen LEDin käyrä nousee jyrkästi noin 1,8 voltista alkaen, ja 10 mA saavutetaan 1,9 voltissa. Sinisen LEDin "
            "käyrä nousee noin 2,8 voltista alkaen, ja 10 mA saavutetaan 2,9 voltissa. Ruudukon välit ovat 1 V ja 5 mA.")
    ax = Axes(f, (96, 300), (470, 66), x=(-2, 4), y=(0, 30), xticks=[-2, -1, 0, 1, 2, 3, 4], yticks=[5, 10, 15, 20, 25, 30],
              xlabel=r"U_\text{D}\ (\text{V})", ylabel=r"I\ (\text{mA})", origin_label=False)
    f.tex(ax.X(-2), 324, "-2", "middle")
    ax.line([(-2, 0), (0, 0)], INK, 3)
    for c, col, lx in (("pii", INK, None), ("punainen", RED_LED, None), ("sininen", BLUE_LED, None)):
        u1 = u_led(c, 30)
        ax.curve(lambda u, c=c: i_led(c, u), 0, u1, col, 3, steps=200)
    # a legend in the empty reverse half, above the axis
    for k, (t, col) in enumerate(((r"\text{piidiodi}", INK), (r"\text{punainen LED}", RED_LED), (r"\text{sininen LED}", BLUE_LED))):
        y = 84 + 36 * k
        f.line(108, y, 136, y, col, 3)
        f.tex(144, y, t, "start", col, w=150)
    f.tex(ax.X(-1), ax.Y(0) - 22, r"I = 0", "middle", bg=True, w=70)
    return f.svg()


# --- Ydinajatus: the solar panel's (U, I) curve at two light levels -------------------------------------------------
def kenno():
    f = new("fy614-kenno", 360, "Kuvaaja mittakaavassa, laskettu luvun aurinkopaneelimallilla: pienen aurinkopaneelin virta I "
            "milliampeereina sen jännitteen U funktiona voltteina kahdella irradianssilla. Kun irradianssi G on "
            "1000 W/m², käyrä alkaa pystyakselilta oikosulkuvirrasta I_k = 200 mA, pysyy lähes vaakasuorana noin neljään "
            "volttiin asti ja laskee sitten jyrkästi vaaka-akselille tyhjäkäyntijännitteeseen U_t = 6,0 V. Kun valon "
            "voimakkuus on 500 W/m², oikosulkuvirta on puolet eli 100 mA, mutta tyhjäkäyntijännite on 5,7 V, vain vähän "
            "pienempi. Ruudukon välit ovat 1 V ja 50 mA.")
    ax = Axes(f, (96, 300), (476, 60), x=(0, 7), y=(0, 250), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[50, 100, 150, 200, 250],
              xlabel=r"U\ (\text{V})", ylabel=r"I\ (\text{mA})")
    for G, col in ((1000, WATER), (500, COLD_LIGHT)):
        ut = u_open(G)
        ax.curve(lambda u, G=G: i_pv(G, u), 0, ut, WATER if G == 1000 else "#4f8fbf", 3, steps=200, dash=None if G == 1000 else "10 7")
        ax.point(0, ISC * G, INK if G == 1000 else MUTED, 6)
        ax.point(ut, 0, INK if G == 1000 else MUTED, 6)
    f.tex(ax.X(1.2), ax.Y(222), r"G = 1000\,\text{W/m}^2", "start", WATER, w=176)
    f.tex(ax.X(1.2), ax.Y(124), r"G = 500\,\text{W/m}^2", "start", "#4f8fbf", w=164)
    f.tex(ax.X(0) + 14, ax.Y(200) - 4, r"I_\text{k}", "start", bg=True, w=40)
    f.tex(ax.X(u_open(1000)) + 6, ax.Y(0) - 30, r"U_\text{t}", "start", bg=True, w=40)
    return f.svg()


# --- Kaava: the series resistor and the voltages to scale -----------------------------------------------------------
def etuvastus():
    f = new("fy614-etuvastus", 340, "Vasemmalla kytkentäkaavio, ei mittakaavassa: jännitelähde U, etuvastus R ja LED "
            "sarjassa, LED päästösuunnassa. Violetti nuoli näyttää virran I kulkevan lähteen plusnavalta vastuksen ja LEDin "
            "kautta miinusnavalle. Vastuksen jännite on U_R ja LEDin jännite U_D. Oikealla pylväs mittakaavassa: lähteen "
            "jännite 6,0 V jakautuu vastuksen jännitteeksi 4,0 V ja LEDin jännitteeksi 2,0 V, joten U = U_R + U_D.")
    xs, xd, top, bot, yd = 60, 290, 70, 286, 178
    wire(f, (xs, 171), (xs, top), (xd, top), (xd, yd - 15))
    wire(f, (xd, yd + 15), (xd, bot), (xs, bot), (xs, 185))
    cell(f, xs, 178)
    f.tex(xs - 32, 178, "U", "end", w=30)
    f.tex(xs + 30, 156, "+", "start", w=24)
    resistor(f, 175, top)
    f.tex(175, top - 30, "R", "middle", w=30)
    f.tex(175, top + 34, r"U_R", "middle", w=50)
    diode(f, xd, yd, True, RED_LED, True, "fy614-glow-k")
    f.tex(xd - 26, yd, r"U_\text{D}", "end", w=50)
    head(f, 110, top, "r"); f.tex(110, top - 28, "I", "middle", CUR, w=24)
    head(f, xd, 244, "d"); head(f, 175, bot, "l")
    # the bar: 6,0 V = 4,0 V + 2,0 V, 36 px per volt
    bx, by0, k = 500, 300, 36
    f.rect(bx, by0 - 6 * k, 44, 4 * k, RULE_LIGHT, INK, 2.5)
    f.rect(bx, by0 - 2 * k, 44, 2 * k, HOT_LIGHT, INK, 2.5)
    f.tex(bx - 12, by0 - 4 * k, r"U_R = 4{,}0\,\text{V}", "end", w=128)
    f.tex(bx - 12, by0 - k, r"U_\text{D} = 2{,}0\,\text{V}", "end", w=128)
    f.tex(bx + 22, by0 - 6 * k - 26, r"U = 6{,}0\,\text{V}", "middle", w=130)
    return f.svg()


# --- Kaava: the power of the panel and its maximum ---------------------------------------------------------------------
def teho():
    f = new("fy614-teho", 470, "Kaksi kuvaajaa mittakaavassa yhteisellä jänniteakselilla, laskettu luvun "
            "aurinkopaneelimallilla, kun irradianssi on 1000 W/m². Ylempi: paneelin virta I milliampeereina jännitteen U "
            "funktiona, käyrä 200 mA:sta 6,0 volttiin. Kohdassa 5,0 V ja 184 mA on piste, ja sen ja origon väliin jäävä "
            "suorakulmio on sävytetty oranssiksi: sen pinta-ala on teho P = U I. Alempi: teho P watteina jännitteen funktiona. "
            "Teho on nolla oikosulussa ja tyhjäkäynnissä ja suurin, noin 0,92 W, kun jännite on noin 5,0 V. Katkoviiva "
            "yhdistää molempien kuvaajien maksimitehopisteet.")
    top = Axes(f, (96, 204), (476, 62), x=(0, 7), y=(0, 250), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[100, 200],
               xlabel=r"U\ (\text{V})", ylabel=r"I\ (\text{mA})", xfmt=lambda v: "", origin_label=False)
    lo = Axes(f, (96, 420), (476, 270), x=(0, 7), y=(0, 1.0), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[0.5, 1.0],
              xlabel=r"U\ (\text{V})", ylabel=r"P\ (\text{W})", yfmt=lambda v: fi(v, 1))
    ut = u_open(1000)
    um = max((ut * k / 2000 for k in range(2001)), key=lambda u: u * i_pv(1000, u))
    im = i_pv(1000, um)
    top.area([(0, 0), (0, im), (um, im), (um, 0)], HEAT_LIGHT, 0.6)
    top.curve(lambda u: i_pv(1000, u), 0, ut, WATER, 3, steps=200)
    lo.curve(lambda u: u * i_pv(1000, u) / 1000, 0, ut, HEAT, 3, steps=200)
    f.line(top.X(um), top.Y(im), lo.X(um), lo.Y(0), MUTED, 1.5, "6 5")
    top.point(um, im, INK, 6)
    lo.point(um, um * im / 1000, INK, 6)
    f.tex(top.X(um / 2), top.Y(im / 2), r"P = U I", "middle", bg=True, w=96)
    f.tex(lo.X(um) - 12, lo.Y(um * im / 1000) - 26, r"\text{maksimitehopiste}", "end", bg=True, w=150)
    return f.svg()


# --- task figures ------------------------------------------------------------------------------------------------------
def ex_led():
    f = new("fy614-exled", 350, "Kuvaaja mittakaavassa: vihreän LEDin virta I milliampeereina sen jännitteen U_D funktiona "
            "voltteina. Vaaka-akselin ruudukon väli on 0,2 V ja numerot on merkitty 0,4 voltin välein, pystyakselin ruudukon "
            "väli on 5 mA. Virta on lähes nolla noin kahteen volttiin asti, minkä jälkeen käyrä nousee jyrkästi ja päättyy "
            "30 milliampeeriin hieman 2,2 voltin oikealle puolelle.")
    xt = [round(0.2 * k, 1) for k in range(1, 16)]
    ax = Axes(f, (96, 290), (480, 62), x=(0, 3.0), y=(0, 30), xticks=xt, yticks=[5, 10, 15, 20, 25, 30],
              xlabel=r"U_\text{D}\ (\text{V})", ylabel=r"I\ (\text{mA})",
              xfmt=lambda v: fi(v, 1) if abs(v / 0.4 - round(v / 0.4)) < 1e-6 else "")
    ax.curve(lambda u: i_led("vihrea", u), 0, u_led("vihrea", 30), GOOD, 3, steps=300)
    return f.svg()


def ex_kenno():
    f = new("fy614-exkenno", 340, "Kuvaaja mittakaavassa: aurinkopaneelin virta I milliampeereina sen jännitteen U "
            "funktiona voltteina, kun irradianssi pysyy samana. Ruudukon välit ovat 1 V ja 50 mA. Käyrä alkaa "
            "pystyakselilta 200 milliampeerista, pysyy lähes vaakasuorana noin neljään volttiin asti, taipuu alas noin viiden "
            "voltin kohdalla ja laskee jyrkästi vaaka-akselille kuuteen volttiin.")
    ax = Axes(f, (96, 290), (476, 62), x=(0, 7), y=(0, 250), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[50, 100, 150, 200, 250],
              xlabel=r"U\ (\text{V})", ylabel=r"I\ (\text{mA})")
    ax.curve(lambda u: i_pv(1000, u), 0, u_open(1000), WATER, 3, steps=200)
    return f.svg()


# --- opening illustration: a breadboard with two LEDs, one lit and one dark ------------------------------------------------
def hero():
    f = H.hero("fy614-hero", "Kuvitus: koulun työpöydällä on kytkentälevy. Vasemmalla on kolmen AA-pariston paristokotelo, "
               "josta punainen ja musta johto kulkevat kytkentälevylle. Levyllä on vastus ja kaksi punaista LEDiä. "
               "Ensimmäinen LED loistaa kirkkaasti, toinen samanlainen LED on kytketty toisin päin, eikä se pala. Taustalla "
               "ikkunan takana paistaa aurinko, ja ikkunalaudalla on pieni aurinkopaneeli.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 380, H.grad(f, "fy614h-wall", RULE_LIGHT, PAPER))
    # the window with the sun and a small panel on the sill
    f.rect(840, 48, 300, 250, H.grad(f, "fy614h-sky", ICE, GLASS), INK, 4, rx=6)
    H.sun(f, "fy614h", 1050, 126, r=38)
    f.line(990, 48, 990, 298, INK, 4)
    f.rect(820, 296, 340, 18, SAND_DARK, INK, 3, rx=3)
    f.path("M866,294 L896,236 L980,236 L950,294 Z", INK, INK, 3)
    for i in range(3):
        for j in range(2):
            x0, y0 = 872 + 26 * i + 15 * j, 288 - 28 * j
            f.path(f"M{x0},{y0} L{x0 + 12},{y0 - 24} L{x0 + 34},{y0 - 24} L{x0 + 22},{y0} Z", WATER)
    # the table
    f.rect(0, 380, 1200, 220, H.grad(f, "fy614h-table", SAND_LIGHT, SAND))
    f.rect(0, 374, 1200, 12, GRAIN)
    for k in range(4):
        y = 430 + 44 * k
        f.path(f"M0,{y} C340,{y - 6} 780,{y + 8} 1200,{y - 2}", stroke=GRAIN, w=2, extra='stroke-opacity="0.35"')
    # the battery holder with three AA cells
    f.rect(118, 420, 236, 104, INK, None, 0, rx=10)
    for i in range(3):
        y = 432 + 28 * i
        f.rect(132, y, 196, 24, GOOD, None, 0, rx=6)
        f.rect(328, y + 6, 12, 12, ALUMINIUM, None, 0, rx=2)
    # the breadboard
    f.rect(420, 420, 400, 140, WHITE, INK, 3, rx=8)
    f.line(436, 438, 804, 438, HOT, 3); f.line(436, 542, 804, 542, COLD, 3)
    f.rect(430, 486, 380, 8, RULE_LIGHT)
    for i in range(23):
        for j in range(4):
            f.circle(444 + 16 * i, 454 + 13 * j, 2.6, RULE)
            f.circle(444 + 16 * i, 504 + 13 * j, 2.6, RULE)
    # wires from the holder to the rails
    f.path("M354,444 C392,444 400,438 444,438", stroke=HOT, w=6, extra='stroke-linecap="round"')
    f.path("M354,500 C392,500 400,542 444,542", stroke=INK, w=6, extra='stroke-linecap="round"')
    # the resistor: body with colour bands, leads into the board
    f.line(476, 454, 476, 420, ALUMINIUM, 4); f.line(556, 454, 556, 420, ALUMINIUM, 4)
    f.path("M476,420 C476,396 496,392 516,392 C536,392 556,396 556,420", stroke=ALUMINIUM, w=4)
    f.rect(490, 380, 52, 26, SAND_LIGHT, INK, 2.5, rx=12)
    for k, col in enumerate((HEAT, HEAT, COPPER, IRON)):
        f.rect(498 + 10 * k, 381, 5, 24, col)
    # LED 1: lit, with its glow
    f.defs_add(f'<radialGradient id="fy614h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{WHITE}" stop-opacity="0.95"/>'
               f'<stop offset="0.25" stop-color="{HOT_LIGHT}" stop-opacity="0.75"/><stop offset="1" stop-color="{HOT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.circle(636, 352, 120, "url(#fy614h-glow)")
    for x in (626, 646):
        f.line(x, 452, x, 380, ALUMINIUM, 4)
    f.path("M614,384 L614,352 A22,22 0 0 1 658,352 L658,384 Z", HOT, INK, 3)
    f.rect(608, 380, 56, 10, HOT, INK, 3, rx=2)
    f.circle(628, 348, 7, WHITE)
    # LED 2: the same LED turned the other way round, dark
    for x in (736, 756):
        f.line(x, 452, x, 380, ALUMINIUM, 4)
    f.path("M724,384 L724,352 A22,22 0 0 1 768,352 L768,384 Z", HOT_LIGHT, INK, 3)
    f.rect(718, 380, 56, 10, HOT_LIGHT, INK, 3, rx=2)
    # wires on the board
    f.path("M444,438 L444,420 C444,404 460,404 476,420", stroke=HOT, w=4, extra='stroke-linecap="round"')
    f.path("M556,420 C580,440 600,440 626,452", stroke=COLD, w=4, extra='stroke-linecap="round"')
    f.path("M646,452 L646,520 L646,542", stroke=INK, w=4, extra='stroke-linecap="round"')
    f.path("M756,452 L756,438", stroke=HOT, w=4, extra='stroke-linecap="round"')
    f.path("M736,452 L736,542", stroke=INK, w=4, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero, "suunnat": suunnat, "ominaiskayra": ominaiskayra, "kenno": kenno, "etuvastus": etuvastus,
           "teho": teho, "ex-led": ex_led, "ex-kenno": ex_kenno}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "suunnat": "reveals: a diode conducts in the forward direction (anode toward +) and blocks in reverse, I = 0",
    "ominaiskayra": "reveals: (U, I) curves of a Si diode and red and blue LEDs, 10 mA at 0,70 / 1,9 / 2,9 V, I = 0 in reverse",
    "kenno": "reveals: a panel's (U, I) curve, I_k 200 mA and U_t 6,0 V at 1000 W/m2, half light halves I_k, U_t 5,7 V",
    "etuvastus": "reveals: 6,0 V = 4,0 V over R + 2,0 V over the LED (U = U_R + U_D)",
    "teho": "reveals: P = U I as the rectangle, maximum power about 0,92 W at about 5,0 V",
    "ex-led": "safe: a green LED's (U, I) curve on a 0,2 V / 5 mA grid, passing (2,2 V; 10 mA), no values written",
    "ex-kenno": "safe: a panel's (U, I) curve from 200 mA to 6,0 V on a 1 V / 50 mA grid, no power or point marked",
}
