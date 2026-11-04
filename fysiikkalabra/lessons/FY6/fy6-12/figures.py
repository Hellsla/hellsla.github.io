"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-12` writes them into lesson.md.
A homogeneous field between two parallel plates: the plates metal grey, the field lines green (#2b8a3e) arrows with \\overline{E},
the force on a charge red (FY4: force red, velocity blue, acceleration orange), equipotential lines dashed grey (#868e96),
potentials and potential energy ink, kinetic energy orange in the energy bars. Every label LaTeX."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    GLASS, ICE, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, WATER, n
import herolib as H
import math

FORCE = HOT          # forces (red, as in FY4)
FIELD = GOOD         # field lines and the field vector
EQ = "#868e96"      # equipotential lines (dashed grey)
POT = INK            # potentials, potential energy, potential graph
KIN = HEAT           # kinetic energy


def plate(f, x0, x1, y, sign):
    """A metal plate seen edge-on, 12 units thick, centred on y; small + or - marks drawn on it (no text)."""
    f.rect(x0, y - 6, x1 - x0, 12, ALUMINIUM, INK, 2.5, rx=2)
    for k in range(int((x1 - x0 - 40) / 40) + 1):
        cx = x0 + 20 + k * 40
        f.line(cx - 4, y, cx + 4, y, INK, 2)
        if sign > 0: f.line(cx, y - 4, cx, y + 4, INK, 2)


def charge(f, x, y, positive=True, r=13):
    f.circle(x, y, r, HOT_LIGHT if positive else COLD, INK, 2.5)
    f.line(x - 6, y, x + 6, y, INK if positive else WHITE, 2.5)
    if positive: f.line(x, y - 6, x, y + 6, INK, 2.5)


def bracket(f, x, y0, y1, tick=7):
    """A vertical dimension line with end ticks."""
    f.line(x, y0, x, y1, INK, 2)
    f.line(x - tick, y0, x + tick, y0, INK, 2); f.line(x - tick, y1, x + tick, y1, INK, 2)


# --- Ydinajatus 1: the field does work like gravity ---------------------------------------------------------------
def kentta():
    f = Fig("fy612-kentta", 340, "Kaksi rinnakkaista kaavakuvaa, ei mittakaavassa. Vasemmalla pallo on korkeudella h maanpinnan "
            "yläpuolella, ja siihen vaikuttaa alaspäin punainen painovoima m kertaa g. Kun pallo putoaa maahan, painovoima tekee "
            "työn W = mgh. Oikealla kaksi vaakasuoraa metallilevyä: ylempi positiivinen ja alempi negatiivinen, levyjen väli d. "
            "Levyjen välissä on homogeeninen sähkökenttä E, jonka kenttäviivat osoittavat alaspäin. Positiiviseen levyyn on "
            "kiinni positiivinen varaus q, ja siihen vaikuttaa alaspäin punainen voima q kertaa E. Kun varaus kulkee levystä "
            "toiseen, sähköinen voima tekee työn W = qEd.")
    # left: a ball above the ground
    f.rect(24, 262, 250, 14, SAND_LIGHT, INK, 2)
    f.circle(110, 92, 16, ALUMINIUM, INK, 2.5)
    f.arrow(110, 110, 110, 172, FORCE, 4, 16)
    f.tex(124, 148, r"m\overline{g}", "start", FORCE)
    bracket(f, 214, 92, 262)
    f.tex(226, 177, "h", "start", w=24)
    f.tex(150, 306, r"W = mgh", "middle", w=140)
    f.line(300, 24, 300, 316, RULE, 2, "8 6")
    # right: two plates and a positive charge at the + plate
    plate(f, 340, 540, 68, +1); plate(f, 340, 540, 268, -1)
    f.tex(330, 68, "+", "end", w=24); f.tex(330, 268, "-", "end", w=24)
    for x in (372, 508):
        f.arrow(x, 84, x, 252, FIELD, 2.5, 14)
    f.tex(384, 196, r"\overline{E}", "start", FIELD)
    charge(f, 440, 90)
    f.arrow(440, 106, 440, 172, FORCE, 4, 16)
    f.tex(452, 148, r"q\overline{E}", "start", FORCE)
    bracket(f, 562, 68, 268)
    f.tex(574, 168, "d", "start", w=22)
    f.tex(450, 306, r"W = qEd", "middle", w=140)
    return f.svg()


# --- Ydinajatus 2: potentials and equipotential surfaces ------------------------------------------------------------
def tasapotentiaali():
    f = Fig("fy612-tasapot", 340, "Kaavakuva mittakaavassa: kaksi vaakasuoraa metallilevyä 4,0 senttimetrin päässä toisistaan. "
            "Ylempi levy on positiivinen ja sen potentiaali on 200 V, alempi negatiivinen levy on nollakohta 0 V. Levyjen välissä "
            "ovat harmaat katkoviivat, joiden potentiaalit ovat 150 V, 100 V ja 50 V; viivat ovat 1,0 senttimetrin välein. "
            "Vihreät kenttäviivat E osoittavat ylhäältä alas ja leikkaavat katkoviivat kohtisuorasti. Potentiaali pienenee "
            "kentän suuntaan 50 V jokaisella senttimetrillä.")
    top, bot, x0, x1 = 60, 280, 170, 470
    plate(f, x0, x1, top, +1); plate(f, x0, x1, bot, -1)
    for k, v in enumerate((150, 100, 50)):
        y = top + (k + 1) * (bot - top) / 4
        f.line(x0, y, x1, y, EQ, 2.5, "10 7")
        f.tex(x0 - 14, y, fi(v) + r"\,\text{V}", "end", POT, w=86)
    f.tex(x0 - 14, top, r"200\,\text{V}", "end", POT, w=86)
    f.tex(x0 - 14, bot, r"0\,\text{V}", "end", POT, w=86)
    for x in (230, 350, 430):
        f.arrow(x, top + 12, x, bot - 14, FIELD, 2.5, 14)
    f.tex(242, top + (bot - top) * 3 / 8, r"\overline{E}", "start", FIELD)
    bracket(f, 500, bot - (bot - top) / 4, bot)
    f.tex(512, bot - (bot - top) / 8, r"1{,}0\,\text{cm}", "start", w=78)
    bracket(f, 500, top, top + (bot - top) / 4)
    f.tex(512, top + (bot - top) / 8, r"50\,\text{V}", "start", POT, w=70)
    return f.svg()


# --- Ydinajatus 4: energy bars of a proton and an electron crossing 200 V ------------------------------------------
def energia():
    f = Fig("fy612-energia", 380, "Pylväskuvaaja mittakaavassa: energia elektronivoltteina, kun hiukkanen lähtee levosta ja kulkee "
            "levyjen välisen 200 voltin potentiaalieron läpi. Vasemmalla protoni, joka lähtee positiiviselta levyltä: alussa sen "
            "potentiaalienergia on 200 eV ja liike-energia nolla, lopussa negatiivisella levyllä potentiaalienergia on nolla ja "
            "liike-energia 200 eV. Oikealla elektroni, joka lähtee negatiiviselta levyltä: alussa kumpikin energia on nolla, "
            "lopussa positiivisella levyllä potentiaalienergia on miinus 200 eV ja liike-energia 200 eV. Kummallakin hiukkasella "
            "energioiden summa pysyy samana. Potentiaalienergian pylväät ovat tummia ja liike-energian oransseja.")
    zero, s = 180, 110 / 200                      # 200 eV = 110 units
    ax = 78
    f.arrow(ax, 306, ax, 50, INK, 2.5, 13)
    f.tex(ax - 10, 34, r"E\ (\text{eV})", "start", w=96)
    for v in (200, 0, -200):
        y = zero - v * s
        f.line(ax - 7, y, ax, y, INK, 2)
        f.tex(ax - 12, y, fi(v), "end", w=54)
    f.line(ax, zero, 584, zero, INK, 2)
    f.line(338, 24, 338, 366, RULE, 2, "8 6")
    panels = ((96, r"\text{protoni}", [(200, 0), (0, 200)]), (350, r"\text{elektroni}", [(0, 0), (-200, 200)]))
    for px, title, groups in panels:
        f.tex(px + 150, 30, title, "middle", w=130)
        for g, (ep, ek) in enumerate(groups):
            gx = px + 12 + g * 122
            for b, (val, col, sym) in enumerate(((ep, POT, r"E_\text{p}"), (ek, KIN, r"E_\text{k}"))):
                bx = gx + b * 50
                if val: f.rect(bx, min(zero, zero - val * s), 42, abs(val) * s, col, INK, 2)
                else: f.line(bx, zero, bx + 42, zero, col, 5)
                f.tex(bx + 21, 320, sym, "middle", w=44)
            f.tex(gx + 46, 352, r"\text{alussa}" if g == 0 else r"\text{lopussa}", "middle", w=110)
    return f.svg()


# --- Kaava: the potential between the plates as a graph ------------------------------------------------------------
def vx_graph():
    f = Fig("fy612-vx", 340, "Kuvaaja mittakaavassa: potentiaali V volteissa etäisyyden x funktiona senttimetreinä, kun x mitataan "
            "negatiivisesta levystä, jonka potentiaali on nolla. Levyjen väli on 4,0 cm ja jännite 200 V. Kuvaaja on origon kautta "
            "kulkeva nouseva suora, joka päättyy positiivisen levyn kohdalle pisteeseen (4,0 cm; 200 V). Kulmakerroinkolmio "
            "näyttää, että kahden senttimetrin matkalla potentiaali muuttuu 100 V, joten kentänvoimakkuus on 5000 V/m.")
    ax = Axes(f, (100, 280), (480, 50), x=(0, 4.4), y=(0, 220), xticks=[1, 2, 3, 4], yticks=[50, 100, 150, 200],
              xlabel=r"x\ (\text{cm})", ylabel=r"V\ (\text{V})")
    ax.line([(0, 0), (4, 200)], POT, 3)
    ax.point(4, 200, POT)
    # slope triangle from x = 1 to x = 3
    f.line(ax.X(1), ax.Y(50), ax.X(3), ax.Y(50), MUTED, 2, "6 5")
    f.line(ax.X(3), ax.Y(50), ax.X(3), ax.Y(150), MUTED, 2, "6 5")
    f.tex((ax.X(1) + ax.X(3)) / 2, ax.Y(50) + 22, r"\Delta x = 2{,}0\,\text{cm}", "middle", w=170, bg=True)
    f.tex(ax.X(3) + 12, ax.Y(100), r"\Delta V = 100\,\text{V}", "start", w=160, bg=True)
    f.tex(ax.X(4) - 12, ax.Y(200) - 24, r"\text{positiivinen levy}", "end", POT, w=200)
    return f.svg()


# --- task figure (L1-05): a potential graph between plates on 1 cm and 50 V gridlines, nothing marked ---------------
def ex_vgraph():
    f = Fig("fy612-exvgraph", 340, "Kuvaaja mittakaavassa: potentiaali V volteissa etäisyyden x funktiona senttimetreinä levyjen "
            "välissä, kun x mitataan negatiivisesta levystä. Ruudukon välit 1 cm ja 50 V. Kuvaaja on suora, joka alkaa origosta "
            "ja nousee tasaisesti pisteeseen (5,0 cm; 250 V), jossa on positiivinen levy.")
    ax = Axes(f, (100, 290), (480, 50), x=(0, 5.5), y=(0, 275), xticks=[1, 2, 3, 4, 5], yticks=[50, 100, 150, 200, 250],
              xlabel=r"x\ (\text{cm})", ylabel=r"V\ (\text{V})")
    ax.line([(0, 0), (5, 250)], POT, 3)
    return f.svg()


# --- opening illustration: northern lights over a snowy Lapland evening ---------------------------------------------
def hero():
    f = H.hero("fy612-hero", "Kuvitus: revontulet talvisen Lapin yllä. Tummalla tähtitaivaalla kaartuu vihreitä revontuliverhoja, "
               "joiden pystysuorat säteet hehkuvat alareunastaan kirkkaimpina. Alhaalla on lumisia tuntureita, kuusikko ja punainen "
               "mökki, jonka ikkunasta loistaa lämmin valo.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy612h-sky", INK, WATER, y1=0, y2=560))
    for k in range(80):
        x, y = H.rnd(k, 3) * 1200, H.rnd(k + 400, 3) * 330
        f.circle(x, y, 1 + 1.4 * H.rnd(k + 800, 3), WHITE)
    f.defs_add(f'<linearGradient id="fy612h-ray" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOOD_LIGHT}" stop-opacity="0"/>'
               f'<stop offset="0.65" stop-color="{GOOD_LIGHT}" stop-opacity="0.75"/><stop offset="1" stop-color="{GOOD}" stop-opacity="0.95"/></linearGradient>')
    # curtains: the lower edge follows a wave, rays of varied height stand on it
    for c, (y0, amp, top, x0, x1, ph) in enumerate(((300, 46, 120, 250, 980, 0.0), (250, 30, 70, 420, 1150, 1.7))):
        k = 0; x = x0
        while x < x1:
            yb = y0 + amp * math.sin((x - x0) / 140 + ph) + 14 * math.sin((x - x0) / 37 + c)
            h = (yb - top) * (0.55 + 0.45 * H.rnd(k, 7 + c))
            f.add(f'<rect x="{n(x)}" y="{n(yb - h)}" width="9" height="{n(h)}" fill="url(#fy612h-ray)" opacity="{0.5 + 0.4 * H.rnd(k + 50, c + 2):.2f}"/>')
            x += 7; k += 1
    # snowy fells and a spruce wood
    H.hills(f, "fy612h", 430, [GLASS, WHITE], amp=60, seed=5)
    for k in range(14):
        x = 40 + k * 86 + 30 * H.rnd(k, 9)
        if 560 < x < 760: continue
        H.spruce(f, x, 520 + 30 * H.rnd(k + 20, 9), 80 + 50 * H.rnd(k + 40, 9), GOOD)
    H.red_house(f, 590, 548, 150, 70, snow=True)
    for wx in (620, 690):
        f.rect(wx + 3, 548 - 70 * 0.72 + 3, 34, 70 * 0.4 - 6, HEAT_LIGHT)
    f.rect(0, 560, 1200, 40, WHITE)
    return f.svg()


FIGURES = {"hero": hero, "kentta": kentta, "tasapotentiaali": tasapotentiaali, "energia": energia, "vx-graph": vx_graph,
           "ex-vgraph": ex_vgraph}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "kentta": "reveals: the field's work W = qEd beside gravity's W = mgh",
    "tasapotentiaali": "reveals: equipotential lines 50 V apart every 1,0 cm between plates at 200 V and 0 V",
    "energia": "reveals: a proton's and an electron's E_p and E_k before and after crossing 200 V",
    "vx-graph": "reveals: V(x) between plates 4,0 cm and 200 V apart, slope 100 V per 2,0 cm",
    "ex-vgraph": "safe: V(x) between plates on 1 cm and 50 V gridlines, 0 V at x = 0 to 250 V at 5,0 cm, nothing marked",
}
