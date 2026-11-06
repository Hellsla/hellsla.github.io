"""Figures of this lesson (scripts/figlib.py, scripts/herolib.py); `python scripts/figures.py fy6-11` writes them into lesson.md.
Colours, one meaning each: the electric field (field lines and the field vector E) green (#2b8a3e), forces red (#c92a2a),
velocity blue (#1971c2), acceleration orange (#e8590c); a positive charge is a light red ball with a + sign, a negative
one (an electron) a light blue ball with a − sign, so the sign is never told by colour alone. The plates' field lines are
traced from the same conductor-plate model as the simulation (lesson-answers.py: 40 strips per plate, the charges solved
so that the plates are equipotential), so their straightness between the plates and their bending at the ends are
computed, not drawn by hand. Every label is LaTeX."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD,
                    COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, n)
import herolib as H
from fbd import FBD, VELOCITY

FIELD, FORCE, VEL, ACC = GOOD, HOT, COLD, HEAT


# --- the plate model (the same as the simulation's) ---------------------------------------------------------------
def _Fp(u, y):
    r2 = u * u + y * y
    v = (0.5 * u * math.log(r2) if r2 > 0 else 0.0) - u
    if y != 0:
        v += y * math.atan(u / y)
    return v


def plate_model(d, L=0.20, N=40):
    w = L / N
    S = [(-L / 2 + j * w, -L / 2 + (j + 1) * w, yp) for yp in (d / 2, -d / 2) for j in range(N)]
    m = len(S)
    M = [[-(_Fp(b - (S[i][0] + S[i][1]) / 2, S[i][2] - y) - _Fp(a - (S[i][0] + S[i][1]) / 2, S[i][2] - y)) for (a, b, y) in S]
         for i in range(m)]
    r = [0.5 if S[i][2] > 0 else -0.5 for i in range(m)]
    for c in range(m):
        pv = max(range(c, m), key=lambda k: abs(M[k][c]))
        M[c], M[pv] = M[pv], M[c]; r[c], r[pv] = r[pv], r[c]
        for k in range(c + 1, m):
            f = M[k][c] / M[c][c]
            if f:
                for j in range(c, m):
                    M[k][j] -= f * M[c][j]
                r[k] -= f * r[c]
    s = [0.0] * m
    for k in range(m - 1, -1, -1):
        s[k] = (r[k] - sum(M[k][j] * s[j] for j in range(k + 1, m))) / M[k][k]

    def E(x, y):
        ex = ey = 0.0
        for (a, b, yp), sj in zip(S, s):
            yy = y - yp
            if abs(yy) < 1e-12:
                yy = 1e-12
            ex += sj * 0.5 * math.log(((x - a) ** 2 + yy * yy) / ((x - b) ** 2 + yy * yy))
            ey += sj * (math.atan((b - x) / yy) - math.atan((a - x) / yy))
        return ex, ey
    return E


def plate_lines(E, d, count, L=0.20, xlim=0.15, ylim=0.085, ds=0.0006):
    out = []
    for i in range(count):
        x, y = -L / 2 + (i + 0.5) * L / count, d / 2 - 1e-4
        pts = [(x, y)]
        for k in range(1500):
            ex, ey = E(x, y); e = math.hypot(ex, ey)
            xm, ym = x + ex / e * ds / 2, y + ey / e * ds / 2
            ex, ey = E(xm, ym); e = math.hypot(ex, ey)
            x, y = x + ex / e * ds, y + ey / e * ds
            if abs(x) > xlim or abs(y) > ylim:
                break
            if y <= -d / 2 and abs(x) <= L / 2 + 0.002:
                pts.append((x, -d / 2)); break
            if k % 3 == 2:
                pts.append((x, y))
        out.append(pts)
    return out


# --- drawing pieces -------------------------------------------------------------------------------------------------
def polyline(f, pts, colour, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{colour}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}/>')


def head_on(f, pts, colour, s=11):
    """A filled arrowhead in the middle of a polyline, pointing along it."""
    i = len(pts) // 2
    (xa, ya), (xb, yb) = pts[i - 1], pts[i + 1]
    L = math.hypot(xb - xa, yb - ya) or 1
    ux, uy = (xb - xa) / L, (yb - ya) / L
    x, y = pts[i][0] + ux * s / 2, pts[i][1] + uy * s / 2
    f.path(f"M{n(x)},{n(y)} L{n(x - ux * s - uy * s * 0.45)},{n(y - uy * s + ux * s * 0.45)} "
           f"L{n(x - ux * s + uy * s * 0.45)},{n(y - uy * s - ux * s * 0.45)} Z", colour)


def charge(f, x, y, sign, r=12):
    """A small charged ball: light red with + or light blue with − (the sign drawn, not only the colour)."""
    f.circle(x, y, r, HOT_LIGHT if sign > 0 else COLD_LIGHT, INK, 2)
    f.line(x - r * 0.5, y, x + r * 0.5, y, INK, 2.5)
    if sign > 0:
        f.line(x, y - r * 0.5, x, y + r * 0.5, INK, 2.5)


def big_charge(f, x, y, sign, r=26):
    f.circle(x, y, r, HOT_LIGHT if sign > 0 else COLD_LIGHT, INK, 2.5)
    f.line(x - 11, y, x + 11, y, INK, 3.5)
    if sign > 0:
        f.line(x, y - 11, x, y + 11, INK, 3.5)


def plate(f, x0, x1, y, sign, marks=12, t=12):
    """A metal plate whose inner face is at y (sign +1: the upper plate, its body above y), with its charge signs."""
    ytop = y - t if sign > 0 else y
    f.rect(x0, ytop, x1 - x0, t, ALUMINIUM, METAL_EDGE, 2, 2)
    for i in range(marks):
        xc, yc = x0 + (i + 0.5) * (x1 - x0) / marks, ytop + t / 2
        f.line(xc - 3.5, yc, xc + 3.5, yc, INK, 2)
        if sign > 0:
            f.line(xc, yc - 3.5, xc, yc + 3.5, INK, 2)


def field_between(f, cx, cy, sc, d, count, ylim=0.085):
    """The plates' traced field lines in green with arrowheads; (cx, cy) is the middle of the gap, sc px per metre."""
    E = plate_model(d)
    for pts in plate_lines(E, d, count, ylim=ylim):
        P = [(cx + x * sc, cy - y * sc) for x, y in pts]
        polyline(f, P, FIELD, 2)
        if len(P) > 4:
            head_on(f, P, FIELD)


