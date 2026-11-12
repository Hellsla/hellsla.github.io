"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-4` writes them into lesson.md.
Circuit diagrams with IEC symbols: a resistor is a rectangle, a battery a long (+) and a short (−) plate, a meter a
circle with its letter; wires orthogonal; conventional current from + to −, current arrows in their own colour."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, COLD, WATER, SAND_LIGHT, SAND,
                    SAND_DARK, GRAIN, METAL_EDGE, IRON, ALUMINIUM, GLASS, n)
import herolib as H

CURRENT = "#7048e8"     # current arrows and their labels (its own colour, apart from the voltages)
VOLT = COLD             # voltage brackets and their labels


# --- circuit pieces (figure units; every label is LaTeX) ---
def wire(f, *pts):
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=3, extra='stroke-linecap="round"')


def resistor(f, cx, cy, vertical=False, w=76, h=28):
    """An IEC resistor: a white rectangle over the wire."""
    if vertical: w, h = h, w
    f.rect(cx - w / 2, cy - h / 2, w, h, WHITE, INK, 3, 2)


def battery(f, cx, cy):
    """A battery on a vertical wire: the long thin plate (+) above, the short thick plate (−) below, with signs."""
    f.rect(cx - 30, cy - 14, 60, 28, WHITE)                    # gap in the wire
    f.line(cx - 28, cy - 8, cx + 28, cy - 8, INK, 3)
    f.line(cx - 13, cy + 8, cx + 13, cy + 8, INK, 8)
    f.tex(cx - 36, cy - 22, "+", "end")
    f.tex(cx - 36, cy + 22, "-", "end")


def node(f, x, y):
    f.circle(x, y, 5.5, INK)


def current(f, x1, y1, x2, y2, label, lx, ly, anchor="middle"):
    """A current arrow beside a wire (conventional direction) and its label in the current's colour."""
    f.arrow(x1, y1, x2, y2, CURRENT, 3, 14)
    f.tex(lx, ly, label, anchor, CURRENT)


def bracket(f, x1, x2, y, label, ly):
    """A voltage bracket under a component: the voltage over it, label in the voltage's colour."""
    f.path(f"M{n(x1)},{n(y - 7)} V{n(y)} H{n(x2)} V{n(y - 7)}", stroke=VOLT, w=2.5)
    f.tex((x1 + x2) / 2, ly, label, "middle", VOLT)


def series():
    f = Fig("fy64-series", 344, "Kytkentäkaavio, ei mittakaavassa: paristo ja kaksi vastusta R1 ja R2 sarjassa samassa "
            "silmukassa. Violetit virtanuolet kulkevat pariston plusnavasta R1:n ja R2:n kautta takaisin miinusnapaan, ja "
            "jokaisen nuolen merkintä on sama I. Sinisillä hakasilla merkityt jännitteet U1 ja U2 ovat vastusten yli, ja "
            "pariston jännite on U.")
    L, R, T, B = 86, 526, 92, 262
    wire(f, (L, 180 - 14), (L, T), (R, T), (R, B), (L, B), (L, 180 + 14))
    battery(f, L, 180)
    f.tex(L + 40, 180, "U", "start")
    for cx, k in ((246, 1), (406, 2)):
        resistor(f, cx, T)
        f.tex(cx, T - 38, f"R_{k}", "middle")
        bracket(f, cx - 38, cx + 38, T + 34, f"U_{k}", T + 60)
    current(f, 124, T - 16, 172, T - 16, "I", 148, T - 40)
    current(f, 302, T - 16, 350, T - 16, "I", 326, T - 40)
    current(f, R + 18, 156, R + 18, 204, "I", R + 30, 180, "start")
    current(f, 330, B + 18, 282, B + 18, "I", 306, B + 42)
    f.tex(300, 186, r"\text{sama virta } I", "middle", CURRENT)
    return f.svg()


