"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-6` writes them into lesson.md.
Circuit diagrams with IEC symbols as in the other FY6 chapters: resistor a rectangle, source two plates (long +, short −);
conventional current from + to − as violet arrows (#7048e8); energy and heat flow orange (#ffc078 -> #e8590c);
temperature red (#c92a2a); every label LaTeX."""
import math
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, GLASS, \
    ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, PAPER, n
import herolib as H

CUR = "#7048e8"     # current arrows and their labels (FY6: conventional current is violet)


def wire(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=64, width=24, fill=WHITE):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, fill, INK, 3)


def source(f, x, y, gap=16):
    """A source on a vertical wire at x, centred on y: long thin plate (+) above, short thick plate (−) below."""
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def current_head(f, x, y, d):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", CUR)


def heat_grad(f, gid, horizontal=True):
    return H.grad(f, gid, HEAT_LIGHT, HEAT, horizontal=horizontal)


# --- Ydinajatus: power as energy per charge times charge per second -------------------------------------------
def energia():
    f = Fig("fy66-energia", 340, "Kytkentäkaavio, ei mittakaavassa: jännitelähde U = 12 V ja vastus R samassa silmukassa. "
            "Violetit nuolet näyttävät virran I = 0,50 A suunnan plusnavalta vastuksen kautta miinusnavalle. Vastuksesta lähtee "
            "oranssi energiavirran nuoli, jonka viereen on merkitty 6,0 J sekunnissa. Alla laskettuna: 12 J coulombia kohti "
            "kertaa 0,50 C sekunnissa on 6,0 J sekunnissa eli 6,0 W.")
    L, Rx, T, B, ym = 80, 330, 70, 236, 153
    wire(f, (L, ym - 8), (L, T), (Rx, T), (Rx, B), (L, B), (L, ym + 8))
    source(f, L, ym)
    f.tex(L - 34, ym - 18, "+", "middle", w=24); f.tex(L - 34, ym + 22, "-", "middle", w=24)
    f.tex(L + 34, ym, r"U = 12\,\text{V}", "start", w=150)
    resistor(f, Rx, ym, True, fill=HOT_LIGHT)
    f.tex(Rx - 24, ym, "R", "end", w=30)
    current_head(f, 205, T, "r"); current_head(f, 205, B, "l"); current_head(f, Rx, 112, "d")
    f.tex(205, T - 34, r"I = 0{,}50\,\text{A}", "middle", CUR, w=170)
    f.block_arrow(354, ym, 434, ym, heat_grad(f, "fy66-en-heat"), 22, 44, 30)
    f.tex(446, ym - 20, r"6{,}0\,\text{J}", "start", w=90)
    f.tex(446, ym + 18, r"\text{sekunnissa}", "start", w=136)
    f.tex(300, 300, r"12\,\tfrac{\text{J}}{\text{C}} \cdot 0{,}50\,\tfrac{\text{C}}{\text{s}} = 6{,}0\,\tfrac{\text{J}}{\text{s}} = 6{,}0\,\text{W}",
          "middle", w=470)
    return f.svg()


# --- Ydinajatus: how the power divides in series and in parallel (bars to scale) --------------------------------
def jako():
    f = Fig("fy66-jako", 380, "Vaakapylväskuvaaja mittakaavassa: vastusten 4 ohmia ja 8 ohmia tehot P watteina, kun ne on "
            "kytketty 12 voltin jännitelähteeseen. Ylhäällä sarjaankytkentä, jossa molempien läpi kulkee sama virta 1,0 A: "
            "4 ohmin vastuksen teho on 4,0 W ja 8 ohmin vastuksen 8,0 W, eli suurempi resistanssi saa suuremman tehon. Alhaalla "
            "rinnankytkentä, jossa molempien yli on sama jännite 12 V: 4 ohmin vastuksen teho on 36 W ja 8 ohmin vastuksen 18 W, "
            "eli pienempi resistanssi saa suuremman tehon.")
    ax = Axes(f, (170, 318), (480, 24), x=(0, 40), y=(0, 10), xticks=[10, 20, 30, 40], yticks=[], xlabel=r"P\ (\text{W})",
              ylabel=None, grid=True)
    rows = [(46, r"\text{sarjaan: sama virta } I = 1{,}0\,\text{A}", None), (88, r"R_1 = 4\,\Omega", 4.0), (130, r"R_2 = 8\,\Omega", 8.0),
            (184, r"\text{rinnan: sama jännite } U = 12\,\text{V}", None), (226, r"R_1 = 4\,\Omega", 36.0), (268, r"R_2 = 8\,\Omega", 18.0)]
    for y, t, P in rows:
        if P is None:
            f.tex(178, y, t, "start", w=360, bg=True)
            continue
        f.tex(158, y, t, "end", w=130)
        f.rect(ax.X(0), y - 13, ax.X(P) - ax.X(0), 26, HEAT_LIGHT, HEAT, 1.5, 3)      # flat, as fy2-6/fi-bars: the colour means heat, not a scale
        f.tex(ax.X(P) + 10, y, fi(P, 1) + r"\,\text{W}" if P < 10 else fi(P) + r"\,\text{W}", "start", w=86)
    f.line(24, 157, 576, 157, RULE, 1.5, "6 5")
    return f.svg()


# --- Ydinajatus: a resistor warms until it gives off heat as fast as it receives electrical energy --------------
def lampo():
    f = Fig("fy66-lampo", 340, "Kaavakuva, ei mittakaavassa: vastuksen lämpötila T ajan t funktiona, kun virta kytketään "
            "hetkellä nolla. Alussa lämpötila on ympäristön lämpötila T0 ja nousee nopeasti, koska lähes koko sähköteho "
            "kasvattaa vastuksen sisäenergiaa. Mitä lämpimämpi vastus on, sitä enemmän lämpöä siirtyy ympäristöön, joten "
            "nousu hidastuu. Lopulta lämpötila tasaantuu katkoviivalla merkittyyn arvoon, jossa vastuksesta siirtyy "
            "ympäristöön lämpöä yhtä nopeasti kuin siihen tulee sähköenergiaa.")
    ax = Axes(f, (80, 296), (490, 66), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"T",
              grid=False, origin_label=False)
    T = lambda t: 1.4 + 6.6 * (1 - math.exp(-t / 2.2))
    f.line(ax.X(0), ax.Y(8), ax.X(10), ax.Y(8), MUTED, 1.5, "6 5")
    ax.curve(T, 0, 10, HOT, 3)
    f.tex(68, ax.Y(1.4), r"T_0", "end", w=40)
    f.tex(68, ax.Y(8), r"T_\text{loppu}", "end", w=70)
    f.tex(ax.X(1.3), ax.Y(2.4), r"\text{nousee nopeasti}", "start", w=200)
    f.tex(ax.X(4.6), ax.Y(9.1), r"P_\text{sisään} = P_\text{ulos}", "start", w=230)
    return f.svg()


# --- Kaava: P = R I^2 for 4 ohm and 8 ohm ---------------------------------------------------------------------
def graph():
    f = Fig("fy66-graph", 360, "Kuvaaja mittakaavassa: vastuksen teho P watteina virran I funktiona ampeereina kahdelle "
            "vastukselle. 8 ohmin vastuksen paraabeli kulkee pisteiden (1,0 A; 8,0 W) ja (2,0 A; 32 W) kautta ja 4 ohmin "
            "vastuksen paraabeli pisteiden (1,0 A; 4,0 W) ja (2,0 A; 16 W) kautta. Katkoviivat merkitsevät 4 ohmin vastuksen "
            "pisteet: kun virta kaksinkertaistuu yhdestä ampeerista kahteen, teho nelinkertaistuu 4,0 watista 16 wattiin.")
    ax = Axes(f, (96, 304), (480, 66), x=(0, 2.5), y=(0, 40), xticks=[0.5, 1, 1.5, 2, 2.5], yticks=[10, 20, 30, 40],
              xlabel=r"I\ (\text{A})", ylabel=r"P\ (\text{W})")
    ax.curve(lambda i: 8 * i * i, 0, math.sqrt(40 / 8), INK, 3)
    ax.curve(lambda i: 4 * i * i, 0, 2.5, HEAT, 3)
    for i, p in ((1, 4), (2, 16)):
        ax.guide(i, p); ax.point(i, p, HEAT)
    for i, p in ((1, 8), (2, 32)):
        ax.point(i, p, INK)
    f.tex(ax.X(math.sqrt(5)) - 14, ax.Y(40) + 4, r"R = 8\,\Omega", "end", w=110)
    f.tex(ax.X(2.5) + 8, ax.Y(25), r"R = 4\,\Omega", "start", HEAT, w=96)
    f.tex(ax.X(0) + 8, ax.Y(4) - 20, r"4{,}0\,\text{W}", "start", HEAT, w=80)     # over its guide by the axis, clear of the 8 Ω curve
    f.tex(ax.X(2) + 14, ax.Y(16) + 16, r"16\,\text{W}", "start", HEAT, w=70)
    return f.svg()


# --- task figure (L1-05): model powers of a resistor, no curve, no resistance written -------------------------
def ex_pi():
    f = Fig("fy66-expi", 360, "Kuvaaja mittakaavassa: vastuksen teho P watteina virran I funktiona ampeereina. Neljä "
            "pistettä: (0,50 A; 1,25 W), (1,0 A; 5,0 W), (1,5 A; 11,25 W) ja (2,0 A; 20 W). Pystyakselin ruudukon väli "
            "on 5 W ja vaaka-akselin 0,5 A.")
    ax = Axes(f, (96, 304), (480, 66), x=(0, 2.5), y=(0, 25), xticks=[0.5, 1, 1.5, 2, 2.5], yticks=[5, 10, 15, 20, 25],
              xlabel=r"I\ (\text{A})", ylabel=r"P\ (\text{W})")
    for i in (0.5, 1.0, 1.5, 2.0):
        ax.point(i, 5 * i * i, HEAT)
    return f.svg()


# --- opening illustration: a toaster on a kitchen counter, its cord to the wall socket ----------------------------
def hero():
    """The chapter's opening illustration, a close-up (teacher 2026-11-11, illustration audit: the same toaster as in
    Resistanssi ja Ohmin laki, so this one looks down into the slots): the heating wires glow, the cord in the
    foreground carries the same current and does not."""
    f = H.hero("fy66-hero", "Kuvitus, lähikuva: leivänpaahdin keittiön työtasolla yläviistosta nähtynä. Paahtimen kahdessa "
               "aukossa hehkuvat punaoranssit vastuslangat, ja niiden yllä väreilee kuuma ilma. Etualalla paahtimen musta "
               "johto kulkee työtason yli seinän pistorasiaan. Johto on tavallisen värinen eikä hehku.")
    H.tiles(f, 380, 95, RULE_LIGHT, PAPER)
    H.wood(f, -10, 380, 1220, 230, "fy66h-top")
    f.line(0, 380, 1200, 380, INK, 3)
    # wall socket and the plug in it
    f.rect(972, 150, 132, 132, WHITE, INK, 3, 14)
    f.circle(1038, 216, 46, GLASS, INK, 2.5)
    f.rect(1010, 190, 56, 62, IRON, INK, 3, 12)
    # the toaster from slightly above: the top face with its two slots, the front face below it
    f.defs_add('<linearGradient id="fy66h-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/>'
               '<stop offset="0.25" stop-color="#ffffff"/><stop offset="0.6" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient>'
               '<linearGradient id="fy66h-topface" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dfe4e9"/><stop offset="1" stop-color="#f4f6f8"/></linearGradient>')
    xl, xr, yt, yf = 130, 770, 170, 330                       # the front edge of the top face runs from xl to xr at yf
    edge = lambda y: (xl + (yf - y) / (yf - yt) * 70, xr - (yf - y) / (yf - yt) * 70)
    f.path(f"M{xl},{yf} L{xr},{yf} L{xr},600 L{xl},600 Z", "url(#fy66h-steel)", INK, 3)
    f.path(f"M{xl},{yf} L{xr},{yf} L{edge(yt)[1]},{yt} L{edge(yt)[0]},{yt} Z", "url(#fy66h-topface)", INK, 3, 'stroke-linejoin="round"')
    f.rect(xr - 4, 430, 40, 24, INK, rx=6)                    # the lever
    f.circle(450, 500, 34, WHITE, INK, 3); f.line(450, 500, 472, 478, INK, 4, cap="round")
    gl = H.glow(f, "fy66h-glow", HEAT_LIGHT, HEAT)
    f.add(f'<ellipse cx="450" cy="{yt + 60}" rx="330" ry="120" fill="{gl}" fill-opacity="0.85"/>')
    for y0, y1 in ((196, 234), (262, 304)):                   # the two slots, the nearer one larger
        (a0, b0), (a1, b1) = edge(y0), edge(y1)
        a0 += 56; b0 -= 56; a1 += 56; b1 -= 56
        f.path(f"M{n(a0)},{y0} L{n(b0)},{y0} L{n(b1)},{y1} L{n(a1)},{y1} Z", INK, INK, 3, 'stroke-linejoin="round"')
        k = 22
        for i in range(k):                                    # the glowing wires down in the slot
            t = (i + 0.5) / k
            x0, x1 = a0 + (b0 - a0) * t, a1 + (b1 - a1) * t
            f.path(f"M{n(x0)},{y0 + 5} L{n(x1)},{y1 - 5}", stroke=HOT, w=5, extra='stroke-linecap="round"')
            f.path(f"M{n(x0)},{y0 + 7} L{n(x1)},{y1 - 7}", stroke=HEAT_LIGHT, w=2, extra='stroke-linecap="round"')
    H.shimmer(f, (270, 360, 450, 540, 630), yt - 8, 120, HEAT)
    # the cord in the foreground: from the toaster over the worktop to the plug, plain black, no glow
    cord = f"M{xr},548 C880,580 880,470 960,468 C1040,466 1040,360 1038,252"
    f.path(cord, stroke=INK, w=18, extra='stroke-linecap="round"')
    f.path(cord, stroke=MUTED, w=4, extra='stroke-linecap="round" stroke-opacity="0.7"')
    return f.svg()


FIGURES = {"hero": hero, "energia": energia, "jako": jako, "lampo": lampo, "graph": graph, "ex-pi": ex_pi}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "energia": "reveals: P = U I as 12 J/C times 0,50 C/s = 6,0 W",
    "jako": "reveals: the powers 4/8 W in series and 36/18 W in parallel of 4 and 8 ohm on 12 V",
    "lampo": "reveals: a resistor's temperature levels off where heat out equals electrical power in (schematic)",
    "graph": "reveals: P = R I^2 parabolas for 4 and 8 ohm, doubling I quadruples P",
    "ex-pi": "safe: four (I, P) points of a resistor on 5 W and 0,5 A gridlines, no curve or resistance",
}
