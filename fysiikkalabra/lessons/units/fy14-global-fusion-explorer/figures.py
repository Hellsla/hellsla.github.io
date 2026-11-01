"""Figures of the unit fy14-global-fusion-explorer (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-global-fusion-explorer` writes them into content/en/units/fy14-global-fusion-explorer/unit.md. hero: the Earth
from space with glowing research sites joined by arcs, a network; no text, no counts that answer a prediction."""
import figlib
from figlib import INK, WHITE, HEAT, HEAT_LIGHT, n
import herolib as H

figlib.set_language({}, ".")
GLOW = "#ffd43b"


def hero():
    f = H.hero("fy14gfe-hero", "Illustration: the Earth seen from space against a dark, starry sky. Small glowing yellow "
               "points mark places on the continents, and thin bright arcs rise above the globe to join many of the points "
               "into a web, like flight routes on an airline map. Around the Earth a faint ring of light suggests a "
               "fusion plasma.")
    H.space(f, seed=5, count=90)
    cx, cy, r = 600, 330, 240
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.55}" ry="{r * 0.42}" fill="none" stroke="#b197fc" stroke-width="6" stroke-opacity="0.35" transform="rotate(-12 {cx} {cy})"/>')
    H.earth(f, "gfe", cx, cy, r)
    u = r / 100
    pts = [(-62, -52), (-45, -35), (-30, -60), (-18, -42), (-40, -10), (-55, 10), (-25, 30), (-8, -55),
           (48, 25), (62, 15), (70, 40), (45, 50), (-70, -20), (5, -48)]
    P = [(cx + x * u, cy + y * u) for x, y in pts]
    links = [(0, 8), (1, 9), (2, 10), (3, 11), (4, 8), (5, 9), (0, 3), (1, 6), (7, 10), (12, 2), (13, 11), (6, 9), (3, 13), (5, 12)]
    for a, b in links:
        (x1, y1), (x2, y2) = P[a], P[b]
        mx, my = (x1 + x2) / 2, min(y1, y2) - 0.35 * abs(x2 - x1) - 30
        f.path(f"M{n(x1)},{n(y1)} Q{n(mx)},{n(my)} {n(x2)},{n(y2)}", stroke=GLOW, w=2.5, extra='stroke-opacity="0.8"')
    for x, y in P:
        f.circle(x, y, 13, HEAT_LIGHT)
        f.circle(x, y, 6, GLOW, HEAT, 1.5)
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.55}" ry="{r * 0.42}" fill="none" stroke="#b197fc" stroke-width="6" stroke-opacity="0.6" '
          f'stroke-dasharray="{n(r * 2.4)} {n(r * 10)}" stroke-dashoffset="{n(-r * 0.2)}" transform="rotate(-12 {cx} {cy})"/>')
    return f.svg()


FIGURES = {"hero": hero}
