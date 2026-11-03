"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-8` writes them into lesson.md.
Nuclide data (decay modes, level and gamma energies) from NNDC NuDat 3 (ENSDF), the same numbers as lesson-answers.py."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, GOOD, GOOD_LIGHT, PAPER, GRAIN, n)
import herolib as H

PROTON, NEUTRON = HOT, ALUMINIUM          # protons red, neutrons light grey (with ink outlines)
ALPHA, BETA, GAMMA = "#7048e8", COLD, HEAT  # alpha violet, beta (electron) blue, gamma photon orange


def photon(f, x1, y1, x2, y2, color=GAMMA, w=3, amp=7, head=15):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2), the wave along the shaft and a filled head."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    shaft = L - head; waves = max(2, round(shaft / 26))
    pts = []
    for i in range(0, 121):
        t = i / 120 * shaft
        s = amp * math.sin(2 * math.pi * waves * t / shaft) * min(1, t / 6, (shaft - t) / 6)
        pts.append(f"{n(x1 + ux * t + px * s)},{n(y1 + uy * t + py * s)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def nucleus(f, cx, cy, Z, N, r=9, seed=1):
    """A nucleus: Z protons and N neutrons packed in a disc (sunflower packing), mixed in a fixed pseudo-random order."""
    A = Z + N
    kinds = [1] * Z + [0] * N
    order = sorted(range(A), key=lambda k: H.rnd(k, seed))
    kinds = [kinds[k] for k in order]
    g = math.pi * (3 - math.sqrt(5))
    pts = [(cx + 1.02 * r * math.sqrt(k + 0.5) * math.cos(k * g), cy + 1.02 * r * math.sqrt(k + 0.5) * math.sin(k * g)) for k in range(A)]
    for (x, y), kd in sorted(zip(pts, kinds), key=lambda t: -math.hypot(t[0][0] - cx, t[0][1] - cy)):
        f.circle(x, y, r, PROTON if kd else NEUTRON, INK, 1.5)
    return 1.02 * r * math.sqrt(A) + r                      # the drawn radius


def hero():
    """The chapter's opening illustration: a smoke detector on a ceiling, cut open to show its small americium source
    and the short alpha tracks in the ionisation chamber; a lamp and a window in the room."""
    f = H.hero("fy88-hero", "Kuvitus: olohuoneen katossa on valkoinen pyöreä savuilmaisin, josta osa on piirretty auki. Sisällä "
               "kahden metallilevyn välisessä kammiossa on pieni americiumnäyte, josta lähtee lyhyitä violetteja hiukkasratoja "
               "ilmaan. Huoneessa on ikkuna ja kattovalaisin.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy88h-wall", PAPER, SAND_LIGHT))
    f.rect(0, 0, 1200, 92, WHITE)                                   # ceiling
    f.line(0, 92, 1200, 92, RULE, 3)
    H.window(f, 860, 200, 250, 250, "fy88h-win")
    f.rect(0, 540, 1200, 60, H.grad(f, "fy88h-floor", SAND, GRAIN))
    # a ceiling lamp on the left
    f.line(200, 92, 200, 190, INK, 3)
    f.path("M150,250 Q200,170 250,250 Z", HEAT_LIGHT, INK, 3)
    f.add(f'<ellipse cx="200" cy="262" rx="70" ry="22" fill="{HEAT_LIGHT}" fill-opacity="0.45"/>')
    # the smoke detector, cut open
    f.add(f'<ellipse cx="560" cy="96" rx="190" ry="20" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="3"/>')
    f.path("M370,96 L380,176 Q560,236 740,176 L750,96 Z", WHITE, INK, 3)
    for x in (420, 470, 650, 700):                                   # vent slots
        f.rect(x - 6, 140, 12, 40, RULE_LIGHT, INK, 2, 4)
    # the cutaway chamber
    f.path("M500,110 L620,110 L640,240 L480,240 Z", GLASS, INK, 3)
    f.rect(500, 120, 120, 10, METAL_EDGE, INK, 2)                    # upper plate
    f.rect(488, 222, 144, 10, METAL_EDGE, INK, 2)                    # lower plate
    f.rect(546, 208, 28, 14, HEAT, INK, 2, 3)                        # the americium source
    for k, ang in enumerate((-150, -125, -100, -75, -50, -30)):
        a = math.radians(ang); L = 58 + 18 * H.rnd(k, 3)
        x2, y2 = 560 + L * math.cos(a), 208 + L * math.sin(a)
        f.line(560, 208, x2, y2, ALPHA, 3, cap="round")
        f.circle(x2, y2, 5, ALPHA, WHITE, 1.5)
    f.circle(714, 156, 9, HOT, INK, 2)                               # the status light
    # a sofa under it
    f.rect(330, 430, 460, 110, COLD, INK, 3, 18)
    f.rect(300, 400, 70, 140, COLD, INK, 3, 18); f.rect(750, 400, 70, 140, COLD, INK, 3, 18)
    f.rect(370, 380, 380, 80, "#2f74b5", INK, 3, 16)
    return f.svg()


