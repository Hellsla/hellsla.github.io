"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-12` writes them into lesson.md.
Colours as in Atomiydin ja radioaktiivinen hajoaminen: alpha violet, beta (electron) blue, gamma photon orange and wavy;
a positive ion red, an electron a small blue dot. Data (photon energies, half-value thicknesses) from lesson-answers.py."""
import importlib.util, math, pathlib
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD,
                    COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, PAPER, SAND_LIGHT, GOOD)
import herolib as H

_spec = importlib.util.spec_from_file_location("fy812_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)
ALPHA, BETA, GAMMA, ION = "#7048e8", COLD, HEAT, HOT


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


def ion_pair(f, x, y, r=3.5):
    """An ion pair: a red positive ion and a blue electron beside it."""
    f.circle(x, y - r - 1, r, ION, WHITE, 1)
    f.circle(x, y + r + 1, r * 0.8, BETA, WHITE, 1)


def energia():
    """Ydinajatus: photon energies on a logarithmic scale; ionising above about 10 eV (water 12,6 eV)."""
    lo, px = -2, 50                                         # 10^-2 eV at x = 30, 50 px per decade
    X = lambda E: 30 + (math.log10(E) - lo) * px
    vis0, vis1 = LA.a["vis-lo"], LA.a["vis-hi"]
    f = Fig("fy812-en", 300, "Fotonin energia logaritmisella asteikolla sadasosaelektronivoltista kymmeneen miljoonaan "
            "elektronivolttiin, jokainen jakoväli kymmenkertainen. Näkyvän valon fotonien energia on 1,7–3,3 elektronivolttia. "
            "Pystysuora katkoviiva 12,6 elektronivoltin kohdalla on veden ionisaatioenergia: sitä suuremman energian fotonit "
            "ovat ionisoivia, ja alue on varjostettu. Ionisoivalla alueella on merkitty röntgenfotoni 60 kiloelektronivolttia "
            "ja cesium-137:n gammafotoni 662 kiloelektronivolttia.")
    xw = X(12.6)
    f.rect(xw, 58, 480 - xw, 142, HOT_LIGHT, extra='fill-opacity="0.35"')
    f.tex(xw - 8, 36, r"\text{ionisoimaton}", "end")
    f.tex(xw + 10, 36, r"\text{ionisoiva}", "start", HOT)
    # the axis
    f.arrow(29, 200, 506, 200, INK, 2.5, 13)
    for k in range(lo, 8):
        f.line(X(10 ** k), 200, X(10 ** k), 207, INK, 2)
    for k in (0, 2, 4, 6):
        f.tex(X(10 ** k), 226, "1" if k == 0 else f"10^{{{k}}}", "middle")
    f.tex(512, 200, r"E\ (\text{eV})", "start")
    # visible light: a rainbow strip
    cols = ["#7048e8", "#1971c2", "#2b8a3e", "#e9c98a", "#e8590c", "#c92a2a"]
    w = (X(vis1) - X(vis0)) / len(cols)
    for i, c in enumerate(cols):
        f.rect(X(vis0) + i * w, 150, w, 50, c)
    f.rect(X(vis0), 150, X(vis1) - X(vis0), 50, "none", INK, 1.5)
    f.tex(X(vis1) - 2, 128, r"\text{näkyvä valo}", "end")
    f.tex((X(vis0) + X(vis1)) / 2, 262, r"1{,}7\text{–}3{,}3\,\text{eV}", "middle", MUTED)
    # the ionisation threshold of water
    f.line(xw, 58, xw, 200, INK, 2, "7 5")
    f.tex(xw + 10, 84, r"12{,}6\,\text{eV}\text{: vesi ionisoituu}", "start", bg=True)
    # X-ray and gamma photons
    for E, lab, anchor, dx in ((60e3, r"\text{röntgen}\ 60\,\text{keV}", "end", -8), (662e3, r"\gamma\ 662\,\text{keV}", "start", 8)):
        f.line(X(E), 200, X(E), 140, GAMMA, 3)
        f.circle(X(E), 140, 6, GAMMA, WHITE, 2)
        f.tex(X(E) + dx, 140, lab, anchor, INK, bg=True)
    return f.svg()


def jaljet():
    """Ydinajatus: tracks through tissue (schematic): alpha short and dense, beta long and sparse, gamma few events."""
    f = Fig("fy812-tr", 380, "Kaavakuva, ei mittakaavassa: kolme vaakasuoraa kudoskaistaa, joissa solut ovat vierekkäin. "
            "Ylimmässä kaistassa alfahiukkanen kulkee vain muutaman solun matkan ja pysähtyy, ja sen rata on täynnä "
            "ionipareja tiheästi vierekkäin. Keskimmäisessä beetahiukkanen eli elektroni kulkee mutkitellen koko kaistan läpi, "
            "ja ionipareja on sen radalla harvakseltaan. Alimmassa gammafotoni kulkee suoraan kaistan läpi ja vuorovaikuttaa vain "
            "kerran: se irrottaa elektronin, joka ionisoi lyhyellä matkalla muutaman molekyylin. Ionipari on piirretty "
            "punaisena positiivisena ionina ja sinisenä elektronina.")
    rows = ((ALPHA, r"\alpha", 70), (BETA, r"\beta", 170), (GAMMA, r"\gamma", 270))
    for _, _, y in rows:                                     # tissue: a band of cells with nuclei
        f.rect(70, y - 38, 500, 76, PAPER, RULE, 1.5, 8)
        for i in range(8):
            x = 70 + i * 62.5
            if i: f.line(x, y - 38, x, y + 38, RULE, 1.5)
            f.add(f'<ellipse cx="{n(x + 31)}" cy="{n(y + 14)}" rx="13" ry="9" fill="{RULE_LIGHT}" stroke="{MUTED}" stroke-width="1.5"/>')
    for col, sym, y in rows:
        f.tex(40, y, sym, "middle", col, size=30)
    # alpha: short, straight, dense
    f.line(70, 70, 205, 70, ALPHA, 4, cap="round")
    for x in range(80, 202, 9): ion_pair(f, x, 70 - 12 if (x // 9) % 2 else 70 + 12, 3)
    f.circle(208, 70, 7, ALPHA, WHITE, 2)
    f.tex(230, 70, r"\text{tiheä ionisaatio, lyhyt matka}", "start", INK, bg=True)
    # beta: long, wiggly, sparse
    pts = [(70 + 6 * i, 170 + 12 * math.sin(i / 5.3) + 6 * math.sin(i / 2.1)) for i in range(84)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=BETA, w=3, extra='stroke-linecap="round"')
    for i in (8, 22, 37, 51, 66, 80):
        ion_pair(f, pts[i][0], pts[i][1] - 16, 3)
    f.tex(320, 220, r"\text{harva ionisaatio}", "middle", INK, bg=True)
    # gamma: passes, one interaction makes a fast electron that ionises a little
    photon(f, 70, 270, 584, 270, GAMMA, 3, 6, 14)
    f.circle(300, 270, 7, HEAT_LIGHT, INK, 1.5)
    sec = [(300, 270), (316, 286), (330, 293), (346, 300)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in sec), stroke=BETA, w=2.5)
    for x, y in sec[1:]: ion_pair(f, x + 4, y - 10, 2.6)
    f.tex(300, 330, r"\text{harvoja vuorovaikutuksia}", "middle", INK)
    # legend
    ion_pair(f, 210, 362, 3.5)
    f.tex(224, 362, r"\text{ionipari: positiivinen ioni ja}\ e^-", "start", MUTED)
    return f.svg()


def lapaisy():
    """Ydinajatus: paper stops alpha, a few millimetres of aluminium stop beta, lead attenuates gamma (schematic)."""
    f = Fig("fy812-la", 360, "Kaavakuva, ei mittakaavassa: vasemmalla säteilylähde, josta lähtee kolme sädettä oikealle. "
            "Violetti alfasäteily pysähtyy ensimmäiseen esteeseen, paperiarkkiin, jonka paksuus on 0,1 millimetriä. Sininen "
            "beetasäteily läpäisee paperin mutta pysähtyy toiseen esteeseen, 5 millimetrin alumiinilevyyn. Oranssi aaltoileva "
            "gammasäteily läpäisee paperin ja alumiinin ja heikkenee 5 senttimetrin lyijykerroksessa; lyijyn jälkeen se on "
            "piirretty ohuempana, koska vain pieni osa siitä pääsee läpi.")
    f.rect(20, 120, 56, 120, IRON, INK, 2.5, 6)
    f.rect(70, 160, 12, 40, HEAT_LIGHT, INK, 2, 2)
    f.tex(48, 270, r"\text{lähde}", "middle")
    # plates
    f.rect(196, 70, 6, 200, WHITE, INK, 2)
    f.rect(318, 70, 26, 200, ALUMINIUM, INK, 2.5)
    f.rect(440, 70, 64, 200, IRON, INK, 2.5)
    for x, lab, d in ((199, r"\text{paperi}", r"0{,}1\,\text{mm}"), (331, r"\text{alumiini}", r"5\,\text{mm}"), (472, r"\text{lyijy}", r"5\,\text{cm}")):
        f.tex(x, 296, lab, "middle"); f.tex(x, 328, d, "middle", MUTED)
    # alpha
    f.arrow(86, 140, 194, 140, ALPHA, 4, 15)
    f.tex(130, 112, r"\alpha", "middle", ALPHA, size=28)
    # beta
    f.arrow(86, 180, 316, 180, BETA, 3, 14)
    f.tex(260, 158, r"\beta", "middle", BETA, size=28)
    # gamma
    photon(f, 86, 220, 440, 220, GAMMA, 3, 7, 1)
    photon(f, 504, 220, 584, 220, GAMMA, 1.5, 4, 12)
    f.tex(390, 196, r"\gamma", "middle", GAMMA, size=28)
    return f.svg()


def gm():
    """Ydinajatus: a Geiger-Müller tube in section: window, gas, wall (-), wire (+); one ion pair grows into an avalanche."""
    f = Fig("fy812-gm", 340, "Kaavakuva, ei mittakaavassa: Geigerin ja Müllerin putki pitkittäin leikattuna. Putki on metallinen "
            "lieriö, joka on täytetty jalokaasulla. Vasemmassa päässä on ohut ikkuna, ja keskellä kulkee ohut metallilanka. "
            "Lanka on positiivisessa ja seinä negatiivisessa jännitteessä, noin 500 volttia. Sininen beetahiukkanen tulee "
            "ikkunan läpi ja irrottaa kaasuatomista elektronin. Elektroni kiihtyy kohti lankaa ja irrottaa matkalla uusia "
            "elektroneja, joten langan lähelle syntyy elektronivyöry. Vyöry näkyy virtapulssina, jonka laskuri laskee.")
    f.rect(120, 110, 350, 120, METAL_EDGE, INK, 3, 10)
    f.rect(132, 122, 326, 96, GLASS, None, 0, 6)
    f.line(120, 120, 120, 220, INK, 5)                       # the thin window, drawn thick to be seen
    f.line(140, 170, 520, 170, GAMMA, 2.5)                   # the wire (anode)
    f.tex(120, 86, r"\text{ikkuna}", "middle")
    f.tex(300, 86, r"\text{metalliseinä}\ (-)", "middle")
    f.tex(480, 196, r"\text{lanka}\ (+)", "start", GAMMA, bg=True)
    # the beta particle, the first ion pair and the avalanche at the wire
    f.arrow(20, 140, 196, 152, BETA, 3, 14)
    f.tex(40, 116, r"\beta", "middle", BETA, size=28)
    f.circle(208, 154, 5, ION, WHITE, 1.5); f.circle(220, 160, 4, BETA, WHITE, 1)
    for k, (dx, dy) in enumerate(((0, 0), (14, -6), (14, 6), (28, -10), (28, 0), (28, 10), (42, -6), (42, 6), (54, -3), (54, 3))):
        f.circle(236 + dx, 170 + dy * 1.4, 3.5, BETA, WHITE, 1)
    f.path("M232,170 L292,150 L292,190 Z", HEAT_LIGHT, extra='fill-opacity="0.5"')
    f.tex(260, 206, r"\text{vyöry}", "middle", INK, bg=True)
    f.tex(400, 140, r"\text{kaasu}", "middle", MUTED)
    # circuit: the wire to the counter, the wall to the voltage source
    f.line(520, 170, 540, 170, INK, 2.5)
    f.rect(500, 124, 80, 46, WHITE, INK, 2.5, 6)
    f.rect(510, 132, 60, 30, COLD_LIGHT, INK, 1.5, 3)
    f.tex(540, 98, r"\text{laskuri}", "middle")
    f.line(300, 230, 300, 290, INK, 2.5); f.line(300, 290, 540, 290, INK, 2.5); f.line(540, 290, 540, 170, INK, 2.5)
    f.line(410, 276, 410, 304, INK, 3); f.line(420, 282, 420, 298, INK, 3)
    f.tex(300, 316, r"U \approx 500\,\text{V}", "start")
    return f.svg()


def vaimeneminen():
    """Kaava: I/I0 against thickness for 662 keV gamma in lead (d½ 5,5 mm) and aluminium (d½ 34 mm)."""
    pb, al = 5.5, 34.0
    f = Fig("fy812-va", 380, "Kuvaaja mittakaavassa: läpi päässeen gammasäteilyn osuus I per I nolla esteen paksuuden d "
            "funktiona, paksuus nollasta 25 millimetriin. Cesium-137:n gammasäteily, kapea säde. Lyijyssä osuus puolittuu "
            "jokaisen 5,5 millimetrin kerroksen jälkeen: 5,5 millimetrin kohdalla puolet, 11 millimetrin kohdalla neljäsosa ja "
            "16,5 millimetrin kohdalla kahdeksasosa. Alumiinissa osuus laskee hitaasti ja on 25 millimetrin kohdalla noin 0,6.")
    ax = Axes(f, (100, 312), (470, 58), x=(0, 25), y=(0, 1.08), xticks=[5, 10, 15, 20, 25], yticks=[0.25, 0.5, 0.75, 1],
              xlabel=r"d\ (\text{mm})", ylabel=r"I : I_0", yfmt=lambda v: fi(v, 2) if v < 1 else "1")
    ax.curve(lambda d: 0.5 ** (d / al), 0, 25, COLD, 3)
    ax.curve(lambda d: 0.5 ** (d / pb), 0, 25, GAMMA, 3)
    for k in (1, 2, 3):
        ax.guide(k * pb, 0.5 ** k); ax.point(k * pb, 0.5 ** k, GAMMA)
    ax.point(0, 1, INK)
    f.tex(ax.X(25) + 8, ax.Y(0.5 ** (25 / al)) - 20, r"\text{alumiini}", "end", COLD, bg=True)
    f.tex(ax.X(5.5) + 14, ax.Y(0.5) - 24, r"\text{lyijy}", "start", GAMMA, bg=True)
    f.tex(ax.X(9), ax.Y(0.98), r"I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}", "start", INK, bg=True)
    f.tex(ax.X(13), ax.Y(0.36), r"d_{1/2} = 5{,}5\,\text{mm}", "start", GAMMA, bg=True)
    return f.svg()


def tuntematon():
    """Tarkista 2: the net count rate behind plates of an unknown material, 800 pulses/min at d = 0, d½ = 12 mm (read off)."""
    R0, D = LA.CHK_R0, LA.CHK_D
    f = Fig("fy812-tu", 380, "Kuvaaja mittakaavassa: gammasäteilyn nettopulssitaajuus pulsseina minuutissa tuntemattoman aineen "
            "levyjen takana levyjen kokonaispaksuuden d funktiona, paksuus nollasta 48 millimetriin, ruudukon väli 2 "
            "millimetriä ja 50 pulssia minuutissa. Ilman levyjä pulssitaajuus on 800 pulssia minuutissa, ja käyrä laskee yhä "
            "loivemmin.")
    ax = Axes(f, (100, 312), (476, 58), x=(0, 48), y=(0, 850), xticks=list(range(2, 49, 2)), yticks=list(range(50, 851, 50)),
              xlabel=r"d\ (\text{mm})", ylabel=r"\text{pulssia}\ /\ \text{min}",
              xfmt=lambda v: fi(v) if v % 6 == 0 else "", yfmt=lambda v: fi(v) if v % 200 == 0 else "")
    ax.curve(lambda d: R0 * 0.5 ** (d / D), 0, 48, GAMMA, 3)
    ax.point(0, R0, GAMMA)
    return f.svg()


def hero():
    """The chapter's opening illustration: a school lab bench: a source in a lead castle, absorber plates in a holder,
    a Geiger-Müller tube on a stand and its counter; radiation from the source, part of it stopped by the plates."""
    f = H.hero("fy812-hero", "Kuvitus: koulun fysiikan laboratorion pöytä. Vasemmalla lyijytiilistä kasattu suoja, jonka "
               "kyljessä on pieni säteilylähde. Lähteestä lähtee oikealle violetteja ja sinisiä hiukkasia ja oransseja "
               "aaltoviivoja. Niiden tiellä on telineessä kolme levyä: paperi, alumiini ja lyijy; violetit hiukkaset "
               "pysähtyvät paperiin, siniset alumiiniin, ja oranssit aallot jatkavat. Oikealla telineeseen kiinnitetty "
               "Geigerin ja Müllerin putki, jonka johto menee laskuriin, ja laskurin näytössä on pulsseja kuvaavia piikkejä.")
    H.tiles(f, 470, 75, RULE_LIGHT, PAPER)
    f.rect(0, 470, 1200, 130, H.grad(f, "fy812h-floor", RULE_LIGHT, RULE, y1=470, y2=600))   # the floor under the table
    f.add(f'<ellipse cx="95" cy="588" rx="30" ry="5" fill="{MUTED}" fill-opacity="0.3"/>')
    f.add(f'<ellipse cx="1105" cy="588" rx="30" ry="5" fill="{MUTED}" fill-opacity="0.3"/>')
    H.wood(f, 40, 470, 1120, 40, "fy812h-table")
    f.rect(80, 510, 30, 76, IRON, INK, 3); f.rect(1090, 510, 30, 76, IRON, INK, 3)
    # lead castle with an opening
    for row in range(4):
        for col in range(3 if row % 2 == 0 else 2):
            x = 150 + col * 80 + (40 if row % 2 else 0); y = 470 - (row + 1) * 46
            f.rect(x, y, 80, 46, IRON, INK, 3, 3)
    f.rect(390, 336, 28, 42, INK, None, 0, 3)                # the source housing against the castle
    f.rect(406, 346, 12, 22, HEAT, None, 0, 2)
    # plates in a holder
    f.rect(470, 456, 190, 14, METAL_EDGE, INK, 3, 3)
    f.rect(490, 250, 10, 206, WHITE, INK, 3)
    f.rect(560, 250, 22, 206, ALUMINIUM, INK, 3)
    f.rect(620, 250, 34, 206, IRON, INK, 3)
    # radiation from the source
    for k, (y, kind) in enumerate(((346, "a"), (366, "b"), (386, "g"), (326, "g"))):
        if kind == "a":
            f.line(420, y, 484, y, ALPHA, 4, cap="round"); f.circle(486, y, 8, ALPHA, WHITE, 2)
        elif kind == "b":
            f.line(420, y, 552, y, BETA, 3, cap="round"); f.circle(554, y, 6, BETA, WHITE, 2)
        else:
            photon(f, 420, y, 620, y, GAMMA, 3.5, 6, 1); photon(f, 654, y, 760, y, GAMMA, 3, 6, 16)
    # the GM tube on a stand
    f.rect(900, 456, 140, 14, METAL_EDGE, INK, 3, 3)
    f.rect(960, 190, 14, 266, ALUMINIUM, INK, 3)
    f.rect(930, 320, 74, 26, IRON, INK, 3, 4)
    f.rect(770, 322, 210, 46, METAL_EDGE, INK, 3, 12)
    f.rect(762, 326, 12, 38, INK, None, 0, 3)
    # cable and counter
    f.path("M980,345 C1060,345 1060,250 1040,230", "none", INK, 4)
    f.rect(960, 120, 200, 120, ALUMINIUM, INK, 3, 12)
    f.rect(980, 138, 160, 70, WHITE, INK, 2.5, 6)
    f.path("M990,190 L1010,190 L1016,150 L1022,190 L1050,190 L1056,160 L1062,190 L1090,190 L1096,146 L1102,190 L1130,190",
           "none", HEAT, 3)
    f.circle(990, 224, 8, INK); f.circle(1130, 224, 8, HEAT)
    return f.svg()


FIGURES = {"hero": hero, "energia": energia, "jaljet": jaljet, "lapaisy": lapaisy, "gm": gm, "vaimeneminen": vaimeneminen,
           "tuntematon": tuntematon}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "energia": "reveals: visible 1,7–3,3 eV is below the ionising threshold 12,6 eV; X-ray and gamma photons above it",
    "jaljet": "reveals: alpha short and dense, beta long and sparse, gamma few interactions",
    "lapaisy": "reveals: paper stops alpha, 5 mm aluminium stops beta, lead attenuates gamma",
    "gm": "reveals: how the GM tube works: window, gas, wire +, wall -, avalanche, counter",
    "vaimeneminen": "reveals: I/I0 = 1/2, 1/4, 1/8 at 5,5, 11 and 16,5 mm of lead; aluminium 0,6 at 25 mm",
    "tuntematon": "safe: net count rate behind an unknown material from 800 pulses/min, 0–48 mm on a 2 mm grid; d½ to be read off",
}
