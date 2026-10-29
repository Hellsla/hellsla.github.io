"""fbd.py: a force diagram that breaks an assessed rule is refused; a right one draws (docs/force-diagrams.md).

  python scripts/test_fbd.py"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from figlib import Fig
from fbd import FBD, FORCE, VELOCITY, ACCEL, NET

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

def problems(build, **kw):
    d = FBD(Fig("t", 300, "test"), 1, body=(0, 0, 40, 40), **kw); build(d); return d.check()

mg = 10 * 9.81
rest = lambda d: d.force("G", (0, -mg), (0, 0), "gravity").force("N", (0, mg), (0, 0), "normal", surface=0)
check("a box at rest on a floor: weight down, normal force up, equal", problems(rest, a_dir=(0, 0)) == [], problems(rest, a_dir=(0, 0)))
check("…and with m and a = 0", problems(rest, m=10, a=(0, 0)) == [])
check("unequal weight and normal force at rest is refused",
      problems(lambda d: d.force("G", (0, -mg), (0, 0), "gravity").force("N", (0, 80), (0, 0), "normal", surface=0), a_dir=(0, 0)) != [])
check("two forces with one symbol are refused",
      any("symbol" in p for p in problems(lambda d: d.force("F", (5, 0), (0, 0), "applied").force("F", (-5, 0), (0, 0), "applied"))))
check("weight not vertical is refused", problems(lambda d: d.force("G", (10, -mg), (0, 0), "gravity")) != [])
# the helium balloon under the ceiling (YTL K2025 4.1): the ceiling pushes it DOWN
ball = lambda d: (d.force("G", (0, -0.03), (0, 0), "gravity").force("F_noste", (0, 0.051), (0, 0), "buoyancy")
                  .force("N", (0, -0.021), (0, 0), "normal", surface=0, outward=(0, -1)))
check("a balloon under a ceiling: the normal force points down, net zero", problems(ball, a_dir=(0, 0)) == [], problems(ball, a_dir=(0, 0)))
check("a ceiling's normal force pointing up is refused",
      any("away from the surface" in p for p in problems(lambda d: d.force("N", (0, 0.02), (0, 0), "normal", surface=0, outward=(0, -1)))))
# incline 30°: normal force perpendicular, friction along, components the projections
th = math.radians(30); G = 50.0
def incline(d, fr=G * math.sin(th)):
    d.force("G", (0, -G), (0, 0), "gravity")
    d.force("N", (-G * math.cos(th) * math.sin(th), G * math.cos(th) * math.cos(th)), (0, 0), "normal", surface=30)
    d.force("F_mu", (fr * math.cos(th), fr * math.sin(th)), (0, 0), "friction", surface=30)
check("a block resting on a 30° slope: N perpendicular, friction up the slope, net zero", problems(incline, a_dir=(0, 0)) == [], problems(incline, a_dir=(0, 0)))
check("a vertical normal force on a slope is refused",
      any("perpendicular" in p for p in problems(lambda d: d.force("N", (0, 40), (0, 0), "normal", surface=30))))
check("friction off the surface direction is refused",
      any("along the contact" in p for p in problems(lambda d: d.force("F_mu", (10, 0), (0, 0), "friction", surface=30))))
check("too little friction on a slope at rest is refused", problems(lambda d: incline(d, 5), a_dir=(0, 0)) != [])
d = FBD(Fig("t", 300, "t"), 1, a_dir=(0, 0)); incline(d); d.component("G_par", "G", (math.cos(th), math.sin(th)))
check("a component is the projection of its force", abs(math.hypot(*d.comps[0]["vec"]) - G * math.sin(th)) < 1e-9)
# tension, drag, the net force against the velocity
check("tension pulling away from the rope is refused",
      problems(lambda d: d.force("T", (0, -5), (0, 0), "tension", rope=(0, 1))) != [])
fall = lambda d: d.force("G", (0, -mg), (0, 0), "gravity").force("F_v", (0, 40), (0, 0), "drag", v_rel=(0, -12))
check("a falling ball speeding up: drag up, net force down", problems(fall, a_dir=(0, -1)) == [])
check("air resistance in the direction of motion is refused",
      problems(lambda d: d.force("F_v", (0, -40), (0, 0), "drag", v_rel=(0, -12))) != [])
up = lambda d: d.force("G", (0, -mg), (0, 0), "gravity").force("F_v", (0, -30), (0, 0), "drag", v_rel=(0, 8))
check("a ball thrown up: net force down although it moves up", problems(up, a_dir=(0, -1)) == [])
check("an object 'still moving forward' needs no forward force: a sliding stone slows down",
      problems(lambda d: d.force("G", (0, -mg), (0, 0), "gravity").force("N", (0, mg), (0, 0), "normal", surface=0)
               .force("F_mu", (-2, 0), (0, 0), "friction", surface=0), a_dir=(-1, 0)) == [])
# drawing
f = Fig("t", 300, "t"); FBD(f, 1, body=(300, 100, 60, 40), a_dir=(0, 0)).force("G", (0, -100), (300, 100), "gravity").force("N", (0, 100), (315, 120), "normal", surface=0).draw()
s = f.svg()
check("the arrows are as long as the forces (scale), labels bold", "\\mathbf{G}" in s and "M300,200 " in s and "M315,20 " in s, s[:400])
check("the body is drawn as a plain rectangle", '<rect x="270" y="80" width="60" height="40"' in s, s[:400])
try:
    FBD(Fig("bad", 300, "t"), 1, body=(0, 0, 40, 40), a_dir=(0, 0)).force("G", (0, -100), (0, 0), "gravity").draw(); ok = False
except ValueError: ok = True
check("draw() refuses a wrong diagram", ok)
FBD(Fig("t", 300, "t"), 1, body=(0, 0, 40, 40), a_dir=(0, 0), wrong="a distractor without the normal force").force("G", (0, -100), (0, 0), "gravity").draw()
check("a diagram marked wrong= draws (distractors, errors to find)", True)

# drawing conventions (Lauri 2026-10-29): they hold for every diagram, a deliberately wrong one too
def refused(build, word, **kw):
    try: d = FBD(Fig("c", 300, "t"), 1, **kw); build(d); d.draw()
    except ValueError as e: return word in str(e)
    return False
check("a point-particle diagram (no body) is refused, even when marked wrong",
      refused(lambda d: d.force("G", (0, -50), (0, 0), "gravity"), "point-particle", wrong="x"))
check("a force starting off the body is refused",
      refused(lambda d: d.force("G", (0, -50), (100, 100), "gravity"), "start on the body", body=(0, 0, 40, 40), wrong="x"))
box = (100, 100, 80, 60)                                            # bottom edge y = 130, from x = 60 to 140
fr = lambda at, v: (lambda d: d.force("F_mu", v, at, "friction", surface=0))
check("friction from the middle of the bottom side, along it, is refused (Lauri's figure 3)",
      refused(fr((80, 130), (-40, 0)), "friction", body=box, wrong="x"))
check("friction from the bottom corner outwards is drawn", not refused(fr((60, 130), (-40, 0)), "friction", body=box, wrong="x"))
check("friction ending at the bottom corner is drawn", not refused(fr((180, 130), (-40, 0)), "friction", body=box, wrong="x"))
check("friction neither starting nor ending on the body is refused", refused(fr((50, 130), (-40, 0)), "friction", body=box, wrong="x"))
th = 25; c, s_ = math.cos(math.radians(th)), math.sin(math.radians(th))
corner = (100 + 40 * c + 30 * s_, 100 - 40 * s_ + 30 * c)           # the lower front corner of a box rotated 25°
check("on a slope: friction up the slope from the lower front corner is drawn",
      not refused(fr(corner, (20 * c, 20 * s_)), "friction", body=(100, 100, 80, 60, th), wrong="x"))
check("on a slope: friction from the middle of the bottom side is refused",
      refused(fr((100 + 30 * s_, 100 + 30 * c), (20 * c, 20 * s_)), "friction", body=(100, 100, 80, 60, th), wrong="x"))
check("weight off the geometric centre is refused",
      refused(lambda d: d.force("G", (0, -50), (110, 100), "gravity"), "geometric centre", body=box, wrong="x"))
check("a normal force from inside the body is refused",
      refused(lambda d: d.force("N", (0, 50), (100, 100), "normal", surface=0), "contact surface", body=box, wrong="x"))
gn = lambda dx: (lambda d: d.force("G", (0, -50), (100, 100), "gravity").force("N", (0, 50), (100 + dx, 130), "normal", surface=0))
check("weight and normal force on one line are refused (they must be told apart)", refused(gn(0), "one line", body=box, wrong="x"))
check("weight and normal force 6 units apart are refused", refused(gn(6), "one line", body=box, wrong="x"))
check("weight and normal force side by side, 14 units apart, are drawn", not refused(gn(14), "one line", body=box, wrong="x"))
check("velocity, acceleration and force have distinct colours", len({FORCE, VELOCITY, ACCEL, NET}) == 4)
f = Fig("m", 300, "t"); d = FBD(f, 1, body=box); d.motion(r"\mathbf{v}", (1, 0), (60, 40)); d.motion(r"\mathbf{a}", (1, 0), (60, 20))
s = f.svg()
check("motion() draws velocity blue and acceleration orange", VELOCITY in s and ACCEL in s and FORCE not in s)
try: FBD(Fig("m", 300, "t"), 1, body=box).motion(r"\mathbf{v}", (1, 0), (100, 100)); ok = False
except ValueError: ok = True
check("a velocity arrow on the body is refused", ok)
print(f"{fails} failure(s)"); sys.exit(1 if fails else 0)
