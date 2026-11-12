"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-6` writes them into lesson.md.
Light is drawn in its real colour (spectral(), the FY8 convention of the chapter Valosähköinen ilmiö ja fotoni), photons
as wavy arrows labelled hf, electrons as small blue dots e⁻. The LED data are the simulation's model values
(lesson-answers.py): U_k a little below hc/(eλ), as in real LEDs."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, COLD, COLD_LIGHT, ALUMINIUM,
                    METAL_EDGE, IRON, HOT, HEAT, SAND_LIGHT)
import herolib as H

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
S, R = 0.035, 18.0                                           # the simulation's LED model: onset width (V), resistance (Ω)
LEDS = [("punainen", 630, 1.88), ("oranssi", 605, 1.95), ("keltainen", 590, 2.00), ("vihreä", 525, 2.30),
        ("sininen", 470, 2.52), ("violetti", 405, 2.95)]
I_mA = lambda U, Uk: S / R * math.log1p(math.exp((U - Uk) / S)) * 1000
f14 = lambda lam: c / (lam * 1e-9) / 1e14                    # frequency in units of 10^14 Hz


def spectral(lam):
    """The colour of light of wavelength lam (nm) as hex, as in the chapter Valosähköinen ilmiö ja fotoni."""
    if lam < 380: return "#7048e8"
    if lam < 440: r, g, b = (440 - lam) / 60, 0.0, 1.0
    elif lam < 490: r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510: r, g, b = 0.0, 1.0, (510 - lam) / 20
    elif lam < 580: r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645: r, g, b = 1.0, (645 - lam) / 65, 0.0
    else: r, g, b = 1.0, 0.0, 0.0
    k = 0.3 + 0.7 * (lam - 380) / 40 if lam < 420 else 1.0
    to = lambda v: round(255 * (v * k) ** 0.8) if v > 0 else 0
    return "#{:02x}{:02x}{:02x}".format(int(to(r) * 0.86), int(to(g) * 0.78), int(to(b) * 0.86))


