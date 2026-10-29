#!/usr/bin/env python3
"""Writes the Ruukkilabra logos (teacher 2026-10-29) into assets/shared/brand/ as clean SVG:
the arch symbol (ruukkilabra-symboli.svg, hand-drawn after the teacher's PNG, also the favicon), the wordmark
(ruukkilabra-logo.svg) and the wordmark with the subtitle of each language (ruukkilabra-logo-<lang>.svg).
The letters are Plus Jakarta Sans ExtraBold turned into paths, so a logo looks the same without the font.
Needs fonttools and brotli (pip install fonttools brotli); run it again only when a logo or a subtitle changes."""
import io, pathlib, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/shared/brand"
FONT = ROOT / "templates/vendor/fonts/plus-jakarta-sans-latin-wght-normal.woff2"
GREEN, ORANGE = "#1a4b2e", "#b85f2a"
SUBTITLES = {"fi": "LUKION FYSIIKKA", "en": "UPPER SECONDARY PHYSICS"}
SYMBOL = (OUT / "ruukkilabra-symboli.svg").read_text()
SYMBOL_BOX = (196, 196, 862, 862)               # viewBox of the symbol; the arch spans y 238..1012 inside it
ARCH_TOP, ARCH_BOTTOM, ARCH_LEFT, ARCH_RIGHT = 238, 1012, 211, 1042


def font(weight):
    f = TTFont(FONT)
    return instantiateVariableFont(f, {"wght": weight})


def text_path(f, text, x, baseline, cap, tracking=0.0):
    """The text as one SVG path whose capital letters are cap units tall; returns (path data, width)."""
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    s = cap / f["OS/2"].sCapHeight
    pen = SVGPathPen(gs)
    for ch in text:
        name = cmap[ord(ch)]
        gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        x += hmtx[name][0] * s + tracking * cap
    return pen.getCommands(), x - tracking * cap


def num(d):
    return re.sub(r"(\d+\.\d{1,2})\d+", r"\1", d)


def symbol_group(height, x, y):
    """The arch drawn height units tall with its top-left at (x, y)."""
    s = height / (ARCH_BOTTOM - ARCH_TOP)
    inner = re.search(r"<svg[^>]*>(.*)</svg>", SYMBOL, re.S).group(1)
    return f'<g transform="translate({x - ARCH_LEFT * s:.2f} {y - ARCH_TOP * s:.2f}) scale({s:.5f})">{inner}</g>', (ARCH_RIGHT - ARCH_LEFT) * s


def logo(subtitle=None):
    heavy, bold = font(800), font(700)
    H = 365                                     # arch height; the proportions follow the teacher's PNG
    sym, w = symbol_group(H, 0, 0)
    tx = w + 0.15 * H
    cap = H * (0.556 if subtitle else 0.61)
    base = H * (0.735 if subtitle else 0.84)
    word, end = text_path(heavy, "Ruukkilabra", tx, base, cap)
    parts = [sym, f'<path fill="{GREEN}" d="{num(word)}"/>']
    if subtitle:
        sub, end2 = text_path(bold, subtitle, tx + 4, 0.98 * H, 0.156 * H, tracking=0.42)
        parts.append(f'<path fill="{GREEN}" d="{num(sub)}"/>')
        end = max(end, end2)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {end:.0f} {H}" role="img"><title>Ruukkilabra</title>{"".join(parts)}</svg>\n'


(OUT / "ruukkilabra-logo.svg").write_text(logo())
for lang, sub in SUBTITLES.items(): (OUT / f"ruukkilabra-logo-{lang}.svg").write_text(logo(sub))
print("wrote", ", ".join(p.name for p in sorted(OUT.glob("ruukkilabra-logo*.svg"))))
