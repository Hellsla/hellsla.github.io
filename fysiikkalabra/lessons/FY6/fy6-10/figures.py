"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-10` writes them into lesson.md.
Colours, one meaning each: a positive charge is a light red disc with an ink plus, a negative charge (an electron) a
blue disc with a white minus as in the other FY6 chapters (#1971c2), forces red filled arrows (#c92a2a, as in FY4),
electric field lines green (#2b8a3e) with filled heads. The force graphs are to scale and their numbers are those of
lesson-answers.py; the other figures are schematic. Every label is LaTeX."""
import math
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GOOD, PAPER, n
import herolib as H

FORCE = HOT          # forces red (FY4 convention)
K, nC, cm = 8.99e9, 1e-9, 1e-2


def F_mN(q1, q2, r):
    """Coulomb force in mN; q1, q2 in nC, r in cm (lesson-answers.py)."""
    return K * abs(q1 * q2) * nC ** 2 / (r * cm) ** 2 * 1000


# --- pieces ---------------------------------------------------------------------------------------------------
def plus(f, x, y, r=9):
    f.circle(x, y, r, HOT_LIGHT, INK, 1.5)
    f.line(x - r * 0.55, y, x + r * 0.55, y, INK, 2); f.line(x, y - r * 0.55, x, y + r * 0.55, INK, 2)


def minus(f, x, y, r=9):
    f.circle(x, y, r, COLD, WHITE, 1.5)
    f.line(x - r * 0.55, y, x + r * 0.55, y, WHITE, 2)


def sphere(f, gid, cx, cy, R, tint=ALUMINIUM):
    """A small metal sphere: a radial gradient from a white highlight to its tint, an ink outline."""
    f.defs_add(f'<radialGradient id="{gid}" cx="0.36" cy="0.32" r="0.75"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{tint}"/></radialGradient>')
    f.circle(cx, cy, R, f"url(#{gid})", INK, 2.5)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- Ydinajatus: rubbing moves electrons, the total charge stays zero ------------------------------------------
def balloon(f, gid, cx, cy, rx=56, ry=70):
    f.defs_add(f'<radialGradient id="{gid}" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{RULE_LIGHT}"/></radialGradient>')
    f.path(f"M{n(cx - 7)},{n(cy + ry + 10)} L{n(cx)},{n(cy + ry - 2)} L{n(cx + 7)},{n(cy + ry + 10)} Z", RULE, INK, 2)
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{rx}" ry="{ry}" fill="url(#{gid})" stroke="{INK}" stroke-width="2.5"/>')


def wool(f, gid, x, y, w, h):
    f.rect(x, y, w, h, H.grad(f, gid, SAND_LIGHT, SAND_DARK), INK, 2.5, rx=14)
    for k in range(5):                                    # the knit: rows of small arcs
        yy = y + 18 + k * (h - 30) / 4
        d = " ".join(f"M{n(x + 10 + 18 * j)},{n(yy)} q9,8 18,0" for j in range(int((w - 20) // 18)))
        f.path(d, stroke=GRAIN, w=1.5, extra='stroke-linecap="round"')


def charges(f, pts, kinds):
    for (x, y), k in zip(pts, kinds):
        (plus if k == "+" else minus)(f, x, y)


def hankaus():
    f = new("fy610-hankaus", 360, "Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla ennen hankausta: ilmapallossa "
            "ja villakankaassa on kummassakin neljä positiivista ja neljä negatiivista varausta, joten kumpikin on "
            "neutraali, Q = 0. Oikealla hankauksen jälkeen: kolme elektronia on siirtynyt villasta ilmapalloon, mitä "
            "näyttää sininen nuoli villasta palloon. Ilmapallossa on neljä positiivista ja seitsemän negatiivista "
            "varausta, Q = −3e, ja villassa neljä positiivista ja yksi negatiivinen, Q = +3e. Varausten summa on "
            "edelleen nolla.")
    f.line(300, 14, 300, 346, RULE, 1.5, "6 6")
    for side, x0 in (("ennen", 0), ("jalkeen", 300)):
        after = side == "jalkeen"
        f.tex(x0 + 150, 26, r"\text{hankauksen jälkeen}" if after else r"\text{ennen hankausta}", "middle")
        bx, by = x0 + 84, 150
        balloon(f, f"fy610-ilma-{side}", bx, by)
        wool(f, f"fy610-villa-{side}", x0 + 168, 92, 116, 120)
        bpts = [(bx - 22, by - 42), (bx + 20, by - 42), (bx - 34, by - 12), (bx, by - 14), (bx + 32, by - 12),
                (bx - 30, by + 18), (bx + 2, by + 16), (bx + 30, by + 18), (bx - 16, by + 46), (bx + 16, by + 46),
                (bx, by - 60)]
        wpts = [(x0 + 190, 116), (x0 + 226, 116), (x0 + 262, 116), (x0 + 190, 152), (x0 + 226, 152), (x0 + 262, 152),
                (x0 + 208, 188), (x0 + 244, 188)]
        if after:
            charges(f, bpts[:11], "+-+-+--+---")
            charges(f, wpts[:5], "+-+++")
            f.arrow(x0 + 240, 300, x0 + 96, 300, COLD, 3.5, 16)
            f.tex(x0 + 150, 330, r"\text{elektroneja}", "middle", COLD)
            f.tex(bx, 258, r"Q = -3e", "middle")
            f.tex(x0 + 226, 258, r"Q = +3e", "middle")
        else:
            charges(f, bpts[:8], "+-+-+-+-")
            charges(f, wpts, "+-+-+-+-")
            f.tex(bx, 258, r"Q = 0", "middle")
            f.tex(x0 + 226, 258, r"Q = 0", "middle")
        if not after:
            f.tex(bx, 296, r"\text{ilmapallo}", "middle", MUTED)
            f.tex(x0 + 226, 296, r"\text{villa}", "middle", MUTED)
    return f.svg()


# --- Ydinajatus: influence in a conductor and polarisation in an insulator --------------------------------------
def influenssi():
    f = new("fy610-influenssi", 360, "Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla johde: negatiivisesti "
            "varattu muovisauva on eristetangon päässä olevan metallipallon vasemmalla puolella. Pallon vapaat elektronit "
            "ovat siirtyneet kauemmas sauvasta, joten pallon sauvan puoleisella pinnalla on kolme positiivista ja "
            "vastakkaisella pinnalla kolme negatiivista varausta; pallo on kokonaisuutena neutraali. Punainen voimanuoli "
            "osoittaa pallosta sauvaa kohti. Oikealla eriste: negatiivisesti varattu ilmapallo seinän vieressä. Seinän "
            "molekyylien varaukset ovat siirtyneet hieman niin, että jokaisen molekyylin positiivinen pää on palloa "
            "kohti. Punainen voimanuoli osoittaa ilmapallosta seinää kohti.")
    f.line(300, 14, 300, 346, RULE, 1.5, "6 6")
    f.tex(150, 26, r"\text{johde}", "middle")
    f.tex(450, 26, r"\text{eriste}", "middle")
    # the conductor: a charged plastic rod and a metal sphere on an insulating stand
    f.rect(14, 138, 96, 26, H.grad(f, "fy610-sauva", RULE_LIGHT, RULE), INK, 2.5, rx=13)
    for x in (36, 62, 88): minus(f, x, 151, 8)
    f.tex(12, 194, r"\text{muovisauva}", "start", MUTED)
    sx = 214
    f.rect(sx - 7, 204, 14, 82, GLASS, INK, 2)
    f.rect(sx - 40, 284, 80, 14, IRON, INK, 2, rx=3)
    sphere(f, "fy610-metalli", sx, 151, 54)
    for (x, y) in ((sx - 42, 122), (sx - 48, 151), (sx - 42, 180)): plus(f, x, y, 8)
    for (x, y) in ((sx + 42, 122), (sx + 48, 151), (sx + 42, 180)): minus(f, x, y, 8)
    f.arrow(sx + 14, 76, sx - 60, 76, FORCE, 3.5, 16)
    f.tex(sx - 72, 76, r"\overline{F}", "end", FORCE)
    f.tex(sx, 326, r"\text{metallipallo}", "middle", MUTED)
    # the insulator: a charged balloon beside a wall whose molecules are polarised
    f.rect(470, 56, 116, 248, H.grad(f, "fy610-seina", SAND_LIGHT, PAPER, horizontal=True), RULE, 2)
    f.line(470, 56, 470, 304, INK, 2.5)
    for i in range(3):
        for j in range(6):
            mx, my = 502 + i * 34, 82 + j * 40
            f.add(f'<ellipse cx="{mx}" cy="{my}" rx="15" ry="10" fill="{WHITE}" stroke="{MUTED}" stroke-width="1.5"/>')
            f.line(mx - 12, my, mx - 4, my, HOT, 2.5); f.line(mx - 8, my - 4, mx - 8, my + 4, HOT, 2.5)
            f.line(mx + 4, my, mx + 12, my, COLD, 2.5)
    balloon(f, "fy610-ilma-inf", 394, 176, 50, 62)
    for (x, y) in ((378, 150), (410, 150), (372, 180), (404, 182), (390, 210)): minus(f, x, y, 8)
    f.arrow(376, 82, 446, 82, FORCE, 3.5, 16)
    f.tex(366, 82, r"\overline{F}", "end", FORCE)
    f.tex(394, 290, r"\text{ilmapallo}", "middle", MUTED)
    f.tex(528, 326, r"\text{seinä}", "middle", MUTED)
    return f.svg()


# --- Ydinajatus: the field around a point charge, qualitatively --------------------------------------------------
def head_on(f, x, y, ang, s=11, col=INK):
    ux, uy = math.cos(ang), math.sin(ang)
    px, py = -uy, ux
    pts = [(x + ux * s, y + uy * s), (x - ux * s + px * s * 0.7, y - uy * s + py * s * 0.7), (x - ux * s - px * s * 0.7, y - uy * s - py * s * 0.7)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", col)


def kentta():
    f = new("fy610-kentta", 340, "Kaavakuva, ei mittakaavassa, kaksi paneelia. Vasemmalla positiivinen pistevaraus, "
            "jonka ympärillä on kahdeksan säteittäistä kenttäviivaa, nuolet varauksesta poispäin. Oikealla negatiivinen "
            "pistevaraus, jonka kenttäviivojen nuolet osoittavat varausta kohti. Kummankin oikealla puolella on pieni "
            "positiivinen koevaraus, ja punainen voimanuoli osoittaa kenttäviivan suuntaan: positiivisesta varauksesta "
            "poispäin ja negatiivista varausta kohti. Kenttäviivat ovat vihreitä, voimanuoli punainen. Viivat ovat lähellä varausta tiheässä ja harvenevat kauempana.")
    f.line(300, 14, 300, 326, RULE, 1.5, "6 6")
    for x0, sign in ((0, 1), (300, -1)):
        cx, cy = x0 + 120, 150
        for k in range(8):
            a = k * math.pi / 4
            r0, r1 = 30, 112
            f.line(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + r1 * math.cos(a), cy + r1 * math.sin(a), GOOD, 2)
            rm = 66
            head_on(f, cx + rm * math.cos(a), cy + rm * math.sin(a), a if sign > 0 else a + math.pi, col=GOOD)
        sphere(f, f"fy610-q-{'p' if sign > 0 else 'n'}", cx, cy, 22, HOT_LIGHT if sign > 0 else COLD)
        f.line(cx - 10, cy, cx + 10, cy, INK if sign > 0 else WHITE, 3)
        if sign > 0: f.line(cx, cy - 10, cx, cy + 10, INK, 3)
        # a small positive test charge on the horizontal line, the force on it along the line
        tx = cx + 104
        plus(f, tx, cy, 8)
        if sign > 0:
            f.arrow(tx + 10, cy - 24, tx + 52, cy - 24, FORCE, 3.5, 14)
        else:
            f.arrow(tx + 30, cy - 24, tx - 12, cy - 24, FORCE, 3.5, 14)
        f.tex(tx + 12, cy - 54, r"\overline{F}", "middle", FORCE)
        f.tex(cx, 296, r"+Q" if sign > 0 else r"-Q", "middle")
    f.tex(12, 26, r"\text{kenttäviiva}", "start", MUTED)
    f.line(84, 40, 104, 70, MUTED, 1.5); f.circle(104, 70, 3.5, MUTED)
    return f.svg()


# --- Kaava: the forces of Coulomb's law -------------------------------------------------------------------------
def coulomb():
    f = new("fy610-coulomb", 364, "Kaavakuva, ei mittakaavassa. Ylhäällä samanmerkkiset varaukset q1 ja q2, molemmat "
            "positiivisia: varaukseen q1 vaikuttava voima F21 osoittaa vasemmalle poispäin q2:sta ja varaukseen q2 "
            "vaikuttava voima F12 oikealle poispäin q1:stä, joten varaukset hylkivät toisiaan. Alhaalla erimerkkiset "
            "varaukset, q1 positiivinen ja q2 negatiivinen: voimat osoittavat toisiaan kohti, joten varaukset vetävät "
            "toisiaan puoleensa. Kaikki neljä voimanuolta ovat yhtä pitkiä. Alimpana varausten keskipisteiden välinen "
            "etäisyys r.")
    f.tex(300, 22, r"\text{samanmerkkiset varaukset hylkivät}", "middle")
    f.tex(300, 192, r"\text{erimerkkiset varaukset vetävät}", "middle")
    f.line(12, 168, 588, 168, RULE, 1.5, "6 6")
    x1, x2, L = 200, 400, 72
    for y, unlike in ((96, False), (266, True)):
        sphere(f, f"fy610-c1-{int(unlike)}", x1, y, 24, HOT_LIGHT)
        sphere(f, f"fy610-c2-{int(unlike)}", x2, y, 24, COLD if unlike else HOT_LIGHT)
        f.line(x1 - 10, y, x1 + 10, y, INK, 3); f.line(x1, y - 10, x1, y + 10, INK, 3)
        f.line(x2 - 10, y, x2 + 10, y, WHITE if unlike else INK, 3)
        if not unlike: f.line(x2, y - 10, x2, y + 10, INK, 3)
        if unlike:
            f.arrow(x1 + 26, y, x1 + 26 + L, y, FORCE, 4, 18); f.arrow(x2 - 26, y, x2 - 26 - L, y, FORCE, 4, 18)
            f.tex(x1 + 54, y - 38, r"\overline{F}_{21}", "middle", FORCE); f.tex(x2 - 54, y - 38, r"\overline{F}_{12}", "middle", FORCE)
        else:
            f.arrow(x1 - 26, y, x1 - 26 - L, y, FORCE, 4, 18); f.arrow(x2 + 26, y, x2 + 26 + L, y, FORCE, 4, 18)
            f.tex(x1 - 62, y - 38, r"\overline{F}_{21}", "middle", FORCE); f.tex(x2 + 62, y - 38, r"\overline{F}_{12}", "middle", FORCE)
        f.tex(x1, y + 44, r"q_1", "middle"); f.tex(x2, y + 44, r"q_2", "middle")
    # the distance between the centres
    y = 342
    f.line(x1, y - 9, x1, y + 9, INK, 2); f.line(x2, y - 9, x2, y + 9, INK, 2)
    f.line(x1, y, 284, y, INK, 2); f.line(316, y, x2, y, INK, 2)
    f.tex(300, y, r"r", "middle", w=26)
    return f.svg()


# --- Kaava: F against r, the inverse square ------------------------------------------------------------------
def kuvaaja():
    f = new("fy610-kuvaaja", 360, "Kuvaaja mittakaavassa: kahden pistevarauksen, q1 = q2 = 20 nC, välinen voima F "
            "millinewtoneina etäisyyden r funktiona senttimetreinä. Käyrä laskee jyrkästi. Etäisyydellä 3 cm voima on "
            "4,0 mN, kaksinkertaisella etäisyydellä 6 cm neljäsosa eli 1,0 mN, kolminkertaisella 9 cm yhdeksäsosa eli "
            "0,44 mN ja nelinkertaisella 12 cm kuudestoistaosa eli 0,25 mN. Pisteiden viereen on merkitty F, F/4, F/9 "
            "ja F/16.")
    ax = Axes(f, (84, 310), (470, 72), x=(0, 14), y=(0, 4.5), xticks=[3, 6, 9, 12], yticks=[1, 2, 3, 4],
              xlabel=r"r\ (\text{cm})", ylabel=r"F\ (\text{mN})")
    ax.curve(lambda r: F_mN(20, 20, r), 2.9, 13.6, COLD, 3)
    for r, lab in ((3, r"F"), (6, r"\tfrac{F}{4}"), (9, r"\tfrac{F}{9}"), (12, r"\tfrac{F}{16}")):
        v = F_mN(20, 20, r)
        ax.point(r, v, INK)
        f.tex(ax.X(r) + 14, ax.Y(v) - 30, lab, "start", w=44)
    f.tex(ax.X(3) + 64, ax.Y(4.0) + 4, r"4{,}0\,\text{mN}", "start", MUTED, w=110)
    ax.guide(3, F_mN(20, 20, 3))
    return f.svg()


# --- Tarkista osaamisesi: a force graph without the charges ---------------------------------------------------
def check_graph():
    f = new("fy610-check", 390, "Kuvaaja mittakaavassa: kahden samanlaisen, yhtä suuresti varatun pienen pallon välinen "
            "voima F millinewtoneina pallojen keskipisteiden etäisyyden r funktiona senttimetreinä, ruudukon välit 1 cm ja "
            "1 mN. Mallin laskemat pisteet ovat (3,0 cm; 8,99 mN), (4,0 cm; 5,06 mN), (5,0 cm; 3,24 mN), (6,0 cm; "
            "2,25 mN) ja (9,0 cm; 1,00 mN), ja niiden kautta kulkee laskeva käyrä.")
    ax = Axes(f, (84, 330), (480, 72), x=(0, 10), y=(0, 10), xticks=list(range(1, 11)), yticks=list(range(1, 11)),
              xlabel=r"r\ (\text{cm})", ylabel=r"F\ (\text{mN})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.curve(lambda r: F_mN(30, 30, r), 2.85, 9.8, COLD, 3)
    for r in (3, 4, 5, 6, 9):
        ax.point(r, F_mN(30, 30, r), INK)
    return f.svg()


# --- the opening illustration -------------------------------------------------------------------------------------
def hero():
    f = H.hero("fy610-hero", "Kuvitus: huoneen vaalea seinä, jossa sininen ilmapallo pysyy kiinni seinässä ilman "
               "teippiä, ja sen naru roikkuu alas. Oikealla tuolin selkänojalla roikkuu villapaita. Vasemmalla pöydällä on "
               "muovikampa, jota kohti pienet paperisilpun palat nousevat pöydältä.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 430, H.grad(f, "fy610h-wall", GLASS, PAPER))
    f.rect(0, 420, 1200, 14, RULE)                                       # skirting board
    f.rect(0, 434, 1200, 166, H.grad(f, "fy610h-floor", SAND_LIGHT, SAND))
    for k in range(5):
        f.line(0, 470 + 30 * k, 1200, 470 + 30 * k, SAND_DARK, 2)
    # the balloon on the wall, with a faint shadow and its string
    f.add(f'<ellipse cx="612" cy="226" rx="98" ry="118" fill="{RULE}" fill-opacity="0.35"/>')
    f.defs_add(f'<radialGradient id="fy610h-balloon" cx="0.35" cy="0.3" r="0.85"><stop offset="0" stop-color="{COLD_LIGHT}"/>'
               f'<stop offset="1" stop-color="{COLD}"/></radialGradient>')
    f.path("M600,346 C590,380 616,410 600,446 C586,480 612,510 598,540", stroke=INK, w=2.5, extra='stroke-linecap="round"')
    f.path("M590,344 L600,328 L610,344 Z", COLD, INK, 2.5)
    f.add('<ellipse cx="600" cy="210" rx="98" ry="120" fill="url(#fy610h-balloon)" stroke="#1f2933" stroke-width="3"/>')
    f.path("M548,140 Q560,112 590,104", stroke=WHITE, w=8, extra='stroke-linecap="round" stroke-opacity="0.7"')
    # the chair with the wool sweater over its back
    f.rect(880, 210, 18, 330, H.grad(f, "fy610h-leg1", SAND, GRAIN, horizontal=True), INK, 3, rx=6)
    f.rect(1060, 210, 18, 330, H.grad(f, "fy610h-leg2", SAND, GRAIN, horizontal=True), INK, 3, rx=6)
    f.rect(866, 196, 226, 30, SAND, INK, 3, rx=10)
    f.rect(866, 392, 226, 28, SAND, INK, 3, rx=8)
    f.path("M880,206 L1080,206 L1102,330 Q1060,346 1040,322 L1020,268 L940,268 L920,322 Q898,346 858,330 Z",
           H.grad(f, "fy610h-wool", HOT_LIGHT, HOT), INK, 3)
    for k in range(4):
        y = 226 + 14 * k
        f.path(" ".join(f"M{900 + 22 * j},{y} q11,9 22,0" for j in range(8)), stroke=WHITE, w=2,
               extra='stroke-linecap="round" stroke-opacity="0.55"')
    # the table with a comb lifting paper bits
    f.rect(70, 330, 330, 22, H.grad(f, "fy610h-top", SAND, GRAIN), INK, 3, rx=6)
    f.rect(96, 352, 18, 190, GRAIN, INK, 3, rx=5); f.rect(356, 352, 18, 190, GRAIN, INK, 3, rx=5)
    f.rect(190, 220, 150, 22, IRON, INK, 3, rx=6)                        # the comb, held above the table
    for k in range(12):
        f.rect(196 + 12 * k, 242, 6, 22, IRON, INK, 1.5, rx=2)
    bits = [(206, 300, 10), (236, 286, -18), (262, 306, 24), (292, 290, 8), (318, 312, -30), (180, 318, 14),
            (246, 318, -6), (300, 320, 40), (330, 324, -12)]
    for x, y, rot in bits:
        f.add(f'<rect x="{x - 9}" y="{y - 5}" width="18" height="10" rx="2" fill="{WHITE}" stroke="{INK}" stroke-width="2" '
              f'transform="rotate({rot} {x} {y})"/>')
    return f.svg()


FIGURES = {"hero": hero, "hankaus": hankaus, "influenssi": influenssi, "kentta": kentta, "coulomb": coulomb,
           "kuvaaja": kuvaaja, "check-graph": check_graph}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "hankaus": "reveals: rubbing moves electrons from the wool to the balloon, Q = -3e and +3e, the total stays zero",
    "influenssi": "reveals: induced charges in a metal sphere and polarised wall molecules make a neutral body attracted",
    "kentta": "reveals: the field lines of a positive and a negative point charge and the force on a positive test charge",
    "coulomb": "reveals: equal and opposite forces F12 and F21, repulsion for like and attraction for unlike charges",
    "kuvaaja": "reveals: F(r) for 20 nC and 20 nC, 4,0 mN at 3 cm, a quarter at twice the distance",
    "check-graph": "safe: F(r) points of two equal charges (30 nC each, not written): 8,99 mN at 3,0 cm ... 1,00 mN at 9,0 cm",
}
