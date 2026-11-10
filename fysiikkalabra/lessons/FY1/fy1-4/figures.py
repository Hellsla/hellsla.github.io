"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-4` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, COLD, HEAT, GOOD, RULE, fi
import math
from figlib import COLD_LIGHT, GLASS, HEAT_LIGHT, HOT_LIGHT, METAL_EDGE, SAND_DARK, SAND_LIGHT, n
import herolib as H
from figlib import ALUMINIUM, GOOD_LIGHT, GRAIN, IRON, SAND
from herolib import grad, rnd
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S

# the cart data of the lesson's first simulation case (t in s, s in m) and the line fitted to it
CART = [(1, 0.6), (2, 0.8), (3, 1.6), (4, 2.1), (5, 2.4), (6, 2.9)]
# the kettle example: water temperature T (°C) every minute
KETTLE = [(0, 20.8), (1, 27.9), (2, 36.5), (3, 43.8), (4, 52.4), (5, 59.6)]


def hero():
    """The chapter's opening illustration: measured points on grid paper, scattered a little, and a ruler laid along the one line that fits them."""
    f = S.hero("fy14-hero", "Kuvitus: ruutupaperi työpöydällä. Paperilla on mittauspisteitä virhepalkkeineen; ne eivät osu täsmälleen samalle "
               "suoralle, ja niiden poikki on vedetty yksi suora viivaimen avulla. Vieressä lyijykynä, pyyhekumi ja laskin.")
    f.rect(0, 0, 1200, 600, grad(f, "fy14h-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(10): f.path(f"M0,{24 + k * 64} q300,{n(-10 + 20 * rnd(k, 3))} 600,0 t600,0", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.5"')
    def P(u, v): return (268 + u * 680 + v * 10, 568 - v * 530 - u * 14)
    corners = [P(-0.03, -0.03), P(1.03, -0.03), P(1.03, 1.03), P(-0.03, 1.03)]
    f.add(f'<path d="M{" L".join(f"{n(x + 10)},{n(y + 12)}" for x, y in corners)} Z" fill="{INK}" fill-opacity="0.2"/>')   # shadow
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in corners) + " Z", WHITE, INK, 2)
    for k in range(1, 40):
        w = 1.5 if k % 5 else 2.2
        f.line(*P(k / 40, -0.02), *P(k / 40, 1.02), COLD_LIGHT, w); f.line(*P(-0.02, k / 40), *P(1.02, k / 40), COLD_LIGHT, w)
    f.line(*P(0.08, 0.08), *P(0.95, 0.08), INK, 3); f.line(*P(0.08, 0.08), *P(0.08, 0.95), INK, 3)
    f.path("M{},{} l-14,-6 v12 Z".format(*map(n, P(0.95, 0.08))).replace("l-14,-6 v12", "l-14,-7 v14"), INK)
    for k in range(1, 9): f.line(*P(0.08 + k * 0.1, 0.08), *P(0.08 + k * 0.1, 0.065), INK, 2); f.line(*P(0.08, 0.08 + k * 0.1), *P(0.065, 0.08 + k * 0.1), INK, 2)
    pts = [(0.17, 0.19, 0.04), (0.26, 0.33, 0.05), (0.35, 0.34, 0.04), (0.44, 0.47, 0.05), (0.53, 0.50, 0.04), (0.62, 0.61, 0.05), (0.71, 0.66, 0.04), (0.80, 0.79, 0.05)]
    a, b = P(0.11, 0.135), P(0.89, 0.855)
    f.line(*a, *b, HEAT, 4, cap="round")
    for u, v, e in pts:
        f.line(*P(u, v - e), *P(u, v + e), COLD, 2.5); f.line(*P(u - 0.01, v - e), *P(u + 0.01, v - e), COLD, 2.5); f.line(*P(u - 0.01, v + e), *P(u + 0.01, v + e), COLD, 2.5)
        x, y = P(u, v); f.circle(x, y, 8, COLD, INK, 2)
    # the transparent ruler laid beside the line
    th = math.atan2(b[1] - a[1], b[0] - a[0]); cx, cy = (a[0] + b[0]) / 2 - math.sin(th) * 50, (a[1] + b[1]) / 2 + math.cos(th) * 50
    g = (f'<g transform="translate({n(cx)},{n(cy)}) rotate({n(math.degrees(th))})"><rect x="-340" y="0" width="680" height="60" rx="5" fill="{GLASS}" fill-opacity="0.7" stroke="{METAL_EDGE}" stroke-width="2.5"/>'
         f'<rect x="-336" y="40" width="672" height="16" rx="3" fill="{WHITE}" fill-opacity="0.5"/>')
    g += "".join(f'<line x1="{-320 + 16 * k}" y1="0" x2="{-320 + 16 * k}" y2="{14 if k % 5 else 26}" stroke="{METAL_EDGE}" stroke-width="2"/>' for k in range(41))
    f.add(g + "</g>")
    # pencil, eraser and calculator beside the paper
    f.add(f'<g transform="translate(1060,330) rotate(-64)"><rect x="-170" y="-13" width="290" height="26" fill="{HEAT_LIGHT}" stroke="{INK}" stroke-width="2"/>'
          f'<line x1="-170" y1="0" x2="120" y2="0" stroke="{HEAT}" stroke-width="2"/><rect x="-196" y="-13" width="20" height="26" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2"/>'
          f'<rect x="-216" y="-13" width="22" height="26" rx="6" fill="{HOT_LIGHT}" stroke="{INK}" stroke-width="2"/>'
          f'<path d="M120,-13 L162,0 L120,13 Z" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="2"/><path d="M148,-4 L162,0 L148,4 Z" fill="{INK}"/></g>')
    f.add(f'<g transform="translate(120,470) rotate(-12)"><rect x="-50" y="-22" width="100" height="44" rx="8" fill="{HOT_LIGHT}" stroke="{INK}" stroke-width="2.5"/>'
          f'<rect x="-50" y="-22" width="38" height="44" rx="8" fill="{COLD_LIGHT}" stroke="{INK}" stroke-width="2.5"/></g>')
    f.add(f'<g transform="translate(130,190) rotate(8)"><rect x="-70" y="-110" width="140" height="220" rx="14" fill="{IRON}" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="-52" y="-92" width="104" height="44" rx="4" fill="{GOOD_LIGHT}" stroke="{INK}" stroke-width="2"/>'
          + "".join(f'<rect x="{-52 + 28 * (k % 4)}" y="{-34 + 30 * (k // 4)}" width="22" height="22" rx="4" fill="{ALUMINIUM if k % 4 < 3 else HEAT_LIGHT}" stroke="{INK}" stroke-width="1.5"/>' for k in range(20)) + "</g>")
    return f.svg()


