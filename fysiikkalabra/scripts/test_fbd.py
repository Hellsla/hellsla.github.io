"""fbd.py: a force diagram that breaks an assessed rule is refused; a right one draws (docs/force-diagrams.md).

  python scripts/test_fbd.py"""
import math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from figlib import Fig
from fbd import FBD

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

def problems(build, **kw):
    d = FBD(Fig("t", 300, "test"), 1, **kw); build(d); return d.check()

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
f = Fig("t", 300, "t"); FBD(f, 1, a_dir=(0, 0)).force("G", (0, -100), (300, 100), "gravity").force("N", (0, 100), (300, 100), "normal", surface=0).draw()
s = f.svg()
check("the arrows are as long as the forces (scale), labels bold", "\\mathbf{G}" in s and "M300,200 " in s and "M300,0 " in s, s[:400])
try:
    FBD(Fig("bad", 300, "t"), 1, a_dir=(0, 0)).force("G", (0, -100), (0, 0), "gravity").draw(); ok = False
except ValueError: ok = True
check("draw() refuses a wrong diagram", ok)
FBD(Fig("t", 300, "t"), 1, a_dir=(0, 0), wrong="a distractor without the normal force").force("G", (0, -100), (0, 0), "gravity").draw()
check("a diagram marked wrong= draws (distractors, errors to find)", True)
print(f"{fails} failure(s)"); sys.exit(1 if fails else 0)