def isotopes():
    """Ydinajatus: carbon-12 and carbon-14 nuclei with their symbols, protons red and neutrons grey."""
    f = Fig("fy88-iso", 340, "Kaksi hiilen ydintä vierekkäin, ei mittakaavassa. Vasemmalla hiili-12: kuusi punaista protonia ja kuusi "
            "harmaata neutronia, merkintä 12 yläindeksinä ja 6 alaindeksinä C:n edessä. Oikealla hiili-14: kuusi protonia ja "
            "kahdeksan neutronia. Molemmissa protoneja on kuusi, joten ne ovat saman alkuaineen isotooppeja. Alhaalla selite: "
            "punainen pallo on protoni, harmaa neutroni.")
    for cx, Nn, sym, zn, seed in ((150, 6, r"{}^{12}_{\phantom{1}6}\text{C}", r"Z = 6,\ N = 6", 2), (450, 8, r"{}^{14}_{\phantom{1}6}\text{C}", r"Z = 6,\ N = 8", 5)):
        nucleus(f, cx, 120, 6, Nn, r=15, seed=seed)
        f.tex(cx, 222, sym, "middle", size=30)
        f.tex(cx, 262, zn, "middle")
    f.line(300, 24, 300, 280, RULE, 2, "6 6")
    f.circle(170, 312, 11, PROTON, INK, 1.5); f.tex(190, 312, r"\text{protoni } p^+", "start")
    f.circle(380, 312, 11, NEUTRON, INK, 1.5); f.tex(400, 312, r"\text{neutroni } n", "start")
    return f.svg()


def zstable(A):
    """The proton number of the most stable nucleus of mass number A (a smooth fit to the valley of stability)."""
    return A / (1.98 + 0.0155 * A ** (2 / 3))


def chart():
    """Ydinajatus: the N-Z chart schematically, the band of stable nuclei bending above N = Z, regions by decay mode."""
    f = Fig("fy88-chart", 380, "Nuklidikartta kaavamaisesti: vaaka-akselilla neutroniluku N nollasta 140:een, pystyakselilla "
            "järjestysluku Z nollasta 90:een. Vihreä vyö on pysyvien ytimien alue. Kevyillä ytimillä se kulkee katkoviivan N = Z "
            "lähellä, raskailla se kaartuu sen alapuolelle, koska raskaissa pysyvissä ytimissä on enemmän neutroneja kuin "
            "protoneja. Vyön alapuolella neutroneja on liikaa ja ydin hajoaa beeta miinus -hajoamisella, yläpuolella neutroneja "
            "on liian vähän ja ydin hajoaa beeta plus -hajoamisella. Vyön yläpäässä, Z yli 82, raskaat ytimet hajoavat usein "
            "alfahajoamisella: violetti nuoli vyön yläpään oikealla puolella osoittaa vinosti alas vasemmalle, koska alfahajoaminen "
            "pienentää sekä neutronilukua että järjestyslukua kahdella.")
    ax = Axes(f, (80, 336), (470, 76), x=(0, 140), y=(0, 90), xticks=[20, 40, 60, 80, 100, 120, 140], yticks=[20, 40, 60, 80],
              xlabel="N", ylabel="Z", grid=True)
    X, Y = ax.X, ax.Y
    ax.line([(0, 0), (90, 90)], MUTED, 2, "7 6")
    f.tex(X(36), Y(44), r"N = Z", "end", MUTED)
    # the band: from A = 4 to A = 208, half-width about 2,2 units across
    top, bot = [], []
    for A in range(10, 212, 4):
        z = zstable(A); nn = A - z
        top.append((nn - 2.2, z + 2.2)); bot.append((nn + 2.2, z - 2.2))
    pts = top + bot[::-1]
    f.add('<polygon points="' + " ".join(f"{n(X(a))},{n(Y(b))}" for a, b in pts) + f'" fill="{GOOD_LIGHT}" stroke="{GOOD}" stroke-width="2"/>')
    f.tex(X(84), Y(22), r"\text{liikaa neutroneja: } \beta^-", "start", BETA)
    f.tex(X(4), Y(68), r"\text{liian vähän: } \beta^+", "start", HOT)
    # alpha: a heavy nucleus beyond the top end of the band steps down and left: (N, Z) -> (N - 2, Z - 2) per decay
    f.circle(X(139), Y(91), 5, ALPHA, WHITE, 1.5)
    f.arrow(X(139) - 3, Y(91) + 3, X(132), Y(84), ALPHA, 2.5, 12)
    f.tex(X(132), Y(93), r"\alpha", "end", ALPHA)
    f.line(X(67), Y(48), X(96), Y(48), GOOD, 1.5)
    f.tex(X(98), Y(48), r"\text{pysyvät}", "start", GOOD)
    return f.svg()


