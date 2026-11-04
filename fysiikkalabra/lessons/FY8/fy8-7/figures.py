"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-7` writes them into lesson.md.
Photon E = hf = hc / lambda; laser photon rate N / t = P lambda / (hc) as in lesson-answers.py. Spectral colours: 405 nm
violet, 480 nm cyan, 530/532 nm green, 570 nm yellow-green, 600 nm orange, 620-694 nm red (FY8 brief: real colours,
never colour alone)."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, GRAIN, GOOD, GOOD_LIGHT, PAPER, n)

H_, C_, E_ = 6.626e-34, 2.998e8, 1.602e-19
HC = H_ * C_
def eV(nm): return HC / (nm * 1e-9) / E_

RED, GREEN, VIOLET = HOT, GOOD, "#7048e8"            # 650-694 nm, 532 nm, 405 nm
ELECTRON = COLD
QD = ((2.0, 480, "#1098ad"), (3.0, 530, GOOD), (4.0, 570, "#a8a21f"), (5.0, 600, HEAT), (6.0, 620, HOT))   # d nm, lambda nm


def photon(f, x1, y1, x2, y2, color=RED, w=3, amp=7, waves=None, head=15, phase=0.0):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2), the wave along the shaft and a filled head."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    shaft = L - head; waves = waves or max(2, round(shaft / 26))
    pts = []
    for i in range(0, 121):
        t = i / 120 * shaft
        s = amp * math.sin(2 * math.pi * waves * t / shaft + phase) * min(1, t / 6, (shaft - t) / 6)
        pts.append(f"{n(x1 + ux * t + px * s)},{n(y1 + uy * t + py * s)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def electron(f, x, y, r=9):
    f.circle(x, y, r, ELECTRON, WHITE, 2)


def was(f, x, y, r=9):
    """Where the electron was before the event: a hollow ring."""
    f.circle(x, y, r, WHITE, ELECTRON, 2)


def processes():
    """Ydinajatus: absorption, spontaneous emission and stimulated emission side by side on two levels."""
    f = Fig("fy87-pr", 380, "Kolme tapahtumaa vierekkäin, kaavakuva, ei mittakaavassa. Kussakin on atomin kaksi energiatasoa, alempi E1 ja "
            "ylempi E2, ja sininen piste on elektroni; rengas näyttää, missä se oli ennen tapahtumaa. Vasemmalla absorptio: "
            "fotoni, jonka energia hf on tasojen erotus, tulee atomiin ja nostaa elektronin tasolle E2, ja fotoni katoaa. "
            "Keskellä spontaani emissio: elektroni putoaa itsestään tasolta E2 tasolle E1, ja fotoni lähtee satunnaiseen "
            "suuntaan, tässä vinosti ylös. Oikealla stimuloitu emissio: saapuva fotoni saa viritetyn atomin elektronin "
            "putoamaan, ja atomista lähtee kaksi samanlaista fotonia samaan suuntaan samassa tahdissa.")
    y2, y1 = 80, 236
    f.tex(40, y2, "E_2", "end"); f.tex(40, y1, "E_1", "end")
    caps = ((r"\text{absorptio}",), (r"\text{spontaani}", r"\text{emissio}"), (r"\text{stimuloitu}", r"\text{emissio}"))
    for i in range(3):
        x0 = 48 + 182 * i
        if i: f.line(x0 - 1, 20, x0 - 1, 360, RULE, 2, "6 6")
        f.line(x0 + 12, y2, x0 + 168, y2, INK, 2.5); f.line(x0 + 12, y1, x0 + 168, y1, INK, 3)
        for k, cap in enumerate(caps[i]):
            f.tex(x0 + 90, (318 if len(caps[i]) == 1 else 302 + 34 * k), cap, "middle")
    # absorption: the photon arrives, the electron goes up, the photon is gone
    x0 = 48
    photon(f, x0 + 10, 158, x0 + 92, 158, RED)
    f.tex(x0 + 46, 124, "hf", "middle", RED)
    was(f, x0 + 128, y1); f.arrow(x0 + 128, y1 - 12, x0 + 128, y2 + 13, ELECTRON, 2.5, 13); electron(f, x0 + 128, y2)
    # spontaneous: the electron drops by itself, a photon leaves in a random direction
    x0 = 230
    was(f, x0 + 60, y2); f.arrow(x0 + 60, y2 + 12, x0 + 60, y1 - 13, ELECTRON, 2.5, 13); electron(f, x0 + 60, y1)
    photon(f, x0 + 80, 196, x0 + 166, 112, RED)
    f.tex(x0 + 140, 186, "hf", "middle", RED)
    # stimulated: one photon in, the electron drops, two identical photons out in step
    x0 = 412
    photon(f, x0 + 8, 161, x0 + 70, 161, RED, waves=2)
    f.tex(x0 + 36, 126, "hf", "middle", RED)
    was(f, x0 + 92, y2); f.arrow(x0 + 92, y2 + 12, x0 + 92, y1 - 13, ELECTRON, 2.5, 13); electron(f, x0 + 92, y1)
    photon(f, x0 + 108, 143, x0 + 172, 143, RED, waves=2)
    photon(f, x0 + 108, 181, x0 + 172, 181, RED, waves=2)
    f.tex(x0 + 140, 110, "hf", "middle", RED)
    return f.svg()


def inversion():
    """Ydinajatus: a three-level laser medium (ruby) pumped into inversion: more atoms on E2 than on E1."""
    f = Fig("fy87-inv", 360, "Kolmitasoisen laseraineen, kuten rubiinin, energiatasot, kaavakuva, ei mittakaavassa. Alimpana perustila "
            "E1, ylimpänä lyhytikäinen taso E3 ja niiden välissä pitkäikäinen taso E2. Vihreä nuoli: pumppaus nostaa atomeja "
            "tasolta E1 tasolle E3. Harmaa katkoviivanuoli: atomit siirtyvät tasolta E3 nopeasti ja ilman valoa tasolle E2. "
            "Punainen nuoli: lasersiirtymä tasolta E2 tasolle E1, aallonpituus 694 nm. Siniset pisteet ovat atomeja: tasolla E2 "
            "on seitsemän ja tasolla E1 neljä, eli ylemmällä tasolla on enemmän atomeja kuin alemmalla. Tätä kutsutaan "
            "populaatioinversioksi.")
    y3, y2, y1 = 60, 150, 300
    a, b = 120, 310
    for y, w in ((y3, 2.5), (y2, 2.5), (y1, 3)):
        f.line(a, y, b, y, INK, w)
    f.tex(110, y3, "E_3", "end"); f.tex(110, y2, "E_2", "end"); f.tex(110, y1, "E_1", "end")
    for k in range(7): electron(f, 136 + 14 * k, y2 - 10, 6)
    for k in range(4): electron(f, 136 + 14 * k, y1 - 10, 6)
    f.arrow(240, y1 - 3, 240, y3 + 2, GREEN, 3.5, 15)
    f.path(f"M262,{y3 + 4} L262,{y2 - 16}", stroke=MUTED, w=2.5, extra='stroke-dasharray="6 5"')
    f.path(f"M262,{y2 - 2} L255,{y2 - 16} L269,{y2 - 16} Z", MUTED)
    f.arrow(286, y2 + 3, 286, y1 - 2, RED, 3.5, 15)
    f.tex(330, 105, r"\text{nopea, ilman valoa}", "start", MUTED)
    f.tex(330, 205, r"\text{laser}\ 694\,\text{nm}", "start", RED)
    f.tex(330, 262, r"\text{pumppaus}", "start", GREEN)
    f.tex(216, 336, r"N_2 > N_1", "middle")
    return f.svg()


def cavity():
    """Ydinajatus: the resonator: an active medium between a full mirror and a partly transmitting one, the pump lamp
    under it, photons along the axis bouncing, side photons escaping, the beam out of the right mirror."""
    f = Fig("fy87-cav", 300, "Laserin rakenne, kaavakuva, ei mittakaavassa. Keskellä vaakasuora sauva aktiivista ainetta. Sen vasemmassa "
            "päässä on peili, joka heijastaa kaiken valon, ja oikeassa päässä peili, joka heijastaa 99 prosenttia ja päästää "
            "läpi 1 prosentin. Sauvan alla on pumppauslamppu, jonka valo nostaa atomeja viritystilaan. Sauvan sisällä punaiset "
            "fotonit kulkevat akselin suuntaisesti edestakaisin peilien välillä ja monistuvat. Kaksi fotonia lähtee vinosti "
            "sivulle ja poistuu sauvasta. Oikean peilin läpi tulee ulos kapea punainen lasersäde.")
    f.defs_add(f'<linearGradient id="fy87c-rod" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT_LIGHT}"/>'
               f'<stop offset="0.5" stop-color="{WHITE}"/><stop offset="1" stop-color="{HOT_LIGHT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy87c-lamp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{GOOD_LIGHT}"/></linearGradient>')
    f.rect(150, 112, 300, 60, "url(#fy87c-rod)", INK, 2.5, 8)
    f.rect(108, 98, 14, 88, METAL_EDGE, INK, 2.5, 3)
    f.rect(474, 98, 10, 88, GLASS, INK, 2.5, 3)
    f.line(479, 102, 479, 182, ALUMINIUM, 3)
    # photons along the axis, both ways
    photon(f, 170, 132, 270, 132, RED); photon(f, 300, 132, 400, 132, RED)
    photon(f, 430, 154, 330, 154, RED); photon(f, 260, 154, 160, 154, RED)
    # side photons escape
    photon(f, 222, 162, 250, 206, HOT_LIGHT, 2.5, 5, 2, 12)
    photon(f, 352, 162, 380, 206, HOT_LIGHT, 2.5, 5, 2, 12)
    # the beam out
    f.rect(484, 138, 92, 8, RED, rx=3)
    f.path("M566,130 L586,142 L566,154 Z", RED)
    # pump lamp under the rod, its light going up
    f.rect(160, 216, 280, 22, "url(#fy87c-lamp)", INK, 2.5, 11)
    for x in (190, 300, 410):
        f.arrow(x, 212, x, 182, GREEN, 2.5, 11)
    f.tex(116, 64, r"\text{peili}\ 100\,\%", "middle")
    f.tex(484, 64, r"\text{peili}\ 99\,\%", "middle")
    f.tex(300, 88, r"\text{aktiivinen aine}", "middle")
    f.tex(588, 186, r"\text{lasersäde}", "end", RED)
    f.tex(300, 270, r"\text{pumppaus}", "middle", GREEN)
    return f.svg()


def qdots():
    """Ydinajatus, Kvanttirakenteet: five CdSe quantum dots, diameters to scale relative to each other, in the colour of
    their light, with d, lambda and the photon energy (example data of the inquiry table)."""
    f = Fig("fy87-qd", 370, "Viisi kvanttipistettä allekkain, halkaisijat keskenään mittakaavassa, kukin piirretty lähettämänsä valon "
            "värisenä. Halkaisija 2,0 nm: aallonpituus 480 nm, fotonin energia 2,58 eV, syaani. 3,0 nm: 530 nm, 2,34 eV, "
            "vihreä. 4,0 nm: 570 nm, 2,18 eV, kellanvihreä. 5,0 nm: 600 nm, 2,07 eV, oranssi. 6,0 nm: 620 nm, 2,00 eV, "
            "punainen. Mitä pienempi piste, sitä lyhyempi aallonpituus ja sitä suurempi fotonin energia.")
    for k, (d, nm, col) in enumerate(QD):
        y = 46 + 68 * k
        f.circle(78, y, 5.5 * d, col, INK, 2)
        f.add(f'<circle cx="{n(78 - 1.6 * d)}" cy="{n(y - 1.6 * d)}" r="{1.1 * d:g}" fill="{WHITE}" fill-opacity="0.45"/>')
        f.tex(150, y, f"d = {d:.1f}".replace(".", "{,}") + r"\,\text{nm}", "start")
        f.tex(316, y, rf"\lambda = {nm}\,\text{{nm}}", "start", col if col not in ("#a8a21f",) else INK)
        f.tex(588, y, f"hf = {eV(nm):.2f}".replace(".", "{,}") + r"\,\text{eV}", "end")
    return f.svg()


def rate_graph():
    """Kaava: the photon rate N / t of a 1,0 mW laser against its wavelength: a line through the origin."""
    f = Fig("fy87-rate", 340, "Kuvaaja mittakaavassa: tehon 1,0 milliwattia laserin lähettämien fotonien määrä sekunnissa aallonpituuden "
            "funktiona. Vaaka-akselilla aallonpituus nollasta 700 nanometriin, pystyakselilla fotonien määrä sekunnissa "
            "yksikkönä 10 potenssiin 15 fotonia sekunnissa, nollasta 3,5:een. Kuvaaja on origon kautta kulkeva suora. Siihen on "
            "merkitty kolme laserosoitinta: violetti 405 nm, 2,04; vihreä 532 nm, 2,68; ja punainen 650 nm, 3,27. Pidemmän "
            "aallonpituuden laser lähettää samalla teholla enemmän fotoneja, koska yksi fotoni kantaa vähemmän energiaa.")
    rate = lambda nm: 1.0e-3 * nm * 1e-9 / HC / 1e15
    ax = Axes(f, (96, 290), (486, 74), x=(0, 700), y=(0, 3.5), xticks=[100, 200, 300, 400, 500, 600, 700],
              yticks=[0.5, 1, 1.5, 2, 2.5, 3, 3.5], xlabel=r"\lambda\ (\text{nm})",
              ylabel=r"\tfrac{N}{t}\ (10^{15}\,\tfrac{1}{\text{s}})", yfmt=lambda v: f"{v:g}".replace(".", "{,}"))
    ax.line([(0, 0), (700, rate(700))], INK, 3)
    for nm, col in ((405, VIOLET), (532, GREEN), (650, RED)):
        ax.point(nm, rate(nm), col, 7)
    f.tex(ax.X(405) - 14, ax.Y(rate(405)) - 26, r"405\,\text{nm}", "end", VIOLET)
    f.tex(ax.X(532) - 14, ax.Y(rate(532)) - 26, r"532\,\text{nm}", "end", GREEN)
    f.tex(ax.X(650) - 14, ax.Y(rate(650)) - 26, r"650\,\text{nm}", "end", RED)
    f.tex(470, 250, r"P = 1{,}0\,\text{mW}", "end")
    return f.svg()


def tunnel():
    """Tunneloituminen (optional): the probability of finding an electron before, inside and after a thin barrier."""
    f = Fig("fy87-tun", 320, "Periaatekuva tunneloitumisesta, ei mittakaavassa. Vasemmalta tulee elektroni, jonka energia E, vaakasuora "
            "katkoviiva, on pienempi kuin keskellä olevan harmaan esteen korkeus. Sininen alue kuvaa elektronin havaitsemisen "
            "todennäköisyyttä: esteen vasemmalla puolella se on suuri, esteen sisällä se pienenee nopeasti, ja esteen oikealla "
            "puolella se on pieni mutta ei nolla. Elektroni voi siis löytyä esteen takaa, vaikka sen energia ei riitä esteen yli.")
    base, top, xa, xb = 260, 90, 270, 330
    f.rect(xa, top, xb - xa, base - top, RULE, INK, 2.5, 2)
    f.line(24, base, 576, base, INK, 2.5)
    yE = 180
    f.line(24, yE, 576, yE, MUTED, 1.5, "7 5")
    k = 0.03
    pts = [(30, base - 62)]
    for i in range(0, 61):
        x = 30 + (xa - 30) * i / 60
        pts.append((x, base - 62 - 6 * math.sin(i / 60 * 7 * math.pi)))
    for i in range(0, 41):
        x = xa + (xb - xa) * i / 40
        pts.append((x, base - 62 * math.exp(-k * (x - xa))))
    hb = 62 * math.exp(-k * (xb - xa))
    pts.append((570, base - hb))
    d = "M30," + str(base) + " L" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + f" L570,{base} Z"
    f.path(d, COLD_LIGHT, ELECTRON, 2.5)
    f.tex(300, 66, r"\text{este}", "middle")
    f.tex(36, yE - 22, "E", "start", MUTED)
    f.tex(150, 290, r"\text{tuleva elektroni}", "middle", ELECTRON)
    f.tex(456, 290, r"\text{esteen takana}", "middle", ELECTRON)
    f.arrow(380, 210, 450, 210, ELECTRON, 2.5, 12)
    return f.svg()


def hero():
    """The chapter's opening illustration: in a dim room a laser pointer draws a thin red beam to a small bright dot on
    the screen, while a torch beside it lights a wide, fading patch."""
    f = Fig("fy87-hero", 600, "Kuvitus: hämärässä luokassa pöydällä on laserosoitin ja taskulamppu, jotka osoittavat samaan valkoiseen "
            "varjostimeen. Laserosoittimesta lähtee ohut punainen säde, joka osuu varjostimeen pienenä kirkkaana pisteenä. "
            "Taskulampun valo leviää laajaksi kartioksi ja valaisee varjostimesta suuren, himmeän ja kellertävän alueen.", width=1200, hero=True)
    f.defs_add(f'<linearGradient id="fy87h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MUTED}"/><stop offset="1" stop-color="{INK}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy87h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND}"/><stop offset="1" stop-color="{GRAIN}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy87h-cone" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.75"/><stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0.12"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy87h-patch" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.55"/><stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy87h-dot" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{WHITE}"/><stop offset="0.35" stop-color="{HOT}"/><stop offset="1" stop-color="{HOT}" stop-opacity="0"/></radialGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy87h-wall)")
    f.rect(0, 450, 1200, 150, "url(#fy87h-desk)")
    f.rect(0, 450, 1200, 10, SAND_LIGHT)
    # the screen on its stand
    f.rect(930, 70, 200, 340, WHITE, INK, 3, 6)
    f.rect(1020, 410, 20, 44, IRON, INK, 2.5); f.rect(975, 446, 110, 12, IRON, INK, 2.5, 3)
    # torch: body on the desk, wide cone, faint patch on the screen
    f.path("M300,372 L930,180 L930,400 L300,412 Z", "url(#fy87h-cone)")
    f.add('<ellipse cx="1030" cy="300" rx="96" ry="110" fill="url(#fy87h-patch)"/>')
    f.rect(130, 368, 150, 48, IRON, INK, 3, 10)
    f.path("M280,360 L312,350 L312,430 L280,422 Z", ALUMINIUM, INK, 3)
    f.rect(170, 362, 26, 8, METAL_EDGE, INK, 2, 3)
    f.rect(150, 416, 40, 36, IRON, INK, 3, 4)
    # laser pointer on a small stand, thin beam to a small dot
    f.rect(170, 236, 120, 22, ALUMINIUM, INK, 3, 10)
    f.rect(290, 241, 14, 12, METAL_EDGE, INK, 2.5, 3)
    f.rect(206, 230, 18, 6, HOT, INK, 2, 2)
    f.rect(214, 258, 16, 40, IRON, INK, 2.5); f.rect(190, 296, 64, 12, IRON, INK, 2.5, 3)
    f.rect(190, 308, 64, 60, SAND_LIGHT, INK, 2.5, 3)
    f.line(304, 247, 1018, 196, HOT_LIGHT, 7, cap="round")
    f.line(304, 247, 1018, 196, HOT, 3, cap="round")
    f.add('<circle cx="1018" cy="196" r="22" fill="url(#fy87h-dot)"/>')
    f.circle(1018, 196, 5, WHITE)
    # a notebook on the desk
    f.path("M520,520 L700,498 L730,560 L540,586 Z", WHITE, INK, 3)
    for t in (0.3, 0.5, 0.7):
        f.line(526 + 36 * t, 520 + 66 * t, 706 + 29 * t, 498 + 62 * t, COLD_LIGHT, 2)
    return f.svg()


FIGURES = {"hero": hero, "processes": processes, "inversion": inversion, "cavity": cavity, "qdots": qdots,
           "rate-graph": rate_graph, "tunnel": tunnel}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "processes": "reveals: absorption, spontaneous and stimulated emission and that stimulated photons are identical",
    "inversion": "reveals: the three-level scheme with pump, fast decay, laser 694 nm and N2 > N1",
    "cavity": "reveals: the mirrors 100 % and 99 %, photons along the axis amplified, the beam out of the partial mirror",
    "qdots": "reveals: quantum-dot diameters 2-6 nm with their wavelengths and photon energies",
    "rate-graph": "reveals: N/t of 1,0 mW lasers at 405, 532 and 650 nm on a line through the origin",
    "tunnel": "safe: schematic of the probability before, inside and behind a barrier",
}
