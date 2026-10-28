"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-1` writes them into lesson.md.
Colours: the energy forms keep the colours of the simulation (potential blue, kinetic light orange, thermal red, hatched);
materials and arrows follow NOTES.md §3."""
import math
from figlib import (Fig, INK, MUTED, WHITE, GLASS, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, ALUMINIUM, METAL_EDGE,
                    IRON, COPPER, SAND, SAND_DARK, GRAIN, n, fi)

POT, KIN, THM = COLD, HEAT_LIGHT, HOT          # potential, kinetic and thermal energy: the same colours as in the simulation


def _ball(f, gid, cx, cy, r, light=ALUMINIUM, dark=IRON):
    f.defs_add(f'<radialGradient id="{gid}" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></radialGradient>')
    f.circle(cx, cy, r, f"url(#{gid})", INK, 2.5)
    f.circle(cx - r * 0.35, cy - r * 0.38, max(2, r * 0.18), WHITE, None)


def _name(f, cx, y, first, second="energia", anchor="middle"):
    """A two-line name: the first part of the compound word, then 'energia'."""
    f.tex(cx, y, rf"\text{{{first}}}", anchor)
    f.tex(cx, y + 30, rf"\text{{{second}}}", anchor)


def _battery(f, cx, cy):
    f.rect(cx - 21, cy - 28, 42, 74, COPPER, INK, 2.5, rx=5)
    f.rect(cx - 21, cy - 28, 42, 22, ALUMINIUM, INK, 2.5, rx=5)
    f.rect(cx - 9, cy - 38, 18, 10, ALUMINIUM, INK, 2.5, rx=2)
    f.line(cx - 8, cy + 14, cx + 8, cy + 14, WHITE, 3); f.line(cx, cy + 6, cx, cy + 22, WHITE, 3)


# ---------------------------------------------------------------- the seven energy forms
def forms():
    f = Fig("fy21-forms", 396, "Kaavakuva: energialajit esimerkein. Mekaaninen energia on potentiaalienergiaa (kallion reunalla oleva pallo) "
            "ja liike-energiaa (vierivä pallo). Lisäksi kuvassa ovat lämpöenergia (kuuma kahvikuppi), kemiallinen energia (paristo), "
            "säteilyenergia (Aurinko), sähköenergia (salama) ja ydinenergia (atomiydin). Kuva on kaavamainen, ei mittakaavassa.")
    f.line(30, 44, 270, 44, INK, 2); f.line(30, 44, 30, 54, INK, 2); f.line(270, 44, 270, 54, INK, 2)
    f.tex(150, 20, r"\text{mekaaninen energia}", "middle")
    r1, r2 = 96, 270
    xs1 = [75, 225, 375, 525]; xs2 = [150, 300, 450]
    # 1 potential energy: a ball on the edge of a cliff, the height above the ground level
    cx = xs1[0]
    f.rect(cx - 42, r1 - 14, 40, 54, ALUMINIUM, INK, 2.5)
    f.line(cx - 42, r1 + 10, cx - 2, r1 + 10, METAL_EDGE, 1.5); f.line(cx - 42, r1 + 26, cx - 2, r1 + 26, METAL_EDGE, 1.5)
    f.rect(cx - 52, r1 + 40, 104, 8, SAND, INK, 2)
    _ball(f, "fy21-pot", cx - 22, r1 - 26, 11)
    f.line(cx + 16, r1 - 26, cx + 16, r1 + 40, MUTED, 1.5, "6 5")
    f.arrow(cx + 16, r1 - 8, cx + 16, r1 + 38, MUTED, 2, 10)
    f.tex(cx + 24, r1 - 14, r"h", "start")
    # 2 kinetic energy: a rolling ball with speed lines and a velocity arrow
    cx = xs1[1]
    f.rect(cx - 52, r1 + 40, 104, 8, SAND, INK, 2)
    _ball(f, "fy21-kin", cx + 2, r1 + 24, 16)
    for i in range(3): f.line(cx - 48, r1 + 12 + i * 12, cx - 26 - (i % 2) * 4, r1 + 12 + i * 12, MUTED, 2)
    f.arrow(cx + 4, r1 - 12, cx + 50, r1 - 12, HEAT, 4, 14)
    f.tex(cx + 28, r1 - 34, r"v", "middle")
    # 3 thermal energy: a hot mug with steam
    cx = xs1[2]
    f.path(f"M{n(cx - 26)},{n(r1 - 8)} L{n(cx - 22)},{n(r1 + 38)} Q{n(cx - 22)},{n(r1 + 46)} {n(cx - 14)},{n(r1 + 46)} L{n(cx + 14)},{n(r1 + 46)} Q{n(cx + 22)},{n(r1 + 46)} {n(cx + 22)},{n(r1 + 38)} L{n(cx + 26)},{n(r1 - 8)} Z", GLASS, INK, 2.5)
    f.path(f"M{n(cx - 24.5)},{n(r1 + 4)} L{n(cx - 21)},{n(r1 + 38)} Q{n(cx - 21)},{n(r1 + 44)} {n(cx - 14)},{n(r1 + 44)} L{n(cx + 14)},{n(r1 + 44)} Q{n(cx + 21)},{n(r1 + 44)} {n(cx + 21)},{n(r1 + 38)} L{n(cx + 24.5)},{n(r1 + 4)} Z", HOT_LIGHT, None, 0)
    f.path(f"M{n(cx + 25)},{n(r1 + 4)} Q{n(cx + 46)},{n(r1 + 4)} {n(cx + 46)},{n(r1 + 20)} Q{n(cx + 46)},{n(r1 + 34)} {n(cx + 22)},{n(r1 + 34)}", "none", INK, 2.5)
    for dx in (-12, 0, 12):
        f.path(f"M{n(cx + dx)},{n(r1 - 16)} q-7,-9 0,-18 q7,-9 0,-18", "none", HOT, 2.5)
    # 4 chemical energy: a battery
    _battery(f, xs1[3], r1 + 2)
    # 5 radiant energy: the Sun with rays
    cx = xs2[0]
    for i in range(12):
        a = math.radians(i * 30)
        f.line(cx + math.cos(a) * 29, r2 + math.sin(a) * 29, cx + math.cos(a) * 43, r2 + math.sin(a) * 43, HEAT, 3, cap="round")
    f.circle(cx, r2, 21, HEAT_LIGHT, HEAT, 2.5)
    # 6 electrical energy: a lightning bolt between two wires
    cx = xs2[1]
    f.line(cx - 54, r2 + 40, cx - 20, r2 + 40, INK, 2.5); f.line(cx + 22, r2 - 40, cx + 54, r2 - 40, INK, 2.5)
    f.path(f"M{n(cx + 8)},{n(r2 - 42)} L{n(cx - 20)},{n(r2 + 4)} L{n(cx - 3)},{n(r2 + 4)} L{n(cx - 10)},{n(r2 + 42)} L{n(cx + 22)},{n(r2 - 8)} L{n(cx + 5)},{n(r2 - 8)} Z", HEAT_LIGHT, INK, 2.5)
    # 7 nuclear energy: a nucleus of protons and neutrons, three arrows out
    cx = xs2[2]
    pts = [(0, 0)] + [(18 * math.cos(math.radians(60 * i + 30)), 18 * math.sin(math.radians(60 * i + 30))) for i in range(6)]
    for i, (dx, dy) in enumerate(pts):
        f.circle(cx + dx, r2 + dy, 10, COPPER if i % 2 == 0 else ALUMINIUM, INK, 2)
    for a in (-90, 30, 150):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        f.arrow(cx + ca * 40, r2 + sa * 40, cx + ca * 58, r2 + sa * 58, HEAT, 3, 10)
    for cx, first in zip(xs1, ["potentiaali-", "liike-", "lämpö-", "kemiallinen"]): _name(f, cx, r1 + 74, first)
    for cx, first in zip(xs2, ["säteily-", "sähkö-", "ydin-"]): _name(f, cx, r2 + 72, first)
    return f.svg()


# ---------------------------------------------------------------- energy changes form: a torch
def chain():
    f = Fig("fy21-chain", 250, "Kaavakuva: energian muuttuminen taskulampussa. Paristossa on kemiallista energiaa. Se muuttuu sähköenergiaksi, "
            "ja lamppu muuttaa sähköenergian säteilyenergiaksi eli valoksi sekä lämpöenergiaksi. Suurin osa muuttuu lämmöksi, joten lämpönuoli on leveämpi. "
            "Kuva on kaavamainen, nuolten leveys ei ole mittakaavassa.")
    cy = 118
    _name(f, 80, 26, "kemiallinen")
    _battery(f, 80, cy)
    f.tex(80, cy + 80, r"\text{paristo}", "middle")
    f.block_arrow(148, cy, 262, cy, HEAT_LIGHT, shaft=20, head=40, headlen=28)
    _name(f, 205, 26, "sähkö-")
    # a bulb: glass globe, filament, metal base
    bx = 322
    f.rect(bx - 15, cy + 28, 30, 26, ALUMINIUM, INK, 2.5, rx=3)
    f.line(bx - 15, cy + 38, bx + 15, cy + 38, METAL_EDGE, 1.5); f.line(bx - 15, cy + 46, bx + 15, cy + 46, METAL_EDGE, 1.5)
    f.circle(bx, cy - 6, 36, GLASS, INK, 2.5)
    f.path(f"M{n(bx - 12)},{n(cy + 28)} L{n(bx - 12)},{n(cy + 6)} L{n(bx - 6)},{n(cy - 6)} L{n(bx)},{n(cy + 6)} L{n(bx + 6)},{n(cy - 6)} L{n(bx + 12)},{n(cy + 6)} L{n(bx + 12)},{n(cy + 28)}", "none", HOT, 2.5)
    f.tex(bx, cy + 80, r"\text{lamppu}", "middle")
    f.block_arrow(366, cy - 22, 430, cy - 52, HEAT_LIGHT, shaft=8, head=26, headlen=22)
    f.block_arrow(366, cy + 22, 430, cy + 52, HEAT_LIGHT, shaft=24, head=40, headlen=26)
    f.tex(444, cy - 56, r"\text{säteily-}", "start"); f.tex(444, cy - 26, r"\text{energia}", "start")
    f.tex(444, cy + 36, r"\text{lämpö-}", "start"); f.tex(444, cy + 66, r"\text{energia}", "start")
    return f.svg()


# ---------------------------------------------------------------- conservation: the same total at the start, on the way and at the end
def _skater(f, x, y, ang, s=0.66):
    """A small skateboarder standing on the track at (x, y); ang in degrees follows the slope of the track."""
    body = (f'<g transform="translate({n(x)},{n(y)}) rotate({ang:.1f}) scale({s})" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="{SAND}" stroke="{GRAIN}" stroke-width="1.5"/>'
            f'<circle cx="-10" cy="-3.4" r="3.4" fill="{INK}"/><circle cx="10" cy="-3.4" r="3.4" fill="{INK}"/>'
            f'<path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="{IRON}" stroke-width="4.4"/>'
            f'<path d="M1,-28 L4,-44" fill="none" stroke="{POT}" stroke-width="7"/>'
            f'<path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="{SAND_DARK}" stroke-width="3.2"/>'
            f'<circle cx="6" cy="-51" r="6.4" fill="{SAND_DARK}"/>'
            f'<path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="{INK}"/></g>')
    f.add(body)


def conservation():
    f = Fig("fy21-conserve", 380, "Kaavakuva: skeittari half-pipessä kolmella hetkellä ja kunkin hetken energiat pylväinä. Alussa skeittari on reunalla levossa, "
            "ja koko energia 800 J on potentiaalienergiaa. Välillä potentiaalienergiaa on 300 J, liike-energiaa 450 J ja lämpöenergiaa 50 J. "
            "Pohjalla potentiaalienergiaa ei ole, liike-energiaa on 700 J ja lämpöenergiaa 100 J. Pylväiden korkeus on mittakaavassa, ja jokaisen "
            "pylvään kokonaiskorkeus vastaa 800 joulea eli kaikilla hetkillä energiaa on yhtä paljon.")
    f.defs_add(f'<pattern id="fy21-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<rect width="8" height="8" fill="{THM}"/><line x1="0" y1="0" x2="0" y2="8" stroke="#f2a69c" stroke-width="3"/></pattern>')
    cols = [100, 300, 500]
    W, HH, top = 80, 54, 38                        # half width of the half-pipe, its depth, y of the rims (figure units)
    bottom = top + HH
    for cx in cols:                                # the half-pipe: a parabola (a quadratic Bezier), a concrete wall under it
        f.path(f"M{cx - W - 10},{top} L{cx - W},{top} Q{cx},{2 * bottom - top} {cx + W},{top} L{cx + W + 10},{top} L{cx + W + 10},{bottom + 14} L{cx - W - 10},{bottom + 14} Z", ALUMINIUM, None, 0)
        f.path(f"M{cx - W - 10},{top} L{cx - W},{top} Q{cx},{2 * bottom - top} {cx + W},{top} L{cx + W + 10},{top}", "none", INK, 3)
    base, per = 292, 0.16                          # bar baseline and pixels per joule
    data = [(800, 0, 0, -1.0), (300, 450, 50, -math.sqrt(300 / 800)), (0, 700, 100, 0.0)]
    for cx, (ep, ek, eth, u) in zip(cols, data):
        _skater(f, cx + W * u, bottom - HH * u * u - 1, math.degrees(math.atan(2 * HH * u / W)) * -1 if u else 0)
        x0 = cx - 55; y = base
        for val, fill in ((eth, "url(#fy21-hatch)"), (ek, KIN), (ep, POT)):
            if val <= 0: continue
            h = val * per
            f.rect(x0, y - h, 44, h, fill, INK, 2); y -= h
        # values beside the segments
        y = base
        for val in (eth, ek, ep):
            if val <= 0: continue
            h = val * per
            f.tex(x0 + 54, min(y - h / 2, base - 15), rf"{fi(val)}\,\text{{J}}", "start"); y -= h
    for cx, cap in zip(cols, ["alussa", "välillä", "lopussa"]):
        f.tex(cx, base + 26, rf"\text{{{cap}}}", "middle")
    ytot = base - 800 * per
    f.line(24, ytot, 576, ytot, INK, 2, "8 6")
    f.tex(300, ytot - 20, r"\text{kokonaisenergia } E = 800\,\text{J}", "middle")
    f.line(30, base, 570, base, INK, 2.5)
    # legend
    ly = base + 66
    for lx, col, sym in ((120, POT, r"E_\text{p}"), (270, KIN, r"E_\text{k}"), (420, "url(#fy21-hatch)", r"E_\text{lämpö}")):
        f.rect(lx, ly - 10, 20, 20, col, INK, 2)
        f.tex(lx + 30, ly, sym, "start")
    return f.svg()


FIGURES = {"energialajit": forms, "energian-muuttuminen": chain, "sailyminen": conservation}
