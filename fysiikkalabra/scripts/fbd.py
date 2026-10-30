"""Force diagrams (voimakuviot) for lesson figures, with their physics checked as they are drawn (docs/force-diagrams.md).

A force diagram (voimakuvio) draws the object alone as a plain rectangle (FBD body=, rotated on a slope) with each force
starting at its point of application on it; the situation itself goes into a separate pictorial situation picture
(tilannekuva). Point-particle diagrams are not used in Finnish upper secondary physics, so FBD refuses them.

A figure function in a lesson's figures.py draws with figlib and puts the forces on the body with an FBD:

    from figlib import Fig
    from fbd import FBD, ground
    def rest():
        f = Fig("fy45-lepo", 300, "Voimakuvio: laatikko lattialla levossa. ...")
        ground(f, 120, 480, 230)
        d = FBD(f, scale=0.9, body=(300, 190, 120, 80), m=12, a=(0, 0))   # px per newton; the rectangle (cx, cy, w, h[, angle])
        d.force("G", (0, -118), (300, 190), kind="gravity")   # vector in newtons, x right, y UP; point of application
        d.force("N", (0, 118), (300, 230), kind="normal", surface=0)
        d.draw()
        return f.svg()

Vectors are in newtons with y pointing up; the figure's y points down, the FBD converts. Each arrow starts at its point
of application and its length is scale times the force, so relative lengths are physically right by construction.

draw() always refuses (ValueError) a diagram that breaks a drawing convention: no body rectangle (a point particle), a
force that does not start on the body, a weight that does not start at the body's geometric centre, a normal force
that does not start at the contact surface, weight and normal force drawn along one line so that they cannot be told
apart, a friction arrow that neither starts nor ends on the body's outline or that runs
along a side of it (start it at a corner, or end it at the surface), a velocity or acceleration arrow on the body.

It also refuses a diagram that breaks a rule a student is assessed on: two forces with one symbol, weight
not vertically down, a normal force not perpendicular to its surface or pointing into it, friction not along its
surface, tension not along its rope pulling away from the object, buoyancy not up, a drag force not against the
velocity relative to the air, a component that is not the projection of its force, or forces whose sum is not m·a
(with m and a given) or not in the direction of a (only the direction given). A deliberately wrong diagram, a
distractor of a choice or an error to find, says so: FBD(..., wrong="the normal force points down") skips the checks
and keeps the reason in the source for the reviewers (the conventions above still hold for it).

Visual conventions (one for every course): a force is a solid red arrow with a filled head and a bold symbol; a
component is a thinner dashed arrow of the same colour with an open head; velocity (blue) and acceleration (orange) are
thin, with an open head and a regular-weight symbol, in colours of their own so that force, velocity and acceleration
are never confused, and never on the body (FBD.motion draws them beside it); the net force, when a teaching figure
shows it, is a hollow green arrow labelled \\Sigma\\overline{F} away from the body.
"""
import math
from figlib import Fig, INK, MUTED, WHITE, RULE, n, translate

FORCE, FORCE_LIGHT, VELOCITY, ACCEL, NET = "#c92a2a", "#f2a69c", "#1971c2", "#e8590c", "#2b8a3e"
BODY, BODY_EDGE = "#f6f1e6", INK      # the plain rectangle of a force diagram
EDGE = 1.5          # figure units: how close to the body's outline a point counts as on it
APART = 12          # figure units: the least gap between weight and normal-force arrows that run side by side
KINDS = ("gravity", "normal", "friction", "tension", "applied", "buoyancy", "drag", "spring", "electric", "other")
TOL = 0.02          # relative to the largest force: drawing tolerance of the checks


def _unit(v):
    L = math.hypot(*v)
    return (v[0] / L, v[1] / L) if L else (0.0, 0.0)


def _dir(deg): return (math.cos(math.radians(deg)), math.sin(math.radians(deg)))


def _dot(a, b): return a[0] * b[0] + a[1] * b[1]


