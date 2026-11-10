"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-11` writes them into lesson.md.
Colours: wavefronts water blue, rays ink, the direction of travel velocity blue, the normal dashed muted, the angles of
incidence and reflection green (a correct pair). No force red: a displacement is not a force."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER, WATER_LIGHT, COLD, COLD_LIGHT, GOOD, ALUMINIUM,
                    METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, GRAIN, ICE, ICE_EDGE, HOT, PAPER, n)
import herolib as H

ROPE = "#8a5f22"


def arc(f, cx, cy, r, a0, a1, color, w=2.5, dash=None):
    """A circular arc from angle a0 to a1 (degrees, counter-clockwise on the page, 0 = right)."""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 0 if a1 > a0 else 1
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f.add(f'<path d="M{n(x0)},{n(y0)} A{n(r)},{n(r)} 0 {large} {sweep} {n(x1)},{n(y1)}" fill="none" stroke="{color}" stroke-width="{w:g}"{d}/>')


def fronts():
    f = Fig("fy511-rin", 340, "Kaavakuva kahdesta aallosta ylhäältä katsottuna. Vasemmalla tasoaalto: aaltorintamat ovat "
            "yhdensuuntaisia suoria, joiden väli on aallonpituus lambda, ja säteet ovat niitä vastaan kohtisuoria nuolia. "
            "Oikealla pistemäisestä lähteestä lähtevä ympyräaalto: aaltorintamat ovat samankeskisiä ympyröitä ja säteet "
            "lähtevät lähteestä joka suuntaan, kohtisuoraan rintamia vastaan.")
    f.rect(12, 44, 276, 236, GLASS, rx=8)
    f.rect(312, 44, 276, 236, GLASS, rx=8)
    f.line(300, 40, 300, 330, RULE, 2, "6 6")
    f.tex(150, 22, r"\text{tasoaalto}", "middle")
    f.tex(450, 22, r"\text{ympyräaalto}", "middle")
    for x in (70, 130, 190, 250):
        f.line(x, 60, x, 264, WATER, 3)
    for y in (96, 162, 228):
        f.arrow(30, y, 278, y, INK, 2.5, 14)
    f.line(70, 292, 130, 292, INK, 2)
    f.line(70, 284, 70, 300, INK, 2); f.line(130, 284, 130, 300, INK, 2)
    f.tex(100, 316, r"\lambda", "middle")
    f.tex(284, 316, r"\text{aaltorintama}", "end")
    cx, cy = 450, 162
    for r in (34, 68, 102):
        f.circle(cx, cy, r, "none", WATER, 3)
    f.circle(cx, cy, 6, INK)
    for k in range(8):
        a = math.radians(22.5 + 45 * k)
        f.arrow(cx + 12 * math.cos(a), cy - 12 * math.sin(a), cx + 124 * math.cos(a), cy - 124 * math.sin(a), INK, 2.5, 14)
    f.tex(584, 316, r"\text{säde}", "end")
    f.line(540, 304, 536, 252, MUTED, 1.5)
    return f.svg()


def rope_panel(f, x0, y0, fixed, after):
    """One rope: from x0 + 20 to the end at x0 + 236, baseline y0. A pulse up (or down) and its direction of travel."""
    xe = x0 + 236
    f.line(x0 + 16, y0, xe, y0, RULE, 1.5, "5 5")
    if fixed:
        f.rect(xe + 4, y0 - 54, 22, 108, IRON, INK, 2.5, 3)
        for k in range(5): f.line(xe + 8, y0 - 36 + 20 * k + 10, xe + 22, y0 - 36 + 20 * k - 4, INK, 1.5)
        f.circle(xe + 2, y0, 5, ALUMINIUM, INK, 2)
    else:
        f.rect(xe - 3, y0 - 62, 6, 124, METAL_EDGE, rx=3)
        f.add(f'<ellipse cx="{xe}" cy="{y0}" rx="11" ry="5" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    xc = x0 + (162 if after else 90)
    sgn = -1 if (fixed and after) else 1
    pts = []
    for i in range(0, 221):
        x = x0 + 16 + i
        pts.append((x, y0 - sgn * 40 * math.exp(-((x - xc) / 22) ** 2)))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=ROPE, w=4)
    d = -1 if after else 1
    ya = y0 - 66
    f.arrow(xc - d * 26, ya, xc + d * 26, ya, COLD, 3, 13)
    f.tex(xc + d * 34, ya, "v", "start" if d > 0 else "end", COLD)


