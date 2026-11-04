"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-12` writes them into lesson.md.
FY7 light chapters (course brief): rays #e64980, normals dashed grey; glass #eef5f9 / #d0e6fb, water #a9d1f0 -> #2f74b5."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    SAND_DARK, GRAIN, HEAT_LIGHT, HEAT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, ICE, GOOD,
                    GOOD_LIGHT, PAPER, n)
import herolib as H

RAY = "#e64980"          # light rays in FY7 (chapters 10–13)
CORE, CLAD = COLD_LIGHT, GLASS


def ray(f, pts, w=3, opacity=1.0, arrow_at=None):
    """A light ray along the points; a small filled arrowhead in the middle of segment arrow_at shows its direction."""
    d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)
    op = f' stroke-opacity="{opacity:g}"' if opacity < 1 else ""
    f.add(f'<path d="{d}" fill="none" stroke="{RAY}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{op}/>')
    for k in ([arrow_at] if isinstance(arrow_at, int) else (arrow_at or [])):
        (x1, y1), (x2, y2) = pts[k], pts[k + 1]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        mx, my = (x1 + x2) / 2 + ux * 6, (y1 + y2) / 2 + uy * 6
        h, hw = 13, 6
        fo = f' fill-opacity="{opacity:g}"' if opacity < 1 else ""
        f.add(f'<path d="M{n(mx)},{n(my)} L{n(mx - ux * h - uy * hw)},{n(my - uy * h + ux * hw)} '
              f'L{n(mx - ux * h + uy * hw)},{n(my - uy * h - ux * hw)} Z" fill="{RAY}"{fo}/>')


def normal(f, x1, y1, x2, y2):
    f.line(x1, y1, x2, y2, MUTED, 1.5, "6 5")


def arc(f, cx, cy, r, a1, a2, color=INK, w=1.5):
    """An angle arc around (cx, cy) from direction a1 to a2 (degrees, 0 = right, 90 = down, SVG y down)."""
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 1 if a2 > a1 else 0
    f.path(f"M{n(p1[0])},{n(p1[1])} A{r},{r} 0 {large},{sweep} {n(p2[0])},{n(p2[1])}", stroke=color, w=w)


def lamp(f, x, y):
    f.rect(x - 16, y - 2, 32, 18, IRON, INK, 2, 3)
    f.circle(x, y - 4, 11, HEAT_LIGHT, INK, 2)


def water_rays():
    f = Fig("fy712-water", 360, "Periaatekuva: veden pohjalla oleva lamppu lähettää kolme valonsädettä vedenpintaan "
            "eri tulokulmissa. Jokaiseen osumakohtaan on piirretty pinnan normaali katkoviivana. Vasemmalla tulokulma "
            "30 astetta on pienempi kuin rajakulma: säde taittuu ilmaan normaalista poispäin, ja heikko osa heijastuu "
            "takaisin veteen. Keskellä tulokulma on rajakulma 48,8 astetta: taittunut säde kulkee pitkin pintaa. "
            "Oikealla tulokulma 65 astetta on suurempi kuin rajakulma: ilmaan ei pääse valoa, vaan koko säde "
            "heijastuu takaisin veteen, eli tapahtuu kokonaisheijastuminen.")
    ys, lx, ly = 150, 90, 312
    f.rect(12, ys, 576, 336 - ys, H.grad(f, "fy712w-water", WATER_LIGHT, WATER))
    f.line(12, ys, 588, ys, INK, 2)
    hits = []
    for deg in (30.0, math.degrees(math.asin(1 / 1.33)), 65.0):
        hx = lx + (ly - 10 - ys) * math.tan(math.radians(deg)); hits.append((hx, deg))
    for hx, deg in hits:
        normal(f, hx, 66, hx, 226)
    # incoming rays from the lamp
    for k, (hx, deg) in enumerate(hits):
        ray(f, [(lx, ly - 10), (hx, ys)], arrow_at=0)
    # 1: refracted into the air (41,7°) and a weak reflection
    h1, d1 = hits[0]
    b = math.asin(1.33 * math.sin(math.radians(d1)))
    ray(f, [(h1, ys), (h1 + 118 * math.sin(b), ys - 118 * math.cos(b))], arrow_at=0)
    ray(f, [(h1, ys), (h1 + 50 * math.sin(math.radians(d1)), ys + 50 * math.cos(math.radians(d1)))], w=2, opacity=0.45)
    # 2: at the critical angle the refracted ray runs along the surface; the rest reflects
    h2, d2 = hits[1]
    ray(f, [(h2, ys - 3), (h2 + 140, ys - 3)], arrow_at=0)
    ray(f, [(h2, ys), (h2 + 56 * math.sin(math.radians(d2)), ys + 56 * math.cos(math.radians(d2)))], w=2.5, opacity=0.7)
    # 3: total internal reflection
    h3, d3 = hits[2]
    L3 = (580 - h3) / math.sin(math.radians(d3))
    ray(f, [(h3, ys), (h3 + L3 * math.sin(math.radians(d3)), ys + L3 * math.cos(math.radians(d3)))], arrow_at=0)
    # angle arcs in the water between the normal (down) and the incoming ray
    for hx, deg in hits:
        arc(f, hx, ys, 34, 90 + deg, 90)
    lamp(f, lx, ly)
    f.tex(hits[0][0] - 36, 36, r"\alpha < \alpha_\text{r}", "middle", w=110)
    f.tex(hits[1][0] + 8, 36, r"\alpha = \alpha_\text{r}", "middle", w=110)
    f.tex(hits[2][0], 36, r"\alpha > \alpha_\text{r}", "middle", w=110)
    f.tex(584, 100, r"\text{ilma}", "end")
    f.tex(584, 246, r"\text{kokonaisheijastuminen}", "end", color=WHITE)
    f.tex(584, 306, r"\text{vesi},\ n = 1{,}33", "end", color=WHITE)
    return f.svg()


