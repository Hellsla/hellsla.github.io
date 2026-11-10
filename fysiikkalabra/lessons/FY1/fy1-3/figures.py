"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-3` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE_LIGHT, HOT, COLD, GOOD, ALUMINIUM, METAL_EDGE, IRON, GLASS, GOOD_LIGHT, fi)
from figlib import PAPER, SAND, SAND_DARK, n
import math
import herolib as H
from figlib import HEAT, SAND_LIGHT
from herolib import rnd, steel
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S


def hero():
    """The chapter's opening illustration: one ball rolling down a ramp, ten hands with stopwatches stopped at slightly different times."""
    f = S.hero("fy13-hero", "Kuvitus: luokan pöydällä kalteva alumiinikouru, jota pitkin teräskuula vierii. Etualalla kymmenen kättä pitää "
               "sekuntikelloja; niiden viisarit ovat pysähtyneet hieman eri kohtiin, vaikka ne mittasivat samaa vierimistä.")
    f.rect(0, 0, 1200, 600, PAPER)
    H.window(f, 70, 40, 220, 200, "fy13h-win")
    H.window(f, 910, 40, 220, 200, "fy13h-win2")
    f.rect(360, 40, 480, 210, GOOD, INK, 3, 4)
    f.add(f'<rect x="374" y="54" width="452" height="182" fill="{INK}" fill-opacity="0.35"/>')
    f.rect(360, 250, 480, 10, SAND, INK, 2)
    for x in (420, 470): f.rect(x, 242, 24, 8, WHITE, None, 0, 2)
    # table
    H.wood(f, 60, 300, 1080, 30, "fy13h-top")
    f.rect(90, 330, 30, 120, SAND_DARK, INK, 2); f.rect(1080, 330, 30, 120, SAND_DARK, INK, 2)
    # ramp: an aluminium channel on a stand, a stop block at the end
    f.rect(230, 214, 16, 86, steel(f, "fy13h-rod"), INK, 2)
    f.rect(214, 292, 48, 10, IRON, INK, 2, 3)
    f.rect(222, 206, 32, 16, IRON, INK, 2, 3)
    f.path("M210,200 L990,282 L990,300 L210,218 Z", steel(f, "fy13h-ramp", vertical=True), INK, 3)
    f.path("M210,200 L990,282", stroke=WHITE, w=2)
    f.rect(990, 266, 26, 34, SAND_DARK, INK, 2, 3)
    x = 600; y = 200 + (282 - 200) * (x - 210) / 780 - 20
    for k, op in ((1, 0.2), (2, 0.1), (3, 0.06)):
        f.add(f'<circle cx="{n(x - 56 * k)}" cy="{n(y - 56 * k * 82 / 780)}" r="20" fill="{IRON}" fill-opacity="{op}"/>')
    f.defs_add(f'<radialGradient id="fy13h-ball" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="{WHITE}"/><stop offset="0.5" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{IRON}"/></radialGradient>')
    f.circle(x, y, 20, "url(#fy13h-ball)", INK, 3)
    # ten hands in front, each with a stopwatch stopped a little apart
    for k in range(10):
        cx = 66 + k * 119; cy = 520 + 10 * (k % 2)
        sleeve = ("#2f74b5", "#e8590c", "#2b8a3e", "#c92a2a", "#6c757d")[k % 5]
        skin = ("#f1c9a5", "#d9a77c", "#f3d2b4", "#b98157", "#eac09a")[k % 5]
        f.path(f"M{cx - 30},600 L{cx - 24},{cy + 52} H{cx + 24} L{cx + 30},600 Z", sleeve)                      # sleeve with a cuff
        f.path(f"M{cx + 6},600 L{cx + 10},{cy + 52} H{cx + 24} L{cx + 30},600 Z", S.dark(sleeve, 0.18))
        f.rect(cx - 26, cy + 46, 52, 12, S.light(sleeve, 0.25), None, 0, 4)
        f.path(f"M{cx - 24},{cy + 50} C{cx - 30},{cy + 20} {cx - 22},{cy - 2} {cx},{cy} C{cx + 24},{cy - 2} {cx + 32},{cy + 22} {cx + 24},{cy + 50} Z", skin)   # palm
        H.stopwatch(f, cx, cy, 40, 0.30 + 0.12 * (rnd(k, 4) - 0.5))
        for j in range(3):                                                                    # fingers curled round the watch
            f.add(f'<ellipse cx="{cx + 36}" cy="{cy - 12 + 15 * j}" rx="11" ry="7.5" fill="{skin}" stroke="{S.dark(skin, 0.3)}" stroke-width="1.5"/>')
        f.path(f"M{cx - 6},{cy - 44} q-2,-16 8,-20 q10,2 8,18 Z", skin, S.dark(skin, 0.3), 1.5)        # the thumb on the button
    return f.svg()