def _cross(a, b): return a[0] * b[1] - a[1] * b[0]


def open_head(f, x2, y2, ux, uy, color, w, head=13):
    """An open V head at (x2, y2) pointing along (ux, uy) in figure coordinates."""
    hw = head * 0.5
    bx, by = x2 - ux * head, y2 - uy * head
    return f.path(f"M{n(bx - uy * hw)},{n(by + ux * hw)} L{n(x2)},{n(y2)} L{n(bx + uy * hw)},{n(by - ux * hw)}", "none", color, w)


def dashed_arrow(f, x1, y1, x2, y2, color=FORCE, w=2.5):
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.line(x1, y1, x2 - ux * 2, y2 - uy * 2, color, w, "7 5")
    return open_head(f, x2, y2, ux, uy, color, w)


def hollow_arrow(f, x1, y1, x2, y2, color=NET, shaft=10, head=26, headlen=22):
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    px, py = -uy, ux
    bx, by = x2 - ux * headlen, y2 - uy * headlen
    pts = [(x1 + px * shaft / 2, y1 + py * shaft / 2), (bx + px * shaft / 2, by + py * shaft / 2), (bx + px * head / 2, by + py * head / 2),
           (x2, y2), (bx - px * head / 2, by - py * head / 2), (bx - px * shaft / 2, by - py * shaft / 2), (x1 - px * shaft / 2, y1 - py * shaft / 2)]
    return f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", WHITE, color, 2.5)


def ground(f, x1, x2, y, angle=0, color=INK, hatch=MUTED, below=True):
    """A surface from x1 to x2 at height y (the left end for a slope rising by angle degrees to the right), hatched on
    its solid side (below, or above for a ceiling)."""
    ux, uy = _dir(angle); L = (x2 - x1) / max(ux, 1e-9)
    ex, ey = x1 + ux * L, y - uy * L
    f.line(x1, y, ex, ey, color, 3, cap="round")
    s = 1 if below else -1
    k, step = 0.0, 16
    while k <= L - 4:
        ax, ay = x1 + ux * k, y - uy * k
        f.line(ax, ay, ax - 10, ay + s * 12, hatch, 1.5)
        k += step
    return (ex, ey)


