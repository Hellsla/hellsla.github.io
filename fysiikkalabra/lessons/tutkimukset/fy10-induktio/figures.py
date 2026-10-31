"""Figures of the investigation Sähkömagneettisen induktion tutkiminen (scripts/figlib.py); `python scripts/investigations.py
figures fy10-induktio` writes them into investigation.md. Velocity is blue (#1971c2, teacher's rule: force, velocity and
acceleration always in different colours); field lines are neutral grey. The pulse graph is a model computed from a point
dipole falling freely through a short coil, never an invented measurement."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_DARK, GRAIN, \
    HEAT_LIGHT, GOOD, GOOD_LIGHT, COLD, n
import herolib as H
from herolib import grad

VELOCITY = "#1971c2"
SCREEN = "#2b3138"


def coil_side(f, x0, x1, cy, ry, turns, w=3):
    """A coil seen from the side, axis horizontal: the back halves of the turns muted, the front halves copper."""
    step = (x1 - x0) / (turns - 1)
    for k in range(turns):
        x = x0 + k * step
        f.path(f"M{n(x)},{n(cy - ry)} A{n(ry * 0.16)},{n(ry)} 0 0 0 {n(x)},{n(cy + ry)}", stroke=METAL_EDGE, w=w - 1)
    for k in range(turns):
        x = x0 + k * step
        f.path(f"M{n(x)},{n(cy - ry)} A{n(ry * 0.16)},{n(ry)} 0 0 1 {n(x)},{n(cy + ry)}", stroke=COPPER, w=w)


def magnet(f, x, y, w, h, vertical=False):
    """A bar magnet: two halves in neutral greys (no pole letters, N would be confused with the number of turns)."""
    if vertical:
        f.rect(x, y, w, h / 2, IRON, INK, 2.5, rx=3); f.rect(x, y + h / 2, w, h / 2, ALUMINIUM, INK, 2.5, rx=3)
    else:
        f.rect(x, y, w / 2, h, IRON, INK, 2.5, rx=3); f.rect(x + w / 2, y, w / 2, h, ALUMINIUM, INK, 2.5, rx=3)


def bench_coil(f, x0, w, lines):
    """A coil lying on its side on a bobbin, axis horizontal, flanges at both ends; `lines` sets the winding density."""
    f.rect(x0, 330, 20, 140, IRON, INK, 2.5, rx=4); f.rect(x0 + w - 20, 330, 20, 140, IRON, INK, 2.5, rx=4)
    f.rect(x0 + 20, 345, w - 40, 110, COPPER, INK, 2.5)
    for k in range(1, lines):
        x = x0 + 20 + k * (w - 40) / lines
        f.line(x, 346, x - 3, 454, "#8f4a20", 1.2 if lines > 30 else 1.5)
    f.add(f'<ellipse cx="{n(x0 + 10)}" cy="400" rx="8" ry="22" fill="{INK}"/>')     # the dark opening of the core


def hero():
    """The opening illustration: a bench with two coils of the same size but different winding, a bar magnet and a
    cylinder magnet, a voltage sensor wired to one coil and to a laptop whose screen shows no graph, a ruler and a
    notebook. No method is shown."""
    f = H.hero("fy10i-hero", "Kuvitus: laboratorion työpöydällä on kaksi samankokoista käämiä, sauvamagneetti ja pieni "
               "lieriömagneetti. Toisen käämin päät on kytketty johtimilla jänniteanturiin, ja anturi on kytketty kannettavaan "
               "tietokoneeseen. Tietokoneen näyttö on tyhjä. Pöydällä on myös viivain ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10ih-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10ih-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # two coils of the same size, the second wound more densely
    bench_coil(f, 60, 220, 20)
    bench_coil(f, 320, 220, 40)
    # terminals of the second coil and leads to the sensor
    for x in (370, 490):
        f.rect(x - 8, 318, 16, 14, IRON, INK, 2, rx=2)
    f.path("M370,318 C380,250 600,250 640,330", stroke=IRON, w=4)
    f.path("M490,318 C500,270 620,270 660,330", stroke=INK, w=4)
    # the voltage sensor box
    f.rect(600, 330, 110, 70, "#e9ecef", INK, 2.5, rx=8)
    f.rect(616, 346, 78, 22, SCREEN, INK, 2, rx=3)
    f.circle(632, 384, 6, IRON, INK, 1.5); f.circle(678, 384, 6, INK, INK, 1.5)
    # cable to the laptop
    f.path("M710,365 C780,365 790,440 840,440", stroke=INK, w=4)
    # the laptop: keyboard base and an empty screen
    f.path("M820,470 L860,430 H1120 L1150,470 Z", "#ced4da", INK, 2.5)
    f.rect(860, 230, 260, 200, IRON, INK, 3, rx=8)
    f.rect(874, 244, 232, 172, "#f8f9fa", INK, 2, rx=4)
    f.rect(874, 244, 232, 20, ALUMINIUM, INK, 2, rx=4)
    # the bar magnet and a small cylinder magnet
    magnet(f, 610, 505, 110, 30)
    f.rect(740, 444, 26, 26, ALUMINIUM, INK, 2.5, rx=4)
    f.rect(740, 444, 26, 9, IRON, INK, 2.5, rx=3)
    # a ruler and a notebook on the desk front
    f.add(f'<g transform="translate(330,535) rotate(-3)"><rect x="-150" y="-14" width="300" height="28" rx="3" fill="#ffe8a3" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="{-140 + 14 * k}" y1="-14" x2="{-140 + 14 * k}" y2="{-4 if k % 5 else 2}" stroke="{INK}" stroke-width="1.5"/>' for k in range(21))
          + "</g>")
    f.add('<g transform="translate(980,530) rotate(5)">'
          f'<rect x="-90" y="-34" width="200" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-18 + 12 * k}" x2="94" y2="{-18 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def flux():
    """The principle: a bar magnet moving towards a coil; its field lines pass through the turns, and the number of them
    through the coil grows as the magnet comes closer. Velocity arrow blue; field lines grey."""
    f = Fig("fy10i-flux", 330, "Kaaviokuva. Vasemmalla on sauvamagneetti, joka liikkuu nopeudella v oikealle kohti käämiä. "
            "Magneetin ympärillä on harmaita kenttäviivoja, joista osa kulkee käämin kierrosten läpi. Käämissä on N kierrosta, "
            "ja sen päiden välille syntyy jännite U, jota mitataan.")
    cx, cy = 150, 165
    clip = 'clip-path="url(#fy10i-flux-clip)"'
    f.defs_add('<clipPath id="fy10i-flux-clip"><rect x="0" y="40" width="600" height="250"/></clipPath>')
    # a bar magnet as two opposite poles near its ends; field lines traced from the right pole (facing the coil)
    pr, pl = (cx + 55, cy), (cx - 55, cy)
    def field(x, y):
        bx = by = 0.0
        for (px, py), q in ((pr, 1.0), (pl, -1.0)):
            dx, dy = x - px, y - py; r3 = (dx * dx + dy * dy) ** 1.5
            bx += q * dx / r3; by += q * dy / r3
        return bx, by
    for deg in (8, 20, 36, 56, 80, 110, 145):
        for side in (1, -1):
            th = math.radians(deg)
            x, y = pr[0] + 8 * math.cos(th), pr[1] - side * 8 * math.sin(th)
            pts = [(x, y)]
            for _ in range(3000):
                bx, by = field(x, y); m = math.hypot(bx, by)
                x += 2 * bx / m; y += 2 * by / m
                pts.append((x, y))
                if math.hypot(x - pl[0], y - pl[1]) < 8 or not (-80 < x < 680 and -60 < y < 390): break
            f.path("M" + " L".join(f"{n(px)},{n(py)}" for px, py in pts), stroke=MUTED, w=1.6, extra=clip)
    magnet(f, cx - 70, cy - 20, 140, 40)
    coil_side(f, 360, 470, cy, 62, 9)
    # leads to the meter
    f.line(470, cy + 60, 470, 270, INK, 2); f.line(360, cy + 60, 360, 270, INK, 2)
    f.line(360, 270, 395, 270, INK, 2); f.line(435, 270, 470, 270, INK, 2)
    f.circle(415, 270, 20, WHITE, INK, 2); f.tex(415, 270, r"U", "middle")
    f.arrow(110, 105, 205, 105, VELOCITY, 4, 16); f.tex(214, 101, r"\overline{v}", "start", VELOCITY)
    f.tex(cx, 228, r"\text{magneetti}", "middle", MUTED, bg=True)
    f.tex(415, 82, r"\text{käämi, } N \text{ kierrosta}", "middle", MUTED, bg=True)
    return f.svg()


def setup():
    """One possible arrangement (mode O): a magnet dropped from rest down a vertical plastic tube through a coil, the drop
    height h from the magnet's centre to the coil's top edge, a soft pad below, the coil wired to a voltage sensor."""
    f = Fig("fy10i-setup", 470, "Kaaviokuva yhdestä mahdollisesta järjestelystä. Pystysuora muoviputki kulkee käämin läpi, ja "
            "putken alapään alla on pehmeä alusta. Magneetti on putken yläosassa levossa. Pudotuskorkeus h on mitattu magneetin "
            "keskikohdasta käämin yläreunaan. Käämin päät on kytketty jänniteanturiin, joka on yhteydessä tietokoneeseen.")
    tx = 200
    # soft pad and bench line
    f.line(60, 440, 560, 440, INK, 2.5)
    f.rect(tx - 60, 418, 120, 22, GOOD_LIGHT, INK, 2, rx=6)
    # the tube (transparent, drawn as two walls)
    f.rect(tx - 22, 40, 44, 360, "#eef5f9", METAL_EDGE, 2)
    # coil around the tube
    f.rect(tx - 46, 300, 92, 70, COPPER, INK, 2.5, rx=3)
    for k in range(1, 10): f.line(tx - 46, 300 + 7 * k, tx + 46, 300 + 7 * k, "#8f4a20", 1.5)
    # magnet inside the tube, at rest near the top
    magnet(f, tx - 15, 70, 30, 50, vertical=True)
    # drop height from the magnet's centre to the coil's top edge
    f.line(tx + 22, 95, 300, 95, MUTED, 1.5, "6 5"); f.line(tx + 46, 300, 300, 300, MUTED, 1.5, "6 5")
    f.line(290, 95, 290, 300, INK, 2); f.line(280, 95, 300, 95, INK, 2); f.line(280, 300, 300, 300, INK, 2)
    f.tex(302, 197, r"h", "start")
    # leads to the sensor
    f.path(f"M{tx + 46},325 C330,325 360,360 420,360", stroke=INK, w=2.5)
    f.path(f"M{tx + 46},350 C320,350 350,385 420,385", stroke=INK, w=2.5)
    f.rect(420, 340, 120, 64, "#e9ecef", INK, 2.5, rx=8)
    f.tex(480, 312, r"\text{jänniteanturi}", "middle", MUTED)
    f.tex(tx - 56, 335, r"\text{käämi}", "end", MUTED)
    f.tex(tx - 30, 95, r"\text{magneetti}", "end", MUTED)
    f.tex(tx - 30, 220, r"\text{putki}", "end", MUTED)
    return f.svg()


def _pulse_model():
    """Induced voltage of a point dipole falling freely along the axis of a short coil, arbitrary units.
    Flux linkage of a coil of length L, radius a, centred at z = 0, dipole at z: proportional to
    [u / sqrt(1 + u^2)] between u = (z - L/2)/a and u = (z + L/2)/a. e = -dLambda/dt."""
    a, L, g = 1.0, 1.4, 1.0
    def lam(z):
        u1, u2 = (z - L / 2) / a, (z + L / 2) / a
        return u2 / math.sqrt(1 + u2 * u2) - u1 / math.sqrt(1 + u1 * u1)
    z0, v0 = 7.0, 2.6        # starts above the coil already moving (fell from higher up)
    ts = [i * 0.004 for i in range(1500)]
    out = []
    for t in ts:
        z = z0 - v0 * t - g * t * t / 2
        if z < -7: break
        v = v0 + g * t
        dz = 1e-4
        dl = (lam(z + dz) - lam(z - dz)) / (2 * dz)
        out.append((t, -dl * v))          # the sign depends on how the coil is connected: the entry pulse drawn positive
    return out


def pulse():
    """The model pulse: the voltage rises to a peak as the magnet enters, changes sign as it leaves; the exit pulse is
    taller and narrower because the magnet is faster. The peak U_max and the area S of the first pulse are marked."""
    data = _pulse_model()
    peak = max(data, key=lambda p: p[1])
    low = min(data, key=lambda p: p[1])
    s = 1.0 / max(peak[1], -low[1])
    t0, t1 = data[0][0], data[-1][0]
    f = Fig("fy10i-pulse", 360, "Mallikuvaaja: indusoitunut jännite U ajan t funktiona, kun magneetti putoaa käämin läpi. "
            "Ensin jännite kasvaa huippuarvoon U max ja palaa nollaan, kun magneetti tulee käämiin. Sitten jännite vaihtaa "
            "merkkiä, kun magneetti lähtee käämistä, ja tämä toinen pulssi on korkeampi ja kapeampi. Ensimmäisen pulssin ja "
            "aika-akselin väliin jäävä pinta-ala on merkitty kirjaimella S. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 200), (470, 70), x=(0, 1.0), y=(0, 1.0), xticks=[], yticks=[], xlabel=r"t", ylabel=r"U", grid=False,
              origin_label=False)
    f.line(90, 200, 90, 340, INK, 2.5)       # the voltage axis continues below the time axis
    # extend the plot below the axis: the time axis is in the middle, negative voltages below it
    def X(t): return ax.X((t - t0) / (t1 - t0))
    def Y(u): return ax.Y(u * s * 0.92)
    zero = next(i for i, p in enumerate(data) if p[0] > peak[0] and p[1] <= 0)
    first = [(X(t), Y(u)) for t, u in data[:zero + 1]]
    f.add('<polygon points="' + " ".join(f"{n(x)},{n(y)}" for x, y in first) + f' {n(first[-1][0])},{n(Y(0))} {n(first[0][0])},{n(Y(0))}" '
          f'fill="{GOOD}" fill-opacity="0.25"/>')
    f.add('<polyline points="' + " ".join(f"{n(X(t))},{n(Y(u))}" for t, u in data) + f'" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    px, py = X(peak[0]), Y(peak[1])
    f.line(90, py, px, py, MUTED, 1.5, "6 5")
    f.tex(84, py, r"U_\text{max}", "end")
    sx = (first[0][0] + first[-1][0]) / 2
    f.tex(sx - 6, Y(peak[1] * 0.35), r"S", "middle", GOOD)
    f.tex(X(low[0]) + 24, Y(low[1]) + 2, r"\text{toinen pulssi}", "start", MUTED)
    f.tex(px + 26, py - 2, r"\text{ensimmäinen pulssi}", "start", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "flux": flux, "setup": setup, "pulse": pulse}
