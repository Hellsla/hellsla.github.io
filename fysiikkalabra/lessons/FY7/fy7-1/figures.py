"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-1` writes them into lesson.md.
Colours (FY7): magnetic field lines and B arrows GOOD #2b8a3e, N pole HOT_LIGHT #f2a69c labelled N, S pole COLD_LIGHT
#d0e6fb labelled S; a compass needle's N half is arrow-shaped (shape and label, never colour alone)."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER, WATER_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN,
                    HOT_LIGHT, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, GOOD, GOOD_LIGHT, ICE, n)
import herolib as H

NPOLE, SPOLE, FIELD = HOT_LIGHT, COLD_LIGHT, GOOD


# --- field lines of magnetic poles (each pole's field ∝ q (P − pole) / d³ in the drawing plane) ---
def field_at(poles, x, y):
    bx = by = 0.0
    for px, py, q in poles:
        dx, dy = x - px, y - py
        d3 = max(math.hypot(dx, dy), 1.0) ** 3
        bx += q * dx / d3; by += q * dy / d3
    return bx, by


def trace(poles, x, y, stop, box=(14, 14, 586, 366), step=2.0, nmax=3000):
    """A field line from (x, y) along the field until stop(x, y) is true or the line leaves the box."""
    pts = [(x, y)]
    for _ in range(nmax):
        bx, by = field_at(poles, x, y); b = math.hypot(bx, by)
        if b == 0: break
        # midpoint step for a smooth line
        mx, my = x + bx / b * step / 2, y + by / b * step / 2
        bx, by = field_at(poles, mx, my); b = math.hypot(bx, by)
        x, y = x + bx / b * step, y + by / b * step
        if not (box[0] <= x <= box[2] and box[1] <= y <= box[3]):
            break
        pts.append((x, y))
        if stop(x, y): break
    return pts


