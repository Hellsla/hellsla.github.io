"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-4` writes them into lesson.md.

Energy-flow (Sankey) diagrams drawn to scale: the thickness of an arrow is proportional to the energy or power it carries.
Colours: warm grey = energy taken in, green = useful energy, orange = losses (heat); the same as in the simulation."""
from figlib import Fig, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, ALUMINIUM


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


FIGURES = {"lamp": sankey_lamp, "pair": sankey_pair}