def parallel():
    f = Fig("fy64-parallel", 404, "Kytkentäkaavio, ei mittakaavassa: paristo ja kaksi vastusta R1 ja R2 rinnan. Pariston "
            "plusnavasta lähtevä virta I jakautuu haarautumispisteessä kahteen haaraan, joissa kulkevat virrat I1 ja I2, ja "
            "virrat yhdistyvät taas toisessa haarautumispisteessä. Kummankin vastuksen yli on sama jännite U kuin pariston "
            "napojen välillä.")
    L, xL, xR, T, M, B = 86, 236, 476, 86, 196, 306
    wire(f, (L, 196 - 14), (L, T), (xR, T), (xR, B), (L, B), (L, 196 + 14))
    wire(f, (xL, T), (xL, M), (xR, M))
    battery(f, L, 196)
    f.tex(L + 40, 196, "U", "start")
    for x, y in ((xL, T), (xR, M)): node(f, x, y)          # only where the wire branches or joins, not at the plain corners
    resistor(f, 356, T); f.tex(356, T - 38, "R_1", "middle")
    resistor(f, 356, M); f.tex(356, M - 36, "R_2", "middle")
    current(f, 132, T - 16, 180, T - 16, "I", 156, T - 40)
    current(f, 408, T - 16, 452, T - 16, "I_1", 430, T - 40)
    current(f, 408, M - 16, 452, M - 16, "I_2", 430, M - 40)
    current(f, 330, B + 18, 282, B + 18, "I", 306, B + 42)
    f.tex(356, 256, r"I = I_1 + I_2", "middle", CURRENT)
    f.tex(300, 384, r"\text{sama jännite } U \text{ kummankin vastuksen yli}", "middle", VOLT, w=470)
    return f.svg()


def graph():
    f = Fig("fy64-graph", 352, "Kuvaaja mittakaavassa: kokonaisresistanssi R ohmeina vastuksen R2 funktiona, kun toinen "
            "vastus R1 on 100 ohmia. Sarjaankytkennän suora nousee 100 ohmista 300 ohmiin, kun R2 kasvaa nollasta 200 "
            "ohmiin. Rinnankytkennän käyrä nousee nollasta noin 67 ohmiin ja pysyy aina 100 ohmin katkoviivan alapuolella; "
            "kohdassa R2 = 100 ohmia se on 50 ohmia.")
    ax = Axes(f, (96, 300), (480, 64), x=(0, 200), y=(0, 300), xticks=[50, 100, 150, 200], yticks=[50, 100, 150, 200, 250, 300],
              xlabel=r"R_2\ (\Omega)", ylabel=r"R\ (\Omega)")
    f.line(ax.X(0), ax.Y(100), ax.X(200), ax.Y(100), MUTED, 1.5, "6 5")
    ax.line([(0, 100), (200, 300)], WATER, 3)
    ax.curve(lambda r: 100 * r / (100 + r), 0, 200, HEAT, 3)
    ax.point(100, 200, WATER); ax.point(100, 50, HEAT)
    f.tex(ax.X(160), ax.Y(292), r"\text{sarjaan}", "end", WATER)
    f.tex(ax.X(200) + 10, ax.Y(200 / 3), r"\text{rinnan}", "start", HEAT)      # at the curve's end, clear of the axis arrow
    f.tex(ax.X(170), ax.Y(100), r"R_1", "middle", MUTED, bg=True)
    return f.svg()


def mixed_circuit(f, x0, W, values=None, reduced=False):
    """A series–parallel circuit in a W-wide panel starting at x0: R1 in series with R2 || R3 (or their R23)."""
    L, R, T, B = x0 + 56, x0 + W - 14, 84, 286
    xa, ym = x0 + 0.5 * W, 190                               # the parallel part between the nodes xa and R
    lab = values or {"U": "U", "R1": "R_1", "R2": "R_2", "R3": "R_3", "R23": "R_{23}"}
    wire(f, (L, 185 - 14), (L, T), (R, T), (R, B), (L, B), (L, 185 + 14))
    battery(f, L, 185)
    f.tex(L + 34, 185, lab["U"], "start")
    resistor(f, (L + xa) / 2, T, w=60); f.tex((L + xa) / 2, T - 34, lab["R1"], "middle")
    if reduced:
        resistor(f, R, 185, vertical=True, w=60)
        f.tex(R - 22, 185, lab["R23"], "end")
    else:
        wire(f, (xa, T), (xa, ym), (R, ym))
        node(f, xa, T); node(f, xa, ym); node(f, R, T); node(f, R, ym)
        resistor(f, (xa + R) / 2, T, w=60); f.tex((xa + R) / 2, T - 34, lab["R2"], "middle")
        resistor(f, (xa + R) / 2, ym, w=60); f.tex((xa + R) / 2, ym + 36, lab["R3"], "middle")


