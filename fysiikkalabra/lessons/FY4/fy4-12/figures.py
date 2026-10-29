"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-12` writes them into lesson.md.
Colours (teacher 2026-10-29): velocity arrows blue #1971c2 (COLD), acceleration arrows orange #e8590c (HEAT), forces red;
body A (the car) is green, body B (the cyclist) brown, so no body ever wears a colour that means a quantity."""
import math
from figlib import (Fig, Axes, INK, MUTED, RULE, RULE_LIGHT, WHITE, COLD, HEAT, HEAT_LIGHT, HOT, GOOD, GOOD_LIGHT, SAND_LIGHT, SAND,
                    SAND_DARK, GRAIN, ALUMINIUM, METAL_EDGE, IRON, COPPER, WATER, WATER_LIGHT, GLASS, ICE, fi, n)
import herolib as H
from herolib import grad, rnd

A_COL, B_COL, B_LIGHT = GOOD, "#8a5f22", SAND_DARK        # the two bodies: green car A, brown cyclist B


# ---------------------------------------------------------------- pictures: a car and a cyclist for the hero
def car(f, x, y, sc=1.0, body=GOOD, light=GOOD_LIGHT, pre="c"):
    """A small car in side view driving to the right: rear bumper at x, tyres on the ground y."""
    def pt(dx, dy): return f"{n(x + dx * sc)},{n(y + dy * sc)}"
    # shadow
    f.add(f'<ellipse cx="{n(x + 120 * sc)}" cy="{n(y + 2 * sc)}" rx="{n(128 * sc)}" ry="{n(9 * sc)}" fill="{INK}" fill-opacity="0.22"/>')
    d = ("M" + pt(2, -30) + " L" + pt(0, -50) + " Q" + pt(0, -66) + " " + pt(16, -68) + " L" + pt(70, -72) + " L" + pt(92, -104) +
         " Q" + pt(98, -112) + " " + pt(110, -112) + " L" + pt(166, -112) + " Q" + pt(182, -112) + " " + pt(192, -100) + " L" + pt(212, -74) +
         " L" + pt(232, -68) + " Q" + pt(244, -64) + " " + pt(244, -48) + " L" + pt(242, -30) + " Z")
    f.path(d, grad(f, f"{pre}-body", light, body, y1=y - 112 * sc, y2=y - 30 * sc), INK, 3)
    # side windows and pillars
    f.path("M" + pt(82, -74) + " L" + pt(100, -102) + " L" + pt(138, -102) + " L" + pt(138, -74) + " Z", GLASS, INK, 2.5)
    f.path("M" + pt(146, -74) + " L" + pt(146, -102) + " L" + pt(166, -102) + " Q" + pt(176, -102) + " " + pt(182, -94) + " L" + pt(198, -74) + " Z", GLASS, INK, 2.5)
    f.line(x + 100 * sc, y - 90 * sc, x + 130 * sc, y - 90 * sc, WHITE, 3, cap="round")
    f.path("M" + pt(8, -52) + " H" + pt(236, -52), stroke=INK, w=1.5, extra='stroke-opacity="0.45"')
    f.rect(x + 100 * sc, y - 60 * sc, 12 * sc, 4 * sc, INK)              # door handle
    f.rect(x + 150 * sc, y - 60 * sc, 12 * sc, 4 * sc, INK)
    # lights, bumpers
    f.path("M" + pt(238, -58) + " L" + pt(244, -56) + " L" + pt(244, -44) + " L" + pt(236, -44) + " Z", HEAT_LIGHT, INK, 2)
    f.path("M" + pt(0, -54) + " L" + pt(6, -56) + " L" + pt(6, -44) + " L" + pt(0, -44) + " Z", HOT, INK, 2)
    f.rect(x - 2 * sc, y - 36 * sc, 248 * sc, 8 * sc, ALUMINIUM, INK, 2, 3)
    # wheels
    for wx in (54, 190):
        f.circle(x + wx * sc, y - 24 * sc, 31 * sc, INK)
        f.circle(x + wx * sc, y - 24 * sc, 14 * sc, ALUMINIUM, METAL_EDGE, 2)
        for k in range(5):
            a = k * 2 * math.pi / 5 + 0.3
            f.line(x + wx * sc, y - 24 * sc, x + (wx + 13 * math.cos(a)) * sc, y - 24 * sc + 13 * math.sin(a) * sc, METAL_EDGE, 2)
        f.circle(x + wx * sc, y - 24 * sc, 3.5 * sc, INK)


def puff(f, x, y, sc=1.0, k=0):
    """An exhaust puff: three overlapping light circles."""
    for dx, dy, r, o in ((0, 0, 10, 0.75), (-18, -6, 14, 0.6), (-40, -2, 18, 0.45)):
        f.add(f'<circle cx="{n(x + dx * sc)}" cy="{n(y + dy * sc)}" r="{n(r * sc)}" fill="{WHITE}" fill-opacity="{o}"/>')


def traffic_light(f, x, ybase, h=210):
    """A pole with a signal head; the green lamp is lit."""
    f.rect(x - 5, ybase - h, 10, h, IRON, INK, 2.5)
    f.rect(x - 30, ybase - h - 98, 60, 100, INK, INK, 2, 8)
    for k, (c, lit) in enumerate(((HOT, False), (HEAT_LIGHT, False), (GOOD_LIGHT, True))):
        cy = ybase - h - 98 + 20 + k * 30
        if lit:
            f.add(f'<circle cx="{n(x)}" cy="{n(cy)}" r="26" fill="{GOOD_LIGHT}" fill-opacity="0.45"/>')
            f.circle(x, cy, 11, GOOD_LIGHT, WHITE, 2.5)
        else:
            f.circle(x, cy, 11, IRON, MUTED, 1.5)
    f.rect(x - 30, ybase - h - 98, 60, 100, "none", INK, 2.5, 8)


def hero():
    """The chapter's opening illustration: at a green light a car starts from rest while a cyclist is already ahead on the same road."""
    f = H.hero("fy412-hero", "Kuvitus: maantie maaseudulla aamupäivällä. Liikennevalot ovat vaihtuneet vihreiksi, ja auto lähtee pysäytysviivalta liikkeelle. "
               "Sen edellä tiellä polkee jo pyöräilijä tasaisessa vauhdissa. Auton takana on pakokaasupilvi ja pyöräilijän takana vauhtiviivoja. "
               "Tienvarressa on tasavälein merkkitolppia, taustalla pelto, punainen talo, koivuja ja kuusimetsää.")
    H.sky(f, "fy412h", 250)
    H.sun(f, "fy412h", 1010, 120, 44)
    H.cloud(f, 220, 84, 0.8); H.cloud(f, 640, 52, 0.55); H.cloud(f, 1090, 210, 0.5)
    H.hills(f, "fy412h", 196, [ALUMINIUM, METAL_EDGE], amp=44, seed=2)
    H.forest(f, 236, 38, 22, IRON, seed=3, depth=20)
    H.forest(f, 258, 44, 26, GOOD, seed=6, depth=12)
    # fields: green pasture and a sand-coloured stubble field with furrows
    f.rect(0, 280, 1200, 140, grad(f, "fy412h-field", GOOD_LIGHT, SAND_LIGHT, y1=280, y2=420))
    f.path("M0,330 Q300,300 620,326 T1200,318 V420 H0 Z", SAND_LIGHT)
    for k in range(9):
        y = 336 + k * 9
        f.path(f"M0,{y} Q300,{y - 24 + k} 620,{y - 5} T1200,{y - 12}", stroke=SAND, w=1.5, extra='stroke-opacity="0.8"')
    H.red_house(f, 120, 330, 150, 80)
    H.birch(f, 330, 352, 150); H.birch(f, 372, 358, 120); H.birch(f, 1010, 352, 140)
    for x, yb, h in ((60, 350, 110), (1120, 345, 120), (1160, 362, 90), (950, 336, 90), (780, 318, 62)):
        H.spruce(f, x, yb, h)
    # verge, road: asphalt band with white edge lines and a dashed centre line
    f.rect(0, 404, 1200, 24, SAND_DARK)
    f.rect(0, 416, 1200, 184, grad(f, "fy412h-verge", GOOD_LIGHT, GOOD, y1=416, y2=600))
    f.rect(0, 424, 1200, 118, IRON)
    f.rect(0, 424, 1200, 118, grad(f, "fy412h-road", METAL_EDGE, IRON, y1=424, y2=542))
    f.line(0, 432, 1200, 432, WHITE, 5); f.line(0, 534, 1200, 534, WHITE, 5)
    for k in range(13):
        f.rect(k * 100 + 20, 480, 56, 7, WHITE)
    # road posts every equal step: positions along the road
    for k in range(10):
        x = 40 + k * 130
        f.rect(x - 5, 548, 10, 26, WHITE, INK, 2)
        f.rect(x - 5, 548, 10, 7, HOT, INK, 1.5)
    # stop line and traffic light at the right of the road in front of the car
    f.rect(596, 436, 14, 96, WHITE)
    traffic_light(f, 640, 430)
    # the car: at the line, starting; exhaust behind it
    car(f, 316, 518, 1.0, A_COL, GOOD_LIGHT, "fy412hc")
    puff(f, 296, 492, 1.0)
    # the cyclist ahead, riding to the right on the far part of the road
    H.rider(f, 770, 910, 498, 44, B_COL, SAND, HOT)
    for k, (dy, L) in enumerate(((-84, 70), (-62, 96), (-40, 60))):
        f.line(738 - L, 498 + dy + 20, 738, 498 + dy + 20, WHITE, 3, cap="round")
    # sign: a round speed-limit sign at the roadside, no digits
    f.rect(1056, 470, 8, 90, IRON, INK, 2)
    f.circle(1060, 452, 34, WHITE, HOT, 9)
    f.rect(1044, 444, 32, 16, INK)
    return f.svg()