def scatter():
    f = Fig("fy14-scatter", 350, "Kuvaaja mittakaavassa: kärryn kulkema matka s ajan t funktiona. Kuusi mittauspistettä (t = 1…6 s) on "
            "hajallaan suoran s = 0,5 m/s · t ympärillä. Pisteitä on suoran molemmin puolin: kolme yläpuolella ja kolme alapuolella, ja "
            "pystysuorat katkoviivat näyttävät kunkin pisteen poikkeaman suorasta. Suora ei kulje jokaisen pisteen kautta.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 7), y=(0, 3.5), xticks=[1, 2, 3, 4, 5, 6], yticks=[1, 2, 3],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    ax.line([(0, 0), (7, 3.5)], INK, 3)
    for t, s in CART:
        f.line(ax.X(t), ax.Y(s), ax.X(t), ax.Y(0.5 * t), MUTED, 1.5, "5 4")
    for t, s in CART:
        ax.point(t, s, COLD)
    # legend in the empty top-left corner
    f.circle(ax.X(0.35), ax.Y(3.25), 6.5, COLD, WHITE, 2)
    f.tex(ax.X(0.35) + 18, ax.Y(3.25), r"\text{mittauspisteet}", "start", COLD, w=190)
    f.line(ax.X(0.35) - 12, ax.Y(2.75), ax.X(0.35) + 12, ax.Y(2.75), INK, 3, cap="round")
    f.tex(ax.X(0.35) + 18, ax.Y(2.75), r"\text{sovitettu suora}", "start", INK, w=190)
    f.tex(ax.X(5.7) + 14, ax.Y(1.6), r"\text{poikkeama}", "start", MUTED, w=150)
    f.line(ax.X(5.7) + 10, ax.Y(1.6), ax.X(5.05), ax.Y(2.45), MUTED, 1.5)
    return f.svg()


def slope():
    f = Fig("fy14-slope", 350, "Kaavakuva mittakaavassa: suora y = kx + b, jonka kulmakerroin on 0,5 ja vakiotermi 1. Suora leikkaa y-akselin "
            "kohdassa y = b = 1. Suoralta on valittu kaksi kaukana toisistaan olevaa pistettä P₁ = (2, 2) ja P₂ = (8, 5). Kulmakolmion "
            "vaakasivu on Δx = x₂ − x₁ = 6 ja pystysivu Δy = y₂ − y₁ = 3, joten kulmakerroin on k = Δy/Δx = 0,5.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 9), y=(0, 6), xticks=[2, 4, 6, 8], yticks=[1, 2, 3, 4, 5], xlabel=r"x", ylabel=r"y")
    ax.line([(0, 1), (9, 5.5)], INK, 3)
    f.line(ax.X(2), ax.Y(2), ax.X(8), ax.Y(2), MUTED, 1.5, "6 5")
    f.line(ax.X(8), ax.Y(2), ax.X(8), ax.Y(5), MUTED, 1.5, "6 5")
    ax.point(0, 1, HEAT)
    ax.point(2, 2, COLD); ax.point(8, 5, COLD)
    f.tex(ax.X(5), ax.Y(2) + 26, r"\Delta x", "middle", w=70)
    f.tex(ax.X(7.7), ax.Y(0.95), r"k = \dfrac{\Delta y}{\Delta x}", "middle", w=150, bg=True)
    f.tex(ax.X(8) + 14, ax.Y(3.5), r"\Delta y", "start", w=70)
    f.tex(ax.X(0) + 14, ax.Y(1) - 24, r"b", "start", HEAT, w=30)
    f.tex(ax.X(2) - 8, ax.Y(2) - 30, r"P_1", "end", COLD, w=50)
    f.tex(ax.X(8) - 14, ax.Y(5) - 26, r"P_2", "end", COLD, w=50)
    f.tex(ax.X(3.4), ax.Y(4.5), r"y = kx + b", "middle", INK, w=140, bg=True)
    return f.svg()


def kettle():
    f = Fig("fy14-kettle", 350, "Kuvaaja mittakaavassa: vedenkeittimen veden lämpötila T ajan t funktiona. Kuusi mittauspistettä minuutin "
            "välein on suoran T = 8,0 °C/min · t + 20 °C ympärillä. Suoralta on luettu kaksi kaukana toisistaan olevaa pistettä, (0 min; 20 °C) "
            "ja (5,0 min; 60 °C). Katkoviiva näyttää, että suora saavuttaa 40 °C:n lämpötilan ajassa 2,5 min.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 6), y=(0, 70), xticks=[1, 2, 3, 4, 5, 6], yticks=[20, 40, 60],
              xlabel=r"t\ (\text{min})", ylabel=r"T\ ({}^\circ\text{C})")
    ax.line([(0, 20), (6, 68)], INK, 3)
    ax.guide(2.5, 40, GOOD)
    for t, T in KETTLE:
        ax.point(t, T, COLD)
    f.circle(ax.X(0), ax.Y(20), 11, "none", HEAT, 2.5)
    f.circle(ax.X(5), ax.Y(60), 11, "none", HEAT, 2.5)
    f.tex(ax.X(0) + 20, ax.Y(20) + 30, r"A", "start", HEAT, w=30)
    f.tex(ax.X(5) + 4, ax.Y(60) + 34, r"B", "start", HEAT, w=30)
    f.line(ax.X(2.5), ax.Y(0), ax.X(2.5), ax.Y(0) + 7, GOOD, 2)
    f.tex(ax.X(2.5), ax.Y(0) + 24, r"2{,}5", "middle", GOOD, w=34, bg=True)
    return f.svg()


def reading():
    """Not in lesson.md: the graph of the inquiry task 'kuvaajasta' (inquiry.json), a line s = 15 km/h t + 5 km read at two grid crossings."""
    f = Fig("fy14-reading", 350, "Kuvaaja mittakaavassa: pyöräilijän matka s ajan t funktiona. Suora leikkaa pystyakselin kohdassa 5 km ja kulkee "
            "ruudukon risteyskohtien (1,0 h; 20 km) ja (3,0 h; 50 km) kautta. Pisteet P₁ ja P₂ on merkitty suoralle.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 3.5), y=(0, 60), xticks=[1, 2, 3], yticks=[10, 20, 30, 40, 50],
              xlabel=r"t\ (\text{h})", ylabel=r"s\ (\text{km})")
    ax.line([(0, 5), (3.5, 57.5)], INK, 3)
    ax.point(1, 20, COLD); ax.point(3, 50, COLD)
    f.tex(ax.X(1) + 16, ax.Y(20) + 30, r"P_1", "start", COLD, w=50)
    f.tex(ax.X(3) - 16, ax.Y(50) + 30, r"P_2", "end", COLD, w=50)
    return f.svg()


def scatter_points():
    """The data of `scatter` without the fitted line, for a task that asks the student to fit it (scripts/figcat.py
    variant): axes to 9 s and 4,5 m so the line can be continued; the description lists the points, not the line."""
    f = Fig("fy14-scatter-points", 350, "Kuvaaja mittakaavassa: kärryn kulkema matka s ajan t funktiona, kuusi mittauspistettä ilman sovitettua suoraa. "
            "Pisteet ovat (1 s; 0,6 m), (2 s; 0,8 m), (3 s; 1,6 m), (4 s; 2,1 m), (5 s; 2,4 m) ja (6 s; 2,9 m). Aika-akseli jatkuu 9 sekuntiin "
            "ja matka-akseli 4,5 metriin, ruudukon väli on 1 s ja 0,5 m.")
    ax = Axes(f, (96, 300), (470, 52), x=(0, 9), y=(0, 4.5), xticks=[1, 2, 3, 4, 5, 6, 7, 8, 9], yticks=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})", yfmt=lambda v: fi(v) if float(v).is_integer() else "")
    for t, s in CART:
        ax.point(t, s, COLD)
    return f.svg()


def candle():
    """Task illustration (fy1-4-L1-04): a candle burning on a saucer; no numbers."""
    f = S.scene("fy14-candle", "Kuvitus: kynttilä palaa lautasella hämärässä huoneessa. Liekin ympärillä on valokehä, ja kynttilän kyljessä on valunutta steariinia.")
    f.rect(0, 0, 600, 360, "#3b3f4a")
    f.add('<circle cx="300" cy="120" r="150" fill="#ffd8a8" opacity="0.12"/><circle cx="300" cy="120" r="80" fill="#ffd8a8" opacity="0.18"/>')
    f.rect(0, 280, 600, 80, "#5a4636"); f.rect(0, 278, 600, 4, "#6e5644")
    f.add('<ellipse cx="300" cy="284" rx="110" ry="16" fill="#d9dee3"/><ellipse cx="300" cy="280" rx="84" ry="10" fill="#eef0f2"/>')
    wax = "#f6efe0"
    f.rect(262, 150, 76, 130, wax, S.dark(wax, 0.3), S.W_OBJ)
    f.rect(312, 150, 26, 130, S.dark(wax, 0.08))
    f.add(f'<ellipse cx="300" cy="150" rx="38" ry="8" fill="{S.dark(wax, 0.06)}" stroke="{S.dark(wax, 0.3)}" stroke-width="{S.W_OBJ}"/>')
    f.path("M272,150 q-4,26 2,40 q6,6 8,-4 q2,-18 0,-36 Z", wax, S.dark(wax, 0.25), 1.25)     # a drip
    f.line(300, 150, 300, 128, "#2b2f36", 3)
    f.add('<path d="M300,64 C318,92 318,118 300,132 C282,118 282,92 300,64 Z" fill="#ffc078"/>'
          '<path d="M300,86 C310,104 310,118 300,128 C290,118 290,104 300,86 Z" fill="#fff3bf"/>'
          '<ellipse cx="300" cy="128" rx="5" ry="7" fill="#4dabf7" opacity="0.7"/>')
    return f.svg()


def spring_masses():
    """Task illustration (fy1-4-L2-05): a steel spring hangs from a stand with a slotted mass; spare masses on the table; no numbers."""
    f = S.scene("fy14-spring", "Kuvitus: teräsjousi riippuu telineestä, ja sen alapäässä on punnusripustin ja punnuksia. Pöydällä on lisää punnuksia "
                "ja viivain jousen venymän mittaamiseen.")
    f.rect(0, 0, 600, 360, "#f3efe6")
    H.wood(f, 0, 310, 600, 50, "fy14s-top")
    metal = "#c4ccd4"
    f.rect(100, 296, 170, 14, "#6c757d", S.dark("#6c757d", 0.35), S.W_OBJ, 3)
    f.rect(120, 30, 12, 268, metal, S.dark(metal, 0.45), S.W_OBJ, 2)
    f.rect(120, 30, 150, 10, metal, S.dark(metal, 0.45), S.W_OBJ, 2)
    x, y0, coils, L = 240, 40, 14, 120
    pts = " ".join(f"{n(x + (10 if k % 2 else -10))},{n(y0 + 10 + k * L / coils)}" for k in range(coils + 1))
    f.add(f'<polyline points="{x},{y0} {x},{y0 + 10} {pts} {x},{y0 + L + 22}" fill="none" stroke="#5b636d" stroke-width="2.5" stroke-linejoin="round"/>')
    f.line(x, y0 + L + 22, x, y0 + L + 40, "#5b636d", 2)
    for k in range(3):                                                              # slotted masses on the hanger
        f.rect(x - 22, y0 + L + 40 + k * 14, 44, 13, "#8a929c", S.dark("#8a929c", 0.4), 1.5, 2)
    ry = 120
    f.rect(296, ry, 22, 190, "#f1dfb5", S.dark("#f1dfb5", 0.4), S.W_OBJ, 2)         # ruler beside the spring
    for k in range(37): f.line(296, ry + 5 + k * 5, 296 + (12 if k % 10 == 0 else 8 if k % 5 == 0 else 5), ry + 5 + k * 5, "#3a4350", 1)
    for k, xx in enumerate((400, 446, 492)):
        for j in range(3 - k % 2):
            f.rect(xx - 18, 296 - 13 * (j + 1), 36, 12, "#8a929c", S.dark("#8a929c", 0.4), 1.5, 2)
    return f.svg()


FIGURES = {"hero": hero, "candle": candle, "spring-masses": spring_masses, "scatter": scatter, "slope": slope, "kettle": kettle, "scatter-points": scatter_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "candle": "safe: the situation only, a burning candle; no numbers",
    "spring-masses": "safe: the situation only, a spring with slotted masses and a ruler; no readings",
    "scatter": "reveals: the fitted line s = 0,5 m/s · t (scatter-points is the same data without it)",
    "scatter-points": "safe: the six points only, axes to 9 s for an extrapolation",
    "slope": "reveals: the slope 0,5 and the intercept 1",
    "kettle": "reveals: the fitted line, the two points read off and 40 °C at 2,5 min",
}