# --- Ydinajatus: the field strength at a point, a positive and a negative test charge -----------------------------
def testivaraus():
    f = Fig("fy611-test", 330, "Kaksi kaavakuvaa vierekkäin, ei mittakaavassa. Kummassakin vasemmalla on suuri positiivinen "
            "varaus Q ja sen oikealla puolella kohta P, johon on tuotu pieni testivaraus. Kohdan P sähkökentän vihreä "
            "nuoli E osoittaa kummassakin kuvassa oikealle, poispäin varauksesta Q. Vasemmassa kuvassa testivaraus on "
            "positiivinen, ja siihen kohdistuvan voiman punainen nuoli F osoittaa samaan suuntaan kuin kenttä. Oikeassa "
            "kuvassa testivaraus on negatiivinen, ja voiman nuoli osoittaa vastakkaiseen suuntaan, kohti varausta Q.")
    f.line(300, 20, 300, 310, RULE, 2, "6 6")
    for ox, sign, title in ((0, 1, r"\text{positiivinen } q"), (300, -1, r"\text{negatiivinen } q")):
        f.tex(ox + 150, 34, title, "middle", w=260)
        big_charge(f, ox + 62, 170, 1)
        f.tex(ox + 62, 222, "Q", "middle", w=30)
        px = ox + 180
        charge(f, px, 170, sign)
        f.tex(px, 206, r"P", "middle", w=30)
        f.arrow(px, 112, px + 86, 112, FIELD, 4, 16)
        f.tex(px + 50, 84, r"\overline{E}", "middle", FIELD, w=40)
        if sign > 0:
            f.arrow(px + 14, 170, px + 96, 170, FORCE, 4, 16)
            f.tex(px + 64, 142, r"\overline{F}", "middle", FORCE, w=40)
        else:
            f.arrow(px - 14, 170, px - 92, 170, FORCE, 4, 16)
            f.tex(px - 60, 142, r"\overline{F}", "middle", FORCE, w=40)
        f.tex(ox + 150, 280, r"\overline{F} = q\overline{E}", "middle", w=170)
    return f.svg()


