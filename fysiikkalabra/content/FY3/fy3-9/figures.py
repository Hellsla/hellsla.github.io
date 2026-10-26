"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-9` writes them into lesson.md."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    ALUMINIUM, IRON, WATER, fi
import herolib as H


def star(f, cx, cy, r=8):
    """A small four-pointed hit mark."""
    q = r * 0.3
    pts = [(cx, cy - r), (cx + q, cy - q), (cx + r, cy), (cx + q, cy + q), (cx, cy + r), (cx - q, cy + q), (cx - r, cy), (cx - q, cy - q)]
    return f.path("M" + " L".join(f"{x:g},{y:g}" for x, y in pts) + " Z", fill=INK)


def particle(f, x, y, vx, vy, length, color=HOT):
    f.circle(x, y, 6.5, color)
    L = math.hypot(vx, vy)
    ux, uy = vx / L, vy / L
    f.arrow(x + ux * 8, y + uy * 8, x + ux * (8 + length), y + uy * (8 + length), HEAT, 2.5, 10)


def micro_boyle():
    f = Fig("fy39-micro", 332, "Mikromalli Boylen laista, kaaviokuva. Vasemmalla sylinterissä on kahdeksan kaasuhiukkasta "
            "tilavuudessa V ja paineessa p. Oikealla samat kahdeksan hiukkasta on puristettu mäntää painamalla puoleen "
            "tilavuuteen V/2 samassa lämpötilassa. Nopeusnuolet ovat yhtä pitkät, mutta männän ja pohjan osumamerkkejä "
            "on kaksi kertaa niin monta, joten paine on 2p. Kaasutilan korkeudet ovat suhteessa 2 : 1.")
    dy = 14
    # (x offset in cylinder, y in cylinder, direction): left cylinder, gas 30..250 -> 220 high; right one is squeezed to 110 high
    parts = [(28, 56, -20, 7), (75, 44, 20, -7), (125, 60, 18, 10), (52, 120, -2, -8), (100, 110, -9, 10),
             (145, 144, 5, -12), (30, 176, 20, 8), (118, 180, 20, -4)]
    for x0, top, name, hits_top, hits_bot in ((40, 30, "V", [38, 138], [60, 140]), (330, 140, "V/2", [23, 66, 110, 146], [23, 83, 108, 146])):
        h = 250 - top
        f.rect(x0, top + dy, 160, h, GLASS)
        f.path(f"M{x0},{14 + dy} V{250 + dy} H{x0 + 160} V{14 + dy}", stroke=INK, w=3)
        f.rect(x0 + 3, top - 14 + dy, 154, 14, ALUMINIUM, INK, 2)
        f.line(x0 + 80, 6 + dy, x0 + 80, top - 14 + dy, INK, 4)
        f.line(x0 + 55, 6 + dy, x0 + 105, 6 + dy, INK, 5, cap="round")
        scale = h / 220
        for px, py, vx, vy in parts:
            y = top + 12 + (py - 30) * scale if top != 30 else py + 0
            particle(f, x0 + px, y + dy, vx, vy, 20)
        for hx in hits_top:
            star(f, x0 + hx, top + 7 + dy)
        for hx in hits_bot:
            star(f, x0 + hx, 243 + dy)
    star(f, 222, 52 + dy)
    f.tex(238, 52 + dy, r"\text{osuma}", "start")
    f.line(218, 200 + dy, 296, 200 + dy, MUTED, 4)
    f.arrow(218, 200 + dy, 316, 200 + dy, HEAT, 4, 18)
    f.tex(267, 172 + dy, r"T\ \text{vakio}", "middle")
    f.tex(120, 290 + dy, r"V\ \text{ja}\ p", "middle")
    f.tex(410, 290 + dy, r"V/2\ \text{ja}\ 2p", "middle")
    return f.svg()


K = 2000.0   # pV in kPa ml


def boyle_graphs():
    f = Fig("fy39-boyle", 580, "Kaksi kuvaajaa samoista mittauksista, mittakaavassa, kun pV = 2000 kPa·ml. Ylhäällä paine "
            "tilavuuden funktiona on laskeva kaari; mittauspisteet V = 10, 15, 20, 30 ja 40 ml ovat kaarella. Alhaalla "
            "paine tilavuuden käänteisluvun 1/V funktiona on origon kautta kulkeva suora, jonka kulmakerroin on pV.")
    vs = [10, 15, 20, 30, 40]
    a = Axes(f, (96, 250), (430, 76), x=(0, 45), y=(0, 250), xticks=[10, 20, 30, 40], yticks=[50, 100, 150, 200, 250],
             xlabel=r"V\ (\text{ml})", ylabel=r"p\ (\text{kPa})")
    a.curve(lambda v: K / v, 8, 45, WATER, 3.5, 160)
    for v in vs:
        a.point(v, K / v)
    f.tex(a.X(45) + 10, a.Y(K / 45) - 4, r"\text{kaari}", "start", WATER)
    b = Axes(f, (96, 520), (430, 346), x=(0, 0.12), y=(0, 250), xticks=[0.04, 0.08, 0.12],
             yticks=[50, 100, 150, 200, 250], xlabel=r"1/V\ (\text{1/ml})", ylabel=r"p\ (\text{kPa})",
             xfmt=lambda v: fi(v, 2))
    b.line([(0, 0), (0.12, K * 0.12)], WATER, 3.5)
    for v in vs:
        b.point(1 / v, K / v)
    f.tex(b.X(0.12) + 10, b.Y(K * 0.12) + 22, r"\text{suora}", "start", WATER)
    return f.svg()