# ---------------------------------------------------------------- schematic figures
def _axis(f, y, x0, step, m_max, tick, label):
    """An x axis in metres, to scale: ticks every `tick` m. Returns the X(m) function."""
    X = lambda m: x0 + m * step
    f.arrow(X(0) - 18, y, X(m_max) + 28, y, INK, 2.5, 13)
    for m in range(0, int(m_max) + 1, tick):
        f.line(X(m), y - 4, X(m), y + 7, INK, 2)
        f.tex(X(m), y + 26, fi(m), "middle")
    f.tex(X(m_max) + 36, y, label, "start")
    return X


def _body(f, x, y, letter, col):
    f.circle(x, y, 17, col, WHITE, 2.5)
    f.tex(x, y, rf"\text{{{letter}}}", "middle", WHITE)


def tilanne():
    f = Fig("fy412-tilanne", 420, "Kaavakuva, jossa kaksi kappaletta on samalla x-akselilla, mittakaavassa. Ylhäällä hetkellä t = 0 kappale A on paikassa "
            "0 m ja liikkuu nopeudella 3,0 m/s oikealle, kappale B on paikassa 60 m ja liikkuu nopeudella 2,0 m/s vasemmalle. "
            "Alhaalla hetkellä t = 12 s kumpikin on paikassa 36 m: kappaleet ovat kohdanneet. Nopeusnuolet ovat sinisiä ja eri pituisia.")
    X = _axis(f, 168, 50, 7.5, 60, 10, r"x\ (\text{m})")
    # upper panel: t = 0
    f.tex(24, 26, r"t = 0", "start")
    for (m, col, letter, v) in ((0, A_COL, "A", 3.0), (60, B_COL, "B", -2.0)):
        y = 70 if letter == "A" else 118
        f.line(X(m), y + 17, X(m), 168, MUTED, 1.5, "6 5")
        _body(f, X(m), y, letter, col)
        f.circle(X(m), 168, 7, col, WHITE, 2)
        sgn = 1 if v > 0 else -1
        f.arrow(X(m) + sgn * 26, y, X(m) + sgn * (26 + abs(v) * 14), y, COLD, 4.5, 16)
    f.tex(X(0) + 44, 38, r"\overline{v}_\text{A}", "start", COLD)
    f.tex(X(60) - 40, 86, r"\overline{v}_\text{B}", "end", COLD)
    f.line(24, 214, 576, 214, MUTED, 1.5, "8 6")
    # lower panel: t = 12 s, both at 36 m
    X2 = _axis(f, 380, 50, 7.5, 60, 10, r"x\ (\text{m})")
    f.tex(24, 242, r"t = 12\,\text{s}", "start")
    for (m, col, letter, v) in ((36, A_COL, "A", 3.0), (36, B_COL, "B", -2.0)):
        y = 282 if letter == "A" else 330
        f.line(X2(m), y + 17, X2(m), 380, MUTED, 1.5, "6 5")
        _body(f, X2(m), y, letter, col)
        sgn = 1 if v > 0 else -1
        f.arrow(X2(m) + sgn * 26, y, X2(m) + sgn * (26 + abs(v) * 14), y, COLD, 4.5, 16)
    f.circle(X2(36), 380, 7.5, INK, WHITE, 2)
    f.tex(X2(36) + 86, 306, r"x_\text{A} = x_\text{B} = 36\,\text{m}", "start")
    return f.svg()