def polyline(f, pts, color=FIELD, w=2):
    f.add(f'<polyline points="{" ".join(f"{n(a)},{n(b)}" for a, b in pts)}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def head_on(f, pts, frac=0.5, color=FIELD, size=12):
    """A filled arrowhead on a polyline at the fraction frac of its length, pointing along the line."""
    if len(pts) < 4: return
    L = [0.0]
    for a, b in zip(pts, pts[1:]): L.append(L[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    target = L[-1] * frac
    i = next(k for k in range(1, len(L)) if L[k] >= target)
    (x0, y0), (x1, y1) = pts[i - 1], pts[min(i + 2, len(pts) - 1)]
    a = math.atan2(y1 - y0, x1 - x0); tx, ty = pts[i]
    tx, ty = tx + math.cos(a) * size / 2, ty + math.sin(a) * size / 2
    hw = size * 0.45
    bx, by = tx - math.cos(a) * size, ty - math.sin(a) * size
    f.path(f"M{n(tx)},{n(ty)} L{n(bx - math.sin(a) * hw)},{n(by + math.cos(a) * hw)} L{n(bx + math.sin(a) * hw)},{n(by - math.cos(a) * hw)} Z", color)


def bar(f, x0, y0, w, h, n_right=True, labels=True, plain=False):
    """A bar magnet: the N half HOT_LIGHT and the S half COLD_LIGHT with their letters; plain draws it unmarked grey."""
    cx = x0 + w / 2
    if plain:
        f.rect(x0, y0, w, h, ALUMINIUM, INK, 2.5, 5)
        f.line(cx, y0, cx, y0 + h, METAL_EDGE, 1.5, "4 4")
        return
    left, right = (SPOLE, NPOLE) if n_right else (NPOLE, SPOLE)
    f.path(f"M{n(x0 + 5)},{n(y0)} H{n(cx)} V{n(y0 + h)} H{n(x0 + 5)} Q{n(x0)},{n(y0 + h)} {n(x0)},{n(y0 + h - 5)} V{n(y0 + 5)} Q{n(x0)},{n(y0)} {n(x0 + 5)},{n(y0)} Z", left)
    f.path(f"M{n(cx)},{n(y0)} H{n(x0 + w - 5)} Q{n(x0 + w)},{n(y0)} {n(x0 + w)},{n(y0 + 5)} V{n(y0 + h - 5)} Q{n(x0 + w)},{n(y0 + h)} {n(x0 + w - 5)},{n(y0 + h)} H{n(cx)} Z", right)
    f.rect(x0, y0, w, h, "none", INK, 2.5, 5)
    f.line(cx, y0, cx, y0 + h, INK, 1.5)
    if labels:
        f.tex(x0 + w / 4, y0 + h / 2, r"\text{S}" if n_right else r"\text{N}", "middle")
        f.tex(x0 + 3 * w / 4, y0 + h / 2, r"\text{N}" if n_right else r"\text{S}", "middle")


def compass(f, cx, cy, ang, r=18):
    """A small compass; ang is the needle's N end direction in radians on the drawing (0 = right, counterclockwise up)."""
    f.circle(cx, cy, r, WHITE, INK, 2)
    ux, uy = math.cos(ang), -math.sin(ang); nx, ny = -uy, ux
    L, w = r - 3, 4.5
    f.path(f"M{n(cx + ux * L)},{n(cy + uy * L)} L{n(cx + nx * w)},{n(cy + ny * w)} L{n(cx - nx * w)},{n(cy - ny * w)} Z", NPOLE, INK, 1.2)
    f.path(f"M{n(cx + nx * w)},{n(cy + ny * w)} L{n(cx - ux * L * 0.8 + nx * w * 0.5)},{n(cy - uy * L * 0.8 + ny * w * 0.5)} "
           f"L{n(cx - ux * L * 0.8 - nx * w * 0.5)},{n(cy - uy * L * 0.8 - ny * w * 0.5)} L{n(cx - nx * w)},{n(cy - ny * w)} Z", SPOLE, INK, 1.2)
    f.circle(cx, cy, 2.2, INK)


def bar_field():
    f = Fig("fy71-bar", 380, "Periaatekuva sauvamagneetin magneettikentästä ylhäältä nähtynä. Vihreät kenttäviivat lähtevät "
            "magneetin pohjoisnavasta N, kaartuvat magneetin ympäri ja palaavat etelänapaan S; magneetin sisällä viivat "
            "jatkuvat etelänavasta pohjoisnapaan, joten jokainen viiva on suljettu silmukka. Nuolenkärjet näyttävät kentän "
            "suunnan. Neljä kompassia magneetin ympärillä kääntyy kenttäviivojen suuntaisiksi: kompassin pohjoispää osoittaa "
            "kentän suuntaan. Navoilla viivat ovat tiheimmillään, joten kenttä on siellä voimakkain.")
    cx, cy, hw, hh = 300, 190, 80, 20
    poles = [(cx + 62, cy, 1), (cx - 62, cy, -1)]
    inside = lambda x, y: cx - hw <= x <= cx + hw and cy - hh <= y <= cy + hh
    for deg in (12, 30, 50, 72, 98, 128):
        for sg in (1, -1):
            a = math.radians(deg) * sg
            x, y = cx + 62 + 26 * math.cos(a), cy - 26 * math.sin(a)
            pts = trace(poles, x, y, inside)
            polyline(f, pts)
            if inside(*pts[-1]) or math.hypot(pts[-1][0] - (cx - 62), pts[-1][1] - cy) < 30:
                head_on(f, pts, 0.5)
            else:                                            # a line that leaves the figure: its mirror image comes into S
                head_on(f, pts, 0.6)
                mirror = [(2 * cx - px, py) for px, py in reversed(pts)]
                polyline(f, mirror); head_on(f, mirror, 0.4)
    for pts in ([(cx + hw, cy), (586, cy)], [(14, cy), (cx - hw, cy)]):   # the axis
        polyline(f, pts); head_on(f, pts, 0.55 if pts[0][0] > cx else 0.45)
    bar(f, cx - hw, cy - hh, 2 * hw, 2 * hh)
    for dy in (-11, 11):                                     # inside the magnet: from S to N
        f.line(cx - hw + 10, cy + dy, cx + hw - 14, cy + dy, FIELD, 1.5, "5 4")
        f.path(f"M{cx + hw - 6},{cy + dy} l-9,-4.5 v9 Z", FIELD)
    for X, Y in ((480, 190), (120, 112), (300, 82), (300, 300)):
        bx, by = field_at(poles, X, Y)
        compass(f, X, Y, math.atan2(-by, bx))
    return f.svg()


def two_magnets():
    """Task figure: two unmarked bar magnets end to end with like poles facing; their field lines bend away from each
    other and leave an empty point midway. No letters, no arrows: the student decides which poles face."""
    f = Fig("fy71-two", 300, "Periaatekuva: kaksi merkitsemätöntä harmaata sauvamagneettia samalla suoralla päät vastakkain, "
            "välissä rako. Vihreät kenttäviivat lähtevät kummankin magneetin raon puoleisesta päästä, kaartuvat poispäin "
            "toisistaan ylös ja alas eivätkä kulje magneetista toiseen. Raon keskelle jää kohta, jonka kautta ei kulje "
            "yhtään viivaa. Viivoissa ei ole suuntanuolia.")
    cy, hh = 150, 18
    A, B = (60, 230), (370, 540)
    poles = [(A[0] + 18, cy, -1), (A[1] - 18, cy, 1), (B[0] + 18, cy, 1), (B[1] - 18, cy, -1)]
    inside = lambda x, y: (A[0] <= x <= A[1] or B[0] <= x <= B[1]) and cy - hh <= y <= cy + hh
    box = (14, 14, 586, 286)
    for px, sgn in ((A[1] - 18, 1), (B[0] + 18, -1)):
        for deg in (-75, -50, -25, 25, 50, 75):
            a = math.radians(deg)
            x, y = px + sgn * (20 + 4 * math.cos(a)), cy - (hh - 2) * math.sin(a)
            polyline(f, trace(poles, x, y, inside, box))
        polyline(f, trace(poles, px + sgn * 20, cy - 1.5, inside, box))
        polyline(f, trace(poles, px + sgn * 20, cy + 1.5, inside, box))
    bar(f, A[0], cy - hh, A[1] - A[0], 2 * hh, plain=True)
    bar(f, B[0], cy - hh, B[1] - B[0], 2 * hh, plain=True)
    return f.svg()


def cut_magnet():
    f = Fig("fy71-cut", 300, "Periaatekuva: sauvamagneetti katkaistaan ensin kahtia ja sitten neljään osaan. Jokaisessa palassa "
            "on edelleen sekä pohjoisnapa N että etelänapa S samassa järjestyksessä kuin alkuperäisessä magneetissa. "
            "Erillistä yksittäistä napaa ei synny.")
    rows = [(50, [(110, 380)]), (150, [(110, 180), (310, 180)]), (250, [(110, 80), (210, 80), (310, 80), (410, 80)])]
    for k, (y, pieces) in enumerate(rows):
        for x0, w in pieces:
            bar(f, x0, y - 22, w, 44)
        f.tex(70, y, ["1", "2", "4"][k], "end", MUTED)
        if k < 2:
            f.line(300, y + 30, 300, y + 70, MUTED, 1.5, "5 4")
    return f.svg()


def domains():
    f = Fig("fy71-dom", 340, "Periaatekuva, ei mittakaavassa: rautakappaleen alkeisalueet. Vasemmalla magnetoimaton rauta, jonka "
            "alkeisalueiden magneettiset suunnat, valkoiset nuolet, osoittavat eri suuntiin, joten niiden vaikutukset "
            "kumoavat toisensa. Oikealla rautakappaleen viereen on tuotu magneetti pohjoisnapa N edellä. Magneetin kenttä "
            "kääntää alkeisalueet ja kasvattaa niitä, joilla on kentän suunta, joten lähes kaikki nuolet osoittavat "
            "magneetista poispäin. Rauta on magnetoitunut: sen magneetin puoleinen pää on etelänapa S, ja magneetti vetää sitä.")
    f.tex(150, 26, r"\text{magnetoimaton rauta}", "middle", w=260)
    f.tex(450, 26, r"\text{magnetoitu rauta}", "middle", w=240)
    f.line(300, 14, 300, 326, RULE, 2, "6 6")
    random_dirs = [200, 70, 320, 135, 15, 250, 290, 100, 175, 40, 230, 340]
    aligned = [0, 8, -6, 0, 4, 0, -10, 0, 6, 0, -4, 0]

    def block(x0, dirs, w=220):
        y0, h = 70, 200
        f.rect(x0, y0, w, h, IRON, INK, 3, 8)
        cols, rows = 4, 3
        cw, ch = w / cols, h / rows
        for i in range(1, cols):
            xs = x0 + i * cw
            f.path(f"M{n(xs + 6)},{y0 + 2} L{n(xs - 8)},{n(y0 + h * 0.36)} L{n(xs + 7)},{n(y0 + h * 0.7)} L{n(xs - 3)},{y0 + h - 2}", stroke=ALUMINIUM, w=1.5)
        for j in range(1, rows):
            ys = y0 + j * ch
            f.path(f"M{x0 + 2},{n(ys - 4)} L{n(x0 + w * 0.4)},{n(ys + 7)} L{n(x0 + w * 0.7)},{n(ys - 6)} L{x0 + w - 2},{n(ys + 3)}", stroke=ALUMINIUM, w=1.5)
        for k, d in enumerate(dirs):
            i, j = k % cols, k // cols
            mx, my = x0 + (i + 0.5) * cw, y0 + (j + 0.5) * ch
            a = math.radians(d); ux, uy = math.cos(a), -math.sin(a)
            f.block_arrow(mx - ux * 18, my - uy * 18, mx + ux * 18, my + uy * 18, WHITE, 6, 16, 12)
    block(40, random_dirs)
    bar(f, 312, 148, 64, 44, n_right=True)
    block(386, aligned, w=194)
    f.tex(400, 296, r"\text{S}", "middle")
    f.tex(566, 296, r"\text{N}", "middle")
    return f.svg()


def earth_field():
    f = Fig("fy71-earth", 380, "Periaatekuva, ei mittakaavassa: Maa ja sen magneettikenttä. Maan sisään on piirretty kuviteltu "
            "sauvamagneetti, joka on noin kymmenen astetta kallellaan pyörimisakseliin nähden. Sen etelänapa S on "
            "maantieteellisen pohjoisnavan lähellä ja pohjoisnapa N maantieteellisen etelänavan lähellä. Vihreät kenttäviivat "
            "lähtevät eteläiseltä pallonpuoliskolta ja kaartuvat avaruuden kautta pohjoiselle pallonpuoliskolle. Pohjoisella "
            "pallonpuoliskolla oleva kompassi osoittaa pohjoiseen ja viivat painuvat siellä jyrkästi maahan.")
    cx, cy, R = 300, 192, 104
    tilt = math.radians(10)

    def rot(x, y):                         # magnetic frame (y up along the magnetic axis) to the drawing
        return cx + x * math.cos(tilt) + y * math.sin(tilt), cy - (-x * math.sin(tilt) + y * math.cos(tilt))
    # the planet: ocean and simple continents
    f.circle(cx, cy, R, WATER_LIGHT)
    f.path(f"M{cx - 30},{cy - 96} q40,-8 70,10 q22,22 6,46 q-26,10 -36,34 q-20,8 -40,-10 q-26,-24 -24,-50 q4,-22 24,-30 Z", SAND_LIGHT, GRAIN, 1.5)
    f.path(f"M{cx + 10},{cy + 20} q30,4 40,30 q2,30 -20,48 q-22,6 -30,-20 q-10,-30 10,-58 Z", SAND_LIGHT, GRAIN, 1.5)
    f.circle(cx, cy, R, "none", INK, 3)
    # field lines r = L R sin²θ outside the planet, both sides of the magnetic axis
    for L in (1.3, 1.65, 2.2):
        th0 = math.asin(math.sqrt(1 / L))
        for side in (1, -1):
            pts = []
            for i in range(121):
                th = th0 + (math.pi - 2 * th0) * i / 120
                r = L * R * math.sin(th) ** 2
                pts.append(rot(side * r * math.sin(th), r * math.cos(th)))
            pts = [q for q in pts if 14 <= q[0] <= 586 and 14 <= q[1] <= 366]
            pts.reverse()                  # from the southern hemisphere to the northern: the field's direction
            polyline(f, pts)
            head_on(f, pts, 0.5)
    # the imagined magnet inside: S towards geographic north
    m = [rot(-13, 58), rot(13, 58), rot(13, -58), rot(-13, -58)]
    mid_l, mid_r = rot(-13, 0), rot(13, 0)
    f.path(f"M{n(m[0][0])},{n(m[0][1])} L{n(m[1][0])},{n(m[1][1])} L{n(mid_r[0])},{n(mid_r[1])} L{n(mid_l[0])},{n(mid_l[1])} Z", SPOLE, INK, 2)
    f.path(f"M{n(mid_l[0])},{n(mid_l[1])} L{n(mid_r[0])},{n(mid_r[1])} L{n(m[2][0])},{n(m[2][1])} L{n(m[3][0])},{n(m[3][1])} Z", NPOLE, INK, 2)
    s_at, n_at = rot(0, 30), rot(0, -30)
    f.tex(s_at[0], s_at[1], r"\text{S}", "middle")
    f.tex(n_at[0], n_at[1], r"\text{N}", "middle")
    # geographic axis
    f.line(cx, cy - R - 34, cx, cy + R + 34, INK, 2, "8 6")
    f.tex(cx, 30, r"\text{maantieteellinen pohjoisnapa}", "middle", w=340)
    f.tex(cx, 352, r"\text{maantieteellinen etelänapa}", "middle", w=320)
    # a compass in the north (about 62° N): the needle along the local field, towards the north
    lat = math.radians(62)
    px, py = cx + (R + 17) * math.cos(lat), cy - (R + 17) * math.sin(lat)
    # local field direction from the dipole in the magnetic frame
    X, Y = px - cx, cy - py
    xm, ym = X * math.cos(tilt) - Y * math.sin(tilt), X * math.sin(tilt) + Y * math.cos(tilt)
    r = math.hypot(xm, ym); c, s = ym / r, xm / r     # θ from the magnetic axis
    # B ∝ (2 cosθ r̂ + sinθ θ̂) with the moment pointing down (towards geographic south): reverse
    br, bt = -2 * c, -s
    bxm = br * s + bt * c; bym = br * c - bt * s
    bx, by = bxm * math.cos(tilt) + bym * math.sin(tilt), -bxm * math.sin(tilt) + bym * math.cos(tilt)
    compass(f, px, py, math.atan2(by, bx), 15)
    return f.svg()


def vector_sum():
    f = Fig("fy71-sum", 350, "Kaavakuva mittakaavassa, ylhäältä nähtynä: kompassin kohdalla Maan magneettikentän vaakakomponentti "
            "B_h = 14 µT osoittaa pohjoiseen eli ylöspäin ja magneetin kenttä B_m = 20 µT itään eli oikealle, kohti "
            "oikealla olevan magneetin etelänapaa S. Kenttien summa B on suorakulmion lävistäjä, ja kompassin neula "
            "kääntyy sen suuntaiseksi kulman θ verran pohjoisesta itään.")
    ox, oy, k = 150, 280, 7.0
    bh, bm = 14 * k, 20 * k
    f.line(ox, oy - bh, ox + bm, oy - bh, MUTED, 1.5, "6 5")
    f.line(ox + bm, oy, ox + bm, oy - bh, MUTED, 1.5, "6 5")
    f.arrow(ox, oy, ox, oy - bh, FIELD, 3, 15)
    f.arrow(ox, oy, ox + bm, oy, FIELD, 3, 15)
    f.arrow(ox, oy, ox + bm, oy - bh, FIELD, 4, 17)
    ang = math.atan2(bh, bm)
    compass(f, ox, oy, ang, 28)
    # θ between north and B
    rr = 62
    f.path(f"M{ox},{oy - rr} A{rr},{rr} 0 0 1 {n(ox + rr * math.cos(ang))},{n(oy - rr * math.sin(ang))}", stroke=INK, w=1.5)
    f.tex(ox + 30, oy - 82, r"\theta", "middle")
    f.tex(ox - 12, oy - bh / 2, r"\overline{B}_\text{h}", "end")
    f.tex(ox + bm / 2 + 20, oy + 22, r"\overline{B}_\text{m}", "middle")
    f.tex(ox + bm + 12, oy - bh - 16, r"\overline{B}", "start")
    bar(f, 380, oy - 20, 150, 40, n_right=True)
    # north
    f.arrow(560, 130, 560, 60, INK, 2.5, 14)
    f.tex(586, 34, r"\text{pohjoinen}", "end", w=130)
    return f.svg()


def inclination():
    f = Fig("fy71-incl", 340, "Kaavakuva mittakaavassa, sivulta nähtynä: Etelä-Suomessa Maan magneettikenttä B = 52 µT osoittaa "
            "pohjoiseen ja 74 astetta vaakatason alapuolelle. Kentän vaakakomponentti B_h on noin 14 µT ja pystykomponentti "
            "B_v noin 50 µT. Kompassi kääntyy vain vaakakomponentin mukaan.")
    f.defs_add(f'<linearGradient id="fy71-soil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    gy = 92
    f.rect(14, gy, 572, 234, "url(#fy71-soil)")
    f.line(14, gy, 586, gy, INK, 2.5)
    f.tex(586, gy - 22, r"\text{maanpinta}", "end", MUTED, w=130)
    ox, k = 200, 4.2
    I = math.radians(74)
    B = 52 * k
    ex, ey = ox + B * math.cos(I), gy + B * math.sin(I)
    f.line(ex, gy, ex, ey, MUTED, 1.5, "6 5")
    f.line(ox, ey, ex, ey, MUTED, 1.5, "6 5")
    f.arrow(ox, gy, ex, gy, FIELD, 3, 13)
    f.arrow(ox, gy, ox, ey, FIELD, 3, 15)
    f.arrow(ox, gy, ex, ey, FIELD, 4, 17)
    rr = 44
    f.path(f"M{ox + rr},{gy} A{rr},{rr} 0 0 1 {n(ox + rr * math.cos(I))},{n(gy + rr * math.sin(I))}", stroke=INK, w=1.5)
    f.tex(ox + 44, gy + 30, "I", "start")
    f.tex(ox + 30, gy - 22, r"\overline{B}_\text{h}", "middle")
    f.tex(ox - 12, gy + 120, r"\overline{B}_\text{v}", "end")
    f.tex(ex + 14, gy + 150, r"\overline{B}", "start")
    f.arrow(380, 40, 470, 40, INK, 2.5, 14)
    f.tex(366, 40, r"\text{pohjoinen}", "end", w=130)
    return f.svg()


def sum_grid():
    """Task figure: B_h = 15 µT north and B_m = 20 µT east from the compass at the origin on a grid of 5 µT, drawn as
    arrows along the axes. No resultant, no needle, no angle."""
    f = Fig("fy71-sumgrid", 340, "Kuvaaja mittakaavassa, ylhäältä nähtynä: ruudukon ruutu on 5 µT. Kompassin kohdasta, ruudukon "
            "origosta, lähtee kaksi vihreää nuolta. Nuoli B_h osoittaa pohjoiseen eli ylöspäin ja nuoli B_m itään eli "
            "oikealle. Nuolten pituus kuvaa kentän suuruutta mikroteslina ruudukon asteikolla. Kokonaiskenttää, "
            "kompassin neulaa ja kulmaa ei ole piirretty.")
    ax = Axes(f, (90, 300), (450, 60), x=(0, 30), y=(0, 20), xticks=list(range(5, 31, 5)), yticks=list(range(5, 21, 5)),
              xlabel=r"\text{itä}\ (\mu\text{T})", ylabel=r"\text{pohjoinen}\ (\mu\text{T})")
    f.arrow(ax.X(0), ax.Y(0), ax.X(0), ax.Y(15), FIELD, 5, 16)
    f.arrow(ax.X(0), ax.Y(0), ax.X(20), ax.Y(0), FIELD, 5, 16)
    f.circle(ax.X(0), ax.Y(0), 5, INK)
    f.tex(ax.X(0) + 16, ax.Y(15), r"\overline{B}_\text{h}", "start", bg=True)
    f.tex(ax.X(20), ax.Y(0) - 22, r"\overline{B}_\text{m}", "middle", bg=True)
    return f.svg()


def incl_grid():
    """Task figure: Earth's field seen from the side as one arrow from the ground at the origin to the point 15 µT north
    and 50 µT down on a grid of 5 µT. The components are not drawn, B and I are not written."""
    f = Fig("fy71-inclgrid", 372, "Kuvaaja mittakaavassa, sivulta nähtynä: vaakasuora maanpinta ja ruudukko, jonka ruutu on 5 µT. "
            "Vaaka-akseli on pohjoiseen ja pystyakseli alaspäin. Maanpinnan origosta lähtee yksi vihreä nuoli B, joka "
            "osoittaa viistosti alas pohjoiseen päin. Nuolen kärki on ruudukon pisteessä, jonka lukuarvot lukija "
            "lukee ruudukolta. Komponentteja ja kulmaa ei ole piirretty.")
    x0, y0, k = 110, 54, 5.0
    f.rect(x0, y0, 40 * k, 55 * k, WHITE)
    for t in range(5, 41, 5):
        f.line(x0 + t * k, y0, x0 + t * k, y0 + 55 * k, RULE_LIGHT, 1.5)
    for t in range(5, 56, 5):
        f.line(x0, y0 + t * k, x0 + 40 * k, y0 + t * k, RULE_LIGHT, 1.5)
    f.line(x0 - 8, y0, x0 + 40 * k + 40, y0, INK, 3)
    f.line(x0, y0, x0, y0 + 55 * k, INK, 2.5)
    for t in range(10, 41, 10):
        f.tex(x0 + t * k, y0 - 22, fi(t), "middle")
    for t in range(10, 51, 10):
        f.tex(x0 - 12, y0 + t * k, fi(t), "end")
    f.tex(x0 + 40 * k + 48, y0 - 22, r"\text{pohjoinen}\ (\mu\text{T})", "start", w=150)
    f.tex(x0 + 14, y0 + 55 * k + 22, r"\text{alas}\ (\mu\text{T})", "start", w=110)
    f.tex(x0 + 40 * k + 40, y0 + 18, r"\text{maanpinta}", "end", MUTED, w=130)
    f.arrow(x0, y0, x0 + 15 * k, y0 + 50 * k, FIELD, 5, 16)
    f.circle(x0, y0, 5, INK)
    f.tex(x0 + 15 * k + 14, y0 + 30 * k, r"\overline{B}", "start", bg=True)
    return f.svg()


def hero():
    """The chapter's opening illustration: an orienteering map on a boulder in a spruce forest, a compass on it, and a
    bar magnet beside the compass turning its needle away from the north."""
    f = H.hero("fy71-hero", "Kuvitus: suunnistuskartta kivellä kuusimetsässä. Kartan päällä on kompassi, ja sen vieressä "
               "sauvamagneetti, jonka punertava ja sininen pää näkyvät. Kompassin neula on kääntynyt kohti magneettia eikä "
               "osoita kartan pohjoisnuolen suuntaan.")
    H.sky(f, "fy71h", 380)
    H.cloud(f, 860, 96, 0.9)
    H.cloud(f, 300, 70, 0.6)
    H.forest(f, 300, 70, 30, ALUMINIUM, 2)
    H.forest(f, 330, 60, 24, METAL_EDGE, 4)
    f.rect(0, 350, 1200, 250, H.grad(f, "fy71h-moss", GOOD_LIGHT, SAND_DARK))
    for x, y, h in ((90, 470, 260), (190, 430, 200), (1010, 460, 250), (1120, 430, 210), (300, 400, 150), (900, 395, 140)):
        H.spruce(f, x, y, h)
    # the boulder
    f.path("M330,560 Q300,470 380,420 Q520,360 700,368 Q860,372 900,450 Q930,520 880,566 Z", IRON, INK, 3)
    f.path("M380,420 Q520,360 700,368 Q860,372 900,450 Q760,410 600,414 Q470,418 380,420 Z", ALUMINIUM)
    # the map, tilted a little
    f.add('<g transform="rotate(-6 620 440)">')
    f.rect(470, 380, 300, 170, WHITE, INK, 2.5, 3)
    f.path("M500,470 q30,-30 70,-12 q30,14 20,40 q-30,24 -66,8 q-30,-14 -24,-36 Z", WATER_LIGHT, WATER, 1.5)
    f.path("M640,400 q50,10 90,40 q20,30 -10,52", stroke=GRAIN, w=2)
    f.path("M620,420 q46,12 76,40 q12,22 -10,40", stroke=GRAIN, w=2)
    f.path("M690,500 q30,-6 60,10", stroke=GRAIN, w=2)
    f.rect(700, 392, 60, 40, GOOD_LIGHT)
    for x in (500, 560, 620, 680, 740):
        f.line(x, 382, x, 548, COLD_LIGHT, 2)
    f.add('</g>')
    # the compass on the map: a baseplate with a round housing
    f.rect(560, 404, 96, 150, GLASS, INK, 2.5, 10, extra='fill-opacity="0.85"')
    f.circle(608, 470, 40, WHITE, INK, 3)
    for i in range(12):
        a = i * math.pi / 6
        f.line(608 + 33 * math.sin(a), 470 - 33 * math.cos(a), 608 + 38 * math.sin(a), 470 - 38 * math.cos(a), MUTED, 2)
    compass(f, 608, 470, math.radians(-10), 34)
    # the bar magnet beside it, its S end towards the compass
    f.path("M700,486 L800,470 L806,504 L706,520 Z", SPOLE, INK, 3)
    f.path("M800,470 L900,454 L906,488 L806,504 Z", NPOLE, INK, 3)
    return f.svg()


def scene():
    """A second everyday scene: a fridge door with magnets holding a drawing and a shopping list."""
    f = H.scene("fy71-scene", "Kuvitus: jääkaapin ovi, jossa magneetit pitävät kiinni lapsen piirustusta ja kauppalistaa. "
                "Oven teräslevy vetää magneetteja puoleensa.")
    f.rect(0, 0, 600, 360, SAND_LIGHT)
    f.rect(150, 14, 300, 332, H.grad(f, "fy71s-door", WHITE, GLASS, horizontal=True), INK, 3, 14)
    f.rect(420, 120, 14, 120, ALUMINIUM, INK, 2, 6)
    f.line(150, 120, 450, 120, RULE, 2)
    # the drawing: a house and a sun
    f.rect(190, 150, 120, 150, WHITE, INK, 2)
    f.path("M210,260 V220 L240,196 L270,220 V260 Z", COPPER, INK, 2)
    f.circle(285, 172, 12, HOT_LIGHT)
    f.rect(330, 170, 80, 120, WHITE, INK, 2)
    for y in (195, 215, 235, 255):
        f.line(342, y, 398, y, MUTED, 2)
    for x, y, c1, c2 in ((250, 146, SPOLE, NPOLE), (370, 164, NPOLE, SPOLE), (220, 50, SPOLE, NPOLE), (360, 60, NPOLE, SPOLE)):
        f.rect(x - 16, y - 9, 16, 18, c1, INK, 2, 3)
        f.rect(x, y - 9, 16, 18, c2, INK, 2, 3)
    return f.svg()


FIGURES = {"hero": hero, "bar-field": bar_field, "cut-magnet": cut_magnet, "domains": domains, "earth-field": earth_field,
           "vector-sum": vector_sum, "inclination": inclination, "scene": scene, "two-magnets": two_magnets,
           "sum-grid": sum_grid, "incl-grid": incl_grid}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "bar-field": "reveals: field lines from N to S and the compass directions around a bar magnet",
    "cut-magnet": "reveals: every piece of a cut magnet has both poles",
    "domains": "reveals: an iron block near a magnet's N pole becomes S at that end",
    "earth-field": "reveals: Earth's magnetic S pole is near the geographic north pole",
    "vector-sum": "reveals: the needle turns along the sum of B_h 14 µT and B_m 20 µT",
    "inclination": "reveals: B_h ≈ 14 µT and B_v ≈ 50 µT for B = 52 µT, I = 74°",
    "sum-grid": "safe: B_h 15 µT north and B_m 20 µT east as arrows on a 5 µT grid, no resultant, needle or angle (REUSE: fy7-1 exercise on the compass deflection)",
    "incl-grid": "safe: Earth's field arrow ending 15 µT north and 50 µT down on a 5 µT grid, no components, B or I (REUSE: fy7-1 exercise on inclination)",
    "two-magnets": "safe: two unmarked magnets end to end, field lines bending away from the gap, no letters or arrows",
}
