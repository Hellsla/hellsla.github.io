"""Figures of the investigation Tuulivoimalan tutkiminen (scripts/figlib.py); `python scripts/investigations.py figures
fy10-tuulivoimala` writes them into investigation.md. The only arrows of a physical quantity are the wind velocities
in the swept-area figure, in the velocity colour (#1971c2). The airflow in the hero is drawn as muted streaks without
arrowheads. No graph of measured or invented data is drawn."""
import math
from figlib import Fig, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN, COLD, GOOD_LIGHT, n
import herolib as H
from herolib import grad

VELOCITY = "#1971c2"
BLADE = WHITE


def blade_path(cx, cy, ang, L, root=6, chord=15, squash=1.0):
    """One blade in the rotor plane at angle ang (0 = up), drawn with the horizontal axis squashed (perspective)."""
    c, s = math.sin(ang), -math.cos(ang)            # unit vector along the blade
    px, py = -s, c                                 # across the blade
    def P(u, w):                                   # u along the blade, w across it
        return n(cx + (c * u + px * w) * squash), n(cy + s * u + py * w)
    pts = [P(8, root), P(L * 0.35, chord), P(L, chord * 0.45), P(L, -chord * 0.2), P(L * 0.35, -chord * 0.3), P(8, -root)]
    return "M" + " L".join(f"{x},{y}" for x, y in pts) + " Z"


def rotor(f, cx, cy, L, turn=0.0, squash=1.0, blades=3):
    for k in range(blades):
        f.path(blade_path(cx, cy, turn + k * 2 * math.pi / blades, L, squash=squash), BLADE, INK, 2)
    f.circle(cx, cy, 9, ALUMINIUM, INK, 2)


def multimeter(f, x, y, w=96, h=130):
    """A handheld multimeter standing on the desk: blank display, dial and two sockets."""
    f.rect(x, y, w, h, "#ffd43b", INK, 2.5, rx=10)
    f.rect(x + 10, y + 10, w - 20, h - 20, IRON, INK, 2, rx=6)
    f.rect(x + 18, y + 18, w - 36, 30, GOOD_LIGHT, INK, 2, rx=3)
    f.circle(x + w / 2, y + 80, 17, ALUMINIUM, INK, 2)
    f.line(x + w / 2, y + 80, x + w / 2 + 9, y + 68, INK, 3)
    f.circle(x + w / 2 - 18, y + h - 22, 5, INK); f.circle(x + w / 2 + 18, y + h - 22, 5, INK)
    return (x + w / 2 - 18, y + h - 22), (x + w / 2 + 18, y + h - 22)


def wire(f, pts, colour=INK, w=3):
    d = f"M{n(pts[0][0])},{n(pts[0][1])}" + "".join(f" Q{n(a)},{n(b)} {n(c)},{n(e)}" for (a, b), (c, e) in zip(pts[1::2], pts[2::2]))
    f.path(d, stroke=colour, w=w, extra='stroke-linecap="round"')