def kohtaus():
    f = Fig("fy412-kohtaus", 350, "(t,x)-kuvaaja mittakaavassa kahdesta tasaisesta liikkeestä. Kappale A lähtee paikasta 0 m ja kulkee nopeudella 3,0 m/s: "
            "suora nousee. Kappale B lähtee paikasta 60 m nopeudella −2,0 m/s: suora laskee. Suorat leikkaavat pisteessä, jossa t = 12 s ja x = 36 m. "
            "Katkoviivat johtavat pisteestä akseleille.")
    ax = Axes(f, (92, 300), (468, 52), x=(0, 16), y=(0, 72), xticks=[4, 8, 12, 16], yticks=[12, 24, 36, 48, 60],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, 0), (16, 48)], A_COL, 3.5)
    ax.line([(0, 60), (16, 28)], B_COL, 3.5)
    ax.guide(12, 36)
    ax.point(12, 36, INK, 7.5)
    f.tex(ax.X(16) + 8, ax.Y(48), r"x_\text{A}", "start", A_COL)
    f.tex(ax.X(16) + 8, ax.Y(28), r"x_\text{B}", "start", B_COL)
    f.tex(ax.X(12) + 14, ax.Y(12), r"\text{kohtaaminen}", "start")
    return f.svg()


def kaava():
    f = Fig("fy412-kaava", 350, "(t,x)-kuvaaja mittakaavassa: paikaltaan lähtevä auto A ja samasta paikasta tasaisella nopeudella 6,0 m/s kulkeva pyöräilijä B. "
            "Auton paikka on paraabeli x = t², pyöräilijän suora. Kuvaajat leikkaavat kaksi kertaa: hetkellä t = 0, jolloin kappaleet ovat samassa paikassa lähtiessään, "
            "ja hetkellä t = 6,0 s paikassa 36 m.")
    ax = Axes(f, (92, 300), (468, 52), x=(0, 8), y=(0, 72), xticks=[2, 4, 6, 8], yticks=[12, 24, 36, 48, 60],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.curve(lambda t: t * t, 0, 8, A_COL, 3.5)
    ax.line([(0, 0), (8, 48)], B_COL, 3.5)
    ax.guide(6, 36)
    ax.point(0, 0, INK, 7.5); ax.point(6, 36, INK, 7.5)
    f.tex(ax.X(8) + 8, ax.Y(64), r"x_\text{A}", "start", A_COL)
    f.tex(ax.X(8) + 8, ax.Y(48), r"x_\text{B}", "start", B_COL)
    f.tex(ax.X(6) + 14, ax.Y(23), r"\text{ohitus}", "start")
    f.tex(ax.X(0) + 18, ax.Y(0) - 30, r"\text{lähtö}", "start")
    return f.svg()


def vt():
    f = Fig("fy412-vt", 350, "(t,v)-kuvaaja mittakaavassa samasta liikkeestä kuin edellinen kuvaaja. Auton nopeus kasvaa suorana nollasta, pyöräilijän nopeus on vakio 6,0 m/s. "
            "Hetkeen t = 3,0 s asti pyöräilijä on edellä ja etumatka kasvaa: suorien väliin jää pinta-ala, joka vastaa etumatkan kasvua 9 m. Hetkestä 3,0 s hetkeen 6,0 s auto pienentää etumatkaa, "
            "ja pinta-ala vastaa pienenemistä 9 m. Hetkellä t = 6,0 s auto on saavuttanut pyöräilijän.")
    ax = Axes(f, (92, 300), (468, 52), x=(0, 8), y=(0, 16), xticks=[2, 4, 6, 8], yticks=[4, 8, 12, 16],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})")
    ax.area([(0, 0), (0, 6), (3, 6)], B_LIGHT, 0.55)
    ax.area([(3, 6), (6, 12), (6, 6)], GOOD_LIGHT, 0.75)
    ax.line([(0, 6), (8, 6)], B_COL, 3.5)
    ax.line([(0, 0), (8, 16)], A_COL, 3.5)
    ax.guide(3, 6, MUTED)
    ax.f.line(ax.X(6), ax.Y(12), ax.X(6), ax.y0, MUTED, 1.5, "6 5")
    ax.point(3, 6, INK, 7)
    f.tex(ax.X(8) + 8, ax.Y(16), r"v_\text{A}", "start", A_COL)
    f.tex(ax.X(8) + 8, ax.Y(6) + 2, r"v_\text{B}", "start", B_COL)
    f.tex(ax.X(1.2), ax.Y(6) - 24, r"+9\,\text{m}", "middle")
    f.tex(ax.X(5.3), ax.Y(6) - 24, r"-9\,\text{m}", "middle")
    return f.svg()


