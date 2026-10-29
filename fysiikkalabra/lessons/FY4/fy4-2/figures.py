"""Figures of fy4-2 (scripts/figlib.py); `python scripts/figures.py fy4-2` writes them into lesson.md.
Colours carry the quantity in every figure: velocity blue (COLD #1971c2), acceleration orange (HEAT #e8590c);
a displacement read as an area is a light tint of the quantity it comes from."""
import math
from figlib import (Fig, Axes, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK,
                    GRAIN, HEAT_LIGHT, HEAT, HOT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE,
                    GOOD, GOOD_LIGHT, fi, n)
import herolib as H
from herolib import grad, rnd

V_COL, A_COL = COLD, HEAT          # velocity and acceleration arrows (teacher 2026-10-29)


# ---------------------------------------------------------------- opening illustration
def hero():
    """The chapter's opening illustration: a stone dropped from a footbridge, its place shown at equal time steps:
    the gaps grow 1 : 3 : 5 : 7 and its velocity arrow grows by the same amount each step."""
    f = H.hero("fy42-hero", "Kuvitus: kevyen liikenteen silta joen yllä kesäpäivänä. Sillan keskellä nuori pudottaa kiven kaiteen yli, "
               "ja rannalla ystävä kuvaa putoamista puhelimella. Kivi on piirretty viiteen kohtaan yhtä pitkin aikavälein: "
               "välit kasvavat alaspäin suhteessa 1 : 3 : 5 : 7, ja kiven vieressä oleva sininen nopeusnuoli pitenee joka "
               "kerta yhtä paljon. Alimmassa kohdassa kivi osuu veteen ja vesi roiskuu. Mittakaava ei ole tarkka, välien suhteet ovat.")
    H.sky(f, "fy42h", 380, ICE, GLASS)
    H.sun(f, "fy42h", 1060, 92, 44, rays=False)
    for bx, by, w in ((330, 60, 22), (366, 46, 18), (700, 104, 20)):     # swallows far away
        f.path(f"M{bx - w},{by - 6} Q{bx - w / 2},{by - 12} {bx},{by} Q{bx + w / 2},{by - 12} {bx + w},{by - 6}", stroke=INK, w=2.5, extra='stroke-linecap="round"')
    H.cloud(f, 230, 80, 0.75); H.cloud(f, 820, 58, 0.55); H.cloud(f, 470, 130, 0.4)
    H.hills(f, "fy42h", 236, [ALUMINIUM, METAL_EDGE], amp=34, seed=6)
    H.forest(f, 290, 44, 24, IRON, seed=2, depth=18)
    H.forest(f, 314, 50, 28, GOOD, seed=9, depth=14)
    # the river between the banks, the far water lighter
    f.rect(0, 330, 1200, 270, grad(f, "fy42h-river", WATER_LIGHT, WATER, y1=330, y2=600))
    for k in range(16):
        x = 60 + rnd(k, 3) * 1080; y = 360 + rnd(k, 5) * 220; w = 40 + 50 * rnd(k, 8)
        f.path(f"M{n(x)},{n(y)} q{n(w / 4)},-5 {n(w / 2)},0 t{n(w / 2)},0", stroke=WHITE, w=2.5, extra='stroke-linecap="round" stroke-opacity="0.6"')
    # left bank: grass slope down to a gravel shore, a birch and a few stones
    f.path("M0,300 H250 Q300,304 322,350 L372,486 Q380,512 404,524 H0 Z", grad(f, "fy42h-grass", GOOD_LIGHT, SAND_LIGHT, y1=300, y2=520))
    f.path("M0,500 H360 Q390,512 404,524 L430,560 H0 Z", SAND, GRAIN, 2)
    for k in range(18): f.circle(20 + rnd(k, 4) * 390, 512 + rnd(k, 6) * 40, 3 + 3 * rnd(k, 2), GRAIN)
    H.birch(f, 92, 330, 210)
    H.spruce(f, 196, 316, 120)
    # right bank: grass to the abutment, a slope and a gravel shore where the friend stands
    f.path("M1200,300 H960 Q920,304 900,350 L862,452 Q850,486 820,500 H1200 Z", "url(#fy42h-grass)")
    f.path("M1200,470 H860 Q830,486 800,520 L780,560 H1200 Z", SAND, GRAIN, 2)
    for k in range(18): f.circle(800 + rnd(k, 7) * 390, 486 + rnd(k, 9) * 60, 3 + 3 * rnd(k, 5), GRAIN)
    H.spruce(f, 1140, 306, 130); H.spruce(f, 1060, 300, 90)
    for k in range(9):                                         # bushes and flowers along the banks
        bx = 30 + k * 34 if k < 5 else 1000 + (k - 5) * 46; by = 318 + 8 * (k % 2)
        for dx, dy, r in ((0, 0, 18), (16, -6, 14), (-14, -4, 13)):
            f.circle(bx + dx, by + dy, r, GOOD, INK, 1.5)
    for k in range(26):
        fx = 20 + rnd(k, 11) * 300 if k < 13 else 910 + rnd(k, 12) * 280; fy = 350 + rnd(k, 13) * 120
        if k < 13 and fx > 300 - (fy - 350) * 0.2: continue
        f.line(fx, fy, fx, fy - 10, GOOD, 2); f.circle(fx, fy - 12, 3.5, WHITE if k % 3 else HOT, INK, 1)
    for k in range(14):
        gx = 30 + rnd(k, 14) * 270 if k < 7 else 940 + rnd(k, 15) * 240; gy = 380 + rnd(k, 16) * 100
        f.path(f"M{n(gx - 8)},{n(gy)} l4,-14 l4,14 l4,-12 l4,12", stroke=GOOD, w=2, extra='stroke-linecap="round" stroke-linejoin="round"')
    for x in (380, 820):                                       # reeds at the water's edge
        for k in range(6):
            xx = x + (k - 3) * 9 + (20 if x > 600 else 0); yy = 528 + 6 * (k % 2) - (40 if x > 600 else 0)
            f.line(xx, yy, xx - 3, yy - 40, GOOD, 3, cap="round")
            f.add(f'<ellipse cx="{n(xx - 3)}" cy="{n(yy - 40)}" rx="4" ry="10" fill="{COPPER}"/>')
    # footbridge: two stone piers in the water, a steel deck, wooden handrail on posts
    deck_y, deck_h = 236, 24
    f.defs_add('<linearGradient id="fy42h-pier" x1="0" y1="0" x2="1" y2="0">'
               f'<stop offset="0" stop-color="{METAL_EDGE}"/><stop offset="0.4" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{METAL_EDGE}"/></linearGradient>')
    for px in (430, 790):
        f.add(f'<ellipse cx="{px}" cy="548" rx="54" ry="10" fill="{WATER}" fill-opacity="0.5"/>')
        f.path(f"M{px - 34},{deck_y + deck_h} L{px - 42},548 H{px + 42} L{px + 34},{deck_y + deck_h} Z", "url(#fy42h-pier)", INK, 3)
        for k in range(1, 7):
            y = deck_y + deck_h + k * 40
            f.line(px - 34 - k * 1.2, y, px + 34 + k * 1.2, y, METAL_EDGE, 2)
            off = 0 if k % 2 else 18
            f.line(px - 10 + off, y - 40, px - 10 + off, y, METAL_EDGE, 2)
        f.path(f"M{px - 30},{548 + 6} q15,8 30,0 t30,0", stroke=WHITE, w=2.5, extra='stroke-linecap="round"')
    f.rect(170, deck_y, 860, deck_h, H.steel(f, "fy42h-deck", vertical=True), INK, 3, 2)
    f.rect(170, deck_y + deck_h - 6, 860, 6, IRON)
    f.rect(150, deck_y - 4, 40, 70, SAND_DARK, INK, 2.5)        # abutments on the banks
    f.rect(1010, deck_y - 4, 40, 70, SAND_DARK, INK, 2.5)
    # the person on the deck, behind the handrail, reaching over it
    px, pf, sc, lean = 566, deck_y, 0.36, 10
    hand = (630, 142)
    H.walker(f, px, pf, GOOD, IRON, sc, lean=lean, hand=hand, stride=0.35)
    for k in range(22):                                         # handrail posts, about chest high
        x = 186 + k * 38.5
        f.rect(x - 3, deck_y - 84, 6, 84, COPPER, INK, 1.5)
    f.rect(176, deck_y - 90, 848, 10, grad(f, "fy42h-rail", SAND_DARK, COPPER), INK, 2, 3)
    f.line(180, deck_y - 44, 1020, deck_y - 44, COPPER, 3)
    f.line(180, deck_y - 20, 1020, deck_y - 20, COPPER, 3)
    sh = (px + 8 * sc + lean * 0.6, pf - 300 * sc)              # the reaching arm is drawn again over the rail
    f.path(f"M{n(sh[0])},{n(sh[1])} L{n(hand[0])},{n(hand[1])}", stroke=GOOD, w=24 * sc, extra='stroke-linecap="round"')
    f.circle(hand[0], hand[1], 13 * sc, SAND_LIGHT)
    # the friend on the right shore, facing left, filming with a phone
    f.add('<g transform="translate(1900,0) scale(-1,1)">')       # mirrored about x = 950
    fh = H.walker(f, 950, 476, SAND_DARK, INK, 0.4, lean=4, hand=(890, 330), stride=0.4)
    f.add("</g>")
    f.rect(1900 - 890 - 8, 312, 16, 28, INK, INK, 2, 3)
    f.rect(1900 - 890 - 5, 316, 10, 20, ICE, None, 0, 2)
    for dx, dy in ((0, 0), (52, 14)):                           # two ducks on the water
        ux, uy = 230 + dx, 572 + dy
        f.add(f'<ellipse cx="{ux}" cy="{uy}" rx="24" ry="10" fill="{COPPER}" stroke="{INK}" stroke-width="2"/>')
        f.circle(ux + 20, uy - 14, 8, GOOD, INK, 2); f.path(f"M{ux + 27},{uy - 15} l9,2 l-9,3 Z", HEAT_LIGHT, INK, 1)
        f.path(f"M{ux - 30},{uy + 10} q12,5 24,0 t24,0 t24,0", stroke=WHITE, w=2, extra='stroke-linecap="round" stroke-opacity="0.8"')
    # the stone at equal time steps: y = y0 + k n², gaps 1 : 3 : 5 : 7; velocity arrow grows linearly
    x0, y0, k = 636, 156, (522 - 156) / 16
    for i in range(5):
        y = y0 + k * i * i
        op = "1" if i in (0, 4) else "0.55"
        f.add(f'<g opacity="{op}">')
        f.add(f'<ellipse cx="{x0}" cy="{n(y)}" rx="12" ry="10" fill="{IRON}" stroke="{INK}" stroke-width="2"/>')
        f.add(f'<ellipse cx="{x0 - 4}" cy="{n(y - 3)}" rx="4" ry="3" fill="{ALUMINIUM}"/>')
        f.add("</g>")
        if i:
            L = 19 * i
            f.arrow(x0 + 44, y - L / 2, x0 + 44, y + L / 2, V_COL, 5, 14)
    # the splash where the stone hits the water
    for dx, dy, r in ((-30, -18, 5), (-20, -34, 4), (24, -22, 5), (34, -8, 4), (10, -40, 3.5), (-40, -4, 3.5)):
        f.circle(x0 + dx, 522 + dy, r, WATER_LIGHT, WATER, 1.5)
    for rx, op in ((24, 0.9), (40, 0.6), (56, 0.35)):
        f.add(f'<ellipse cx="{x0}" cy="534" rx="{rx}" ry="{rx * 0.2:g}" fill="none" stroke="{WHITE}" stroke-width="3" stroke-opacity="{op}"/>')
    return f.svg()


