"""Figures of FY7 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY7` writes them into
solutions.md. Three are task figures that carry no answer (the ion implanter, the dynamo's voltage, the steel's spectrum);
the rest are model answers. Colours (FY7 brief): force #c92a2a, velocity #1971c2, magnetic field #2b8a3e (× into the
page), electric field #8a5f22, an ion beam #7048e8; a positive ion #f2a69c with its sign drawn."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, HOT, HOT_LIGHT, COLD, GOOD, HEAT_LIGHT, n

FORCE, VEL, FIELD, EFIELD, BEAM = HOT, COLD, GOOD, "#8a5f22", "#7048e8"

# fy7-s5 data (answers.py): NIST wavelengths in air (nm), the order k and the measured angle (°)
LINES = [(656.28, 1, 23.2), (486.13, 1, 17.0), (434.05, 1, 15.1), (410.17, 1, 14.2), (656.28, 2, 52.0), (486.13, 2, 35.7)]


def in_mark(f, x, y, a=6):
    """Magnetic field into the page: a cross."""
    f.line(x - a, y - a, x + a, y + a, FIELD, 2.2)
    f.line(x - a, y + a, x + a, y - a, FIELD, 2.2)


def ion(f, x, y, r=11):
    """A positive ion with its sign."""
    f.circle(x, y, r, HOT_LIGHT, INK, 2)
    f.line(x - r * 0.5, y, x + r * 0.5, y, INK, 2.2); f.line(x, y - r * 0.5, x, y + r * 0.5, INK, 2.2)


def implanter():
    """fy7-s1 task figure: source, accelerating gap, velocity selector (field into the page, plates without polarity),
    analyser magnet (field into the page) bending the beam up through a half circle to the slit and the wafer."""
    f = Fig("fy7-s1-implanter", 380, "Periaatekuva, ei mittakaavassa: ioni-istutin. Alhaalla vasemmalla ionilähde, josta ionit "
            "kiihdytetään jännitteellä U kahden verkkoelektrodin välissä. Sen jälkeen ionit kulkevat vaakasuoraan oikealle "
            "nopeusvalitsimen kahden vaakasuoran levyn välistä, joiden etäisyys on d. Levyjen napaisuutta ei ole merkitty. "
            "Valitsimessa on magneettikenttä B s paperiin sisään. Oikealla analysointimagneetin kammiossa on magneettikenttä B "
            "paperiin sisään. Siinä ionisuihku kaartuu puoliympyrän, jonka säde on r, ylös ja takaisin vasemmalle, ja kulkee "
            "kammion vasemman seinän raosta piikiekkoon, joka on valitsimen yläpuolella.")
    yb = 300                                            # the beam line
    f.rect(14, yb - 20, 48, 40, ALUMINIUM, INK, 2, 5)
    f.tex(38, yb + 44, r"\text{lähde}", "middle", w=80)
    for x in (76, 98):                                  # accelerating grids
        f.line(x, yb - 30, x, yb + 30, INK, 2.5, "4 3")
    f.tex(87, yb - 46, "U", "middle")
    # velocity selector
    x1, x2 = 124, 300
    f.rect(x1, yb - 44, x2 - x1, 10, METAL_EDGE, INK, 1.5, 2)
    f.rect(x1, yb + 34, x2 - x1, 10, METAL_EDGE, INK, 1.5, 2)
    for x in (150, 212, 274):
        in_mark(f, x, yb - 17); in_mark(f, x, yb + 17)
    f.tex((x1 + x2) / 2, yb + 66, r"\text{nopeusvalitsin}", "middle", w=190)
    f.tex(x1 - 4, yb - 64, r"\overline{B}_\text{s}", "start", FIELD)
    f.line(x2 + 10, yb - 34, x2 + 10, yb + 34, MUTED, 1.5)
    for y in (yb - 34, yb + 34): f.line(x2 + 4, y, x2 + 16, y, MUTED, 1.5)
    f.tex(x2 + 18, yb + 26, "d", "start", MUTED)                 # below the beam line, clear of it
    # analyser magnet
    wall, r = 340, 100
    f.rect(wall, 60, 250, 290, GLASS, None)
    f.rect(wall, 60, 250, 290, "none", INK, 2.5, 6)
    for i in range(3):
        for j in range(4):
            x, y = wall + 40 + 80 * i, 92 + 72 * j
            if abs(math.hypot(x - wall, y - (yb - r)) - r) < 22 or (x < wall + 110 and abs(y - (yb - r)) < 16): continue
            in_mark(f, x, y)
    f.tex(582, 330, r"\overline{B}", "end", FIELD)
    f.line(62, yb, wall, yb, BEAM, 3)
    f.path(f"M{wall},{yb} A{r},{r} 0 0 0 {wall},{yb - 2 * r}", stroke=BEAM, w=3)
    f.line(wall, yb - 2 * r, 236, yb - 2 * r, BEAM, 3)
    f.line(wall, yb - r, wall + r * math.cos(math.radians(-30)), yb - r + r * math.sin(math.radians(-30)), MUTED, 1.5, "5 4")
    f.circle(wall, yb - r, 3, MUTED)
    f.tex(wall + 58, yb - r + 6, "r", "middle")
    # slit in the left wall and the wafer
    f.rect(wall - 3, yb - 2 * r - 30, 6, 22, INK); f.rect(wall - 3, yb - 2 * r + 8, 6, 22, INK)
    f.rect(214, yb - 2 * r - 46, 14, 92, ALUMINIUM, METAL_EDGE, 2, 2)
    f.tex(206, yb - 2 * r - 66, r"\text{piikiekko}", "end", w=120)
    f.tex(wall + 8, 36, r"\text{analysointimagneetti}", "start", w=230)
    return f.svg()


def selector_forces():
    """fy7-s1 a: the model answer. Field into the page, the upper plate positive, E down; on an ion moving straight to
    the right the magnetic force points up and the electric force down, equally long."""
    f = Fig("fy7-s1-forces", 330, "Kaavakuva nopeusvalitsimesta: ylempi levy on positiivinen ja alempi negatiivinen, joten "
            "sähkökenttä E osoittaa levyjen välissä alaspäin. Magneettikenttä osoittaa paperiin sisään, mitä kuvaavat vihreät "
            "ristit. Levyjen välissä on positiivinen ioni, jonka nopeus v osoittaa oikealle. Ioniin vaikuttaa magneettinen voima "
            "F m ylöspäin ja sähköinen voima F s alaspäin. Voimanuolet ovat yhtä pitkät, koska suoraan kulkevaan ioniin "
            "vaikuttavat voimat kumoavat toisensa.")
    yt, yb = 50, 280
    f.rect(60, yt - 12, 480, 12, METAL_EDGE, INK, 1.5, 2); f.rect(60, yb, 480, 12, METAL_EDGE, INK, 1.5, 2)
    f.tex(40, yt - 6, "+", "middle"); f.tex(40, yb + 6, "-", "middle")
    for x in (110, 490):
        f.arrow(x, yt + 14, x, yb - 14, EFIELD, 2.5, 13)
    f.tex(122, 230, r"\overline{E}", "start", EFIELD)
    for x in (190, 410):
        for y in (90, 240): in_mark(f, x, y)
    f.tex(470, 100, r"\overline{B}_\text{s}", "end", FIELD)
    cx, cy = 300, 165
    f.arrow(cx, cy, cx, cy - 92, FORCE, 4, 16); f.tex(cx + 14, cy - 82, r"\overline{F}_\text{m}", "start", FORCE)
    f.arrow(cx, cy, cx, cy + 92, FORCE, 4, 16); f.tex(cx + 14, cy + 82, r"\overline{F}_\text{s}", "start", FORCE)
    f.arrow(cx + 14, cy, cx + 120, cy, VEL, 3.5, 15); f.tex(cx + 128, cy, r"\overline{v}", "start", VEL)
    ion(f, cx, cy)
    return f.svg()


def dynamo_signal():
    """fy7-s2 task figure: the open-circuit voltage of the hub dynamo, peak 14 V, period 30 ms, 0–90 ms."""
    f = Fig("fy7-s2-signal", 380, "Kuvaaja: napadynamon jännite u ajan t funktiona aikavälillä 0–90 ms, kun valo on pois päältä. "
            "Jännite vaihtelee sinimuotoisesti. Se alkaa nollasta ja nousee huippuarvoon 14 V kohdassa 7,5 ms, laskee arvoon "
            "miinus 14 V kohdassa 22,5 ms ja palaa nollaan kohdassa 30 ms. Sama vaihtelu toistuu kolme kertaa. Ruudukon "
            "pystysuorat viivat ovat 5 ms:n ja vaakasuorat 2 V:n välein.")
    ax = Axes(f, (70, 334), (470, 64), x=(0, 90), y=(-16, 16), xticks=list(range(0, 91, 5)), yticks=list(range(-16, 17, 2)),
              xlabel=r"t\ (\text{ms})", ylabel=r"u\ (\text{V})", xfmt=lambda v: str(v) if v % 10 == 0 else "",
              yfmt=lambda v: (str(v) if v >= 0 else "-" + str(-v)) if v % 4 == 0 else "", origin_label=False)
    f.tex(ax.X(0), 358, "0", "middle")
    f.line(ax.X(0), ax.Y(0), ax.X(90), ax.Y(0), MUTED, 1.5, "6 5")
    ax.curve(lambda t: 14 * math.sin(2 * math.pi * t / 30), 0, 90, INK, 3, steps=360)
    return f.svg()


def planck(lam_um, T):
    """Planck's spectral radiance (relative), wavelength in µm."""
    c2 = 14387.77                                       # hc/k in µm·K
    return lam_um ** -5 / (math.exp(c2 / (lam_um * T)) - 1)


