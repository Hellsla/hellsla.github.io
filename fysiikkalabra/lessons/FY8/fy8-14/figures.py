"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-14` writes them into lesson.md.
Colours as in the chapters Ionisoiva säteily ja elimistö and Säteilyannos ja säteilyturvallisuus Suomessa: photons
(X-ray, gamma, annihilation) orange and wavy, electrons and beta particles blue dots, the positron red, soft tissue light
red, bone sand. The numbers come from lesson-answers.py (imported, one source)."""
import importlib.util, math, pathlib
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD,
                    COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, PAPER, SAND_LIGHT, SAND, SAND_DARK, GRAIN, GOOD)
import herolib as H

_spec = importlib.util.spec_from_file_location("fy814_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)
PHOTON, ELECTRON, POSITRON, TISSUE, BONE = HEAT, COLD, HOT, HOT_LIGHT, SAND_LIGHT


def photon(f, x1, y1, x2, y2, color=PHOTON, w=3, amp=6, head=14):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2), the wave along the shaft and a filled head."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    shaft = L - head; waves = max(2, round(shaft / 24))
    pts = []
    for i in range(0, 121):
        t = i / 120 * shaft
        s = amp * math.sin(2 * math.pi * waves * t / shaft) * min(1, t / 6, (shaft - t) / 6)
        pts.append(f"{n(x1 + ux * t + px * s)},{n(y1 + uy * t + py * s)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def rontgen():
    """Ydinajatus: an X-ray tube above a forearm (soft tissue and two bones) and a detector; the bones cast a shadow."""
    f = Fig("fy814-rontgen", 380, "Kaavakuva, ei mittakaavassa: röntgenkuvaus. Ylhäällä lasinen röntgenputki: vasemmalla "
            "hehkuva katodi, josta elektronit kiihdytetään oikealle anodille. Anodista lähtee alaspäin viuhkana "
            "röntgenfotoneja aaltoviivoina. Niiden tiellä on kyynärvarren poikkileikkaus: pehmytkudos ja sen sisällä kaksi "
            "luuta. Luihin osuvat fotonit pysähtyvät, muut jatkavat kudoksen läpi alla olevaan ilmaisimeen. Ilmaisimeen "
            "piirtyy luiden kohdalle vaaleampi varjo, koska sinne osuu vähemmän säteilyä.")
    F = (400, 84)                                                     # focal spot on the anode
    arm, bones = (400, 205, 132, 46), [(362, 207, 22), (442, 210, 17)]
    yd = 304
    # the detector with the shadow: shade each 4-unit strip by the bone length on the ray from F to it
    for xd in range(250, 550, 4):
        L = 0.0
        for (bx, by, r) in bones:
            ux, uy = xd + 2 - F[0], yd - F[1]; m = math.hypot(ux, uy); ux, uy = ux / m, uy / m
            b = (F[0] - bx) * ux + (F[1] - by) * uy; c = (F[0] - bx) ** 2 + (F[1] - by) ** 2 - r * r
            if b * b - c > 0: L += 2 * math.sqrt(b * b - c)
        f.rect(xd, yd, 4, 22, IRON if L == 0 else METAL_EDGE if L < 18 else ALUMINIUM if L < 34 else WHITE)
    f.rect(250, yd, 300, 22, "none", INK, 2.5)
    # the tube: glass envelope, cathode and anode
    f.rect(222, 26, 248, 58, GLASS, INK, 2.5, 26)
    f.rect(236, 44, 14, 22, IRON, INK, 2); f.path("M250,50 q5,5 0,10", "none", HEAT, 2.5)
    f.path("M392,40 L436,40 L436,74 L406,74 Z", IRON, INK, 2)
    for k in range(6): f.circle(268 + k * 22, 55, 4.5, ELECTRON, WHITE, 1.5)
    f.arrow(380, 55, 398, 55, ELECTRON, 2, 9)
    f.tex(310, 72, "e^-", "middle", ELECTRON)
    f.tex(210, 55, r"\text{röntgenputki}", "end")
    # the arm
    f.add(f'<ellipse cx="{arm[0]}" cy="{arm[1]}" rx="{arm[2]}" ry="{arm[3]}" fill="{TISSUE}" stroke="{INK}" stroke-width="2.5"/>')
    for (bx, by, r) in bones:
        f.circle(bx, by, r, BONE, INK, 2.5); f.circle(bx, by, r * 0.38, SAND, None)
    # photons: rays from F; those through a bone end at the bone
    for xd in (266, 316, 368, 412, 462, 520):
        ux, uy = xd - F[0], yd - F[1]; m = math.hypot(ux, uy); ux, uy = ux / m, uy / m
        stop = None
        for (bx, by, r) in bones:
            b = (F[0] - bx) * ux + (F[1] - by) * uy; c = (F[0] - bx) ** 2 + (F[1] - by) ** 2 - r * r
            if b * b - c > 0: t = -b - math.sqrt(b * b - c); stop = t if stop is None or t < stop else stop
        tend = stop if stop is not None else (yd - 2 - F[1]) / uy
        photon(f, F[0] + ux * 34, F[1] + uy * 34, F[0] + ux * tend, F[1] + uy * tend, PHOTON, 2.5, 3.5, 11)
    f.tex(250, 166, r"\text{pehmytkudos}", "end")
    f.line(536, 206, 470, 210, INK, 1.5); f.tex(542, 206, r"\text{luu}", "start")
    f.tex(238, yd + 11, r"\text{ilmaisin}", "end")
    f.tex(400, 352, r"\text{luiden varjo}", "middle")
    f.line(400, 336, 400, 330, INK, 1.5)
    return f.svg()


def pet():
    """Ydinajatus: a positron from F-18 annihilates with an electron; the two 511 keV photons fly in opposite directions
    to two detectors of the ring, and the source lies on the line between them."""
    f = Fig("fy814-pet", 380, "Kaavakuva, ei mittakaavassa: PET-kuvaus. Vasemmalla potilaan poikkileikkaus ilmaisinrenkaan "
            "keskellä. Kehon sisällä fluori-18-ydin lähettää positronin, joka kulkee lyhyen matkan ja kohtaa elektronin. "
            "Kohtaamispisteestä lähtee kaksi fotonia vastakkaisiin suuntiin, ja ne osuvat renkaan kahteen ilmaisimeen, jotka "
            "on väritetty oransseiksi. Ilmaisimien välille on piirretty katkoviivajana, jolla annihilaation täytyy olla. "
            "Oikealla suurennos: positroni ja elektroni kohtaavat, ja syntyy kaksi 511 kiloelektronivoltin fotonia, jotka "
            "lähtevät 180 asteen kulmassa toisiinsa nähden.")
    C, R, ND = (186, 176), 146, 36
    A = (210, 160)                                                    # the annihilation point
    th = math.radians(-28); ux, uy = math.cos(th), math.sin(th)
    def ring_t(sgn):
        b = (A[0] - C[0]) * ux * sgn + (A[1] - C[1]) * uy * sgn; c = (A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2 - R * R
        return -b + math.sqrt(b * b - c)
    t1, t2 = ring_t(1), ring_t(-1)
    P1, P2 = (A[0] + ux * t1, A[1] + uy * t1), (A[0] - ux * t2, A[1] - uy * t2)
    hit = {int(((math.atan2(P[1] - C[1], P[0] - C[0]) + 2 * math.pi) % (2 * math.pi)) / (2 * math.pi) * ND) for P in (P1, P2)}
    for d in range(ND):
        a0, a1 = 2 * math.pi * d / ND + 0.02, 2 * math.pi * (d + 1) / ND - 0.02
        pts = [(C[0] + r * math.cos(a), C[1] + r * math.sin(a)) for a, r in ((a0, R), (a1, R), (a1, R + 14), (a0, R + 14))]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", HEAT if d in hit else ALUMINIUM, INK, 1.5)
    f.add(f'<ellipse cx="{C[0]}" cy="{C[1] + 6}" rx="104" ry="70" fill="{TISSUE}" stroke="{INK}" stroke-width="2.5"/>')
    f.line(P1[0], P1[1], P2[0], P2[1], MUTED, 1.5, "7 5")
    N0 = (196, 178)                                                   # the F-18 nucleus
    for k, (dx, dy) in enumerate(((0, 0), (5, 3), (-4, 4), (2, -5), (-5, -3), (6, -3))):
        f.circle(N0[0] + dx, N0[1] + dy, 4, HOT if k % 2 else IRON, WHITE, 1)
    f.path(f"M{N0[0] + 8},{N0[1] - 4} q4,-8 8,-6 q4,2 6,-8", "none", POSITRON, 2.5)
    f.circle(A[0], A[1], 5, POSITRON, WHITE, 1.5)
    photon(f, A[0] + ux * 8, A[1] + uy * 8, P1[0] - ux * 2, P1[1] - uy * 2, PHOTON, 3, 5, 13)
    photon(f, A[0] - ux * 8, A[1] - uy * 8, P2[0] + ux * 2, P2[1] + uy * 2, PHOTON, 3, 5, 13)
    f.tex(186, 362, r"\text{ilmaisinrengas}", "middle")
    # the enlargement on the right
    f.line(360, 20, 360, 360, RULE, 2, "6 6")
    f.tex(476, 40, r"e^+ + e^- \rightarrow \gamma + \gamma", "middle")
    f.circle(410, 118, 7, POSITRON, WHITE, 2); f.circle(542, 118, 6, ELECTRON, WHITE, 2)
    f.arrow(422, 118, 462, 118, POSITRON, 2.5, 11); f.arrow(530, 118, 490, 118, ELECTRON, 2.5, 11)
    f.tex(410, 88, "e^+", "middle", POSITRON); f.tex(542, 88, "e^-", "middle", ELECTRON)
    f.arrow(476, 140, 476, 182, INK, 2.5, 12)
    f.circle(476, 222, 8, WHITE, HEAT, 3)
    photon(f, 466, 222, 380, 222, PHOTON, 3, 5, 13); photon(f, 486, 222, 572, 222, PHOTON, 3, 5, 13)
    f.tex(424, 194, r"511\,\text{keV}", "middle", PHOTON)
    f.tex(528, 252, r"511\,\text{keV}", "middle", PHOTON)
    f.tex(430, 252, r"180^\circ", "middle")
    f.line(378, 318, 412, 318, MUTED, 1.5, "7 5")
    f.tex(420, 318, r"\text{lähde janalla}", "start")
    return f.svg()


def sadehoito():
    """Ydinajatus: five beams from different directions cross at the tumour: 5 · 0,40 Gy = 2,0 Gy there, 0,40 Gy where one passes."""
    f = Fig("fy814-sade", 360, "Kaavakuva, ei mittakaavassa: sädehoito viidestä suunnasta. Potilaan poikkileikkauksen "
            "keskellä on kasvain. Viisi säteilykeilaa tulee kehon ulkopuolelta eri suunnista, ja jokainen kulkee kasvaimen "
            "kautta kehon läpi. Keilat leikkaavat vain kasvaimen kohdalla, joten kasvain saa viiden keilan annoksen, "
            "5 kertaa 0,40 graytä eli 2,0 graytä. Terve kudos keilan varrella saa vain yhden keilan annoksen, noin 0,40 graytä.")
    T = (252, 180)
    f.add(f'<ellipse cx="250" cy="184" rx="168" ry="112" fill="{TISSUE}" stroke="{INK}" stroke-width="2.5"/>')
    for k in range(5):
        a = math.radians(-90 + 72 * k); ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux
        L1, L2, wb = 146, 140, 17
        pts = [(T[0] - ux * L1 + px * wb, T[1] - uy * L1 + py * wb), (T[0] + ux * L2 + px * wb, T[1] + uy * L2 + py * wb),
               (T[0] + ux * L2 - px * wb, T[1] + uy * L2 - py * wb), (T[0] - ux * L1 - px * wb, T[1] - uy * L1 - py * wb)]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", HEAT, None, 0, 'fill-opacity="0.22"')
        hx, hy = T[0] - ux * (L1 + 6), T[1] - uy * (L1 + 6)
        hp = [(hx + px * 24, hy + py * 24), (hx - px * 24, hy - py * 24), (hx - px * 24 - ux * 14, hy - py * 24 - uy * 14), (hx + px * 24 - ux * 14, hy + py * 24 - uy * 14)]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in hp) + " Z", IRON, INK, 2)
    f.circle(T[0], T[1], 15, HOT, INK, 2.5)
    f.line(T[0] + 16, T[1] - 6, 434, 132, INK, 1.5)
    f.tex(440, 124, r"\text{kasvain}", "start"); f.tex(440, 156, r"2{,}0\,\text{Gy}", "start", HOT)
    B = (T[0] + 0.0, T[1] + 70)                                       # a point on the downward-going beam (k = 0)
    f.line(B[0] + 16, B[1], 434, 252, INK, 1.5)
    f.tex(440, 244, r"\text{terve kudos}", "start"); f.tex(440, 276, r"0{,}40\,\text{Gy}", "start", HEAT)
    f.tex(452, 40, r"\text{keila}", "start")
    f.line(446, 48, 330, 72, INK, 1.5)
    return f.svg()


def kontrasti():
    """Kaava: I/I0 against thickness at about 60 keV for soft tissue (d½ 3,4 cm) and bone (d½ 1,1 cm)."""
    dt, db = LA.DT, LA.DB
    f = Fig("fy814-kontrasti", 380, "Kuvaaja mittakaavassa: läpi päässeen röntgensäteilyn osuus I per I nolla kerroksen "
            "paksuuden d funktiona, paksuus nollasta 8 senttimetriin, fotonien energia noin 60 kiloelektronivolttia. "
            "Pehmytkudoksessa osuus puolittuu jokaisen 3,4 senttimetrin kerroksen jälkeen, luussa jo 1,1 senttimetrin "
            "jälkeen: 1,1 senttimetrin kohdalla luun läpi pääsee puolet ja 2,2 senttimetrin kohdalla neljäsosa, kun "
            "pehmytkudoksen läpi pääsee 3,4 senttimetrin kohdalla puolet. Luun käyrä laskee siis paljon jyrkemmin.")
    ax = Axes(f, (100, 312), (470, 58), x=(0, 8), y=(0, 1.08), xticks=[1, 2, 3, 4, 5, 6, 7, 8], yticks=[0.25, 0.5, 0.75, 1],
              xlabel=r"d\ (\text{cm})", ylabel=r"I : I_0", yfmt=lambda v: fi(v, 2) if v < 1 else "1")
    ax.curve(lambda d: 0.5 ** (d / dt), 0, 8, HOT, 3)
    ax.curve(lambda d: 0.5 ** (d / db), 0, 8, GRAIN, 3)
    ax.guide(dt, 0.5); ax.point(dt, 0.5, HOT)
    for k in (1, 2):
        ax.guide(k * db, 0.5 ** k); ax.point(k * db, 0.5 ** k, GRAIN)
    ax.point(0, 1, INK)
    f.tex(ax.X(8) + 4, ax.Y(0.46), r"\text{pehmytkudos}", "end", HOT, bg=True)
    f.tex(ax.X(0.2), ax.Y(0.36), r"\text{luu}", "start", GRAIN, bg=True)
    f.tex(ax.X(3.6), ax.Y(0.92), r"I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}", "start", INK, bg=True)
    f.tex(ax.X(3.6) + 10, ax.Y(0.62), r"d_{1/2} = 3{,}4\,\text{cm}", "start", HOT, bg=True)
    f.tex(ax.X(4.3), ax.Y(0.15), r"d_{1/2} = 1{,}1\,\text{cm}", "start", GRAIN, bg=True)
    return f.svg()


def mittari():
    """Ydinajatus: a beta thickness gauge on a paper machine: source below the web, detector above, the reading adjusts the press."""
    f = Fig("fy814-mittari", 340, "Kaavakuva, ei mittakaavassa: paperikoneen paksuusmittari. Vaakasuora paperirata kulkee "
            "vasemmalta oikealle kahden telaparin välistä. Radan alapuolella on beetasäteilylähde, josta elektronit "
            "kulkevat sinisinä pisteinä ylöspäin paperin läpi. Osa pysähtyy paperiin, osa pääsee radan yläpuolella olevaan "
            "ilmaisimeen. Ilmaisimesta johto vie lukeman säätölaitteeseen, joka ohjaa telojen puristusta: mitä paksumpi "
            "paperi, sitä vähemmän säteilyä pääsee läpi.")
    y = 176
    for cx in (70, 530):
        for dy in (-26, 26): f.circle(cx, y + dy, 24, ALUMINIUM, INK, 2.5); f.circle(cx, y + dy, 6, IRON, None)
    f.rect(46, y - 3, 508, 6, WHITE, INK, 2)
    f.arrow(384, y - 18, 440, y - 18, INK, 2.5, 12)
    # source below, detector above
    f.rect(258, 232, 84, 50, IRON, INK, 2.5, 6); f.rect(282, 226, 36, 8, HEAT_LIGHT, INK, 1.5)
    f.rect(258, 72, 84, 52, ALUMINIUM, INK, 2.5, 6); f.rect(276, 120, 48, 8, GLASS, INK, 1.5)
    for k, (x, top) in enumerate(((286, 128), (300, 150), (314, 128), (293, 168), (308, 168))):
        y0 = 222
        f.line(x, y0, x, top + 10, ELECTRON, 2)
        f.circle(x, top + 6, 5, ELECTRON, WHITE, 1.5)
    # cable to the controller and back to the rolls
    f.path("M342,94 C400,94 420,60 440,60", "none", INK, 3)
    f.rect(440, 36, 72, 48, WHITE, INK, 2.5, 6); f.rect(452, 46, 48, 18, GLASS, INK, 1.5)
    f.path("M476,84 C476,120 520,120 530,142", "none", INK, 2.5, 'stroke-dasharray="6 5"')
    f.tex(250, 98, r"\text{ilmaisin}", "end")
    f.tex(250, 258, r"\text{lähde}\ (\beta^-)", "end")
    f.tex(362, 214, r"\text{paperirata}", "start")
    f.tex(500, 60, r"\text{säätö}", "start")
    f.tex(300, 316, r"\text{paksumpi paperi: vähemmän läpi}", "middle")
    return f.svg()


def hero():
    """Opening illustration: a PET-CT scanner room: the gantry with its ring, a patient on the bed going in, a monitor
    behind a window showing a cross-section with one bright spot."""
    f = H.hero("fy814-hero", "Kuvitus: sairaalan PET-TT-kuvaushuone. Keskellä suuri valkoinen kuvauslaite, jonka keskellä "
               "on pyöreä aukko. Potilas makaa peiton alla kuvauspöydällä, joka liukuu aukkoon. Vasemmalla seinässä on "
               "ikkuna valvomoon, jossa näytöllä on tumma poikkileikkauskuva ja siinä yksi kirkas oranssi täplä.")
    H.tiles(f, 470, 75, RULE_LIGHT, PAPER)
    f.rect(0, 0, 1200, 470, GLASS)
    # window to the control room with a monitor
    f.rect(60, 120, 300, 220, WHITE, INK, 4, 8)
    f.rect(76, 136, 268, 188, COLD_LIGHT, INK, 2, 4)
    f.rect(130, 170, 160, 110, INK, INK, 3, 6)
    f.add(f'<ellipse cx="210" cy="225" rx="62" ry="38" fill="{IRON}"/>')
    f.circle(232, 214, 9, HEAT_LIGHT); f.circle(232, 214, 5, WHITE)
    f.rect(196, 280, 28, 22, IRON); f.rect(170, 300, 80, 8, IRON)
    # gantry
    f.rect(560, 120, 360, 400, WHITE, INK, 4, 60)
    f.rect(580, 140, 320, 360, ALUMINIUM, None, 0, 48)
    f.circle(740, 310, 128, INK); f.circle(740, 310, 116, GLASS)
    f.add(f'<circle cx="740" cy="310" r="122" fill="none" stroke="{HEAT}" stroke-width="5" stroke-dasharray="14 6"/>')
    f.rect(600, 500, 280, 30, IRON, INK, 3, 6)
    # bed and patient (the head inside the bore)
    f.rect(760, 352, 400, 24, METAL_EDGE, INK, 3, 6); f.rect(1040, 376, 60, 140, IRON, INK, 3, 4)
    f.rect(980, 516, 180, 20, IRON, INK, 3, 4)
    f.path("M700,352 Q700,312 740,312 L1110,320 Q1140,326 1140,352 Z", COLD_LIGHT, INK, 3)
    f.circle(672, 334, 22, SAND_LIGHT, INK, 3)
    f.rect(612, 354, 160, 12, METAL_EDGE, INK, 2, 4)
    return f.svg()


FIGURES = {"hero": hero, "rontgen": rontgen, "pet": pet, "sadehoito": sadehoito, "mittari": mittari, "kontrasti": kontrasti}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "rontgen": "reveals: how an X-ray image arises: bone stops more photons and casts a lighter shadow on the detector",
    "pet": "reveals: e+ + e- -> two 511 keV photons at 180°; the source lies on the line between the two detectors",
    "sadehoito": "reveals: five beams crossing at the tumour: 5 · 0,40 Gy = 2,0 Gy there, 0,40 Gy in healthy tissue on one beam",
    "mittari": "reveals: a beta thickness gauge: thicker paper lets less radiation through to the detector",
    "kontrasti": "reveals: I/I0 at about 60 keV halving every 3,4 cm in soft tissue and every 1,1 cm in bone",
}
