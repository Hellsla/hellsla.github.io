"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-4` writes them into lesson.md.
The double-slit dots use the simulation's model (assets/sims/fy8/fy8-4/sim.js): fringes 2,0 mm apart under a
single-slit envelope whose first zero is at 10 mm, sampled with a Park–Miller generator so the figure redraws identically."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    ALUMINIUM, METAL_EDGE, IRON, GLASS, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

MOMENTUM = "#7048e8"
XMIN, BW, NB = -12.0, 0.05, 480


def inten(x, both=True):
    u = math.pi * x / 10.0
    env = 1.0 if x == 0 else (math.sin(u) / u) ** 2
    return math.cos(math.pi * x / 2.0) ** 2 * env if both else env


def sample(count, seed, both=True):
    """count screen positions (mm) and heights in [0, 1) drawn from the model distribution."""
    C, s = [], 0.0
    for i in range(NB):
        s += inten(XMIN + BW * (i + 0.5), both); C.append(s)
    out, st = [], seed
    def r():
        nonlocal st
        st = (st * 16807) % 2147483647; return st / 2147483647
    for _ in range(count):
        t = r() * C[-1]; i = next(k for k, v in enumerate(C) if v > t)
        out.append((XMIN + BW * (i + 0.5) + (r() - 0.5) * BW, r()))
    return out