def fibre():
    f = Fig("fy712-fibre", 340, "Periaatekuva valokuidusta, ei mittakaavassa. Ylhäällä kuitu pituussuunnassa leikattuna: "
            "keskellä ydin, jonka taitekerroin on n1, sen ympärillä kuori, jonka taitekerroin n2 on vähän pienempi, ja "
            "uloimpana muovinen suojapäällyste. Valonsäde etenee ytimessä siksakkia: se osuu ytimen ja kuoren "
            "rajapintaan tulokulmassa, joka on suurempi kuin rajakulma, ja kokonaisheijastuu joka kerta takaisin "
            "ytimeen. Alhaalla oikealla sama kuitu poikkileikkauksena: ydin, kuori ja päällyste sisäkkäisinä "
            "ympyröinä.")
    x0, x1 = 24, 576
    f.rect(x0, 40, x1 - x0, 160, IRON, INK, 2.5, 6)            # jacket
    f.rect(x0, 56, x1 - x0, 128, CLAD, INK, 2)                  # cladding
    f.rect(x0, 100, x1 - x0, 40, CORE, INK, 2)                  # core
    # zigzag ray at 20° to the axis (schematic): bounces between y = 100 and y = 140
    th = math.radians(20); step = 40 / math.tan(th)
    pts, x, y, down = [(x0, 120)], x0 + 20 / math.tan(th), 140, True
    while x < x1:
        pts.append((x, y)); x += step; y = 100 if down else 140; down = not down
    last = pts[-1]; rem = x1 - last[0]
    pts.append((x1, last[1] + (-1 if last[1] == 140 else 1) * rem * math.tan(th)))
    ray(f, pts, w=3, arrow_at=[1, 3])
    # the angle at the third bounce (on the top boundary): normal down into the core, arc to the incoming ray
    bx, by = next(p for p in pts[1:] if p[1] == 100 and p[0] > 250)
    normal(f, bx, 64, bx, 176)
    arc(f, bx, by, 30, 90, 180 - 20 + 0.0, INK)
    f.tex(bx - 60, 78, r"\alpha", "middle", w=30)
    f.line(bx - 52, 86, bx - 20, 110, MUTED, 1.5)
    f.tex(bx + 14, 78, r"\alpha > \alpha_\text{r}", "start", w=110)
    # labels with leaders below the fibre
    f.tex(132, 162, r"\text{kuori}\ n_2", "start", w=110)
    f.line(110, 136, 110, 246, MUTED, 1.5); f.tex(60, 262, r"\text{ydin}\ n_1", "start", w=110)
    f.line(260, 192, 260, 290, MUTED, 1.5); f.tex(210, 306, r"\text{suojapäällyste}", "start")
    # end-on cross-section
    cx, cy = 506, 270
    f.circle(cx, cy, 54, IRON, INK, 2.5); f.circle(cx, cy, 42, CLAD, INK, 2); f.circle(cx, cy, 14, CORE, INK, 2)
    f.circle(cx, cy, 4, RAY)
    f.tex(440, 270, r"n_1 > n_2", "end", w=110)
    return f.svg()


PHI = 38            # the back facets' angle to the girdle in the schematic stone (degrees)


