"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-1` writes them into lesson.md.
Light is drawn in its real colour (spectral(), FY8 convention); ultraviolet, which cannot be seen, as violet with
the label naming it. Photons are wavy arrows labelled hf, electrons small blue dots e⁻ with blue velocity arrows."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, COLD, COLD_LIGHT, ALUMINIUM,
                    METAL_EDGE, IRON, COPPER, HEAT, HEAT_LIGHT, SAND_LIGHT, GOOD)
import herolib as H

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
E_eV = lambda lam_nm: h * c / (lam_nm * 1e-9) / e          # photon energy in eV from λ in nm
W_NA, W_ZN = 2.28, 4.31
UV = "#7048e8"                                              # ultraviolet drawn as violet (it has no colour of its own)


def spectral(lam):
    """The colour of light of wavelength lam (nm) as hex, an approximation of what the eye sees (380–700 nm)."""
    if lam < 380: return UV
    if lam < 440: r, g, b = (440 - lam) / 60, 0.0, 1.0
    elif lam < 490: r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510: r, g, b = 0.0, 1.0, (510 - lam) / 20
    elif lam < 580: r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645: r, g, b = 1.0, (645 - lam) / 65, 0.0
    else: r, g, b = 1.0, 0.0, 0.0
    k = 0.3 + 0.7 * (lam - 380) / 40 if lam < 420 else 1.0
    to = lambda v: round(255 * (v * k) ** 0.8) if v > 0 else 0
    return "#{:02x}{:02x}{:02x}".format(int(to(r) * 0.86), int(to(g) * 0.78), int(to(b) * 0.86))   # a little darker: it reads on white