def _dots(f, X, ya, values, binw, color=COLD, step=16, r=7):
    """Readings stacked in bins of binw on the axis at height ya; returns the highest stack's top y."""
    bins = {}
    for v in values:
        bins.setdefault(round(v / binw), []).append(v)
    top = ya
    for b, vs in bins.items():
        for j, v in enumerate(vs):
            cy = ya - 12 - j * step
            f.circle(X(b * binw), cy, r, color, WHITE, 2)
            top = min(top, cy - r)
    return top


def _axis(f, X, ya, lo, hi, ticks, title=r"t\ (\text{s})", ext=24):
    """A time axis with an arrowhead, ticks with LaTeX numbers (decimal comma) and the title at the arrow end."""
    f.arrow(X(lo) - 12, ya, X(hi) + ext, ya, INK, 2.5, 13)
    for t in ticks:
        f.line(X(t), ya, X(t), ya + 7, INK, 2)
        f.tex(X(t), ya + 26, fi(t), "middle")
    if title:
        f.tex(X(hi) + ext + 6, ya, title, "start")


def error_types():
    f = Fig("fy13-err", 400, "Kaavakuva samasta mittauksesta kahdella tavalla, aika-akseli mittakaavassa. Ylhäällä on satunnaisvirhe: "
            "kymmenen tulosta hajaantuu oikean arvon 2,40 s molemmin puolin, ja keskiarvo 2,41 s on lähellä oikeaa arvoa. "
            "Alhaalla on systemaattinen virhe: kymmenen tulosta on tiiviissä ryhmässä, mutta ryhmä on kokonaan oikean arvon "
            "oikealla puolella ja keskiarvo 2,59 s on noin 0,19 s liian suuri.")
    X = lambda t: 60 + (t - 2.2) / 0.6 * 430
    A = [2.30, 2.34, 2.36, 2.38, 2.40, 2.41, 2.43, 2.45, 2.48, 2.52]
    B = [2.55, 2.57, 2.58, 2.58, 2.59, 2.60, 2.60, 2.61, 2.62, 2.64]
    for ya, vals, title, sys_ in ((158, A, r"\text{Satunnaisvirhe: tulokset hajaantuvat}", False),
                                  (354, B, r"\text{Systemaattinen virhe: tulokset siirtyvät}", True)):
        f.tex(14, ya - 132, title, "start")
        m = sum(vals) / len(vals)
        f.line(X(2.4), ya, X(2.4), ya - 86, GOOD, 2.5, "7 6")
        f.line(X(m), ya, X(m), ya - 86, INK, 2.5)
        _dots(f, X, ya, vals, 0.02)
        _axis(f, X, ya, 2.2, 2.8, [2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8])
        f.tex(X(2.4) - 9, ya - 100, r"\text{oikea arvo}", "end", GOOD)
        f.tex(X(m) + 9, ya - 100, r"\text{keskiarvo}", "start")
        if sys_:
            f.arrow(X(2.4) + 2, ya - 66, X(m) - 2, ya - 66, HOT, 3.5, 14)
            f.tex((X(2.4) + X(m)) / 2, ya - 84, r"\Delta t_\text{sys}", "middle", HOT)
    f.line(24, 206, 576, 206, MUTED, 1.5, "8 6")
    return f.svg()