def rope():
    f = Fig("fy511-koysi", 380, "Kaavakuva, ei mittakaavassa: köyden pulssin heijastuminen kahdessa tapauksessa. "
            "Vasemmalla köyden pää on kiinnitetty seinään (kiinteä pää), oikealla pää on rengas, joka liukuu kitkatta "
            "pystysuoraa tankoa pitkin (vapaa pää). Ylärivillä ennen heijastumista ylöspäin suuntautunut pulssi etenee "
            "oikealle kohti päätä. Alarivillä heijastumisen jälkeen pulssi etenee vasemmalle: kiinteästä päästä "
            "heijastunut pulssi on kääntynyt alaspäin, vapaasta päästä heijastunut on yhä ylöspäin.")
    f.tex(150, 22, r"\text{kiinteä pää}", "middle")
    f.tex(450, 22, r"\text{vapaa pää}", "middle")
    f.line(300, 40, 300, 368, RULE, 2, "6 6")
    f.line(12, 204, 588, 204, RULE_LIGHT, 1.5)
    for x0, fixed in ((12, True), (312, False)):
        f.tex(x0 + 4, 60, r"\text{ennen}", "start", MUTED)
        rope_panel(f, x0, 140, fixed, False)
        f.tex(x0 + 4, 226, r"\text{jälkeen}", "start", MUTED)
        rope_panel(f, x0, 300, fixed, True)
    return f.svg()


def diffraction():
    f = Fig("fy511-diff", 360, "Kaavakuva, ei mittakaavassa: tasoaalto tulee vasemmalta esteeseen, jossa on rako, ylhäältä "
            "katsottuna. Vasemmalla rako on noin neljän aallonpituuden levyinen: raon kohdalla aaltorintamat jatkavat "
            "suorina, ja vain reunoilla ne kaartuvat hieman varjoon. Raon pisteisiin on piirretty pienet Huygensin "
            "alkeisaallot. Oikealla rako on aallonpituutta kapeampi: raon takana aaltorintamat ovat "
            "puoliympyröitä, ja aalto leviää koko alueelle raon taakse.")
    lam = 26
    f.tex(150, 22, r"b \approx 4\lambda", "middle")
    f.tex(450, 22, r"b < \lambda", "middle")
    f.line(300, 40, 300, 348, RULE, 2, "6 6")
    for k, (x0, half) in enumerate(((12, 2 * lam), (312, 0.35 * lam))):
        cid = f"fy511-diffclip{k}"
        f.defs_add(f'<clipPath id="{cid}"><rect x="{x0}" y="44" width="276" height="292" rx="8"/></clipPath>')
        f.rect(x0, 44, 276, 292, GLASS, rx=8)
        xb, yc = x0 + 70, 190
        g = [f'<g clip-path="url(#{cid})">']
        for x in (x0 + 14, x0 + 40, x0 + 66):
            g.append(f'<line x1="{x}" y1="44" x2="{x}" y2="336" stroke="{WATER}" stroke-width="3"/>')
        for m in range(1, 9):
            r = m * lam
            if half > lam:            # wide gap: straight in the beam, quarter circles round the edges
                top, bot = yc - half, yc + half
                g.append(f'<path d="M{n(xb)},{n(top - r)} A{r},{r} 0 0 1 {n(xb + r)},{n(top)} L{n(xb + r)},{n(bot)} '
                         f'A{r},{r} 0 0 1 {n(xb)},{n(bot + r)}" fill="none" stroke="{WATER}" stroke-width="3" stroke-opacity="{1 - 0.06 * m:.2f}"/>')
            else:
                g.append(f'<path d="M{n(xb)},{n(yc - r)} A{r},{r} 0 0 1 {n(xb)},{n(yc + r)}" fill="none" stroke="{WATER}" stroke-width="3" stroke-opacity="{1 - 0.08 * m:.2f}"/>')
        g.append("</g>")
        f.add("".join(g))
        f.rect(xb - 5, 44, 10, yc - half - 44, ALUMINIUM, INK, 2)
        f.rect(xb - 5, yc + half, 10, 336 - yc - half, ALUMINIUM, INK, 2)
        srcs = [yc - half + 2 * half * (j + 0.5) / 4 for j in range(4)] if half > lam else [yc]
        for y in srcs:
            if half > lam:
                f.path(f"M{n(xb)},{n(y - 11)} A11,11 0 0 1 {n(xb)},{n(y + 11)}", stroke=ICE_EDGE, w=2)
            f.circle(xb, y, 4, INK)
        f.arrow(x0 + 8, 318, x0 + 50, 318, COLD, 3, 13)
    return f.svg()


