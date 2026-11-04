"""Figures of the unit fy9-kokeellisuus (FY9, the exam review course; scripts/figlib.py, herolib.py).
`python3 scripts/units.py figures fy9-kokeellisuus` writes them into content/fi/units/fy9-kokeellisuus/unit.md.

hero   the opening illustration: a school lab bench with a pendulum on a stand, a stopwatch, a metre stick and a
       notebook with measured points and a fitted line (no text)
kartta the overview of an experimental task: plan (question, variables, instruments) and analysis (graph, result
       with its uncertainty, error sources and conclusion) as one loop
virhe  the theory graph: mass against volume of cooking oil weighed in a beaker that was not tared. The fitted line
       has the slope rho and the intercept 52 g, the beaker's mass: a systematic error moves the line, not its slope.
       Data: m = 52,0 g + 0,910 g/cm^3 * V plus small invented scatter (example data)."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, COLD, COLD_LIGHT, HOT, HEAT, HEAT_LIGHT,
                    SAND, SAND_LIGHT, SAND_DARK, GRAIN, ALUMINIUM, METAL_EDGE, IRON, COPPER, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

# the theory graph's data (example data, invented and rounded)
V_OIL = [20, 40, 60, 80, 100]                    # cm^3
M_OIL = [70.4, 88.6, 106.9, 124.5, 143.3]        # g, beaker included (52,0 g) + 0,910 g/cm^3 * V + scatter


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def hero():
    """The lab bench of an experimental task: a pendulum swinging on a stand, a stopwatch, a metre stick and an
    open notebook with measured points and the straight line fitted through them."""
    f = H.hero("fy9ko-hero", "Kuvitus: koulun laboratorion pöytä. Vasemmalla teräksisessä telineessä riippuu langan "
               "varassa kuparinen heilurin punnus, joka on heilahtanut sivuun; katkoviivakaari näyttää heilahduksen. "
               "Pöydällä on metrimitta ja sekuntikello. Oikealla on avoin vihko, jonka ruudukolla on mittauspisteitä "
               "ja niiden lomitse vedetty suora. Kuvassa ei ole tekstiä.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 430, H.grad(f, "fy9ko-wall", "#fbf8f1", PAPER))
    for x in range(0, 1201, 100): f.line(x, 0, x, 430, RULE_LIGHT, 1.5)          # a tiled lab wall, faint
    H.window(f, 860, 60, 240, 200, "fy9ko-win")
    # the bench
    f.rect(0, 430, 1200, 170, H.grad(f, "fy9ko-bench", SAND_DARK, SAND))
    f.line(0, 430, 1200, 430, INK, 3)
    for k in range(1, 4): f.path(f"M0,{430 + 40 * k} q300,-8 600,0 t600,0", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.5"')
    # the stand: base, rod, arm and clamp
    st = H.steel(f, "fy9ko-steel", vertical=False)
    f.rect(150, 410, 220, 24, IRON, INK, 2.5, 4)
    f.rect(196, 80, 14, 332, st, INK, 2)
    f.rect(196, 92, 250, 14, H.steel(f, "fy9ko-steel2", vertical=True), INK, 2)
    f.rect(420, 84, 30, 30, IRON, INK, 2, 3)
    # the pendulum: the string from the clamp, swung out by 14 degrees; the dashed arc of the swing
    px, py, L = 435, 114, 250
    a = math.radians(14)
    bx, by = px + L * math.sin(a), py + L * math.cos(a)
    f.path(f"M{n(px - L * math.sin(a))},{n(py + L * math.cos(a))} A{L},{L} 0 0 0 {n(bx)},{n(by)}", stroke=MUTED, w=2, extra='stroke-dasharray="8 7"')
    f.line(px, py, px, py + L, RULE, 2, "6 6")                                   # the rest position, faint
    f.line(px, py, bx, by, INK, 2.5)
    f.defs_add(f'<radialGradient id="fy9ko-bob" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="#e2a06d"/><stop offset="1" stop-color="{COPPER}"/></radialGradient>')
    f.circle(bx, by + 20, 24, "url(#fy9ko-bob)", INK, 2.5)
    # the metre stick on the bench, with its scale
    f.rect(120, 470, 520, 30, "#f7e7a6", INK, 2.5, 3)
    for k in range(0, 51):
        x = 130 + k * 10
        f.line(x, 470, x, 470 + (14 if k % 10 == 0 else 9 if k % 5 == 0 else 6), INK, 1.5)
    # the stopwatch
    H.stopwatch(f, 720, 500, 46, 0.31)
    # the notebook: two pages, a grid, points and a fitted line
    f.path("M800,560 L815,330 L1000,322 L1000,552 Z", WHITE, INK, 2.5)
    f.path("M1000,552 L1000,322 L1185,330 L1170,560 Z", "#fbfbf7", INK, 2.5)
    f.line(1000, 322, 1000, 552, MUTED, 2)
    for k in range(1, 11):                                                       # grid on the right page
        y = 330 + k * 21
        f.line(1004, y, 1181 - k * 0.6, y, COLD_LIGHT, 1.5)
    for k in range(1, 9):
        x = 1000 + k * 20
        f.line(x, 326, x - k * 0.4, 552, COLD_LIGHT, 1.5)
    for k in range(1, 9):                                                        # lines of text on the left page
        y = 350 + k * 22
        f.line(830, y, 980 - (40 if k % 3 == 0 else 0), y, RULE, 2)
    f.line(1018, 536, 1018, 340, INK, 2); f.line(1018, 536, 1168, 536, INK, 2)    # the axes
    f.line(1022, 520, 1162, 372, COLD, 3, cap="round")                           # the fitted line
    for (x, y) in [(1040, 503), (1065, 470), (1090, 452), (1112, 418), (1138, 404), (1156, 375)]:
        f.circle(x, y, 5.5, INK, WHITE, 1.5)
    # a pencil beside the notebook
    f.path("M770,585 L905,566 L912,575 L777,594 Z", HEAT_LIGHT, INK, 2)
    f.path("M905,566 L924,569 L912,575 Z", SAND_LIGHT, INK, 1.5)
    return f.svg()


def kartta():
    """The loop of an experimental task: plan on the left (question and hypothesis, variables, instruments and
    repeats), analysis on the right (table and graph, result with uncertainty, error sources and conclusion)."""
    f = Fig("fy9ko-kartta", 380, "Kaavakuva kokeellisen tehtävän vaiheista kahtena sarakkeena. Vasemmalla suunnittelu "
            "ylhäältä alas: tutkimuskysymys ja hypoteesi, muuttujat ja vakioitavat suureet, välineet ja toistomittaukset. "
            "Alhaalta nuoli vie oikeaan sarakkeeseen, analyysiin, alhaalta ylös: taulukko, kuvaaja ja sovitus, tulos "
            "muodossa x keskiarvo plus miinus delta x, virhelähteet ja johtopäätös. Ylhäältä katkoviivanuoli palaa "
            "tutkimuskysymykseen: johtopäätös voi synnyttää uuden kysymyksen.")
    f.tex(150, 22, r"\text{suunnittelu}", "middle", MUTED)
    f.tex(450, 22, r"\text{analyysi}", "middle", MUTED)
    boxes = {  # (column, row): two lines
        (0, 0): (r"\text{tutkimuskysymys}", r"\text{ja hypoteesi}"),
        (0, 1): (r"\text{muuttujat ja}", r"\text{vakioitavat suureet}"),
        (0, 2): (r"\text{välineet ja}", r"\text{toistomittaukset}"),
        (1, 2): (r"\text{taulukko, kuvaaja}", r"\text{ja sovitus}"),
        (1, 1): (r"\text{tulos}", r"\bar{x} \pm \Delta x"),
        (1, 0): (r"\text{virhelähteet ja}", r"\text{johtopäätös}"),
    }
    X0, W, Y0, H_, GAP = 20, 260, 50, 82, 30
    for (c, r), (l1, l2) in boxes.items():
        x, y = X0 + c * 300, Y0 + r * (H_ + GAP)
        f.rect(x, y, W, H_, GLASS if c == 0 else SAND_LIGHT, INK, 2.5, 10)
        f.tex(x + W / 2, y + 26, l1, "middle")
        f.tex(x + W / 2, y + 56, l2, "middle")
    cx0, cx1 = X0 + W / 2, X0 + 300 + W / 2
    for r in (0, 1):                                                              # down the plan, up the analysis
        y1, y2 = Y0 + r * (H_ + GAP) + H_, Y0 + (r + 1) * (H_ + GAP)
        f.arrow(cx0, y1 + 2, cx0, y2 - 2, INK, 2.5, 12)
        f.arrow(cx1, y2 - 2, cx1, y1 + 2, INK, 2.5, 12)
    yb = Y0 + 2 * (H_ + GAP) + H_ / 2
    f.arrow(X0 + W + 2, yb, X0 + 300 - 2, yb, INK, 2.5, 12)                      # plan -> analysis
    yt = Y0 + H_ / 2
    f.line(X0 + 300 - 2, yt, X0 + W + 16, yt, MUTED, 2.5, "7 6")                  # back to a new question
    f.path(f"M{X0 + W + 2},{n(yt)} L{X0 + W + 16},{n(yt - 6)} L{X0 + W + 16},{n(yt + 6)} Z", MUTED)
    return f.svg()


def virhe():
    """Mass against volume of oil weighed in an untared beaker: points, the fitted line extended (dashed) to the
    vertical axis, the intercept b = 52 g (the beaker) and a slope triangle k = rho."""
    k, b = fit(V_OIL, M_OIL)
    f = Fig("fy9ko-virhe", 420, "Kuvaaja mittakaavassa: dekantterilasissa punnitun ruokaöljyn massa m tilavuuden V "
            "funktiona. Viisi mittauspistettä tilavuuksilla 20, 40, 60, 80 ja 100 kuutiosenttimetriä on lähes suoralla. "
            "Pisteisiin sovitettu suora on jatkettu katkoviivana pystyakselille, jonka se leikkaa kohdassa b noin 52 g, "
            "ei origossa. Tämä vakiotermi on punnitsematta jääneen lasin massa eli systemaattinen virhe. Suoran "
            "kulmakerroin k on öljyn tiheys noin 0,91 grammaa kuutiosenttimetrille, ja se näkyy suoran kolmiosta.")
    ax = Axes(f, (80, 370), (480, 70), x=(0, 110), y=(0, 160), xticks=[0, 20, 40, 60, 80, 100], yticks=[0, 40, 80, 120, 160],
              xlabel=r"V\ (\text{cm}^3)", ylabel=r"m\ (\text{g})")
    ax.line([(0, b), (20, b + 20 * k)], INK, 2.5, dash="8 6")
    ax.line([(20, b + 20 * k), (106, b + 106 * k)], INK, 3)
    for v, m in zip(V_OIL, M_OIL): ax.point(v, m)
    # the intercept, marked on the axis and named
    f.circle(ax.X(0), ax.Y(b), 7, HOT, WHITE, 2)
    f.tex(ax.X(3), ax.Y(34), r"b \approx 52\,\text{g} = \text{lasin massa}", "start", HOT)
    f.tex(ax.X(3), ax.Y(12), r"\text{systemaattinen virhe}", "start", INK)
    # the slope triangle between 40 and 90 cm^3 on the line
    a1, a2 = 40, 90
    f.line(ax.X(a1), ax.Y(b + a1 * k), ax.X(a2), ax.Y(b + a1 * k), COLD, 2)
    f.line(ax.X(a2), ax.Y(b + a1 * k), ax.X(a2), ax.Y(b + a2 * k), COLD, 2)
    f.tex(ax.X((a1 + a2) / 2), ax.Y(b + a1 * k) + 20, r"\Delta V", "middle", COLD)
    f.tex(ax.X(a2) + 10, ax.Y(b + (a1 + a2) / 2 * k), r"\Delta m", "start", COLD)
    f.tex(ax.X(28), ax.Y(150), r"k = \tfrac{\Delta m}{\Delta V} = \rho", "start", COLD, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "virhe": virhe}