def photon(f, x1, y1, x2, y2, colour, period=14.0, amp=6.0, w=3, head=15):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2) with a filled head."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    body = L - head
    pts = []
    for i in range(int(body / 1.5) + 1):
        s = i * 1.5; a = amp * math.sin(2 * math.pi * s / period) * min(1, s / 8, (body - s) / 8)
        pts.append((x1 + ux * s + px * a, y1 + uy * s + py * a))
    f.add(f'<polyline points="{" ".join(f"{n(a)},{n(b)}" for a, b in pts)}" fill="none" stroke="{colour}" stroke-width="{w}" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", colour)


def vyot():
    """Ydinajatus: the bands of an LED's semiconductor; at the junction an electron falls into a hole and one photon
    of energy hf ≈ E_g leaves."""
    f = Fig("fy86-vyot", 330, "Kaavakuva, ei mittakaavassa: LEDin puolijohteen energiavyöt. Pystysuunnassa on energia. Ylhäällä on "
            "johtavuusvyö ja alhaalla valenssivyö, ja niiden välissä on energia-aukko E g, jonka energioilla elektronilla ei voi "
            "olla tilaa. Pystysuora katkoviiva on rajapinta: vasemmalla on n-alue, jonka johtavuusvyössä on sinisiä elektroneja "
            "e miinus, oikealla p-alue, jonka valenssivyössä on tyhjiä paikkoja eli aukkoja valkoisina ympyröinä. Rajapinnalla "
            "elektroni putoaa johtavuusvyöstä valenssivyön aukkoon, ja siitä lähtee oikealle punainen aaltoviivanuoli, fotoni, "
            "jonka energia hf on likimain energia-aukon suuruinen.")
    x0, x1, xj = 200, 540, 370
    f.arrow(26, 300, 26, 34, INK, 2.5, 13)
    f.tex(40, 34, "E", "start")
    f.rect(x0, 54, x1 - x0, 56, GLASS, INK, 2.5, 4)
    f.rect(x0, 226, x1 - x0, 56, RULE_LIGHT, INK, 2.5, 4)
    f.tex(188, 82, r"\text{johtavuusvyö}", "end")
    f.tex(188, 254, r"\text{valenssivyö}", "end")
    f.line(xj, 40, xj, 296, MUTED, 1.5, "6 5")
    f.tex(285, 24, r"\text{n-alue}", "middle")
    f.tex(455, 24, r"\text{p-alue}", "middle")
    # E_g as a bracket in the gap on the left
    f.line(222, 110, 222, 226, INK, 2); f.line(214, 110, 230, 110, INK, 2); f.line(214, 226, 230, 226, INK, 2)
    f.tex(236, 168, r"E_\text{g}", "start")
    for x in (282, 314, 346):                                   # electrons at the bottom of the conduction band (n side)
        f.circle(x, 96, 8, COLD, WHITE, 1.5)
    for x in (430, 466, 502):                                   # holes at the top of the valence band (p side)
        f.circle(x, 240, 8, WHITE, INK, 2)
    f.tex(314, 134, "e^-", "middle", COLD)
    f.tex(466, 204, r"\text{aukko}", "middle")
    # the transition at the junction and the photon it gives
    f.circle(xj, 96, 8, COLD, WHITE, 1.5)
    f.line(xj, 106, xj, 216, COLD, 2.5, "7 5")
    f.path(f"M{xj},{230} L{xj - 7},{214} L{xj + 7},{214} Z", COLD)
    f.circle(xj, 240, 8, WHITE, INK, 2)
    red = spectral(630)
    photon(f, xj + 14, 168, 540, 168, red, period=630 / 45, amp=6)
    f.tex(470, 140, "hf", "middle", red)
    return f.svg()


def spektrit():
    """Ydinajatus: the spectra of an incandescent lamp, a red LED and a red laser diode, each scaled to its own
    maximum; the LED's band is about 20 nm wide, the laser diode's line about 1 nm."""
    f = Fig("fy86-spektrit", 360, "Kuvaaja: kolmen valonlähteen spektri samalla aallonpituusakselilla 380–720 nanometriä, pystyakselilla "
            "suhteellinen intensiteetti. Hehkulampun spektri on jatkuva: oranssi käyrä nousee tasaisesti violetista punaiseen. "
            "Punaisen LEDin spektri on kapea huippu aallonpituudella 630 nanometriä, ja sen leveys on noin 20 nanometriä. "
            "Punaisen laserdiodin spektri on hyvin kapea viiva aallonpituudella 650 nanometriä, leveys noin 1 nanometri (kuva on suuntaa-antava, ei mittakaavassa). "
            "LEDin ja laserdiodin huiput on skaalattu samaan korkeuteen, hehkulampun käyrä matalammaksi.")
    ax = Axes(f, (84, 306), (470, 70), x=(380, 720), y=(0, 1.1), xticks=[400, 450, 500, 550, 600, 650, 700], yticks=[0.5, 1.0],
              xlabel=r"\lambda\ (\text{nm})", ylabel=r"\text{suhteellinen intensiteetti}", xfmt=lambda v: fi(v),
              yfmt=lambda v: fi(v, 1))
    planck = lambda lam: (lam * 1e-9) ** -5 / (math.exp(h * c / (lam * 1e-9 * 1.381e-23 * 2800)) - 1)
    pmax = planck(720)
    ax.curve(lambda lam: 0.62 * planck(lam) / pmax, 390, 720, HEAT, 3)
    sl = 20 / 2.3548
    ax.curve(lambda lam: math.exp(-0.5 * ((lam - 630) / sl) ** 2), 585, 675, spectral(630), 3, steps=180)
    sd = 2 / 2.3548
    ax.curve(lambda lam: math.exp(-0.5 * ((lam - 650) / sd) ** 2), 644, 656, spectral(650), 3, steps=120)
    f.tex(ax.X(470), ax.Y(0.48), r"\text{hehkulamppu}", "middle", HEAT)
    f.tex(ax.X(612), ax.Y(0.88), r"\text{LED}", "end", spectral(630))
    f.tex(ax.X(658), ax.Y(1.0), r"\text{laserdiodi}", "start", spectral(650))
    return f.svg()


def iu():
    """Kaava: the I–U curves of the red, green and blue LED (model values); the straight part extended to I = 0
    gives the threshold voltage U_k."""
    f = Fig("fy86-iu", 380, "Kuvaaja mittakaavassa: kolmen LEDin virta milliampeereina jännitteen funktiona, jänniteakseli 0–3,5 volttia. "
            "Punaisen LEDin virta on lähes nolla noin 1,8 volttiin asti ja kasvaa sitten suoraviivaisesti. Vihreän LEDin käyrä on "
            "samanmuotoinen mutta oikealla, sinisen vielä oikeammalla. Kunkin käyrän suora osa on jatkettu katkoviivalla "
            "jänniteakselille, ja leikkauskohta on LEDin kynnysjännite U k: punaisella 1,88, vihreällä 2,30 ja sinisellä 2,52 volttia.")
    ax = Axes(f, (90, 322), (500, 64), x=(0, 3.5), y=(0, 30), xticks=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5], yticks=[5, 10, 15, 20, 25, 30],
              xlabel=r"U\ (\text{V})", ylabel=r"I\ (\text{mA})", xfmt=lambda v: fi(v, 1))
    for (name, lam, Uk), Imax in zip((LEDS[0], LEDS[3], LEDS[4]), (30, 25, 20)):
        col = spectral(lam)
        Uend = Uk + Imax / 1000 * R
        ax.line([(Uk, 0), (Uk + 0.24, 0.24 / R * 1000)], col, 2, "6 5")
        ax.curve(lambda U: I_mA(U, Uk), 0, Uend, col, 3, steps=200)
        ax.point(Uk, 0, col, 6)
        f.tex(ax.X(Uend) + 10, ax.Y(Imax), r"\text{" + name + "}", "start", col)
    f.tex(ax.X(1.80), ax.Y(4.2), r"U_\text{k}", "end", spectral(630))
    return f.svg()


