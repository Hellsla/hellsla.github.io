"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-10` writes them into lesson.md.
Colours: the wave's propagation (a velocity) is blue COLD as in FY4/FY5; a displacement is ink, never force red."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, COLD_LIGHT, GLASS, ICE, SAND, SAND_LIGHT,
                    SAND_DARK, GRAIN, METAL_EDGE, IRON, ALUMINIUM, COPPER, HEAT, HEAT_LIGHT, HOT, GOOD, GOOD_LIGHT, WATER, WATER_LIGHT)
import herolib as H

ROPE = GRAIN            # a rope is drawn in the brown of sand grains, 5 px
SPRING = METAL_EDGE     # a steel spring's coils


def rope_path(fn, x0, x1, step=3):
    pts = []
    x = x0
    while x <= x1 + 1e-9:
        pts.append(f"{n(x)},{n(fn(x))}")
        x += step
    return "M" + " L".join(pts)


def double_arrow(f, x1, y1, x2, y2, color=INK, w=2.5, head=12):
    """A two-headed arrow: the to-and-fro motion of one point of the medium."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    f.arrow(mx, my, x1, y1, color, w, head)
    f.arrow(mx, my, x2, y2, color, w, head)


def dimension(f, x1, x2, y, label, color=INK, above=True):
    """A dimension line with end ticks between x1 and x2 at height y, its label centred above or below."""
    f.line(x1, y, x2, y, color, 2)
    f.line(x1, y - 8, x1, y + 8, color, 2)
    f.line(x2, y - 8, x2, y + 8, color, 2)
    f.tex((x1 + x2) / 2, y - 20 if above else y + 22, label, "middle", color)


def types():
    """Ydinajatus: a transverse wave on a rope (points move up and down) and a longitudinal wave on a spring
    (coils move to and fro along it, compressions and rarefactions); both travel to the right."""
    f = Fig("fy510-types", 412, "Kaavakuva, ei mittakaavassa. Ylhäällä poikittainen aalto: naru on siniaallon muotoinen, ja sininen "
            "nuoli osoittaa aallon etenemissuunnan oikealle. Kolmessa narun kohdassa pystysuora kaksipäinen nuoli näyttää, "
            "että kohta liikkuu ylös ja alas eli kohtisuoraan etenemissuuntaa vastaan. Alhaalla pitkittäinen aalto: pitkän "
            "kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harvennus). Yhden kierroksen "
            "yllä vaakasuora kaksipäinen nuoli näyttää, että kierros liikkuu edestakaisin jousen suuntaisesti. Sininen nuoli "
            "osoittaa tämänkin aallon etenemissuunnan oikealle.")
    # --- transverse ---
    f.tex(24, 24, r"\text{poikittainen aalto}", "start")
    f.arrow(440, 24, 560, 24, COLD, 3.5, 16)
    f.tex(432, 24, r"v", "end", COLD)
    y0, A, lam, xs = 112, 40, 200, 60
    yf = lambda x: y0 - A * math.sin(2 * math.pi * (x - xs) / lam)
    f.line(xs, y0, 580, y0, RULE, 1.5, "6 5")
    f.path(rope_path(yf, xs, 576), stroke=ROPE, w=5, extra='stroke-linecap="round"')
    for k in range(0, 21):
        x = xs + k * 25
        f.circle(x, yf(x), 3.5, INK)
    for x in (110, 260, 410):                                           # at a crest, a zero crossing and a trough
        double_arrow(f, x, y0 - A - 10, x, y0 + A + 10)
    f.tex(110, 184, r"\text{kohdan liike}", "middle")
    f.line(12, 208, 588, 208, RULE, 2, "6 6")
    # --- longitudinal ---
    f.tex(24, 226, r"\text{pitkittäinen aalto}", "start")
    f.arrow(440, 226, 560, 226, COLD, 3.5, 16)
    f.tex(432, 226, r"v", "end", COLD)
    yc, a, lamL, step = 304, 16, 200, 15
    xsL = 60
    f.line(xsL - 6, yc, 572, yc, IRON, 1.5)
    for k in range(0, 34):
        x0 = xsL + k * step
        x = x0 + a * math.sin(2 * math.pi * (x0 - xsL) / lamL)
        col, w = (INK, 3) if k == 4 else (SPRING, 2.5)                   # coil 4 is the one whose motion is marked
        f.add(f'<ellipse cx="{n(x)}" cy="{yc}" rx="5" ry="30" fill="none" stroke="{col}" stroke-width="{w}"/>')
    # compressions where the coils crowd (x0 − xs = λ/2 + nλ), rarefactions between; coil 4 sits at x0 = 120
    xm = 120 + a * math.sin(2 * math.pi * 60 / lamL)
    double_arrow(f, xm - a - 6, 262, xm + a + 6, 262)
    f.tex(xm + a + 14, 262, r"\text{kierroksen liike}", "start")
    f.tex(160, 354, r"\text{tihentymä}", "middle")
    f.tex(360, 354, r"\text{tihentymä}", "middle")
    f.tex(260, 384, r"\text{harvennus}", "middle")
    f.tex(460, 384, r"\text{harvennus}", "middle")
    return f.svg()


def birth():
    """Kaava: the wave is born at the source; after T/4, T/2, 3T/4 and T the front has gone λ/4, λ/2, 3λ/4 and λ."""
    f = Fig("fy510-birth", 420, "Kaavakuva: narun pää alkaa heilua ylös ja alas, ja narusta on piirretty neljä kuvaa allekkain hetkillä "
            "neljäsosa jaksonajasta, puolet, kolme neljäsosaa ja koko jaksonaika. Katkoviiva näyttää, mihin asti aalto on "
            "kunakin hetkenä edennyt: neljäsosan aallonpituudesta, puolet, kolme neljäsosaa ja koko aallonpituuden. "
            "Alimman kuvan alla mittajana näyttää, että yhden jaksonajan aikana aalto on edennyt yhden aallonpituuden. "
            "Rintaman takana naru on levossa.")
    xs, lam, A = 120, 320, 24
    rows = [(r"t = \tfrac{1}{4}T", 0.25, 58), (r"t = \tfrac{1}{2}T", 0.5, 140), (r"t = \tfrac{3}{4}T", 0.75, 222), (r"t = T", 1.0, 304)]
    for label, frac, yr in rows:
        front = xs + frac * lam
        def yf(x, frac=frac, yr=yr):
            u = (x - xs) / lam
            return yr - (A * math.sin(2 * math.pi * (frac - u)) if u <= frac else 0.0)
        f.tex(98, yr, label, "end")
        f.line(front, yr - 36, front, yr + 36, MUTED, 1.5, "6 5")
        f.path(rope_path(yf, xs, 576), stroke=ROPE, w=5, extra='stroke-linecap="round"')
        f.rect(xs - 16, yf(xs) - 9, 16, 18, SAND_DARK, INK, 2, 3)        # the hand's handle
    f.arrow(470, 360, 560, 360, COLD, 3.5, 16)
    f.tex(462, 360, r"v", "end", COLD)
    dimension(f, xs, xs + lam, 364, r"\lambda", INK, above=False)
    return f.svg()


def graphs():
    """Kaava: the same wave as a snapshot (x, y) with λ and as one point's (t, y) graph with T; λ = 1,0 m, T = 0,50 s."""
    f = Fig("fy510-graphs", 556, "Kaksi kuvaajaa samasta aallosta allekkain, amplitudi 4 cm. Ylempi on valokuva koko narusta yhdellä "
            "hetkellä: vaaka-akselilla paikka x metreinä nollasta 2,5 metriin ja pystyakselilla poikkeama y senttimetreinä. "
            "Kahden peräkkäisen harjan väli, 1,0 m, on merkitty aallonpituudeksi lambda ja harjan korkeus amplitudiksi A. "
            "Alempi on yhden narun kohdan poikkeama ajan funktiona: vaaka-akselilla aika t sekunteina nollasta 1,25 sekuntiin. "
            "Kahden peräkkäisen huipun väli, 0,50 s, on merkitty jaksonajaksi T. Kuvaajat näyttävät samanmuotoisilta, mutta "
            "niiden vaaka-akselien suureet ovat eri.")
    f.tex(24, 22, r"\text{valokuva: koko naru yhdellä hetkellä}", "start")
    f.tex(24, 310, r"\text{yksi kohta: poikkeama ajan funktiona}", "start")
    f.line(12, 282, 588, 282, RULE, 2, "6 6")
    for top, xr, xmax, xlab, period, sym, ticks in (
            (0, (0, 2.5), 2.5, r"x\ (\text{m})", 1.0, r"\lambda", [0.5, 1.0, 1.5, 2.0, 2.5]),
            (286, (0, 1.25), 1.25, r"t\ (\text{s})", 0.5, r"T", [0.25, 0.5, 0.75, 1.0, 1.25])):
        ax = Axes(f, (96, top + 236), (476, top + 104), x=xr, y=(-6, 6), xticks=ticks, yticks=[-4, 0, 4],
                  xlabel=xlab, ylabel=r"y\ (\text{cm})", x_at=0, xfmt=lambda v: "", origin_label=False)
        for t in ticks:
            f.tex(ax.X(t), top + 256, fi(t), "middle", MUTED)
        c1 = 0.25 if top == 0 else 0.125                                # the first crest or peak
        ax.curve(lambda u, c1=c1, period=period: 4 * math.cos(2 * math.pi * (u - c1) / period), 0, xmax, INK, 3)
        c2 = c1 + period
        dimension(f, ax.X(c1), ax.X(c2), ax.Y(5.2), sym, INK)
        f.line(ax.X(c1), ax.Y(4), ax.X(c1), ax.Y(5.2) + 8, MUTED, 1.5, "5 4")
        f.line(ax.X(c2), ax.Y(4), ax.X(c2), ax.Y(5.2) + 8, MUTED, 1.5, "5 4")
        xa = ax.X(c1)                                                   # the amplitude under the first crest
        f.arrow(xa, ax.Y(0), xa, ax.Y(4), INK, 2, 10)
        f.tex(xa + 7, ax.Y(0.9), "A", "start")
    return f.svg()