# ---------------------------------------------------------------- theory figures
def _cart(f, cx, yroad, body=ALUMINIUM, op=1.0):
    """A small cart standing on the road at yroad, its centre at cx."""
    f.add(f'<g opacity="{op:g}">')
    f.rect(cx - 22, yroad - 30, 44, 18, body, INK, 2.5, 4)
    f.rect(cx - 10, yroad - 40, 20, 10, COLD_LIGHT, INK, 2, 2)
    for wx in (cx - 12, cx + 12):
        f.circle(wx, yroad - 8, 7, IRON, INK, 2); f.circle(wx, yroad - 8, 2.5, ALUMINIUM)
    f.add("</g>")


def strobe():
    """Ydinajatus: a cart speeding up and a cart slowing down, photographed at equal time steps, with the velocity
    (blue, length to scale) and the constant acceleration (orange) at every step."""
    f = Fig("fy42-strobe", 368, "Kaavakuva kahdesta kärrystä, jotka on kuvattu yhden sekunnin välein, välit mittakaavassa. Ylhäällä kärry "
            "lähtee levosta ja kiihtyy: välit kasvavat, sininen nopeusnuoli pitenee joka sekunti yhtä paljon ja oranssi "
            "kiihtyvyysnuoli osoittaa liikkeen suuntaan ja pysyy samanpituisena. Alhaalla kärry hidastuu: välit lyhenevät, "
            "nopeusnuoli lyhenee ja kiihtyvyysnuoli osoittaa liikettä vastaan; viimeisessä kuvassa kärry on hetken "
            "paikallaan, mutta kiihtyvyysnuoli on yhä sama.")
    rows = ((140, [50 + 50 * t * t for t in range(4)], [0, 1, 2, 3], 1, r"\text{kiihtyvä liike}"),
            (322, [50 + 100 * (3 * t - 0.5 * t * t) for t in range(4)], [3, 2, 1, 0], -1, r"\text{hidastuva liike}"))
    for yroad, xs, vs, adir, title in rows:
        f.tex(24, yroad - 116, title + r"\text{, kuvat } 1\,\text{s} \text{ välein}", "start")
        f.rect(24, yroad, 552, 10, SAND_LIGHT, None)
        f.line(24, yroad, 576, yroad, INK, 2.5)
        for i, (x, v) in enumerate(zip(xs, vs)):
            _cart(f, x, yroad, op=0.45 + 0.55 * i / 3)
            if v: f.arrow(x, yroad - 56, x + 25 * v, yroad - 56, V_COL, 4, 14)
            f.arrow(x - 18 * adir, yroad + 30, x + 18 * adir, yroad + 30, A_COL, 4, 13)
        i_v = max(range(4), key=lambda i: vs[i])
        f.tex(xs[i_v] + 25 * vs[i_v] / 2, yroad - 84, r"\overline{v}", "middle", V_COL)
        xa = xs[-1] + 26 if adir > 0 else xs[0] + 26
        f.tex(xa, yroad + 30, r"\overline{a}", "start", A_COL)
    f.line(24, 196, 576, 196, MUTED, 1.5, "8 6")
    return f.svg()


