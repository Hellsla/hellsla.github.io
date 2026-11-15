"""Figures of the FY9 unit fy9-voimat (scripts/figlib.py, fbd.py, herolib.py); `python3 scripts/units.py figures fy9-voimat`
writes them into content/fi/units/fy9-voimat/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a car tows a trailer of firewood along a lakeside road in autumn (no text, no people)
kartta      the recognition chart of the review (Mistä tunnistan, mitä lakia käytän?): task signs -> the law or method
kalteva     a sled sliding down a snowy slope: the situation picture and the sled's force diagram with the weight's
            components dashed (kinetic friction up the slope, acceleration down it)
hihna       the Sovella error task, not in unit.md: a box on an accelerating conveyor belt and a student's force diagram
            with one error; `PYTHONPATH=scripts python3 lessons/units/fy9-voimat/figures.py` pastes it into the text of
            the activity "hihna" in inquiry.json (figcat ids cannot name a unit's figure)
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, HEAT, HOT, COLD, COLD_LIGHT, ICE, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, n)
from fbd import FBD, ground
import herolib as H

figlib.set_language({}, ",")

ACCENT = "#1a4d2e"                                        # the site's own dark green (site.css --accent, the buttons)
WOOD, WOOD_DARK = "#d9b26a", "#a97a35"
BOX, BOX_EDGE = SAND_LIGHT, WOOD_DARK


def _dir(deg): return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def hero():
    """An autumn afternoon by a Finnish lake: a red car tows a small trailer of firewood along the shore road; birches and
    spruces, the far shore's forest and a calm lake. The car and the trailer are the two bodies of the Why question."""
    f = H.hero("fy9vo-hero", "Kuvitus: syksyinen iltapäivä järven rannalla. Etualan tiellä punainen henkilöauto vetää perässään "
               "pientä peräkärryä, jossa on polttopuita. Auto ja kärry on yhdistetty vetoaisalla. Tien takana on järvi ja sen "
               "toisella rannalla metsää, tien varressa koivuja ja kuusia.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9vo-sky", "#cfe3f1", "#f6f1e6"))
    H.cloud(f, 250, 90, 1.1); H.cloud(f, 900, 70, 0.9); H.cloud(f, 620, 140, 0.7)
    H.forest(f, 300, 46, 34, "#3f6b4f", seed=7, depth=24)
    f.rect(0, 300, 1200, 110, H.grad(f, "fy9vo-lake", "#a9d1f0", "#7fb3dc"))
    for x0, x1, y in ((80, 300, 330), (420, 700, 352), (820, 1100, 336), (160, 460, 384), (760, 1040, 392)):
        f.line(x0, y, x1, y, WHITE, 2, cap="round")
    f.path("M0,410 Q300,398 600,406 T1200,404 V600 H0 Z", "#b9c98a")           # the autumn verge
    f.path("M0,440 L1200,432 L1200,540 L0,548 Z", "#8a8f96")                    # the road
    for x in range(30, 1200, 140): f.rect(x, 487, 70, 6, WHITE)                  # the centre line
    f.path("M0,548 L1200,540 V600 H0 Z", "#a3b86c")
    for x, h, yl in ((70, 190, 440), (1120, 210, 436)):
        H.birch(f, x, yl, h)
    H.spruce(f, 1010, 436, 150, "#2b6a3e"); H.spruce(f, 170, 440, 120, "#2b6a3e")
    for k in range(14):                                                          # a few yellow leaves on the verge
        f.circle(40 + H.rnd(k, 5) * 1120, 418 + H.rnd(k + 40, 5) * 14, 4, "#f2c94c")
    yg = 520                                                                     # the wheels stand on the road
    # the trailer: a box on one axle, logs stacked in it, a tow bar to the car's hitch
    f.rect(250, 430, 230, 62, "#c4ccd4", INK, 3, 4)
    f.line(250, 446, 480, 446, METAL_EDGE, 2)
    for row, (y, xs) in enumerate(((418, range(270, 470, 30)), (394, range(285, 455, 30)), (370, range(300, 440, 30)))):
        for x in xs:
            f.circle(x, y, 14, WOOD, WOOD_DARK, 2.5); f.circle(x, y, 5, GRAIN)
    f.rect(470, 470, 120, 8, IRON, INK, 2)                                       # the tow bar
    f.circle(365, yg - 24, 26, INK); f.circle(365, yg - 24, 11, ALUMINIUM, INK, 2)
    # the car, facing right (forward)
    f.path("M580,500 L580,452 Q584,436 606,432 L660,428 L712,384 Q726,372 750,372 L846,372 Q868,372 884,390 L924,428 "
           "L968,436 Q994,442 996,466 L996,500 Z", HOT, INK, 3)
    f.path("M720,426 L752,388 Q760,382 772,382 L800,382 L800,426 Z", GLASS, INK, 2)
    f.path("M812,382 L842,382 Q858,382 868,394 L896,426 L812,426 Z", GLASS, INK, 2)
    f.line(806, 432, 806, 494, "#a32222", 2)
    f.rect(976, 448, 16, 12, HEAT_LIGHT, INK, 1.5, 3)                            # a headlight
    f.rect(584, 446, 10, 14, "#ffd8a8", INK, 1.5, 2)                             # a tail light
    for cx in (660, 914):
        f.circle(cx, yg - 24, 30, INK); f.circle(cx, yg - 24, 13, ALUMINIUM, INK, 2)
    f.path("M220,526 Q600,534 1010,524", stroke="#757b82", w=5, extra='stroke-linecap="round" stroke-opacity="0.6"')
    return f.svg()