def snapshot():
    """Task figure (tarkistus 2): a rope's snapshot, crests at x = 0,5, 2,0 and 3,5 m on gridlines, A = 4 cm; no λ marked."""
    f = Fig("fy510-snapshot", 320, "Kuvaaja mittakaavassa: narun valokuva yhdellä hetkellä. Vaaka-akselilla paikka x metreinä nollasta "
            "neljään metriin, apuviivat puolen metrin välein ja lukuarvot metrin välein. Pystyakselilla poikkeama y "
            "senttimetreinä, apuviivat kahden senttimetrin välein. Naru on siniaallon muotoinen, ja sen harjat, korkeudella "
            "4 cm, ovat kohdissa 0,5 m, 2,0 m ja 3,5 m. Aallonpituutta ei ole merkitty.")
    ticks = [0.5 * k for k in range(1, 9)]
    ax = Axes(f, (80, 270), (500, 64), x=(0, 4), y=(-6, 6), xticks=ticks, yticks=[-6, -4, -2, 0, 2, 4, 6],
              xlabel=r"x\ (\text{m})", ylabel=r"y\ (\text{cm})", x_at=0, xfmt=lambda v: "", origin_label=False,
              yfmt=lambda v: fi(v) if v in (-4, 0, 4) else "")
    for t in (1, 2, 3, 4):
        f.tex(ax.X(t), 292, fi(t), "middle", MUTED)
    ax.curve(lambda x: 4 * math.cos(2 * math.pi * (x - 0.5) / 1.5), 0, 4, INK, 3)
    return f.svg()


