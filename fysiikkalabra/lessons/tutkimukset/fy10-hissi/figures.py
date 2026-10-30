"""Figures of the investigation Hissin kulkema matka kiihtyvyydestä (scripts/figlib.py); `python scripts/investigations.py
figures fy10-hissi` writes them into investigation.md. Velocity arrows are blue and acceleration arrows orange (teacher's
rule: force, velocity and acceleration always in different colours). The graphs show model shapes only, without numbers
and never invented measurements."""
from figlib import Fig, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, COLD, COLD_LIGHT, HOT, GOOD, n
import herolib as H
from herolib import grad

VEL, ACC = "#1971c2", "#e8590c"
CONCRETE, SHAFT, TAPE = "#b9c0c7", "#d5dde4", "#ffe8a3"


# ---------------------------------------------------------------- the model motion (shapes only)
T_END = 10.0
PHASES = (0.8, 2.6, 7.2, 9.0)          # start of speeding up, start of cruise, start of slowing down, stop


def _ramp(t, a, b):
    """0 before a, 1 after b, a smooth (cosine) step between: a real lift changes its acceleration gradually."""
    import math
    if t <= a: return 0.0
    if t >= b: return 1.0
    return 0.5 - 0.5 * math.cos(math.pi * (t - a) / (b - a))


def acc(t):
    """A lift going up from rest to rest: a smooth positive pulse, zero while cruising, an equal negative pulse."""
    t0, t1, t2, t3 = PHASES; r = 0.5
    up = _ramp(t, t0, t0 + r) - _ramp(t, t1 - r, t1)
    down = _ramp(t, t2, t2 + r) - _ramp(t, t3 - r, t3)
    return up - down


def integrate(fn, offset=0.0, steps=2000):
    """Trapezoid sums of fn(t) + offset from 0 to T_END: the lists (t, v) and (t, s), as the spreadsheet does."""
    dt = T_END / steps; ts = [k * dt for k in range(steps + 1)]
    a = [fn(t) + offset for t in ts]; v = [0.0]; s = [0.0]
    for k in range(1, len(ts)):
        v.append(v[-1] + (a[k - 1] + a[k]) / 2 * dt)
        s.append(s[-1] + (v[-2] + v[-1]) / 2 * dt)
    return ts, a, v, s


def panel(f, x0, x1, ytop, ybot, yzero, ylabel, tlabel=True):
    """Hand-made axes for a shape graph whose quantity may be negative: the time axis at the zero level, no numbers."""
    f.arrow(x0, ybot, x0, ytop - 18, INK, 2.5, 13)
    f.arrow(x0 - 1, yzero, x1 + 20, yzero, INK, 2.5, 13)
    f.tex(x0 + 12, ytop - 14, ylabel, "start")
    if tlabel: f.tex(x1 + 26, yzero, r"t", "start")


