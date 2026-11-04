"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-10` writes them into lesson.md.
FY7 optics colours (course brief): light rays #e64980 (apart from force, velocity and acceleration), normals dashed
grey #6b7480; water #a9d1f0 -> #2f74b5, glass #eef5f9. Angles are drawn to scale with n(water) = 1,33."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER, WATER_LIGHT, SAND, SAND_LIGHT,
                    SAND_DARK, GRAIN, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, HEAT_LIGHT, HOT,
                    HOT_LIGHT, PAPER, n)
import herolib as H

RAY = "#e64980"
RAD = math.radians
N_WATER = 1.33


def refr(a1, n1, n2):
    """The refraction angle in degrees (Snell)."""
    return math.degrees(math.asin(n1 * math.sin(RAD(a1)) / n2))


def ray(f, x1, y1, x2, y2, w=3.5, head=15, at=0.55, color=RAY):
    """A light ray from (x1, y1) to (x2, y2) with a filled arrowhead part-way along it (NOTES 3: arrows as paths)."""
    f.line(x1, y1, x2, y2, color, w, cap="round")
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    tx, ty = x1 + ux * (L * at + head / 2), y1 + uy * (L * at + head / 2)
    bx, by = tx - ux * head, ty - uy * head; hw = head * 0.5
    f.path(f"M{n(tx)},{n(ty)} L{n(bx - uy * hw)},{n(by + ux * hw)} L{n(bx + uy * hw)},{n(by - ux * hw)} Z", fill=color)


def arc(f, cx, cy, r, a_from, a_to, color=INK, w=2):
    """An angle arc around (cx, cy); angles in degrees clockwise from straight up (screen coordinates)."""
    p = lambda a: (cx + r * math.sin(RAD(a)), cy - r * math.cos(RAD(a)))
    (x1, y1), (x2, y2) = p(a_from), p(a_to)
    sweep = 1 if a_to > a_from else 0
    big = 1 if abs(a_to - a_from) > 180 else 0
    f.path(f"M{n(x1)},{n(y1)} A{r},{r} 0 {big},{sweep} {n(x2)},{n(y2)}", stroke=color, w=w)


def normal(f, x, y1, y2):
    f.line(x, y1, x, y2, MUTED, 2, dash="8 6")


def water_grad(f, gid, y1, y2):
    return H.grad(f, gid, COLD_LIGHT, WATER_LIGHT, y1=y1, y2=y2)


# --- Ydinajatus: the rays at an interface -------------------------------------------------------------------------
def interface():
    a1 = 50; a2 = refr(a1, 1.00, N_WATER)          # 35,2°
    f = Fig("fy710-interface", 360, "Kaavakuva, kulmat mittakaavassa: valonsäde tulee ilmasta vedenpintaan. Pinnan "
            "osumiskohtaan on piirretty harmaa katkoviiva, normaali, joka on kohtisuorassa pintaa vastaan. Tuleva säde "
            "tulee vasemmalta ylhäältä normaalin kanssa kulmassa alfa 1, joka on 50 astetta. Ohuempi heijastunut säde "
            "lähtee oikealle ylös yhtä suuressa kulmassa beeta. Taittunut säde jatkuu veteen oikealle alas kulmassa "
            "alfa 2, joka on 35 astetta, eli se on taittunut kohti normaalia.")
    cx, cy, L = 300, 176, 170
    f.rect(16, cy, 568, 168, water_grad(f, "fy710-if-water", cy, 344), rx=6)
    f.line(16, cy, 584, cy, INK, 2.5)
    normal(f, cx, 22, 340)
    sx, sy = cx - L * math.sin(RAD(a1)), cy - L * math.cos(RAD(a1))
    rx, ry = cx + L * math.sin(RAD(a1)), cy - L * math.cos(RAD(a1))
    tx, ty = cx + 150 * math.sin(RAD(a2)), cy + 150 * math.cos(RAD(a2))
    arc(f, cx, cy, 62, -a1, 0); arc(f, cx, cy, 62, 0, a1); arc(f, cx, cy, 70, 180 - a2, 180)
    ray(f, sx, sy, cx, cy)
    ray(f, cx, cy, rx, ry, w=2, head=12)
    ray(f, cx, cy, tx, ty, w=3, head=14)
    f.tex(cx - 88 * math.sin(RAD(a1 / 2)), cy - 88 * math.cos(RAD(a1 / 2)) - 4, r"\alpha_1", "middle")
    f.tex(cx + 88 * math.sin(RAD(a1 / 2)), cy - 88 * math.cos(RAD(a1 / 2)) - 4, r"\beta", "middle")
    f.tex(cx + 98 * math.sin(RAD(a2 / 2)), cy + 98 * math.cos(RAD(a2 / 2)) + 4, r"\alpha_2", "middle")
    f.tex(sx - 10, sy - 14, r"\text{tuleva}", "end", RAY)
    f.tex(rx + 10, ry - 14, r"\text{heijastunut}", "middle", RAY)
    f.tex(tx + 12, ty + 4, r"\text{taittunut}", "start", RAY)
    f.tex(cx - 10, 330, r"\text{normaali}", "end", MUTED)
    f.tex(28, cy - 26, r"\text{ilma},\ n_1", "start")
    f.tex(28, cy + 28, r"\text{vesi},\ n_2", "start")
    return f.svg()