def sovitus(fit=True):
    """Kaava: the threshold voltages of six LEDs against the frequency of their light, with the least-squares line;
    its slope is h/e. fit=False: the points only."""
    pts = [(f14(lam), Uk, spectral(lam)) for _, lam, Uk in LEDS]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    mx, my = sum(xs) / 6, sum(ys) / 6
    k = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); b = my - k * mx
    label = ("Kuvaaja mittakaavassa: kuuden LEDin kynnysjännite U k voltteina niiden valon taajuuden f funktiona, taajuusakseli "
             "nollasta 8 kertaa 10 potenssiin 14 hertsiin. Pisteet ovat LEDien värisiä: punainen 4,76 ja 1,88; oranssi 4,96 ja 1,95; "
             "keltainen 5,08 ja 2,00; vihreä 5,71 ja 2,30; sininen 6,38 ja 2,52; violetti 7,40 ja 2,95, taajuudet kertaa 10 "
             "potenssiin 14 hertsiä ja jännitteet voltteina.")
    if fit:
        label += (" Pisteisiin on sovitettu suora, joka jatkuu katkoviivana lähelle origoa ja leikkaa pystyakselin hieman nollan "
                  "alapuolella. Suoralle on piirretty kulmakerrointa kuvaava kolmio, ja merkintä kertoo, että kulmakerroin k on h jaettuna e:llä.")
    f = Fig("fy86-sovitus" if fit else "fy86-sovitus-p", 380, label)
    ax = Axes(f, (90, 322), (420, 64), x=(0, 8), y=(0, 3.5), xticks=[1, 2, 3, 4, 5, 6, 7, 8],
              yticks=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5], xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{k}\ (\text{V})",
              yfmt=lambda v: fi(v, 1))
    if fit:
        ax.line([(0.4, k * 0.4 + b), (4.3, k * 4.3 + b)], INK, 2, "7 6")
        ax.line([(4.3, k * 4.3 + b), (7.9, k * 7.9 + b)], INK, 3)
        ya, yb = k * 5.0 + b, k * 7.0 + b
        f.line(ax.X(5), ax.Y(ya), ax.X(7), ax.Y(ya), MUTED, 1.5, "6 5")
        f.line(ax.X(7), ax.Y(ya), ax.X(7), ax.Y(yb), MUTED, 1.5, "6 5")
        f.tex(ax.X(6), ax.Y(ya) + 20, r"\Delta f", "middle", MUTED)
        f.tex(ax.X(7) + 10, ax.Y((ya + yb) / 2) + 10, r"\Delta U_\text{k}", "start", MUTED)
        f.tex(ax.X(0.6), ax.Y(3.0), r"\text{kulmakerroin } k = \tfrac{h}{e}", "start", bg=True)
    for x, y, col in pts:
        ax.point(x, y, col, 6.5)
    return f.svg()