def steel_spectrum():
    """fy7-s4 task figure: the black-body spectrum of the slab (T = 2,898·10⁻³ m·K : 2,00 µm), normalised to its peak,
    with the visible band shaded. The peak sits on the 2,0 µm gridline."""
    T = 2898.0 / 2.00
    peak = planck(14387.77 / (4.965114 * T), T)
    f = Fig("fy7-s4-spectrum", 380, "Kuvaaja: kuuman teräsaihion lähettämän säteilyn suhteellinen intensiteetti aallonpituuden "
            "lambda funktiona välillä 0–6 mikrometriä. Käyrä nousee jyrkästi noin 0,7 mikrometrin kohdalta, saavuttaa huippunsa "
            "ja laskee sen jälkeen loivasti. Huippu on ruudukon pystysuoralla viivalla 2,0 mikrometrin kohdalla. Näkyvän valon alue "
            "0,38–0,75 mikrometriä on varjostettu; siinä käyrä on lähes nollassa. Ruudukon pystysuorat viivat ovat 0,5 "
            "mikrometrin välein.")
    ax = Axes(f, (80, 330), (480, 50), x=(0, 6), y=(0, 1.1), xticks=[i / 2 for i in range(13)], yticks=[0.2, 0.4, 0.6, 0.8, 1.0],
              xlabel=r"\lambda\ (\mu\text{m})", ylabel=r"\text{suhteellinen intensiteetti}", xfmt=lambda v: str(int(v)) if v == int(v) else "",
              yfmt=lambda v: f"{v:.1f}".replace(".", "{,}"))
    ax.area([(0.38, 0), (0.38, 1.1), (0.75, 1.1), (0.75, 0)], "#be4bdb", 0.18)
    f.tex(ax.X(0.565), ax.Y(1.04), r"\text{näkyvä}", "start", MUTED, size=20)
    ax.curve(lambda l: planck(l, T) / peak if l > 0.2 else 0, 0.25, 6, INK, 3, steps=400)
    return f.svg()