def history():
    """Task figure (exercise L2-01): one point's (t, y) graph, T = 0,40 s (upward zero crossings at 0, 0,40 s …), A = 5 cm."""
    f = Fig("fy510-history", 320, "Kuvaaja mittakaavassa: narun yhden kohdan poikkeama y senttimetreinä ajan t funktiona nollasta "
            "kahteen sekuntiin. Aika-akselilla apuviivat 0,2 sekunnin välein ja lukuarvot 0,4 sekunnin välein. Käyrä on "
            "siniaalto, jonka huiput ovat korkeudella 5 cm. Käyrä alkaa nollasta ylöspäin ja leikkaa aika-akselin ylöspäin "
            "noustessaan hetkillä 0, 0,4, 0,8, 1,2, 1,6 ja 2,0 s.")
    ticks = [0.2 * k for k in range(1, 11)]
    ax = Axes(f, (80, 270), (500, 64), x=(0, 2.0), y=(-6, 6), xticks=ticks, yticks=[-5, 0, 5],
              xlabel=r"t\ (\text{s})", ylabel=r"y\ (\text{cm})", x_at=0, xfmt=lambda v: "", origin_label=False)
    for t in (0.4, 0.8, 1.2, 1.6, 2.0):
        f.tex(ax.X(t), 292, fi(round(t, 1)), "middle", MUTED)
    ax.curve(lambda t: 5 * math.sin(2 * math.pi * t / 0.4), 0, 2.0, INK, 3, steps=240)
    return f.svg()