def _trace(poly, p, d, n_gem, maxb=5):
    """A ray inside a convex stone: from p in direction d to the first facet; total reflection while the angle of
    incidence exceeds the critical angle, else it leaves there. Returns the points, the hits (point, angle of
    incidence in degrees, outward normal, facet direction) and whether it left the stone."""
    pts, hits = [p], []
    for _ in range(maxb):
        best = None
        for i in range(len(poly)):
            a, b = poly[i], poly[(i + 1) % len(poly)]
            ex, ey = b[0] - a[0], b[1] - a[1]
            det = -d[0] * ey + d[1] * ex
            if abs(det) < 1e-12: continue
            rx, ry = a[0] - p[0], a[1] - p[1]
            s, t = (-rx * ey + ry * ex) / det, (d[0] * ry - d[1] * rx) / det
            if s > 1e-6 and -1e-9 <= t <= 1 + 1e-9 and (best is None or s < best[0]): best = (s, ex, ey)
        s, ex, ey = best
        q = (p[0] + s * d[0], p[1] + s * d[1]); L = math.hypot(ex, ey); u = (ex / L, ey / L)
        nrm = (u[1], -u[0])
        if nrm[0] * d[0] + nrm[1] * d[1] < 0: nrm = (-nrm[0], -nrm[1])
        cosi = nrm[0] * d[0] + nrm[1] * d[1]
        inc = math.degrees(math.acos(min(1.0, cosi)))
        pts.append(q); hits.append((q, inc, nrm, u, d))
        if n_gem * math.sin(math.radians(inc)) <= 1: return pts, hits, True
        d = (d[0] - 2 * cosi * nrm[0], d[1] - 2 * cosi * nrm[1]); p = q
    return pts, hits, False


def _refracted(n_gem, inc, nrm, d):
    """The ray leaving the stone: sin β = n sin α, on the far side of the normal with the incoming ray's tangential part."""
    b = math.asin(n_gem * math.sin(math.radians(inc)))
    cosi = nrm[0] * d[0] + nrm[1] * d[1]
    tx, ty = d[0] - cosi * nrm[0], d[1] - cosi * nrm[1]; tl = math.hypot(tx, ty) or 1
    return (math.cos(b) * nrm[0] + math.sin(b) * tx / tl, math.cos(b) * nrm[1] + math.sin(b) * ty / tl)


def _gem(f, cx, n_gem, name):
    """One brilliant-cut stone in cross-section (schematic, back facets at PHI to the girdle) and one vertical ray
    entering its table: total reflection where the angle of incidence exceeds the critical angle, else it leaks out."""
    yt, yg, half, table = 60, 110, 126, 62
    depth = half * math.tan(math.radians(PHI))
    poly = [(cx - table, yt), (cx + table, yt), (cx + half, yg - 8), (cx + half, yg), (cx, yg + depth), (cx - half, yg), (cx - half, yg - 8)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in poly) + " Z", COLD_LIGHT if n_gem > 2 else GLASS, INK, 2.5)
    f.line(cx - half, yg, cx + half, yg, INK, 1.5)
    pts, hits, out = _trace(poly, (cx - 30, yt), (0.0, 1.0), n_gem)
    q1, inc1, nrm1, u1, d1 = hits[0]
    normal(f, q1[0] - nrm1[0] * 36, q1[1] - nrm1[1] * 36, q1[0] + nrm1[0] * 46, q1[1] + nrm1[1] * 46)
    # the angle of incidence at the first back facet: between the inward normal and the way back up the ray
    a_n = math.degrees(math.atan2(-nrm1[1], -nrm1[0]))
    arc(f, q1[0], q1[1], 30, -90, a_n)
    ray(f, [(cx - 30, 20)] + pts, arrow_at=[0, 2] if len(pts) > 2 else [0])
    qe, ince, nrme, ue, de = hits[-1]
    dout = _refracted(n_gem, ince, nrme, de)
    ray(f, [qe, (qe[0] + 56 * dout[0], qe[1] + 56 * dout[1])], arrow_at=0)
    if len(hits) == 1:                                      # it leaked at the first facet: a weak reflection stays inside
        c = nrme[0] * de[0] + nrme[1] * de[1]
        r = (de[0] - 2 * c * nrme[0], de[1] - 2 * c * nrme[1])
        ray(f, [qe, (qe[0] + 50 * r[0], qe[1] + 50 * r[1])], w=2, opacity=0.45)
    f.tex(q1[0] + 6, q1[1] - 52, fr"{PHI}^\circ", "start", w=50)
    f.tex(cx, 280, name, "middle", w=250)


