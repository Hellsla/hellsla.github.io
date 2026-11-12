"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-9` writes them into lesson.md.
Circuit diagrams with IEC symbols: resistor a rectangle, source two plates (long +, short −), meters circles with
their letter; conventional current from + to − as violet arrows (#7048e8, as in the other FY6 chapters); energy flow
as filled orange arrows; potentials in blue; every label LaTeX. The numbers are those of lesson-answers.py."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    GLASS, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN, PAPER, n
import herolib as H

CUR = "#7048e8"     # conventional current (FY6)
POT = COLD          # potentials


# --- circuit pieces -------------------------------------------------------------------------------------------
def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=60, width=22):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def source(f, x, y, gap=16):
    """A source on a vertical wire at x, centred on y: the long thin plate (+) above, the short thick plate (−) below."""
    f.rect(x - 28, y - gap / 2 - 3, 56, gap + 6, WHITE)
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def lamp(f, x, y, r=20):
    f.circle(x, y, r, WHITE, INK, 3)
    d = r * 0.7071
    f.line(x - d, y - d, x + d, y + d, INK, 2.5); f.line(x - d, y + d, x + d, y - d, INK, 2.5)


def meter(f, x, y, letter, r=20):
    f.circle(x, y, r, WHITE, INK, 3)
    f.tex(x, y, r"\text{" + letter + "}", "middle", w=30)


def terminal(f, x, y):
    f.circle(x, y, 6, WHITE, INK, 2.5)


def head(f, x, y, d, s=10, col=CUR):
    """A filled current arrowhead at (x, y) pointing r, l, u or d."""
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", col)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- Ydinajatus: discharging and charging ---------------------------------------------------------------------
def panel(f, y0, charging):
    """One loop: the battery (akku) and a lamp (discharging) or a charger and the battery (charging)."""
    top, bot, xl, xr = y0 + 60, y0 + 172, 130, 430
    ym = (top + bot) / 2
    wire(f, (xl, ym - 8), (xl, top), (xr, top), (xr, ym - 8)); wire(f, (xl, ym + 8), (xl, bot), (xr, bot), (xr, ym + 8))
    f.tex(12, y0 + 22, r"\text{Lataaminen}" if charging else r"\text{Purkautuminen}", "start", w=220)
    gid = f"fy69-en-{'c' if charging else 'd'}"
    H.grad(f, gid, HEAT_LIGHT, HEAT, horizontal=True)
    if charging:
        f.rect(xl - 38, ym - 40, 76, 80, SAND_LIGHT, INK, 2.5, rx=8)        # the charger: a box round its source
        source(f, xl, ym); wire(f, (xl, ym - 40), (xl, ym - 8)); wire(f, (xl, ym + 8), (xl, ym + 40))
        f.tex(xl - 46, ym, r"\text{laturi}", "end", w=80)
        source(f, xr, ym)
        f.tex(xr + 34, ym, r"\text{akku}", "start", w=70)
        f.arrow(xr - 44, ym - 20, xr - 44, ym + 22, CUR, 3, 14)             # inside the battery: + to −
        f.block_arrow(196, ym - 2, 354, ym - 2, f"url(#{gid})", 18, 38, 28)
    else:
        source(f, xl, ym)
        f.tex(xl - 36, ym, r"\text{akku}", "end", w=70)
        lamp(f, xr, ym)
        f.tex(xr + 30, ym, r"\text{lamppu}", "start", w=100)
        f.arrow(xl + 44, ym + 20, xl + 44, ym - 22, CUR, 3, 14)             # inside the battery: − to +
        f.block_arrow(196, ym - 2, 354, ym - 2, f"url(#{gid})", 18, 38, 28)
    head(f, 280, top, "r"); head(f, 380, bot, "l")
    f.tex(280, top - 22, r"I", "middle", CUR, w=24)
    f.tex(260, ym + 34, r"\text{energia}", "middle", w=110)