# --- Ydinajatus: wavefronts turn at the interface --------------------------------------------------------------------
def wavefronts():
    a1 = 50; a2 = refr(a1, 1.00, N_WATER)
    s1, c1, s2, c2 = math.sin(RAD(a1)), math.cos(RAD(a1)), math.sin(RAD(a2)), math.cos(RAD(a2))
    f = Fig("fy710-wavefronts", 360, "Kaavakuva, mittakaavassa veden taitekertoimella 1,33: valoaalto tulee ilmasta "
            "vinosti vedenpintaan. Aaltorintamat ovat yhdensuuntaisia viivoja, jotka ovat kohtisuorassa sädettä "
            "vastaan. Ilmassa rintamien väli on aallonpituus lambda 1. Rintaman vasen pää on jo vedessä, kun oikea pää "
            "on vielä ilmassa. Vedessä rintamat ovat lähempänä toisiaan, aallonpituus lambda 2 on lyhyempi, ja "
            "rintamat ovat kääntyneet niin, että säde etenee lähempänä normaalia.")
    cx, cy = 300, 170
    lam1 = 40.0; lam2 = lam1 / N_WATER; D = lam1 / s1     # fronts meet the surface every D in both media
    W1 = 140.0; W2 = W1 * c2 / c1                          # the beam is wider in water
    f.rect(16, cy, 568, 174, water_grad(f, "fy710-wf-water", cy, 344), rx=6)
    f.line(16, cy, 584, cy, INK, 2.5)
    normal(f, cx, 22, 338)
    d1, t1, d2, t2 = (s1, c1), (c1, -s1), (s2, c2), (c2, -s2)

    def clip(p, q, ylim, above):
        """The part of the segment p-q above (y <= ylim) or below (y >= ylim) a horizontal line."""
        (x1, y1), (x2, y2) = p, q
        inside = (lambda y: y <= ylim + 1e-9) if above else (lambda y: y >= ylim - 1e-9)
        if inside(y1) and inside(y2): return p, q
        if not inside(y1) and not inside(y2): return None
        t = (ylim - y1) / (y2 - y1); m = (x1 + t * (x2 - x1), ylim)
        return (p, m) if inside(y1) else (m, q)

    centres = {}
    for k in range(-5, 8):
        xk = cx + k * D
        for upper, (d, t, W) in ((True, (d1, t1, W1)), (False, (d2, t2, W2))):
            sk = (xk - cx) * d[0]                          # the front's distance along the central ray
            mx, my = cx + sk * d[0], cy + sk * d[1]
            p, q = (mx - W / 2 * t[0], my - W / 2 * t[1]), (mx + W / 2 * t[0], my + W / 2 * t[1])
            seg = clip(p, q, cy, upper)
            seg = seg and clip(*seg, 34 if upper else 332, not upper)
            if not seg: continue
            (x1, y1), (x2, y2) = seg
            if math.hypot(x2 - x1, y2 - y1) < 6: continue
            f.line(x1, y1, x2, y2, INK, 2.5, cap="round")
            centres[(upper, k)] = (mx, my)
    # the rays along the beam's middle
    L1 = 2.95 * lam1
    ray(f, cx - L1 * s1, cy - L1 * c1, cx, cy, w=3, at=0.5)
    ray(f, cx, cy, cx + 150 * s2, cy + 150 * c2, w=3, at=0.6)
    # wavelength marks just outside the beam: lambda_1 between two fronts in air, lambda_2 in water
    def mark(c, d, t, off, lam, label, side):
        ox, oy = c[0] + off * t[0], c[1] + off * t[1]
        ex, ey = ox + lam * d[0], oy + lam * d[1]
        f.line(ox, oy, ex, ey, INK, 2)
        for x, y in ((ox, oy), (ex, ey)): f.line(x - 7 * t[0], y - 7 * t[1], x + 7 * t[0], y + 7 * t[1], INK, 2)
        f.tex((ox + ex) / 2 + side * 26 * t[0], (oy + ey) / 2 + side * 26 * t[1], label, "middle")
    c_up = centres[(True, -2)]
    mark(c_up, d1, t1, W1 / 2 + 16, lam1, r"\lambda_1", 1)
    c_dn = centres[(False, 2)]
    mark(c_dn, d2, t2, -(W2 / 2 + 16), lam2, r"\lambda_2", -1)
    f.tex(28, 46, r"\text{ilma}", "start")
    f.tex(28, 322, r"\text{vesi}", "start")
    return f.svg()