def diamond():
    f = Fig("fy712-diamond", 310, "Periaatekuva, ei mittakaavassa: kaksi samanmuotoista hiottua kiveä poikkileikkauksena. "
            f"Kummankin kiven yläpinnasta tulee pystysuoraan alas sama valonsäde, joka osuu alaviistopintaan {PHI} asteen "
            "tulokulmassa. Vasemmalla timantissa, jonka taitekerroin on 2,42 ja rajakulma 24,4 astetta, säde "
            "kokonaisheijastuu kahdesti ja palaa ylöspäin ulos kiven yläosasta. Oikealla lasissa, jonka taitekerroin on "
            "1,50 ja rajakulma 41,8 astetta, tulokulma on pienempi kuin rajakulma: suurin osa valosta taittuu ulos "
            "kiven alapuolelta, ja vain heikko osa heijastuu.")
    _gem(f, 150, 2.42, r"\text{timantti},\ \alpha_\text{r} = 24{,}4^\circ")
    _gem(f, 450, 1.50, r"\text{lasi},\ \alpha_\text{r} = 41{,}8^\circ")
    f.line(300, 20, 300, 290, RULE, 1.5, "6 5")
    return f.svg()


def critical_graph():
    f = Fig("fy712-graph", 340, "Kuvaaja mittakaavassa: rajakulma asteina aineen taitekertoimen n1 funktiona, kun "
            "toinen aine on ilmaa, jonka taitekerroin on 1,00. Käyrä laskee 90 asteesta, kun n1 on 1,00, ensin "
            "jyrkästi ja sitten loivemmin. Merkityt pisteet: vesi, n1 = 1,33, rajakulma 48,8 astetta; lasi, n1 = 1,50, "
            "41,8 astetta; timantti, n1 = 2,42, 24,4 astetta.")
    ax = Axes(f, (96, 290), (520, 76), x=(1.0, 2.6), y=(0, 90), xticks=[1.2 + 0.2 * k for k in range(8)],
              yticks=[15 * k for k in range(1, 7)], xlabel=r"n_1", ylabel=r"\alpha_\text{r}\ (^\circ)",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 5) % 2 == 0 else "",
              yfmt=lambda v: fi(v) if v % 30 == 0 else "")
    f.tex(ax.X(1.0), 314, r"1{,}0", "middle")
    f.tex(84, 282, r"0", "end")
    ax.curve(lambda x: math.degrees(math.asin(1 / x)), 1.0, 2.6, RAY, 3)
    for nn, name, dx, dy, anc in ((1.33, r"\text{vesi}", -12, 26, "end"), (1.50, r"\text{lasi}", 12, -22, "start"),
                                  (2.42, r"\text{timantti}", 0, -36, "middle")):
        v = math.degrees(math.asin(1 / nn))
        ax.point(nn, v, INK)
        f.tex(ax.X(nn) + dx, ax.Y(v) + dy, name, anc, bg=True)
    f.tex(520, 112, r"n_2 = 1{,}00\ (\text{ilma})", "end", w=200, bg=True)
    return f.svg()