def tv_graph():
    """Ydinajatus: the (t,v) graph of uniformly accelerated motion is a line whose slope is the acceleration;
    three lines for a > 0, a = 0, a < 0."""
    f = Fig("fy42-tv", 330, "Kaavakuva kahdesta (t,v)-kuvaajasta, ei lukuarvoja. Vasemmalla suora nousee alkunopeudesta v0, ja suoralta "
            "valitut kaksi pistettä rajaavat kolmion: aikaväli Δt ja nopeuden muutos Δv, joiden suhde on kiihtyvyys a. "
            "Oikealla kolme suoraa samasta alkunopeudesta: nouseva suora on kiihtyvyys a suurempi kuin nolla, vaakasuora "
            "suora kiihtyvyys nolla eli tasainen liike ja laskeva suora kiihtyvyys pienempi kuin nolla.")
    kw = dict(x=(0, 10), y=(0, 10), xticks=[], yticks=[], grid=False, origin_label=False)
    a = Axes(f, (50, 290), (236, 70), xlabel="t", ylabel="v", **kw)
    a.line([(0, 2), (10, 8)], V_COL, 4)
    p1, p2 = (3, 3.8), (8, 6.8)
    a.line([p1, (p2[0], p1[1]), p2], MUTED, 2, "8 6")
    a.point(0, 2, V_COL); a.point(*p1, V_COL); a.point(*p2, V_COL)
    f.tex(a.X(5.5), a.Y(p1[1]) + 24, r"\Delta t", "middle")
    f.tex(a.X(p2[0]) + 12, a.Y(5.3), r"\Delta v", "start")
    f.tex(a.x0 - 10, a.Y(2), "v_0", "end")
    f.tex(a.X(0.6), a.Y(8.6), r"a = \dfrac{\Delta v}{\Delta t}", "start", A_COL)
    f.line(316, 30, 316, 300, RULE, 1.5, "6 6")
    b = Axes(f, (360, 290), (500, 70), xlabel="t", ylabel="v", **kw)
    for end, col, tx in ((8.5, V_COL, "a > 0"), (5, MUTED, "a = 0"), (1.5, INK, "a < 0")):
        b.line([(0, 5), (10, end)], col, 4)
        f.tex(b.X(10) + 10, b.Y(end), tx, "start", col)
    b.point(0, 5, INK)
    f.tex(b.x0 - 10, b.Y(5), "v_0", "end")
    return f.svg()