# --- Ydinajatus: apparent depth ----------------------------------------------------------------------------------
def depth():
    f = Fig("fy710-depth", 360, "Kaavakuva, kulmat veden taitekertoimella 1,33: uima-altaan poikkileikkaus. Altaan "
            "pohjalla vasemmalla on kolikko. Siitä lähtee kaksi sädettä vinosti ylös oikealle. Vedenpinnassa säteet "
            "taittuvat normaalista poispäin ja jatkuvat oikealla ylhäällä olevaan silmään. Säteiden jatkeet on piirretty "
            "harmaina katkoviivoina takaisin veteen: ne kohtaavat kolikon yläpuolella, ja siinä kohdassa silmä näkee "
            "kolikon. Kolikko näyttää olevan lähempänä pintaa kuin todellisuudessa.")
    ys, coin = 120, (262.0, 306.0)
    f.rect(16, ys, 568, 216, water_grad(f, "fy710-dp-water", ys, 336), rx=6)
    f.rect(16, 324, 568, 12, SAND_LIGHT, rx=4)
    f.line(16, ys, 584, ys, INK, 2.5)
    def a_air(xs):
        a_w = math.degrees(math.atan2(xs - coin[0], coin[1] - 6 - ys))   # angle in water from the normal
        return refr(a_w, N_WATER, 1.00)                                  # angle in air
    def exit_for(T):
        """The exit point on the surface whose refracted ray reaches the point T (bisection)."""
        lo, hi = coin[0] + 1, min(T[0], coin[0] + (coin[1] - 6 - ys) * math.tan(RAD(48.5)))
        for _ in range(60):
            mid = (lo + hi) / 2
            if mid + (ys - T[1]) * math.tan(RAD(a_air(mid))) > T[0]: hi = mid
            else: lo = mid
        return (lo + hi) / 2
    lines = []
    for T in ((444.0, 34.0), (458.0, 56.0)):       # the two rays reach the eye's front edge
        xs = exit_for(T); lines.append((xs, a_air(xs)))
        ray(f, coin[0], coin[1] - 6, xs, ys, w=2.5, at=0.3)
        ray(f, xs, ys, T[0], T[1], w=2.5, at=0.45)
    f.line(lines[0][0], ys, lines[0][0], ys - 60, MUTED, 1.5, dash="6 5")   # the normal at an exit point
    # where the back-extended rays meet: the apparent position of the coin (x = xs - (Y - ys) tan a_air)
    (x1, b1), (x2, b2) = lines
    m1, m2 = math.tan(RAD(b1)), math.tan(RAD(b2))
    Y = ys + (x2 - x1) / (m2 - m1)
    X = x1 - m1 * (Y - ys)
    for xs, b in lines:
        f.line(xs, ys, X, Y, MUTED, 2, dash="7 6")
    # the coin and its image
    f.path(f"M{n(coin[0] - 22)},{n(coin[1])} a22,7 0 1,0 44,0 a22,7 0 1,0 -44,0 Z", "#e9c98a", INK, 2)
    f.path(f"M{n(X - 22)},{n(Y)} a22,7 0 1,0 44,0 a22,7 0 1,0 -44,0 Z", "none", INK, 2, extra='stroke-dasharray="5 4"')
    # the eye
    exx, eyy = 488, 44
    f.path(f"M{exx - 36},{eyy} Q{exx},{eyy - 26} {exx + 36},{eyy} Q{exx},{eyy + 26} {exx - 36},{eyy} Z", WHITE, INK, 2.5)
    f.circle(exx - 12, eyy, 10, COLD, INK, 1.5); f.circle(exx - 12, eyy, 4, INK)
    f.tex(coin[0] - 34, coin[1] - 2, r"\text{kolikko}", "end")
    f.tex(X - 34, Y - 4, r"\text{näennäinen paikka}", "end")
    f.tex(28, ys - 28, r"\text{ilma}", "start")
    f.tex(572, 296, r"\text{vesi}", "end")
    return f.svg()