# --- Ydinajatus: field lines of a point charge and of a pair of opposite charges ----------------------------------
def kenttaviivat():
    f = Fig("fy611-lines", 340, "Kaksi kenttäviivakuvaa vierekkäin, kaavakuva. Vasemmalla positiivinen pistevaraus, josta "
            "lähtee tasaisesti joka suuntaan kaksitoista vihreää suoraa kenttäviivaa nuolet ulospäin; viivat harvenevat "
            "kauempana varauksesta. Oikealla positiivinen ja yhtä suuri negatiivinen varaus vierekkäin. Kenttäviivat lähtevät "
            "positiivisesta varauksesta ja kaartuvat negatiiviseen varaukseen; viivat ovat tiheimmillään varausten "
            "lähellä ja niiden välissä. Viivat eivät leikkaa toisiaan.")
    f.line(250, 20, 250, 320, RULE, 2, "6 6")
    # a point charge
    cx, cy = 125, 165
    for k in range(12):
        a = k * math.pi / 6 + math.pi / 12
        c, s = math.cos(a), math.sin(a)
        P = [(cx + c * 32, cy + s * 32), (cx + c * 75, cy + s * 75), (cx + c * 108, cy + s * 108)]
        polyline(f, P, FIELD, 2)
        head_on(f, P, FIELD)
    big_charge(f, cx, cy, 1, 22)
    f.tex(cx, 312, r"+Q", "middle", w=60)
    # a pair +Q, -Q: field lines traced in the plane through them (point charges, E ~ r / r^3)
    qa, qb, y0 = (360, 165), (500, 165), 165
    def E(x, y):
        ex = ey = 0.0
        for (qx, qy), qq in ((qa, 1), (qb, -1)):
            dx, dy = x - qx, y - qy; r3 = (dx * dx + dy * dy) ** 1.5
            ex += qq * dx / r3; ey += qq * dy / r3
        return ex, ey
    for k in range(12):
        a = k * math.pi / 6 + math.pi / 12
        x, y = qa[0] + 24 * math.cos(a), qa[1] + 24 * math.sin(a)
        pts = [(x, y)]
        for _ in range(900):
            ex, ey = E(x, y); e = math.hypot(ex, ey)
            x, y = x + ex / e * 1.5, y + ey / e * 1.5
            if math.hypot(x - qb[0], y - qb[1]) < 24 or not (262 < x < 588 and 26 < y < 290):
                break
            pts.append((x, y))
        pts = pts[::4] + [pts[-1]]
        polyline(f, pts, FIELD, 2)
        if len(pts) > 6:
            head_on(f, pts, FIELD)
    big_charge(f, *qa, 1, 22)
    big_charge(f, *qb, -1, 22)
    f.tex(430, 312, r"+Q \text{ ja } -Q", "middle", w=170)
    return f.svg()