def decays():
    """Ydinajatus: alpha, beta-minus and gamma decay side by side; what leaves the nucleus and how Z and A change."""
    f = Fig("fy88-dec", 360, "Kolme hajoamislajia vierekkäin, kaavakuva, ei mittakaavassa. Vasemmalla alfahajoaminen: ytimestä "
            "lähtee kahden protonin ja kahden neutronin muodostama alfahiukkanen eli heliumydin, ja ytimen järjestysluku pienenee "
            "kahdella ja massaluku neljällä. Keskellä beeta miinus -hajoaminen: ytimen neutroni muuttuu protoniksi, ytimestä lähtee "
            "elektroni ja antineutriino, järjestysluku kasvaa yhdellä ja massaluku pysyy. Oikealla gammahajoaminen: viritystilassa "
            "oleva ydin lähettää gammafotonin, ja järjestysluku ja massaluku pysyvät samoina.")
    for x in (200, 400): f.line(x, 14, x, 346, RULE, 2, "6 6")
    for i, (title, change) in enumerate(((r"\alpha", r"Z - 2,\ A - 4"), (r"\beta^-", r"Z + 1,\ A\ \text{sama}"), (r"\gamma", r"Z, A\ \text{samat}"))):
        x0 = 200 * i
        nucleus(f, x0 + 64, 150, 9, 11, r=8, seed=7 + i)
        f.tex(x0 + 100, 36, title, "middle", (ALPHA, BETA, GAMMA)[i], size=30)
        f.tex(x0 + 100, 300, change, "middle")
    # alpha: 2 p + 2 n flying out
    for dx, dy, kd in ((0, 0, 1), (14, 0, 0), (0, 14, 0), (14, 14, 1)):
        f.circle(150 + dx, 100 + dy, 7, PROTON if kd else NEUTRON, INK, 1.5)
    f.arrow(112, 128, 140, 112, ALPHA, 3, 12)
    f.tex(160, 160, r"{}^4_2\text{He}", "middle", ALPHA)
    # beta: electron and antineutrino
    f.arrow(312, 130, 352, 100, BETA, 3, 12)
    f.circle(362, 92, 7, BETA, WHITE, 2)
    f.tex(372, 66, r"e^-", "middle", BETA)
    f.line(312, 168, 346, 196, MUTED, 2, "5 4")
    f.circle(354, 202, 5, WHITE, MUTED, 2)
    f.tex(366, 230, r"\bar{\nu}", "middle", MUTED)
    # gamma
    photon(f, 512, 140, 586, 100, GAMMA, 3, 6, 13)
    f.tex(560, 160, r"\gamma", "middle", GAMMA)
    f.tex(470, 240, r"\text{viritystila } {}^{\ast}", "middle")
    return f.svg()


