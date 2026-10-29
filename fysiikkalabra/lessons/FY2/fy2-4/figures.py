"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-4` writes them into lesson.md.

Energy-flow (Sankey) diagrams drawn to scale: the thickness of an arrow is proportional to the energy or power it carries.
Colours: warm grey = energy taken in, green = useful energy, orange = losses (heat); the same as in the simulation."""
from figlib import Fig, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, ALUMINIUM
from figlib import HOT, METAL_EDGE
import herolib as H


def hero():
    """The chapter's opening illustration: an incandescent bulb and an LED bulb shining equally bright, heat rising only from the first."""
    f = H.hero("fy24-hero", "Kuvitus: kaksi kattolamppua rinnakkain pimeässä huoneessa. Vasemmalla hehkulamppu, jonka hehkulanka hohtaa ja "
               "jonka yläpuolella väreilee lämpöä; oikealla ledilamppu. Molempien valokeilat ovat yhtä kirkkaat.")
    f.rect(0, 0, 1200, 600, "#2b3440")
    f.rect(0, 0, 1200, 40, INK)
    for cx, led in ((370, False), (830, True)):
        f.add(f'<path d="M{cx - 60},300 L{cx - 230},600 H{cx + 230} L{cx + 60},300 Z" fill="{HEAT_LIGHT}" fill-opacity="0.28"/>')
        f.add(f'<circle cx="{cx}" cy="260" r="120" fill="{HEAT_LIGHT}" fill-opacity="0.25"/>')
        f.line(cx, 40, cx, 160, INK, 4)
        f.rect(cx - 26, 160, 52, 50, ALUMINIUM, INK, 3, 4)
        for k in range(3): f.line(cx - 26, 172 + 12 * k, cx + 26, 176 + 12 * k, METAL_EDGE, 2)
        if led:
            f.path(f"M{cx - 30},210 L{cx - 70},260 Q{cx - 78},340 {cx},346 Q{cx + 78},340 {cx + 70},260 L{cx + 30},210 Z", WHITE, INK, 3)
            f.path(f"M{cx - 54},270 Q{cx},250 {cx + 54},270 L{cx + 50},310 Q{cx},326 {cx - 50},310 Z", "#fff4d6")
            for k in range(5): f.circle(cx - 36 + 18 * k, 292, 5, HEAT_LIGHT)
        else:
            f.path(f"M{cx - 30},210 L{cx - 40},236 Q{cx - 92},270 {cx - 80},318 Q{cx - 60},356 {cx},356 Q{cx + 60},356 {cx + 80},318 Q{cx + 92},270 {cx + 40},236 L{cx + 30},210 Z", "#fff4d6", INK, 3)
            f.path(f"M{cx - 10},212 L{cx - 22},290 M{cx + 10},212 L{cx + 22},290", stroke=METAL_EDGE, w=2)
            f.path(f"M{cx - 22},290 q6,-12 11,0 t11,0 t11,0 t11,0", stroke=HEAT, w=4)
            f.add(f'<circle cx="{cx}" cy="292" r="30" fill="{HEAT}" fill-opacity="0.25"/>')
            H.shimmer(f, [cx - 140, cx - 104, cx + 104, cx + 140], 330, 130, HOT)
    return f.svg()


def grad(f, gid, x0, x1, c0, c1):
    """A horizontal gradient along the flow, in figure coordinates."""
    f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{x1}" y2="0">'
               f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>')
    return f"url(#{gid})"


