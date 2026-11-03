"""Figures of the FY12 review unit fy12-mittaaminen (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy12-mittaaminen` writes them into content/fi/units/fy12-mittaaminen/unit.md. Every number drawn is computed here:
the heating series of the graph anatomy (invented example data) and the cart of the linearisation figure
(s = a t^2 / 2 with a = 0,50 m/s^2, model values)."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    SAND_DARK, GRAIN, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON,
                    GOOD, GOOD_LIGHT, PAPER)
import herolib as H
from herolib import grad, rnd


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


# the graph anatomy: water heated in a kettle, read every minute, each reading uncertain by 1,0 °C (example data)
HEAT_T = [1, 2, 3, 4, 5, 6]                                     # min
HEAT_TEMP = [24.9, 30.6, 37.8, 43.1, 50.2, 55.6]                 # °C
HEAT_DT = 1.0                                                   # °C, the uncertainty bar of each reading
HEAT_K, HEAT_B = _fit(HEAT_T, HEAT_TEMP)                        # 6,23 °C/min and 18,6 °C


def _extreme_lines():
    """The steepest and the shallowest line that still pass through every uncertainty bar (searched in small steps)."""
    ok = []
    for i in range(4000, 9000):
        k = i / 1000
        lo = max(T - k * t - HEAT_DT for t, T in zip(HEAT_T, HEAT_TEMP))
        hi = min(T - k * t + HEAT_DT for t, T in zip(HEAT_T, HEAT_TEMP))
        if lo <= hi: ok.append((k, (lo + hi) / 2))
    return ok[-1], ok[0]


# the linearisation: a cart starting from rest, s = a t^2 / 2 (model values)
CART_A = 0.50                                                   # m/s^2
CART_T = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]                          # s
CART_S = [CART_A * t * t / 2 for t in CART_T]                    # m


def hero():
    """Opening illustration of the Why question: a school lab bench. A measuring cylinder with liquid stands on a digital
    scale, a bottle beside it; in the middle an open notebook with a table and a graph whose points scatter round one
    fitted line; a ruler and a stopwatch on the right. No text, no numerals."""
    f = H.hero("fy12m-hero", "Kuvitus: koulun laboratorion työpöytä. Vasemmalla digitaalisella vaa'alla on mittalasi, jossa on nestettä, "
               "ja sen vieressä pullo. Keskellä on avoin vihko: vasemmalla sivulla mittaustaulukko ja oikealla sivulla kuvaaja, jonka "
               "pisteet ovat virhejanoineen hieman hajallaan yhden sovitetun suoran ympärillä. Oikealla pöydällä ovat viivain ja sekuntikello.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 360, grad(f, "fy12m-h-wall", "#efe7d6", PAPER))
    for k in range(6):                                         # tiles on the wall
        f.line(0, 60 + 60 * k, 1200, 60 + 60 * k, RULE_LIGHT, 2)
    f.rect(0, 360, 1200, 240, grad(f, "fy12m-h-bench", SAND, SAND_DARK))
    f.line(0, 360, 1200, 360, GRAIN, 3)
    for k in range(5):
        y = 392 + 44 * k
        f.path(f"M0,{y} q300,{n(-8 + 16 * rnd(k, 5))} 600,0 t600,0", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.45"')

    # left: the digital scale with the measuring cylinder, and a bottle
    f.add(f'<ellipse cx="190" cy="452" rx="150" ry="16" fill="{INK}" fill-opacity="0.18"/>')
    f.rect(52, 404, 276, 44, grad(f, "fy12m-h-scale", ALUMINIUM, METAL_EDGE), INK, 3, 10)
    f.rect(78, 414, 92, 24, INK, None, 2, 4)
    for k in range(3):                                         # display segments, no numerals
        f.rect(86 + 26 * k, 420, 18, 12, GOOD_LIGHT, None, 2, 2)
    f.circle(214, 426, 9, IRON, INK, 2); f.circle(248, 426, 9, IRON, INK, 2)
    f.rect(64, 392, 252, 14, IRON, INK, 2.5, 4)                # the weighing plate
    # the measuring cylinder: foot, glass tube, liquid with a meniscus, scale marks
    f.rect(118, 376, 132, 16, GLASS, INK, 2.5, 4)
    f.rect(146, 128, 76, 250, GLASS, None, 0, 0, 'fill-opacity="0.85"')
    f.rect(148, 238, 72, 138, grad(f, "fy12m-h-liquid", WATER_LIGHT, WATER), None)
    f.path("M148,238 Q184,250 220,238", WHITE, extra='fill-opacity="0.6"')
    f.path("M146,378 V128 M222,128 V378", stroke=INK, w=3)
    f.path("M140,124 Q146,128 152,126 M216,126 Q222,128 228,124", stroke=INK, w=2.5)
    for k in range(13):
        y = 360 - 18 * k
        f.line(146, y, 146 + (22 if k % 5 == 0 else 13), y, INK, 2)
    f.line(160, 150, 160, 370, WHITE, 4, cap="round")
    # the bottle
    f.path("M330,360 V250 Q330,226 350,214 V180 H378 V214 Q398,226 398,250 V360 Z", grad(f, "fy12m-h-bottle", HEAT_LIGHT, HEAT), INK, 3)
    f.rect(346, 166, 36, 16, IRON, INK, 2.5, 3)
    f.rect(336, 268, 56, 52, SAND_LIGHT, INK, 2, 4)
    f.line(346, 284, 382, 284, MUTED, 3, cap="round"); f.line(346, 300, 372, 300, MUTED, 3, cap="round")

    # middle: the open notebook, a table on the left page and a graph on the right page
    f.add(f'<path d="M444,402 L956,402 L968,560 L432,560 Z" fill="{INK}" fill-opacity="0.18"/>')
    f.path("M440,386 L696,396 L696,548 L428,544 Z", WHITE, INK, 2.5)
    f.path("M696,396 L952,386 L964,544 L696,548 Z", WHITE, INK, 2.5)
    f.line(696, 396, 696, 548, RULE, 3)
    for k in range(6):                                         # the table: rows and one column rule
        y = 418 + 22 * k
        f.line(456, y, 680, y + 2, RULE, 2)
    f.line(560, 410, 560, 534, RULE, 2)
    for k in range(5):
        y = 429 + 22 * k
        f.line(472, y, 472 + 40 + 12 * rnd(k, 2), y, MUTED, 3, cap="round")
        f.line(580, y + 1, 580 + 50 + 20 * rnd(k, 4), y + 1, COLD, 3, cap="round")
    # the graph on the right page
    gx0, gy0 = 724, 528
    for k in range(1, 10):
        f.line(gx0 + 22 * k, 412, gx0 + 22 * k, gy0, COLD_LIGHT, 1.5)
    for k in range(1, 6):
        f.line(gx0, gy0 - 22 * k, gx0 + 214, gy0 - 22 * k, COLD_LIGHT, 1.5)
    f.arrow(gx0, gy0, gx0 + 222, gy0, INK, 2.5, 11)
    f.arrow(gx0, gy0, gx0, 404, INK, 2.5, 11)
    f.line(gx0 + 6, gy0 - 14, gx0 + 206, gy0 - 108, HOT, 3.5, cap="round")
    for k, (u, d) in enumerate(((0.12, 5), (0.27, -6), (0.42, 4), (0.58, -5), (0.73, 6), (0.88, -3))):
        x = gx0 + 6 + u * 200; y = gy0 - 14 - u * 94 + d
        f.line(x, y - 13, x, y + 13, COLD, 2.5); f.line(x - 5, y - 13, x + 5, y - 13, COLD, 2.5); f.line(x - 5, y + 13, x + 5, y + 13, COLD, 2.5)
        f.circle(x, y, 5.5, COLD, WHITE, 2)
    # a pencil across the notebook
    f.add(f'<g transform="translate(640,568) rotate(-8)"><rect x="-150" y="-9" width="230" height="18" fill="{HEAT_LIGHT}" stroke="{INK}" stroke-width="2"/>'
          f'<rect x="-168" y="-9" width="18" height="18" rx="4" fill="{HOT_LIGHT}" stroke="{INK}" stroke-width="2"/>'
          f'<path d="M80,-9 L110,0 L80,9 Z" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="2"/><path d="M101,-3 L110,0 L101,3 Z" fill="{INK}"/></g>')

    # right: a ruler lying on the bench and a stopwatch
    f.add(f'<g transform="translate(1062,500) rotate(-14)"><rect x="-120" y="-20" width="240" height="40" rx="4" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="{-108 + 12 * k}" y1="-20" x2="{-108 + 12 * k}" y2="{-6 if k % 5 else 2}" stroke="{INK}" stroke-width="2"/>' for k in range(19))
          + "</g>")
    f.add(f'<ellipse cx="1060" cy="404" rx="70" ry="12" fill="{INK}" fill-opacity="0.18"/>')
    H.stopwatch(f, 1060, 320, 76, 0.18)
    return f.svg()


def kartta():
    """The overview of the lesson as one chain: from the measurement to the reported result, with what each step asks."""
    f = Fig("fy12m-kartta", 448, "Kaavio: mittauksesta tulokseen viidessä vaiheessa, jotka on yhdistetty alaspäin osoittavilla nuolilla. "
            "1 Mittaus: lukema, epävarmuus Δx ja tarkkuus. 2 Kuvaaja: akseleilla suure ja yksikkö. 3 Sovitus: suora tai "
            "linearisointi. 4 Tulkinta: kulmakerroin k ja vakiotermi b yksiköineen. 5 Tulos: k ± Δk ja mallin pätevyysalue.", size=26)
    steps = [(r"\text{Mittaus}", r"\text{lukema}, \ \Delta x, \ \text{tarkkuus}"),
             (r"\text{Kuvaaja}", r"\text{suure (yksikkö)}"),
             (r"\text{Sovitus}", r"\text{suora tai linearisointi}"),
             (r"\text{Tulkinta}", r"k \text{ ja } b \text{ yksiköineen}"),
             (r"\text{Tulos}", r"k \pm \Delta k, \ \text{pätevyysalue}")]
    colours = [(COLD_LIGHT, COLD), (COLD_LIGHT, COLD), (HEAT_LIGHT, HEAT), (HEAT_LIGHT, HEAT), (GOOD_LIGHT, GOOD)]
    top, h, gap = 14, 64, 26
    for i, ((name, note), (fill, edge)) in enumerate(zip(steps, colours)):
        y = top + i * (h + gap)
        f.rect(14, y, 572, h, WHITE, edge, 2.5, 10)
        f.rect(14, y, 196, h, fill, edge, 2.5, 10)
        f.rect(196, y + 2.5, 14, h - 5, fill)
        f.line(210, y, 210, y + h, edge, 2.5)
        f.circle(42, y + h / 2, 18, WHITE, edge, 2.5)
        f.tex(42, y + h / 2, str(i + 1), "middle")
        f.tex(70, y + h / 2, name, "start", w=132)
        f.tex(222, y + h / 2, note, "start", w=358)
        if i < len(steps) - 1:
            f.arrow(110, y + h + 2, 110, y + h + gap - 2, INK, 2.5, 12)
    return f.svg()


def anatomia():
    """The parts of a fitted graph: points with uncertainty bars, the fitted line, the steepest and the shallowest line,
    the slope read from two far-apart points of the line, and the intercept on the vertical axis."""
    (k_hi, b_hi), (k_lo, b_lo) = _extreme_lines()
    f = Fig("fy12m-anatomia", 410, "Kuvaaja mittakaavassa, keksitty esimerkkiaineisto: veden lämpötila θ celsiusasteina ajan t funktiona "
            f"minuutteina. Kuusi mittauspistettä hetkillä 1–6 min, jokaisella pystysuora epävarmuusjana ±1 °C. Pisteiden lomaan on sovitettu "
            f"yhtenäinen suora θ = {f'{HEAT_K:.1f}'.replace('.', ',')} °C/min · t + {HEAT_B:.0f} °C, ja katkoviivoina ovat jyrkin ja loivin suora, jotka "
            "vielä kulkevat kaikkien janojen kautta. Suoralle on piirretty kolmio kaukana toisistaan olevien pisteiden t = 1 min ja t = 6 min "
            "väliin: vaakasivu on Δt ja pystysivu Δθ, ja kulmakerroin on k = Δθ/Δt. Suora leikkaa pystyakselin kohdassa b, joka on alkulämpötila. "
            "Oikeassa alakulmassa on selite: katkoviiva tarkoittaa jyrkintä ja loivinta suoraa.", size=27)
    ax = Axes(f, (84, 356), (462, 60), x=(0, 7), y=(0, 60), xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[15, 30, 45, 60],
              xlabel=r"t\ (\text{min})", ylabel=r"\theta\ (^\circ\text{C})")
    ax.line([(0, b_hi), (6.6, b_hi + 6.6 * k_hi)], MUTED, 2, dash="8 6")
    ax.line([(0, b_lo), (7, b_lo + 7 * k_lo)], MUTED, 2, dash="8 6")
    ax.line([(0, HEAT_B), (6.9, HEAT_B + 6.9 * HEAT_K)], INK, 3)
    # the slope triangle between t = 1 min and t = 6 min on the fitted line
    y1, y2 = HEAT_B + HEAT_K, HEAT_B + 6 * HEAT_K
    f.line(ax.X(1), ax.Y(y1), ax.X(6), ax.Y(y1), HEAT, 2.5)
    f.line(ax.X(6), ax.Y(y1), ax.X(6), ax.Y(y2), HEAT, 2.5)
    for t, T in zip(HEAT_T, HEAT_TEMP):
        x, y0, y9 = ax.X(t), ax.Y(T - HEAT_DT), ax.Y(T + HEAT_DT)
        f.line(x, y0, x, y9, COLD, 2.5); f.line(x - 6, y0, x + 6, y0, COLD, 2.5); f.line(x - 6, y9, x + 6, y9, COLD, 2.5)
        ax.point(t, T, COLD)
    f.tex(ax.X(3.5), ax.Y(y1) + 22, r"\Delta t", "middle", HEAT)
    f.tex(ax.X(6) + 12, ax.Y((y1 + y2) / 2) + 26, r"\Delta \theta", "start", HEAT)
    f.tex(ax.X(3.2), ax.Y(52), r"k = \dfrac{\Delta \theta}{\Delta t}", "end", INK)
    f.circle(ax.X(0), ax.Y(HEAT_B), 9, "none", INK, 2)
    f.tex(ax.X(0) + 16, ax.Y(HEAT_B) + 14, "b", "start")
    lx, ly = ax.X(3.7), ax.Y(7)                                    # the legend in the empty lower right corner
    f.line(lx, ly, lx + 34, ly, MUTED, 2.5, "8 6")
    f.tex(lx + 42, ly, r"\text{jyrkin, loivin}", "start", MUTED)
    return f.svg()


def linearisointi():
    """The same cart data twice: s against t is a curve, s against t^2 a line through the origin with the slope a/2."""
    f = Fig("fy12m-linearisointi", 340, "Kaksi kuvaajaa samasta mallin aineistosta: levosta tasaisesti kiihtyvä vaunu, kiihtyvyys 0,50 m/s². "
            "Vasemmalla matka s metreinä ajan t funktiona: kuusi pistettä hetkillä 0,5–3,0 s asettuvat ylöspäin kaartuvalle käyrälle. "
            "Oikealla sama matka ajan neliön t² funktiona: pisteet ovat origon kautta kulkevalla suoralla, jonka kulmakerroin on "
            "puolet kiihtyvyydestä, 0,25 m/s².", size=27)
    left = Axes(f, (52, 284), (200, 60), x=(0, 3.5), y=(0, 2.5), xticks=[1, 2, 3], yticks=[1, 2],
                xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})", arrow_room=20)
    left.curve(lambda t: CART_A * t * t / 2, 0, 3.2, MUTED, 2, dash="7 6")
    for t, s in zip(CART_T, CART_S): left.point(t, s, COLD)
    right = Axes(f, (352, 284), (470, 60), x=(0, 10), y=(0, 2.5), xticks=[3, 6, 9], yticks=[1, 2],
                 xlabel=r"t^2\ (\text{s}^2)", ylabel=r"s\ (\text{m})", arrow_room=20)
    right.line([(0, 0), (9.8, CART_A * 9.8 / 2)], INK, 3)
    for t, s in zip(CART_T, CART_S): right.point(t * t, s, COLD)
    f.tex(right.X(5.2), right.Y(0.45), r"k = \tfrac{a}{2}", "start", INK)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "anatomia": anatomia, "linearisointi": linearisointi}
