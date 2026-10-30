"""Figures of the investigation Hypyn tutkiminen voimalevyllä (scripts/figlib.py); `python scripts/investigations.py
figures fy10-hyppy` writes them into investigation.md. Forces are red and acceleration orange (fbd.py, teacher's rule:
force, velocity and acceleration always in different colours). The force–time graph is a model shape only: no
numbers, no measured or invented data points."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, \
    COLD, COLD_LIGHT, HEAT_LIGHT, n
from fbd import FBD, ground
import herolib as H
from herolib import grad


# --- the model shape of the force–time curve, N/G against t (time unit 1 s, g cancels: see model()) -----------------

def _s(x):
    """A smooth step from 0 to 1 on 0..1."""
    x = min(max(x, 0.0), 1.0)
    return (1 - math.cos(math.pi * x)) / 2


T_DIP, T_LOW, T_PEAK, T_HOLD, T_OFF = 0.30, 0.45, 0.66, 0.84, 1.04   # movement starts, deepest unweighting, push peak, take-off


def _push(t):
    """N/G from quiet standing to take-off: rest (1), unweighting (below 1), braking and push (above 1), take-off (0)."""
    if t < T_DIP: return 1.0
    if t < T_LOW: return 1 - 0.6 * _s((t - T_DIP) / (T_LOW - T_DIP))
    if t < T_PEAK: return 0.4 + 2.0 * _s((t - T_LOW) / (T_PEAK - T_LOW))
    if t < T_HOLD: return 2.4 - 0.25 * _s((t - T_PEAK) / (T_HOLD - T_PEAK))
    if t < T_OFF: return 2.15 * (1 - _s((t - T_HOLD) / (T_OFF - T_HOLD)))
    return 0.0


def _area(fn, a, b, steps=4000):
    h = (b - a) / steps
    return sum(fn(a + (k + 0.5) * h) for k in range(steps)) * h


# impulse principle in units of G: the net area (N/G - 1) from rest to take-off is v0/g; the flight lasts 2 v0/g
NET = _area(lambda t: _push(t) - 1, 0, T_OFF)
T_LAND = T_OFF + 2 * NET
T_CROSS = next(k / 1000 for k in range(int(T_LOW * 1000), 2000) if _push(k / 1000) >= 1)   # N back up to G
LAND_RISE, LAND_FALL, SETTLE = 0.05, 0.16, 0.20


def _land_shape(t):
    """N/G after touch-down before scaling: a sharp rise, a fall below 1 and a settle back to 1."""
    u = t - T_LAND
    if u < 0: return 0.0
    if u < LAND_RISE: return _s(u / LAND_RISE)
    if u < LAND_RISE + LAND_FALL: return 1 - _s((u - LAND_RISE) / LAND_FALL)
    return 0.0


# after touch-down the force rises steeply, falls below G and settles back to G; the landing peak is scaled so that
# its net impulse stops the jumper: the same momentum change as at take-off, NET in units of G
_END = T_LAND + LAND_RISE + LAND_FALL + SETTLE


def _base(t):
    """The level under the landing peak: from 0 at touch-down to 0.6 G, then back to G."""
    u = t - T_LAND
    if u < 0: return 0.0
    if u < LAND_RISE + LAND_FALL: return 0.6 * _s(u / (LAND_RISE + LAND_FALL))
    return 0.6 + 0.4 * _s((u - LAND_RISE - LAND_FALL) / SETTLE)


PEAK = (NET + (_END - T_LAND) - _area(_base, T_LAND, _END)) / _area(_land_shape, T_LAND, _END)


def curve(t):
    """N/G at time t: the whole model jump."""
    if t < T_OFF: return _push(t)
    if t < T_LAND: return 0.0
    return PEAK * _land_shape(t) + _base(t)


# --- figures ---------------------------------------------------------------------------------------------------------

def jumper(f, x, yfeet, shirt=COLD, trousers=INK, sc=1.0):
    """herolib.person with the hands on the hips (the O procedure: no arm swing), elbows out."""
    s = sc
    f.path(f"M{n(x - 26 * s)},{n(yfeet)} L{n(x - 20 * s)},{n(yfeet - 150 * s)} H{n(x + 20 * s)} L{n(x + 26 * s)},{n(yfeet)} H{n(x + 6 * s)} L{n(x)},{n(yfeet - 100 * s)} L{n(x - 6 * s)},{n(yfeet)} Z", trousers)
    for sgn in (-1, 1):
        f.path(f"M{n(x + sgn * 28 * s)},{n(yfeet - 236 * s)} L{n(x + sgn * 66 * s)},{n(yfeet - 196 * s)} L{n(x + sgn * 34 * s)},{n(yfeet - 154 * s)}",
               stroke=shirt, w=22 * s, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{n(x - 34 * s)},{n(yfeet - 140 * s)} Q{n(x - 38 * s)},{n(yfeet - 250 * s)} {n(x)},{n(yfeet - 256 * s)} Q{n(x + 38 * s)},{n(yfeet - 250 * s)} {n(x + 34 * s)},{n(yfeet - 140 * s)} Z", shirt)
    for sgn in (-1, 1): f.circle(x + sgn * 32 * s, yfeet - 154 * s, 11 * s, SAND_LIGHT)
    f.rect(x - 9 * s, yfeet - 276 * s, 18 * s, 24 * s, SAND_LIGHT)
    f.circle(x, yfeet - 296 * s, 30 * s, SAND_LIGHT)
    f.path(f"M{n(x - 31 * s)},{n(yfeet - 296 * s)} Q{n(x - 30 * s)},{n(yfeet - 332 * s)} {n(x)},{n(yfeet - 330 * s)} Q{n(x + 32 * s)},{n(yfeet - 330 * s)} {n(x + 31 * s)},{n(yfeet - 300 * s)} Q{n(x + 6 * s)},{n(yfeet - 312 * s)} {n(x - 31 * s)},{n(yfeet - 296 * s)} Z", INK)


def hero():
    """The opening illustration: a student in mid-air above a force plate, hands on the hips, the plate wired to a laptop that
    shows empty axes: the curve is what the students predict in Ennusta."""
    f = H.hero("fy10h-hero", "Kuvitus: opiskelija on hypännyt suoraan ylös voimalevyn päältä ja on ilmassa kädet "
               "lanteilla. Hänen varjonsa näkyy levyllä. Voimalevystä kulkee johto pöydällä olevaan tietokoneeseen, "
               "jonka näytöllä on tyhjä koordinaatisto, johon mittaus piirtyy.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10hh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 490, 1200, 110, grad(f, "fy10hh-floor", SAND_DARK, SAND, horizontal=True))
    for k in range(4): f.line(0, 512 + 24 * k, 1200, 508 + 24 * k, GRAIN, 1.5)
    f.line(0, 490, 1200, 490, INK, 3)
    # the force plate on the floor and the jumper's shadow on it
    f.rect(330, 466, 300, 24, ALUMINIUM, INK, 2.5, rx=4)
    f.rect(342, 472, 276, 6, METAL_EDGE, None, rx=2)
    f.add(f'<ellipse cx="480" cy="465" rx="62" ry="7" fill="{INK}" fill-opacity="0.18"/>')
    # the jumper in mid-air, feet clearly above the plate
    jumper(f, 480, 400, sc=1.05)
    # a few faint speed lines below the feet: moving up
    for dx, L in ((-28, 34), (0, 46), (28, 34)):
        f.path(f"M{480 + dx},{414} v{L}", stroke=MUTED, w=2.5, extra='stroke-linecap="round" stroke-opacity="0.5"')
    # the cable from the plate to the laptop on a table
    f.path("M630,480 C700,480 720,470 760,470 S820,420 870,404", stroke=INK, w=3)
    f.rect(840, 400, 300, 14, IRON, INK, 2.5, rx=3)                       # table top
    f.line(860, 414, 860, 490, INK, 5); f.line(1120, 414, 1120, 490, INK, 5)
    f.path("M900,400 L1080,400 L1092,392 L888,392 Z", ALUMINIUM, INK, 2.5)  # keyboard base
    f.rect(906, 272, 168, 116, IRON, INK, 2.5, rx=6)
    f.rect(916, 282, 148, 96, WHITE, None, rx=2)
    # the screen: empty axes, the measurement is still to come (the students predict the curve themselves)
    f.line(926, 368, 1056, 368, INK, 2); f.line(926, 368, 926, 290, INK, 2)
    f.path("M1056,368 l-8,-4 v8 Z", INK); f.path("M926,290 l-4,8 h8 Z", INK)
    return f.svg()


def forces():
    """Force diagrams of the jumper as a rectangle: at rest N = G; during the push N > G and the acceleration is up."""
    f = Fig("fy10h-forces", 340, "Kaksi voimakuviota, hyppääjä suorakulmiona. Vasemmalla hyppääjä seisoo levossa "
            "voimalevyllä: paino G osoittaa keskipisteestä alas ja levyn tukivoima N alapinnasta ylös, ja nuolet ovat "
            "yhtä pitkät. Oikealla hyppääjä ponnistaa: tukivoima N on pidempi kuin paino G, ja hyppääjän vieressä "
            "oleva oranssi nuoli a näyttää kiihtyvyyden ylöspäin.")
    S = 0.75
    for cx, title, Nmag, a_dir in ((160, r"\text{levossa}", 100, (0, 0)), (440, r"\text{ponnistuksen aikana}", 180, (0, 1))):
        cy, w, h = 190, 70, 160
        bottom = cy + h / 2
        f.rect(cx - 100, bottom, 200, 12, ALUMINIUM, INK, 2.5, rx=3)             # the force plate
        f.tex(cx, 26, title, "middle", MUTED)
        d = FBD(f, S, body=(cx, cy, w, h), a_dir=a_dir)
        d.force("G", (0, -100), (cx, cy), "gravity", lab=(-24, -10))
        d.force("N", (0, Nmag), (cx + 22, bottom), "normal", surface=0, lab=(30, 12))
        d.draw()
        if a_dir != (0, 0): d.motion(r"\overline{a}", (0, 1), (cx + 80, cy + 30), 64, lab=(18, 8))
    # the two diagrams apart
    f.line(300, 14, 300, 326, MUTED, 1.5, "6 6")
    return f.svg()


def model():
    """The model force–time curve of a countermovement jump, N against t: the G level, the areas below and above G
    before take-off, the flight time and numbered phases. No numbers and no data points."""
    f = Fig("fy10h-model", 420, "Kuvaaja: voimalevyn tukivoima N ajan t funktiona mallin mukaan, ilman lukuarvoja. "
            "Vaakasuora katkoviiva on paino G. Kuvaajaan on merkitty numeroin kuusi vaihetta: 1 tasainen osa painon "
            "kohdalla, 2 notko painon alapuolella, 3 korkea huippu painon yläpuolella, joka laskee nollaan, 4 nollaosa, "
            "5 jyrkkä ja korkea huippu sekä 6 paluu painon tasolle. Ennen irtoamista painon alapuolelle jäävä alue on "
            "merkitty miinusmerkillä ja yläpuolelle jäävä alue plusmerkillä. Nollaosan pituus on merkitty t lento. "
            "Kuvaajassa ei ole mittauspisteitä.")
    tmax = _END + 0.12
    ax = Axes(f, (70, 360), (480, 60), x=(0, tmax), y=(0, PEAK * 1.08), xticks=[], yticks=[], xlabel=r"t",
              ylabel=r"N", grid=False)
    up = [(t, curve(t)) for t in [T_DIP + (T_OFF - T_DIP) * k / 300 for k in range(301)]]
    ax.area([(T_DIP, 1)] + [(t, min(v, 1)) for t, v in up if t <= T_CROSS] + [(T_CROSS, 1)], COLD_LIGHT, 0.8)
    ax.area([(T_CROSS, 1)] + [(t, max(v, 1)) for t, v in up if t >= T_CROSS] + [(T_OFF, 1)], HEAT_LIGHT, 0.8)
    f.line(ax.X(0), ax.Y(1), ax.X(tmax), ax.Y(1), MUTED, 2, "6 5")
    f.tex(ax.X(0) - 10, ax.Y(1), r"G", "end", MUTED)
    ax.curve(curve, 0, tmax, INK, 3, steps=600)
    # the signs of the areas
    f.tex(ax.X((T_DIP + T_CROSS) / 2), ax.Y(0.8), r"\boldsymbol{-}", "middle", size=32)
    f.tex(ax.X((T_PEAK + T_HOLD) / 2), ax.Y(1.5), r"\boldsymbol{+}", "middle", size=32)
    # flight time between take-off and touch-down
    yb = ax.Y(0) + 20                                   # the flight time under the time axis
    f.line(ax.X(T_OFF), yb, ax.X(T_LAND), yb, INK, 2)
    for t in (T_OFF, T_LAND): f.line(ax.X(t), yb - 8, ax.X(t), yb + 8, INK, 2)
    f.tex((ax.X(T_OFF) + ax.X(T_LAND)) / 2, yb + 24, r"t_\text{lento}", "middle")
    # the numbered phases
    marks = [(T_DIP / 2, 1.45, 1), (T_DIP - 0.08, 0.5, 2), (T_PEAK - 0.08, 2.75, 3), ((T_OFF + T_LAND) / 2, 0.45, 4),
             (T_LAND + LAND_RISE + 0.09, PEAK * 0.9, 5), (_END + 0.05, 1.45, 6)]
    for t, v, k in marks:
        x, y = ax.X(t), ax.Y(v)
        f.circle(x, y, 13, WHITE, INK, 2)
        f.tex(x, y, rf"\text{{{k}}}", "middle", size=18)
    return f.svg()


FIGURES = {"hero": hero, "forces": forces, "model": model}