def fibre_angles():
    """fy7-s4 c: the light ray entering the fibre's end face from air at θ, refracting to β and meeting the core–cladding
    boundary at the critical angle α_r = 90° − β. Angles exaggerated."""
    f = Fig("fy7-s4-fibre", 300, "Kaavakuva, kulmat liioiteltuja: valokuidun pää sivulta. Keskellä ydin, jonka taitekerroin on n 1, "
            "ylä- ja alapuolella kuori, jonka taitekerroin on n 2. Vasemmalla ilmaa. Säde tulee ilmasta kuidun päätypintaan "
            "kulmassa theeta päätypinnan normaaliin nähden ja taittuu ytimessä kulmaan beeta. Säde osuu ytimen ja kuoren "
            "rajapintaan kulmassa alfa r rajapinnan normaaliin nähden ja heijastuu kokonaan takaisin ytimeen. Kulmat beeta ja "
            "alfa r ovat yhdessä 90 astetta.")
    x0, yt, yb = 200, 90, 230
    f.rect(x0, 40, 380, 50, "#e7f5ff", METAL_EDGE, 1.5); f.rect(x0, yb, 380, 50, "#e7f5ff", METAL_EDGE, 1.5)
    f.rect(x0, yt, 380, yb - yt, "#d0ebff", INK, 2)
    f.tex(560, 65, r"\text{kuori } n_2", "end", MUTED); f.tex(560, 255, r"\text{kuori } n_2", "end", MUTED)
    f.tex(560, 200, r"\text{ydin } n_1", "end", MUTED)
    f.tex(60, 110, r"\text{ilma}", "start", MUTED)                  # above the incoming ray
    yc = 180
    f.line(80, yc, 330, yc, MUTED, 1.5, "6 5")                         # normal of the end face
    th, be = math.radians(34), math.radians(22)
    sx = x0 - 130; sy = yc + 130 * math.tan(th)
    f.line(sx, sy, x0, yc, INK, 3)
    hx = x0 + (yc - yt) / math.tan(be)
    f.line(x0, yc, hx, yt, INK, 3)
    f.arrow(hx, yt, hx + 70 * math.cos(be), yt + 70 * math.sin(be), INK, 3, 13)
    f.line(hx, yt - 30, hx, yt + 90, MUTED, 1.5, "6 5")                # normal of the core–cladding boundary
    f.path(f"M{n(x0 - 60)},{yc} A60,60 0 0 1 {n(x0 - 60 * math.cos(th))},{n(yc + 60 * math.sin(th))}", stroke=INK, w=1.5)
    f.tex(x0 - 72, yc + 22, r"\theta", "end")
    f.path(f"M{n(x0 + 60)},{yc} A60,60 0 0 0 {n(x0 + 60 * math.cos(be))},{n(yc - 60 * math.sin(be))}", stroke=INK, w=1.5)
    f.tex(x0 + 70, yc - 14, r"\beta", "start")
    f.path(f"M{n(hx)},{yt + 46} A46,46 0 0 1 {n(hx - 46 * math.sin(math.pi / 2 - be))},{n(yt + 46 * math.cos(math.pi / 2 - be))}", stroke=INK, w=1.5)
    f.tex(hx - 24, yt + 64, r"\alpha_\text{r}", "end")
    return f.svg()