def esimerkki():
    f = Fig("fy412-esimerkki", 350, "(t,x)-kuvaaja mittakaavassa esimerkin tilanteesta: pyöräilijä B on aluksi 16 m auton A edellä ja kulkee nopeudella 6,0 m/s; "
            "auto lähtee levosta kiihtyvyydellä 2,0 m/s². Suora x = 16 + 6t ja paraabeli x = t² leikkaavat hetkellä t = 8,0 s paikassa 64 m.")
    ax = Axes(f, (92, 300), (468, 52), x=(0, 10), y=(0, 100), xticks=[2, 4, 6, 8, 10], yticks=[16, 32, 48, 64, 80, 96],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.curve(lambda t: t * t, 0, 10, A_COL, 3.5)
    ax.line([(0, 16), (10, 76)], B_COL, 3.5)
    ax.guide(8, 64)
    ax.point(0, 16, B_COL); ax.point(0, 0, A_COL)
    ax.point(8, 64, INK, 7.5)
    f.tex(ax.X(10) + 8, ax.Y(98), r"x_\text{A}", "start", A_COL)
    f.tex(ax.X(10) + 8, ax.Y(76) + 10, r"x_\text{B}", "start", B_COL)
    return f.svg()


def kaksi_karrya():
    """For tasks: two carts' (t,x) graphs without the answer: A is a line from the origin, B a line from 30 m, they cross."""
    f = Fig("fy412-kaksi-karrya", 340, "(t,x)-kuvaaja mittakaavassa kahdesta tasaisesta liikkeestä. Kärry A lähtee paikasta 0 m ja kulkee tasaisesti paikkaan 60 m hetkeen 10 s mennessä. "
            "Kärry B lähtee paikasta 40 m ja kulkee tasaisesti paikkaan 20 m hetkeen 10 s mennessä. Suorat leikkaavat toisensa kuvaajan sisällä. Kohtaamispistettä ei ole merkitty.")
    ax = Axes(f, (92, 296), (470, 52), x=(0, 12), y=(0, 70), xticks=[2, 4, 6, 8, 10, 12], yticks=[10, 20, 30, 40, 50, 60, 70],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, 0), (10, 60)], A_COL, 3.5)
    ax.line([(0, 40), (10, 20)], B_COL, 3.5)
    ax.point(0, 0, A_COL); ax.point(0, 40, B_COL)
    ax.point(10, 60, A_COL); ax.point(10, 20, B_COL)
    f.tex(ax.X(10) + 12, ax.Y(60), r"x_\text{A}", "start", A_COL)
    f.tex(ax.X(10) + 12, ax.Y(20), r"x_\text{B}", "start", B_COL)
    return f.svg()