# --- Ydinajatus: the uniform field between two plates, the same force at two places --------------------------------
def levyt(points=False):
    if points:
        f = Fig("fy611-abc", 340, "Kaavakuva: kaksi vaakasuoraa yhdensuuntaista metallilevyä, ylempi positiivinen ja alempi "
                "negatiivinen. Levyjen väliin on piirretty vihreät kenttäviivat ylhäältä alas. Levyjen välissä viivat ovat "
                "suoria, yhdensuuntaisia ja yhtä tiheässä, mutta levyjen päissä ne kaartuvat ulospäin ja harvenevat. Kuvaan on "
                "merkitty kolme kohtaa: A on levyjen välissä keskellä, B levyjen välissä lähellä ylempää levyä ja vasemmalla "
                "keskikohdasta, ja C levyjen oikean pään ulkopuolella levyjen puolivälin korkeudella.")
    else:
        f = Fig("fy611-plates", 340, "Kaavakuva: kaksi vaakasuoraa yhdensuuntaista metallilevyä. Ylemmässä levyssä on "
                "positiivista ja alemmassa negatiivista varausta. Vihreät kenttäviivat kulkevat ylemmästä levystä alempaan. "
                "Levyjen välissä viivat ovat suoria, yhdensuuntaisia ja tasavälein, joten kenttä on homogeeninen. Levyjen päissä "
                "viivat kaartuvat ulospäin ja harvenevat. Levyjen välissä on kaksi samanlaista positiivista palloa eri kohdissa, "
                "ja kumpaankin kohdistuu yhtä suuri punainen voimanuoli F alaspäin, kentän suuntaan.")
    cx, cy, sc, d = 300, 172, 2000, 0.06
    field_between(f, cx, cy, sc, d, 12, ylim=0.08)
    top, bot = cy - d / 2 * sc, cy + d / 2 * sc
    plate(f, 100, 500, top, 1)
    plate(f, 100, 500, bot, -1)
    f.tex(86, top - 6, "+", "end", w=24)
    f.tex(86, bot + 6, "-", "end", w=24)
    if points:
        for (x, y, t, anchor) in ((300, cy, "A", "start"), (200, top + 22, "B", "start"), (556, cy, "C", "start")):
            f.circle(x, y, 7, INK, WHITE, 2)
            f.tex(x + 12, y - 16, t, anchor, w=28, bg=True)
    else:
        for x, y in ((212, cy - 34), (408, cy + 6)):
            charge(f, x, y, 1)
            f.arrow(x, y + 13, x, y + 54, FORCE, 4, 15)
            f.tex(x + 12, y + 38, r"\overline{F}", "start", FORCE, w=40, bg=True)
        f.tex(540, cy, r"\overline{E}", "start", FIELD, w=40)
    return f.svg()