# --- Kaava: refraction angle against the incidence angle ----------------------------------------------------------
def graph():
    f = Fig("fy710-graph", 360, "Kuvaaja mittakaavassa: taitekulma alfa 2 tulokulman alfa 1 funktiona, kun valo tulee "
            "ilmasta, jonka taitekerroin on 1,00, veteen (taitekerroin 1,33) ja timanttiin (2,42). Molemmat käyrät "
            "kulkevat suoran alfa 2 = alfa 1 alapuolella, joten säde taittuu kohti normaalia. Käyrät kaartuvat "
            "loivemmiksi: tulokulmalla 90 astetta taitekulma on vedessä 48,8 ja timantissa 24,4 astetta. Katkoviiva "
            "alfa 2 = alfa 1 kuvaa tilannetta, jossa aineilla on sama taitekerroin.")
    ax = Axes(f, (92, 306), (420, 56), x=(0, 90), y=(0, 90), xticks=[10 * k for k in range(1, 10)],
              yticks=[10 * k for k in range(1, 10)], xlabel=r"\alpha_1\ (^\circ)", ylabel=r"\alpha_2\ (^\circ)",
              xfmt=lambda v: fi(v) if v % 30 == 0 else "", yfmt=lambda v: fi(v) if v % 30 == 0 else "")
    ax.line([(0, 0), (90, 90)], MUTED, 2, dash="8 6")
    ax.curve(lambda a: refr(a, 1.00, N_WATER), 0, 90, WATER, 3)
    ax.curve(lambda a: refr(a, 1.00, 2.42), 0, 90, RAY, 3)
    f.tex(ax.X(90) + 10, ax.Y(refr(90, 1, N_WATER)), r"\text{vesi}", "start", WATER)
    f.tex(ax.X(90) + 10, ax.Y(refr(90, 1, 2.42)), r"\text{timantti}", "start", RAY)
    f.tex(ax.X(90) + 10, ax.Y(90) + 4, r"\alpha_2 = \alpha_1", "start", MUTED, w=120)
    f.tex(ax.X(4), ax.Y(80), r"n_1 = 1{,}00", "start", w=120)
    return f.svg()


# --- task figures ------------------------------------------------------------------------------------------------
FIT_A1 = [10, 20, 30, 40, 50, 60, 70]
FIT_A2 = [7, 13, 20, 26, 31, 36, 39]          # protractor readings, whole degrees (lesson-answers.py fits them)


def fit():
    """Task figure (inquiry 'mittaus'): sin a1 (air) against sin a2 (acrylic) with the line Graphical Analysis fitted."""
    xs = [math.sin(RAD(v)) for v in FIT_A2]; ys = [math.sin(RAD(v)) for v in FIT_A1]
    N = len(xs); mx, my = sum(xs) / N, sum(ys) / N
    A = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); B = my - A * mx
    f = Fig("fy710-fit", 360, "Kuvaaja mittakaavassa: laserkokeen mittaustulokset. Vaaka-akselilla on taitekulman "
            "sini, sin alfa 2, akryylissä ja pystyakselilla tulokulman sini, sin alfa 1, ilmassa. Seitsemän "
            "mittauspistettä tulokulmilla 10, 20, 30, 40, 50, 60 ja 70 astetta ja niihin sovitettu suora, joka kulkee "
            "lähes origon kautta. Ruudukon väli on 0,1 kummallakin akselilla.")
    ax = Axes(f, (100, 306), (440, 50), x=(0, 0.7), y=(0, 1.0), xticks=[0.1 * k for k in range(1, 8)],
              yticks=[0.1 * k for k in range(1, 11)], xlabel=r"\sin\alpha_2", ylabel=r"\sin\alpha_1",
              xfmt=lambda v: fi(v, 1) if round(v * 10) % 2 == 0 else "", yfmt=lambda v: fi(v, 1) if round(v * 10) % 2 == 0 else "")
    ax.line([(0, B), (0.67, A * 0.67 + B)], COLD, 3)
    for x, y in zip(xs, ys): ax.point(x, y, RAY)
    return f.svg()