def mixed():
    f = Fig("fy64-mixed", 340, "Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Vasemmalla paristoon on kytketty vastus "
            "R1 ja sen kanssa sarjaan kahden rinnakkaisen vastuksen R2 ja R3 ryhmä. Oikealla sama kytkentä, jossa "
            "rinnakkaiset vastukset on korvattu yhdellä vastuksella R23, joka on sarjassa R1:n kanssa.")
    mixed_circuit(f, 16, 276)
    f.line(300, 20, 300, 320, RULE, 2, "6 6")
    mixed_circuit(f, 312, 276, reduced=True)
    f.tex(150, 318, r"R_2 \text{ ja } R_3 \text{ rinnan}", "middle", w=220)
    f.tex(450, 318, r"R = R_1 + R_{23}", "middle", w=220)
    return f.svg()


def task_mixed():
    """Task figure (level 3): R1 = 40 Ω in series with R2 = 60 Ω || R3 = 120 Ω on a 12 V battery; no currents written."""
    f = Fig("fy64-task-mixed", 312, "Kytkentäkaavio: 12 voltin paristoon on kytketty 40 ohmin vastus R1 ja sen kanssa sarjaan "
            "kahden rinnakkaisen vastuksen ryhmä, jossa R2 on 60 ohmia ja R3 on 120 ohmia.")
    mixed_circuit(f, 40, 520, {"U": r"12\,\text{V}", "R1": r"R_1 = 40\,\Omega", "R2": r"R_2 = 60\,\Omega", "R3": r"R_3 = 120\,\Omega"})
    return f.svg()


def siirto_mixed():
    """Transfer-task figure: 20 Ω in series with 60 Ω || 30 Ω on a 12 V battery; no currents written."""
    f = Fig("fy64-siirto-mixed", 312, "Kytkentäkaavio: 12 voltin paristoon on kytketty 20 ohmin vastus ja sen kanssa sarjaan "
            "kahden rinnakkaisen vastuksen ryhmä, jossa toinen vastus on 60 ohmia ja toinen 30 ohmia.")
    mixed_circuit(f, 40, 520, {"U": r"12\,\text{V}", "R1": r"20\,\Omega", "R2": r"60\,\Omega", "R3": r"30\,\Omega"})
    return f.svg()