def wavy(f, x1, y1, x2, y2, wl, amp, color, w=3, head=16):
    """A photon: a sine-wave shaft from (x1, y1) and a filled arrowhead with its tip at (x2, y2)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    body = L - head
    pts = []
    for k in range(int(body) + 1):
        a = amp * math.sin(2 * math.pi * k / wl) * min(1, k / 6, (body - k) / 6)
        pts.append(f"{n(x1 + ux * k + px * a)},{n(y1 + uy * k + py * a)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.45
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def electron(f, x, y, r=11):
    f.circle(x, y, r, COLD, INK, 2)


def buildup():
    f = Fig("fy84-bu", 380, "Kaavakuva: kaksoisrakokokeen varjostin kolmessa vaiheessa, kun yksittäiset fotonit tai elektronit "
            "osuvat siihen yksi kerrallaan. 10 osuman jälkeen pisteet näyttävät satunnaisilta, 200 osuman jälkeen raidat alkavat "
            "erottua ja 5000 osuman jälkeen näkyy selvä raitakuvio. Alimpana on aaltomallin mukainen intensiteetti, jonka "
            "huiput ovat samoissa kohdissa kuin tiheimmät pisteraidat. Pisteet on arvottu mallin todennäköisyysjakaumasta.")
    x0, x1 = 156, 584
    X = lambda x: x0 + (x - XMIN) / 24 * (x1 - x0)
    for row, (N, seed) in enumerate(((10, 7), (200, 11), (5000, 13))):
        y0 = 16 + row * 82; h = 64
        f.rect(x0, y0, x1 - x0, h, WHITE, INK, 2)
        r = 2.6 if N <= 200 else 1.3
        dots = " ".join(f"M{n(X(x)) if r > 2 else round(X(x), 1)},{round(y0 + 5 + yy * (h - 10), 1)}h0" for x, yy in sample(N, seed))
        f.add(f'<path d="{dots}" stroke="{HOT}" stroke-width="{2 * r:g}" stroke-linecap="round" fill="none"/>')
        f.tex(x0 - 14, y0 + h / 2, rf"N = {N}", "end")
    # the wave model's intensity on the same scale
    yb, yt = 352, 270
    f.line(x0, yb, x1, yb, INK, 2)
    pts = [(x, inten(x)) for x in [XMIN + 24 * k / 480 for k in range(481)]]
    f.add('<polyline points="' + " ".join(f"{n(X(x))},{n(yb - v * (yb - yt))}" for x, v in pts) + f'" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    f.tex(x0 - 14, (yb + yt) / 2 + 4, r"\text{aalto}", "end")
    for x in (-4, -2, 0, 2, 4):
        f.line(X(x), 16, X(x), yb, RULE, 1.5, "5 5")
    return f.svg()


def patterns():
    f = Fig("fy84-pa", 340, "Kaavakuva kolmesta osumajakaumasta samalla varjostimella. Vasemmalla vain yksi rako on auki: "
            "yksi leveä huippu ilman raitoja. Keskellä molemmat raot ovat auki: raitakuvio, jonka tummissa kohdissa osumia "
            "ei juuri ole, vaikka yhden raon kuviossa niissä on paljon osumia. Oikealla molemmat raot ovat auki, mutta "
            "kulkureitti mitataan: raidat katoavat, ja jakauma on kahden yhden raon kuvion summa. Pystyakselit ovat "
            "osumien määrä samalla osumien kokonaismäärällä, ei lukuarvoja.")
    panels = ((20, r"\text{yksi rako}", "one"), (214, r"\text{kaksi rakoa}", "both"), (408, r"\text{reitti mitataan}", "path"))
    for px, title, kind in panels:
        w, yb, yt = 172, 250, 90
        X = lambda x: px + (x + 12) / 24 * w
        f.tex(px + w / 2, 36, title, "middle", w=180)
        # equal totals: one slit and the measured path carry the same share as the fringes, so the curves are normalised to the same area
        fn = (lambda x: inten(x, False)) if kind != "both" else (lambda x: inten(x, True) * 2)
        top = 2.0
        f.rect(px, yt - 10, w, yb - yt + 10, GLASS)
        f.add('<polyline points="' + " ".join(f"{n(X(x))},{n(yb - fn(x) / top * (yb - yt))}" for x in [-12 + 24 * k / 400 for k in range(401)])
              + f'" fill="none" stroke="{HOT}" stroke-width="3" stroke-linejoin="round"/>')
        f.arrow(px, yb, px + w, yb, INK, 2.5, 12)
        f.line(X(1.0), yt - 10, X(1.0), yb, GOOD, 2, "5 4")
        f.tex(X(1.0) + 4, yb + 22, r"x_0", "start", GOOD)
        f.tex(px + w - 4, yb + 22, r"x", "end")
        if kind != "one": f.line(px - 8, 64, px - 8, 300, RULE, 2, "6 6")
    f.tex(300, 318, r"\text{sama osumien kokonaismäärä}", "middle", MUTED, w=360)
    return f.svg()


def compton():
    f = Fig("fy84-co", 380, "Comptonin ilmiö periaatekuvana, ei mittakaavassa. Ennen: röntgenfotoni, jonka energia on hf, "
            "tulee vasemmalta levossa olevaa elektronia kohti. Jälkeen: fotoni siroaa vinosti ylös, ja sen aallonpituus on "
            "pidempi ja energia hf' pienempi; elektroni lähtee liikkeelle vinosti alas, ja sen nopeutta kuvaa sininen nuoli. "
            "Alla violetit liikemääränuolet: tulevan fotonin liikemäärä on sironneen fotonin ja elektronin liikemäärien "
            "vektorisumma.")
    f.tex(150, 22, r"\text{ennen}", "middle")
    f.tex(450, 22, r"\text{jälkeen}", "middle")
    f.line(300, 12, 300, 222, RULE, 2, "6 6")
    # before: a short-wavelength photon towards the electron at rest
    wavy(f, 24, 128, 212, 128, 16, 9, INK)
    f.tex(110, 96, r"hf", "middle")
    electron(f, 238, 128)
    f.tex(238, 162, r"e^-", "middle", COLD)
    f.tex(238, 196, r"\text{levossa}", "middle", MUTED)
    # after: the scattered photon (longer wavelength) up-right, the electron down-right
    ex, ey = 348, 128
    wavy(f, ex + 4, ey - 6, 560, 46, 30, 9, INK)
    f.tex(492, 104, r"hf'", "start")
    # the electron's path, its velocity and its momentum p_e all point along (130, 60), the p_e arrow of the triangle below
    ux, uy = 130 / math.hypot(130, 60), 60 / math.hypot(130, 60)
    P = lambda d: (ex + d * ux, ey + d * uy)
    electron(f, *P(110))
    f.arrow(*P(126), *P(212), COLD, 3, 14)
    f.tex(P(212)[0] + 6, P(212)[1] - 14, r"\overline{v}", "start", COLD)
    f.tex(P(110)[0] - 14, P(110)[1] + 30, r"e^-", "end", COLD)
    f.circle(ex, ey, 4, MUTED)
    f.line(ex, ey, *P(98), MUTED, 1.5, "4 4")
    # momentum vectors: p = p' + p_e
    f.line(12, 240, 588, 240, RULE_LIGHT, 1.5)
    ox, oy = 150, 312
    f.arrow(ox, oy, ox + 300, oy, MOMENTUM, 3.5, 16)
    f.tex(ox + 150, oy + 26, r"\overline{p} = \dfrac{h}{\lambda}", "middle", MOMENTUM, w=110)
    tipx, tipy = ox + 170, oy - 60
    f.arrow(ox, oy, tipx, tipy, MOMENTUM, 3, 14)
    f.tex(ox + 64, oy - 50, r"\overline{p}'", "end", MOMENTUM)
    f.arrow(tipx, tipy, ox + 300, oy, MOMENTUM, 3, 14)
    f.tex(ox + 258, oy - 46, r"\overline{p}_e", "start", MOMENTUM)
    f.tex(20, oy - 18, r"\text{liikemäärät}", "start", MUTED)
    return f.svg()


def hero():
    """The chapter's opening illustration: a weak-light double-slit experiment on a lab table, the screen dotted with hits."""
    f = H.hero("fy84-hero", "Kuvitus: hämärä laboratorio. Pöydällä on laser, jonka valoa himmennetään suodattimilla, kaksoisrakolevy "
               "ja varjostin. Valonsäde on niin heikko, että se on piirretty katkoviivana. Varjostimella on punaisia pisteitä, "
               "jotka tihentyvät pystysuoriksi raidoiksi. Pöydän vieressä ilmaisimen näytöllä näkyy laskuri.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy84h-wall", INK, IRON, y1=0, y2=600))
    # a faint lamp glow on the wall
    f.add(f'<ellipse cx="600" cy="250" rx="520" ry="210" fill="{METAL_EDGE}" fill-opacity="0.18"/>')
    # table
    f.rect(0, 430, 1200, 40, H.grad(f, "fy84h-top", H.SAND_DARK, H.GRAIN, y1=430, y2=470))
    f.rect(0, 470, 1200, 130, "#8a5f22")
    for x in (150, 1050): f.rect(x, 470, 26, 130, H.GRAIN)
    # laser on its stand
    f.rect(70, 352, 230, 64, H.grad(f, "fy84h-laser", ALUMINIUM, METAL_EDGE, y1=352, y2=416), INK, 3, 8)
    f.rect(296, 368, 22, 32, IRON, INK, 3, 3)
    f.rect(140, 416, 26, 16, IRON, INK, 2)
    f.rect(230, 416, 26, 16, IRON, INK, 2)
    f.circle(110, 384, 9, HOT, INK, 2)
    # filters: three grey disks on posts
    for k, x in enumerate((372, 412, 452)):
        f.rect(x - 4, 386, 8, 46, IRON)
        f.add(f'<ellipse cx="{x}" cy="384" rx="11" ry="34" fill="{MUTED}" fill-opacity="{0.55 + 0.15 * k:.2f}" stroke="{INK}" stroke-width="2.5"/>')
    # the weak beam: dashed and faint
    f.line(318, 384, 640, 384, HOT, 3, "3 12", cap="round")
    # the double-slit plate on a post
    f.rect(636, 300, 18, 130, ALUMINIUM, INK, 3, 2)
    for y in (362, 398): f.rect(640, y, 10, 10, INK)
    # the probability wave behind the slits, as faint arcs
    for r in (40, 80, 120, 160):
        for y in (367, 403):
            f.path(f"M{n(654 + r * 0.5)},{n(y - r * 0.866)} A{r},{r} 0 0 1 {n(654 + r * 0.5)},{n(y + r * 0.866)}", stroke=HOT_LIGHT, w=2, extra='stroke-opacity="0.35"')
    # the screen with its hits
    f.rect(880, 150, 230, 270, PAPER, INK, 4, 6)
    f.rect(980, 420, 30, 12, IRON)
    for x, yy in sample(900, 29):
        f.circle(995 + x * 9.5, 166 + yy * 238, 2.4, HOT)
    # a counter display on a small box
    f.rect(470, 200, 120, 76, IRON, INK, 3, 6)
    f.rect(484, 214, 92, 34, GOOD_LIGHT, INK, 2, 3)
    for k in range(4): f.rect(492 + k * 20, 222, 12, 18, GOOD)
    f.circle(500, 262, 5, HEAT_LIGHT)
    H.wire(f, (530, 276), (880, 300), sag=60, colour=MUTED, w=3)
    return f.svg()


FIGURES = {"hero": hero, "buildup": buildup, "patterns": patterns, "compton": compton}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "buildup": "reveals: random single hits build up the fringe pattern of the wave model",
    "patterns": "reveals: one slit gives no fringes, two give fringes, measuring the path removes them",
    "compton": "reveals: the scattered photon has a longer wavelength and the electron recoils; momentum triangle",
}