def levels():
    """Ydinajatus: Co-60 beta-minus decay to Ni-60 and the two gamma photons, level energies to scale (NNDC)."""
    f = Fig("fy88-lv", 380, "Energiatasokaavio, energiat mittakaavassa: koboltti-60 hajoaa beeta miinus -hajoamisella nikkeli-60:n "
            "viritystilaan, jonka energia on 2505,8 keV perustilan yläpuolella. Ydin palaa perustilaan kahdessa vaiheessa: ensin "
            "tasolle 1332,5 keV, jolloin lähtee gammafotoni 1173,2 keV, ja sitten perustilaan, jolloin lähtee gammafotoni "
            "1332,5 keV. Tiedot NNDC:n NuDat-tietokannasta.")
    k, y0 = 0.108, 344                                  # px per keV, y of the Ni-60 ground state
    Y = lambda E: y0 - k * E
    # Co-60 level, 2823,1 keV above the Ni-60 ground state (Q value), at left
    f.line(40, Y(2823), 190, Y(2823), INK, 3)
    f.tex(115, Y(2823) - 22, r"{}^{60}_{27}\text{Co}", "middle")
    f.arrow(160, Y(2823) + 3, 262, Y(2505.8) - 3, BETA, 3, 13)
    f.tex(170, Y(2650) + 34, r"\beta^-", "start", BETA)
    for E in (2505.8, 1332.5, 0):
        f.line(250, Y(E), 430, Y(E), INK, 3)
    f.tex(440, Y(2505.8), r"2505{,}8\,\text{keV}", "start")
    f.tex(440, Y(1332.5), r"1332{,}5\,\text{keV}", "start")
    f.tex(440, Y(0), r"0", "start")
    f.tex(340, Y(0) + 24, r"{}^{60}_{28}\text{Ni}", "middle")
    photon(f, 300, Y(2505.8) + 3, 300, Y(1332.5) - 2, GAMMA, 3, 6, 14)
    photon(f, 370, Y(1332.5) + 3, 370, Y(0) - 2, GAMMA, 3, 6, 14)
    f.tex(282, Y(1919), r"1173{,}2", "end", GAMMA)
    f.tex(352, Y(666), r"1332{,}5", "end", GAMMA)
    return f.svg()


def shifts():
    """Kaava: on the N-Z chart one step of each decay from a parent cell: alpha (-2, -2), beta- (-1, +1), beta+ (+1, -1)."""
    f = Fig("fy88-sh", 360, "Nuklidikartan ote, ruudukko: vaaka-akselilla neutroniluku N, pystyakselilla järjestysluku Z, yksi ruutu "
            "yksi yksikkö. Keskellä emoydin. Alfahajoaminen siirtää ytimen kaksi ruutua alas ja kaksi vasemmalle (Z − 2, N − 2). "
            "Beeta miinus -hajoaminen siirtää yhden ruudun ylös ja yhden vasemmalle (Z + 1, N − 1). Beeta plus -hajoaminen "
            "siirtää yhden ruudun alas ja yhden oikealle (Z − 1, N + 1). Gammahajoamisessa ydin pysyy samassa ruudussa.")
    s, x0, y0 = 46, 140, 40                             # cell size, grid's top-left corner; 6 columns x 6 rows
    for i in range(7):
        f.line(x0 + i * s, y0, x0 + i * s, y0 + 6 * s, RULE_LIGHT, 1.5)
        f.line(x0, y0 + i * s, x0 + 6 * s, y0 + i * s, RULE_LIGHT, 1.5)
    C = lambda col, row: (x0 + (col + 0.5) * s, y0 + (row + 0.5) * s)   # row 0 at the top (largest Z)
    pc, pr = 3, 2                                        # the parent
    def cell(col, row, fill, stroke=INK):
        f.rect(x0 + col * s + 3, y0 + row * s + 3, s - 6, s - 6, fill, stroke, 2, 5)
    cell(pc, pr, HEAT_LIGHT)
    cell(pc - 2, pr + 2, WHITE, ALPHA); cell(pc - 1, pr - 1, COLD_LIGHT, BETA); cell(pc + 1, pr + 1, HOT_LIGHT, HOT)
    px, py = C(pc, pr)
    for (col, row), colr, lab, lx, ly, anc in (((pc - 2, pr + 2), ALPHA, r"\alpha", -14, 30, "end"),
                                              ((pc - 1, pr - 1), BETA, r"\beta^-", -8, -30, "end"),
                                              ((pc + 1, pr + 1), HOT, r"\beta^+", 14, 30, "start")):
        tx, ty = C(col, row); L = math.hypot(tx - px, ty - py); ux, uy = (tx - px) / L, (ty - py) / L
        f.arrow(px + ux * 18, py + uy * 18, tx - ux * 16, ty - uy * 16, colr, 3, 12)
        f.tex(tx + lx, ty + ly, lab, anc, colr)
    f.path(f"M{n(px + 10)},{n(py - 17)} A 14 14 0 1 1 {n(px + 17)},{n(py - 6)}", stroke=GAMMA, w=2.5)
    f.tex(px + 30, py - 30, r"\gamma", "start", GAMMA)
    # axes
    f.arrow(x0, y0 + 6 * s + 18, x0 + 6 * s + 30, y0 + 6 * s + 18, INK, 2.5, 13)
    f.tex(x0 + 6 * s + 36, y0 + 6 * s + 18, "N", "start")
    f.arrow(x0 - 18, y0 + 6 * s, x0 - 18, y0 - 6, INK, 2.5, 13)
    f.tex(x0 - 28, y0 + 4, "Z", "end")
    return f.svg()