# --- Kaava: E = U / d from the work done on a charge that crosses the gap -------------------------------------------
def tyo():
    f = Fig("fy611-work", 340, "Kaavakuva, ei mittakaavassa: jännitelähde U on kytketty johtimilla kahteen vaakasuoraan "
            "levyyn, plusnapa ylempään ja miinusnapa alempaan. Levyjen etäisyys on d. Levyjen välissä vihreät kenttäviivat "
            "osoittavat alas. Positiivinen varaus q lähtee ylemmän levyn luota ja kulkee katkoviivaa pitkin alemmalle levylle. "
            "Siihen kohdistuu koko matkan sama punainen voima F, joka on q kertaa E ja osoittaa alas. Kun varaus kulkee "
            "matkan d, kenttä tekee työn F kertaa d, joka on yhtä suuri kuin q kertaa U.")
    top, bot, x0, x1 = 90, 250, 200, 520
    for x in range(232, 520, 48):
        f.arrow(x, top + 6, x, bot - 6, FIELD, 2, 11)
    plate(f, x0, x1, top, 1, 10)
    plate(f, x0, x1, bot, -1, 10)
    # the source on the left: a cell symbol, + up
    xs = 92
    f.add(f'<polyline points="{x0},{top - 6} {xs},{top - 6} {xs},{163}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    f.add(f'<polyline points="{x0},{bot + 6} {xs},{bot + 6} {xs},{177}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    f.line(xs - 24, 163, xs + 24, 163, INK, 3)
    f.line(xs - 12, 177, xs + 12, 177, INK, 7)
    f.tex(xs - 34, 170, "U", "end", w=30)
    f.tex(xs + 30, 150, "+", "start", w=24)
    f.tex(xs + 30, 190, "-", "start", w=24)
    # the charge's path and the force on it
    xq = 330
    f.line(xq, top + 22, xq, bot - 10, MUTED, 2, "6 5")
    charge(f, xq, top + 30, 1)
    f.tex(xq - 20, top + 30, "q", "end", w=26, bg=True)
    f.arrow(xq, top + 44, xq, top + 104, FORCE, 4, 15)
    f.tex(xq + 12, top + 82, r"\overline{F} = q\overline{E}", "start", FORCE, w=130, bg=True)
    # the distance d
    xd = 552
    f.line(xd, top, xd, bot, INK, 2)
    f.line(xd - 8, top, xd + 8, top, INK, 2); f.line(xd - 8, bot, xd + 8, bot, INK, 2)
    f.tex(xd + 14, (top + bot) / 2, "d", "start", w=26)
    f.tex(360, 300, r"W = Fd = qEd = qU", "middle", w=300)
    return f.svg()


# --- Kaava: E along the midline, from the middle to past the end of the plates (the simulation's model) ------------
PROFILE_X = [0, 1, 2, 3, 4, 5, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13, 14]


def profiili():
    U, d = 2000.0, 0.04
    E = plate_model(d)
    pts = [(x, U * abs(E(x / 100, 0.0)[1]) / 1000) for x in PROFILE_X]
    f = Fig("fy611-profile", 340, "Kuvaaja mittakaavassa, laskettu simulaation levymallilla: sähkökentän voimakkuus E "
            "kilovoltteina metriä kohti levyjen puolivälin korkeudella kohdan x funktiona, kun jännite on 2,0 kV ja levyjen "
            "etäisyys 4,0 cm. Levyjen keskikohta on x = 0 ja levyn pää x = 10 cm. Välillä 0–7 cm kentän voimakkuus on vakio "
            "50 kV/m, joka on U jaettuna d:llä. Lähellä levyn päätä se alkaa pienetä, levyn päässä se on noin 38 kV/m ja "
            "levyjen ulkopuolella 14 cm:n kohdalla enää noin 9 kV/m.")
    ax = Axes(f, (96, 280), (484, 60), x=(0, 14), y=(0, 60), xticks=list(range(2, 15, 2)), yticks=[10, 20, 30, 40, 50, 60],
              xlabel=r"x\ (\text{cm})", ylabel=r"E\ (\text{kV/m})")
    f.line(ax.X(10), ax.Y(60), ax.X(10), ax.y0, MUTED, 1.5, "6 5")
    f.tex(ax.X(10) + 8, ax.Y(56), r"\text{levyn pää}", "start", MUTED, w=120, bg=True)
    f.line(ax.x0, ax.Y(50), ax.X(7), ax.Y(50), MUTED, 1.5, "6 5")
    ax.line(pts, FIELD, 3)
    f.tex(ax.X(2), ax.Y(50) - 22, r"E = \tfrac{U}{d}", "middle", FIELD, w=90, bg=True)
    return f.svg()


# --- Kaava: an electron entering the field: v blue, F red, a orange -------------------------------------------------
def elektroni():
    f = Fig("fy611-electron", 340, "Kaavakuva, ei mittakaavassa: kaksi vaakasuoraa levyä, ylempi positiivinen ja alempi "
            "negatiivinen; vihreät kenttäviivat osoittavat alas. Elektroni tulee vasemmalta levyjen väliin vaakasuorassa, ja "
            "sen sininen nopeusnuoli v osoittaa oikealle. Levyjen välissä elektronin rata kaartuu tasaisesti ylöspäin kohti "
            "positiivista levyä. Radan kohdassa on punainen voimanuoli F ja oranssi kiihtyvyysnuoli a, jotka molemmat "
            "osoittavat ylös, kenttää vastaan.")
    top, bot, x0, x1, ym = 96, 256, 150, 530, 196
    for x in range(176, 530, 56):
        f.arrow(x, top + 6, x, bot - 6, FIELD, 2, 11)
    plate(f, x0, x1, top, 1, 12)
    plate(f, x0, x1, bot, -1, 12)
    f.tex(x1 + 26, top + 40, r"\overline{E}", "start", FIELD, w=40)
    # the path: straight before the plates, a parabola between them, straight after
    path = [(40, ym), (x0, ym)]
    for k in range(1, 21):
        x = x0 + (x1 - x0) * k / 20
        path.append((x, ym - 70 * (k / 20) ** 2))
    path.append((x1 + 50, ym - 70 - 70 * 2 * 50 / (x1 - x0)))
    polyline(f, path, MUTED, 2, "6 5")
    charge(f, 60, ym, -1)
    f.arrow(76, ym, 140, ym, VEL, 4, 15)
    f.tex(108, ym + 26, r"\overline{v}", "middle", VEL, w=36)
    xe = 320; ye = ym - 70 * ((xe - x0) / (x1 - x0)) ** 2
    charge(f, xe, ye, -1)
    f.arrow(xe - 8, ye - 14, xe - 8, ye - 60, FORCE, 4, 15)
    f.tex(xe - 18, ye - 46, r"\overline{F}", "end", FORCE, w=40, bg=True)
    f.arrow(xe + 10, ye - 14, xe + 10, ye - 50, ACC, 4, 15)
    f.tex(xe + 20, ye - 40, r"\overline{a}", "start", ACC, w=36, bg=True)
    f.tex(60, ym + 34, r"-e", "middle", w=40)
    return f.svg()


# --- task figure (L1-05): the force on a ball for four charges at the same point ------------------------------------
FQ_PTS = [(1.0, 31.0), (2.0, 59.0), (3.0, 91.0), (4.0, 119.0)]          # answers.py fy6-11-L1-05


def fq_graph():
    f = Fig("fy611-fq", 340, "Kuvaaja mittakaavassa: pieneen palloon kohdistuva sähköinen voima F mikronewtoneina pallon "
            "varauksen q funktiona nanocoulombeina, kun pallo on aina samassa kohdassa kahden levyn välissä. Ruudukon väli on "
            "0,5 nC ja 10 µN. Mittauspisteet ovat (1,0 nC; 31 µN), (2,0 nC; 59 µN), (3,0 nC; 91 µN) ja (4,0 nC; 119 µN). "
            "Pisteisiin on sovitettu origon kautta kulkeva suora, joka on piirretty varaukseen 4,5 nC asti.")
    ax = Axes(f, (96, 290), (484, 66), x=(0, 4.5), y=(0, 140), xticks=[0.5 * k for k in range(1, 10)],
              yticks=list(range(10, 141, 10)), xlabel=r"q\ (\text{nC})", ylabel=r"F\ (\mu\text{N})",
              xfmt=lambda v: fi(v, 0) if round(v * 2) % 2 == 0 else "", yfmt=lambda v: fi(v, 0) if v % 20 == 0 else "")
    ax.line([(0, 0), (4.5, 135)], FORCE, 3)
    for q, F in FQ_PTS:
        ax.point(q, F, INK, 6)
    return f.svg()


# --- opening illustration: an air purifier draws dust out of a sunbeam ----------------------------------------------
def hero():
    f = H.hero("fy611-hero", "Kuvitus: aurinkoinen olohuone. Vasemmalla ikkunasta tulee vino auringonsäde, jossa leijuu "
               "pölyhiukkasia. Keskellä lattialla seisoo valkoinen pylvään muotoinen ilmanpuhdistin, jonka kyljessä on "
               "ritilä. Pölyhiukkaset kulkevat kaarevina jonoina säteestä puhdistimen ritilää kohti. Oikealla on sininen "
               "sohva ja ruukkukasvi.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy611h-wall", "#f6f1e6", "#f1dfb5", y1=0, y2=470))
    f.rect(0, 470, 1200, 130, H.grad(f, "fy611h-floor", SAND_DARK, "#d9b26a", y1=470, y2=600))
    for k in range(9):                                                                          # floor boards
        f.line(k * 150 + 40, 470, k * 150 - 30, 600, "#a97a35", 1.5)
    f.line(0, 470, 1200, 470, "#a97a35", 3)
    # the window and its light
    f.rect(70, 70, 260, 250, "#a5d8ff", INK, 4, 4)
    f.line(200, 70, 200, 320, WHITE, 8); f.line(70, 195, 330, 195, WHITE, 8)
    f.rect(70, 70, 260, 250, "none", INK, 4, 4)
    f.rect(52, 318, 296, 16, WHITE, INK, 2.5, 3)
    beam = H.grad(f, "fy611h-beam", "#ffc078", "#f6f1e6", horizontal=True)
    f.add(f'<path d="M110,330 L330,320 L760,600 L360,600 Z" fill="{beam}" fill-opacity="0.45"/>')
    # dust specks in the beam and drifting to the purifier's grille
    for k in range(46):
        t = H.rnd(k, 5)
        x = 200 + 400 * t + 60 * H.rnd(k + 90, 5); y = 360 + 200 * t * H.rnd(k + 40, 5) + 30 * H.rnd(k + 70, 5)
        f.circle(x, y, 2.5 + 2 * H.rnd(k + 200, 5), "#a97a35")
    for row, (ya, yb) in enumerate(((300, 250), (380, 320), (450, 390))):
        for k in range(7):
            s = k / 6
            x = 470 + 140 * s; y = ya + (yb - ya) * s * s
            f.circle(x, y, 3.2 - 1.2 * s, "#a97a35")
    # the purifier: a white tower with a grille and a blue ring
    px = 650
    f.rect(px - 10, 456, 160, 22, "#6b7480", None, 2, 8)
    f.rect(px, 170, 140, 296, H.grad(f, "fy611h-tower", WHITE, "#c4ccd4", horizontal=True), INK, 3, 26)
    for y in range(214, 430, 18):
        f.line(px + 22, y, px + 118, y, "#6b7480", 4, cap="round")
    f.rect(px + 30, 184, 80, 12, "#d0e6fb", "#1971c2", 2.5, 6)
    # sofa and a plant on the right
    f.rect(880, 330, 300, 140, "#1971c2", INK, 3, 22)
    f.rect(880, 280, 300, 90, "#d0e6fb", INK, 3, 22)
    f.rect(860, 340, 50, 130, "#1971c2", INK, 3, 16); f.rect(1150, 340, 50, 130, "#1971c2", INK, 3, 16)
    f.path("M800,470 L790,400 L860,400 L850,470 Z", "#b8622d", INK, 3)
    for k in range(7):
        a = -math.pi / 2 + (k - 3) * 0.32
        f.path(f"M825,400 Q{n(825 + 60 * math.cos(a) - 20)},{n(400 + 70 * math.sin(a))} {n(825 + 110 * math.cos(a))},{n(400 + 120 * math.sin(a))} "
               f"Q{n(825 + 50 * math.cos(a) + 20)},{n(400 + 50 * math.sin(a))} 825,400 Z", "#2b8a3e", INK, 2)
    return f.svg()