def protractor():
    """Task figure (exercise L2-04): a laser ray from air into a glass half-cylinder on a protractor, a1 = 50°, a2 = 30°."""
    f = Fig("fy710-protractor", 380, "Kaavakuva: ylhäältä nähtynä lasinen puolisylinteri astelevyn keskellä. "
            "Puolisylinterin tasainen pinta on vaakasuorassa astelevyn halkaisijalla, ja kaareva puoli on alhaalla. "
            "Normaali on pystysuora katkoviiva. Astelevyn kehällä on viivat kymmenen asteen välein ja numerot 20 asteen "
            "välein normaalista mitattuina. Laserin säde tulee vasemmalta ylhäältä keskipisteeseen ja jatkuu lasissa "
            "oikealle alas. Heikko heijastunut säde lähtee oikealle ylös.")
    cx, cy, R = 300, 186, 150
    f.circle(cx, cy, R + 34, WHITE, RULE, 2)
    f.path(f"M{cx - R},{cy} A{R},{R} 0 0,0 {cx + R},{cy} Z", GLASS, INK, 2.5)
    f.line(cx - R - 34, cy, cx + R + 34, cy, INK, 2)
    normal(f, cx, cy - R - 30, cy + R + 30)
    for a in range(0, 360, 10):
        x1, y1 = cx + (R + 34) * math.sin(RAD(a)), cy - (R + 34) * math.cos(RAD(a))
        k = 14 if a % 30 == 0 else 9
        x2, y2 = cx + (R + 34 - k) * math.sin(RAD(a)), cy - (R + 34 - k) * math.cos(RAD(a))
        f.line(x1, y1, x2, y2, INK, 1.5)
    for q in (-1, 1):            # upper-left (air) and lower-right (glass) quadrants: degrees from the normal
        for a in (20, 40, 60, 80):
            ang = -a if q < 0 else 180 - a
            f.tex(cx + (R + 8) * math.sin(RAD(ang)), cy - (R + 8) * math.cos(RAD(ang)), fi(a), "middle", MUTED, size=22)
    a1, a2 = 50, 30
    L = R + 70
    ray(f, cx - L * math.sin(RAD(a1)), cy - L * math.cos(RAD(a1)), cx, cy, at=0.3)
    ray(f, cx, cy, cx + (R + 40) * math.sin(RAD(a1)), cy - (R + 40) * math.cos(RAD(a1)), w=1.5, head=10, at=0.75)
    ray(f, cx, cy, cx + (R + 40) * math.sin(RAD(a2)), cy + (R + 40) * math.cos(RAD(a2)), at=0.75)
    f.tex(24, 36, r"\text{ilma}", "start")
    f.tex(cx - 70, cy + 64, r"\text{lasi}", "middle")
    return f.svg()