def spectrum():
    """Task figure: a gamma spectrum of a Co-60 source, counts against photon energy, two peaks (NNDC energies)."""
    f = Fig("fy88-sp", 340, "Kaavamainen gammaspektri koboltti-60-lähteestä: vaaka-akselilla gammafotonin energia kiloelektronivoltteina "
            "nollasta 1600:aan, pystyakselilla havaittujen fotonien määrä mielivaltaisin yksiköin. Matalalla energialla on loiva "
            "tausta, ja spektrissä on kaksi kapeaa piikkiä kohdissa 1173,2 keV ja 1332,5 keV, lähes yhtä korkeina. Energiat "
            "NNDC:n NuDat-tietokannasta; piikkien muoto ja korkeus on piirretty kaavamaisesti.")
    ax = Axes(f, (70, 290), (460, 60), x=(0, 1600), y=(0, 10), xticks=[400, 800, 1200, 1600], yticks=[], xlabel=r"E\ (\text{keV})",
              ylabel=r"\text{fotonien määrä}", grid=False)
    def counts(E):
        bg = 2.2 * math.exp(-E / 380) + (0.9 if E < 1050 else 0.25)
        return bg + 8.0 * math.exp(-((E - 1173.2) / 14) ** 2) + 7.4 * math.exp(-((E - 1332.5) / 15) ** 2)
    ax.curve(counts, 30, 1560, INK, 3, steps=600)
    f.tex(ax.X(1173.2) - 14, ax.Y(9.0), r"1173{,}2", "end", GAMMA)
    f.tex(ax.X(1332.5) + 14, ax.Y(8.4), r"1332{,}5", "start", GAMMA)
    for E in (1173.2, 1332.5): f.line(ax.X(E), ax.Y(counts(E)) - 6, ax.X(E), ax.Y(counts(E)) - 22, GAMMA, 2)
    return f.svg()


FIGURES = {"hero": hero, "isotopes": isotopes, "chart": chart, "decays": decays, "levels": levels, "shifts": shifts, "spectrum": spectrum}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "isotopes": "reveals: C-12 has 6 p + 6 n, C-14 6 p + 8 n",
    "chart": "reveals: which region decays by beta-, beta+ and alpha relative to the stability band",
    "decays": "reveals: how Z and A change in alpha, beta- and gamma decay",
    "levels": "reveals: the Ni-60 levels 2505,8 and 1332,5 keV and that the two gammas are their differences",
    "shifts": "reveals: the chart steps of alpha (-2, -2), beta- (+1, -1) and beta+ (-1, +1) in (Z, N)",
    "spectrum": "safe: two gamma peaks of Co-60 at 1173,2 and 1332,5 keV, no level diagram",
}
