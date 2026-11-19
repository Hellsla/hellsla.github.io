"""figlib animation primitives (work queue 8f): the still is the drawing without animation, every cycle starts and ends
where the group is drawn, and the motion is the physics it claims (closed bouncing paths, momentum, projection).

  python scripts/test_figanim.py"""
import math, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from figlib import Fig, bounce_speed, drift_track, collision_frames

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

def near(a, b, tol=1e-6): return abs(a - b) <= tol

def frames_of(svg, i=0):
    m = re.findall(r"@keyframes [^{]+\{((?:[^{}]|\{[^{}]*\})*)\}", svg)[i]
    return [(float(p), tuple(float(v) for v in re.findall(r"-?\d+\.?\d*(?=px|deg)", body)), float(re.search(r"opacity:([\d.]+)", body).group(1)))
            for p, body in re.findall(r"([\d.]+)%\{([^}]*)\}", m)]

def draw(anim, kind):
    f = Fig("t", 200, "testi", anim=anim)
    if anim:
        {"osc": lambda: f.oscillate(10, 0.3, 2, "y"), "trav": lambda: f.travel(100, 3, clip=(0, 0, 100, 50)),
         "orbit": lambda: f.orbit(100, 100, 4), "drift": lambda: f.drift(50, 50, (0, 0, 200, 100), bounce_speed(200, 5, 2, 5), bounce_speed(100, 5, 3, 5), 5, 5)}[kind]()
    f.circle(50, 50, 5)
    if anim: f.end()
    return f.svg()

def strip(svg):
    svg = re.sub(r"<defs>.*?</defs>\n  ", "", svg, flags=re.S)
    svg = re.sub(r'<g class="fa-k"[^>]*>|<g clip-path="[^"]*">|</g>', "", svg)
    return re.sub(r"\n\s*\n", "\n", svg.replace(' class="fig-anim"', ""))

# the still: the same drawing without animation
for kind in ("osc", "trav", "orbit", "drift"):
    check(f"{kind}: the still is the plain drawing", strip(draw(True, kind)) == re.sub(r"\n\s*\n", "\n", draw(False, kind)), strip(draw(True, kind))[:200])
check("no animation without anim=True", "fa-k" not in draw(False, "osc"))
try: Fig("x", 10, "t").oscillate(1); check("a primitive needs anim=True", False)
except AssertionError: check("a primitive needs anim=True", True)

# every cycle starts and ends where the group is drawn
for kind in ("osc", "trav" if False else "orbit", "drift"):
    fr = frames_of(draw(True, kind))
    check(f"{kind}: starts at 0", fr[0][0] == 0 and all(near(v, 0) for v in fr[0][1]), fr[0])
    check(f"{kind}: ends where it began", fr[-1][0] == 100 and all(near(v, 0, 1e-3) for v in fr[-1][1][:2]) and (kind != "orbit" or near(abs(fr[-1][1][-1]), 360)), fr[-1])
check("an orbit turns a whole turn counter-clockwise", frames_of(draw(True, "orbit"))[-1][1][-1] == -360)

# oscillate: a sine with the phase, zero at the drawn position
f = Fig("o", 10, "t", anim=True); f.oscillate(8, 0.25, 2, "x", samples=24); f.end()
fr = frames_of(f.svg())
check("oscillate: amplitude 8 about a centre 8 away from where it is drawn", near(min(v[1][0] for v in fr), -16, 1e-2) and near(max(v[1][0] for v in fr), 0, 1e-2), (min(v[1][0] for v in fr), max(v[1][0] for v in fr)))

# the projection of the orbit is the orbit's own x or y at every time
for axis in ("x", "y"):
    for cw in (False, True):
        for th in (0, 40, 130, 250):
            R = 30; f = Fig("p", 10, "t", anim=True); f.project(R, th, 4, axis, cw); f.end()
            fr = frames_of(f.svg()); worst = 0
            for t, (dx, dy), _ in fr:
                ang = math.radians(th) + (-1 if cw else 1) * 2 * math.pi * t / 100
                true = (R * math.cos(ang) - R * math.cos(math.radians(th))) if axis == "x" else (-R * math.sin(ang) + R * math.sin(math.radians(th)))
                worst = max(worst, abs((dx if axis == "x" else dy) - true))
            check(f"project {axis} cw={cw} θ0={th}: follows the orbit point", worst < 0.2, worst)