def purku_lataus():
    f = new("fy69-purku", 384, "Kaksi kytkentäkaaviota päällekkäin, ei mittakaavassa. Ylempi: akku purkautuu. Akku on "
            "vasemmalla, plusnapa eli pitkä levy ylhäällä, ja lamppu oikealla. Violetti virta kulkee akun plusnavasta "
            "yläjohdinta pitkin lamppuun ja alajohdinta pitkin miinusnapaan; akun sisällä virta kulkee miinusnavalta "
            "plusnavalle. Oranssi energianuoli osoittaa akusta lamppuun. Alempi: akkua ladataan. Laturi on vasemmalla ja "
            "akku oikealla, molempien plusnapa ylhäällä. Virta kulkee laturin plusnavasta akun plusnapaan, joten akun "
            "sisällä virta kulkee nyt plusnavalta miinusnavalle eli päinvastaiseen suuntaan. Energianuoli osoittaa "
            "laturista akkuun.")
    panel(f, 0, False)
    f.line(12, 190, 588, 190, RULE, 1.5, "6 6")
    panel(f, 192, True)
    return f.svg()


# --- Ydinajatus: capacity as the area of the (t, I) graph ------------------------------------------------------
def capacity():
    f = new("fy69-kapasiteetti", 340, "Kuvaaja mittakaavassa: purkuvirta I ampeereina ajan t funktiona tunteina. Virta on "
            "vakio 0,50 A ajan 0–4,0 h ja sen jälkeen nolla, kun akku on tyhjä. Kuvaajan ja aika-akselin väliin jäävä "
            "suorakulmio on sävytetty; sen pinta-ala on varaus Q = It = 0,50 A · 4,0 h = 2,0 Ah.")
    ax = Axes(f, (92, 284), (480, 56), x=(0, 5), y=(0, 0.8), xticks=[1, 2, 3, 4, 5], yticks=[0.2, 0.4, 0.6, 0.8],
              xlabel=r"t\ (\text{h})", ylabel=r"I\ (\text{A})")
    ax.area([(0, 0), (0, 0.5), (4, 0.5), (4, 0)], GOOD_LIGHT, 0.75)
    ax.line([(0, 0.5), (4, 0.5), (4, 0), (4.9, 0)], CUR, 3)
    f.tex(ax.X(2), ax.Y(0.25) - 16, r"Q = It", "middle", w=120)
    f.tex(ax.X(2), ax.Y(0.25) + 18, r"= 2{,}0\,\text{Ah}", "middle", w=150)
    f.tex(ax.X(2), ax.Y(0.5) - 22, r"0{,}50\,\text{A}", "middle", CUR, w=100)
    return f.svg()


# --- Kaava: the charging circuit --------------------------------------------------------------------------------
TOP, BOT, XC, XR, XA, XB, XV = 82, 300, 86, 214, 316, 430, 532


