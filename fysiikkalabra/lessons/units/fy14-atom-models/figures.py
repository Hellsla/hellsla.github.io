"""Figures of the unit fy14-atom-models (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-atom-models` writes them into content/en/units/fy14-atom-models/unit.md. English: decimal point.
The alpha paths are integrated here for a pure Coulomb force; the hydrogen levels are E_n = -13.6 eV / n^2; the
Balmer wavelengths are the measured values in air (Wikipedia, Balmer series, 2026-11-01)."""
import math
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, SAND, SAND_LIGHT, n)
import herolib as H

figlib.set_language({}, ".")

BALMER = [(656.3, "#e03131"), (486.1, "#15aabf"), (434.0, "#3b5bdb"), (410.2, "#7048e8")]   # measured, in air
D_FM = 27.4          # distance of closest approach, head-on, of a 2.0e7 m/s alpha particle to a gold nucleus (computed in the text)


def hero():
    """A dark lab: a glowing hydrogen discharge tube, its light through a slit and a grating onto a white screen, where
    it makes four separate coloured lines. No text."""
    f = H.hero("fy14am-hero", "Illustration: a darkened laboratory. On the left a thin glass tube on a stand glows with a soft "
               "pink-violet light. Its light passes through a narrow slit and a small glass grating on the bench. On a white "
               "screen on the right the light appears not as a rainbow but as four separate thin lines: red, turquoise, blue "
               "and violet, with darkness between them.")
    f.rect(0, 0, 1200, 600, H.grad(f, "am-room", "#26313c", "#1a222b"))
    f.rect(0, 470, 1200, 130, H.grad(f, "am-bench", "#7a5a32", "#5a4024"))
    f.line(0, 470, 1200, 470, "#a07a46", 4)
    # the discharge tube on a stand, glowing
    f.add('<defs><radialGradient id="am-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f3d9fa" stop-opacity="0.9"/><stop offset="1" stop-color="#cc5de8" stop-opacity="0"/></radialGradient></defs>')
    f.add('<ellipse cx="190" cy="270" rx="120" ry="210" fill="url(#am-glow)"/>')
    f.rect(184, 420, 12, 50, METAL_EDGE)
    f.rect(140, 460, 100, 12, METAL_EDGE, rx=4)
    f.rect(170, 70, 40, 34, IRON, INK, 2, 4)
    f.rect(170, 404, 40, 34, IRON, INK, 2, 4)
    f.rect(176, 104, 28, 300, "#e599f7", "#f8f0fc", 3, 12)
    f.rect(186, 112, 8, 284, "#fbe7ff", rx=4)
    f.line(190, 60, 190, 70, METAL_EDGE, 4)
    # the beam to the slit and grating
    f.path("M210,250 L470,262 L470,278 L210,290 Z", "#e599f7", extra='fill-opacity="0.25"')
    f.rect(462, 214, 16, 110, IRON, INK, 2)
    f.rect(466, 262, 8, 16, "#e599f7")
    f.rect(466, 324, 8, 146, METAL_EDGE)
    f.rect(560, 230, 20, 80, GLASS, METAL_EDGE, 3, 3)
    f.rect(566, 310, 8, 160, METAL_EDGE)
    f.path("M478,264 L560,262 L560,278 L478,276 Z", "#e599f7", extra='fill-opacity="0.3"')
    # the screen
    f.rect(900, 80, 220, 380, "#f8f9fa", INK, 3, 4)
    f.rect(1000, 460, 20, 12, METAL_EDGE)
    # fans of light from the grating to four lines on the screen
    ys = [380, 230, 180, 160]
    for (lam, col), y in zip(BALMER, ys):
        f.path(f"M580,268 L900,{y - 6} L900,{y + 6} L580,272 Z", col, extra='fill-opacity="0.22"')
        f.rect(904, y - 5, 212, 10, col)
    # the straight-through image of the slit, dimmer
    f.path("M580,268 L900,262 L900,274 L580,272 Z", "#e599f7", extra='fill-opacity="0.12"')
    return f.svg()


def alpha_path(b, x0=-7.0, xmax=7.0, dt=0.002):
    """Path of an alpha particle (units of d, speed 1 far away) past a nucleus at the origin, a = 0.5 r / |r|^3."""
    x, y, vx, vy = x0, b, 1.0, 0.0
    pts = [(x, y)]
    for _ in range(40000):
        def acc(x, y):
            r3 = (x * x + y * y) ** 1.5
            return 0.5 * x / r3, 0.5 * y / r3
        ax1, ay1 = acc(x, y)
        x2, y2 = x + vx * dt / 2, y + vy * dt / 2
        vx2, vy2 = vx + ax1 * dt / 2, vy + ay1 * dt / 2
        ax2, ay2 = acc(x2, y2)
        x, y = x + vx2 * dt, y + vy2 * dt
        vx, vy = vx + ax2 * dt, vy + ay2 * dt
        pts.append((x, y))
        if abs(x) > 7.5 or abs(y) > 4.2: break
    return pts[::20]