def absolute_zero():
    f = Fig("fy39-kelvin", 622, "Kuvaajat mittakaavassa, kun T on 0–400 K. Ylhäällä kaasun tilavuus vakiopaineessa, "
            "alhaalla kaasun paine vakiotilavuudessa kelvinlämpötilan funktiona. Mittauspisteet välillä 253–373 K "
            "ovat suoralla. Suoran katkoviivalla piirretty jatke kulkee origon kautta: tilavuus tai paine olisi nolla "
            "absoluuttisessa nollapisteessä 0 K eli −273 °C.")
    ts = [253, 283, 313, 343, 373]
    for (y0, y1, ymax, yt, ylab, k, yf, tag) in (
            (240, 76, 3.2, [1, 2, 3], r"V\ (\textsf{l})", 2 / 273.15, lambda v: fi(v), "a"),
            (556, 396, 160, [50, 100, 150], r"p\ (\text{kPa})", 101 / 273.15, lambda v: fi(v), "b")):
        ax = Axes(f, (96, y0), (430, y1), x=(0, 400), y=(0, ymax), xticks=[100, 200, 300, 400], yticks=yt,
                  xlabel=r"T\ (\text{K})", ylabel=ylab, yfmt=yf, origin_label=False)
        f.tex(ax.x0, y0 + 24, r"0", "middle")
        f.tex(ax.x0, y0 + 58, r"-273^\circ\text{C}", "middle", MUTED)
        ax.line([(0, 0), (253, k * 253)], MUTED, 3, "10 8")
        ax.line([(253, k * 253), (373, k * 373)], WATER, 3.5)
        for t in ts:
            ax.point(t, k * t, WATER)
        f.tex(ax.X(105), ax.Y(k * 105) - 24, r"\text{jatke}", "middle", MUTED, bg=True)
    return f.svg()


def iso_processes():
    f = Fig("fy39-iso", 412, "Kaksi tilanmuutosta, kaaviokuva. Vasemmalla isobaarinen: sylinterin mäntää kuormittaa "
            "vakiopainoinen kappale, joten kaasun lämmetessä lämpötilasta T₁ lämpötilaan T₂ mäntä nousee ja tilavuus "
            "kasvaa V₁:stä V₂:een; hiukkasten nopeusnuolet ovat pidempiä. Oikealla isokoorinen: jäykän, suljetun "
            "astian tilavuus V pysyy samana, ja kaasun lämmetessä paineenmittarin viisari kääntyy suuremman paineen "
            "p₂ kohdalle.")
    base, wall_top = 340, 110
    f.tex(150, 26, r"\text{isobaarinen}", "middle")
    f.tex(450, 26, r"\text{isokoorinen}", "middle")
    f.line(300, 12, 300, 400, RULE, 2, "8 6")
    pos = [(0.0, 0.1, 1, 0.4), (0.95, 0.2, -1, 0.6), (0.45, 0.5, 0.5, -1), (1.0, 0.8, -1, -0.5), (0.05, 0.9, 1, -0.3)]

    def fill(x, w, h, length, col, gas):
        f.rect(x, base - h, w, h, gas)
        for ux, uy, vx, vy in pos:
            px = x + 14 + ux * (w - 28)
            py = base - h + 14 + uy * (h - 28)
            particle(f, px, py, vx, vy, length, col)

    # isobaric: cold at x 30, hot at x 170; gas heights 70 and 105 (V proportional to T: 300 K and 450 K)
    for x, h, length, gas, tn, vn in ((30, 90, 12, COLD_LIGHT, "T_1", "V_1"), (170, 135, 22, HOT_LIGHT, "T_2", "V_2")):
        w = 90
        fill(x, w, h, length, COLD if h == 90 else HOT, gas)
        f.path(f"M{x},{wall_top} V{base} H{x + w} V{wall_top}", stroke=INK, w=3)
        top = base - h
        f.rect(x + 3, top - 12, w - 6, 12, ALUMINIUM, INK, 2)
        f.rect(x + 15, top - 40, w - 30, 28, IRON, INK, 2.5, 3)
        f.tex(x + w / 2, top - 26, r"m", "middle", WHITE)
        f.tex(x + w / 2, base + 24, tn + r"\text{, }" + vn, "middle")
    f.line(33, base - 90 - 12, 260, base - 90 - 12, MUTED, 1.5, "6 5")
    f.block_arrow(128, 290, 164, 290, HEAT, 14, 26, 16)
    f.tex(146, 318, r"Q", "middle")
    # isochoric: vessel with a pressure gauge on a fixed lid
    for x, length, gas, col, ang, pn, tn in ((345, 12, COLD_LIGHT, COLD, -35, "p_1", "T_1"), (465, 22, HOT_LIGHT, HOT, 25, "p_2", "T_2")):
        w, h = 90, 135
        fill(x, w, h, length, col, gas)
        f.path(f"M{x},{wall_top} V{base} H{x + w} V{wall_top}", stroke=INK, w=3)
        top = base - h
        f.rect(x - 3, top - 12, w + 6, 12, IRON, INK, 2.5)
        f.line(x + w / 2, top - 12, x + w / 2, top - 30, INK, 3)
        cx, cy, r = x + w / 2, top - 62, 32
        f.circle(cx, cy, r, WHITE, INK, 2.5)
        for a in range(-120, 121, 40):
            c, s = math.sin(math.radians(a)), -math.cos(math.radians(a))
            f.line(cx + c * (r - 4), cy + s * (r - 4), cx + c * (r - 11), cy + s * (r - 11), MUTED, 1.5)
        c, s = math.sin(math.radians(ang)), -math.cos(math.radians(ang))
        f.arrow(cx, cy, cx + c * (r - 8), cy + s * (r - 8), HOT, 2.5, 10)
        f.circle(cx, cy, 3.5, INK)
        f.tex(x + w / 2, base + 24, tn + r"\text{, }" + pn, "middle")
    f.block_arrow(438, 290, 462, 290, HEAT, 14, 26, 14)
    f.tex(450, 318, r"Q", "middle")
    return f.svg()


