"""Figures of fy4-13 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy4-13` writes them into lesson.md.
Every force diagram is an FBD: one body alone as a plain rectangle, its arrows drawn to scale and its physics checked as it
is drawn. A situation is a separate pictorial situation picture (tilannekuva); no point-particle diagrams.
Two bodies joined by a light string over a light, frictionless pulley: each body has its own diagram, the string pulls both
with a force of the same size T (a different arrow on each body)."""
import math
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, ICE, GLASS, COLD, COLD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, COPPER, HOT, GOOD, n
from fbd import FBD, ground
import herolib as H
from herolib import grad, rnd

g = 9.81
CART, CART_EDGE = COLD_LIGHT, COLD
BLOCK = IRON


def hero():
    """The chapter's opening illustration: a cart on a laboratory table is pulled by a string over a pulley that carries a hanging weight."""
    f = H.hero("fy413-hero", "Kuvitus: fysiikan luokan pöytä. Pöydällä on kärry, jonka päällä on kaksi metallipunnusta. Kärryyn sidottu lanka kulkee pöydän "
               "reunalla olevan väkipyörän yli, ja langan toisessa päässä roikkuu yksi metallipunnus. Pöydällä on mitta-asteikko ja sekuntikello, "
               "ja oppilas seisoo pöydän vieressä.")
    f.rect(0, 0, 1200, 470, grad(f, "fy413h-wall", WHITE, GLASS, y1=0, y2=470))
    H.window(f, 880, 70, 240, 230, "fy413h-win")
    f.rect(70, 110, 300, 14, SAND_DARK, INK, 3, 3)                          # a shelf with a few jars
    for k, c in enumerate((ICE, COLD_LIGHT, "#b2f2bb")):
        f.rect(100 + k * 90, 64, 60, 46, c, INK, 3, 8)
    f.rect(0, 470, 1200, 130, grad(f, "fy413h-floor", SAND_LIGHT, SAND, y1=470, y2=600))
    for k in range(1, 7): f.line(0, 470 + k * 22, 1200, 470 + k * 22, SAND, 2)
    f.line(0, 470, 1200, 470, INK, 3)
    # the table: top, front board, legs
    for lx in (110, 760):
        f.rect(lx, 354, 26, 170, grad(f, f"fy413h-leg{lx}", SAND_DARK, SAND, horizontal=True), INK, 3)
    f.rect(70, 330, 770, 24, grad(f, "fy413h-top", SAND_DARK, SAND), INK, 3, 3)
    for k in range(1, 4): f.path(f"M{90 + k * 40},{340 + 4 * (k % 2)} q200,-4 400,0", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.5"')
    # a measuring scale and a stopwatch on the table
    f.rect(120, 336, 560, 12, WHITE, INK, 2)
    for k in range(0, 57):
        f.line(124 + k * 9.8, 336, 124 + k * 9.8, 336 + (10 if k % 5 == 0 else 6), INK, 1.5)
    H.stopwatch(f, 150, 292, 30, 0.18)
    # the cart with two metal weights
    cx0, cx1 = 250, 450
    f.rect(cx0, 262, cx1 - cx0, 34, grad(f, "fy413h-cart", COLD_LIGHT, COLD), INK, 3, 5)
    f.rect(cx0 + 10, 270, cx1 - cx0 - 20, 6, "#ffffff", None, 1, 3, extra='fill-opacity="0.5"')
    for wx in (cx0 + 40, cx0 + 112):
        f.rect(wx, 218, 56, 44, H.steel(f, f"fy413h-m{wx}"), INK, 3, 6)
        f.rect(wx + 8, 226, 40, 6, "#ffffff", None, 1, 3, extra='fill-opacity="0.5"')
    for wx in (cx0 + 36, cx1 - 36):
        f.circle(wx, 312, 22, INK); f.circle(wx, 312, 14, ALUMINIUM, METAL_EDGE, 2); f.circle(wx, 312, 4, INK)
    f.rect(cx1 - 2, 270, 14, 6, IRON, INK, 2, 2)                            # the hook where the string is tied
    # the pulley on a bent rod clamped to the table edge
    px, py, pr = 872, 290, 30
    f.path(f"M812,330 V318 Q812,{py} {px},{py}", stroke=IRON, w=7, extra='stroke-linecap="round"')
    f.rect(796, 316, 34, 18, IRON, INK, 3, 3)
    f.circle(px, py, pr, ALUMINIUM, INK, 3); f.circle(px, py, pr - 9, "#ffffff", METAL_EDGE, 2)
    for k in range(6):
        a = k * math.pi / 3
        f.line(px + math.cos(a) * 6, py + math.sin(a) * 6, px + math.cos(a) * (pr - 9), py + math.sin(a) * (pr - 9), METAL_EDGE, 2)
    f.circle(px, py, 6, IRON, INK, 2)
    # the string: horizontal from the cart's hook, over the pulley, down to the hanging weight
    ytop = py - pr
    f.path(f"M{cx1 + 12},273 H{px} A{pr},{pr} 0 0 1 {px + pr},{py} V396", stroke=COPPER, w=4, extra='stroke-linecap="round"')
    f.path(f"M{px + pr - 14},396 h28 v14 h-28 Z", IRON, INK, 2)               # the hanger
    f.rect(px + pr - 28, 410, 56, 44, H.steel(f, "fy413h-hang"), INK, 3, 6)
    f.rect(px + pr - 20, 418, 40, 6, "#ffffff", None, 1, 3, extra='fill-opacity="0.5"')
    f.add(f'<ellipse cx="{px + pr}" cy="{472}" rx="46" ry="8" fill="{INK}" fill-opacity="0.12"/>')
    H.person(f, 1010, 560, COLD, INK, 0.78, "down")
    return f.svg()


# ---------------------------------------------------------------- pictorial parts of the situation pictures
def pulley(f, x, y, r=12):
    f.circle(x, y, r, ALUMINIUM, INK, 2.5); f.circle(x, y, r - 5, WHITE, METAL_EDGE, 1.5); f.circle(x, y, 2.5, INK)


def cart(f, x, y, w=60, extra_block=True):
    """A small pictorial cart on wheels; (x, y) is the left end of its bottom edge (the table top is y). Returns the right end of its body."""
    f.rect(x, y - 30, w, 18, CART, INK, 2.5, 3)
    f.circle(x + 13, y - 7, 7, INK); f.circle(x + w - 13, y - 7, 7, INK)
    f.circle(x + 13, y - 7, 3, ALUMINIUM); f.circle(x + w - 13, y - 7, 3, ALUMINIUM)
    if extra_block: f.rect(x + 12, y - 44, w - 24, 14, BLOCK, INK, 2.5, 2)
    return x + w


def block(f, x, y, w, h, fill=BLOCK):
    f.rect(x, y, w, h, fill, INK, 2.5, 3)


def table_scene(f, ox=0, oy=0, with_motion=True):
    """Situation picture: a cart on a table, a string over a pulley at the table edge, a weight hanging beside the table (about 290 × 260)."""
    top = 170 + oy
    f.rect(ox + 20, top, 214, 12, SAND_DARK, GRAIN, 2.5, 2)
    f.rect(ox + 28, top + 12, 12, 108, SAND_DARK, GRAIN, 2.5)
    f.rect(ox + 190, top + 12, 12, 108, SAND_DARK, GRAIN, 2.5)
    f.line(ox + 10, top + 120, ox + 290, top + 120, INK, 2.5)
    pulley(f, ox + 244, top - 12)
    f.rect(ox + 226, top - 4, 12, 10, METAL_EDGE, INK, 1.5)
    cart_right = cart(f, ox + 70, top)
    ys = top - 20
    f.path(f"M{ox + cart_right},{ys} H{ox + 244} A12,12 0 0 1 {ox + 256},{top - 12} V{top + 60}", stroke=COPPER, w=2.5)
    block(f, ox + 244, top + 60, 24, 32)
    f.line(ox + 256, top + 60, ox + 256, top + 56, COPPER, 2.5)
    return top


def atwood_scene(f, ox=0, oy=0, m1h=36, m2h=48):
    """Situation picture: a string over a pulley hung from the ceiling, a lighter body (left) and a heavier one (right)."""
    ground(f, ox + 70, ox + 190, oy + 26, below=False)
    f.line(ox + 130, oy + 26, ox + 130, oy + 62, IRON, 4)
    pulley(f, ox + 130, oy + 74, 22)
    f.line(ox + 108, oy + 74, ox + 108, oy + 176, COPPER, 2.5); f.line(ox + 152, oy + 74, ox + 152, oy + 212, COPPER, 2.5)
    block(f, ox + 94, oy + 176, 28, m1h); block(f, ox + 134, oy + 212, 36, m2h)


# ---------------------------------------------------------------- theory figures
def _karry(fid, label, m1, m2, S):
    """The cart on the table with the hanging weight: the situation picture (cart with v and a) and the force diagram of each body."""
    a = m2 * g / (m1 + m2); T = m1 * a
    f = Fig(fid, 340, label)
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    table_scene(f, 0, 6)
    FBD(f, 1).motion(r"\overline{v}", (1, 0), (82, 124), 60)
    FBD(f, 1).motion(r"\overline{a}", (1, 0), (82, 84), 40)
    f.tex(52, 150, r"m_1", "middle"); f.tex(214, 240, r"m_2", "middle")
    f.line(300, 12, 300, 332, RULE, 1.5, "6 6")
    f.line(310, 182, 590, 182, RULE, 1.5, "6 6")
    f.tex(312, 22, r"\text{voimakuvio: kärry}", "start", MUTED)
    f.tex(312, 202, r"\text{voimakuvio: punnus}", "start", MUTED)
    cx, cy = 440, 108
    d = FBD(f, S, body=(cx, cy, 80, 40), m=m1, a=(a, 0))
    d.force("G_1", (0, -m1 * g), (cx, cy), "gravity", lab=(22, -4))
    d.force("N", (0, m1 * g), (cx - 22, cy + 20), "normal", surface=0, lab=(-22, 2))
    d.force("T_1", (T, 0), (cx + 40, cy - 6), "tension", rope=(1, 0), lab=(22, 2))
    d.draw()
    cx, cy = 440, 276
    d = FBD(f, S, body=(cx, cy, 56, 44), m=m2, a=(0, -a))
    d.force("G_2", (0, -m2 * g), (cx, cy), "gravity", lab=(22, 2))
    d.force("T_2", (0, T), (cx, cy - 22), "tension", rope=(0, 1), lab=(22, 2))
    d.draw()
    return f.svg()


def tilanne():
    """Ydinajatus: the cart on the table with the hanging weight, and the force diagram of each body (m1 = 1,0 kg, m2 = 0,50 kg)."""
    return _karry("fy413-tilanne", "Kaksi kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: pöydällä on kärry, ja siihen sidottu lanka kulkee pöydän "
                  "reunan väkipyörän yli riippuvaan punnukseen. Kärryn yllä ovat ohuet nuolet: sininen nopeus oikealle ja lyhyempi oranssi kiihtyvyys oikealle. "
                  "Oikealla ylhäällä kärryn voimakuvio, kärry suorakulmiona: paino G1 keskipisteestä alas, pöydän tukivoima N alapinnasta ylös ja yhtä pitkä kuin "
                  "paino sekä langan jännitysvoima T1 oikealta reunalta oikealle. Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 keskipisteestä alas ja "
                  "langan jännitysvoima T2 yläpinnasta ylös. Nuoli T2 on lyhyempi kuin G2, ja nuolet T1 ja T2 ovat yhtä pitkät.", 1.0, 0.50, 6.0)


def esimerkki():
    """Esimerkki: the cart of 1,5 kg and the weight of 0,60 kg."""
    return _karry("fy413-esimerkki", "Esimerkin kärry ja riippuva punnus. Vasemmalla tilannekuva: pöydällä oleva kärry, lanka väkipyörän yli riippuvaan punnukseen, ja kärryn yllä "
                  "sininen nopeus ja oranssi kiihtyvyys oikealle. Oikealla ylhäällä kärryn voimakuvio: paino G1 alas, yhtä pitkä tukivoima N ylös ja jännitysvoima T1 oikealle. "
                  "Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 alas ja lyhyempi jännitysvoima T2 ylös. Nuolet T1 ja T2 ovat yhtä pitkät.", 1.5, 0.60, 4.5)


def _atwood(fid, label, m1, m2, S):
    """Two bodies over a pulley (m1 < m2): the situation picture and the force diagram of each body."""
    a = (m2 - m1) * g / (m1 + m2); T = 2 * m1 * m2 * g / (m1 + m2)
    f = Fig(fid, 380, label)
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    atwood_scene(f, 0, 30, m1h=26 + 18 * m1, m2h=26 + 18 * m2)
    FBD(f, 1).motion(r"\overline{a}", (0, 1), (60, 236), 44, lab=(-22, -4))
    FBD(f, 1).motion(r"\overline{a}", (0, -1), (212, 252), 44, lab=(22, 4))
    f.tex(108, 270, r"m_1", "middle"); f.tex(152, 316, r"m_2", "middle")
    f.line(300, 12, 300, 368, RULE, 1.5, "6 6")
    f.line(310, 190, 590, 190, RULE, 1.5, "6 6")
    f.tex(312, 22, r"\text{voimakuvio: kevyempi}", "start", MUTED)
    f.tex(312, 206, r"\text{voimakuvio: raskaampi}", "start", MUTED)
    cx, cy = 440, 128
    d = FBD(f, S, body=(cx, cy, 56, 36), m=m1, a=(0, a))
    d.force("G_1", (0, -m1 * g), (cx, cy), "gravity", lab=(22, 2))
    d.force("T_1", (0, T), (cx, cy - 18), "tension", rope=(0, 1), lab=(22, 2))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (540, 150), 44, lab=(22, 0))
    cx, cy = 440, 302
    d = FBD(f, S, body=(cx, cy, 64, 48), m=m2, a=(0, -a))
    d.force("G_2", (0, -m2 * g), (cx, cy), "gravity", lab=(22, 2))
    d.force("T_2", (0, T), (cx, cy - 24), "tension", rope=(0, 1), lab=(22, 2))
    d.draw()
    d.motion(r"\overline{a}", (0, -1), (540, 280), 44, lab=(22, 0))
    return f.svg()