def kartta():
    """The recognition chart (teacher 2026-11-15, replaces the concept map): "Mistä tunnistan, mitä lakia käytän?". One
    card per sign in the task's own words (YO language): the sign on top, the choice it leads to and, as the result in a
    pill in the site's dark green, the law or method; no list of formulas. Stacked for a phone: a spine down the left from the start box."""
    rows = [
        (r"\text{vakionopeus tai levossa}", r"\to\ a = 0", r"\Sigma\overline{F} = \overline{0}"),
        (r"\text{lähtee levosta tai kiihtyy}", r"\to\ a \neq 0", r"\Sigma\overline{F} = m\overline{a}"),
        (r"\text{tanko tai vipu voi kiertyä}", r"\to\ \text{myös momentit}", r"\Sigma M = 0"),
        (r"\text{kaksi kappaletta köydellä}", r"\to\ \text{yhtälö kummallekin}", r"\Sigma F_i = m_i a_i"),
        (r"\text{kitkaton pinta}", r"\to\ \text{ei kitkavoimaa}", r"F_\mu = 0"),
        (r"\text{liukuu karhealla pinnalla}", r"\to\ \text{liikekitka}", r"F_\mu = \mu N"),
        (r"\text{ilmanvastus, nopeus tasaantuu}", r"\to\ \text{voimat tasapainossa}", r"F_\text{v} = G"),
    ]
    hub_h, x0, x1, ch, gap, top = 72, 30, 372, 72, 14, 98
    height = top + len(rows) * (ch + gap) - gap + 8
    f = Fig("fy9vo-kartta", height, ARIA_KARTTA, width=380, size=21)
    f.line(14, hub_h + 8, 14, top + len(rows) * (ch + gap) - gap - ch / 2, RULE, 3)
    f.rect(8, 8, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, 8 + 26, r"\textbf{mistä tunnistan lain?}", "middle", INK, w=330)
    f.tex(190, 8 + 54, r"\text{voimakuvio ensin, sitten tunnusmerkki}", "middle", INK, size=17, w=340)
    for k, (sign, choice, law) in enumerate(rows):
        y = top + k * (ch + gap)
        f.line(14, y + ch / 2, x0, y + ch / 2, RULE, 3)
        f.rect(x0, y, x1 - x0, ch, WHITE, MUTED, 2, 10)
        f.tex(x0 + 14, y + 22, sign, "start", INK, size=19, w=x1 - x0 - 28)
        f.line(x0 + 10, y + 40, x1 - 10, y + 40, RULE_LIGHT, 1.5)
        f.tex(x0 + 14, y + 55, choice, "start", MUTED, size=17, w=170)
        f.rect(x1 - 134, y + 44, 124, 24, ACCENT, ACCENT, 2, 8)
        f.tex(x1 - 72, y + 56, law, "middle", WHITE, size=17, w=116)
    return f.svg()


ARIA_KARTTA = ("Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita voimakuviosta ja katso, mikä tehtävän tunnusmerkki sopii. "
               "Vakionopeus tai levossa: kiihtyvyys on nolla, joten voimien summa on nolla. Lähtee levosta tai kiihtyy: kiihtyvyys ei "
               "ole nolla, joten voimien summa on massa kertaa kiihtyvyys. Tanko tai vipu voi kiertyä: myös momenttien summa on nolla. "
               "Kaksi kappaletta köydellä: oma liikeyhtälö kummallekin kappaleelle. Kitkaton pinta: ei kitkavoimaa. Liukuu karhealla "
               "pinnalla: liikekitka on kitkakerroin kertaa tukivoima. Ilmanvastus ja nopeus tasaantuu: voimat ovat tasapainossa ja "
               "ilmanvastus on yhtä suuri kuin paino.")


