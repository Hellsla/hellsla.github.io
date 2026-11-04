"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-15` writes them into lesson.md.
A proton is drawn with a red outline and a neutron with a grey one (as in the chapter Atomiydin ja radioaktiivinen
hajoaminen); a u quark is a light red disc and a d quark a light blue one, each with its letter; an electron is a small
blue dot, a positron a red one; a photon is an orange wavy arrow, a W boson a violet wavy line; velocities are blue
arrows. Every figure is a schematic, not to scale."""
import math
from figlib import (Fig, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT,
                    COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, GOOD, GOOD_LIGHT, PAPER)
import herolib as H

W_BOSON = "#7048e8"
QUARK = {"u": HOT_LIGHT, "d": COLD_LIGHT}


def wavy(f, x1, y1, x2, y2, colour, period=16.0, amp=6.0, w=3, head=15):
    """A wavy line from (x1, y1) to (x2, y2); with head > 0 it ends in a filled arrowhead (a photon)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    body = L - head
    pts = []
    for i in range(int(body / 1.5) + 1):
        s = i * 1.5; a = amp * math.sin(2 * math.pi * s / period) * min(1, s / 8, (body - s) / 8 if head else 1)
        pts.append((x1 + ux * s + px * a, y1 + uy * s + py * a))
    f.add(f'<polyline points="{" ".join(f"{n(a)},{n(b)}" for a, b in pts)}" fill="none" stroke="{colour}" stroke-width="{w}" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    if head:
        bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
        f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", colour)


def gluon(f, x1, y1, x2, y2, loops=4, r=6.0):
    """A gluon: a coiled spring between two quarks."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    pts = []
    steps = 80
    for i in range(steps + 1):
        t = i / steps; ph = 2 * math.pi * loops * t
        s = t * L + r * 0.8 * math.sin(ph) * min(1, t * 6, (1 - t) * 6)
        a = r * (1 - math.cos(ph)) * 0.5 * min(1, t * 6, (1 - t) * 6)
        pts.append((x1 + ux * s + px * a, y1 + uy * s + py * a))
    f.add(f'<polyline points="{" ".join(f"{n(a)},{n(b)}" for a, b in pts)}" fill="none" stroke="{MUTED}" stroke-width="2" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')


def quark(f, x, y, r, kind, size=24):
    f.circle(x, y, r, QUARK[kind], INK, 2)
    f.tex(x, y - 1, kind, "middle", size=size)


def octagon(cx, cy, R, rot=math.pi / 8):
    return "M" + " L".join(f"{n(cx + R * math.cos(rot + k * math.pi / 4))},{n(cy + R * math.sin(rot + k * math.pi / 4))}" for k in range(8)) + " Z"


# ---------------------------------------------------------------------------------------------------- opening scene
def hero():
    """The chapter's opening illustration: the end view of a large particle detector at the LHC, a collision in its
    centre sending out particle tracks, a person beside it for scale."""
    f = H.hero("fy815-hero", "Kuvitus: suuren hiukkasilmaisimen pääty edestä nähtynä. Ilmaisin on kahdeksankulmainen, "
               "monikerroksinen rakenne, jonka keskellä kulkee ohut suihkuputki. Keskellä kaksi protonia on törmännyt, ja "
               "törmäyskohdasta lähtee joka suuntaan kaarevia hiukkasratoja oransseina, sinisinä, vihreinä ja punaisina "
               "viivoina. Ilmaisimen vieressä lattialla seisoo ihminen, joka on vain pieni osa ilmaisimen korkeudesta.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 560, 1200, 40, RULE)
    f.line(0, 560, 1200, 560, INK, 3)
    cx, cy = 560, 290
    # the support frame under the detector
    f.path(f"M{cx - 210},560 L{cx - 150},470 L{cx + 150},470 L{cx + 210},560 Z", METAL_EDGE, INK, 3)
    for R, fill in ((265, IRON), (228, METAL_EDGE), (188, COPPER), (140, SAND), (96, GLASS)):
        f.path(octagon(cx, cy, R), fill, INK, 3)
    # the muon chambers: light slabs in the outer ring
    for k in range(8):
        a = math.pi / 8 + k * math.pi / 4 + math.pi / 8
        for rr in (236, 252):
            x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
            dx, dy = -math.sin(a) * 34, math.cos(a) * 34
            f.line(x - dx, y - dy, x + dx, y + dy, ALUMINIUM, 6, cap="round")
    # calorimeter cells: radial lines
    for k in range(32):
        a = k * math.pi / 16
        f.line(cx + 146 * math.cos(a), cy + 146 * math.sin(a), cx + 182 * math.cos(a), cy + 182 * math.sin(a), SAND, 2)
    # tracks: curved paths from the centre
    tracks = ((0.3, 210, 0.35, HEAT), (1.2, 175, -0.5, COLD), (2.0, 230, 0.25, GOOD), (2.8, 160, -0.6, HOT),
              (3.5, 205, 0.4, HEAT), (4.2, 185, -0.35, COLD), (4.9, 240, 0.2, HOT), (5.6, 170, -0.45, GOOD))
    for a, R, bend, colour in tracks:
        ex, ey = cx + R * math.cos(a), cy + R * math.sin(a)
        mx, my = cx + R * 0.5 * math.cos(a + bend), cy + R * 0.5 * math.sin(a + bend)
        f.path(f"M{cx},{cy} Q{n(mx)},{n(my)} {n(ex)},{n(ey)}", "none", colour, 4, 'stroke-linecap="round"')
    # the collision flash and the beam pipe
    star = []
    for k in range(16):
        r = 34 if k % 2 == 0 else 14
        a = k * math.pi / 8
        star.append(f"{n(cx + r * math.cos(a))},{n(cy + r * math.sin(a))}")
    f.path("M" + " L".join(star) + " Z", HEAT_LIGHT, HEAT, 2)
    f.circle(cx, cy, 7, WHITE, INK, 2)
    # a person for scale, right of the detector
    H.person(f, 960, 560, shirt=COLD, sc=1.0)
    return f.svg()


# ---------------------------------------------------------------------------------------------------- Ydinajatus
def skaalat():
    """Atom -> nucleus -> proton -> quarks, each magnified from the last."""
    f = Fig("fy815-skaalat", 330, "Kaavakuva, ei mittakaavassa: kolme suurennosta vasemmalta oikealle. Vasemmalla atomi, "
            "noin 10 potenssiin miinus 10 metriä: vaaleansininen elektronipilvi, jossa on kolme sinistä elektronia, ja "
            "keskellä pieni ydin. Keskellä ydin suurennettuna, noin 10 potenssiin miinus 14 metriä: punaisia protoneja ja "
            "harmaita neutroneja tiiviisti yhdessä. Oikealla yksi protoni suurennettuna, noin 10 potenssiin miinus 15 "
            "metriä: sen sisällä kolme kvarkkia u, u ja d, joiden välillä on gluonien jousimaiset viivat. Kvarkit ja "
            "elektronit ovat pienempiä kuin noin 10 potenssiin miinus 18 metriä.")
    y = 135
    # atom
    f.circle(100, y, 80, COLD_LIGHT, COLD, 2)
    for a in (0.6, 2.6, 4.3):
        f.circle(100 + 56 * math.cos(a), y + 56 * math.sin(a), 7, COLD, INK, 1.5)
    f.circle(100, y, 5, HOT, INK, 1.5)
    # magnifier lines to the nucleus
    f.line(103, y - 4, 300, y - 72, MUTED, 1.5, "6 5"); f.line(103, y + 4, 300, y + 72, MUTED, 1.5, "6 5")
    f.circle(300, y, 72, WHITE, MUTED, 1.5)
    nuc = [(-34, -14, True), (-6, -30, False), (24, -22, True), (-26, 18, False), (4, 4, True), (34, 10, False),
           (-4, 34, True), (26, 38, False)]
    for dx, dy, pr in nuc:
        f.circle(300 + dx, y + dy, 17, HOT if pr else ALUMINIUM, INK, 2)
    px, py = 334, y + 10      # this nucleon is magnified: make it a proton
    f.circle(px, py, 17, HOT, INK, 2)
    f.line(px + 6, py - 16, 500, y - 72, MUTED, 1.5, "6 5"); f.line(px + 6, py + 16, 500, y + 72, MUTED, 1.5, "6 5")
    # proton with three quarks
    f.circle(500, y, 72, WHITE, HOT, 3)
    q = [(466, y - 20, "u"), (534, y - 20, "u"), (500, y + 36, "d")]
    for i in range(3):
        (x1, y1, _), (x2, y2, _) = q[i], q[(i + 1) % 3]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        gluon(f, x1 + ux * 20, y1 + uy * 20, x2 - ux * 20, y2 - uy * 20, 3, 6)
    for x, yy, k in q:
        quark(f, x, yy, 19, k)
    for x, name, size in ((100, r"\text{atomi}", r"10^{-10}\,\text{m}"), (300, r"\text{ydin}", r"10^{-14}\,\text{m}"),
                          (500, r"\text{protoni}", r"10^{-15}\,\text{m}")):
        f.tex(x, 246, name, "middle")
        f.tex(x, 288, r"\text{noin}\ " + size, "middle")
    return f.svg()


def taulukko():
    """The standard model's particles: three generations of quarks and leptons, the mediators and the Higgs boson."""
    f = Fig("fy815-taulukko", 378, "Standardimallin perushiukkaset taulukkona. Kolme ensimmäistä saraketta ovat sukupolvet "
            "I, II ja III. Kahdella ylimmällä rivillä ovat kvarkit: u, c ja t, varaus plus kaksi kolmasosaa e, sekä d, s ja "
            "b, varaus miinus yksi kolmasosa e. Kahdella alimmalla rivillä ovat leptonit: elektroni, myoni ja tau, varaus "
            "miinus e, sekä niiden neutriinot, varaus nolla. Neljännessä sarakkeessa ovat välittäjähiukkaset gluoni, "
            "fotoni ja Z-bosoni, varaus nolla, sekä W-bosonit, varaus plus tai miinus e. Viidennessä sarakkeessa on "
            "Higgsin bosoni H, varaus nolla. Kvarkit ovat hiekanvärisissä, leptonit vaaleansinisissä, välittäjät vihreissä "
            "ja Higgsin bosoni punertavassa ruudussa.")
    x0, cw, gap = 134, 84, 5
    y0, ch, rg = 50, 66, 4
    X = lambda c: x0 + c * (cw + gap)
    Y = lambda r: y0 + r * (ch + rg)
    for c, g in enumerate(("I", "II", "III")):
        f.tex(X(c) + cw / 2, 30, r"\text{" + g + "}", "middle")
    rows = [((r"u", r"c", r"t"), r"+2e/3", SAND_LIGHT, (r"g", r"0")),
            ((r"d", r"s", r"b"), r"-e/3", SAND_LIGHT, (r"\gamma", r"0")),
            ((r"e^-", r"\mu^-", r"\tau^-"), r"-e", COLD_LIGHT, (r"Z^0", r"0")),
            ((r"\nu_e", r"\nu_\mu", r"\nu_\tau"), r"0", COLD_LIGHT, (r"W^\pm", r"\pm e"))]

    def cell(c, r, sym, q, fill):
        f.rect(X(c), Y(r), cw, ch, fill, INK, 2, 6)
        f.tex(X(c) + cw / 2, Y(r) + 19, sym, "middle", size=26)
        f.tex(X(c) + cw / 2, Y(r) + 49, q, "middle", MUTED)
    for r, (syms, q, fill, (msym, mq)) in enumerate(rows):
        for c, s in enumerate(syms):
            cell(c, r, s, q, fill)
        cell(3, r, msym, mq, GOOD_LIGHT)
    cell(4, 0, "H", "0", HOT_LIGHT)
    # group labels with brackets
    for (r1, r2, name) in ((0, 1, r"\text{kvarkit}"), (2, 3, r"\text{leptonit}")):
        ya, yb = Y(r1) + 4, Y(r2) + ch - 4
        f.line(126, ya, 126, yb, INK, 2); f.line(126, ya, 131, ya, INK, 2); f.line(126, yb, 131, yb, INK, 2)
        f.tex(120, (ya + yb) / 2, name, "end")
    # legend for the last two columns
    ly = 350
    f.rect(X(0), ly - 11, 22, 22, GOOD_LIGHT, INK, 2, 4)
    f.tex(X(0) + 30, ly, r"\text{välittäjähiukkaset}", "start")
    f.rect(X(3) - 4, ly - 11, 22, 22, HOT_LIGHT, INK, 2, 4)
    f.tex(X(3) + 26, ly, r"\text{Higgsin bosoni}", "start")
    return f.svg()


def hadronit():
    """The proton uud and the neutron udd with their charge sums."""
    f = Fig("fy815-hadronit", 345, "Kaavakuva, ei mittakaavassa: vasemmalla protoni, punareunainen ympyrä, jonka sisällä on "
            "kaksi u-kvarkkia ja yksi d-kvarkki gluonien jousimaisten viivojen yhdistäminä. Alla protoni p on uud, ja "
            "varaus on plus kaksi kolmasosaa plus kaksi kolmasosaa miinus yksi kolmasosa eli plus 1 alkeisvarausta. "
            "Oikealla neutroni, harmaareunainen ympyrä, jonka sisällä on yksi u-kvarkki ja kaksi d-kvarkkia. Alla "
            "neutroni n on udd, ja varaus on plus kaksi kolmasosaa miinus yksi kolmasosa miinus yksi kolmasosa eli 0.")
    for cx, edge, kinds, name, sumtex in ((150, HOT, "uud", r"\text{protoni}\ p = uud", r"q = (+\tfrac{2}{3} + \tfrac{2}{3} - \tfrac{1}{3})\,e = +e"),
                                          (450, METAL_EDGE, "udd", r"\text{neutroni}\ n = udd", r"q = (+\tfrac{2}{3} - \tfrac{1}{3} - \tfrac{1}{3})\,e = 0")):
        cy = 125
        f.circle(cx, cy, 98, WHITE, edge, 3)
        pos = [(cx - 40, cy - 22), (cx + 40, cy - 22), (cx, cy + 44)]
        for i in range(3):
            (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % 3]
            L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
            gluon(f, x1 + ux * 27, y1 + uy * 27, x2 - ux * 27, y2 - uy * 27, 3, 7)
        for (x, y), k in zip(pos, kinds):
            quark(f, x, y, 26, k, 28)
        f.tex(cx, 252, name, "middle")
        f.tex(cx, 300, sumtex, "middle", w=270)
    f.line(300, 30, 300, 320, RULE, 1.5, "6 5")
    return f.svg()


def electron(f, x, y, anti=False):
    f.circle(x, y, 10, HOT if anti else COLD, INK, 2)


def annihilaatio():
    """Left: electron and positron annihilate into two 511 keV photons. Right: pair production near a nucleus."""
    f = Fig("fy815-annihilaatio", 345, "Kaavakuva, ei mittakaavassa, kaksi tapahtumaa. Vasemmalla annihilaatio: ylhäällä "
            "sininen elektroni ja punainen positroni liikkuvat toisiaan kohti, siniset nopeusnuolet. Alempana ne ovat "
            "hävinneet, ja kohtaamiskohdasta lähtee kaksi oranssia fotonia vastakkaisiin suuntiin, kummankin energia "
            "511 kiloelektronivolttia. Oikealla parinmuodostus: oranssi fotoni, jonka energia hf on vähintään 1,022 "
            "megaelektronivolttia, tulee atomiytimen lähelle ja muuttuu elektroniksi ja positroniksi, jotka lähtevät "
            "eri suuntiin.")
    f.line(300, 20, 300, 325, RULE, 1.5, "6 5")
    # left: annihilation
    f.tex(150, 30, r"\text{annihilaatio}", "middle")
    y1 = 92
    electron(f, 50, y1); f.arrow(64, y1, 112, y1, COLD, 3, 13)
    electron(f, 250, y1, True); f.arrow(236, y1, 188, y1, COLD, 3, 13)
    f.tex(50, y1 + 32, "e^-", "middle"); f.tex(250, y1 + 32, "e^+", "middle")
    f.block_arrow(150, 132, 150, 176, RULE_LIGHT, 12, 28, 18)
    y2 = 212
    f.circle(150, y2, 5, HEAT)
    wavy(f, 140, y2, 26, y2, HEAT, 16, 6, 3, 15)
    wavy(f, 160, y2, 274, y2, HEAT, 16, 6, 3, 15)
    f.tex(70, y2 - 32, r"hf", "middle"); f.tex(230, y2 - 32, r"hf", "middle")
    f.tex(150, 268, r"\text{kumpikin}\ hf = 511\,\text{keV}", "middle")
    # right: pair production
    f.tex(450, 30, r"\text{parinmuodostus}", "middle")
    vx, vy = 440, 170
    wavy(f, 318, vy, vx - 4, vy, HEAT, 16, 6, 3, 15)
    f.tex(372, vy - 32, r"hf", "middle")
    f.circle(420, 236, 17, HOT, INK, 2); f.circle(440, 246, 17, ALUMINIUM, INK, 2)
    f.tex(430, 282, r"\text{ydin}", "middle")
    f.line(vx, vy, 530, 104, INK, 2, "5 4"); electron(f, 540, 97); f.arrow(552, 88, 578, 69, COLD, 3, 12)
    f.line(vx, vy, 530, 214, INK, 2, "5 4"); electron(f, 540, 219, True); f.arrow(553, 226, 581, 240, COLD, 3, 12)
    f.tex(520, 66, "e^-", "end"); f.tex(530, 254, "e^+", "end")
    f.tex(450, 318, r"hf \ge 1{,}022\,\text{MeV}", "middle")
    return f.svg()


def valittaja():
    """Two electrons repel by exchanging a photon (a space-time sketch, time upwards)."""
    f = Fig("fy815-valittaja", 330, "Kaavakuva sähkömagneettisesta vuorovaikutuksesta, aika kulkee alhaalta ylös. Kaksi "
            "elektronia lähestyy toisiaan alhaalta. Kohdassa, jossa ne ovat lähimpänä, niiden välillä kulkee oranssi "
            "aaltoviiva, vaihdettu fotoni gamma. Sen jälkeen elektronit loittonevat toisistaan: ne hylkivät toisiaan. "
            "Vasemmassa reunassa ylöspäin osoittava nuoli, aika.")
    f.arrow(46, 300, 46, 60, MUTED, 2.5, 13)
    f.tex(46, 36, r"\text{aika}", "middle", MUTED)
    va, vb, y = (240, 178), (380, 178), 178
    for (sx, sy), (vx, vy), (ex, ey), lab in (((200, 300), va, (150, 52), (150, 300)), ((420, 300), vb, (470, 52), (470, 300))):
        f.line(sx, sy, vx, vy, INK, 3); f.line(vx, vy, ex, ey, INK, 3)
        # arrowheads along the paths
        for (ax, ay), (bx, by) in (((sx, sy), (vx, vy)), ((vx, vy), (ex, ey))):
            mx, my = (ax + bx) / 2, (ay + by) / 2
            L = math.hypot(bx - ax, by - ay); ux, uy = (bx - ax) / L, (by - ay) / L
            f.path(f"M{n(mx + ux * 9)},{n(my + uy * 9)} L{n(mx - ux * 7 - uy * 7)},{n(my - uy * 7 + ux * 7)} "
                   f"L{n(mx - ux * 7 + uy * 7)},{n(my - uy * 7 - ux * 7)} Z", INK)
        electron(f, sx, sy); electron(f, ex, ey)
        f.tex(ex + (-34 if ex < 300 else 34), ey, "e^-", "middle")
        f.tex(sx + (-34 if sx < 300 else 34), sy, "e^-", "middle")
    wavy(f, va[0] + 4, y, vb[0] - 4, y, HEAT, 18, 7, 3, 0)
    f.tex(310, y - 36, r"\gamma", "middle")
    f.tex(310, y + 40, r"\text{fotoni}", "middle")
    return f.svg()


def beeta():
    """Kaava: beta-minus decay at the quark level, time to the right: d -> u + W-, W- -> e- + anti-nu_e."""
    f = Fig("fy815-beeta", 350, "Kaavakuva beeta miinus -hajoamisesta kvarkkitasolla, aika kulkee vasemmalta oikealle. "
            "Vasemmalla neutroni n, kvarkit u, d ja d. Kolme vaakasuoraa viivaa kulkee oikealle. Ylimmät kaksi kvarkkia, "
            "u ja d, jatkavat muuttumattomina. Alimman viivan d-kvarkki muuttuu keskellä u-kvarkiksi ja lähettää violetin "
            "aaltoviivan, W miinus -bosonin, joka kulkee alas oikealle ja muuttuu elektroniksi e miinus ja elektronin "
            "antineutriinoksi. Oikealla protoni p, kvarkit u, d ja u.")
    ys = (90, 140, 190)
    xa, xb, vx = 104, 445, 240
    f.rect(52, 62, 54, 156, WHITE, METAL_EDGE, 3, 26)
    f.rect(443, 62, 54, 156, WHITE, HOT, 3, 26)
    f.tex(79, 40, r"n\ (udd)", "middle")
    f.tex(470, 40, r"p\ (uud)", "middle")
    for y, k1, k2 in zip(ys, "udd", "udu"):
        if y == ys[2]:
            f.line(xa, y, vx, y, INK, 3); f.line(vx, y, xb, y, INK, 3)
        else:
            f.line(xa, y, xb, y, INK, 3)
        quark(f, 79, y, 19, k1); quark(f, 470, y, 19, k2)
    f.circle(vx, ys[2], 5, INK)
    wx, wy = 330, 272
    wavy(f, vx, ys[2], wx, wy, W_BOSON, 16, 6, 3, 0)
    f.tex(268, 252, r"W^-", "end", W_BOSON)
    f.circle(wx, wy, 5, INK)
    f.arrow(wx, wy, 452, 248, INK, 2.5, 13); electron(f, 464, 246)
    f.tex(484, 246, "e^-", "start")
    f.arrow(wx, wy, 452, 312, INK, 2.5, 13); f.circle(464, 314, 9, WHITE, INK, 2)
    f.tex(484, 314, r"\bar{\nu}_e", "start")
    f.arrow(60, 316, 190, 316, MUTED, 2.5, 13)
    f.tex(200, 316, r"\text{aika}", "start", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "skaalat": skaalat, "taulukko": taulukko, "hadronit": hadronit, "annihilaatio": annihilaatio,
           "valittaja": valittaja, "beeta": beeta}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "skaalat": "safe: schematic zoom atom -> nucleus -> proton with three quarks and their sizes",
    "taulukko": "reveals: the standard model chart with every particle's charge",
    "hadronit": "reveals: proton uud and neutron udd with their charge sums +e and 0",
    "annihilaatio": "reveals: e- + e+ -> two 511 keV photons; pair production needs hf >= 1,022 MeV",
    "valittaja": "reveals: electrons repel by exchanging a photon",
    "beeta": "reveals: beta-minus decay d -> u + W-, W- -> e- + anti-nu_e",
}
