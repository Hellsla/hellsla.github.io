"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-10` writes them into lesson.md.
A proton is a red disc, a neutron a grey one (as in the chapter Atomiydin ja radioaktiivinen hajoaminen); energy flow is
orange; a photon is a wavy arrow. The atomic masses and every plotted value come from lesson-answers.py (one source)."""
import importlib.util, math, pathlib
from figlib import Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, ALUMINIUM, METAL_EDGE, IRON, PAPER, GOOD_LIGHT
import herolib as H

_spec = importlib.util.spec_from_file_location("fy810_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)
PROTON, NEUTRON = HOT, ALUMINIUM


def nucleon(f, x, y, r, proton):
    f.circle(x, y, r, PROTON if proton else NEUTRON, INK, 2)


def helium(f, x, y, r):
    """Two protons and two neutrons packed together."""
    d = r * 0.92
    for dx, dy, pr in ((-d, -d, True), (d, -d, False), (-d, d, False), (d, d, True)):
        nucleon(f, x + dx, y + dy, r, pr)


def photon(f, x1, y1, x2, y2, colour, period=16.0, amp=6.0, w=3, head=15):
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


def bars(fid, label, lo, hi, ticks, digits, left, right, m_left, m_right, gap_lines):
    """Two mass bars on a vertical axis that starts at lo (broken-axis mark at the foot), the difference bracketed."""
    f = Fig(fid, 350, label)
    x0, y0, y1 = 130, 290, 56
    Y = lambda v: y0 - (v - lo) / (hi - lo) * (y0 - y1)
    for t in ticks:
        f.line(x0, Y(t), 560, Y(t), RULE_LIGHT, 1.5)
        f.line(x0 - 7, Y(t), x0, Y(t), INK, 2)
        f.tex(x0 - 12, Y(t), fi(t, digits), "end")
    f.line(x0, y0, 560, y0, INK, 2.5)
    f.arrow(x0, y0 + 1, x0, y1 - 28, INK, 2.5, 13)
    f.tex(x0 + 12, y1 - 36, r"m\ (\text{u})", "start")
    # the broken-axis mark: the axis does not start from zero
    f.rect(x0 - 9, y0 - 26, 18, 12, WHITE)
    f.line(x0 - 9, y0 - 22, x0 + 9, y0 - 28, INK, 2); f.line(x0 - 9, y0 - 12, x0 + 9, y0 - 18, INK, 2)
    for (xa, xb, top, colour, name, val) in ((160, 240, m_left, RULE, left, m_left), (280, 360, m_right, GOOD_LIGHT, right, m_right)):
        f.rect(xa, Y(top), xb - xa, y0 - Y(top), colour, INK, 2.5)
        f.tex((xa + xb) / 2, Y(top) - 20, fi(val, 6) + r"\,\text{u}", "middle", bg=True)
        f.tex((xa + xb) / 2, y0 + 30, name, "middle")
    # the difference: dashed level of the left bar, bracket beside the right one
    f.line(240, Y(m_left), 428, Y(m_left), MUTED, 1.5, "6 5"); f.line(360, Y(m_right), 428, Y(m_right), MUTED, 1.5, "6 5")
    f.line(420, Y(m_left), 420, Y(m_right), HOT, 3)
    f.line(412, Y(m_left), 428, Y(m_left), HOT, 3); f.line(412, Y(m_right), 428, Y(m_right), HOT, 3)
    mid = (Y(m_left) + Y(m_right)) / 2
    for k, s in enumerate(gap_lines):
        f.tex(437, mid + (k - (len(gap_lines) - 1) / 2) * 34, s, "start", HOT, bg=True)
    return f


def massat():
    """Ydinajatus: helium-4 atom against two hydrogen atoms and two neutrons; the mass defect bracketed."""
    a = LA.a
    fmt = lambda v: f"{v:.6f}".replace(".", ",")
    f = bars("fy810-massat", "Pylväskuva, pystyakseli mittakaavassa mutta katkaistu: se alkaa arvosta 3,990 u eikä nollasta. "
             f"Vasen pylväs on kahden vetyatomin ja kahden neutronin yhteenlaskettu massa, {fmt(a['hook-parts'])} u. Oikea pylväs "
             f"on helium-4-atomin massa, {fmt(a['hook-he'])} u. Pylväiden ero eli massavaje on {fmt(a['hook-diff'])} u, ja se on "
             "merkitty punaisella hakasulkeella.",
             3.990, 4.040, [4.000, 4.010, 4.020, 4.030, 4.040], 3, r"2m_\text{H} + 2m_\text{n}", r"m({}^{4}\text{He})",
             a["hook-parts"], a["hook-he"], [r"\Delta m", fi(round(a["hook-diff"], 6), 6) + r"\,\text{u}"])
    return f.svg()


def reaktio():
    """Kaava, reaction energy: U-238 against Th-234 + He-4; the difference gives Q."""
    a, M = LA.a, LA.MASS
    after = M["Th234"] + M["He4"]
    lab = ("Pylväskuva, pystyakseli mittakaavassa mutta katkaistu: se alkaa arvosta 238,040 u eikä nollasta. Vasen pylväs on "
           "uraani-238-atomin massa, 238,050787 u. Oikea pylväs on alfahajoamisessa syntyvien torium-234- ja helium-4-atomien "
           "yhteinen massa, 238,046204 u. Ero 0,004583 u on merkitty punaisella hakasulkeella, ja se vastaa reaktioenergiaa "
           "Q = 4,27 MeV.")
    f = bars("fy810-reaktio", lab, 238.040, 238.055, [238.045, 238.050, 238.055], 3, r"{}^{238}\text{U}",
             r"{}^{234}\text{Th} + {}^{4}\text{He}", M["U238"], after,
             [fi(round(a["u238-alpha-du"], 6), 6) + r"\,\text{u}", r"Q = " + fi(round(a["u238-alpha-Q"], 2), 2) + r"\,\text{MeV}"])
    return f.svg()


def energia():
    """Ydinajatus: the free nucleons lie higher in energy than the nucleus; joining releases E_B, separating needs it."""
    f = Fig("fy810-energia", 345, "Kaavakuva, ei mittakaavassa: energiatasot. Ylempi vaakaviiva on erillisten protonien ja "
            "neutronien energia: sen päällä on kaksi punaista protonia ja kaksi harmaata neutronia erillään. Alempi vaakaviiva "
            "on helium-4-ytimen energia: sen päällä samat neljä nukleonia tiiviisti yhdessä. Vasemmalla oranssi nuoli ylöspäin: "
            "ytimen hajottaminen nukleoneiksi vaatii sidosenergian E B. Oikealla oranssi nuoli alaspäin: kun ydin muodostuu, "
            "sama energia vapautuu. Tasojen väliin on kirjoitettu E B = Δm c².")
    f.tex(315, 40, r"\text{erilliset protonit ja neutronit}", "middle")
    f.line(140, 112, 490, 112, INK, 3)
    for x, pr in ((205, True), (275, False), (355, True), (425, False)):
        nucleon(f, x, 92, 17, pr)
    f.line(140, 285, 490, 285, INK, 3)
    helium(f, 315, 254, 15)
    f.tex(315, 316, r"\text{ydin}\ {}^{4}_{2}\text{He}", "middle")
    f.tex(315, 150, r"E_\text{B} = \Delta m\,c^2", "middle", HEAT)
    f.block_arrow(95, 282, 95, 116, HEAT, 14, 30, 24)
    f.tex(118, 200, r"\text{tarvitaan}\ E_\text{B}", "start")
    f.block_arrow(538, 116, 538, 282, HEAT, 14, 30, 24)
    f.tex(515, 200, r"\text{vapautuu}\ E_\text{B}", "end")
    return f.svg()


def _curve_axes(f):
    return Axes(f, (130, 300), (540, 60), x=(0, 250), y=(0, 10), xticks=[50, 100, 150, 200, 250], yticks=[2, 4, 6, 8, 10],
                xlabel="A", ylabel=r"E_\text{B}/A\ (\text{MeV})")


def kayra():
    """Kaava: binding energy per nucleon of the table's 32 nuclides against A; He-4, Fe-56, U-238 and H-2 named,
    the directions in which fusion and fission release energy."""
    a = LA.a
    f = Fig("fy810-kayra", 350, "Kuvaaja mittakaavassa: sidosenergia nukleonia kohti megaelektronivoltteina massaluvun A "
            "funktiona, A nollasta 250:een, pystyakseli nollasta 10 megaelektronivolttiin. Pisteet ovat 32 ytimen arvoja "
            "atomimassoista laskettuina. Deuteriumilla arvo on 1,11 MeV, helium-4:llä 7,07 MeV, joka on selvästi naapureitaan "
            "suurempi. Arvo nousee jyrkästi kevyillä ytimillä, on suurin noin 8,8 MeV rauta-56:n ja nikkeli-62:n kohdalla ja "
            "pienenee loivasti raskaita ytimiä kohti: uraani-238:lla 7,57 MeV. Vasemmalla oranssi nuoli ylöspäin oikealle: "
            "fuusio eli kevyiden ytimien yhtyminen. Oikealla oranssi nuoli vasemmalle kohti huippua: fissio eli raskaan "
            "ytimen halkeaminen.")
    ax = _curve_axes(f)
    f.block_arrow(190, 264, 220, 176, HEAT_LIGHT, 12, 28, 22)
    f.tex(232, 226, r"\text{fuusio}", "start", HEAT)
    f.block_arrow(500, 170, 360, 170, HEAT_LIGHT, 12, 28, 22)
    f.tex(430, 204, r"\text{fissio}", "middle", HEAT)
    for s, _, Z, A, _ in LA.NUCLIDES:
        ax.point(A, a[f"{s}{A}-EBA"], HEAT, 5.5)
    he = (ax.X(4), ax.Y(a["He4-EBA"]))
    f.line(he[0] + 3, he[1] - 6, 168, 74, MUTED, 1.5)
    f.tex(170, 62, r"{}^{4}\text{He}", "start")
    fe = (ax.X(56), ax.Y(a["Fe56-EBA"]))
    f.line(fe[0] + 5, fe[1] - 5, 262, 70, MUTED, 1.5)
    f.tex(264, 62, r"{}^{56}\text{Fe}", "start")
    u = (ax.X(238), ax.Y(a["U238-EBA"]))
    f.tex(u[0] - 4, u[1] + 30, r"{}^{238}\text{U}", "middle")
    h2 = (ax.X(2), ax.Y(a["H2-EBA"]))
    f.tex(h2[0] + 14, h2[1] - 4, r"{}^{2}\text{H}", "start")
    return f.svg()


def kayra_points():
    """Task figure (Tarkista 2): the same 32 points, no names and no fusion or fission arrows."""
    a = LA.a
    f = Fig("fy810-kayra-t", 350, "Kuvaaja mittakaavassa: sidosenergia nukleonia kohti megaelektronivoltteina massaluvun A "
            "funktiona, A nollasta 250:een, pystyakseli nollasta 10 megaelektronivolttiin. Pisteet ovat 32 ytimen arvoja "
            "atomimassoista laskettuina: arvo nousee jyrkästi kevyillä ytimillä, on suurin noin 8,8 MeV, kun A on noin 60, ja "
            "pienenee loivasti arvoon 7,6 MeV, kun A on noin 240. Kuvaan ei ole merkitty ytimien nimiä eikä reaktioita.")
    ax = _curve_axes(f)
    for s, _, Z, A, _ in LA.NUCLIDES:
        ax.point(A, a[f"{s}{A}-EBA"], HEAT, 5.5)
    return f.svg()


def hero():
    """The chapter's opening illustration: a balance in a lab; on the lower pan two protons and two neutrons apart, on
    the higher pan the same four packed into a helium nucleus that sends out photons."""
    f = H.hero("fy810-hero", "Kuvitus: laboratorion pöydällä on vanhanaikainen vaaka. Vasemmassa, alempana olevassa vaakakupissa "
               "on erillään kaksi punaista protonia ja kaksi harmaata neutronia. Oikeassa, ylempänä olevassa kupissa samat neljä "
               "hiukkasta ovat tiiviisti yhdessä heliumytimenä, joka hehkuu ja lähettää kaksi oranssia fotonia. Erilliset "
               "hiukkaset painavat enemmän kuin niistä koottu ydin.")
    H.tiles(f, 470, 75, RULE_LIGHT, PAPER)
    H.wood(f, 40, 470, 1120, 40, "fy810h-table")
    f.rect(80, 510, 30, 76, IRON, INK, 3); f.rect(1090, 510, 30, 76, IRON, INK, 3)
    # the balance: foot, post, tilted beam (left side down)
    f.path("M520,470 L680,470 L650,440 L550,440 Z", METAL_EDGE, INK, 3)
    f.rect(588, 170, 24, 272, ALUMINIUM, INK, 3, 4)
    tilt = math.radians(5.5)
    cx, cy, half = 600, 170, 300
    lx, ly = cx - half * math.cos(tilt), cy + half * math.sin(tilt)
    rx, ry = cx + half * math.cos(tilt), cy - half * math.sin(tilt)
    dx, dy = 9 * math.sin(tilt), 9 * math.cos(tilt)
    f.path(f"M{n(lx - dx)},{n(ly - dy)} L{n(rx - dx)},{n(ry - dy)} L{n(rx + dx)},{n(ry + dy)} L{n(lx + dx)},{n(ly + dy)} Z", IRON, INK, 3)
    f.circle(cx, cy, 16, METAL_EDGE, INK, 3)
    # the pointer
    f.path(f"M{n(cx - 7)},{n(cy + 14)} L{n(cx + 7)},{n(cy + 14)} L{n(cx + 3 - 70 * math.sin(tilt))},{n(cy + 120)} Z", HOT, INK, 2)
    for (px, py, drop) in ((lx, ly, 175), (rx, ry, 175)):
        bot = py + drop
        f.line(px, py + 8, px - 105, bot, INK, 2.5); f.line(px, py + 8, px + 105, bot, INK, 2.5)
        f.path(f"M{n(px - 125)},{n(bot)} Q{n(px)},{n(bot + 70)} {n(px + 125)},{n(bot)} Z", ALUMINIUM, INK, 3)
        f.circle(px, py + 8, 7, INK)
    # left pan: four nucleons apart
    lb = ly + 175
    for k, (ox, pr) in enumerate(((-78, True), (-26, False), (26, True), (78, False))):
        nucleon(f, lx + ox, lb - 10 + (6 if abs(ox) < 40 else 0) - 14, 24, pr)
    # right pan: the helium nucleus, glowing, two photons out
    rb = ry + 175
    hx, hy = rx, rb - 40
    f.circle(hx, hy, 66, HEAT_LIGHT)
    f.circle(hx, hy, 52, PAPER)
    helium(f, hx, hy, 22)
    photon(f, hx + 58, hy - 52, hx + 150, hy - 150, HEAT, 18, 7, 4, 20)
    photon(f, hx - 58, hy - 52, hx - 130, hy - 160, HEAT, 18, 7, 4, 20)
    return f.svg()


FIGURES = {"hero": hero, "massat": massat, "energia": energia, "kayra": kayra, "reaktio": reaktio, "kayra-points": kayra_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "massat": "reveals: 2 m_H + 2 m_n = 4,032980 u against m(He-4) = 4,002603 u, the mass defect 0,030377 u",
    "energia": "reveals: separating a nucleus needs E_B, forming it releases E_B (energy levels)",
    "kayra": "reveals: the E_B/A curve with He-4, Fe-56, U-238 named and the directions of fusion and fission",
    "reaktio": "reveals: U-238 alpha decay, mass before and after, 0,004583 u and Q = 4,27 MeV",
    "kayra-points": "safe: E_B/A of 32 nuclides against A, no names and no fusion or fission arrows",
}