def hero():
    """The chapter's opening illustration: a sealed crisp bag puffed up on a tray table high above the clouds."""
    f = H.hero("fy39-hero", "Kuvitus: lentokoneen istuimen tarjottimella on pullistunut, kireä sipsipussi ja vesimuki. "
               "Ikkunasta näkyvät pilvet kaukana alapuolella.")
    f.rect(0, 0, 1200, 600, H.RULE_LIGHT)
    f.path("M0,0 H1200 V60 Q600,20 0,60 Z", H.WHITE)
    # window
    f.rect(780, 70, 230, 300, H.WHITE, H.RULE, 6, 100)
    f.add('<clipPath id="fy39h-win"><rect x="800" y="90" width="190" height="260" rx="90"/></clipPath>')
    f.add('<g clip-path="url(#fy39h-win)">')
    f.rect(800, 90, 190, 260, H.grad(f, "fy39h-sky", H.COLD, H.ICE))
    for cx, cy, sc in ((830, 300, 0.8), (950, 320, 0.9), (880, 340, 1.0)): H.cloud(f, cx, cy, sc)
    f.add("</g>")
    f.rect(800, 90, 190, 260, extra=f'rx="90" fill="none" stroke="{H.INK}" stroke-width="3"')
    # seat back and tray table
    f.rect(120, 40, 520, 560, H.grad(f, "fy39h-seat", H.METAL_EDGE, H.IRON), H.INK, 3, 40)
    f.rect(170, 80, 420, 60, H.ALUMINIUM, H.INK, 2, 14)
    f.path("M60,430 H760 L720,480 H100 Z", H.RULE, H.INK, 3)
    f.rect(100, 480, 620, 16, H.MUTED)
    # the puffed crisp bag
    f.path("M260,250 Q206,335 262,420 Q380,462 500,420 Q556,335 500,250 Q380,208 260,250 Z", H.COLD, H.INK, 3)
    f.path("M248,246 H512 L506,268 H254 Z", H.ALUMINIUM, H.INK, 2.5)
    f.path("M252,412 H508 L514,434 H246 Z", H.ALUMINIUM, H.INK, 2.5)
    f.path("M300,300 Q380,284 460,300", stroke=H.WHITE, w=4, extra='stroke-opacity="0.7" stroke-linecap="round"')
    f.circle(380, 352, 44, H.SAND_DARK, H.SAND, 3)
    # cup of water
    f.path("M560,330 L572,428 H640 L652,330 Z", H.GLASS, H.INK, 3)
    f.path("M563,354 L572,426 H640 L649,354 Z", H.WATER_LIGHT)
    f.path("M560,330 L572,428 H640 L652,330", stroke=H.INK, w=3)
    return f.svg()


FIGURES = {"hero": hero, "micro-boyle": micro_boyle, "boyle-graphs": boyle_graphs, "absolute-zero": absolute_zero,
           "iso-processes": iso_processes}