# --- opening illustration and the summary scene ------------------------------------------------------------------
def hero():
    """A glass of water with a straw on a kitchen table: the straw seems broken at the water surface."""
    f = H.hero("fy710-hero", "Kuvitus: keittiön pöydällä on vesilasi, jossa on raidallinen pilli. Pillin vedessä oleva "
               "osa näyttää siirtyneen sivuun, joten pilli näyttää katkeavan vedenpinnan kohdalla. Takana ikkuna, josta "
               "aurinko paistaa.")
    f.rect(0, 0, 1200, 600, PAPER)
    # window behind with the sky
    f.rect(120, 60, 360, 300, H.grad(f, "fy710h-sky", H.ICE, GLASS), INK, 4, 8)
    f.line(300, 60, 300, 360, INK, 4); f.line(120, 210, 480, 210, INK, 4)
    H.sun(f, "fy710h", 400, 130, r=34)
    # table
    f.rect(0, 440, 1200, 160, H.grad(f, "fy710h-table", SAND_LIGHT, SAND))
    f.line(0, 440, 1200, 440, INK, 3)
    # the glass: water inside, the rim and walls
    gx0, gx1, gtop, gbot, wl = 500, 700, 150, 470, 270
    f.path(f"M{gx0},{gtop} L{gx0 + 16},{gbot} H{gx1 - 16} L{gx1},{gtop}", "none", INK, 4)
    f.path(f"M{gx0 + 6},{wl} L{gx0 + 16},{gbot - 4} H{gx1 - 16} L{gx1 - 6},{wl} Z",
           H.grad(f, "fy710h-water", COLD_LIGHT, WATER_LIGHT))
    f.path(f"M{gx0 + 6},{wl} Q{(gx0 + gx1) / 2},{wl + 10} {gx1 - 6},{wl}", "none", WATER, 3)
    # the straw: above the water a slanting tube, below it shifted sideways (it looks broken)
    def straw(x1, y1, x2, y2, w=22):
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); px, py = -dy / L * w / 2, dx / L * w / 2
        f.path(f"M{n(x1 + px)},{n(y1 + py)} L{n(x2 + px)},{n(y2 + py)} L{n(x2 - px)},{n(y2 - py)} L{n(x1 - px)},{n(y1 - py)} Z", WHITE, INK, 3)
        for k in range(1, 6):
            t0, t1 = k / 6 - 0.04, k / 6 + 0.04
            ax, ay, bx, by = x1 + dx * t0, y1 + dy * t0, x1 + dx * t1, y1 + dy * t1
            f.path(f"M{n(ax + px)},{n(ay + py)} L{n(bx + px)},{n(by + py)} L{n(bx - px)},{n(by - py)} L{n(ax - px)},{n(ay - py)} Z", HOT)
    straw(760, 40, 640, wl)
    straw(612, wl + 2, 560, gbot - 14)
    # the glass's front highlight and a lemon slice
    f.line(gx0 + 24, gtop + 30, gx0 + 34, gbot - 40, WHITE, 6, cap="round")
    return f.svg()


def scene():
    """A calm lake in the evening: the shore's trees reflected on the water, stones visible on the bottom near the shore."""
    f = H.scene("fy710-scene", "Kuvitus: tyyni järvi illalla. Vastarannan kuuset heijastuvat vedenpinnasta "
                "ylösalaisin. Etualalla rannan lähellä näkyy veden läpi kiviä pohjassa.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy710s-sky", HEAT_LIGHT, GLASS))
    f.rect(0, 170, 600, 190, H.grad(f, "fy710s-lake", WATER_LIGHT, WATER))
    f.rect(0, 160, 600, 12, GOOD)
    for k, x in enumerate(range(20, 600, 46)):
        h = 70 + 30 * H.rnd(k, 3)
        f.path(f"M{x - 18},{160} L{x},{160 - h} L{x + 18},{160} Z", GOOD, INK, 1.5)
        f.path(f"M{x - 18},{172} L{x},{172 + h * 0.85} L{x + 18},{172} Z", GOOD, extra='opacity="0.4"')
    # the near shore with stones under shallow water
    f.path("M0,360 L0,318 C80,306 170,322 240,360 Z", SAND_LIGHT)
    for x, y, r in ((360, 330, 16), (420, 312, 12), (480, 336, 18), (300, 344, 11)):
        f.circle(x, y, r, IRON, INK, 1.5)
    f.path("M200,360 C280,318 420,300 600,294 L600,360 Z", WATER_LIGHT, extra='opacity="0.55"')
    return f.svg()


FIGURES = {"hero": hero, "interface": interface, "wavefronts": wavefronts, "depth": depth, "graph": graph,
           "scene": scene, "fit": fit, "protractor": protractor}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "interface": "reveals: reflection at beta = alpha_1 and refraction towards the normal from air into water (50° -> 35°)",
    "wavefronts": "reveals: the wavefronts turn and come closer together (shorter wavelength) when light enters water",
    "depth": "reveals: the rays from a coin bend away from the normal and the coin appears higher than it is",
    "graph": "reveals: a2 against a1 for air -> water and air -> diamond, a2 < a1 and at most 48,8° / 24,4°",
    "fit": "safe: example data sin a1 (air) against sin a2 (acrylic) with a fitted line, no slope written",
    "protractor": "safe: a ray from air into a glass half-cylinder on a protractor (a1 = 50°, a2 = 30° to be read off)",
}