def ryhma():
    """Tarkista osaamisesi: another group's measurement, the points and their fitted line on graph paper; the slope is
    read from two grid crossings of the line, (4,6; 1,80) and (7,0; 2,80)."""
    f = Fig("fy86-ryhma", 380, "Kuvaaja mittakaavassa ruutupaperilla: LEDien kynnysjännite U k voltteina 1,5:stä 3,5:een valon taajuuden f "
            "funktiona, taajuusakseli 4,0:sta 8,0:aan kertaa 10 potenssiin 14 hertsiä. Pystysuuntaiset ruutuviivat ovat 0,2 kertaa "
            "10 potenssiin 14 hertsin ja vaakasuuntaiset 0,1 voltin välein. Kuusi mittauspistettä ja niihin sovitettu suora, "
            "joka kulkee täsmälleen ruutuviivojen risteysten kautta kohdissa taajuus 4,6 ja jännite 1,80 sekä taajuus 7,0 ja jännite 2,80.")
    xt = [round(4.2 + 0.2 * i, 1) for i in range(20)]
    yt = [round(1.6 + 0.1 * i, 1) for i in range(20)]
    ax = Axes(f, (100, 322), (420, 64), x=(4.0, 8.0), y=(1.5, 3.5), xticks=xt, yticks=yt,
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{k}\ (\text{V})",
              xfmt=lambda v: fi(v, 0) if abs(v - round(v)) < 1e-9 else "",
              yfmt=lambda v: fi(v, 1) if abs(v * 2 - round(v * 2)) < 1e-9 else "")
    f.tex(ax.x0 - 12, ax.y0, fi(1.5, 1), "end")
    f.tex(ax.x0, ax.y0 + 24, fi(4, 0), "middle")
    k = 1.0 / 2.4                                               # V per 10^14 Hz: through (4,6; 1,80) and (7,0; 2,80)
    line = lambda x: 1.80 + k * (x - 4.6)
    ax.line([(4.2, line(4.2)), (7.8, line(7.8))], INK, 3)
    for lam, d in ((650, 0.03), (590, -0.02), (560, 0.02), (505, -0.03), (470, 0.01), (430, -0.01)):
        x = f14(lam)
        ax.point(x, line(x) + d, spectral(lam), 6.5)
    return f.svg()