def tangent():
    """Ydinajatus: the (t,x) graph of a cart speeding up is a curve; the instantaneous velocity at a moment is the
    slope of the tangent there."""
    f = Fig("fy42-tangent", 340, "Kaavakuva (t,x)-kuvaajasta, ei lukuarvoja. Levosta kiihtyvän kärryn kuvaaja on ylöspäin kaartuva käyrä, "
            "joka jyrkkenee koko ajan. Käyrän pisteeseen P on piirretty katkoviivana tangentti eli suora, joka sivuaa käyrää "
            "siinä kohdassa. Tangentilta on valittu kaksi kaukana toisistaan olevaa pistettä, ja niiden aikaväli Δt ja paikan "
            "muutos Δx muodostavat kolmion. Tangentin kulmakerroin Δx jaettuna Δt:llä on kärryn hetkellinen nopeus "
            "hetkellä, jota P vastaa.")
    ax = Axes(f, (70, 300), (440, 64), x=(0, 10), y=(0, 10), xticks=[], yticks=[], grid=False, origin_label=False,
              xlabel="t", ylabel="x")
    xf = lambda t: 0.1 * t * t
    ax.curve(xf, 0, 9.6, INK, 4)
    tp = 6.0; xp, vp = xf(tp), 0.2 * tp                        # P at t = 6: x = 3,6, slope 1,2
    tl = lambda t: xp + vp * (t - tp)
    ta, tb = 3.0, 9.8                                          # the tangent drawn from t = 3 (x = 0) to t = 9,8
    ax.line([(ta, tl(ta)), (tb, tl(tb))], V_COL, 3, "10 7")
    q1, q2 = (5.0, tl(5.0)), (9.4, tl(9.4))
    ax.line([q1, (q2[0], q1[1]), q2], MUTED, 2, "6 5")
    ax.point(*q1, V_COL); ax.point(*q2, V_COL)
    ax.point(tp, xp, INK, 8)
    f.tex(ax.X(tp) - 14, ax.Y(xp) - 22, r"P", "end")
    f.tex(ax.X(7.2), ax.Y(q1[1]) + 24, r"\Delta t", "middle")
    f.tex(ax.X(q2[0]) + 12, ax.Y((q1[1] + q2[1]) / 2), r"\Delta x", "start")
    f.tex(ax.X(tb) + 8, ax.Y(tl(tb)) + 14, r"\text{tangentti}", "start", V_COL)
    f.tex(ax.X(0.4), ax.Y(8.4), r"v = \dfrac{\Delta x}{\Delta t}", "start", V_COL)
    return f.svg()