def hero():
    """Opening illustration: at a summer cottage a girl has flicked the end of a long rope once; the single hump runs
    along the taut rope towards a post with a bell hanging from its arm. One scale for the yard (about 100 px/m: the
    girl 1,6 m, the rope 6,3 m, the post 2 m); the cottage, sauna and shore trees stand farther back and are smaller."""
    f = H.hero("fy510-hero", "Kuvitus: kesämökin piha järven rannalla. Vasemmalla tyttö pitelee pitkän narun päätä. Hän on "
               "juuri heilauttanut narua kerran. Narun toinen pää on sidottu puutolppaan, jonka "
               "varresta roikkuu messinkinen kello. Kireän narun keskivaiheilla on yksi kumpu matkalla kohti tolppaa. "
               "Taustalla ovat järvi, metsäinen ranta, punainen mökki, sauna ja koivuja.")
    H.sky(f, "fy510h", 330)
    H.cloud(f, 250, 80, 0.75); H.cloud(f, 760, 56, 0.5); H.cloud(f, 1080, 120, 0.6)
    # far shore and the lake
    H.forest(f, 268, 40, 24, METAL_EDGE, seed=5, depth=12)
    H.forest(f, 282, 30, 20, GOOD, seed=2, depth=10)
    f.rect(0, 290, 1200, 60, H.grad(f, "fy510h-lake", WATER_LIGHT, WATER, y1=290, y2=350))
    for k, (x, y, L) in enumerate(((120, 306, 90), (420, 318, 70), (700, 304, 110), (980, 322, 80), (560, 334, 60))):
        f.line(x, y, x + L, y, WHITE, 3, cap="round")
    # the yard: lawn rising from the shore, a sand path
    f.path("M0,352 Q300,336 620,346 T1200,340 V600 H0 Z", H.grad(f, "fy510h-grass", GOOD_LIGHT, GOOD, y1=340, y2=600))
    f.path("M0,600 Q240,520 520,500 T1200,470 V510 Q820,520 560,546 T120,600 Z", SAND_LIGHT)
    # farther back (about 40 px/m): the red cottage, the sauna by the shore, birches and spruces
    H.red_house(f, 760, 382, 220, 88)
    H.red_house(f, 330, 368, 110, 56)
    H.spruce(f, 690, 388, 120); H.spruce(f, 1170, 376, 120); H.spruce(f, 470, 372, 90)
    H.birch(f, 1110, 384, 150); H.birch(f, 70, 430, 250)
    # the post (2 m) with an arm, the bell hanging from it
    px, py = 1000, 548
    f.add(f'<ellipse cx="{px}" cy="{py + 4}" rx="34" ry="7" fill="{INK}" fill-opacity="0.18"/>')
    f.rect(px - 13, py - 224, 26, 224, H.grad(f, "fy510h-post", SAND_DARK, SAND, horizontal=True), INK, 3, 3)
    f.rect(px - 13, py - 230, 90, 18, SAND_DARK, INK, 3, 3)                     # arm
    f.path(f"M{px + 13},{py - 182} L{px + 46},{py - 212}", stroke=GRAIN, w=7, extra='stroke-linecap="round"')   # brace
    bx, by = px + 58, py - 212                                                   # the bell's hanger
    f.line(bx, by, bx, by + 10, INK, 3)
    f.path(f"M{bx - 17},{by + 48} Q{bx - 18},{by + 12} {bx},{by + 10} Q{bx + 18},{by + 12} {bx + 17},{by + 48} L{bx + 24},{by + 58} H{bx - 24} Z",
           H.grad(f, "fy510h-bell", HEAT_LIGHT, COPPER), INK, 3)
    f.circle(bx, by + 64, 6, IRON, INK, 2)
    # the girl (about 110 px/m, 1,6 m), her hand back at rest after the single flick
    gx, gy = 200, 562
    f.add(f'<ellipse cx="{gx}" cy="{gy + 2}" rx="50" ry="9" fill="{INK}" fill-opacity="0.18"/>')
    hand = (292, 446)
    H.walker(f, gx, gy, HEAT, COLD, 0.46, lean=4, hand=hand, stride=0.5)
    # the rope: tied to the post at 1 m, taut and nearly level, one hump on its way (a smooth pulse about 1,5 m long)
    tie = (px - 13, py - 110)
    def ry(x):
        t = (x - hand[0]) / (tie[0] - hand[0])
        base = hand[1] + (tie[1] - hand[1]) * t + 5 * math.sin(math.pi * t)
        bump = 74 * math.exp(-((x - 630) / 58) ** 2)
        return base - bump
    pts = " L".join(f"{n(x)},{n(ry(x))}" for x in range(hand[0], int(tie[0]) + 1, 4))
    f.path("M" + pts, stroke=INK, w=10, extra='stroke-linecap="round"')
    f.path("M" + pts, stroke=COPPER, w=6, extra='stroke-linecap="round"')
    f.path(f"M{tie[0] - 2},{tie[1] - 9} h30 M{tie[0] - 2},{tie[1] + 9} h30", stroke=COPPER, w=5)     # the knot round the post
    f.circle(hand[0], hand[1], 11, SAND_LIGHT, INK, 2)
    return f.svg()