def hero():
    """The chapter's opening illustration: an adjustable power supply feeds four LEDs on a breadboard at the same
    voltage; the red and the yellow shine, the green glows faintly, the blue stays dark."""
    f = H.hero("fy86-hero", "Kuvitus: laboratorion pöydällä on säädettävä jännitelähde, josta punainen ja musta johto vievät virran "
               "kytkentälevylle. Levyllä on rinnakkain neljä LEDiä samassa jännitteessä. Punainen ja keltainen LED loistavat "
               "kirkkaasti ja lähettävät valoaan aaltoviivoina, vihreä hehkuu himmeästi, ja sininen LED on pimeä.")
    H.tiles(f, 440, 75, RULE_LIGHT, "#f6f1e6")
    f.rect(0, 440, 1200, 160, H.grad(f, "fy86h-floor", RULE_LIGHT, RULE, y1=440, y2=600))   # the floor under the table
    f.add(f'<ellipse cx="85" cy="582" rx="30" ry="5" fill="{MUTED}" fill-opacity="0.3"/>')
    f.add(f'<ellipse cx="1115" cy="582" rx="30" ry="5" fill="{MUTED}" fill-opacity="0.3"/>')
    H.wood(f, 30, 440, 1140, 40, "fy86h-table")
    f.rect(70, 480, 30, 100, IRON, INK, 3); f.rect(1100, 480, 30, 100, IRON, INK, 3)
    # adjustable power supply: case, a dark display with bars, a knob, two terminals
    f.rect(90, 250, 250, 190, H.grad(f, "fy86h-case", ALUMINIUM, METAL_EDGE), INK, 3, 10)
    f.rect(118, 276, 194, 64, INK, None, 2, 6)
    for k, hgt in enumerate((30, 38, 22)):
        f.rect(140 + 54 * k, 324 - hgt, 34, hgt, HOT, None, 2, 3)
    f.circle(170, 390, 28, METAL_EDGE, INK, 3); f.line(170, 390, 186, 370, INK, 4)
    f.circle(262, 392, 13, HOT, INK, 2.5); f.circle(306, 392, 13, INK, INK, 2.5)
    # breadboard with holes
    f.rect(420, 392, 680, 48, WHITE, INK, 3, 6)
    for i in range(34):
        for j in range(2):
            f.rect(436 + 19.5 * i, 404 + 16 * j, 6, 6, RULE, None, 2, 1)
    # wires from the terminals to the rails of the board
    f.path("M262,392 C262,470 380,470 420,404", "none", HOT, 6)
    f.path("M306,392 C306,500 400,500 432,432", "none", INK, 6)
    # four LEDs on the board: lit red and yellow, faint green, dark blue
    for x, lam, glow in ((560, 630, 1.0), (700, 590, 1.0), (840, 525, 0.25), (980, 470, 0.0)):
        col = spectral(lam)
        if glow > 0:
            r = 40 + 90 * glow
            f.add(f'<circle cx="{x}" cy="300" r="{r:g}" fill="{H.glow(f, f"fy86h-g{lam}", WHITE, col)}" fill-opacity="{0.35 + 0.5 * glow:g}"/>')
        f.line(x - 12, 352, x - 12, 404, METAL_EDGE, 4); f.line(x + 12, 352, x + 12, 410, METAL_EDGE, 4)
        body = col if glow > 0 else COLD_LIGHT
        f.path(f"M{x - 30},{352} L{x - 30},{300} A30,30 0 0 1 {x + 30},{300} L{x + 30},{352} Z", body, INK, 3,
               extra=f'fill-opacity="{0.55 + 0.45 * max(glow, 0.3):g}"')
        f.rect(x - 36, 348, 72, 10, body, INK, 3, 3)
        if glow >= 1:
            for ang in (-60, -20, 20, 60):
                a = math.radians(ang - 90)
                photon(f, x + 44 * math.cos(a), 290 + 44 * math.sin(a), x + 150 * math.cos(a), 290 + 150 * math.sin(a), col,
                       period=lam / 40, amp=5, w=4, head=18)
    return f.svg()


FIGURES = {"hero": hero, "vyot": vyot, "spektrit": spektrit, "iu": iu, "sovitus": sovitus, "ryhma": ryhma}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "vyot": "reveals: an electron falling across the band gap gives one photon hf ≈ E_g",
    "spektrit": "reveals: the LED's band is about 20 nm wide, the laser diode's line about 1 nm, the lamp's spectrum continuous",
    "iu": "reveals: U_k of the red, green and blue LED (1,88 V, 2,30 V, 2,52 V) by extending the straight part",
    "sovitus": "reveals: the fitted line of the six LEDs and that its slope is h/e",
    "ryhma": "safe: another group's points and fitted line on graph paper; the slope is not given",
}