def area():
    """Kaava: the displacement is the area under the (t,v) line: a rectangle v0 t and a triangle ½ (a t) t."""
    f = Fig("fy42-area", 340, "Kaavakuva (t,v)-kuvaajasta, ei lukuarvoja. Nopeus kasvaa suoraviivaisesti alkunopeudesta v0 hetkellä 0 "
            "nopeuteen v hetkellä t. Suoran alle jäävä alue on jaettu kahteen osaan: sininen suorakulmio, jonka korkeus on "
            "v0 ja leveys t, ja oranssi kolmio sen päällä, jonka korkeus on nopeuden kasvu at ja leveys t. Suorakulmion ala "
            "on v0 kertaa t ja kolmion ala puolet a t:n ja t:n tulosta; yhdessä ne ovat siirtymä Δx.")
    ax = Axes(f, (80, 300), (430, 64), x=(0, 10), y=(0, 10), xticks=[], yticks=[], grid=False, origin_label=False,
              xlabel="t", ylabel="v")
    v0, v1, t1 = 3.5, 8.5, 9.0
    ax.area([(0, 0), (t1, 0), (t1, v0), (0, v0)], COLD_LIGHT, 0.9)
    ax.area([(0, v0), (t1, v0), (t1, v1)], HEAT_LIGHT, 0.75)
    ax.line([(0, v0), (t1, v1)], V_COL, 4)
    ax.line([(t1, 0), (t1, v1)], MUTED, 1.5, "6 5")
    ax.line([(0, v0), (t1, v0)], MUTED, 1.5, "6 5")
    ax.point(0, v0, V_COL); ax.point(t1, v1, V_COL)
    f.tex(ax.x0 - 10, ax.Y(v0), "v_0", "end")
    f.tex(ax.x0 - 10, ax.Y(v1), "v", "end")
    f.line(ax.x0 - 7, ax.Y(v1), ax.x0, ax.Y(v1), INK, 2)
    f.line(ax.x0, ax.Y(v1), ax.X(t1), ax.Y(v1), RULE_LIGHT, 1.5)
    f.tex(ax.X(t1), ax.y0 + 24, "t", "middle")
    f.tex(ax.X(t1 / 2), ax.Y(v0 / 2), r"v_0\,t", "middle")
    f.tex(ax.X(t1 * 0.62), ax.Y(v0 + (v1 - v0) * 0.36), r"\tfrac{1}{2}\,a t\cdot t", "middle")
    f.tex(ax.X(t1) + 12, ax.Y((v0 + v1) / 2), r"a t", "start", A_COL)
    f.tex(ax.X(t1) + 12, ax.Y(v0 / 2), r"v_0", "start")
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id; no answer drawn)
FALL_T = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
FALL_S = [0.002, 0.018, 0.065, 0.128, 0.223, 0.338, 0.477, 0.646, 0.832]


