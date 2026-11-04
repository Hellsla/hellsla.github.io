"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-14` writes them into lesson.md.
FY7 light chapters (course brief): rays #e64980, normals dashed grey. The interference colours of a film are computed,
not chosen: the reflectance of the film at normal incidence (single-layer formula with the Fresnel amplitudes, the same
model as the simulation) is weighted with the CIE 1931 colour-matching functions (the multi-lobe fit of Wyman, Sloan &
Shirley 2013) and turned into sRGB; the brightness is scaled so that the strongest reflection of the film is white."""
import cmath
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    GRAIN, HEAT_LIGHT, HEAT, COLD_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

RAY = "#e64980"          # light rays in FY7 (chapters 10–15)
N_SOAP, N_COAT, N_GLASS, N_OIL, N_WATER = 1.33, 1.38, 1.52, 1.47, 1.33


# --- the model: reflectance of a thin film and its colour in white light ---
def refl(d, lam, nf, ns):
    """Share of the light reflected at normal incidence by a film (index nf, thickness d in nm) on a medium ns, light
    from air: r = (r1 + r2 e^(-iδ)) / (1 + r1 r2 e^(-iδ)), δ = 2π · 2nd / λ."""
    r1, r2 = (1 - nf) / (1 + nf), (nf - ns) / (nf + ns)
    e = cmath.exp(-1j * 4 * math.pi * nf * d / lam)
    return abs((r1 + r2 * e) / (1 + r1 * r2 * e)) ** 2


def _g(x, mu, s1, s2):
    t = (x - mu) / (s1 if x < mu else s2)
    return math.exp(-0.5 * t * t)


def _cmf(l):
    return (1.056 * _g(l, 599.8, 37.9, 31.0) + 0.362 * _g(l, 442.0, 16.0, 26.7) - 0.065 * _g(l, 501.1, 20.4, 26.2),
            0.821 * _g(l, 568.8, 46.9, 40.5) + 0.286 * _g(l, 530.9, 16.3, 31.1),
            1.217 * _g(l, 437.0, 11.8, 36.0) + 0.681 * _g(l, 459.0, 26.0, 13.8))


_M = ((3.2406, -1.5372, -0.4986), (-0.9689, 1.8758, 0.0415), (0.0557, -0.2040, 1.0570))
_LAMS = list(range(400, 701, 2))


def _rgb_lin(w):
    X = Y = Z = 0.0
    for l in _LAMS:
        c = _cmf(l); v = w(l); X += v * c[0]; Y += v * c[1]; Z += v * c[2]
    return [sum(_M[i][j] * (X, Y, Z)[j] for j in range(3)) for i in range(3)]


_WHITE = _rgb_lin(lambda l: 1.0)


def film_colour(d, nf=N_SOAP, ns=1.0, norm=None):
    """The colour (hex) of the white light that a film of thickness d (nm) reflects; norm is the reflectance shown as
    full white (default: the film's strongest reflection, at a quarter-wave layer for 550 nm)."""
    norm = norm or max(refl(550 / (4 * nf), 550, nf, ns), refl(550 / (2 * nf), 550, nf, ns))
    lin = [min(1.0, max(0.0, v / wv)) for v, wv in zip(_rgb_lin(lambda l: refl(d, l, nf, ns) / norm), _WHITE)]
    g = [255 * (12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055) for v in lin]
    return "#%02x%02x%02x" % tuple(round(v) for v in g)


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


def dim_arrow(f, x, y1, y2, color=INK):
    """A vertical dimension line with filled heads at both ends."""
    f.line(x, y1 + 9, x, y2 - 9, color, 1.5)
    f.path(f"M{n(x)},{n(y1)} L{n(x - 5)},{n(y1 + 10)} L{n(x + 5)},{n(y1 + 10)} Z", color)
    f.path(f"M{n(x)},{n(y2)} L{n(x - 5)},{n(y2 - 10)} L{n(x + 5)},{n(y2 - 10)} Z", color)


# --- Ydinajatus: the two reflections of a soap film ---
def reflections():
    f = Fig("fy714-refl", 360, "Periaatekuva, ei mittakaavassa: saippuakalvo poikkileikkauksena, ilmaa molemmin puolin. "
            "Kalvon paksuus d on suurennettu, ja säteet on piirretty vinoon, jotta ne erottuvat; luvussa tarkastellaan "
            "kohtisuoraan tulevaa valoa. Ylhäältä tuleva säde heijastuu osittain kalvon yläpinnasta: tämä on säde 1, "
            "ja siinä heijastunut aalto saa puolen aallonpituuden siirtymän, koska valo heijastuu suuremman "
            "taitekertoimen aineesta. Osa valosta jatkaa kalvoon, heijastuu kalvon alapinnasta ilmaa vasten ilman "
            "siirtymää ja palaa yläpinnan läpi ilmaan: tämä on säde 2. Säde 2 kulkee kalvossa lisämatkan, kaksi "
            "kertaa kalvon paksuuden. Heikko osa valosta jatkaa alapinnan läpi alas.")
    yt, yb = 150, 230
    f.rect(12, yt, 576, yb - yt, GLASS)
    f.line(12, yt, 588, yt, INK, 2.5); f.line(12, yb, 588, yb, INK, 2.5)
    th = math.radians(22); b = math.asin(math.sin(th) / N_SOAP)
    A = (250, yt); B = (A[0] + (yb - yt) * math.tan(b), yb); C = (A[0] + 2 * (yb - yt) * math.tan(b), yt)
    top = 56
    f.line(A[0], 64, A[0], yb + 16, MUTED, 1.5, "6 5")                       # the normal at the first hit
    ray(f, [(A[0] - (yt - top) * math.tan(th), top), A], arrow_at=0)
    ray(f, [A, (A[0] + (yt - top) * math.tan(th), top)], arrow_at=0)         # ray 1
    ray(f, [A, B, C, (C[0] + (yt - top) * math.tan(th), top)], arrow_at=[0, 2])   # ray 2
    ray(f, [B, (B[0] + 100 * math.tan(th), yb + 100)], w=2, opacity=0.45)
    f.tex(A[0] + (yt - top) * math.tan(th), 34, "1", "middle", w=30)
    f.tex(C[0] + (yt - top) * math.tan(th), 34, "2", "middle", w=30)
    f.tex(226, 118, r"\tfrac{1}{2}\lambda\ \text{siirtymä}", "end")
    f.tex(256, 266, r"\text{ei siirtymää}", "start")
    dim_arrow(f, 150, yt, yb)
    f.tex(136, 190, "d", "end", w=30)
    f.tex(584, 84, r"\text{ilma},\ n = 1{,}00", "end")
    f.tex(584, 190, r"\text{saippuakalvo},\ n = 1{,}33", "end")
    f.tex(584, 300, r"\text{ilma},\ n = 1{,}00", "end")
    return f.svg()


# --- Ydinajatus: why the thinnest film is dark and a quarter-wave film bright ---
def _wave(f, x0, x1, y, amp, shift, color, w=3):
    """y = -amp · sin(2π (x - x0) / L + shift) drawn from x0 to x1 (one wavelength L = 100 units)."""
    pts = []
    for i in range(121):
        x = x0 + (x1 - x0) * i / 120
        pts.append((x, y - amp * math.sin(2 * math.pi * (x - x0) / 100 + shift)))
    d = "M" + " L".join(f"{n(px)},{n(py)}" for px, py in pts)
    f.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round"/>')


def phase():
    f = Fig("fy714-phase", 360, "Kaavakuva: kalvosta heijastuneet aallot 1 ja 2 sekä niiden summa kahdessa tapauksessa. "
            "Vasemmalla kalvo on paljon ohuempi kuin aallonpituus. Aalto 1 on kääntynyt yläpinnan heijastuksessa, "
            "aalto 2 ei, eikä aalto 2 ole jäänyt jälkeen, joten aallot ovat vastakkaisessa vaiheessa: harja kohtaa "
            "pohjan, ja summa on vaakasuora suora eli heijastunutta valoa ei ole. Oikealla kalvo on niin paksu, että "
            "aalto 2 kulkee puoli aallonpituutta pidemmän matkan. Silloin aallot ovat samassa vaiheessa, ja summa on "
            "kaksinkertainen aalto eli heijastus on voimakas.")
    rows = (100, 170, 250)
    for px0, title, shift2, result in ((70, r"\text{hyvin ohut kalvo}", 0.0, r"\text{heikentävä}"),
                                       (362, r"2nd = \tfrac{1}{2}\lambda", math.pi, r"\text{vahvistava}")):
        x1 = px0 + 214
        f.tex((px0 + x1) / 2 - 16, 36, title, "middle")
        f.line(px0 + 25, 72, px0 + 25, 300, MUTED, 1.5, "6 5")          # the crest of wave 1 (inverted)
        _wave(f, px0, x1, rows[0], 22, math.pi, RAY)                      # wave 1: inverted at the top surface
        _wave(f, px0, x1, rows[1], 22, shift2, RAY)                       # wave 2: no shift, later by 2nd
        if shift2 == 0.0: f.line(px0, rows[2], x1, rows[2], INK, 3)
        else: _wave(f, px0, x1, rows[2], 44, math.pi, INK)
        for y, lab in zip(rows, ("1", "2", "1 + 2")):
            f.tex(px0 - 12, y, lab, "end")
        f.tex((px0 + x1) / 2 - 16, 330, result, "middle")
    f.line(300, 20, 300, 340, RULE, 1.5, "6 5")
    return f.svg()


# --- Ydinajatus: the colours of a soap film against its thickness ---
def bands():
    f = Fig("fy714-bands", 300, "Kuva lasketuista väreistä: valkoisessa valossa saippuakalvosta, jonka taitekerroin on "
            "1,33, heijastuneen valon väri kalvon paksuuden funktiona, kun valo tulee kohtisuoraan. Yläpuolella "
            "kiilan muotoinen kalvo poikkileikkauksena, sen paksuus kasvaa vasemmalta oikealle nollasta 1000 "
            "nanometriin (paksuus suurennettu). Värinauha alkaa vasemmalta mustana, muuttuu harmaansiniseksi, "
            "valkoiseksi, keltaiseksi, oranssiksi ja noin 200 nanometrin kohdalla purppuraksi, sitten siniseksi, "
            "vihreäksi, keltaiseksi ja taas purppuraksi. Mitä paksumpi kalvo, sitä haaleammiksi värit muuttuvat. "
            "Värien kirkkaus on vahvistettu: todellinen heijastus on vain muutamia prosentteja.")
    x0, x1, y0, y1 = 40, 500, 130, 190
    X = lambda d: x0 + (x1 - x0) * d / 1000
    f.path(f"M{x0},{y0 - 14} L{x1},{y0 - 70} L{x1},{y0 - 14} Z", GLASS, INK, 2)
    step = 8
    for k in range(0, 1000, step):
        f.rect(X(k), y0, (x1 - x0) * step / 1000 + 0.6, y1 - y0, film_colour(k + step / 2))
    f.rect(x0, y0, x1 - x0, y1 - y0, "none", INK, 2)
    for d in range(0, 1001, 200):
        f.line(X(d), y1, X(d), y1 + 7, INK, 2)
        f.tex(X(d), y1 + 26, fi(d), "middle")
    for d in range(100, 1000, 200):
        f.line(X(d), y1, X(d), y1 + 5, MUTED, 1.5)
    f.tex(512, 160, r"d\ (\text{nm})", "start")
    f.tex(x0, 34, r"\text{saippuakalvo},\ n = 1{,}33", "start")
    return f.svg()


# --- Kaava: reflection of glass with and without a quarter-wave MgF2 coating ---
def graph():
    dq = 550 / (4 * N_COAT)
    f = Fig("fy714-graph", 340, "Kuvaaja mittakaavassa: kohtisuoraan tulevasta valosta heijastuvan valon osuus R "
            "prosentteina aallonpituuden funktiona välillä 400–700 nm. Pinnoittamaton lasi, jonka taitekerroin on "
            "1,52, heijastaa kaikilla aallonpituuksilla noin 4,3 prosenttia, vaakasuora musta viiva. Kun lasin pinnalla "
            "on magnesiumfluoridikerros, jonka taitekerroin on 1,38 ja paksuus 99,6 nanometriä eli neljäsosa "
            "aallonpituudesta 550 nanometriä kalvossa, vihreä käyrä laskee pienimpään arvoonsa noin 1,3 prosenttia "
            "550 nanometrin kohdalla ja nousee reunoille: 400 nanometrin kohdalla noin 2,2 ja 700 nanometrin kohdalla noin 1,6 "
            "prosenttiin. Taitekertoimien riippuvuutta "
            "aallonpituudesta ei ole otettu huomioon.")
    ax = Axes(f, (96, 286), (470, 64), x=(400, 700), y=(0, 5), xticks=[450 + 50 * k for k in range(6)],
              yticks=[1, 2, 3, 4, 5], xlabel=r"\lambda\ (\text{nm})", ylabel=r"R\ (\%)",
              xfmt=lambda v: fi(v) if v % 100 == 0 else "", origin_label=False)
    f.tex(ax.X(400), 310, "400", "middle")
    f.tex(80, 280, "0", "end")
    bare = refl(0, 550, N_COAT, N_GLASS) * 100
    ax.line([(400, bare), (700, bare)], INK, 3)
    ax.curve(lambda l: refl(dq, l, N_COAT, N_GLASS) * 100, 400, 700, GOOD, 3)
    rmin = refl(dq, 550, N_COAT, N_GLASS) * 100
    ax.guide(550, rmin); ax.point(550, rmin, GOOD)
    f.tex(ax.X(700), ax.Y(bare) - 22, r"\text{ilman pinnoitetta}", "end", bg=True)
    f.tex(ax.X(645), ax.Y(0.6), r"\text{MgF}_2\text{-pinnoite}", "middle", color=GOOD, bg=True)
    return f.svg()


# --- the opening illustration: soap bubbles over a garden table ---
def _bubble(f, gid, cx, cy, r, dtop, dbot, opacity=0.8):
    """A soap bubble whose wall thickens from dtop at the top to dbot at the bottom (it drains): horizontal bands in
    the computed interference colours, a white highlight and a thin outline."""
    f.defs_add(f'<clipPath id="{gid}"><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}"/></clipPath>')
    f.add(f'<g clip-path="url(#{gid})" opacity="{opacity:g}">')
    steps = 40
    for k in range(steps):
        t = (k + 0.5) / steps
        d = dtop + (dbot - dtop) * t ** 1.6
        y = cy - r + 2 * r * k / steps
        f.rect(cx - r, y, 2 * r, 2 * r / steps + 0.8, film_colour(d))
    f.add('</g>')
    f.circle(cx, cy, r, "none", WHITE, 3)
    f.path(f"M{n(cx - r * 0.62)},{n(cy - r * 0.38)} A{n(r * 0.72)},{n(r * 0.72)} 0 0 1 {n(cx - r * 0.18)},{n(cy - r * 0.7)}",
           stroke=WHITE, w=max(4, r * 0.06), extra='stroke-linecap="round" stroke-opacity="0.9"')


def hero():
    f = H.hero("fy714-hero", "Kuvitus: aurinkoisena päivänä puutarhan yllä leijuu kolme saippuakuplaa. Suurimman kuplan "
               "pinnassa on vaakasuoria väriraitoja: ylhäällä harmaata ja valkoista, sitten keltaista, oranssia, "
               "purppuraa, sinistä ja vihreää, alempana taas keltaista ja purppuraa. Pöydällä on kulho saippuavettä "
               "ja kuplarengas. Värit on laskettu saippuakalvon paksuudesta, joka kasvaa kuplan yläosasta alaosaan.")
    H.sky(f, "fy714h", 600)
    H.sun(f, "fy714h", 1080, 96, 50)
    H.cloud(f, 230, 90, 0.9); H.cloud(f, 860, 70, 0.6)
    H.hills(f, "fy714h-hill", 430, [GOOD_LIGHT, GOOD], amp=22, seed=3)
    f.rect(0, 470, 1200, 130, H.grad(f, "fy714h-lawn", GOOD_LIGHT, GOOD))
    # the table with a bowl of soap water and the wand
    f.rect(120, 470, 330, 22, SAND, INK, 2.5, 4)
    f.rect(150, 492, 18, 100, SAND, INK, 2.5); f.rect(402, 492, 18, 100, SAND, INK, 2.5)
    f.path("M200,470 Q205,430 240,428 L330,428 Q365,430 370,470 Z", COLD_LIGHT, INK, 2.5)
    f.path("M210,440 Q285,452 360,440", stroke=WATER, w=2)
    f.line(330, 444, 420, 330, IRON, 6, cap="round")
    f.circle(436, 312, 24, "none", IRON, 6)
    _bubble(f, "fy714h-b1", 640, 280, 170, 30, 900)
    _bubble(f, "fy714h-b2", 930, 250, 78, 120, 700, 0.75)
    _bubble(f, "fy714h-b3", 470, 150, 54, 200, 650, 0.75)
    return f.svg()


def scene():
    """A second everyday scene: an oil film on a puddle on asphalt after rain, its colours computed for oil on water."""
    f = H.scene("fy714-scene", "Kuvitus: sateen jälkeen asfaltilla on lätäkkö, ja sen pinnalla on ohut öljykalvo. "
                "Kalvossa näkyy kiemurtelevia renkaita sinistä, vihreää, keltaista ja purppuraa, sillä kalvo on "
                "keskeltä paksumpi kuin reunoilta. Värit on laskettu öljykalvolle veden päällä.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy714s-asphalt", "#6c757d", INK))
    for k in range(160):
        f.circle(600 * H.rnd(k, 4), 360 * H.rnd(k + 400, 4), 1.5 + 1.5 * H.rnd(k + 800, 4), MUTED)
    f.path("M70,210 C60,120 200,70 320,80 C450,90 560,140 540,230 C525,300 380,320 260,312 C140,306 80,280 70,210 Z",
           H.grad(f, "fy714s-water", "#4f8fbf", WATER), INK, 2.5)
    # the oil film: nested rings, thickest in the middle; colours computed for oil (1,47) on water (1,33)
    norm = refl(550 / (4 * N_OIL), 550, N_OIL, N_WATER)
    for k in range(14):
        s = 1 - k / 14
        d = 120 + 520 * (k / 13)
        cx, cy = 300 + 18 * math.sin(k * 0.9), 196 + 6 * math.cos(k * 1.3)
        f.path(f"M{n(cx - 210 * s)},{n(cy + 6 * s)} C{n(cx - 200 * s)},{n(cy - 90 * s)} {n(cx + 40 * s)},{n(cy - 110 * s)} "
               f"{n(cx + 190 * s)},{n(cy - 50 * s)} C{n(cx + 250 * s)},{n(cy + 10 * s)} {n(cx + 110 * s)},{n(cy + 100 * s)} "
               f"{n(cx - 40 * s)},{n(cy + 90 * s)} C{n(cx - 150 * s)},{n(cy + 82 * s)} {n(cx - 214 * s)},{n(cy + 50 * s)} "
               f"{n(cx - 210 * s)},{n(cy + 6 * s)} Z", film_colour(d, N_OIL, N_WATER, norm),
               extra='fill-opacity="0.85"')
    f.path("M70,210 C60,120 200,70 320,80 C450,90 560,140 540,230 C525,300 380,320 260,312 C140,306 80,280 70,210 Z",
           "none", INK, 2.5)
    return f.svg()


FIGURES = {"hero": hero, "reflections": reflections, "phase": phase, "bands": bands, "graph": graph, "scene": scene}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "reflections": "reveals: a soap film reflects at both surfaces, a half-wavelength shift only at the top one, extra path 2d",
    "phase": "reveals: a very thin soap film is dark (the waves cancel) and a film with 2nd = λ/2 reflects strongly",
    "bands": "reveals: the computed colours of a soap film (n = 1,33) for 0–1000 nm, black at 0, purple near 200 nm",
    "graph": "reveals: R of glass 4,3 % and with a 99,6 nm MgF2 layer 1,3 % at 550 nm, 2,2 % at 400 nm and 1,6 % at 700 nm",
}