def _sled(f, x0, y0, s, deg, L=92, hh=30):
    """A plastic sled on a slope that starts at (x0, y0) and rises at deg: its runner's middle s along the slope.
    Returns the sled's centre (figure coordinates)."""
    t = _dir(deg); nrm = (-t[1], t[0])
    bx, by = x0 + s * t[0], y0 - s * t[1]
    P = lambda u, v: (bx + u * t[0] + v * nrm[0], by - u * t[1] - v * nrm[1])
    shell = [P(-L / 2, 0), P(L / 2, 0), P(L / 2 + 14, hh * 0.9), P(L / 2 + 4, hh), P(-L / 2, hh)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in shell) + " Z", COLD, INK, 2.5)
    a, b = P(-L / 2 + 10, hh * 0.55), P(L / 2 - 6, hh * 0.55)
    f.line(a[0], a[1], b[0], b[1], COLD_LIGHT, 3, cap="round")
    return P(0, hh / 2)


def kalteva():
    """Kaava: a sled slides down a snowy slope of 25° (kinetic friction coefficient 0,15), speeding up. Left the situation
    picture with v and a beside the sled; right its force diagram, the sled a rectangle tilted with the slope: G from
    the centre straight down, N from the bottom face perpendicular to the slope, friction from the uphill bottom corner
    up the slope, and G's components dashed. Lengths to scale (G = 100 units)."""
    deg, mu, G = 25.0, 0.15, 100.0
    th = math.radians(deg)
    f = Fig("fy9vo-kalteva", 380, "Kaksi kuvaa. Vasemmalla tilannekuva: muovipulkka liukuu lumista rinnettä alas vasemmalle. Rinne "
            "nousee oikealle kulmassa alfa vaakatasoon nähden. Pulkan yllä sininen nopeusnuoli ja oranssi kiihtyvyysnuoli "
            "osoittavat rinnettä alas. Oikealla pulkan voimakuvio, pulkka rinteen suuntaisesti kallistettuna suorakulmiona: "
            "paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan rinteestä ulospäin ja liikekitka F myy "
            "alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit on piirretty katkoviivoin keskipisteestä: G x "
            "rinnettä alas ja G y kohtisuoraan rinnettä kohti. Komponentti G y on yhtä pitkä kuin tukivoima, ja G x on "
            "selvästi pidempi kuin kitka, joten voimien summa osoittaa rinnettä alas. Nuolten pituudet ovat mittakaavassa.", size=28)
    f.tex(130, 22, r"\text{tilannekuva}", "middle", MUTED)
    x0, y0 = 22, 316
    t = _dir(deg); L = 250
    x1, y1 = x0 + L * t[0], y0 - L * t[1]
    f.path(f"M{n(x0)},{n(y0)} L{n(x1)},{n(y1)} L{n(x1)},{n(y0 + 18)} L{n(x0)},{n(y0 + 18)} Z", "#f8fbfd", INK, 2.5)
    f.path(f"M{n(x0 + 30)},{n(y0 + 8)} L{n(x1 - 10)},{n(y0 + 8)}", stroke="#d7e3ec", w=6, extra='stroke-linecap="round"')
    c = _sled(f, x0, y0, 120, deg)
    down = (-t[0], t[1])                                                         # down the slope, figure coordinates (y down)
    away = (-t[1], -t[0])                                                        # out of the slope, figure coordinates
    for col, lab, off in ((COLD, r"\overline{v}", 42), (HEAT, r"\overline{a}", 86)):
        sx, sy = c[0] + 34 * t[0] + off * away[0], c[1] - 34 * t[1] + off * away[1]
        ex, ey = sx + 64 * down[0], sy + 64 * down[1]
        f.line(sx, sy, ex - 2 * down[0], ey - 2 * down[1], col, 2.5)
        for sgn in (1, -1):
            ang = math.atan2(down[1], down[0]) + math.pi + sgn * 0.45
            f.line(ex, ey, ex + 13 * math.cos(ang), ey + 13 * math.sin(ang), col, 2.5, cap="round")
        f.tex(sx + 16, sy - 8, lab, "start", col)
    f.path(f"M{n(x0 + 58)},{n(y0)} A58,58 0 0 0 {n(x0 + 58 * t[0])},{n(y0 - 58 * t[1])}", "none", INK, 2)
    f.tex(x0 + 82, y0 - 14, r"\alpha", "middle")
    f.line(276, 20, 276, 360, RULE, 1.5, "6 6")
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 444, 176, 100, 58
    nrm = (-t[1], t[0])
    bc = (cx - h / 2 * nrm[0], cy + h / 2 * nrm[1])                               # the middle of the bottom face
    upc = (bc[0] + w / 2 * t[0], bc[1] - w / 2 * t[1])                           # the uphill bottom corner
    N = G * math.cos(th); F = mu * N
    d = FBD(f, 1.45, body=(cx, cy, w, h, deg), a_dir=(-t[0], -t[1]))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-16, 22))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 20 * t[0], bc[1] - 20 * t[1]), "normal", surface=deg, lab=(-12, -12))
    d.force("F_mu", (F * t[0], F * t[1]), upc, "friction", surface=deg, lab=(16, -14))
    d.component("G_x", "G", (-t[0], -t[1]), lab=(-24, 4))
    d.component("G_y", "G", (t[1], -t[0]), lab=(28, 6))
    d.draw()
    f.path(f"M{n(cx)},{n(cy + 44)} A44,44 0 0 0 {n(cx + 44 * math.sin(th))},{n(cy + 44 * math.cos(th))}", "none", INK, 2)
    f.tex(cx + 18, cy + 64, r"\alpha", "middle")
    return f.svg()