def atwood():
    """Kaava: two hanging bodies of 0,30 kg and 0,60 kg; the lighter one rises, the heavier one falls with the same acceleration."""
    return _atwood("fy413-atwood", "Kaksi riippuvaa kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: katosta riippuvan väkipyörän yli kulkevan langan vasemmassa "
                   "päässä on kevyempi kappale ja oikeassa raskaampi. Kevyemmän vieressä on oranssi nuoli ylös ja raskaamman vieressä yhtä pitkä oranssi nuoli alas: "
                   "kiihtyvyyden suuruus on sama. Oikealla ylhäällä kevyemmän kappaleen voimakuvio, kappale suorakulmiona: langan jännitysvoima T1 yläpinnasta ylös ja "
                   "paino G1 keskipisteestä alas, ja T1 on pidempi kuin G1. Oikealla alhaalla raskaamman kappaleen voimakuvio: T2 yläpinnasta ylös ja G2 keskipisteestä alas, ja "
                   "G2 on pidempi kuin T2. Nuolet T1 ja T2 ovat yhtä pitkät.", 0.30, 0.60, 9.0)


# ---------------------------------------------------------------- task figures
def virhe():
    """Etsi virhe: the cart's diagram with the hanging weight's weight drawn as a force on the cart (1,0 kg cart, 0,50 kg weight)."""
    m1, m2 = 1.0, 0.50
    f = Fig("fy413-virhe", 230, "Opiskelijan piirtämä voimakuvio pöydällä olevasta kärrystä, joka on sidottu langalla väkipyörän yli riippuvaan punnukseen. Kärry on suorakulmio. "
            "Keskipisteestä lähtee nuoli G1 alas ja alapinnasta yhtä pitkä nuoli N ylös. Kärryn oikeasta reunasta lähtee oikealle nuoli G2, joka on lyhyempi kuin G1 "
            "ja yhtä pitkä kuin riippuvan punnuksen paino. Muita nuolia ei ole.")
    cx, cy = 280, 105
    d = FBD(f, 7.0, body=(cx, cy, 100, 50), wrong="the weight G2 of the hanging body drawn as a force on the cart: the string pulls the cart with the tension T, which is smaller than G2")
    d.force("G_1", (0, -m1 * g), (cx, cy), "gravity", lab=(24, 0))
    d.force("N", (0, m1 * g), (cx - 28, cy + 25), "normal", surface=0, lab=(-24, 0))
    d.force("G_2", (m2 * g, 0), (cx + 50, cy - 8), "other", lab=(24, 0))
    d.draw()
    f.tex(60, 24, r"\text{voimakuvio: kärry}", "start", MUTED)
    return f.svg()