def scatter():
    """Alpha paths near one gold nucleus, to scale in femtometres."""
    f = Fig("fy14am-scatter", 420, "Drawing to scale of alpha particles that move from left to right past one gold nucleus, a small red "
            "dot in the middle. Each path starts at a different distance b from the line through the centre of the nucleus. "
            "Paths that start far from the line bend only a little. Paths closer to the line bend more, and the closest ones "
            "turn back towards the left. A scale bar shows 50 femtometres. The whole atom would be about 10 000 times wider "
            "than this drawing.")
    S, cx, cy = 34, 300, 240            # figure units per d (27.4 fm), position of the nucleus
    for b, col in ((0.12, HOT), (-0.3, HEAT), (0.6, "#7048e8"), (-1.2, COLD), (2.4, GOOD), (-3.6, MUTED)):
        pts = alpha_path(b)
        d = " ".join(f"{n(cx + S * x)},{n(cy - S * y)}" for x, y in pts if abs(cy - S * y - 240) < 230)
        f.add(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
        # an arrowhead near the end of each path
        (xa, ya), (xb, yb) = pts[-6], pts[-1]
        f.arrow(cx + S * xa, cy - S * ya, cx + S * xb, cy - S * yb, col, 3, 14)
    f.line(40, cy, 560, cy, RULE, 1.5, "6 5")
    f.circle(cx, cy, max(3, 7.3 / D_FM * S), HOT, INK, 1.5)
    f.tex(cx + 14, cy + 22, r"\text{nucleus}", "start", bg=True)
    # b for the 1.2 d path
    f.line(60, cy, 60, cy + S * 1.2, INK, 2)
    f.tex(52, cy + S * 0.6, "b", "end")
    # scale bar: 50 fm
    L = 50 / D_FM * S
    f.line(470, 40, 470 + L, 40, INK, 3)
    f.line(470, 32, 470, 48, INK, 2); f.line(470 + L, 32, 470 + L, 48, INK, 2)
    f.tex(470 + L / 2, 18, r"50\ \text{fm}", "middle")
    return f.svg()


def lines():
    """The visible lines of hydrogen on a wavelength scale, as seen through a grating."""
    f = Fig("fy14am-lines", 220, "The visible spectrum of hydrogen gas as seen through a grating, on a wavelength scale from 380 to "
            "720 nanometres. On a dark background there are only four thin bright lines: violet at 410 nanometres, blue at 434, "
            "turquoise at 486 and red at 656 nanometres. Between them there is no light.")
    X = lambda l: 40 + (l - 380) / (720 - 380) * 520
    f.rect(40, 30, 520, 90, "#15191e", INK, 2)
    for lam, col in BALMER:
        f.rect(X(lam) - 3, 30, 6, 90, col)
    for t in (400, 450, 500, 550, 600, 650, 700):
        f.line(X(t), 120, X(t), 130, INK, 2)
    for lam, col in BALMER:
        anchor, dx = {410.2: ("end", 6), 434.0: ("start", -6)}.get(lam, ("middle", 0))
        f.tex(X(lam) + dx, 154, rf"{lam:.0f}", anchor, color=INK)
    f.tex(560, 196, r"\lambda\ (\text{nm})", "end")
    return f.svg()


def levels():
    """Energy levels of hydrogen to scale, with the Balmer jumps and the first Lyman jump."""
    f = Fig("fy14am-levels", 560, "Energy-level diagram of the hydrogen atom, drawn to scale. Horizontal lines: n = 1 at minus 13.6 "
            "electronvolts at the bottom, n = 2 at minus 3.40, n = 3 at minus 1.51, n = 4 at minus 0.85, then n = 5 and n = 6 "
            "crowding just below zero, which is the energy of a free electron. Downward arrows show jumps to n = 2 from n = 3, 4, "
            "5 and 6, coloured red, turquoise, blue and violet, with the wavelengths 656, 486, 434 and 410 nanometres. A grey "
            "arrow from n = 2 to n = 1 gives ultraviolet light of 122 nanometres.")
    top, S = 50, 34.0                     # y of 0 eV, units per eV
    Y = lambda E: top - E * S
    x0, x1 = 120, 470
    f.line(x0, Y(0), x1, Y(0), MUTED, 2, "8 6")
    f.tex(x1 + 8, Y(0) - 10, r"0\ \text{eV}", "start")
    f.tex(x0 - 10, Y(0) - 10, r"n = \infty", "end")
    for k in range(1, 7):
        E = -13.6 / k ** 2
        f.line(x0, Y(E), x1, Y(E), INK, 3 if k < 5 else 2)
    for k, dy in ((1, 0), (2, 0), (3, 12), (4, -9)):
        E = -13.6 / k ** 2
        f.tex(x0 - 10, Y(E) + dy, rf"n = {k}", "end")
        f.tex(x1 + 8, Y(E) + dy, rf"{E:.2f}\ \text{{eV}}", "start")
    for (lam, col), k, x in zip(BALMER, (3, 4, 5, 6), (250, 310, 370, 430)):
        f.arrow(x, Y(-13.6 / k ** 2), x, Y(-3.4) - 1, col, 4, 16)
        f.tex(x, Y(-3.4) + 30, rf"{lam:.0f}", "middle", color=col)
    f.tex(340, Y(-3.4) + 62, r"\lambda\ \text{in nm}", "middle")
    f.arrow(160, Y(-3.4), 160, Y(-13.6) - 1, MUTED, 4, 16)
    f.tex(176, Y(-8.5), r"122\ \text{nm (UV)}", "start", color=INK)
    return f.svg()


FIGURES = {"hero": hero, "scatter": scatter, "lines": lines, "levels": levels}