def charging_circuit(f, values):
    ym = (TOP + BOT) / 2
    yt, yb = TOP + 26, BOT - 26                 # the battery's terminals
    wire(f, (XC, ym - 8), (XC, TOP), (XB, TOP), (XB, yt))
    wire(f, (XC, ym + 8), (XC, BOT), (XB, BOT), (XB, yb))
    wire(f, (XB, yt), (XB, 236 - 8)); wire(f, (XB, 236 + 8), (XB, yb))
    f.rect(XC - 38, ym - 46, 76, 92, SAND_LIGHT, INK, 2.5, rx=8)
    wire(f, (XC, ym - 46), (XC, ym - 8)); wire(f, (XC, ym + 8), (XC, ym + 46))
    source(f, XC, ym)
    f.tex(XC + 46, ym - 2, r"U_\text{lat}", "start", w=70)
    resistor(f, XR, TOP)
    f.tex(XR, TOP - 30, r"R", "middle", w=30)
    meter(f, XA, TOP, "A")
    # the battery: R_s and E inside a dashed box, the terminals on its edge
    f.rect(XB - 40, yt, 80, yb - yt, "none", MUTED, 2, rx=6, extra='stroke-dasharray="7 6"')
    resistor(f, XB, 156, vertical=True, length=50, width=20)
    source(f, XB, 236)
    f.tex(XB - 48, 156, r"R_\text{s}", "end", w=50)
    f.tex(XB - 48, 236, r"E", "end", w=30)
    terminal(f, XB, yt); terminal(f, XB, yb)
    f.tex(XB, BOT + 32, r"\text{akku}", "middle", w=80)
    # the voltmeter across the terminals
    wire(f, (XB, yt), (XV, yt), (XV, ym - 20), w=2.5); wire(f, (XV, ym + 20), (XV, yb), (XB, yb), w=2.5)
    f.circle(XB, yt, 4, INK); f.circle(XB, yb, 4, INK)
    meter(f, XV, ym, "V")
    f.tex(XV + 26, ym - 34, r"U", "start", w=28)
    # currents: out of the charger's +, into the battery's +
    head(f, 150, TOP, "r"); head(f, 380, TOP, "r"); head(f, 260, BOT, "l")
    head(f, XB, 196, "d")
    f.tex(150, TOP - 26, r"I", "middle", CUR, w=24)
    if values:
        f.tex(XR, TOP + 32, r"0{,}40\,\Omega", "middle", w=90)


def circuit():
    f = new("fy69-piiri", 360, "Latauspiirin kytkentäkaavio, ei mittakaavassa. Vasemmalla laturi, jonka jännite on U_lat ja "
            "plusnapa ylhäällä. Yläjohtimessa ovat laturin ja johtojen resistanssi R ja virtamittari A. Oikealla on akku "
            "katkoviivalla rajattuna: sen sisällä sisäinen resistanssi R_s ja lähdejännite E, jonka plusnapa on ylhäällä. "
            "Akun navat ovat katkoviivan reunalla, ja jännitemittari V on kytketty niiden väliin; se näyttää napajännitteen U. "
            "Violetit virtanuolet kulkevat laturin plusnavasta yläjohdinta pitkin akun plusnapaan, akun läpi alaspäin ja "
            "alajohdinta pitkin takaisin laturin miinusnapaan.")
    charging_circuit(f, False)
    return f.svg()


