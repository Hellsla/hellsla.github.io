"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-12` writes them into lesson.md.
Wave displacement is never drawn in force red: the first wave is water blue, the second violet, their sum ink."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, WATER, WATER_LIGHT, GLASS, SAND, SAND_LIGHT,
                    SAND_DARK, GRAIN, ICE, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, HEAT, HEAT_LIGHT, n)
import herolib as H

VIOLET = "#7048e8"


def pulse(x, c, w):
    """A smooth pulse of unit height centred at c (a raised cosine of half-width w)."""
    return 0.5 * (1 + math.cos(math.pi * (x - c) / w)) if abs(x - c) < w else 0.0


def poly(f, pts, color, w=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f.add(f'<polyline points="{" ".join(f"{n(a)},{n(b)}" for a, b in pts)}" fill="none" stroke="{color}" stroke-width="{w:g}" '
          f'stroke-linejoin="round" stroke-linecap="round"{d}/>')


def pulses():
    f = Fig("fy512-pul", 400, "Kaavakuva: kaksi pulssia kohtaa narussa, kaksi tapausta vierekkäin ja kolme hetkeä allekkain. "
            "Vasemmalla pulssit ovat yhtä suuret ja samalla puolella narua; kohtaamishetkellä narun poikkeama on pulssien "
            "poikkeamien summa, kaksinkertainen. Oikealla pulssit ovat yhtä suuret mutta eri puolilla; kohtaamishetkellä ne "
            "kumoavat toisensa ja naru on hetken suora. Kohtaamisen jälkeen kummassakin tapauksessa pulssit jatkavat "
            "alkuperäisen muotoisina omiin suuntiinsa. Yksittäiset pulssit on piirretty kohtaamishetkellä katkoviivoin.")
    f.tex(268, 22, r"\text{samalla puolella}", "middle")
    f.tex(488, 22, r"\text{eri puolilla}", "middle")
    f.line(378, 44, 378, 386, RULE, 2, "6 6")
    rows = ((100, r"\text{ennen}", 0), (216, r"\text{kohdatessa}", 1), (326, r"\text{jälkeen}", 2))
    amp, w = 34, 30
    for yc, name, k in rows:
        f.tex(14, yc - 4, name, "start", MUTED)
        for x0, x1, sign in ((162, 372, 1), (384, 592, -1)):
            mid = (x0 + x1) / 2
            sep = (70, 0, -70)[k]                   # how far each pulse is from the meeting point (negative: passed through)
            c1, c2 = mid - sep, mid + sep
            xs = [x0 + (x1 - x0) * i / 120 for i in range(121)]
            y1 = lambda x: amp * pulse(x, c1, w)
            y2 = lambda x: sign * amp * pulse(x, c2, w)
            if k == 1:
                poly(f, [(x, yc - y1(x)) for x in xs], WATER, 2.5, "7 5")
                poly(f, [(x, yc - y2(x)) for x in xs], VIOLET, 2.5, "3 9")
            poly(f, [(x, yc - y1(x) - y2(x)) for x in xs], INK, 3.5 if k == 1 else 3)
            if k != 1:                              # the direction of travel above each pulse
                for c, col, sgn_dir in ((c1, WATER, 1 if k == 0 else 1), (c2, VIOLET, -1)):
                    yv = yc - amp - 14 if (col == WATER or sign > 0) else yc + amp + 14
                    f.arrow(c - 14 * sgn_dir, yv, c + 16 * sgn_dir, yv, col, 2.5, 11)
            if k == 0:
                f.circle(c1, yc - amp, 4, WATER)
                f.circle(c2, yc - sign * amp, 4, VIOLET)
    return f.svg()


def hyperbola(cx, cy, c, dsl, sgn, y_top, y_bot, scale):
    """Points (figure units) of the branch |r1 − r2| = dsl around foci (cx ∓ c, cy), on the side sgn."""
    a = dsl / 2
    pts = []
    if a == 0:
        return [(cx, y_top), (cx, y_bot)]
    b = math.sqrt(c * c - a * a)
    for i in range(81):
        y = y_top + (y_bot - y_top) * i / 80
        Y = (cy - y)
        pts.append((cx + sgn * a * math.sqrt(1 + Y * Y / (b * b)), y))
    return pts


def pattern():
    f = Fig("fy512-kuv", 384, "Kaavakuva ylhäältä: kaksi samassa vaiheessa värähtelevää lähdettä S1 ja S2 aaltoaltaan "
            "alareunassa, niiden väli kaksi aallonpituutta. Kummastakin leviää ympyränmuotoisia aaltoja: aallonharjat "
            "yhtenäisinä ja aallonpohjat katkoviivoina sinisinä kaarina. Missä harja kohtaa harjan, interferenssi on "
            "vahvistava; nämä kohdat ovat yhtenäisillä mustilla viivoilla, joiden matkaero on 0 tai yksi aallonpituus. "
            "Niiden välissä katkoviivoitetut mustat solmuviivat, joilla harja kohtaa pohjan ja matkaero on puoli tai puolitoista "
            "aallonpituutta. Kuvio on mittakaavassa.")
    cx, cy, lam = 300, 352, 40
    c = lam                                          # d = 2λ, so c = d/2 = λ
    s1, s2 = (cx - c, cy), (cx + c, cy)
    f.defs_add('<clipPath id="fy512-kuv-clip"><rect x="40" y="40" width="520" height="314"/></clipPath>')
    f.rect(40, 40, 520, 314, GLASS)
    g = []
    for (sx, sy) in (s1, s2):
        for k in range(1, 10):
            g.append(f'<circle cx="{sx}" cy="{sy}" r="{k * lam}" fill="none" stroke="{WATER}" stroke-width="2"/>')
            g.append(f'<circle cx="{sx}" cy="{sy}" r="{k * lam - lam / 2}" fill="none" stroke="{WATER_LIGHT}" stroke-width="2" stroke-dasharray="5 5"/>')
    f.add('<g clip-path="url(#fy512-kuv-clip)">' + "".join(g) + "</g>")
    # antinodal lines Δs = 0 and Δs = λ (solid), nodal lines Δs = λ/2 and 3λ/2 (dashed)
    def branch(dsl, sgn, dash):
        pts = [(x, y) for x, y in hyperbola(cx, cy, c, dsl, sgn, 52, cy, 1) if 44 < x < 556]
        poly(f, pts, INK, 2.5, dash)
        return pts[0]
    top0 = branch(0, 1, None)
    topA = branch(lam, 1, None); branch(lam, -1, None)
    branch(lam / 2, 1, "8 6"); topN = branch(lam / 2, -1, "8 6")
    branch(1.5 * lam, 1, "8 6"); branch(1.5 * lam, -1, "8 6")
    f.rect(40, 40, 520, 314, "none", INK, 2.5, 6)
    for (sx, sy), name, anchor, dx in ((s1, "S_1", "end", -12), (s2, "S_2", "start", 12)):
        f.circle(sx, sy, 7, INK, WHITE, 2)
        f.tex(sx + dx, sy + 2, name, anchor, bg=True)
    f.tex(top0[0] + 8, 22, r"\Delta s = 0", "start")
    f.tex(topA[0] + 6, 22, r"\Delta s = \lambda", "start")
    f.tex(topN[0], 22, r"\text{solmuviiva}", "middle")
    return f.svg()


def path_difference():
    f = Fig("fy512-mat", 360, "Kaavakuva: lähteet S1 ja S2 ovat vasemmalla allekkain, ja piste P on oikealla. Lähteestä S1 "
            "pisteeseen P on matka s1 ja lähteestä S2 matka s2. Pisteen P ympäri piirretty kaari, jonka säde on s2, leikkaa "
            "janan S1P. Leikkauskohdan ja lähteen S1 väliin jäävä paksu jana on matkaero, delta s = s1 − s2. Ei mittakaavassa.")
    S1, S2, P = (110, 56), (110, 206), (380, 262)
    s1 = math.dist(S1, P); s2 = math.dist(S2, P)
    ux, uy = (S1[0] - P[0]) / s1, (S1[1] - P[1]) / s1
    Q = (P[0] + ux * s2, P[1] + uy * s2)              # on the line P -> S1, at the distance s2 from P
    a0 = math.atan2(S2[1] - P[1], S2[0] - P[0]); a1 = math.atan2(Q[1] - P[1], Q[0] - P[0])
    arc = [(P[0] + s2 * math.cos(a0 + (a1 - a0) * i / 40), P[1] + s2 * math.sin(a0 + (a1 - a0) * i / 40)) for i in range(41)]
    poly(f, arc, MUTED, 1.5, "6 5")
    f.line(*P, *S2, INK, 2.5)
    f.line(*P, *Q, INK, 2.5)
    f.line(*Q, *S1, WATER, 7, cap="round")
    for (x, y), name, dx, anchor in ((S1, "S_1", -14, "end"), (S2, "S_2", -14, "end")):
        f.circle(x, y, 8, INK, WHITE, 2)
        f.tex(x + dx, y, name, anchor)
    f.circle(*P, 8, WHITE, INK, 3)
    f.tex(P[0] + 16, P[1], r"\text{P}", "start")
    f.tex((P[0] + Q[0]) / 2 + 14, (P[1] + Q[1]) / 2 - 22, "s_1", "middle")
    f.tex((P[0] + S2[0]) / 2, (P[1] + S2[1]) / 2 + 24, "s_2", "middle")
    f.tex((Q[0] + S1[0]) / 2 + 18, (Q[1] + S1[1]) / 2 - 22, r"\Delta s", "start", WATER)
    f.line(12, 316, 588, 316, RULE_LIGHT, 1.5)
    f.tex(300, 338, r"\Delta s = s_1 - s_2", "middle", w=220)
    return f.svg()


def conditions():
    f = Fig("fy512-ehd", 384, "Kaavakuva: kahden aallon poikkeamat pisteessä P ajan funktiona ja niiden summa, kaksi tapausta "
            "vierekkäin. Vasemmalla matkaero on yksi aallonpituus: sininen ja violetti aalto ovat samassa vaiheessa, harja "
            "harjan kohdalla, ja summan amplitudi on kaksinkertainen. Oikealla matkaero on puoli aallonpituutta: aallot ovat "
            "vastakkaisessa vaiheessa, harja pohjan kohdalla, ja summa on koko ajan nolla.")
    f.tex(220, 22, r"\Delta s = \lambda", "middle")
    f.tex(470, 22, r"\Delta s = \tfrac{1}{2}\lambda", "middle", w=140)
    f.line(345, 44, 345, 372, RULE, 2, "6 6")
    amp = 26
    rows = ((92, 1, r"y_1"), (178, 1, r"y_2"), (292, 2, r"y_1 + y_2"))
    for x0, x1, shift in ((130, 320, 0.0), (370, 568, 0.5)):
        for yc, span, name in rows:
            f.line(x0, yc, x1 + 6, yc, MUTED, 1.5)
            if x0 == 130:                           # the row names once, left of the first case
                f.tex(x0 - 12, yc, name, "end", INK if span == 2 else (WATER if name == "y_1" else VIOLET), w=110)
        def y(i, which, x0=x0, x1=x1, shift=shift):
            u = 2 * (i / 120)                        # two periods across the panel
            a = math.sin(2 * math.pi * u)
            b = math.sin(2 * math.pi * (u - shift))
            return {1: a, 2: b, 3: a + b}[which]
        xs = [x0 + (x1 - x0) * i / 120 for i in range(121)]
        poly(f, [(xs[i], rows[0][0] - amp * y(i, 1)) for i in range(121)], WATER, 3)
        poly(f, [(xs[i], rows[1][0] - amp * y(i, 2)) for i in range(121)], VIOLET, 3)
        poly(f, [(xs[i], rows[2][0] - amp * y(i, 3)) for i in range(121)], INK, 3.5)
        xpk = x0 + (x1 - x0) / 8                     # the first crest of y1: dashed guide through all three rows
        f.line(xpk, 56, xpk, 352, MUTED, 1.5, "5 5")
    f.tex(225, 362, r"\text{vahvistava}", "middle")
    f.tex(469, 362, r"\text{heikentävä}", "middle")
    return f.svg()


def fourier():
    f = Fig("fy512-fou", 384, "Kaavakuva kahdessa osassa. Ylhäällä kolme siniaaltoa, joiden taajuudet ovat 220, 660 ja 1100 "
            "hertsiä ja amplitudit suhteessa yksi, kolmasosa ja viidesosa, ohuina viivoina, ja niiden summa paksuna "
            "mustana käyränä, joka on jo lähes kanttiaallon muotoinen. Alhaalla saman summan spektri: pystypylväät "
            "taajuuksilla 220, 660 ja 1100 hertsiä, pituudet amplitudien suhteessa.")
    x0, x1, yc, amp = 60, 560, 96, 52
    xs = [x0 + (x1 - x0) * i / 300 for i in range(301)]
    comps = ((1, 1.0, WATER), (3, 1 / 3, VIOLET), (5, 1 / 5, GOOD))
    f.line(x0, yc, x1 + 6, yc, MUTED, 1.5)
    for k, A, col in comps:
        poly(f, [(x, yc - amp * A * math.sin(2 * math.pi * k * 2 * (x - x0) / (x1 - x0))) for x in xs], col, 2)
    poly(f, [(x, yc - amp * sum(A * math.sin(2 * math.pi * k * 2 * (x - x0) / (x1 - x0)) for k, A, _ in comps)) for x in xs], INK, 3.5)
    f.tex(x0 - 8, 30, r"\text{signaali}", "start")
    ax = Axes(f, (96, 330), (500, 200), x=(0, 1200), y=(0, 1.2), xticks=[220, 660, 1100], yticks=[],
              xlabel=r"f\ (\text{Hz})", ylabel=r"A", grid=False, xfmt=lambda v: fi(v), origin_label=True)
    for (k, A, col) in comps:
        fx = 220 * k
        f.rect(ax.X(fx) - 9, ax.Y(A), 18, ax.Y(0) - ax.Y(A), col)
    return f.svg()


def hero():
    """The chapter's opening illustration: two loudspeakers on stands in a schoolyard play the same tone, sound spreads
    from both as rings, and a student walks along a path in front of them."""
    f = H.hero("fy512-hero", "Kuvitus: koulun pihalla on kaksi kaiutinta jalustoilla vierekkäin. Molemmista leviää ääntä "
               "samankeskisinä kaarina, ja kaaret menevät toistensa päälle. Kaiuttimien edessä opiskelija kävelee pihan "
               "poikki kulkevaa polkua pitkin ja kuuntelee.")
    H.sky(f, "fy512h")
    H.cloud(f, 860, 96, 0.9)
    H.cloud(f, 1080, 160, 0.6)
    H.forest(f, 330, 50, 28, ALUMINIUM, 3)
    H.red_house(f, 60, 330, 300, 170)
    f.rect(0, 330, 1200, 270, GOOD_LIGHT)
    f.path("M0,520 C300,500 900,500 1200,520 V570 C900,552 300,552 0,570 Z", SAND_LIGHT)
    f.path("M0,520 C300,500 900,500 1200,520", stroke=SAND, w=3)
    # sound rings from both speakers (crests), clipped to the yard above the path
    f.defs_add('<clipPath id="fy512h-clip"><rect x="0" y="0" width="1200" height="520"/></clipPath>')
    rings = []
    for sx in (480, 720):
        for k in range(1, 9):
            r = 46 * k
            rings.append(f'<circle cx="{sx}" cy="330" r="{r}" fill="none" stroke="{COLD}" stroke-width="5" stroke-opacity="{n(0.55 - 0.05 * k)}"/>')
    f.add('<g clip-path="url(#fy512h-clip)">' + "".join(rings) + "</g>")
    for sx in (480, 720):
        f.line(sx, 380, sx - 30, 470, INK, 6, cap="round"); f.line(sx, 380, sx + 30, 470, INK, 6, cap="round"); f.line(sx, 360, sx, 470, INK, 6)
        f.rect(sx - 40, 270, 80, 110, IRON, INK, 4, 8)
        f.circle(sx, 300, 16, METAL_EDGE, INK, 3)
        f.circle(sx, 345, 26, METAL_EDGE, INK, 3)
        f.circle(sx, 345, 9, INK)
    H.walker(f, 900, 540, coat=COLD, sc=0.62, stride=0.8)
    return f.svg()


FIGURES = {"hero": hero, "pulssit": pulses, "kuvio": pattern, "matkaero": path_difference, "ehdot": conditions, "fourier": fourier}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pulssit": "reveals: pulses add while they overlap and pass through each other unchanged",
    "kuvio": "reveals: antinodal lines at Δs = 0 and λ, nodal lines at λ/2 and 3λ/2 for d = 2λ",
    "matkaero": "safe: geometry of s1, s2 and Δs = s1 − s2 without numbers",
    "ehdot": "reveals: Δs = λ gives double amplitude, Δs = λ/2 gives zero",
    "fourier": "reveals: a near-square wave as the sum of 220, 660 and 1100 Hz sines and its spectrum",
}
