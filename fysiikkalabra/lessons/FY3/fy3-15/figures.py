"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-15` writes them into lesson.md."""
from figlib import Fig, Axes, INK, HEAT, HEAT_LIGHT, COLD, GOOD, GOOD_LIGHT, RULE, RULE_LIGHT, fi
import herolib as H


def hero():
    """The chapter's opening illustration: a combined heat and power plant in winter with district heating pipes to the town."""
    f = H.hero("fy315-hero", "Kuvitus: talvinen yhteistuotantovoimalaitos. Piipusta ja voimalasta nousee höyryä, voimalinjat "
               "vievät sähköä pois, ja kaukolämpöputket kulkevat kaupunkiin: punainen meno kuumaa vettä, sininen paluu "
               "jäähtynyttä vettä. Kerrostalojen ikkunat loistavat lämpiminä.")
    H.sky(f, "fy315h", 600, H.COLD_LIGHT, H.WHITE)
    # Composition tightened (teacher 2026-11-11, illustration audit): the scene drawn 1,15 times larger and lower, so
    # the snow no longer fills the lower half, and the district heating pipes end in the town's first house instead
    # of at the picture's edge.
    f.add('<g transform="matrix(1.15 0 0 1.15 -40 4)">')
    H.forest(f, 380, 50, 26, H.ALUMINIUM, seed=11, depth=60)
    f.path("M0,420 Q600,380 1200,420 V600 H0 Z", H.WHITE)
    # chimney, plant halls, plume
    f.rect(260, 70, 50, 330, H.grad(f, "fy315h-chimney", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    for y in (100, 130): f.rect(260, y, 50, 14, H.HOT_LIGHT)
    H.cloud(f, 330, 50, 0.9, H.WHITE, extra=f'stroke="{H.RULE}" stroke-width="2.5"')
    H.cloud(f, 460, 30, 0.7, H.WHITE, extra=f'stroke="{H.RULE}" stroke-width="2.5"')
    f.rect(120, 260, 200, 160, H.RULE_LIGHT, H.INK, 3)
    f.rect(320, 300, 220, 120, H.ALUMINIUM, H.INK, 3)
    f.path("M120,260 L220,220 L320,260 Z", H.RULE, H.INK, 3)
    for x in range(140, 300, 40): f.rect(x, 290, 24, 50, H.HEAT_LIGHT, H.INK, 2)
    f.rect(470, 210, 40, 90, H.grad(f, "fy315h-stack", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    # power lines to the left
    for x, h in ((60, 230),):
        f.path(f"M{x},{420} L{x + 20},{420 - h} L{x + 40},420 M{x - 10},{420 - h + 30} H{x + 50}", stroke=H.INK, w=4)
    f.path("M0,240 Q40,250 70,220 M110,220 Q130,250 150,262", stroke=H.INK, w=2)
    # district heating pipes to the town
    f.path("M540,390 C660,390 700,456 790,456 H884 V430", stroke=H.HOT, w=16, extra='stroke-linecap="round" stroke-linejoin="round" fill="none"')
    f.path("M540,410 C650,410 690,476 790,476 H912 V430", stroke=H.COLD, w=16, extra='stroke-linecap="round" stroke-linejoin="round" fill="none"')
    for x, w, h in ((860, 120, 200), (1000, 160, 260), (1120, 100, 180)):
        f.rect(x, 440 - h, w, h, H.RULE_LIGHT, H.INK, 3)
        for wx in range(x + 16, x + w - 24, 36):
            for wy in range(440 - h + 20, 420, 44):
                f.rect(wx, wy, 22, 26, H.HEAT_LIGHT if H.rnd(wx * 7 + wy, 3) > 0.3 else H.GLASS, H.INK, 1.5)
    f.add('</g>')
    return f.svg()


def scene():
    """A second everyday scene: a district-heating radiator warming a room on a winter evening."""
    f = H.scene("fy315-scene", "Kuvitus: talvi-ilta kotona. Ikkunan alla oleva kaukolämpöpatteri lämmittää huonetta, ja lämmin ilma "
                "nousee patterin yltä. Ulkona sataa lunta.")
    f.rect(0, 0, 600, 360, H.PAPER)
    f.rect(0, 300, 600, 60, H.RULE); f.line(0, 300, 600, 300, H.INK, 3)
    f.rect(170, 30, 260, 160, H.grad(f, "fy315s-night", H.COLD, H.WATER), H.INK, 3, 4)
    for k in range(18): f.circle(180 + H.rnd(k, 4) * 240, 40 + H.rnd(k + 30, 4) * 140, 2.5, H.WHITE)
    f.path("M170,170 Q260,150 340,166 T430,160 V190 H170 Z", H.WHITE)
    f.line(300, 30, 300, 190, H.INK, 3)
    f.rect(160, 190, 280, 12, H.RULE_LIGHT, H.INK, 2.5)
    f.rect(190, 220, 220, 70, H.WHITE, H.INK, 3, 6)
    for x in range(210, 400, 22): f.line(x, 226, x, 284, H.RULE, 3)
    f.path("M190,276 H160 V300 M410,234 H440 V300", stroke=H.INK, w=6)
    f.path("M160,300 V320", stroke=H.HOT, w=8); f.path("M440,300 V320", stroke=H.COLD, w=8)
    for x in (230, 300, 370):
        f.path(f"M{x},214 c10,-14 -10,-26 0,-40", stroke=H.HEAT, w=4, extra='stroke-linecap="round" stroke-opacity="0.8"')
    return f.svg()


def chain_bars():
    """Task figure (no lesson.md block): the power along a condensing plant's energy chain as four bars on gridlines:
    P0 = 400 MW (fuel), P1 = 350 MW (after the boiler), P2 = 150 MW (after the steam cycle), P3 = 140 MW (electricity)."""
    f = Fig("fy315-chain-bars", 330, "Pylväskuvaaja mittakaavassa: lauhdevoimalaitoksen teho energiaketjun vaiheissa. Pylväiden korkeudet ovat "
            "P_0 = 400 MW (polttoaine), P_1 = 350 MW (kattilan jälkeen), P_2 = 150 MW (höyrykierron jälkeen) ja P_3 = 140 MW "
            "(generaattorin ja muuntajan jälkeen eli sähkö). Ruudukon väli on 50 MW.")
    ax = Axes(f, (96, 280), (470, 56), x=(0, 4), y=(0, 450), xticks=[], yticks=list(range(50, 451, 50)),
              xlabel="", ylabel=r"P\ (\text{MW})", yfmt=lambda v: fi(v) if v % 100 == 0 else "")
    for k, (name, v, col) in enumerate((("P_0", 400, HEAT), ("P_1", 350, HEAT), ("P_2", 150, HEAT), ("P_3", 140, COLD))):
        x0, x1 = ax.X(k + 0.2), ax.X(k + 0.8)
        f.rect(x0, ax.Y(v), x1 - x0, ax.y0 - ax.Y(v), col, INK, 2.5)
        f.tex((x0 + x1) / 2, ax.y0 + 26, name, "middle")
    return f.svg()



def sankey():
    """The energy chain of a condensing power plant as an energy-flow diagram to scale, 100 MW = 40 units (0,4 per MW).
    Drawn with figures.py in the series' model fy2-4/lamp (teacher 2026-11-11, illustration audit group C): warm grey
    for the power taken in, orange for each heat loss, green for the useful electricity, ink outlines, arrowheads 8
    units wider than their shafts. The hand-made SVG it replaces had the same numbers: 500 = 40 + 248 + 12 + 200 MW."""
    f = Fig("fy315-sankey", 420, "Virtauskaavio (Sankey) lauhdevoimalaitoksen energiaketjusta. Polttoaineen teho 500 MW kulkee "
            "vasemmalta oikealle kaistana, joka kapenee vaihe vaiheelta. Kattilassa savukaasujen mukana menee 40 MW, "
            "turbiinissa ja lauhduttimessa lämpönä mereen 248 MW ja generaattorissa ja muuntajassa 12 MW. Sähköä saadaan "
            "200 MW, eli 40 prosenttia polttoaineen tehosta. Kaistojen ja nuolten leveydet ovat mittakaavassa, 100 MW on "
            "40 pikseliä.")
    k, x0, ytop, e, r = 0.4, 30, 76, 8, 20                     # units per MW, band start, band top, head overhang, turn radius
    fuel, losses, el = 500, ((120, 40), (230, 248), (400, 12)), 200
    xg, tip = 440, 566                                          # where the electricity leaves the band, its arrow tip
    f.defs_add(f'<linearGradient id="fy315s-in" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{xg}" y2="0">'
               f'<stop offset="0" stop-color="{RULE_LIGHT}"/><stop offset="1" stop-color="{RULE}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy315s-ok" gradientUnits="userSpaceOnUse" x1="{xg}" y1="0" x2="{tip}" y2="0">'
               f'<stop offset="0" stop-color="{GOOD_LIGHT}"/><stop offset="1" stop-color="{GOOD}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy315s-loss" x1="0" y1="0" x2="0" y2="1">'
               f'<stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    # the band: its top edge flat, its bottom edge stepping up where each loss leaves it
    yb, pts, ends = ytop + fuel * k, [], []
    for x, P in losses:
        pts.append((x, yb)); yb -= P * k; pts.append((x, yb)); ends.append((x, yb + P * k, P * k))
    assert abs(yb - (ytop + el * k)) < 1e-9                     # what is left is the electricity
    d = f"M{x0},{ytop} H{xg} V{yb:g} " + " ".join(f"L{x:g},{y:g}" for x, y in reversed(pts)) + f" L{x0},{ytop + fuel * k:g} Z"
    f.path(d, "url(#fy315s-in)", INK, 2)
    # each loss turns down from the band's bottom edge and ends in an arrowhead
    yh = {120: 322, 230: 334, 400: 236}
    for x, yb_, w in ends:
        xi, xo, yt = x + r, x + r + w, yb_ + r
        hl = 14 + w * 0.12
        f.path(f"M{x:g},{yb_ - w:g} A{r + w:g},{r + w:g} 0 0 1 {xo:g},{yt:g} V{yh[x]} H{xo + e:g} L{(xi + xo) / 2:g},{yh[x] + hl:g} "
               f"L{xi - e:g},{yh[x]} H{xi:g} V{yt:g} A{r},{r} 0 0 0 {x:g},{yb_:g} Z", "url(#fy315s-loss)", INK, 2)
    # the electricity: green, on the band's top edge, to its tip
    ye = ytop + el * k; xh = tip - 30
    f.path(f"M{xg},{ytop} H{xh} V{ytop - e} L{tip},{(ytop + ye) / 2:g} L{xh},{ye + e:g} V{ye:g} H{xg} Z", "url(#fy315s-ok)", INK, 2)
    # labels: each beside its own arrow, none on the frame
    f.tex(x0, 34, r"\text{polttoaine } 500\,\text{MW}", "start", w=250)
    f.tex(576, 34, r"\text{sähkö } 200\,\text{MW}", "end", GOOD, w=230)
    f.tex(148, 368, r"\text{savukaasut}", "middle", w=150)
    f.tex(148, 400, r"40\,\text{MW}", "middle", w=110)
    f.tex(366, 300, r"\text{lauhdutin}", "start", w=150)
    f.tex(366, 334, r"248\,\text{MW}", "start", w=110)
    f.tex(450, 196, r"\text{generaattori}", "start", w=145)
    f.tex(450, 228, r"\text{ja muuntaja}", "start", w=145)
    f.tex(450, 260, r"12\,\text{MW}", "start", w=110)
    f.path("M410,400 H450 M410,392 V408 M450,392 V408", stroke=INK, w=2.5)
    f.tex(460, 400, r"= 100\,\text{MW}", "start", w=110)
    return f.svg()

FIGURES = {"hero": hero, "scene": scene, "chain-bars": chain_bars, "sankey": sankey}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "chain-bars": "safe: the powers along a condensing plant's chain as bars on gridlines; no efficiencies, no losses",
}