def law():
    f = Fig("fy511-laki", 340, "Kaavakuva: tuleva säde osuu seinän pintaan kohdassa O, ja heijastunut säde lähtee siitä. "
            "Kohdasta O on piirretty katkoviivalla pinnan normaali eli pintaa vastaan kohtisuora suora. Tulokulma alfa on "
            "tulevan säteen ja normaalin välinen kulma ja heijastuskulma beeta heijastuneen säteen ja normaalin välinen "
            "kulma; molemmat ovat 40 astetta. Harmaalla on merkitty säteen ja pinnan välinen kulma, 90 astetta miinus "
            "alfa, jota ei käytetä tulokulmana.")
    O = (300, 262); a = 40; R = 220
    sa, ca = math.sin(math.radians(a)), math.cos(math.radians(a))
    f.rect(12, O[1], 576, 22, ALUMINIUM)
    for x in range(20, 588, 18): f.line(x, O[1] + 20, x + 14, O[1] + 4, METAL_EDGE, 1.5)
    f.line(12, O[1], 588, O[1], INK, 3)
    f.line(O[0], O[1], O[0], 66, MUTED, 2, "7 6")
    f.tex(O[0], 48, r"\text{normaali}", "middle")
    f.arrow(O[0] - R * sa, O[1] - R * ca, O[0] - 4 * sa, O[1] - 4 * ca, INK, 3, 15)
    f.arrow(O[0], O[1], O[0] + R * sa, O[1] - R * ca, INK, 3, 15)
    arc(f, *O, 72, 90, 90 + a, GOOD, 3)
    arc(f, *O, 72, 90 - a, 90, GOOD, 3)
    m = math.radians(90 + a / 2); f.tex(O[0] + 96 * math.cos(m), O[1] - 96 * math.sin(m), r"\alpha", "middle", GOOD)
    m = math.radians(90 - a / 2); f.tex(O[0] + 96 * math.cos(m), O[1] - 96 * math.sin(m), r"\beta", "middle", GOOD)
    arc(f, *O, 128, 90 + a, 180, MUTED, 2, "5 4")
    m = math.radians(180 - (90 - a) / 2); f.tex(O[0] + 152 * math.cos(m) - 4, O[1] - 152 * math.sin(m), r"90^\circ - \alpha", "end", MUTED)
    f.tex(O[0], O[1] + 46, "O", "middle")
    f.line(O[0], O[1] + 4, O[0], O[1] + 30, MUTED, 1.5)
    f.tex(20, 72, r"\text{tuleva säde}", "start")
    f.tex(580, 72, r"\text{heijastunut säde}", "end")
    f.tex(580, 240, r"\text{seinä}", "end")
    return f.svg()


