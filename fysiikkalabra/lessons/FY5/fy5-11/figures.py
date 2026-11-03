"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-11` writes them into lesson.md.
Colours: wavefronts water blue, rays ink, the direction of travel velocity blue, the normal dashed muted, the angles of
incidence and reflection green (a correct pair). No force red: a displacement is not a force."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER, WATER_LIGHT, COLD, COLD_LIGHT, GOOD, ALUMINIUM,
                    METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, GRAIN, ICE_EDGE, PAPER, n)
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
    for k, (x0, half) in enumerate(((12, 2 * lam), (312, lam / 2))):
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
    """The chapter's opening illustration: a harbour seen from above, waves from the sea pass a narrow gap in the breakwater
    and spread into the basin, rocking a boat moored in a corner."""
    f = H.hero("fy511-hero", "Kuvitus: satama ylhäältä katsottuna. Yläosassa on avomeri, jolla aallonharjat kulkevat "
               "suorina riveinä kohti rantaa. Kivistä tehty aallonmurtaja kulkee poikki kuvan, ja sen keskellä on kapea "
               "aukko. Aukon takana sataman altaassa aallonharjat ovat kaaria, jotka ulottuvat altaan nurkkiin asti. "
               "Laitureissa on veneitä, ja nurkassa oleva vene keinuu aalloissa.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy511h-sea", WATER_LIGHT, WATER))
    for y in (40, 100, 160, 220):                      # straight crests on the open sea
        f.path(f"M0,{y} " + " ".join(f"Q{x + 30},{y - 8} {x + 60},{y}" for x in range(0, 1200, 60)), stroke=WHITE, w=5, extra='stroke-linecap="round" stroke-opacity="0.8"')
    gap0, gap1, yb = 560, 640, 262
    # the basin: crests spreading from the gap, clipped to the basin
    f.defs_add('<clipPath id="fy511h-basin"><rect x="150" y="300" width="900" height="300"/></clipPath>')
    arcs = "".join(f'<path d="M{600 - r},300 A{r},{r} 0 0 0 {600 + r},300" fill="none" stroke="{WHITE}" stroke-width="5" stroke-opacity="{0.85 - 0.07 * k:.2f}" stroke-linecap="round"/>'
                   for k, r in enumerate(range(60, 720, 60)))
    f.add(f'<g clip-path="url(#fy511h-basin)">{arcs}</g>')
    # quays at both sides and at the bottom (stone)
    for x, w in ((0, 150), (1050, 150)):
        f.rect(x, 300, w, 300, SAND_DARK)
        f.rect(x, 300, w, 300, "none", INK, 3)
    f.rect(0, 560, 1200, 40, SAND_DARK, INK, 3)
    for x in range(10, 150, 46):
        f.line(x, 300, x, 560, SAND, 3)
    for x in range(1060, 1200, 46):
        f.line(x, 300, x, 560, SAND, 3)
    # the breakwater: a band of rocks with a gap
    for x0, x1 in ((0, gap0), (gap1, 1200)):
        f.rect(x0, yb, x1 - x0, 40, METAL_EDGE)
        for k, x in enumerate(range(x0 + 18, x1 - 10, 34)):
            f.circle(x, yb + 10 + 18 * (k % 2), 15, ALUMINIUM if k % 3 else IRON, INK, 2)
    # boats: moored at the quays, one rocking in the lower-left corner
    def boat(cx, cy, ang, hull, deck):
        f.add(f'<g transform="translate({cx} {cy}) rotate({ang})"><path d="M-60,0 Q-50,-22 0,-24 Q50,-22 70,0 Q50,22 0,24 Q-50,22 -60,0 Z" '
              f'fill="{hull}" stroke="{INK}" stroke-width="3"/><rect x="-24" y="-11" width="40" height="22" rx="5" fill="{deck}" stroke="{INK}" stroke-width="2.5"/></g>')
    boat(214, 360, 90, WHITE, COLD_LIGHT)
    boat(986, 380, 90, WHITE, SAND_LIGHT)
    boat(986, 470, 90, COLD_LIGHT, WHITE)
    boat(230, 506, 72, WHITE, SAND_LIGHT)
    for x, y in ((150, 360), (150, 506), (1050, 380), (1050, 470)):
        f.circle(x, y, 7, IRON, INK, 2)
    f.path("M150,360 L178,360", stroke=INK, w=2); f.path("M1050,380 L1022,380", stroke=INK, w=2); f.path("M1050,470 L1022,470", stroke=INK, w=2)
    f.path("M150,506 L198,496", stroke=INK, w=2)
    # the rocking boat's own small ripples
    for r in (82, 100):
        f.add(f'<ellipse cx="230" cy="506" rx="{r}" ry="{r * 0.45:.0f}" transform="rotate(72 230 506)" fill="none" stroke="{WHITE}" stroke-width="3" stroke-opacity="0.6"/>')
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