def scene():
    """Beside the summary: a wave going round a stadium stand, spectators rising and sitting down in turn."""
    f = H.scene("fy510-scene", "Kuvitus: stadionin katsomo. Kolmessa rivissä istuu katsojia, ja keskellä joukko katsojia on noussut "
                "seisomaan kädet ylhäällä. Seisovien vieressä katsojat ovat puoliksi nousseet tai istuutumassa. Katsojat "
                "eivät vaihda paikkaa, mutta nousemisen kohta kiertää katsomossa.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy510s-sky", ICE, GLASS))
    shirts = [COLD, HEAT, GOOD, COPPER, HOT, IRON]
    for r, (ybase, sc) in enumerate(((180, 0.62), (260, 0.7), (346, 0.78))):
        f.rect(0, ybase - 6, 600, 18 + 6 * r, METAL_EDGE)
        f.rect(0, ybase + 12 + 6 * r, 600, 80, ALUMINIUM)
        for k in range(12):
            x = 30 + k * 50 + (r % 2) * 22
            if x > 590: continue
            lift = math.exp(-((x - 300) / 70) ** 2)                      # how far up each spectator is
            yb = ybase - 4
            hgt = (54 + 52 * lift) * sc
            col = shirts[(k + 2 * r) % len(shirts)]
            f.rect(x - 15 * sc, yb - hgt, 30 * sc, hgt, col, rx=8 * sc)
            f.circle(x, yb - hgt - 15 * sc, 13 * sc, SAND_LIGHT)
            if lift > 0.45:
                for sgn in (-1, 1):
                    f.path(f"M{n(x + sgn * 11 * sc)},{n(yb - hgt + 6 * sc)} L{n(x + sgn * 22 * sc)},{n(yb - hgt - 40 * sc)}",
                           stroke=col, w=9 * sc, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "types": types, "birth": birth, "graphs": graphs,
           "valokuva": snapshot, "yt-kuvaaja": history}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "types": "reveals: points of a transverse wave move across, coils of a longitudinal wave along the direction of travel",
    "birth": "reveals: in one period the wave advances one wavelength (v = λ/T)",
    "graphs": "reveals: λ is read off a snapshot (x, y) and T off one point's (t, y) graph",
    "valokuva": "safe: a rope's snapshot, crests at 0,5, 2,0 and 3,5 m on gridlines, λ not marked",
    "yt-kuvaaja": "safe: one point's (t, y) graph over 0–2,0 s, upward zero crossings every 0,4 s, T not marked",
}