def huygens():
    f = Fig("fy511-huyg", 350, "Kaavakuva: Huygensin periaate selittää heijastuslain. Tasoaallon aaltorintama AB osuu "
            "vinosti seinään: piste A on jo seinällä, kun piste B on vielä matkan päässä. Kun B etenee säteen suuntaan "
            "seinälle kohtaan C, kohdasta A lähtenyt alkeisaalto on ehtinyt yhtä pitkän matkan, ja sen säde on yhtä "
            "suuri kuin matka BC. Myös A:n ja C:n puolivälistä on piirretty pienempi alkeisaalto. Heijastunut "
            "aaltorintama CD sivuaa alkeisaaltoja. Rintama AB muodostaa seinän kanssa kulman alfa ja rintama CD kulman "
            "beeta, ja kulmat ovat yhtä suuret.")
    yw, a = 296, 40
    sa, ca = math.sin(math.radians(a)), math.cos(math.radians(a))
    A = (140, yw); F = 252
    B = (A[0] + F * ca, A[1] - F * sa); Ls = F * sa / ca
    C = (B[0] + Ls * sa, yw); D = (A[0] + Ls * sa, yw - Ls * ca); M = ((A[0] + C[0]) / 2, yw)
    f.rect(12, yw, 576, 22, ALUMINIUM)
    for x in range(20, 588, 18): f.line(x, yw + 20, x + 14, yw + 4, METAL_EDGE, 1.5)
    f.line(12, yw, 588, yw, INK, 3)
    for c, r, a0, a1 in ((A, Ls, 18, 112), (M, Ls / 2, 12, 168)):     # parts of the wavelets around their tangent points
        arc(f, c[0], c[1], r, a0, a1, ICE_EDGE, 2, "6 5")
    f.line(A[0], A[1], B[0], B[1], WATER, 4)
    f.line(C[0], C[1], D[0], D[1], WATER, 4)
    f.arrow(B[0], B[1], C[0] - 3 * sa, C[1] - 3 * ca, INK, 2.5, 14)
    f.arrow(A[0], A[1], D[0], D[1], INK, 2.5, 14)
    for P in (A, B, C, D, M): f.circle(P[0], P[1], 5, INK)
    arc(f, A[0], A[1], 54, 0, a, GOOD, 3)
    arc(f, C[0], C[1], 54, 180 - a, 180, GOOD, 3)
    f.tex(A[0] + 72 * math.cos(math.radians(a / 2)), yw - 72 * math.sin(math.radians(a / 2)), r"\alpha", "middle", GOOD)
    f.tex(C[0] - 72 * math.cos(math.radians(a / 2)), yw - 72 * math.sin(math.radians(a / 2)), r"\beta", "middle", GOOD)
    f.tex(A[0] - 12, yw - 18, "A", "end")
    f.tex(C[0] + 12, yw - 18, "C", "start")
    f.tex(B[0] + 14, B[1] - 6, "B", "start")
    f.tex(D[0] - 14, D[1] - 6, "D", "end")
    f.tex(196, 52, r"\text{alkeisaalto}", "middle")
    tip = (A[0] + Ls * math.cos(math.radians(100)), yw - Ls * math.sin(math.radians(100)))
    f.line(160, 68, tip[0] + 3, tip[1] - 3, MUTED, 1.5)
    return f.svg()