def curve(f, ts, ys, x0, x1, yzero, scale, color=INK, w=3, dash=None):
    step = max(1, len(ts) // 240)
    pts = " ".join(f"{n(x0 + t / T_END * (x1 - x0))},{n(yzero - y * scale)}" for t, y in list(zip(ts, ys))[::step] + [(ts[-1], ys[-1])])
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f.add(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}/>')


# ---------------------------------------------------------------- figures
def phone(f, x, y, w=34, h=7):
    """A phone lying flat on the floor, seen from the side."""
    f.rect(x - w / 2, y - h, w, h, INK, None, rx=2)
    f.rect(x - w / 2 + 3, y - h + 1.5, w - 6, 2, METAL_EDGE, None)


def hero():
    """The opening illustration: a cut-away of a four-storey school building. In the middle the lift shaft with the car
    between two floors, a student in the car and a phone lying on the car floor; the counterweight lower in the shaft.
    On the left a staircase rises through an opening in the slab from the second floor to the third; at its foot a second
    student measures the rise of one step with a ruler (steps x rise = floor-to-floor height, not the room height)."""
    f = H.hero("fy10h-hero", "Kuvitus: läpileikkaus nelikerroksisesta koulurakennuksesta. Keskellä on hissikuilu, jossa hissikori "
               "on kahden kerroksen välissä matkalla. Korissa seisoo opiskelija, ja korin lattialla on puhelin. Kuilussa kulkee "
               "kori köysissä, ja vastapaino on alempana kuilun reunalla. Vasemmalla portaat nousevat toisesta kerroksesta "
               "välipohjan aukon kautta kolmanteen kerrokseen. Portaiden alapäässä toinen opiskelija mittaa viivaimella yhden "
               "askelman nousua: askelmien määrä kertaa nousu on kerroskorkeus lattiasta seuraavan kerroksen lattiaan. Oikealla "
               "kerroksissa on ikkunat.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10hh-wall", GLASS, "#dfe9ef"))
    slabs = [568, 436, 304, 172, 40]                       # top of each floor slab, from the ground floor up
    sx0, sx1 = 480, 720                                    # the shaft
    f.rect(sx0, 0, sx1 - sx0, 600, SHAFT)
    for x in (sx0 + 26, sx1 - 26): f.line(x, 0, x, 600, METAL_EDGE, 3)          # guide rails
    hole = (150, 420)                                      # the stairwell opening in the third floor's slab
    for y in slabs:
        left = [(0, hole[0]), (hole[1], sx0)] if y == slabs[2] else [(0, sx0)]
        for a, b in left: f.rect(a, y, b - a, 16, CONCRETE, INK, 2.5)
        f.rect(sx1, y, 1200 - sx1, 16, CONCRETE, INK, 2.5)
    for y in slabs[:-1]:                                   # floors: a light floor strip and the landing doors
        left = [(0, hole[0]), (hole[1], sx0)] if y == slabs[2] else [(0, sx0)]
        for a, b in left: f.rect(a, y - 6, b - a, 6, SAND, None)
        f.rect(sx1, y - 6, 1200 - sx1, 6, SAND, None)
        f.rect(sx0 - 14, y - 96, 14, 96, ALUMINIUM, INK, 2)
    f.rect(sx0 - 3, 0, 3, 600, INK); f.rect(sx1, 0, 3, 600, INK)
    # the windows on the right
    for y in slabs[1:]:
        for x in (800, 990):
            f.rect(x, y + 16 + 26, 130, 62, grad(f, f"fy10hh-win{x}{y}", "#cfe8fb", WHITE), INK, 2.5, rx=3)
            f.line(x + 65, y + 42, x + 65, y + 104, INK, 2)
    # the machine and pulley at the top, the ropes, the car between floors 2 and 3, the counterweight lower down
    cx = 585; car_top, car_bot = 214, 356
    f.circle(640, 22, 14, IRON, INK, 2.5)
    f.line(cx, 24, cx, car_top, INK, 2.5); f.line(cx + 8, 24, cx + 8, car_top, INK, 2.5)
    f.line(cx + 6, 10, 640, 10, INK, 2.5)
    f.line(690, 22, 690, 420, INK, 2.5)
    f.rect(678, 420, 24, 110, IRON, INK, 2.5, rx=3)
    f.rect(508, car_top, 156, car_bot - car_top, "#eef2f5", INK, 3, rx=4)
    f.rect(508, car_bot - 12, 156, 12, ALUMINIUM, INK, 2.5)
    f.line(650, car_top + 54, 650, car_top + 82, METAL_EDGE, 3)                    # handrail
    H.person(f, 560, car_bot - 12, shirt=COLD, trousers=INK, sc=0.33)
    phone(f, 620, car_bot - 12)
    # the stairs from the second floor up through the opening to the third floor; at the foot a student measures the
    # rise of one step with a ruler: the number of steps times the rise is the floor-to-floor height
    yb, yt, xb, xt, steps = slabs[1] - 6, slabs[2] - 6, 170, hole[1], 12
    rise, run = (yb - yt) / steps, (xt - xb) / steps
    d = f"M{n(xb)},{n(yb)}" + "".join(f" v{n(-rise)} h{n(run)}" for _ in range(steps)) + f" L{n(xt)},{n(slabs[2] + 16)} L{n(xb + 30)},{n(yb)} Z"
    f.path(d, CONCRETE, INK, 2.5)
    f.rect(xb - 12, yb - 22, 8, 22, TAPE, INK, 1.5, rx=1)
    for k in range(5): f.line(xb - 12, yb - 4 - 4 * k, xb - 12 + (5 if k % 2 == 0 else 3), yb - 4 - 4 * k, INK, 1)
    H.walker(f, xb - 46, yb, GOOD, INK, 0.25, stride=0.4, hand=(xb - 12, yb - 18))
    # a plant and a bench on the ground floor, a desk on the top floor
    f.rect(120, slabs[0] - 6 - 36, 160, 10, SAND_DARK, INK, 2); f.line(136, slabs[0] - 32, 136, slabs[0] - 6, INK, 3); f.line(264, slabs[0] - 32, 264, slabs[0] - 6, INK, 3)
    f.rect(390, slabs[0] - 46, 30, 40, HOT, INK, 2, rx=4)
    for dx, dy in ((-12, -70), (2, -84), (16, -66)): f.circle(405 + dx, slabs[0] + dy, 16, GOOD)
    f.rect(140, slabs[3] - 50, 180, 10, SAND_DARK, INK, 2); f.line(154, slabs[3] - 40, 154, slabs[3] - 6, INK, 3); f.line(306, slabs[3] - 40, 306, slabs[3] - 6, INK, 3)
    f.rect(780, slabs[0] - 70, 60, 64, COLD_LIGHT, INK, 2, rx=4)
    return f.svg()