def malli_atwood():
    """Model diagram for the drawing task of the checks: bodies of 0,40 kg and 0,80 kg over a pulley."""
    return _atwood("fy413-malli-atwood", "Mallikuvio: kaksi riippuvaa kappaletta, 0,40 kg ja 0,80 kg, langan päissä väkipyörän yli. Vasemmalla tilannekuva, jossa "
                   "kevyempi nousee ja raskaampi laskee, ja oranssit nuolet kertovat kiihtyvyydet. Oikealla ylhäällä kevyemmän kappaleen voimakuvio: jännitysvoima T1 ylös, "
                   "pidempi kuin paino G1 alas. Oikealla alhaalla raskaamman kappaleen voimakuvio: jännitysvoima T2 ylös ja pidempi paino G2 alas. Nuolet T1 ja T2 ovat yhtä pitkät.", 0.40, 0.80, 7.0)


def malli_ketju():
    """Model diagram for exercise L2-01: two crates one under the other, a rope each, lifted with acceleration 1,2 m/s² (50 kg above, 30 kg below)."""
    m1, m2, a = 50.0, 30.0, 1.2
    T2 = m2 * (g + a); T1 = (m1 + m2) * (g + a)
    f = Fig("fy413-malli-ketju", 400, "Mallikuvio: kaksi laatikkoa roikkuu köysien varassa päällekkäin ja nousee kiihtyen. Vasemmalla tilannekuva: nosturin köysi kannattelee ylempää laatikkoa, "
            "ja alempi laatikko roikkuu toisen köyden päässä ylemmän alla. Oranssi nuoli osoittaa kiihtyvyyden ylös. Oikealla ylhäällä ylemmän laatikon voimakuvio: nosturin köyden "
            "jännitysvoima T1 ylös, paino G1 keskipisteestä alas ja alemman köyden jännitysvoima T2 alapinnasta alas. Oikealla alhaalla alemman laatikon voimakuvio: köyden jännitysvoima T2 "
            "yläpinnasta ylös ja paino G2 alas. Nuoli T1 on pisin, ja T2 on yhtä pitkä molemmissa kuvioissa.")
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    ground(f, 90, 210, 40, below=False)
    f.line(150, 40, 150, 120, COPPER, 2.5); block(f, 124, 120, 52, 40); f.line(150, 160, 150, 215, COPPER, 2.5); block(f, 132, 215, 36, 34)
    f.tex(150, 140, r"m_1", "middle", WHITE); f.tex(150, 232, r"m_2", "middle", WHITE)
    FBD(f, 1).motion(r"\overline{a}", (0, 1), (222, 190), 60, lab=(22, 0))
    f.line(300, 12, 300, 388, RULE, 1.5, "6 6")
    f.line(310, 214, 590, 214, RULE, 1.5, "6 6")
    f.tex(312, 22, r"\text{voimakuvio: ylempi}", "start", MUTED)
    f.tex(312, 230, r"\text{voimakuvio: alempi}", "start", MUTED)
    S = 0.09
    cx, cy = 440, 150
    d = FBD(f, S, body=(cx, cy, 64, 40), m=m1, a=(0, a))
    d.force("T_1", (0, T1), (cx, cy - 20), "tension", rope=(0, 1), lab=(26, 2))
    d.force("G_1", (0, -m1 * g), (cx, cy), "gravity", lab=(-26, 2))
    d.force("T_2", (0, -T2), (cx + 18, cy + 20), "tension", rope=(0, -1), lab=(26, 2))
    d.draw()
    cx, cy = 440, 316
    d = FBD(f, S, body=(cx, cy, 52, 34), m=m2, a=(0, a))
    d.force("T_2", (0, T2), (cx, cy - 17), "tension", rope=(0, 1), lab=(26, 2))
    d.force("G_2", (0, -m2 * g), (cx, cy), "gravity", lab=(26, 2))
    d.draw()
    return f.svg()


FIGURES = {"hero": hero, "tilanne": tilanne, "esimerkki": esimerkki, "atwood": atwood, "virhe": virhe, "malli-atwood": malli_atwood, "malli-ketju": malli_ketju}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "esimerkki": "reveals: the situation picture and the two force diagrams of the worked example (cart 1,5 kg, weight 0,60 kg)",
    "tilanne": "reveals: the situation picture and the two force diagrams of a cart pulled over a table by a hanging weight (a theory figure)",
    "atwood": "reveals: the situation picture and the two force diagrams of two bodies hanging over a pulley (a theory figure)",
    "virhe": "safe: a deliberately wrong diagram (the hanging weight's weight drawn as a force on the cart) for error-finding; its description lists the arrows, not the error",
    "malli-atwood": "reveals: the model diagrams of two bodies of 0,40 kg and 0,80 kg over a pulley (shown after the drawing attempt)",
    "malli-ketju": "reveals: the model diagrams of two crates hanging one under the other and lifted with acceleration (shown in the solution)",
}