def hero():
    """The chapter's opening illustration: a harbour seen from a drone. Straight crests on the open sea reach the breakwater;
    behind its narrow gap they spread as half circles across the whole basin and rock the boats moored in the corners
    that lie in the breakwater's shadow. Drawn in true perspective: points on the water (X across, Z ahead, in metres)
    are projected from a camera 34 m up, tilted 32° down."""
    f = H.hero("fy511-hero", "Kuvitus: satama ylhäältä viistosti katsottuna. Taustalla on avomeri, jolla aallonharjat kulkevat "
               "suorina riveinä kohti satamaa. Kivistä tehdyssä aallonmurtajassa on keskellä kapea aukko, jonka "
               "kummallakin puolella on pieni majakka. Aukon takana sataman altaassa aallonharjat leviävät puoliympyröinä "
               "koko altaan leveydelle, myös aallonmurtajan taakse altaan nurkkiin, joissa laiturin veneet keinuvat. "
               "Laitureilla on punaisia venevajoja ja kuusia, ja kaukana merellä purjevene.")
    th, F, h = math.radians(32), 760, 34.0
    cy = 50 + F * math.tan(th)                          # the horizon at y = 50

    def P(X, Z, e=0.0):
        d = (h - e) * math.sin(th) + Z * math.cos(th)
        v = (e - h) * math.cos(th) + Z * math.sin(th)
        return 600 + F * X / d, cy - F * v / d

    def poly(pts, close=True):
        s = " L".join(f"{n(x)},{n(y)}" for x, y in (P(*p) for p in pts))
        return "M" + s + (" Z" if close else "")

    ZQ, ZB, DB, W, G, LAM = 49.0, 104.0, 9.0, 40.0, 8.0, 7.0     # front quay, breakwater, its width, basin half-width, half gap, λ
    # sky and the far archipelago
    f.rect(0, 0, 1200, 60, H.grad(f, "fy511h-sky", ICE, GLASS))
    f.rect(0, 50, 1200, 550, H.grad(f, "fy511h-sea", WATER_LIGHT, WATER, y1=50, y2=600))
    H.forest(f, 50, 16, 14, METAL_EDGE, seed=4, x0=70, x1=300, depth=0)
    H.forest(f, 50, 11, 12, METAL_EDGE, seed=7, x0=860, x1=1010, depth=0)
    # straight crests on the open sea (broken where the wind breaks them), closer together towards the horizon
    for k in range(1, 40):
        Z = ZB + DB + 4 + LAM * k
        wpx = F / (Z * math.cos(th) + h * math.sin(th))   # px per metre at that distance
        if wpx < 2.2: break
        _, y = P(0, Z)
        amp = 0.18 * LAM * wpx * math.sin(th)
        x, j = -30 + 60 * H.rnd(k, 3), 0
        while x < 1220:
            L = (14 + 10 * H.rnd(j + 40 * k, 9)) * wpx
            f.path(f"M{n(x)},{n(y)} q{n(L / 2)},{n(-amp)} {n(L)},0", stroke=WHITE, w=round(max(1.5, min(4.5, 0.5 * wpx)), 1),
                   extra=f'stroke-linecap="round" stroke-opacity="{0.9 - 0.02 * k:.2f}"')
            x += L + (3 + 5 * H.rnd(j + 40 * k, 2)) * wpx; j += 1
    # the basin: half circles from the gap's centre (0, ZB), clipped to the basin's water
    f.defs_add(f'<clipPath id="fy511h-basin"><path d="{poly([(-W, ZQ), (-W, ZB), (W, ZB), (W, ZQ)])}"/></clipPath>')
    g = []
    for k in range(1, 20):
        r = LAM * k
        segs = 48
        pts = []
        for i in range(segs + 1):
            a = math.pi * i / segs                      # 0 .. π: from +X through towards the viewer to -X
            pts.append((r * math.cos(a), ZB - r * math.sin(a)))
        for i in range(segs):
            a = math.pi * (i + 0.5) / segs
            amp = 0.45 + 0.5 * math.sin(a) ** 2         # strongest straight through the gap, weaker sideways
            (xa, ya), (xb, yb) = P(*pts[i]), P(*pts[i + 1])
            wpx = F / (pts[i][1] * math.cos(th) + h * math.sin(th))
            g.append(f'<path d="M{n(xa)},{n(ya)} L{n(xb)},{n(yb)}" stroke="{WHITE}" stroke-width="{n(min(6, max(2.5, 0.5 * wpx)))}" '
                     f'stroke-opacity="{amp * (1 - 0.025 * k):.2f}" stroke-linecap="round"/>')
    f.add(f'<g clip-path="url(#fy511h-basin)">{"".join(g)}</g>')
    # land: headlands on both sides reaching past the breakwater, the front quay; a stone edge faces the water
    ground = H.grad(f, "fy511h-land", SAND_LIGHT, SAND_DARK, y1=60, y2=600)
    for sgn in (-1, 1):
        f.path(poly([(sgn * W, ZQ - 30), (sgn * W, ZB + DB), (sgn * (W + 6), ZB + DB + 22), (sgn * (W + 30), ZB + DB + 52),
                     (sgn * 300, ZB + 90), (sgn * 300, ZQ - 30)]), ground, INK, 2.5)
        f.path(poly([(sgn * W, ZB + DB), (sgn * (W + 6), ZB + DB + 22), (sgn * (W + 30), ZB + DB + 52), (sgn * 300, ZB + 90)], close=False),
               stroke=WHITE, w=4, extra='stroke-opacity="0.7"')
    f.path(poly([(-300, ZQ), (300, ZQ), (300, ZQ - 30), (-300, ZQ - 30)]), ground)
    f.path(poly([(-W, ZQ), (W, ZQ)], close=False), stroke=INK, w=3)
    # quay stone edge: a band of granite blocks along the waterline
    for sgn in (-1, 1):
        for k in range(18):
            Z0 = ZQ + k * (ZB - ZQ) / 18
            f.path(poly([(sgn * W, Z0), (sgn * (W + 1.6), Z0), (sgn * (W + 1.6), Z0 + (ZB - ZQ) / 18), (sgn * W, Z0 + (ZB - ZQ) / 18)]),
                   ALUMINIUM if k % 2 else RULE, INK, 1.5)
    for k in range(-12, 12):
        X0 = k * 4
        if X0 < -W or X0 + 4 > W: continue
        f.path(poly([(X0, ZQ), (X0 + 4, ZQ), (X0 + 4, ZQ - 1.6), (X0, ZQ - 1.6)]), ALUMINIUM if k % 2 else RULE, INK, 1.5)
    # the breakwater: a rubble mound 3 m high with a gap in the middle
    for s0, s1 in ((-W - 2, -G), (G, W + 2)):
        f.path(poly([(s0, ZB, 0), (s1, ZB, 0), (s1, ZB, 3), (s0, ZB, 3)]), IRON, INK, 2.5)         # face towards the basin
        f.path(poly([(s0, ZB, 3), (s1, ZB, 3), (s1, ZB + DB, 3), (s0, ZB + DB, 3)]), METAL_EDGE, INK, 2.5)  # top
        xe = s1 if s0 < 0 else s0
        f.path(poly([(xe, ZB, 0), (xe, ZB + DB, 0), (xe, ZB + DB, 3), (xe, ZB, 3)]), IRON, INK, 2.5)   # end face at the gap
        k = 0
        for row, Zr in enumerate((ZB + 1.6, ZB + 4.5, ZB + 7.4)):
            X = s0 + (row % 2) * 1.3
            while X < s1 - 1:
                cx, cyy = P(X + 0.9, Zr, 3.2)
                rr = 1.2 * F / (Zr * math.cos(th) + h * math.sin(th))
                if -20 < cx < 1220:
                    f.circle(cx, cyy, round(rr * (0.8 + 0.3 * H.rnd(k, 5)), 1), ALUMINIUM if k % 3 else RULE, INK, 1.5)
                X += 2.6; k += 1
    # beacons at the gap: a red one on the left, a green one on the right, on white towers
    for sgn, col in ((-1, HOT), (1, GOOD)):
        bx, bz = sgn * (G + 2.2), ZB + DB / 2
        (x0, y0), (_, y1) = P(bx, bz, 3), P(bx, bz, 10)
        wpx = F / (bz * math.cos(th) + h * math.sin(th))
        f.rect(x0 - 1.2 * wpx, y1, 2.4 * wpx, y0 - y1, WHITE, INK, 2)
        f.rect(x0 - 1.2 * wpx, y1 + (y0 - y1) * 0.35, 2.4 * wpx, (y0 - y1) * 0.25, col, INK, 2)
        f.rect(x0 - 1.6 * wpx, y1 - 2 * wpx, 3.2 * wpx, 2 * wpx, col, INK, 2, 3)
        f.path(f"M{n(x0 - 1.9 * wpx)},{n(y1 - 2 * wpx)} L{n(x0)},{n(y1 - 3.4 * wpx)} L{n(x0 + 1.9 * wpx)},{n(y1 - 2 * wpx)} Z", INK)

    def box(X0, X1, Z0, Z1, hh, wall, roof):
        """A gabled shed on the land, ridge along Z, its gable towards the viewer."""
        ridge, Xm = hh + (X1 - X0) * 0.4, (X0 + X1) / 2
        near, far = (X1, X0) if X1 < 0 else (X0, X1)    # the long wall facing the basin and the camera
        f.path(poly([(far, Z0, hh), (far, Z1, hh), (Xm, Z1, ridge), (Xm, Z0, ridge)]), roof, INK, 2)
        f.path(poly([(near, Z0, 0), (near, Z1, 0), (near, Z1, hh), (near, Z0, hh)]), wall, INK, 2)
        f.path(poly([(near, Z0, hh), (near, Z1, hh), (Xm, Z1, ridge), (Xm, Z0, ridge)]), METAL_EDGE, INK, 2)
        f.path(poly([(X0, Z0, 0), (X1, Z0, 0), (X1, Z0, hh), (Xm, Z0, ridge), (X0, Z0, hh)]), wall, INK, 2)
        f.path(poly([(Xm - (X1 - X0) * 0.2, Z0, 0), (Xm + (X1 - X0) * 0.2, Z0, 0), (Xm + (X1 - X0) * 0.2, Z0, hh * 0.8), (Xm - (X1 - X0) * 0.2, Z0, hh * 0.8)]), IRON, INK, 1.5)
        for Zw in (Z0 + (Z1 - Z0) * 0.3, Z0 + (Z1 - Z0) * 0.7):
            f.path(poly([(near, Zw - 1, hh * 0.45), (near, Zw + 1, hh * 0.45), (near, Zw + 1, hh * 0.8), (near, Zw - 1, hh * 0.8)]), GLASS, INK, 1.5)

    def tree(X, Z, hh):
        x, y = P(X, Z, 0)
        wpx = F / (Z * math.cos(th) + h * math.sin(th))
        H.spruce(f, x, y, hh * wpx)

    # the land behind, back to front (sorted by distance so nearer things cover farther ones)
    items = [(Z, "t", (X, Z, hh)) for X, Z, hh in ((-112, 168, 14), (-92, 152, 12), (-130, 140, 15), (104, 166, 14), (86, 146, 11),
                                                    (124, 136, 15), (-72, 128, 11), (70, 126, 12), (-64, 116, 11), (66, 110, 12),
                                                    (-62, 76, 11), (64, 66, 12))]
    items += [(104, "b", (-60, -49, 92, 104, 4.0, HOT, IRON)), (96, "b", (49, 60, 84, 96, 4.0, HOT, IRON))]
    for _, kind, a in sorted(items, key=lambda t: -t[0]):
        (tree if kind == "t" else box)(*a)
    # a sailing boat far out at sea
    sx, sy = P(-70, 260)
    f.path(f"M{n(sx - 16)},{n(sy)} L{n(sx + 16)},{n(sy)} L{n(sx + 11)},{n(sy + 6)} L{n(sx - 12)},{n(sy + 6)} Z", WHITE, INK, 1.5)
    f.path(f"M{n(sx)},{n(sy - 2)} L{n(sx)},{n(sy - 34)} L{n(sx + 14)},{n(sy - 4)} Z", WHITE, INK, 1.5)
    f.path(f"M{n(sx - 2)},{n(sy - 30)} L{n(sx - 2)},{n(sy - 4)} L{n(sx - 14)},{n(sy - 4)} Z", WHITE, INK, 1.5)

    # boats: hulls drawn on the water plane, a cabin on top
    def boat(X, Z, ang, L, hull, cabin, rock=0.0):
        ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        def q(u, v, e=0.0): return (X + u * ca - v * sa, Z + u * sa + v * ca, e)
        outline = [(-L / 2, 0), (-L * 0.42, L * 0.15), (L * 0.1, L * 0.17), (L * 0.38, L * 0.1), (L / 2, 0), (L * 0.38, -L * 0.1), (L * 0.1, -L * 0.17), (-L * 0.42, -L * 0.15)]
        rk = math.radians(rock)
        hull_top = [q(u, v, 0.9 + v * math.sin(rk)) for u, v in outline]
        hull_bot = [q(u * 0.92, v * 0.8, 0) for u, v in outline]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in (P(*p) for p in hull_bot)) + " Z", INK, extra='fill-opacity="0.25"')
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in (P(*p) for p in hull_top)) + " Z", hull, INK, 2)
        cab = [q(u, v, 1.0 + v * math.sin(rk)) for u, v in ((-L * 0.25, -L * 0.09), (L * 0.08, -L * 0.09), (L * 0.08, L * 0.09), (-L * 0.25, L * 0.09))]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in (P(*p) for p in cab)) + " Z", cabin, INK, 2)

    # rocking boats in the corners behind the breakwater (their own ripple rings), moored boats along the quays
    for sgn in (-1, 1):
        cxz = (sgn * (W - 10), ZB - 6)
        for rr in (7.5, 10.5):
            pts = [P(cxz[0] + rr * math.cos(a), cxz[1] + rr * 0.8 * math.sin(a)) for a in [i * math.pi / 24 for i in range(49)]]
            f.add('<path d="M' + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{WHITE}" stroke-width="2.5" stroke-opacity="0.55"/>')
        boat(cxz[0], cxz[1], sgn * 8, 11, WHITE, COLD_LIGHT if sgn < 0 else SAND_LIGHT, rock=6)
    boat(-W + 3.2, 72, 90, 9, WHITE, SAND_LIGHT); boat(-W + 3.2, 58, 90, 8, COLD_LIGHT, WHITE)
    boat(W - 3.2, 76, 90, 9, WHITE, COLD_LIGHT); boat(W - 3.2, 61, 90, 8, SAND_LIGHT, WHITE)
    # bollards on the front quay
    for X in (-27, -9, 9, 27):
        x, y = P(X, ZQ - 2, 0)
        f.rect(x - 7, y - 16, 14, 16, IRON, INK, 2, 3); f.rect(x - 10, y - 20, 20, 6, INK, None, 2, 2)
    return f.svg()


FIGURES = {"hero": hero, "rintamat": fronts, "koysi": rope, "diffraktio": diffraction, "heijastuslaki": law, "huygens": huygens}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "rintamat": "safe: plane and circular wavefronts with rays perpendicular to them, λ marked",
    "koysi": "reveals: a fixed end inverts the pulse, a free end does not",
    "diffraktio": "reveals: a gap about λ wide spreads the wave into the whole region behind it",
    "heijastuslaki": "reveals: α = β measured from the normal, not from the surface",
    "huygens": "reveals: the Huygens construction of the reflected front, α = β",
}