def vaiheet():
    """The phases of a trip upward: the car with a phone on its floor; velocity (blue) and acceleration (orange) arrows."""
    f = Fig("fy10h-vaiheet", 330, "Kaaviokuva hissin ylöspäin suuntautuvan matkan kolmesta vaiheesta. Kussakin vaiheessa on "
            "hissikori köysissä, ja korin lattialla on puhelin. Vasemmalla hissi lähtee liikkeelle: sininen nopeusnuoli v "
            "osoittaa ylöspäin ja oranssi kiihtyvyysnuoli a ylöspäin. Keskellä hissi liikkuu tasaisella nopeudella: nopeusnuoli "
            "osoittaa ylöspäin ja on pisin, ja kiihtyvyys on nolla. Oikealla hissi hidastuu: nopeusnuoli osoittaa yhä ylöspäin, "
            "mutta kiihtyvyysnuoli osoittaa alaspäin.")
    panels = [(105, r"\text{liikkeellelähtö}", 46, 50), (300, r"\text{tasainen nopeus}", 90, 0), (495, r"\text{hidastuminen}", 46, -50)]
    for x, title, vlen, alen in panels:
        f.tex(x, 22, title, "middle", MUTED, size=20)
        f.line(x, 44, x, 96, IRON, 2.5)
        f.rect(x - 40, 96, 80, 130, "#eef2f5", INK, 3, rx=4)
        f.rect(x - 40, 214, 80, 12, ALUMINIUM, INK, 2)
        phone(f, x, 214)
        # arrows beside the car: velocity left of it, acceleration right of it
        f.arrow(x - 54, 196, x - 54, 196 - vlen, VEL, 4, 14)
        f.tex(x - 60, 196 - vlen / 2 - 6, r"\overline{v}", "end", VEL)
        if alen:
            y0 = 160 if alen > 0 else 120
            f.arrow(x + 54, y0, x + 54, y0 - alen, ACC, 4, 14)
            f.tex(x + 60, y0 - alen / 2, r"\overline{a}", "start", ACC)
        else:
            f.tex(x, 250, r"a = 0", "middle", ACC)
    f.tex(300, 300, r"\text{hissi kulkee ylöspäin}", "middle", MUTED, size=20)
    return f.svg()