def range_half():
    f = Fig("fy13-half", 330, "Kaavakuva, ei lukuarvoja: kuusi mittaustulosta aika-akselilla. Suurin tulos t_max ja pienin tulos "
            "t_min rajaavat vaihteluvälin, jonka pituus on t_max − t_min. Keskiarvo on merkitty pystyviivalla. Vaihteluvälin "
            "puolikas Δt on arvio satunnaisvirheestä, ja tulos ilmoitetaan muodossa keskiarvo plus miinus Δt.")
    X = lambda t: 70 + (t - 3.0) / 0.4 * 420
    vals = [3.07, 3.12, 3.15, 3.19, 3.25, 3.31]
    m = sum(vals) / len(vals)
    ya = 170
    _dots(f, X, ya, vals, 0.01)
    # the range above the dots
    f.line(X(3.07), ya - 26, X(3.07), ya - 66, MUTED, 1.5, "6 5"); f.line(X(3.31), ya - 26, X(3.31), ya - 66, MUTED, 1.5, "6 5")
    f.arrow(X(3.07) + 8, ya - 56, X(3.31) - 8, ya - 56, MUTED, 2.5, 12); f.arrow(X(3.31) - 8, ya - 56, X(3.07) + 8, ya - 56, MUTED, 2.5, 12)
    f.tex(X(3.19), ya - 88, r"t_\text{max} - t_\text{min}", "middle")
    _axis(f, X, ya, 3.0, 3.4, [], title=r"t")
    f.tex(X(3.07), ya + 26, r"t_\text{min}", "middle"); f.tex(X(3.31), ya + 26, r"t_\text{max}", "middle")
    f.path(f"M{X(m)},{ya + 7} L{X(m) - 8},{ya + 22} L{X(m) + 8},{ya + 22} Z", INK)      # the mean, a marker under the axis
    f.tex(X(m), ya + 44, r"\bar{t}", "middle")
    # the result bar: mean plus and minus the half-range
    d = (3.31 - 3.07) / 2
    f.rect(X(m - d), 236, X(m + d) - X(m - d), 16, GOOD_LIGHT, GOOD, 2.5)
    f.line(X(m), 230, X(m), 258, INK, 2.5)
    f.tex(X(m - d) - 10, 244, r"\bar{t} - \Delta t", "end"); f.tex(X(m + d) + 10, 244, r"\bar{t} + \Delta t", "start")
    f.tex(300, 292, r"\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}", "middle")
    return f.svg()


def _scale(f, x0, reading, empty, obj_label=None):
    """A kitchen scale: body, pan and a display with the reading. x0 is the left edge of the 200 px wide body."""
    f.rect(x0, 206, 200, 100, ALUMINIUM, INK, 2.5, 10)
    f.rect(x0 + 24, 188, 152, 18, METAL_EDGE, INK, 2.5, 6)
    f.rect(x0 + 40, 238, 120, 44, GLASS, INK, 2)
    f.tex(x0 + 100, 260, reading, "middle")
    if not empty:
        f.rect(x0 + 62, 128, 76, 60, IRON, INK, 2.5, 6)
        f.line(x0 + 74, 142, x0 + 126, 142, ALUMINIUM, 2)


def zero_scale():
    f = Fig("fy13-zero", 392, "Kaavakuva, ei mittakaavassa: keittiövaaka kahdesti. Vasemmalla pannu on tyhjä, mutta vaaka näyttää "
            "1,2 g, joten nollakohta on väärin. Oikealla pannulla on rautakappale ja vaaka näyttää 48,7 g. Kappaleen massa "
            "saadaan vähentämällä nollalukema lukemasta: 48,7 g miinus 1,2 g on 47,5 g.")
    _scale(f, 50, r"1{,}2\,\text{g}", True)
    _scale(f, 350, r"48{,}7\,\text{g}", False)
    f.tex(150, 336, r"\text{tyhjä: } m_0", "middle"); f.tex(450, 336, r"\text{lukema } m_\text{lukema}", "middle")
    f.line(300, 48, 300, 352, MUTED, 1.5, "8 6")
    f.tex(300, 28, r"\text{systemaattinen virhe: nollakohta}", "middle")
    f.tex(300, 372, r"m = m_\text{lukema} - m_0", "middle")
    return f.svg()