# --- Kaava: the potential round the charging loop ---------------------------------------------------------------
def potential():
    U, RI, RsI, E = 4.5, 0.88, 0.22, 3.40
    f = new("fy69-potentiaali", 372, "Potentiaalikuvaaja, pystyakseli mittakaavassa, vaaka-akseli kaavamainen: latauspiirin "
            "silmukka kierretään laturin miinusnavasta A laturin, vastuksen R ja akun kautta takaisin A:han, kun laturin "
            "jännite on 4,5 V, R = 0,40 ohmia, akun lähdejännite 3,40 V ja sisäinen resistanssi 0,10 ohmia, jolloin virta on "
            "2,2 A. Laturissa potentiaali nousee 4,5 volttia. Vastuksessa R se laskee 0,88 V ja on akun plusnavassa B 3,62 V, "
            "mikä on napajännite. Akun sisäisessä resistanssissa se laskee 0,22 V arvoon 3,40 V kohdassa C ja akun "
            "lähdejännitteen kohdalla 3,40 V nollaan. Virta kulkee akun läpi plusnavalta miinusnavalle, joten "
            "potentiaali laskee akussa.")
    path = [(0, 0), (1, 0), (1, U), (2.6, U), (3.6, U - RI), (5, U - RI), (6, E), (6.8, E), (6.8, 0), (8, 0)]
    ax = Axes(f, (96, 286), (500, 62), x=(0, 8), y=(0, 5.5), xticks=[], yticks=[1, 2, 3, 4, 5],
              xlabel=r"\text{kohta}", ylabel=r"V\ (\text{V})", origin_label=False)
    for x0, x1, t in [(0.7, 1.3, r"U_\text{lat}"), (2.6, 3.6, r"R"), (5, 6, r"R_\text{s}"), (6.5, 7.1, r"E")]:
        f.rect(ax.X(x0), ax.Y(5.5), ax.X(x1) - ax.X(x0), ax.Y(0) - ax.Y(5.5), GLASS)
        f.tex((ax.X(x0) + ax.X(x1)) / 2, ax.Y(5.5) + 16, t, "middle", w=60)
    for t in [1, 2, 3, 4, 5]:
        f.line(97, ax.Y(t), 500, ax.Y(t), RULE_LIGHT, 1.5)
    f.tex(84, 280, "0", "end")
    ax.line(path, POT, 3)
    for x, name in [(0, "A"), (4.3, "B"), (6.4, "C"), (8, "A")]:
        f.line(ax.X(x), 286, ax.X(x), 293, INK, 2)
        f.tex(ax.X(x), 314, name, "middle", w=28)
        v = {0: 0, 4.3: U - RI, 6.4: E, 8: 0}[x]
        ax.point(x, v, POT, 5.5)
    # the changes under the curve between gridlines, each under its own step; B's potential above its point
    f.tex(ax.X(1) + 10, ax.Y(1.5), r"+4{,}5\,\text{V}", "start", w=100)
    f.tex(ax.X(3.1), ax.Y(2.5), r"-0{,}88\,\text{V}", "middle", w=100)
    f.tex(ax.X(4.3), ax.Y(4.2), r"3{,}62\,\text{V}", "middle", POT, w=90)
    f.tex(ax.X(5.5), ax.Y(2.5), r"-0{,}22\,\text{V}", "middle", w=100)
    f.tex(ax.X(6.8) - 10, ax.Y(1.5), r"-3{,}40\,\text{V}", "end", w=100, bg=True)
    return f.svg()


# --- Kaava: where the charger's energy goes (one full charge, to scale) -----------------------------------------
def energy_flow():
    f = new("fy69-energia", 340, "Energiavirtakaavio mittakaavassa: nuolten leveys on verrannollinen energiaan. Laturi antaa "
            "täydessä latauksessa tyhjästä täyteen 9,0 Wh energiaa, kun laturin jännite on 4,5 V ja akun kapasiteetti 2,0 Ah. "
            "Siitä 7,6 Wh varastoituu akkuun kemialliseksi energiaksi ja jatkaa nuolena oikealle. Alaspäin erkanee kaksi "
            "kapeaa nuolta: 1,1 Wh muuttuu laturin ja johtojen sisäenergiaksi ja 0,3 Wh akun sisäenergiaksi, ja ne "
            "siirtyvät lämpönä ympäristöön.")
    k = 10.0                                    # px per Wh
    y_top, W, Wk, WR, Ws = 96, 9.0, 7.6, 1.12, 0.28
    yb = y_top + W * k                          # 186
    x1, x2 = 250, 370                           # where the two losses leave the band
    # the colours of fy2-4/lamp (teacher 2026-11-11, group C): grey the charger's electrical energy until the battery,
    # green the useful part stored in the battery, orange the two losses to internal energy; each gradient runs along
    # its own flow, and the widths stay to scale
    def lin(gid, c0, c1, xa, ya, xb, yb_):
        f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{n(xa)}" y1="{n(ya)}" x2="{n(xb)}" y2="{n(yb_)}">'
                   f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>')
        return f"url(#{gid})"
    yr, yk = y_top + (W - WR) * k, y_top + Wk * k                 # the band's bottom after the first loss; the useful part's bottom
    def poly(pts, fill): f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", fill, INK, 1.5)
    poly([(40, y_top), (x2, y_top), (x2, yr), (x1, yr), (x1, yb), (40, yb)], lin("fy69-flow-in", RULE_LIGHT, RULE, 40, 0, x2, 0))
    poly([(x2, y_top), (520, y_top), (520, y_top - 14), (566, y_top + Wk * k / 2), (520, yk + 14), (520, yk), (x2, yk)],
         lin("fy69-flow-ok", GOOD_LIGHT, GOOD, x2, 0, 566, 0))
    poly([(x1, yr), (x1 + WR * k, yr), (x1 + WR * k, 266), (x1 + WR * k + 9, 266), (x1 + WR * k / 2, 292), (x1 - 9, 266), (x1, 266)],
         lin("fy69-flow-h1", HEAT_LIGHT, HEAT, 0, yr, 0, 292))
    poly([(x2, yk), (x2 + Ws * k, yk), (x2 + Ws * k, 266), (x2 + Ws * k + 8, 266), (x2 + Ws * k / 2, 290), (x2 - 8, 266), (x2, 266)],
         lin("fy69-flow-h2", HEAT_LIGHT, HEAT, 0, yk, 0, 290))
    f.tex(40, y_top - 26, r"W_\text{lat} = 9{,}0\,\text{Wh}", "start", w=200)
    f.tex(40, y_top - 58, r"\text{laturista}", "start", w=120)
    f.tex(566, y_top - 58, r"\text{akkuun kemiallisena}", "end", GOOD, w=260)
    f.tex(566, y_top - 26, r"7{,}6\,\text{Wh}", "end", GOOD, w=100)
    f.tex(x1 + WR * k / 2 - 22, 314, r"1{,}1\,\text{Wh}", "end", w=100)
    f.tex(x1 + WR * k / 2 - 22, 282, r"\text{laturi ja johdot}", "end", w=200)
    f.tex(x2 + Ws * k / 2 + 22, 314, r"0{,}3\,\text{Wh}", "start", w=100)
    f.tex(x2 + Ws * k / 2 + 22, 282, r"\text{akku}", "start", w=70)
    f.tex(40, 222, r"\text{sisäenergiaksi:}", "start", w=180)
    return f.svg()