def fall_points():
    f = Fig("fy42-fall", 360, "(t,s)-kuvaaja mittakaavassa: pudotetun teräskuulan putoamismatka s videon yhdeksästä kuvasta 0,05 sekunnin "
            "välein, hetkestä 0 hetkeen 0,40 sekuntia. Pisteet: 0,002; 0,018; 0,065; 0,128; 0,223; 0,338; 0,477; 0,646 ja "
            "0,832 metriä. Pisteisiin ei ole sovitettu käyrää.")
    ax = Axes(f, (96, 314), (476, 64), x=(0, 0.45), y=(0, 0.9), xticks=[0.1, 0.2, 0.3, 0.4], yticks=[0.2, 0.4, 0.6, 0.8],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    for t, s in zip(FALL_T, FALL_S): ax.point(t, s, INK)
    return f.svg()


def ex_tv():
    f = Fig("fy42-extv", 350, "(t,v)-kuvaaja mittakaavassa: potkulaudan nopeus kasvaa tasaisesti. Suora alkaa nopeudesta 2,0 metriä "
            "sekunnissa hetkellä 0 ja päättyy nopeuteen 7,0 metriä sekunnissa hetkellä 5,0 sekuntia.")
    ax = Axes(f, (96, 300), (476, 64), x=(0, 6), y=(0, 8), xticks=[1, 2, 3, 4, 5, 6], yticks=[1, 2, 3, 4, 5, 6, 7, 8],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.line([(0, 2.0), (5.0, 7.0)], V_COL, 3.5)
    ax.point(0, 2.0, V_COL); ax.point(5.0, 7.0, V_COL)
    return f.svg()


def ex_tangent():
    f = Fig("fy42-extan", 370, "(t,x)-kuvaaja mittakaavassa: levosta kiihtyvän kärryn paikka on ylöspäin kaartuva käyrä hetkestä 0 "
            "hetkeen 7 sekuntia. Käyrän pisteeseen hetkellä 4,0 sekuntia, paikassa 8,0 metriä, on piirretty katkoviivana "
            "tangentti. Tangentti leikkaa aika-akselin hetkellä 2,0 sekuntia ja kulkee pisteen (6,0 s; 16 m) kautta.")
    ax = Axes(f, (96, 320), (476, 64), x=(0, 7), y=(0, 24), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=list(range(2, 25, 2)),
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})", yfmt=lambda v: fi(v) if v % 4 == 0 else "")
    ax.curve(lambda t: 0.5 * t * t, 0, 6.9, INK, 3.5)
    ax.line([(2.0, 0.0), (7.0, 20.0)], V_COL, 3, "10 7")
    ax.point(4.0, 8.0, INK, 7)
    f.tex(ax.X(4.0) - 12, ax.Y(8.0) - 20, r"P", "end")
    return f.svg()


def check_tv():
    f = Fig("fy42-chktv", 350, "(t,v)-kuvaaja mittakaavassa: sähköpotkulaudan nopeus kasvaa tasaisesti. Suora alkaa nopeudesta 2,0 metriä "
            "sekunnissa hetkellä 0 ja päättyy nopeuteen 6,0 metriä sekunnissa hetkellä 8,0 sekuntia.")
    ax = Axes(f, (96, 300), (476, 64), x=(0, 9), y=(0, 7), xticks=list(range(1, 10)), yticks=list(range(1, 8)),
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", xfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.line([(0, 2.0), (8.0, 6.0)], V_COL, 3.5)
    ax.point(0, 2.0, V_COL); ax.point(8.0, 6.0, V_COL)
    return f.svg()


FIGURES = {"hero": hero, "strobe": strobe, "tv-graph": tv_graph, "tangent": tangent, "area": area,
           "fall-points": fall_points, "ex-tv": ex_tv, "ex-tangent": ex_tangent, "check-tv": check_tv}

# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "strobe": "reveals: velocity arrows growing and shrinking at constant acceleration, the acceleration at the turning point (a theory figure)",
    "tv-graph": "safe: schematic (t,v) lines with symbols only, no values",
    "tangent": "safe: schematic tangent of a (t,x) curve, symbols only",
    "area": "reveals: the area derivation of x = x0 + v0 t + ½ a t² (a theory figure)",
    "fall-points": "safe: measured fall points only, no fitted curve and no coefficients",
    "ex-tv": "safe: a (t,v) line on a grid; the slope is not marked",
    "ex-tangent": "safe: a (t,x) curve and its tangent on a grid; the slope is not marked",
    "check-tv": "safe: a (t,v) line on a grid; the area is not marked",
}