class FBD:
    def __init__(self, fig, scale, body=None, m=None, a=None, a_dir=None, g=9.81, wrong=None, draw_body=True):
        """scale: figure units per newton (for a diagram without numbers, per unit of your own). m, a: mass (kg) and
        acceleration (m/s², (ax, ay) with y up) when known, so the forces must sum to m·a; a_dir: only the
        acceleration's direction ((0, 0) for none, e.g. at rest or at constant velocity), so the sum must point that
        way. body: the object as a rectangle (cx, cy, w, h) or (cx, cy, w, h, angle), centre in figure coordinates,
        angle in degrees anticlockwise (a box on a slope); draw() draws it plainly unless draw_body=False (the figure
        drew it). Each force starts at its own point of application on the body."""
        if body is not None and len(body) == 4: body = (*body, 0)
        self.f, self.s, self.m, self.a, self.a_dir, self.g, self.wrong = fig, scale, m, a, a_dir, g, wrong
        self.body, self.draw_body = body, draw_body
        self.forces, self.comps, self.notes = [], [], []

    def force(self, sym, vec, at, kind="other", name=None, surface=None, outward=None, rope=None, v_rel=None,
              label=None, lab=None, tex=None, push=False):
        """sym: the plain symbol ("G", "N", "F_mu", "T_1") the checks know it by; tex: its LaTeX when not \\overline{sym}.
        surface: the contact surface's angle in degrees (0 horizontal; for normal and friction), outward: the unit
        normal pointing out of the surface towards the object (default up-left of the surface direction), rope: the
        direction along the rope away from the object, v_rel: the object's velocity relative to the air (drag).
        lab: the label's offset (dx, dy) in figure units from the arrow tip (default along the arrow). push=True draws
        the arrow ending at its point of application, outside the body (a push from outside, e.g. a handle or a ceiling)."""
        if kind not in KINDS: raise ValueError(f"force {sym}: kind {kind!r} is not one of {KINDS}")
        self.forces.append(dict(sym=sym, vec=tuple(vec), at=at, kind=kind, name=name, surface=surface, outward=outward,
                                rope=rope, v_rel=v_rel, lab=lab, tex=tex or _bold(sym), push=push))
        return self

    def component(self, sym, of, axis, lab=None, at=None, tex=None):
        """The projection of force `of` on the unit direction `axis` ((x, y), y up), drawn dashed from the same point
        (or from `at`). It is drawn in place of nothing: the original force stays, and the reader sees the difference."""
        F = next(x for x in self.forces if x["sym"] == of); u = _unit(axis); k = _dot(F["vec"], u)
        self.comps.append(dict(sym=sym, of=of, vec=(u[0] * k, u[1] * k), at=at, lab=lab, tex=tex or _bold_comp(sym)))
        return self

    def check(self):
        """The physics problems of the diagram, as sentences (empty when right)."""
        out, F = [], self.forces
        syms = [x["sym"] for x in F] + [c["sym"] for c in self.comps]
        for s in set(syms):
            if syms.count(s) > 1: out.append(f"two arrows share the symbol {s}: name each force unambiguously")
        big = max((math.hypot(*x["vec"]) for x in F), default=1) or 1
        eps = TOL * big
        for x in F:
            v, k, s = x["vec"], x["kind"], x["sym"]
            if math.hypot(*v) == 0: out.append(f"{s} has no length"); continue
            if k in ("gravity",) and (abs(v[0]) > eps or v[1] >= 0): out.append(f"{s}: weight points vertically down")
            if k == "buoyancy" and (abs(v[0]) > eps or v[1] <= 0): out.append(f"{s}: buoyancy points vertically up")
            if k in ("normal", "friction"):
                if x["surface"] is None: out.append(f"{s}: give the contact surface's angle (surface=)"); continue
                t = _dir(x["surface"]); nrm = x["outward"] or (-t[1], t[0])
                if k == "normal":
                    if abs(_dot(v, t)) > eps: out.append(f"{s}: a normal force is perpendicular to the contact surface")
                    if _dot(v, nrm) <= 0: out.append(f"{s}: a normal force pushes away from the surface, out of it")
                if k == "friction" and abs(_dot(v, nrm)) > eps: out.append(f"{s}: friction acts along the contact surface")
            if k == "tension":
                if x["rope"] is None: out.append(f"{s}: give the rope's direction away from the object (rope=)")
                elif abs(_cross(_unit(v), _unit(x["rope"]))) > TOL or _dot(v, x["rope"]) <= 0:
                    out.append(f"{s}: tension acts along the rope and pulls the object towards the rope")
            if k == "drag" and x["v_rel"] is not None:
                if abs(_cross(_unit(v), _unit(x["v_rel"]))) > TOL or _dot(v, x["v_rel"]) >= 0:
                    out.append(f"{s}: air resistance is opposite to the velocity relative to the air")
        for c in self.comps:
            par = next(x for x in F if x["sym"] == c["of"])
            if math.hypot(*c["vec"]) > math.hypot(*par["vec"]) * (1 + TOL): out.append(f"{c['sym']} is longer than its force {c['of']}")
        net = (sum(x["vec"][0] for x in F), sum(x["vec"][1] for x in F))
        if self.m is not None and self.a is not None:
            want = (self.m * self.a[0], self.m * self.a[1])
            if math.hypot(net[0] - want[0], net[1] - want[1]) > eps:
                out.append(f"the forces sum to ({net[0]:.3g}, {net[1]:.3g}) N, but m·a = ({want[0]:.3g}, {want[1]:.3g}) N")
        elif self.a_dir is not None:
            d = _unit(self.a_dir)
            if d == (0.0, 0.0):
                if math.hypot(*net) > eps: out.append("the object does not accelerate, so its forces must cancel (equal and opposite lengths)")
            elif math.hypot(*net) <= eps or abs(_cross(_unit(net), d)) > 0.05 or _dot(net, d) <= 0:
                out.append("the net force must point in the direction of the acceleration")
        return out

    def _local(self, p):
        """p in the body's own frame: (u along its width, v along its height, up), from its centre."""
        cx, cy, w, h, ang = self.body; c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        dx, dy = p[0] - cx, cy - p[1]
        return dx * c + dy * s, -dx * s + dy * c

    def _where(self, p):
        """'in', 'edge' or 'out' of the body rectangle."""
        u, v = self._local(p); w, h = self.body[2] / 2, self.body[3] / 2
        if abs(u) <= w - EDGE and abs(v) <= h - EDGE: return "in"
        if abs(u) <= w + EDGE and abs(v) <= h + EDGE: return "edge"
        return "out"

    def conventions(self):
        """The drawing-convention problems (they hold for a deliberately wrong diagram too), as sentences."""
        if self.body is None:
            return ["draw the object as a rectangle (body=): point-particle force diagrams are not used"]
        out = []
        for x in self.forces:
            s, p = x["sym"], x["at"]
            if p is None: out.append(f"{s}: give its point of application on the body (at=)"); continue
            if self._where(p) == "out": out.append(f"{s} must start on the body, at its point of application")
            if x["kind"] == "friction":
                p, q = self._ends(x)
                ends = [self._where(p) == "edge", self._where(q) == "edge"]
                mid = [(p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t) for t in (0.25, 0.5, 0.75)]
                if not any(ends) or any(self._where(m) != "out" for m in mid):
                    out.append(f"{s}: friction starts or ends on the body's outline and is drawn outside it, never along a side "
                               "from the middle of it (start it at a corner)")
        cx, cy = self.body[:2]
        for x in self.forces:
            if x["kind"] == "gravity" and x["at"] and math.hypot(x["at"][0] - cx, x["at"][1] - cy) > EDGE:
                out.append(f"{x['sym']}: the weight starts at the body's geometric centre")
            if x["kind"] == "normal" and x["at"] and self._where(x["at"]) == "in" and not x.get("push"):
                out.append(f"{x['sym']}: a normal force starts at the contact surface")
        for gw in (x for x in self.forces if x["kind"] == "gravity"):
            for nf in (x for x in self.forces if x["kind"] == "normal"):
                if self._overlap(gw, nf):
                    out.append(f"{gw['sym']} and {nf['sym']} run along one line: draw them apart so both can be told apart "
                               f"(at least {APART} units side by side)")
        for c in self.comps:
            if c["at"] is not None and self._where(c["at"]) == "out": out.append(f"{c['sym']} must start on the body")
        return out

    def _overlap(self, a, b):
        """Two parallel arrows closer than APART to each other along a common stretch."""
        (a1, a2), (b1, b2) = self._ends(a), self._ends(b)
        u = _unit((a2[0] - a1[0], a2[1] - a1[1])); v = _unit((b2[0] - b1[0], b2[1] - b1[1]))
        if abs(_cross(u, v)) > 0.05: return False
        side = abs(_cross(u, (b1[0] - a1[0], b1[1] - a1[1])))
        if side >= APART: return False
        ta = sorted((0.0, _dot(u, (a2[0] - a1[0], a2[1] - a1[1])))); tb = sorted(_dot(u, (p[0] - a1[0], p[1] - a1[1])) for p in (b1, b2))
        return min(ta[1], tb[1]) - max(ta[0], tb[0]) > 4

    def draw(self, label_size=None):
        p = self.conventions() + ([] if self.wrong else self.check())
        if p: raise ValueError(f"{self.f.fid}: " + "; ".join(p))
        if self.draw_body:
            cx, cy, w, h, ang = self.body
            self.f.rect(cx - w / 2, cy - h / 2, w, h, BODY, BODY_EDGE, 2.5,
                        extra=f'transform="rotate({n(-ang)} {n(cx)} {n(cy)})"' if ang else "")
        for x in self.forces: self._arrow(x, solid=True, size=label_size)
        for c in self.comps:
            c = dict(c); c["at"] = c["at"] or next(x for x in self.forces if x["sym"] == c["of"])["at"]
            self._arrow(c, solid=False, size=label_size)
        return self

    def net(self, at, lab=None):
        """The net force as its own hollow arrow away from the body (a teaching figure only; never on the forces)."""
        v = (sum(x["vec"][0] for x in self.forces), sum(x["vec"][1] for x in self.forces))
        x2, y2 = at[0] + v[0] * self.s, at[1] - v[1] * self.s
        hollow_arrow(self.f, at[0], at[1], x2, y2)
        u = _unit((x2 - at[0], y2 - at[1])); d = lab or (u[0] * 26, u[1] * 26)
        self.f.tex(x2 + d[0], y2 + d[1], r"\Sigma\overline{F}", "middle", NET)
        return self

    def motion(self, sym, vec, at, length=None, lab=None, kind=None):
        """A velocity or acceleration arrow beside the body (thin, open head): not a force. kind: "velocity" (blue) or
        "acceleration" (orange); by default from the symbol (\\overline{a} is an acceleration). vec gives the
        direction (y up); length in figure units (default 70). With a body it must lie wholly outside it."""
        kind = kind or ("acceleration" if r"\overline{a}" in sym else "velocity")
        if kind not in ("velocity", "acceleration"): raise ValueError(f"motion {sym}: kind {kind!r}")
        col = ACCEL if kind == "acceleration" else VELOCITY
        u = _unit(vec); L = length or 70
        x1, y1 = at; x2, y2 = x1 + u[0] * L, y1 - u[1] * L
        if self.body is not None and any(self._where((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)) != "out" for t in (0, 0.25, 0.5, 0.75, 1)):
            raise ValueError(f"{self.f.fid}: {sym}: a {kind} arrow is not a force and is drawn beside the body, not on it")
        self.f.line(x1, y1, x2 - u[0] * 2, y2 + u[1] * 2, col, 2.5)
        open_head(self.f, x2, y2, u[0], -u[1], col, 2.5)
        d = lab or (u[0] * 22, -u[1] * 22 - 4)
        self.f.tex(x2 + d[0], y2 + d[1], sym, "middle", col)
        return self

    def _ends(self, x):
        """The arrow's tail and tip in figure coordinates."""
        (px, py), (vx, vy) = x["at"], x["vec"]
        if x.get("push"): return (px - vx * self.s, py + vy * self.s), (px, py)
        return (px, py), (px + vx * self.s, py - vy * self.s)

    def _arrow(self, x, solid, size):
        (x1, y1), (x2, y2) = self._ends(x)
        if solid: self.f.arrow(x1, y1, x2, y2, FORCE, 4, 18)
        else: dashed_arrow(self.f, x1, y1, x2, y2)
        u = _unit((x2 - x1, y2 - y1))
        if x.get("push"):                                          # labelled at its tail, away from the body
            d = x["lab"] or (-u[0] * 22, -u[1] * 22)
            self.f.tex(x1 + d[0], y1 + d[1], x["tex"], "middle", FORCE, size=size); return
        d = x["lab"] or (u[0] * 24, u[1] * 24)
        self.f.tex(x2 + d[0], y2 + d[1], x["tex"], "middle", FORCE, size=size)


def _bold(sym):
    """\\overline{G}, \\overline{F}_\\mu, \\overline{T}_1 from "G", "F_mu", "T_1"."""
    base, _, sub = sym.partition("_")
    sub = {"mu": r"\mu"}.get(sub, sub)
    return rf"\overline{{{base}}}" + (f"_{{{sub}}}" if sub else "")


def _bold_comp(sym):
    """A component's symbol: G_x → \\overline{G}_x is a vector component; the course writes components plain with a
    subscript (G_x) only for their scalar values, so the arrow keeps the bold base."""
    return _bold(sym)