def hero():
    """The opening illustration: a fan at the left of a desk blows towards a model wind turbine (both seen at an angle,
    so the rotor plane faces the fan); wires from the turbine base run to a variable resistor and two multimeters; a
    tape lies between the fan and the turbine, a vane anemometer and a notebook lie on the desk."""
    f = H.hero("fy10t-hero", "Kuvitus: työpöydän vasemmassa reunassa on puhallin, joka puhaltaa kohti tuulivoimalan "
               "pienoismallia. Ilmavirtaa kuvaavat katkoviivat kulkevat puhaltimesta roottoriin. Voimalan juurelta lähtevät "
               "johdot kulkevat säädettävään vastukseen ja kahteen yleismittariin. Puhaltimen ja voimalan välissä pöydällä "
               "on mittanauha, ja pöydällä on myös käsikäyttöinen tuulimittari ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10th-wall", GLASS, "#dfe9ef"))
    f.rect(0, 430, 1200, 170, grad(f, "fy10th-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 452 + 24 * k, 1200, 448 + 24 * k, GRAIN, 1.5)
    f.line(0, 430, 1200, 430, INK, 3)

    # the fan: a foot, a pole, the motor housing behind the guard, the guard seen at an angle (facing right)
    fx, fy = 205, 225
    f.add(f'<ellipse cx="150" cy="438" rx="78" ry="14" fill="{IRON}" stroke="{INK}" stroke-width="2.5"/>')
    f.rect(140, 300, 20, 138, ALUMINIUM, INK, 2.5)
    f.rect(108, 190, 80, 72, IRON, INK, 2.5, rx=18)                  # motor housing
    f.rect(140, 255, 20, 50, IRON, INK, 2.5)
    for k, r in enumerate([128, 96, 64, 32]):
        f.add(f'<ellipse cx="{fx}" cy="{fy}" rx="{n(r * 0.36)}" ry="{r}" fill="{GLASS if k == 0 else "none"}" '
              f'stroke="{INK}" stroke-width="{2.5 if k == 0 else 1.5}"/>')
    for k in range(12):
        a = k * math.pi / 6
        f.line(fx, fy, fx + 128 * 0.36 * math.cos(a), fy + 128 * math.sin(a), INK, 1.2)
    f.circle(fx, fy, 12, IRON, INK, 2)

    # the airflow from the fan towards the rotor: muted streaks, no arrowheads (not a velocity vector)
    for k, y0 in enumerate([138, 182, 226, 270, 314]):
        y1 = 231 + (y0 - 226) * 1.05
        f.path(f"M{fx + 70},{y0} C{fx + 180},{y0 + 6 * (k - 2)} {520},{y1 - 4 * (k - 2)} {580},{n(y1)}",
               stroke=MUTED, w=2.5, extra='stroke-dasharray="14 12" stroke-linecap="round"')

    # the model turbine: base, tower, nacelle behind the rotor (to the right), rotor facing the fan
    tx, hub_y = 650, 231
    f.rect(600, 418, 110, 18, IRON, INK, 2.5, rx=4)
    f.path(f"M{tx + 4},{418} L{tx + 9},{hub_y + 6} H{tx + 19} L{tx + 24},{418} Z", WHITE, INK, 2.5)
    f.rect(tx + 4, hub_y - 13, 62, 26, WHITE, INK, 2.5, rx=10)          # nacelle
    rotor(f, tx - 6, hub_y, 112, turn=0.35, squash=0.42)
    f.path(f"M{tx - 6},{hub_y - 10} Q{tx - 24},{hub_y} {tx - 6},{hub_y + 10} Z", ALUMINIUM, INK, 2)   # nose cone

    # the circuit on the desk: wires from the base to a variable resistor and two multimeters
    rx0, ry0 = 860, 372
    f.rect(rx0, ry0, 150, 58, IRON, INK, 2.5, rx=6)                     # variable resistor (rheostat)
    f.rect(rx0 + 12, ry0 + 14, 126, 18, "#e8b27a", INK, 2, rx=4)        # the winding
    for k in range(14): f.line(rx0 + 18 + 9 * k, ry0 + 14, rx0 + 18 + 9 * k, ry0 + 32, "#a46a2a", 1.5)
    f.rect(rx0 + 52, ry0 - 16, 22, 28, ALUMINIUM, INK, 2, rx=3)          # slider
    f.line(rx0 + 10, ry0 - 6, rx0 + 140, ry0 - 6, INK, 3)
    f.circle(rx0 + 8, ry0 + 44, 5, INK)                               # end terminal of the winding
    f.circle(rx0 + 142, ry0 - 6, 5, INK)                              # terminal of the slider bar
    L, S = (rx0 + 8, ry0 + 44), (rx0 + 142, ry0 - 6)
    a1, a2 = multimeter(f, 740, 300)
    v1, v2 = multimeter(f, 1060, 300)
    wire(f, [(700, 428), (712, 470), a1])                             # generator -> ammeter
    wire(f, [a2, (820, 470), L])                                      # ammeter -> load
    wire(f, [S, (900, 520), (708, 432)], colour=MUTED)                # slider -> back to the generator
    wire(f, [v1, (1000, 480), L])                                     # voltmeter across the load
    wire(f, [v2, (1110, 470), S], colour=MUTED)
    # the tape between the fan and the turbine, an anemometer and a notebook
    f.rect(232, 470, 420, 26, "#ffe8a3", INK, 2.5, rx=3)
    for k in range(41): f.line(240 + 10 * k, 470, 240 + 10 * k, 470 + (14 if k % 5 == 0 else 8), INK, 1.5)
    f.add(f'<g transform="translate(450,550) rotate(-12)">'
          f'<rect x="-14" y="-6" width="96" height="26" rx="10" fill="{IRON}" stroke="{INK}" stroke-width="2.5"/>'
          f'<circle cx="-34" cy="7" r="30" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2.5"/>'
          f'<circle cx="-34" cy="7" r="7" fill="{INK}"/>'
          + "".join(f'<line x1="-34" y1="7" x2="{n(-34 + 26 * math.cos(a))}" y2="{n(7 + 26 * math.sin(a))}" stroke="{INK}" stroke-width="1.5"/>'
                    for a in [k * math.pi / 3 for k in range(6)])
          + "</g>")
    f.add('<g transform="translate(1000,540) rotate(-5)">'
          f'<rect x="-80" y="-34" width="200" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-64" y1="{-18 + 12 * k}" x2="104" y2="{-18 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def meter(f, x, y, letter, r=26):
    f.circle(x, y, r, WHITE, INK, 2.5)
    f.tex(x, y, rf"\text{{{letter}}}", "middle")


def circuit():
    """The measuring circuit: generator, ammeter in series, variable load resistor, voltmeter across the load."""
    f = Fig("fy10t-circuit", 290, "Kytkentäkaavio. Vasemmalla on generaattori G. Siitä lähtevässä yläjohtimessa on "
            "virtamittari A sarjassa, ja johdin jatkuu oikealle säädettävään kuormitusvastukseen, joka on piirretty "
            "suorakulmiona, jonka läpi kulkee vino nuoli. Jännitemittari V on kytketty kuormitusvastuksen rinnalle "
            "sen kumpaankin napaan. Alajohdin palaa vastukselta generaattorille. Yläjohtimeen on merkitty sähkövirta I "
            "ja jännitemittarin viereen jännite U.")
    L, R, T, B = 90, 390, 70, 250
    gy = (T + B) / 2
    # wires of the main loop
    f.line(L, T, L, gy - 32, INK, 2.5); f.line(L, gy + 32, L, B, INK, 2.5)
    f.line(L, T, 219, T, INK, 2.5); f.line(271, T, R, T, INK, 2.5)
    f.line(R, T, R, 120, INK, 2.5); f.line(R, 200, R, B, INK, 2.5); f.line(L, B, R, B, INK, 2.5)
    # generator
    f.circle(L, gy, 32, WHITE, INK, 2.5); f.tex(L, gy, r"\text{G}", "middle")
    # ammeter in series
    meter(f, 245, T, "A")
    f.arrow(120, T, 178, T, INK, 2.5, 13); f.tex(149, T - 24, r"I", "middle")
    # variable load resistor
    f.rect(R - 15, 120, 30, 80, WHITE, INK, 2.5)
    f.arrow(R - 34, 214, R + 34, 106, INK, 2, 13)
    # voltmeter across the load
    vx = 520
    f.line(R, 96, vx, 96, INK, 2.5); f.line(vx, 96, vx, 134, INK, 2.5)
    f.line(vx, 186, vx, 226, INK, 2.5); f.line(vx, 226, R, 226, INK, 2.5)
    f.circle(R, 96, 5, INK); f.circle(R, 226, 5, INK)
    meter(f, vx, 160, "V")
    f.tex(vx + 34, 160, r"U", "start")
    # labels
    f.tex(L + 42, gy + 42, r"\text{generaattori}", "start", MUTED)
    f.tex(R - 26, 140, r"\text{kuormitusvastus}", "end", MUTED)
    return f.svg()


def swept():
    """The swept area A = pi r^2 seen from the front, and the wind arriving at speed v seen from the side."""
    f = Fig("fy10t-swept", 340, "Kaaviokuva. Vasemmalla roottori edestä: kolmen lavan kärjet piirtävät pyöriessään "
            "katkoviivalla merkityn ympyrän. Ympyrän säde r on etäisyys navan keskeltä lavan kärkeen, ja ympyrän pinta-ala "
            "on roottorin pyyhkäisemä pinta-ala A, joka on pii kertaa r toiseen. Oikealla sama roottori sivulta: "
            "kolme sinistä nopeusnuolta v osoittaa vasemmalta kohti roottoria, kohtisuoraan roottorin tasoa vastaan.")
    cx, cy, r = 165, 160, 118
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{GLASS}" stroke="{MUTED}" stroke-width="2" stroke-dasharray="7 6"/>')
    rotor(f, cx, cy, r, turn=0.0)
    a = math.radians(60)
    ex, ey = cx + r * math.sin(a), cy - r * math.cos(a)
    f.line(cx, cy, ex, ey, INK, 2.5); f.circle(ex, ey, 4, INK)
    f.tex((cx + ex) / 2 + 14, (cy + ey) / 2 + 2, r"r", "start")
    f.tex(cx, cy + r + 32, r"A = \pi r^2", "middle")
    # side view: rotor edge-on, nacelle and a short tower stub
    sx = 480
    f.rect(sx - 4, cy - r, 8, 2 * r, WHITE, INK, 2)
    f.rect(sx + 2, cy - 12, 56, 24, WHITE, INK, 2, rx=8)
    f.path(f"M{sx - 2},{cy - 10} Q{sx - 20},{cy} {sx - 2},{cy + 10} Z", ALUMINIUM, INK, 2)
    f.path(f"M{sx + 22},{cy + 12} L{sx + 18},{cy + r + 40} H{sx + 38} L{sx + 34},{cy + 12} Z", WHITE, INK, 2)
    for y in (cy - 80, cy, cy + 80):
        f.arrow(sx - 150, y, sx - 26, y, VELOCITY, 4, 16)     # equal lengths: the same speed everywhere
    f.tex(sx - 100, cy - 104, r"\overline{v}", "middle", VELOCITY)
    return f.svg()


FIGURES = {"hero": hero, "circuit": circuit, "swept": swept}