# --- Voimakuvion valinta (task fy6-11-L2-08, docs/exercise-types.md type 3) ---------------------------------------
# A small negatively charged bead (m = 0,10 g, q = -20 nC) moves to the right between horizontal plates, the positive
# plate below, so the field E = 1,0e5 N/C points up and the electric force F_s = |q| E = 2,0 mN points down, against the
# field; its weight G = 0,98 mN also points down. Four option diagrams to one scale (50 units per millinewton); only
# "pick-alas" is right, each other has one error. Air resistance is neglected in the task.
PK_G, PK_FS, PK_S = 0.10e-3 * 9.81 * 1e3, 20e-9 * 1.0e5 * 1e3, 50.0       # mN, mN, figure units per mN
PK_BODY = (150, 165, 104, 36)
PK_DESC = "Voimakuvio mittakaavassa: varattu helmi suorakulmiona. Keskipisteestä alaspäin osoittaa paino G. "


def _pick(name, desc, fs_up=False, weight=True, v_force=False, wrong=None):
    """An option of task fy6-11-L2-08: G from the centre; the electric force F_s from a point left of the centre, down
    (right: against the upward field, the bead is negative) or, as an error, up along the field; weight=False leaves the
    weight out (as if it were negligible like an electron's); v_force draws the velocity into the diagram as if it were a
    force (in velocity blue, fy5-4 and fy4-5 style)."""
    cx, cy, w, h = PK_BODY
    f = Fig(f"fy611-pick-{name}", 320, desc, width=300)
    d = FBD(f, PK_S, body=PK_BODY, a_dir=None if wrong else (0, -1), wrong=wrong)
    if weight:
        d.force("G", (0, -PK_G), (cx, cy), "gravity", lab=(22, -4))
    d.force("F_s", (0, PK_FS if fs_up else -PK_FS), (cx - 34, cy), "electric", tex=r"\overline{F}_\text{s}",
            lab=(-30, 10 if fs_up else -10))
    d.draw()
    if v_force:                                                    # the error: the velocity drawn into the force diagram
        x1, y = cx + w / 2, cy                                     # like a force, but in velocity blue (it is no force)
        f.arrow(x1, y, x1 + PK_G * PK_S, y, VELOCITY, 4, 18)
        f.tex(x1 + PK_G * PK_S - 10, y - 26, r"\overline{v}", "middle", VELOCITY)
    return f.svg()