def hihna():
    """Sovella error task: a box rides on a conveyor belt that speeds up to the right; the box does not slip. Left the
    situation picture (v and a beside the box), right a student's force diagram with one error: the friction points
    backwards (left), against the motion, although static friction must point forward to speed the box up. The
    description lists what is drawn, never whether it is right."""
    f = Fig("fy9vo-hihna", 340, "Kaksi kuvaa. Vasemmalla tilannekuva: pahvilaatikko on vaakasuoralla kuljetinhihnalla, joka lähtee "
            "liikkeelle oikealle ja kiihtyy. Laatikko ei liu'u hihnalla. Laatikon yllä sininen nopeusnuoli ja oranssi "
            "kiihtyvyysnuoli osoittavat oikealle. Oikealla opiskelijan piirtämä laatikon voimakuvio, laatikko suorakulmiona: "
            "paino G keskipisteestä alas, tukivoima N alapinnasta ylös yhtä pitkänä kuin paino ja kitkavoima F myy alapinnan "
            "vasemmasta kulmasta vasemmalle. Kuvion vieressä oranssi kiihtyvyysnuoli osoittaa oikealle.", size=28)
    f.tex(130, 22, r"\text{tilannekuva}", "middle", MUTED)
    yb = 236                                                                     # the belt's top surface
    f.rect(26, yb, 220, 22, "#495057", INK, 2.5, 11)
    for x in (37, 235): f.circle(x, yb + 11, 9, ALUMINIUM, INK, 2)
    for x in range(56, 220, 26): f.line(x, yb + 4, x + 10, yb + 4, "#868e96", 2, cap="round")
    f.rect(54, yb + 22, 10, 50, IRON, INK, 2); f.rect(208, yb + 22, 10, 50, IRON, INK, 2)
    ground(f, 16, 256, yb + 72)
    f.rect(96, yb - 64, 84, 64, BOX, BOX_EDGE, 2.5, 3)                           # the cardboard box
    f.line(96, yb - 44, 180, yb - 44, BOX_EDGE, 2); f.line(138, yb - 64, 138, yb - 44, BOX_EDGE, 2)
    for col, lab, y in ((COLD, r"\overline{v}", 120), (HEAT, r"\overline{a}", 84)):
        f.line(110, y, 172, y, col, 2.5)
        for sgn in (1, -1): f.line(174, y, 162, y + sgn * 6, col, 2.5, cap="round")
        f.tex(196, y, lab, "middle", col)
    f.line(276, 20, 276, 320, RULE, 1.5, "6 6")
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 430, 180, 100, 70
    G = 100.0
    d = FBD(f, 0.9, body=(cx, cy, w, h), wrong="the static friction points backwards, against the velocity: it must point "
            "forward (right), because it is the only horizontal force and the box speeds up to the right")
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-18, 4))
    d.force("N", (0, G), (cx + 22, cy + h / 2), "normal", surface=0, lab=(20, 0))
    d.force("F_mu", (-30, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-6, -18))
    d.motion(r"\overline{a}", (1, 0), (cx + w / 2 + 20, cy - 10), length=62, lab=(16, -18))
    d.draw()
    return f.svg()


def paste_hihna():
    """Put hihna() into the text of the Sovella activity "hihna" of inquiry.json in place of the figure there."""
    import json, pathlib, re
    p = pathlib.Path(__file__).resolve().parents[3] / "content" / "fi" / "units" / "fy9-voimat" / "inquiry.json"
    raw = p.read_text(); d = json.loads(raw)
    a = next(a for a in d["activities"] if a["id"] == "hihna")
    svg = hihna()
    a["text"] = re.sub(r"<svg .*?</svg>", lambda m: svg, a["text"], flags=re.S) if "<svg" in a["text"] else a["text"] + "\n\n" + svg
    new = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    if new != raw: p.write_text(new); print("pasted hihna into inquiry.json")


if __name__ == "__main__":
    paste_hihna()


FIGURES = {"hero": hero, "kartta": kartta, "kalteva": kalteva}
REUSE = {"kartta": "reveals: the key laws of the FY4 force chapters (Newton's laws, weight, friction, slope, coupled bodies, terminal velocity)",
         "kalteva": "reveals: the force diagram of a sled sliding down a slope with kinetic friction and the weight's components"}