def grating_graph():
    """fy7-s5 a: sin θ against kλ for the six hydrogen lines, a line through the origin and the point its slope is read from."""
    xs = [k * l for l, k, _ in LINES]; ys = [math.sin(math.radians(t)) for _, _, t in LINES]
    slope = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    f = Fig("fy7-s5-graph", 420, "Kuvaaja: maksimin suunnan sini sin theeta kertaluvun ja aallonpituuden tulon k lambda funktiona. "
            "Kuusi mustaa pistettä: (410; 0,245), (434; 0,261), (486; 0,292), (656; 0,394), (972; 0,584) ja (1313; 0,788), "
            "vaaka-akselilla nanometreinä. Pisteisiin on sovitettu origon kautta kulkeva suora, jolta on merkitty piste "
            "(1300 nm; 0,780). Suoran kulmakerroin on 6,00 kertaa 10 potenssiin miinus 4 per nanometri.")
    ax = Axes(f, (90, 370), (470, 50), x=(0, 1400), y=(0, 0.9), xticks=list(range(0, 1401, 100)), yticks=[i / 10 for i in range(10)],
              xlabel=r"k\lambda\ (\text{nm})", ylabel=r"\sin\theta", xfmt=lambda v: str(v) if v % 400 == 0 else "",
              yfmt=lambda v: f"{v:.1f}".replace(".", "{,}") if round(v * 10) % 2 == 0 else "")
    ax.line([(0, 0), (1400, 1400 * slope)], INK, 2.5)
    for x, y in zip(xs, ys): ax.point(x, y)
    ax.guide(1300, 0.780)
    f.circle(ax.X(1300), ax.Y(0.780), 11, "none", INK, 1.5)
    f.tex(ax.X(1300) - 16, ax.Y(0.780) - 26, r"(1300;\ 0{,}780)", "end", INK, bg=True)
    return f.svg()


FIGURES = {"fy7-s1-implanter": implanter, "fy7-s1-forces": selector_forces, "fy7-s2-signal": dynamo_signal,
           "fy7-s4-spectrum": steel_spectrum, "fy7-s4-fibre": fibre_angles, "fy7-s5-graph": grating_graph}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy7-s1-implanter": "safe: the implanter's layout with symbols only; the plates' polarity is not shown (task fy7-s1)",
    "fy7-s1-forces": "reveals: the forces and the plate polarity of task fy7-s1 a (its solution)",
    "fy7-s2-signal": "safe: the dynamo voltage the student reads the period and peak from (task fy7-s2)",
    "fy7-s4-spectrum": "safe: the steel's spectrum the student reads the peak from (task fy7-s4)",
    "fy7-s4-fibre": "reveals: the angle geometry of task fy7-s4 c (its solution)",
    "fy7-s5-graph": "reveals: the model graph and slope of task fy7-s5 (its solution)",
}