def example_plot():
    f = Fig("fy13-ex", 330, "Mittaustulokset (t, aika) mittakaavassa: kuusi tulosta väliltä 3,07 s – 3,31 s, keskiarvo 3,18 s ja "
            "tulos 3,18 s ± 0,12 s vihreällä palkilla.")
    X = lambda t: 70 + (t - 3.0) / 0.4 * 420
    vals = [3.12, 3.25, 3.07, 3.31, 3.19, 3.15]
    m = sum(vals) / len(vals)
    ya = 150
    f.line(X(m), ya, X(m), ya - 88, INK, 2.5)
    _dots(f, X, ya, vals, 0.01)
    _axis(f, X, ya, 3.0, 3.4, [3.0, 3.1, 3.2, 3.3, 3.4])
    f.tex(X(m) - 10, ya - 100, r"\bar{t} = 3{,}18\,\text{s}", "end")
    f.rect(X(m - 0.12), 236, X(m + 0.12) - X(m - 0.12), 16, GOOD_LIGHT, GOOD, 2.5)
    f.line(X(m), 230, X(m), 258, INK, 2.5)
    f.tex(300, 292, r"t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}", "middle")
    return f.svg()


def pendulum_dots():
    """A task-only picture: five repeated readings on a time axis, no mean and no range marked, to be read off."""
    f = Fig("fy13-dots", 170, "Kuvaaja mittakaavassa: heilurin kymmenen heilahduksen aika t viidessä toistossa pisteinä aika-akselilla. "
            "Akseli kulkee 12,0 sekunnista 13,0 sekuntiin, pystyviivat ja pienet merkit joka 0,1 sekunnin kohdalla ja numerot "
            "joka 0,2 sekunnin kohdalla. Pisteet ovat kohdissa 12,2 s, 12,4 s, 12,6 s, 12,7 s ja 12,9 s.")
    X = lambda t: 50 + (t - 12.0) * 440
    ya = 110
    for k in range(11):
        t = 12.0 + k / 10
        f.line(X(t), ya - 70, X(t), ya, RULE_LIGHT, 1.5)
        f.line(X(t), ya, X(t), ya + 7, INK, 2)
    _dots(f, X, ya, [12.4, 12.9, 12.6, 12.2, 12.7], 0.1)
    _axis(f, X, ya, 12.0, 13.0, [12.0, 12.2, 12.4, 12.6, 12.8, 13.0])
    return f.svg()


def paper_stack():
    """Task illustration (fy1-3-L3-02): a stack of copy paper beside an upright ruler; no readings."""
    f = S.scene("fy13-paper", "Kuvitus: pöydällä on pino kopiopaperia, ja pinon vieressä seisoo pystysuora viivain. Pinon yläreuna on viivaimen "
                "lukeman kohdalla, mutta numeroita ei ole kuvassa.")
    f.rect(0, 0, 600, 360, "#f3efe6")
    H.wood(f, 0, 290, 600, 70, "fy13p-top")
    x0, y0, w, h, d = 150, 170, 260, 120, 46          # front face of the stack, depth drawn up-right
    f.path(f"M{x0},{y0} l{d},-{d * 0.55} h{w} l-{d},{d * 0.55} Z", "#ffffff", "#9aa3ad", S.W_OBJ)
    f.path(f"M{x0 + w},{y0} l{d},-{d * 0.55} v{h} l-{d},{d * 0.55} Z", "#e4e7ea", "#9aa3ad", S.W_OBJ)
    f.rect(x0, y0, w, h, "#f6f7f8", "#9aa3ad", S.W_OBJ)
    for k in range(1, 40):                                # sheet edges on the front face
        f.add(f'<line x1="{x0}" y1="{n(y0 + k * h / 40)}" x2="{x0 + w}" y2="{n(y0 + k * h / 40)}" stroke="#c9ced3" stroke-width="0.8"/>')
    rx = 470                                              # ruler standing upright
    f.rect(rx, 60, 34, 230, "#f1dfb5", S.dark("#f1dfb5", 0.4), S.W_OBJ, 2)
    for k in range(0, 46):
        y = 286 - k * 5
        f.line(rx, y, rx + (14 if k % 10 == 0 else 9 if k % 5 == 0 else 6), y, "#3a4350", 1)
    f.line(x0 + w + d + 4, y0 - d * 0.55, rx - 4, y0 - d * 0.55, "#6b7480", 1.25, "5 4")
    return f.svg()