def ei_kohtaa():
    """For tasks: a faster body ahead; the (t,x) graph for t >= 0 only, no crossing in sight."""
    f = Fig("fy412-ei-kohtaa", 340, "(t,x)-kuvaaja mittakaavassa kahdesta tasaisesta liikkeestä. Auto A lähtee paikasta 0 m nopeudella 3,0 m/s ja pyöräilijä B paikasta 20 m nopeudella 5,0 m/s. "
            "Pyöräilijän suora on koko ajan auton suoran yläpuolella ja nousee jyrkemmin, joten suorat erkanevat toisistaan.")
    ax = Axes(f, (92, 296), (470, 52), x=(0, 12), y=(0, 90), xticks=[2, 4, 6, 8, 10, 12], yticks=[20, 40, 60, 80],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, 0), (12, 36)], A_COL, 3.5)
    ax.line([(0, 20), (12, 80)], B_COL, 3.5)
    ax.point(0, 0, A_COL); ax.point(0, 20, B_COL)
    f.tex(ax.X(12) + 12, ax.Y(36), r"x_\text{A}", "start", A_COL)
    f.tex(ax.X(12) + 12, ax.Y(80), r"x_\text{B}", "start", B_COL)
    return f.svg()


FIGURES = {"hero": hero, "tilanne": tilanne, "kohtaus": kohtaus, "kaava": kaava, "vt": vt, "esimerkki": esimerkki, "kaksi-karrya": kaksi_karrya, "ei-kohtaa": ei_kohtaa}
REUSE = {"hero": "decorative", "tilanne": "safe", "kohtaus": "reveals: the meeting time and place of the uniform head-on example",
         "kaava": "reveals: the passing time of the d = 0 example", "vt": "reveals: the passing time of the d = 0 example",
         "esimerkki": "reveals: the worked example's answer", "kaksi-karrya": "safe: two crossing lines without the crossing marked", "ei-kohtaa": "safe: two diverging lines, no crossing for t >= 0"}