# --- a task figure: a charging current in two constant steps -----------------------------------------------------
def ex_current():
    f = new("fy69-excurrent", 330, "Kuvaaja mittakaavassa: akun latausvirta I ampeereina ajan t funktiona tunteina, ruudukon "
            "välit 0,5 h ja 0,5 A. Virta on 2,0 A ajan 0–1,5 h, sitten 1,0 A ajan 1,5–2,5 h ja sen jälkeen nolla.")
    ax = Axes(f, (92, 280), (480, 56), x=(0, 3), y=(0, 2.5), xticks=[0.5, 1, 1.5, 2, 2.5, 3], yticks=[0.5, 1, 1.5, 2, 2.5],
              xlabel=r"t\ (\text{h})", ylabel=r"I\ (\text{A})")
    ax.line([(0, 2.0), (1.5, 2.0), (1.5, 1.0), (2.5, 1.0), (2.5, 0), (2.95, 0)], CUR, 3)
    return f.svg()


# --- opening illustration: a phone charging on a table ----------------------------------------------------------
def hero():
    f = H.hero("fy69-hero", "Kuvitus: älypuhelin latautuu puisella pöydällä illalla. Puhelimesta kulkee johto seinän "
               "pistorasiassa olevaan valkoiseen laturiin. Puhelimen näytössä on akun kuva, joka on lähes täynnä vihreää, "
               "ja sen vieressä salaman merkki. Pöydällä on myös kahvikuppi, ja seinällä lamppu valaisee.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 380, H.grad(f, "fy69h-wall", GLASS, PAPER))
    # wall lamp glow
    f.defs_add(f'<radialGradient id="fy69h-glow"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.8"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.circle(200, 120, 170, "url(#fy69h-glow)")
    f.path("M160,70 L240,70 L262,140 L138,140 Z", HEAT_LIGHT, INK, 3)
    f.rect(192, 40, 16, 30, IRON, INK, 2.5)
    # the socket with the charger
    f.rect(820, 160, 150, 150, WHITE, INK, 3, rx=14)
    f.rect(838, 178, 114, 114, GLASS, RULE, 2, rx=10)
    f.rect(850, 196, 90, 92, WHITE, INK, 3, rx=12)                       # the charger plugged in
    f.rect(864, 212, 62, 8, RULE_LIGHT, None, 0, rx=4)
    f.rect(884, 286, 22, 24, METAL_EDGE, INK, 2.5, rx=4)                   # the cable's plug
    # the table
    f.rect(0, 380, 1200, 220, H.grad(f, "fy69h-table", SAND_LIGHT, SAND))
    f.rect(0, 372, 1200, 16, SAND_DARK)
    for k in range(6):
        y = 410 + 32 * k
        f.path(f"M0,{y} C300,{y - 6} 700,{y + 8} 1200,{y - 2}", stroke=GRAIN, w=2, extra='stroke-opacity="0.35"')
    # the cable from the charger down the wall to the phone
    f.path("M895,310 C895,380 900,430 820,452 C740,474 700,470 690,470", stroke=INK, w=7, extra='stroke-linecap="round"')
    f.path("M895,310 C895,380 900,430 820,452 C740,474 700,470 690,470", stroke=ALUMINIUM, w=3, extra='stroke-linecap="round"')
    # the phone lying on the table, seen from above at an angle
    f.path("M430,410 L690,428 Q712,430 710,452 L700,520 Q698,540 676,538 L414,520 Q394,518 396,496 L406,430 Q410,408 430,410 Z",
           IRON, INK, 3)
    f.path("M436,424 L682,441 Q694,442 693,454 L685,512 Q684,524 672,523 L424,506 Q412,505 413,493 L421,437 Q423,423 436,424 Z",
           INK)
    # battery icon on the screen: body, nub, a green fill nearly full, a lightning bolt beside it
    f.path("M478,452 L598,460 L594,500 L474,492 Z", "none", WHITE, 4)
    f.path("M600,470 L610,471 L608,489 L598,488 Z", WHITE)
    f.path("M484,458 L572,464 L569,494 L480,488 Z", GOOD_LIGHT)
    f.path("M484,458 L572,464 L569,494 L480,488 Z", "none", GOOD, 2)
    f.path("M636,452 L620,480 L634,481 L626,506 L652,472 L638,471 L648,453 Z", HEAT_LIGHT, HEAT, 2)
    # a coffee cup
    f.path("M210,380 L300,380 L292,470 Q290,486 274,486 L236,486 Q220,486 218,470 Z", COLD_LIGHT, INK, 3)
    f.path("M298,400 Q336,404 330,432 Q324,454 294,452", stroke=INK, w=6)
    f.path("M216,380 Q255,368 296,380", stroke=INK, w=3)
    for x0 in (236, 262):
        f.path(f"M{x0},362 C{x0 - 12},346 {x0 + 12},334 {x0},318 C{x0 - 12},302 {x0 + 8},292 {x0 + 2},280", stroke=MUTED, w=3,
               extra='stroke-linecap="round" stroke-opacity="0.55"')
    return f.svg()


FIGURES = {"hero": hero, "purku-lataus": purku_lataus, "kapasiteetti": capacity, "latauspiiri": circuit,
           "potentiaali": potential, "energia": energy_flow, "ex-current": ex_current}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "purku-lataus": "reveals: the current runs through the battery from + to - while charging, from - to + while discharging",
    "kapasiteetti": "reveals: the capacity Q = It = 2,0 Ah as the area under a constant 0,50 A for 4,0 h",
    "latauspiiri": "safe: the charging circuit with U_lat, R, ammeter, battery (E, R_s) and voltmeter, symbols only",
    "potentiaali": "reveals: the potential round a charging loop, 4,5 V charger, drops 0,88 V, 0,22 V and 3,40 V",
    "energia": "reveals: one full charge, 9,0 Wh from the charger, 7,6 Wh stored, 1,1 Wh and 0,3 Wh to internal energy",
    "ex-current": "safe: a charging current of 2,0 A for 1,5 h and 1,0 A for 1,0 h, the charge not written",
}