def hero():
    """The opening illustration: a sea cable on the bottom of the Baltic between two shores, and a magnified view of
    the glass fibre inside with light zigzagging along it."""
    f = H.hero("fy712-hero", "Kuvitus: meren poikkileikkaus. Vasemmalla ja oikealla rannalla on kaupungit, ja meren "
               "pohjassa kulkee merikaapeli rannalta toiselle. Keskellä suurennuslasin kaltaisessa ympyrässä näkyy "
               "kaapelin sisällä oleva lasikuitu, jonka ytimessä valonsäde etenee siksakkia heijastuen kuidun "
               "reunoilta.")
    H.sky(f, "fy712h", 240)
    H.cloud(f, 300, 80, 0.8); H.cloud(f, 960, 60, 0.6)
    f.rect(0, 230, 1200, 370, H.grad(f, "fy712h-sea", WATER_LIGHT, WATER))
    # sea bottom and the two shores
    f.path("M0,190 L120,190 Q200,200 250,300 Q300,470 420,520 Q600,560 800,530 Q930,500 980,330 Q1020,210 1080,200 "
           "L1200,200 L1200,600 L0,600 Z", H.grad(f, "fy712h-bed", SAND_LIGHT, SAND))
    for k in range(40):
        x = 300 + 640 * H.rnd(k, 7); f.circle(x, 560 + 30 * H.rnd(k + 50, 7), 3, GRAIN)
    # towns on the shores
    for x, w, h in ((14, 44, 70), (62, 52, 110), (120, 40, 60)):
        f.rect(x, 190 - h, w, h, SAND_LIGHT, INK, 2.5)
        for j in range(int(h // 30)):
            f.rect(x + 10, 190 - h + 12 + 30 * j, 12, 12, HEAT_LIGHT, INK, 1.5)
    for x, w, h in ((1090, 46, 64), (1142, 44, 90)):
        f.rect(x, 200 - h, w, h, SAND_LIGHT, INK, 2.5)
        for j in range(int(h // 30)):
            f.rect(x + 10, 200 - h + 12 + 30 * j, 12, 12, HEAT_LIGHT, INK, 1.5)
    # the cable on the bottom
    f.path("M150,190 Q210,205 252,300 Q302,470 420,515 Q600,553 800,524 Q928,494 976,330 Q1015,215 1080,200",
           stroke=INK, w=8, extra='stroke-linecap="round"')
    # the magnified view: a circle with the fibre and the zigzag ray, joined to the cable by two lines
    cx, cy, r = 600, 370, 130
    f.line(560, 548, cx - 86, cy + 98, WHITE, 3); f.line(640, 548, cx + 86, cy + 98, WHITE, 3)
    f.circle(600, 548, 12, "none", WHITE, 3)
    f.defs_add(f'<clipPath id="fy712h-lens"><circle cx="{cx}" cy="{cy}" r="{r - 3}"/></clipPath>')
    f.circle(cx, cy, r, PAPER, INK, 4)
    f.add('<g clip-path="url(#fy712h-lens)">')
    f.rect(cx - r, cy - 70, 2 * r, 140, IRON)
    f.rect(cx - r, cy - 54, 2 * r, 108, CLAD)
    f.rect(cx - r, cy - 22, 2 * r, 44, CORE)
    xs, y, pts, up = cx - r - 40, cy + 22, [], True
    while xs < cx + r + 60:
        pts.append((xs, y)); xs += 70; y = cy - 22 if up else cy + 22; up = not up
    ray(f, pts, w=5)
    f.add('</g>')
    f.circle(cx, cy, r, "none", INK, 4)
    return f.svg()


def scene():
    """A second everyday scene: a fibre-optic lamp on a shelf, its fibres glowing at the tips only."""
    f = H.scene("fy712-scene", "Kuvitus: hyllyllä on kuitulamppu. Sen jalustasta nousee kimppu ohuita läpinäkyviä "
                "muovikuituja, jotka kaartuvat joka suuntaan. Kuidut eivät hehku sivuiltaan, mutta jokaisen kuidun "
                "pää loistaa kirkkaana pisteenä.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 290, 600, 70, H.grad(f, "fy712s-shelf", SAND_LIGHT, SAND))
    f.line(0, 290, 600, 290, INK, 2.5)
    # the base
    f.path("M250,290 L262,236 H338 L350,290 Z", IRON, INK, 3)
    f.rect(270, 226, 60, 12, ALUMINIUM, INK, 2.5, 3)
    # the fibres: curves from the base fanning out, a bright tip at the end of each
    tips = []
    for k in range(15):
        a = math.radians(-160 + k * 140 / 14)
        L = 150 + 26 * H.rnd(k, 3)
        ex, ey = 300 + L * math.cos(a) * 1.25, 226 + L * math.sin(a) * 0.95
        f.path(f"M{n(292 + k)},226 Q{n(300 + (ex - 300) * 0.2)},{n(226 - L * 0.7)} {n(ex)},{n(ey)}", stroke=RULE, w=2.5)
        tips.append((ex, ey))
    f.defs_add(f'<radialGradient id="fy712s-glow"><stop offset="0" stop-color="{WHITE}"/><stop offset="0.35" '
               f'stop-color="{RAY}"/><stop offset="1" stop-color="{RAY}" stop-opacity="0"/></radialGradient>')
    for ex, ey in tips:
        f.circle(ex, ey, 13, "url(#fy712s-glow)")
    return f.svg()


FIGURES = {"hero": hero, "water": water_rays, "fibre": fibre, "diamond": diamond, "graph": critical_graph, "scene": scene}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "water": "reveals: below α_r light refracts out, at α_r it grazes the surface, above α_r it reflects totally (water 48,8°)",
    "fibre": "reveals: the ray stays in the core by total reflection at the core–cladding boundary (n1 > n2)",
    "diamond": "reveals: at 38° a diamond (α_r 24,4°) reflects totally and a glass stone (α_r 41,8°) leaks",
    "graph": "reveals: the critical angle against air for water 48,8°, glass 41,8°, diamond 24,4°",
}