def pick_alas():
    return _pick("alas", PK_DESC + "Keskipisteen vasemmalta puolelta lähtee sähköinen voima F s suoraan alaspäin; sen nuoli "
                 "on kaksi kertaa niin pitkä kuin painon nuoli.")


def pick_ylos():
    return _pick("ylos", PK_DESC + "Keskipisteen vasemmalta puolelta lähtee sähköinen voima F s suoraan ylöspäin; sen nuoli "
                 "on kaksi kertaa niin pitkä kuin painon nuoli.", fs_up=True,
                 wrong="the electric force drawn along the field: the bead is negative, so the force points against E, down")


def pick_nopeus():
    return _pick("nopeus", PK_DESC + "Keskipisteen vasemmalta puolelta lähtee sähköinen voima F s suoraan alaspäin; sen nuoli "
                 "on kaksi kertaa niin pitkä kuin painon nuoli. Oikeasta kyljestä lähtee sininen nopeuden nuoli v "
                 "vaakasuoraan oikealle, yhtä pitkänä kuin painon nuoli.", v_force=True,
                 wrong="the velocity v drawn as a force")


def pick_ilman():
    return _pick("ilman", "Voimakuvio mittakaavassa: varattu helmi suorakulmiona. Keskipisteen vasemmalta puolelta lähtee "
                 "sähköinen voima F s suoraan alaspäin; sen nuoli on yhtä pitkä kuin muiden kuvioiden sähköisen voiman "
                 "nuoli eli kaksi kertaa niin pitkä kuin niiden painon nuoli. Painoa ei ole piirretty.",
                 weight=False,
                 wrong="the weight left out as for an electron, although here G = 0,98 mN is half the electric force 2,0 mN")