def photon(f, x1, y1, x2, y2, colour, period=14.0, amp=6.0, w=3, head=15):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2) with a filled head; period is the drawn wiggle."""
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


def electron(f, x, y, r=7):
    f.circle(x, y, r, COLD, WHITE, 1.5)


def ilmio():
    """Ydinajatus: red light on zinc frees no electrons however many photons arrive; ultraviolet frees them at once."""
    f = Fig("fy81-ilmio", 340, "Kaavakuva, ei mittakaavassa: vaakasuora sinkkilevy kuvan alareunassa. Vasemmalla levylle osuu "
            "neljä punaisen valon fotonia, aallonpituus 650 nanometriä, aaltoviivanuolina, joissa on merkintä hf. Levystä ei "
            "irtoa yhtään elektronia. Oikealla levylle osuu vain kaksi ultraviolettivalon fotonia, aallonpituus 254 nanometriä, "
            "ja kummankin osumakohdasta lähtee sininen elektroni e miinus, jolla on nopeusnuoli v viivalla ylhäällä ylös ja "
            "oikealle. Pystysuora katkoviiva erottaa tilanteet.")
    H.steel(f, "fy81-zinc")
    f.rect(30, 262, 540, 34, "url(#fy81-zinc)", INK, 2.5, 4)
    f.tex(300, 318, r"\text{sinkkilevy}", "middle")
    f.line(300, 18, 300, 250, RULE, 2, "6 6")
    red = spectral(650)
    f.tex(40, 28, r"\text{punainen valo}", "start")
    f.tex(40, 60, r"\lambda = 650\,\text{nm}", "start", MUTED)
    for k in range(4):
        photon(f, 70 + 52 * k, 92, 112 + 52 * k, 256, red, period=650 / 40)
    f.tex(68, 168, "hf", "end", red)
    f.tex(334, 28, r"\text{ultraviolettivalo}", "start")
    f.tex(334, 60, r"\lambda = 254\,\text{nm}", "start", MUTED)
    for k, (x1, x2) in enumerate(((352, 394), (430, 472))):
        photon(f, x1, 92, x2, 256, UV, period=254 / 40)
        ex, ey = x2 + 20, 222 - 4 * k
        electron(f, ex, ey)
        f.arrow(ex + 7, ey - 6, ex + 50, ey - 44, COLD, 3, 13)
    f.tex(350, 168, "hf", "end", UV)
    f.tex(512, 246, "e^-", "start", COLD)
    f.tex(546, 170, r"\overline{v}", "start", COLD)
    return f.svg()


def energia():
    """Ydinajatus: energy to scale (60 units per eV) for sodium: one photon gives its energy hf to one electron."""
    k, yb = 60, 222
    ytop = yb - W_NA * k
    f = Fig("fy81-energia", 304, "Energiakaavio mittakaavassa natriumille: alempi vaakaviiva on elektronin energia metallissa, "
            "ylempi 2,28 elektronivolttia korkeammalla energia, jolla elektroni juuri pääsee irti. Ero on irrotustyö W. Kolme "
            "pystysuoraa fotoninuolta alkavat alemmalta viivalta, ja niiden pituus on fotonin energia hf. Punaisen valon "
            "fotoni, 650 nanometriä ja 1,91 elektronivolttia, jää viivan alle: hf on pienempi kuin W, eikä elektroni irtoa. "
            "Vihreän valon fotoni, 544 nanometriä, ulottuu juuri viivalle: hf on yhtä suuri kuin W. Violetin valon fotoni, "
            "405 nanometriä ja 3,06 elektronivolttia, ulottuu viivan yli; ylimenevä osa, 0,78 elektronivolttia, on "
            "elektronin suurin liike-energia E k max, merkitty sinisellä hakasella.")
    f.line(160, yb, 500, yb, INK, 2.5)
    f.line(160, ytop, 500, ytop, INK, 2.5, "8 6")
    f.tex(150, ytop, r"\text{irti}", "end")
    f.tex(144, yb, r"\text{metallissa}", "end")
    # W as a bracket on the right
    f.line(520, ytop, 520, yb, INK, 2); f.line(512, ytop, 528, ytop, INK, 2); f.line(512, yb, 528, yb, INK, 2)
    f.tex(532, (ytop + yb) / 2, "W", "start")
    for x, lam, rel in ((200, 650, "<"), (320, 544, "="), (440, 405, ">")):
        E = E_eV(lam) if lam != 544 else W_NA
        col = spectral(lam)
        photon(f, x, yb - 8, x, yb - E * k, col, period=lam / 40, amp=5)
        electron(f, x, yb, 7)
        f.tex(x + 14, yb - E * k / 2 - (0 if lam != 405 else 20), "hf", "start", col)
        f.tex(x, yb + 26, fi(lam) + r"\,\text{nm}", "middle", MUTED)
        f.tex(x, yb + 56, "hf " + rel + " W", "middle")
    f.tex(186, yb - 16, "e^-", "end", COLD)
    # E_k,max of the violet photon as a blue bracket
    ytopE = yb - E_eV(405) * k
    f.line(466, ytopE, 466, ytop, COLD, 2.5); f.line(459, ytopE, 473, ytopE, COLD, 2.5); f.line(459, ytop, 473, ytop, COLD, 2.5)
    f.tex(478, (ytopE + ytop) / 2 - 6, r"E_\text{k,max}", "start", COLD)
    return f.svg()


def kuvaaja():
    """Kaava: E_k,max against f for sodium and zinc, parallel lines with slope h starting at the threshold frequencies."""
    hv = h / e * 1e14                                        # eV per 10^14 Hz
    f = Fig("fy81-kuvaaja", 400, "Kuvaaja mittakaavassa: irtoavien elektronien suurin liike-energia elektronivoltteina valon "
            "taajuuden funktiona, taajuusakseli nollasta 16 kertaa 10 potenssiin 14 hertsiin. Natriumin suora alkaa vaaka-"
            "akselilta rajataajuudelta 5,5 kertaa 10 potenssiin 14 hertsiä ja nousee arvoon 4,3 elektronivolttia. Sinkin suora "
            "alkaa rajataajuudelta 10,4 kertaa 10 potenssiin 14 hertsiä ja on natriumin suoran suuntainen. Rajataajuuden "
            "alapuolella elektroneja ei irtoa. Natriumin suoralle on piirretty katkoviivoin kulmakerrointa kuvaava kolmio, ja "
            "merkintä kertoo, että kulmakerroin on Planckin vakio h.")
    ax = Axes(f, (96, 340), (420, 56), x=(0, 16), y=(0, 5), xticks=list(range(2, 17, 2)), yticks=[1, 2, 3, 4, 5],
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"E_\text{k,max}\ (\text{eV})")
    for W, col, name in ((W_NA, HEAT, "natrium"), (W_ZN, IRON, "sinkki")):
        f0 = W / hv
        ax.line([(f0, 0), (16, hv * 16 - W)], col, 3)
        ax.point(f0, 0, col)
        f.tex(ax.X(16) + 10, ax.Y(hv * 16 - W), r"\text{" + name + "}", "start", col)
        f.tex(ax.X(f0) - 8, ax.y0 - 20, "f_0", "end", col)
    # slope triangle on the sodium line
    a, b = 9, 13
    ya, yb_ = hv * a - W_NA, hv * b - W_NA
    f.line(ax.X(a), ax.Y(ya), ax.X(b), ax.Y(ya), MUTED, 1.5, "6 5")
    f.line(ax.X(b), ax.Y(ya), ax.X(b), ax.Y(yb_), MUTED, 1.5, "6 5")
    f.tex(ax.X(1.2), ax.Y(3.7), r"\text{kulmakerroin} = h", "start", bg=True)
    return f.svg()


def hero():
    """The chapter's opening illustration: two charged electroscopes with zinc plates; ultraviolet light discharges one,
    bright red light leaves the other charged."""
    f = H.hero("fy81-hero", "Kuvitus: laboratorion pöydällä on kaksi lasikupuista elektroskooppia, joiden päällä on kiiltävä "
               "sinkkilevy. Vasemman yllä pieni ultraviolettilamppu loistaa violettina, levystä lentää pieniä sinisiä "
               "elektroneja ja elektroskoopin lehdet riippuvat alhaalla. Oikean yllä suuri punainen lamppu loistaa kirkkaasti, "
               "mutta elektroneja ei irtoa ja elektroskoopin lehdet ovat yhä erillään.")
    H.tiles(f, 480, 75, RULE_LIGHT, "#f6f1e6")
    H.wood(f, 30, 480, 1140, 40, "fy81h-table")
    f.rect(70, 520, 30, 66, IRON, INK, 3); f.rect(1100, 520, 30, 66, IRON, INK, 3)
    H.steel(f, "fy81h-zinc")
    red = spectral(650)
    for cx, uv in ((390, True), (820, False)):
        # glass dome on a base, rod with leaves, zinc plate on top
        f.rect(cx - 130, 446, 260, 34, METAL_EDGE, INK, 3, 4)
        f.path(f"M{cx - 112},446 L{cx - 112},300 Q{cx - 112},222 {cx},222 Q{cx + 112},222 {cx + 112},300 L{cx + 112},446 Z", GLASS, INK, 3,
               extra='fill-opacity="0.85"')
        f.rect(cx - 9, 178, 18, 64, ALUMINIUM, INK, 2)
        f.line(cx, 242, cx, 370, INK, 6)
        if uv:   # discharged: the leaves hang down
            f.path(f"M{cx - 2},336 L{cx - 12},420 L{cx - 2},420 Z", COPPER, INK, 2)
            f.path(f"M{cx + 2},336 L{cx + 12},420 L{cx + 2},420 Z", COPPER, INK, 2)
        else:    # still charged: the leaves spread
            f.path(f"M{cx - 2},336 L{cx - 62},402 L{cx - 54},410 Z", COPPER, INK, 2)
            f.path(f"M{cx + 2},336 L{cx + 62},402 L{cx + 54},410 Z", COPPER, INK, 2)
        f.rect(cx - 110, 162, 220, 18, "url(#fy81h-zinc)", INK, 3, 3)
    # the ultraviolet lamp: small, a violet glow, two photons, electrons leaving the plate
    f.add(f'<circle cx="236" cy="52" r="74" fill="{H.glow(f, "fy81h-uvglow", "#b9a5f5", UV)}"/>')
    f.rect(186, 20, 100, 44, INK, None, 2, 10)
    f.rect(196, 60, 80, 12, UV, None, 2, 4)
    for x1, x2 in ((222, 330), (262, 404)):
        photon(f, x1, 86, x2, 154, UV, period=9, amp=6, w=4, head=18)
    for x, y in ((352, 112), (446, 96), (478, 134), (420, 62), (496, 74)):
        f.circle(x, y, 9, COLD, WHITE, 2.5)
    # the red lamp: large and bright, many photons that free nothing
    f.add(f'<circle cx="1000" cy="48" r="120" fill="{H.glow(f, "fy81h-redglow", "#ffb3a8", red)}"/>')
    f.path("M916,12 L1084,12 L1064,66 L936,66 Z", INK)
    f.rect(944, 62, 112, 16, red, None, 2, 6)
    for k in range(4):
        photon(f, 950 + 32 * k, 90, 752 + 46 * k, 154, red, period=20, amp=5, w=4, head=18)
    return f.svg()


FIGURES = {"hero": hero, "ilmio": ilmio, "energia": energia, "kuvaaja": kuvaaja}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "ilmio": "reveals: red light frees no electrons from zinc, ultraviolet frees them",
    "energia": "reveals: for sodium hf < W at 650 nm, hf = W at 544 nm, E_k,max = 0,78 eV at 405 nm",
    "kuvaaja": "reveals: E_k,max(f) lines of sodium and zinc start at f0 = W/h and have slope h",
}