def malli():
    """The model shapes of a trip upward on one time axis: a(t) a positive and a negative pulse, v(t) a rounded
    trapezoid, s(t) curving up, straight, curving down to a constant. Shapes only: no numbers, no measured points."""
    f = Fig("fy10h-malli", 600, "Kolme mallikuvaajaa allekkain samalla aika-akselilla, ilman lukuarvoja ja mittauspisteitä. "
            "Ylimpänä kiihtyvyys a ajan funktiona: alussa ja lopussa nolla, liikkeellelähdössä positiivinen pyöristetty "
            "kumpu, tasaisen nopeuden aikana nolla ja hidastuessa yhtä suuri negatiivinen kuoppa. Keskellä nopeus v: nollasta "
            "kasvaa tasaiseen arvoon, pysyy vakiona ja pienenee takaisin nollaan. Alimpana kuljettu matka s: kasvaa ensin "
            "kiihtyen, sitten tasaisesti suorana ja lopuksi hidastuen, kunnes pysyy vakiona. Katkoviivat erottavat liikkeen "
            "vaiheet. Nopeuden muutos on kiihtyvyyskuvaajan pinta-ala, ja matka on nopeuskuvaajan pinta-ala.")
    ts, a, v, s = integrate(acc)
    x0, x1 = 90, 500
    rows = [(a, r"a", 40, 170, 105, 50), (v, r"v", 230, 380, 380, 0), (s, r"s", 430, 580, 580, 0)]
    vmax, smax = max(v), max(s)
    for t in PHASES:
        X = x0 + t / T_END * (x1 - x0)
        f.line(X, 30, X, 580, MUTED, 1.5, "5 5")
    for ys, lab, top, bot, zero, _ in rows:
        panel(f, x0, x1, top + 10, bot, zero, lab)
    curve(f, ts, a, x0, x1, 105, 50)
    curve(f, ts, v, x0, x1, 380, 125 / vmax)
    curve(f, ts, s, x0, x1, 580, 125 / smax)
    # the areas named where they apply
    f.add(f'<polygon points="{" ".join(f"{n(x0 + t / T_END * (x1 - x0))},{n(105 - y * 50)}" for t, y in zip(ts, a) if t <= PHASES[1] + 0.01)} {n(x0 + PHASES[1] / T_END * (x1 - x0))},105" fill="{ACC}" fill-opacity="0.18"/>')
    f.tex(x0 + 1.7 / T_END * (x1 - x0), 84, r"\Delta v", "middle", INK, size=20)
    f.add(f'<polygon points="{n(x0)},380 {" ".join(f"{n(x0 + t / T_END * (x1 - x0))},{n(380 - y * 125 / vmax)}" for t, y in list(zip(ts, v))[::10])} {n(x1)},380" fill="{VEL}" fill-opacity="0.12"/>')
    f.tex(x0 + 4.9 / T_END * (x1 - x0), 340, r"\text{pinta-ala} = s", "middle", INK, size=20)
    return f.svg()


def ryominta():
    """A small constant error in the acceleration: the velocity drifts linearly, the distance error grows with t^2."""
    f = Fig("fy10h-ryominta", 470, "Kaksi mallikuvaajaa allekkain, ilman lukuarvoja. Ylempänä nopeus v ajan funktiona: "
            "yhtenäinen viiva on laskettu oikeasta kiihtyvyydestä ja palaa lopussa nollaan. Katkoviiva on laskettu "
            "kiihtyvyydestä, jossa on pieni vakiovirhe: se kulkee aluksi lähes yhtenäisen viivan päällä, mutta erkanee siitä "
            "tasaisesti, eikä nopeus palaa lopussa nollaan. Jäljelle jäävä nopeus on merkitty v loppu. Alempana matka s: "
            "katkoviivan ja yhtenäisen viivan ero kasvaa yhä nopeammin ajan kuluessa.")
    err = 0.04
    ts, a, v, s = integrate(acc)
    _, _, ve, se = integrate(acc, err)
    x0, x1 = 90, 470
    vmax, smax = max(ve), max(se)
    panel(f, x0, x1, 40, 210, 210, r"v")
    panel(f, x0, x1, 260, 440, 440, r"s")
    curve(f, ts, v, x0, x1, 210, 150 / vmax)
    curve(f, ts, ve, x0, x1, 210, 150 / vmax, MUTED, 3, "8 6")
    curve(f, ts, s, x0, x1, 440, 160 / smax)
    curve(f, ts, se, x0, x1, 440, 160 / smax, MUTED, 3, "8 6")
    # the leftover velocity at the end
    ye = 210 - ve[-1] * 150 / vmax
    f.line(x1 + 4, ye, x1 + 4, 210, INK, 2); f.line(x1 - 4, ye, x1 + 12, ye, INK, 2)
    f.tex(x1 + 2, ye - 18, r"v_\text{loppu}", "middle")
    f.line(x0 + 20, 282, x0 + 58, 282, INK, 3); f.tex(x0 + 66, 282, r"\text{ilman virhettä}", "start", INK, size=20)
    f.line(x0 + 20, 312, x0 + 58, 312, MUTED, 3, "8 6"); f.tex(x0 + 66, 312, r"\text{nollakohdan virhe}", "start", MUTED, size=20)
    return f.svg()


FIGURES = {"hero": hero, "vaiheet": vaiheet, "malli": malli, "ryominta": ryominta}