FIGURES = {"hero": hero, "test": testivaraus, "lines": kenttaviivat, "plates": levyt, "work": tyo, "profile": profiili,
           "electron": elektroni, "abc": lambda: levyt(points=True), "fq-graph": fq_graph,
           "pick-alas": pick_alas, "pick-ylos": pick_ylos, "pick-nopeus": pick_nopeus, "pick-ilman": pick_ilman}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "test": "reveals: the force on a positive test charge is along E, on a negative one opposite (F = qE)",
    "lines": "reveals: the field-line pictures of a point charge and of a +Q/-Q pair (a theory figure)",
    "plates": "reveals: the field between parallel plates is uniform: the same force on equal charges at two places",
    "work": "reveals: E = U / d from W = F d = q U (a theory figure)",
    "profile": "reveals: E = U / d = 50 kV/m on the midline up to about 7 cm, about 38 kV/m at the end of the plate, small outside",
    "electron": "reveals: an electron's force and acceleration point against E, towards the + plate; its path bends",
    "abc": "safe: plates with traced field lines and three marked points A (middle), B (near the + plate), C (outside the end)",
    "fq-graph": "safe: four (q, F) points at one place between plates and a fitted line through the origin, no slope written",
    "pick-alas": "reveals: the right option of task fy6-11-L2-08 (a negative bead in an upward field: G and F_s both down)",
    "pick-ylos": "safe: a wrong option of task fy6-11-L2-08 (the electric force on a negative bead drawn along the field)",
    "pick-nopeus": "safe: a wrong option of task fy6-11-L2-08 (the velocity, a blue arrow, drawn into the force diagram as if it were a force)",
    "pick-ilman": "safe: a wrong option of task fy6-11-L2-08 (the weight left out although it is half the electric force)",
}