def flow(f, tag, x0, ytop, H, eta, xs, xend, yloss, xhead_in=None, xtip=None):
    """The three arrows of one device. The input arrow (thickness H) runs from x0 to the split at xs (with an arrowhead
    pointing at the device box when xhead_in is given), the useful arrow (eta * H) stays on the top edge to xend and the
    loss arrow ((1 - eta) * H) bends down so that its top edge is at yloss. Returns (useful, loss) = (y centre, y bottom)."""
    Ta, Th = H * eta, H * (1 - eta)
    tip = xtip or xend + 30
    gi = grad(f, f"{tag}-in", x0, xs, RULE_LIGHT, RULE)
    go = grad(f, f"{tag}-ok", xs, tip, GOOD_LIGHT, GOOD)
    gl = grad(f, f"{tag}-loss", xs, tip, HEAT_LIGHT, HEAT)
    e = 8                                                              # an arrowhead is wider than its shaft by e on each side
    if xhead_in:
        f.path(f"M{x0},{ytop} L{xhead_in - 22},{ytop} L{xhead_in - 22},{ytop - e} L{xhead_in},{ytop + H / 2} L{xhead_in - 22},{ytop + H + e} "
               f"L{xhead_in - 22},{ytop + H} L{x0},{ytop + H} Z", fill=gi, stroke=INK, w=2)
    else:
        f.path(f"M{x0},{ytop} L{xs},{ytop} L{xs},{ytop + H} L{x0},{ytop + H} Z", fill=gi, stroke=INK, w=2)
    f.path(f"M{xs},{ytop} L{xend},{ytop} L{xend},{ytop - e} L{tip},{ytop + Ta / 2} L{xend},{ytop + Ta + e} L{xend},{ytop + Ta} L{xs},{ytop + Ta} Z",
           fill=go, stroke=INK, w=2)
    cx = xs + 90
    f.path(f"M{xs},{ytop + Ta} C{cx},{ytop + Ta} {xs + 30},{yloss} {cx + 40},{yloss} L{xend},{yloss} L{xend},{yloss - e} L{tip},{yloss + Th / 2} "
           f"L{xend},{yloss + Th + e} L{xend},{yloss + Th} L{cx + 40},{yloss + Th} C{xs + 30},{yloss + Th} {cx},{ytop + H} {xs},{ytop + H} Z",
           fill=gl, stroke=INK, w=2)
    return ytop + Ta / 2, yloss + Th


def bulb(f, cx, cy):
    """An incandescent lamp: glass bulb with a glowing filament and a metal base."""
    f.circle(cx, cy - 16, 34, GLASS, INK, 2.5)
    f.path(f"M{cx - 16},{cy - 16} L{cx - 8},{cy - 30} L{cx},{cy - 4} L{cx + 8},{cy - 30} L{cx + 16},{cy - 16}", stroke=HEAT, w=3)
    f.rect(cx - 16, cy + 18, 32, 30, ALUMINIUM, INK, 2.5, rx=4)
    f.line(cx - 16, cy + 28, cx + 16, cy + 28, INK, 1.5)
    f.line(cx - 16, cy + 38, cx + 16, cy + 38, INK, 1.5)


def sankey_lamp():
    f = Fig("fy24-lamp", 350, "Energiavirtakuvio mittakaavassa: hehkulamppu ottaa sähköenergiaa 100 J. Sähkö kulkee vasemmalta lampun kuvaan. "
            "Oikealle jatkuu ohut vihreä nuoli, valon energia 5 J, ja paksu oranssi nuoli, lämmön energia 95 J. Nuolten paksuudet ovat "
            "suhteessa energioihin, joten valon osuus on 5 prosenttia tulevasta energiasta.")
    ytop, H, eta = 96, 120, 0.05
    flow(f, "fy24l", 30, ytop, H, eta, 292, 520, 196, xhead_in=190)
    f.rect(190, 70, 102, 172, WHITE, INK, 2.5, rx=12)
    bulb(f, 241, 126)
    f.tex(30, 28, r"\text{hehkulamppu}", "start")
    f.tex(30, 70, r"E_\text{o} = 100\,\text{J}", "start")
    f.tex(30, ytop + H + 32, r"\text{sähkö}", "start", MUTED)
    f.tex(412, ytop - 28, r"E_\text{a} = 5\,\text{J}\ (\text{valo})", "middle", GOOD, w=230)
    f.tex(412, 196 + 114 + 28, r"E_\text{h} = 95\,\text{J}\ (\text{lämpö})", "middle", w=250)
    f.tex(241, 270, r"\eta = 5\,\%", "middle", w=110)
    return f.svg()