def hero():
    """The chapter's opening illustration: a living room in a winter evening. One power strip feeds a floor lamp, a
    table lamp and an old string of window lights; the lamps shine, but the string is dark because one bulb is broken."""
    f = H.hero("fy64-hero", "Kuvitus: olohuone talvi-iltana. Ikkunan yläreunassa roikkuu vanha jouluvalosarja, jonka "
               "kaikki lamput ovat pimeinä, koska yksi lamppu on rikki ja roikkuu irti kannastaan. Saman jatkojohdon "
               "pistorasioihin kytketyt lattiavalaisin ja pöytävalaisin palavat kirkkaasti.")
    f.rect(0, 0, 1200, 600, SAND_LIGHT)                                   # wall
    f.rect(0, 470, 1200, 130, H.grad(f, "fy64h-floor", SAND_DARK, SAND))   # floor
    for x in range(-40, 1240, 160): f.line(x, 470, x - 60, 600, GRAIN, 2)
    f.line(0, 470, 1200, 470, GRAIN, 3)
    # window with a night sky and snow on the sill
    f.rect(330, 70, 540, 330, WHITE, INK, 3, 6)
    f.rect(348, 88, 504, 294, H.grad(f, "fy64h-sky", INK, "#2f74b5"))
    f.line(600, 88, 600, 382, WHITE, 12)
    f.line(348, 235, 852, 235, WHITE, 12)
    for k in range(26):
        f.circle(360 + H.rnd(k, 4) * 480, 100 + H.rnd(k + 40, 4) * 270, 2 + 2 * H.rnd(k + 80, 4), WHITE)
    f.path("M348,382 Q460,362 600,374 T852,370 V382 H348 Z", WHITE)
    f.rect(316, 398, 568, 18, WHITE, INK, 3, 3)
    # the string of lights: a sagging cord with bulbs, all dark; one bulb hangs loose from its socket
    pts = [(330 + 540 * t, 96 + 70 * math.sin(math.pi * t) + 14 * math.sin(3 * math.pi * t)) for t in [i / 40 for i in range(41)]]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=4, extra='stroke-linecap="round"')
    for i in range(1, 12):
        x, y = pts[int(i * 40 / 12)]
        f.rect(x - 7, y, 14, 14, IRON, INK, 2, 2)
        if i == 7:                                                    # the broken one, fallen out of its socket
            f.add(f'<ellipse cx="{n(x + 16)}" cy="{n(y + 62)}" rx="11" ry="16" transform="rotate(-30 {n(x + 16)} {n(y + 62)})" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2"/>')
            f.line(x, y + 14, x + 10, y + 46, INK, 2)
        else:
            f.add(f'<ellipse cx="{n(x)}" cy="{n(y + 30)}" rx="11" ry="16" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="2"/>')
    # the string's plug cord down the wall to the power strip
    f.path("M330,96 C300,180 290,360 310,470 C330,520 600,500 670,526", stroke=INK, w=4)
    # power strip on the floor with three plugs
    f.rect(620, 534, 280, 34, WHITE, INK, 3, 8)
    for x in (650, 730, 810): f.rect(x, 524, 40, 22, IRON, INK, 2, 4)
    f.rect(870, 541, 20, 20, "#c92a2a", INK, 2, 4)                       # the strip's switch, on
    # floor lamp on the right, glowing
    f.add(f'<circle cx="1010" cy="160" r="150" fill="{HEAT_LIGHT}" fill-opacity="0.35"/>')
    f.add(f'<circle cx="1010" cy="170" r="90" fill="{WHITE}" fill-opacity="0.45"/>')
    f.path("M940,150 L1080,150 L1050,90 L970,90 Z", WHITE, INK, 3)
    f.path("M948,150 L1072,150 L1062,132 L958,132 Z", HEAT_LIGHT)
    f.line(1010, 150, 1010, 500, INK, 6)
    f.add(f'<ellipse cx="1010" cy="504" rx="54" ry="12" fill="{IRON}" stroke="{INK}" stroke-width="3"/>')
    f.path("M1010,510 C990,520 860,500 830,526", stroke=INK, w=4)
    # side table with a lit table lamp on the left
    f.rect(70, 352, 200, 16, SAND, INK, 3, 3)
    f.line(96, 368, 96, 470, INK, 6); f.line(244, 368, 244, 470, INK, 6)
    f.add(f'<circle cx="170" cy="250" r="110" fill="{HEAT_LIGHT}" fill-opacity="0.35"/>')
    f.path("M120,280 L220,280 L200,220 L140,220 Z", WHITE, INK, 3)
    f.path("M126,280 L214,280 L208,264 L132,264 Z", HEAT_LIGHT)
    f.line(170, 280, 170, 340, INK, 5)
    f.rect(138, 338, 64, 14, IRON, INK, 2, 4)
    f.path("M200,346 C300,360 280,500 420,512 C560,524 700,490 750,526", stroke=INK, w=4)
    return f.svg()


FIGURES = {"hero": hero, "series": series, "parallel": parallel, "graph": graph, "mixed": mixed,
           "task-mixed": task_mixed, "siirto-mixed": siirto_mixed}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "series": "reveals: the same current I everywhere in a series circuit",
    "parallel": "reveals: I = I1 + I2 and the same U over both branches",
    "graph": "reveals: series R grows, parallel R stays below the smaller resistor",
    "mixed": "safe: symbolic reduction of R2 || R3 to R23, no numbers",
    "task-mixed": "safe: 12 V, R1 = 40 Ω in series with 60 Ω || 120 Ω, no currents",
    "siirto-mixed": "safe: 12 V, 20 Ω in series with 60 Ω || 30 Ω, no currents",
}