def pendulum_timing():
    """Task illustration (fy1-3-L2-07): a pendulum on a stand, a hand ready on a stopwatch; no numbers."""
    f = S.scene("fy13-pend", "Kuvitus: telineeseen ripustettu heiluri heilahtaa, ja haalea välikuva näyttää sen ääriasennon. Etualalla käsi pitää "
                "sekuntikelloa peukalo käynnistysnapilla.")
    f.rect(0, 0, 600, 360, "#f3efe6")
    H.wood(f, 0, 310, 600, 50, "fy13t-top")
    f.rect(120, 296, 160, 14, "#6c757d", S.dark("#6c757d", 0.35), S.W_OBJ, 3)
    f.rect(132, 40, 12, 258, "#c4ccd4", S.dark("#c4ccd4", 0.45), S.W_OBJ, 2)
    f.rect(132, 40, 140, 10, "#c4ccd4", S.dark("#c4ccd4", 0.45), S.W_OBJ, 2)
    px, py, L = 250, 50, 200
    for ang, op in ((-22, 0.3), (14, 1)):
        a = math.radians(ang); bx, by = px + L * math.sin(a), py + L * math.cos(a)
        f.add(f'<g opacity="{op}"><line x1="{px}" y1="{py}" x2="{n(bx)}" y2="{n(by)}" stroke="#3a4350" stroke-width="1.5"/></g>')
        if op < 1: f.add(f'<circle cx="{n(bx)}" cy="{n(by)}" r="16" fill="#9aa3ad" opacity="0.3"/>')
        else: f.ball("fy13t-bob", bx, by, 16, "#aab4bf")
    f.add(f'<path d="M{n(px + 0.8 * L * math.sin(math.radians(-22)))},{n(py + 0.8 * L * math.cos(math.radians(-22)))} A{0.8 * L},{0.8 * L} 0 0 0 {n(px + 0.8 * L * math.sin(math.radians(14)))},{n(py + 0.8 * L * math.cos(math.radians(14)))}" '
          f'fill="none" stroke="#6b7480" stroke-width="1.25" stroke-dasharray="5 4"/>')
    cx, cy, skin, sleeve = 470, 250, "#eac09a", "#2f74b5"
    f.path(f"M{cx - 30},360 L{cx - 24},{cy + 52} H{cx + 24} L{cx + 30},360 Z", sleeve)
    f.rect(cx - 26, cy + 46, 52, 12, S.light(sleeve, 0.25), None, 0, 4)
    f.path(f"M{cx - 24},{cy + 50} C{cx - 30},{cy + 20} {cx - 22},{cy - 2} {cx},{cy} C{cx + 24},{cy - 2} {cx + 32},{cy + 22} {cx + 24},{cy + 50} Z", skin)
    H.stopwatch(f, cx, cy, 40, 0.0)
    for j in range(3): f.add(f'<ellipse cx="{cx + 36}" cy="{cy - 12 + 15 * j}" rx="11" ry="7.5" fill="{skin}" stroke="{S.dark(skin, 0.3)}" stroke-width="1.5"/>')
    f.path(f"M{cx - 6},{cy - 44} q-2,-16 8,-20 q10,2 8,18 Z", skin, S.dark(skin, 0.3), 1.5)
    return f.svg()


FIGURES = {"hero": hero, "paper-stack": paper_stack, "pendulum-timing": pendulum_timing, "error-types": error_types, "range-half": range_half, "zero-scale": zero_scale, "example-plot": example_plot,
           "pendulum-dots": pendulum_dots}

REUSE = {
    "paper-stack": "safe: the situation only, a paper stack beside a ruler; no readings",
    "pendulum-timing": "safe: the situation only, a pendulum and a hand-held stopwatch; no numbers",
    "pendulum-dots": "safe: five repeated readings on a time axis, no mean or range marked",
}