def sankey_pair():
    f = Fig("fy24-pair", 450, "Kaksi energiavirtakuviota samassa mittakaavassa. Ylhäällä hehkulamppu ottaa tehon 60 W ja antaa valotehoa 3 W; "
            "hyötysuhde on 5 prosenttia, ja 57 W muuttuu lämmöksi. Alhaalla ledilamppu ottaa tehon 10 W ja antaa saman valotehon 3 W; "
            "hyötysuhde on 30 prosenttia, ja 7 W muuttuu lämmöksi. Molemmissa vihreä valoteho-nuoli on yhtä paksu, mutta ledilampun tuleva "
            "nuoli on kuudesosa hehkulampun tulevasta nuolesta.")
    s = 1.6                                                            # 1,6 px per watt in both diagrams
    # filament lamp, 60 W
    ytop, H = 84, 60 * s
    yl = ytop + 40
    flow(f, "fy24a", 30, ytop, H, 3.0 / 60, 200, 500, yl, xtip=532)
    f.tex(30, 26, r"\text{hehkulamppu}", "start")
    f.tex(30, 58, r"P_\text{o} = 60\,\text{W}", "start")
    f.tex(30, ytop + H + 30, r"\eta = 5\,\%", "start")
    f.tex(372, ytop - 28, r"P_\text{a} = 3\,\text{W}\ (\text{valo})", "middle", GOOD, w=230)
    f.tex(372, yl + 57 * s + 30, r"P_\text{h} = 57\,\text{W}\ (\text{lämpö})", "middle", w=250)
    rule = 268
    f.line(30, rule, 570, rule, RULE, 1.5, "6 5")
    # LED lamp, 10 W
    ytop2, H2 = rule + 84, 10 * s
    yl2 = ytop2 + 34
    f.tex(30, rule + 28, r"\text{ledilamppu}", "start")
    f.tex(30, rule + 60, r"P_\text{o} = 10\,\text{W}", "start")
    flow(f, "fy24b", 30, ytop2, H2, 3.0 / 10, 200, 500, yl2, xtip=532)
    f.tex(372, ytop2 - 28, r"P_\text{a} = 3\,\text{W}\ (\text{valo})", "middle", GOOD, w=230)
    f.tex(30, ytop2 + H2 + 30, r"\eta = 30\,\%", "start")
    f.tex(372, yl2 + 7 * s + 30, r"P_\text{h} = 7\,\text{W}\ (\text{lämpö})", "middle", w=230)
    return f.svg()


def sankey_grid():
    """A task figure: a motor's energy-flow diagram on squared paper, the input labelled, the outputs without values."""
    f = Fig("fy24-grid", 380, "Energiavirtakuvio mittakaavassa ruutupaperilla: sähkömoottoriin tulee sähköenergiaa 240 J. Tulevan "
            "nuolen paksuus on 8 ruutua. Moottorista lähtee oikealle vihreä hyötyenergian nuoli, liike-energia, jonka paksuus on "
            "2 ruutua, ja alas kaartuva oranssi häviöiden nuoli, lämpö, jonka paksuus on 6 ruutua. Nuolten paksuudet ovat suhteessa "
            "energioihin; hyötyenergian ja häviöiden arvoja ei ole merkitty.")
    sq = 20                                                            # one square of the paper, in figure units
    ytop, H, eta = 80, 8 * sq, 0.25
    flow(f, "fy24g", 30, ytop, H, eta, 310, 510, 200, xhead_in=190, xtip=550)
    grid = "".join(f'<line x1="30" y1="{y}" x2="570" y2="{y}"/>' for y in range(60, 341, sq))
    grid += "".join(f'<line x1="{x}" y1="60" x2="{x}" y2="340"/>' for x in range(30, 571, sq))
    f.add(f'<g stroke="{INK}" stroke-opacity="0.22" stroke-width="1.2">{grid}</g>')   # over the arrows, so their squares can be counted
    f.rect(190, 64, 120, 192, WHITE, INK, 2.5, rx=12)
    f.circle(250, 150, 34, ALUMINIUM, INK, 2.5)                        # the motor: a housing, a shaft and a pulley
    f.circle(250, 150, 12, WHITE, INK, 2.5)
    f.rect(212, 186, 76, 14, ALUMINIUM, INK, 2, rx=3)
    f.tex(250, 228, r"\text{moottori}", "middle", w=120)
    f.tex(30, 20, r"\text{sähkömoottori}", "start", w=200)
    f.tex(36, 54, r"E_\text{o} = 240\,\text{J}", "start", w=180, bg=True)
    f.tex(36, 258, r"\text{sähkö}", "start", MUTED, w=90, bg=True)
    f.tex(430, 50, r"\text{liike-energia}", "middle", GOOD, w=190, bg=True)
    f.tex(430, 352, r"\text{lämpö (häviöt)}", "middle", w=210, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "lamp": sankey_lamp, "pair": sankey_pair, "grid": sankey_grid}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "lamp": "reveals: the useful and wasted energy and the efficiency 5 %, printed",
    "pair": "reveals: every power and both efficiencies, printed",
    "grid": "safe: input 240 J labelled, output arrows 2 and 6 squares thick on squared paper, no output values or efficiency",
}