# drift: inside the room, every wall hit reverses one velocity component, closed path, constant speed between hits
box, r, T = (20, 40, 300, 180), 6, 8.0
for kx, ky in ((1, 1), (2, 3), (-3, 2), (4, 0)):
    vx, vy = bounce_speed(box[2] - box[0], T, kx, r), bounce_speed(box[3] - box[1], T, ky, r)
    x0, y0 = 100, 90
    fr = drift_track(x0, y0, box, vx, vy, T, r)
    inside = all(box[0] + r - 1e-6 <= x0 + dx <= box[2] - r + 1e-6 and box[1] + r - 1e-6 <= y0 + dy <= box[3] - r + 1e-6 for _, dx, dy in fr)
    check(f"drift {kx},{ky}: stays in the box", inside)
    check(f"drift {kx},{ky}: closed", near(fr[-1][1], 0, 1e-6) and near(fr[-1][2], 0, 1e-6) and fr[0][0] == 0 and fr[-1][0] == 1, fr[-1])
    speeds = []
    for (t0, a0, b0), (t1, a1, b1) in zip(fr, fr[1:]):
        dt = (t1 - t0) * T
        speeds.append(((a1 - a0) / dt, (b1 - b0) / dt))
    check(f"drift {kx},{ky}: speed components are ±v between hits", all(near(abs(sx), abs(vx), 1e-2) and near(abs(sy), abs(vy), 1e-2) for sx, sy in speeds), speeds[:3])
    check(f"drift {kx},{ky}: the speed is constant (elastic walls)", len({round(math.hypot(*s), 2) for s in speeds}) == 1)
try: drift_track(50, 50, box, 37.3, 12.1, T, r); check("a path that does not close is refused", False)
except ValueError: check("a path that does not close is refused", True)

# collision: momentum conserved, energy conserved when elastic and lost when not, the bodies do not pass through each other
for m1, m2, v1, v2, e in ((1, 1, 60, 0, 1), (2, 1, 50, -20, 1), (1, 3, 40, 0, 0), (1, 2, 40, 10, 0.5)):
    f1, f2, info = collision_frames(100, 300, 40, 40, v1, v2, m1, m2, e)
    check(f"collide {m1},{m2},{v1},{v2},e={e}: momentum conserved", near(m1 * v1 + m2 * v2, m1 * info["u1"] + m2 * info["u2"], 1e-9))
    k0, k1 = m1 * v1 ** 2 + m2 * v2 ** 2, m1 * info["u1"] ** 2 + m2 * info["u2"] ** 2
    check(f"collide {m1},{m2},{v1},{v2},e={e}: energy {'kept' if e == 1 else 'lost'}", near(k0, k1, 1e-6) if e == 1 else k1 < k0)
    if e == 0: check("collide: sticking bodies leave together", near(info["u1"], info["u2"]))
    check(f"collide {m1},{m2}: separation along the run is never negative", all((100 + a[1] + 20) <= (300 + b[1] - 20) + 1e-6 for a, b in zip(f1[:3], f2[:3])), (f1, f2))
    check(f"collide {m1},{m2}: loops from the drawn position", f1[0][1:] == (0, 0, 0, 1) and f1[-1][1:] == (0, 0, 0, 1))

# travel: a window and its clip path; a pulse drawn mid-way starts that far into its run
f = Fig("w", 100, "t", anim=True); f.travel(80, 2, start=0.25, clip=(0, 0, 80, 40)); f.end()
svg = f.svg()
check("travel: clipped, the clipPath in defs", 'clip-path="url(#fa-w-0-clip)"' in svg and '<clipPath id="fa-w-0-clip">' in svg)
check("travel: starts into its run (negative delay)", "--fa-d:-0.5s" in svg, svg[:400])
check("travel: groups are balanced", svg.count("<g") == svg.count("</g>"))

print("\nFAIL" if fails else "\nall ok"); sys.exit(1 if fails else 0)
