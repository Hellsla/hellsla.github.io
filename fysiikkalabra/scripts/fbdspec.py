"""Force diagrams written as a short spec inside a text, drawn by scripts/fbd.py at build time (teacher 2026-10-30:
a model solution whose step is "Voimakuvio" shows a drawn force diagram, never one described in words).

A solution step (exercises/solutions.md, an inquiry task's solution, a Sovella solution) puts the diagram right after
its "**Voimakuvio:**" sentence as a fenced block; the block is the same in every language (symbols and numbers only):

    ```voimakuvio
    pinta 0              the contact surface's angle in degrees (0 level, 30 a slope rising to the right, -30 to the
                         left); leave it out when nothing supports the body (hanging, falling, a lift's rope)
    G 118                the weight, from the centre, straight down (N, or any unit used for every force)
    N 118                the normal force, from the contact surface, perpendicular to it (needs pinta); `N 118 työntö`
                         draws it outside the body ending at the contact surface ("alhaalta ylös alapintaan asti")
    F_mu 30 vasen        friction along the surface, from a bottom corner: vasen | oikea | ylös | alas (ylös = up the slope);
                         another symbol is friction with the word `kitka`: `F 24 oikea kitka` (the road's push on a wheel)
    F 40 30              any other force: its size and direction in degrees (0 right, 90 up) or a word
    F 40 0 työntö        a push: the arrow ends on the body (a hand pushing a box)
    F 40 0 @ala          any force but G, N and friction can name the face it acts on (@ala @ylä @vasen @oikea):
                         it starts (a push: ends) at the middle of that face; forces along one line are moved apart
    T 40 90              a rope's tension, from the outline, along the rope
    F_v 20 ylös          air resistance; F_n buoyancy (noste); F_j a spring; other symbols are "other" forces
    a oikea              the acceleration's direction (a word or degrees; 0 alone: the body does not accelerate; on
                         a slope ylös/alas mean up/down the slope, for forces the words are always absolute):
                         drawn beside the body in orange and used to check that the forces sum that way
    v oikea              the velocity's direction, drawn beside the body in blue (never as a force); optional
    akselit 0            the x-y axes (x at this angle); `komponentit G` draws G's components on them, dashed
    erikseen             level surface only: the horizontal forces get their own scale (the largest drawn 0,6 times
                         the largest vertical one). This happens by itself when every force is horizontal or vertical
                         and one direction's largest force is under 0,4 of the other's (a car's 620 N driving force
                         beside a 10 kN weight); the sums along each axis then still show, and the text alternative
                         says the scales differ
    ---                  a second body of a coupled system (each body gets its own diagram, side by side)
    ```

The diagram is drawn to scale: one linear scale for every force and component, so equal forces are drawn equal and a
sum of forces stays a sum. Only a force under MIN_SHOWN of the largest is drawn at MIN_SHOWN (to be seen), and the text
alternative then says so. The diagram has with the conventions and physics checks of fbd.FBD (weight from the centre, normal force
from the contact surface and perpendicular to it, friction from the surface along it, tension along its rope, the sum
of the forces along the acceleration, components separate and dashed): a spec that breaks one is a build error, so a
wrong diagram never reaches the page. `python scripts/fbdspec.py check` finds every "Voimakuvio" step without a drawn
diagram (CI) and renders every spec; `python scripts/fbdspec.py show <file>` writes the diagrams of one file to
preview/fbd-<lang>-<course>-<id>-<file>.html for a look (its own page, so parallel looks do not overwrite each other)."""
import hashlib, html, math, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fbd, figlib, i18n
from figlib import Fig, MUTED, INK

ROOT = pathlib.Path(__file__).resolve().parents[1]
FENCE = re.compile(r"```voimakuvio\n(.*?)```", re.S)
WORDS = {"oikea": 0, "right": 0, "vasen": 180, "left": 180, "ylös": 90, "up": 90, "alas": 270, "down": 270}
KIND = [(r"^G(_|$)", "gravity"), (r"^N(_|$)", "normal"), (r"^F_(\\?mu|μ)", "friction"), (r"^T(_|$)", "tension"),
        (r"^F_(v|vastus)$", "drag"), (r"^F_(n|noste)$", "buoyancy"), (r"^F_(j|jousi)$", "spring")]
W, H = 120, 70                     # the body rectangle (figure units)


def kind_of(sym):
    return next((k for pat, k in KIND if re.search(pat, sym)), "applied")


def tex_of(sym):
    """G -> \\overline{G}, F_mu -> \\overline{F}_{\\mu}, T_1 -> \\overline{T}_{1}, F_AP -> \\overline{F}_{\\text{AP}}."""
    base, _, sub = sym.partition("_")
    sub = r"\mu" if sub in ("mu", "μ") else rf"\text{{{sub}}}" if sub.isalpha() else sub       # F_AP, F_i: names, upright
    return rf"\overline{{{base}}}" + (f"_{{{sub}}}" if sub else "")


def parse(spec):
    """[{surface, forces: [(sym, size, deg or word, push)], a, axes, comps}] per body."""
    bodies = []
    for chunk in re.split(r"^---\s*$", spec, flags=re.M):
        b = dict(surface=None, forces=[], a=None, v=None, axes=None, comps=[], split=False, kinds={})
        for raw in chunk.splitlines():
            line = raw.split("#")[0].strip()
            if not line: continue
            t = line.split()
            if t[0] == "pinta": b["surface"] = float(t[1].replace(",", "."))
            elif t[0] == "a": b["a"] = t[1]
            elif t[0] == "v": b["v"] = t[1]
            elif t[0] == "akselit": b["axes"] = float(t[1].replace(",", ".")) if len(t) > 1 else 0.0
            elif t[0] == "komponentit": b["comps"] += t[1:]
            elif t[0] in ("erikseen", "separate"): b["split"] = True
            else:
                if len(t) < 2: raise ValueError(f"voimakuvio: '{line}': a force needs its size")
                rest = t[2:]; face = next((w for w in rest if w in SIDES), None); rest = [w for w in rest if w not in SIDES]
                if "kitka" in rest or "friction" in rest:                             # a friction force with its own symbol
                    b["kinds"][t[0]] = "friction"; rest = [w for w in rest if w not in ("kitka", "friction")]
                if kind_of(t[0]) == "normal": rest = [None] + rest                  # a normal force: its face is its direction
                                                                                   # (`työntö`: drawn from below up to the face)
                b["forces"].append((t[0], float(t[1].replace(",", ".")), rest[0] if rest else None,
                                    "työntö" in rest or "push" in rest, face))
        if not b["forces"]: raise ValueError("voimakuvio: a body without forces")
        bodies.append(b)
    return bodies


def _unit(deg): return (math.cos(math.radians(deg)), math.sin(math.radians(deg)))


def _outline(cx, cy, ang, d):
    """The point where a ray from the centre in direction d (y up) leaves the rectangle rotated by ang, in figure coords."""
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    u, v = d[0] * c + d[1] * s, -d[0] * s + d[1] * c                  # d in the body's frame
    k = min(W / 2 / abs(u) if abs(u) > 1e-9 else 1e9, H / 2 / abs(v) if abs(v) > 1e-9 else 1e9)
    lu, lv = u * k, v * k
    return cx + lu * c - lv * s, cy - (lu * s + lv * c)


def _local(cx, cy, ang, u, v):
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return cx + u * c - v * s, cy - (u * s + v * c)


def direction(word, surface=None):
    """A direction word or degrees -> degrees (y up). Words are absolute (ylös = vertically up), except for the
    acceleration on a slope: see along()."""
    if word is None: raise ValueError("voimakuvio: give the direction (a word or degrees)")
    if word in WORDS: return WORDS[word]
    return float(word.replace(",", "."))


def along(word, surface):
    """The acceleration's direction in degrees: on a slope, ylös/alas (up/down) mean up or down the slope."""
    if surface not in (None, 0) and word in ("ylös", "up", "alas", "down"):
        up = surface if surface > 0 else surface + 180                           # up the slope
        return up if word in ("ylös", "up") else up + 180
    return direction(word, surface)


def _dir_words(deg):
    T = i18n.t
    deg %= 360
    for d, k in ((0, "right"), (90, "up"), (180, "left"), (270, "down"), (360, "right")):
        if abs(deg - d) < 1: return T(f"fbd.dir_{k}")
    return T("fbd.dir_deg", deg=f"{round(deg)}")


SIDES = {"@ala": (0, -1), "@ylä": (0, 1), "@vasen": (-1, 0), "@oikea": (1, 0)}                                          # a face of the body, in its own frame
MIN_SHOWN = 0.15                   # a force under this share of the largest is drawn at it, to be seen
SPLIT = 0.6                        # an axis on its own scale: its largest force drawn this share of the other axis' largest
MIN_AXIS = 0.4                     # on a level surface with every force horizontal or vertical, an axis whose largest force is
                                   # under this share of the other axis' largest gets its own scale (a cyclist's 24 N beside 785 N)


def _face(word):
    """A contact face word (default the bottom) -> its outward unit vector in the body's frame."""
    if word is None: return SIDES["@ala"]
    if word not in SIDES: raise ValueError(f"voimakuvio: '{word}' is not a face: @ala, @ylä, @vasen or @oikea")
    return SIDES[word]


def _rot(ang, u, v):
    """A vector of the body's frame (u along its width, v up its height) in the world frame (y up)."""
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return (u * c - v * s, u * s + v * c)


def _surface(f, p, q, solid):
    """A contact surface from p to q (figure coords), hatched on its solid side (unit vector solid, y up)."""
    f.line(p[0], p[1], q[0], q[1], INK, 3, cap="round")
    L = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
    k = 6.0
    while k <= L - 4:
        ax, ay = p[0] + ux * k, p[1] + uy * k
        f.line(ax, ay, ax + solid[0] * 12 - ux * 8, ay - solid[1] * 12 - uy * 8, MUTED, 1.5)
        k += 16


def _forces(b, cx, cy, ang, shown, scale):
    """(sym, vec, at, kind, extra, description direction) of each force of a body; shown(size) is the drawn size."""
    out, faces = [], set()
    def taken(u):                                                                  # another force starts near u on the body
        c, s_ = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        return any(abs((at[0] - cx) * c - (at[1] - cy) * s_ - u) < 20 for _, _, _, at, k, _ in out if k not in ("gravity", "normal"))
    order = sorted(b["forces"], key=lambda x: kind_of(x[0]) == "normal")            # the normal forces last: they dodge
    for sym, size, word, push, face in order:
        k = b.get("kinds", {}).get(sym) or kind_of(sym)
        if k in ("normal", "friction"): horiz = (_face(face)[1] == 0) == (k == "normal")
        elif k == "gravity": horiz = False
        else: horiz = round(direction(word)) % 180 == 0
        L = shown(size, horiz)
        if b["split"] and k not in ("normal", "friction", "gravity") and round(direction(word)) % 90:
            raise ValueError(f"voimakuvio: `erikseen` needs every force horizontal or vertical ({sym})")
        if k == "gravity":
            out.append((sym, (0, -size), (0, -L), (cx, cy), k, {})); continue
        if k in ("normal", "friction"):
            if b["surface"] is None: raise ValueError(f"voimakuvio: {sym} needs `pinta`")
            fo = _face(face); faces.add(face or "@ala")
            nrm = _rot(ang, -fo[0], -fo[1])                                        # into the body, out of the surface
            tan = _rot(ang, -fo[1], fo[0]) if fo[1] == 0 else _rot(ang, 1, 0)      # along the face: up a side, right on top/bottom
            half = (W / 2, H / 2)
            if k == "normal":
                off = 0.3 * (W if fo[1] else H) * (1 if ang >= 0 else -1)
                if fo[1]:                                                           # beside G's line, clear of its shaft,
                    clear = lambda u: abs(u * math.cos(math.radians(ang)) - fo[1] * H / 2 * math.sin(math.radians(ang))) >= 16
                    cands = [u for f_ in (0.3, 0.38) for u in (off * f_ / 0.3, -off * f_ / 0.3) if clear(u)]
                    off = next((u for u in cands if not taken(u)), cands[0] if cands else off)   # away from other forces' tails
                ux, vy = (off, fo[1] * half[1]) if fo[1] else (fo[0] * half[0], off)
                out.append((sym, (nrm[0] * size, nrm[1] * size), (nrm[0] * L, nrm[1] * L), _local(cx, cy, ang, ux, vy), k,
                            dict(surface=math.degrees(math.atan2(tan[1], tan[0])), outward=nrm, **({"push": True} if push else {}))))
                continue
            sgn = {"oikea": 1, "right": 1, "ylös": 1, "up": 1, "vasen": -1, "left": -1, "alas": -1, "down": -1}.get(word)
            if sgn is None: raise ValueError(f"voimakuvio: {sym}: friction is vasen, oikea, ylös or alas along the surface")
            if not fo[1] and word in ("oikea", "right", "vasen", "left"): raise ValueError(f"voimakuvio: {sym}: on a side face friction is ylös or alas")
            if fo[1] and word in ("ylös", "up", "alas", "down"):                    # up/down a slope
                if ang == 0: raise ValueError(f"voimakuvio: {sym}: on a level surface friction is vasen or oikea")
                if ang < 0: sgn = -sgn
            t = (tan[0] * sgn, tan[1] * sgn)
            ux, vy = (sgn * half[0], fo[1] * half[1]) if fo[1] else (fo[0] * half[0], sgn * half[1])  # the corner it starts at
            out.append((sym, (t[0] * size, t[1] * size), (t[0] * L, t[1] * L), _local(cx, cy, ang, ux, vy), k,
                        dict(surface=math.degrees(math.atan2(tan[1], tan[0])), outward=nrm)))
            continue
        u = _unit(direction(word))
        if face: fo = _face(face); at = _local(cx, cy, ang, fo[0] * W / 2, fo[1] * H / 2)       # from the middle of that face
        else: at = (cx, cy) if k == "buoyancy" else _outline(cx, cy, ang, (-u[0], -u[1]) if push else u)   # a push ends on the outline
        extra = {"rope": u} if k == "tension" else {"v_rel": (-u[0], -u[1])} if k == "drag" else {}
        if push: extra["push"] = True
        out.append((sym, (u[0] * size, u[1] * size), (u[0] * L, u[1] * L), at, k, extra))
    return _apart(out, scale), faces


def _apart(out, scale):
    """Two forces drawn along one line (two weights from the centre, a drag and a buoyancy both up) are moved apart
    sideways, along the face they start on, so both arrows show; a second weight is then drawn as an "other" force
    (its own centre of mass is not the body's centre)."""
    res, weights = [], 0
    first = next((i for i, x in enumerate(out) if x[4] == "gravity"), None)        # the weight stays at the centre
    order = ([out[first]] if first is not None else []) + [x for i, x in enumerate(out) if i != first]
    for sym, vec, L, at, k, extra in order:
        if k == "gravity":
            weights += 1
            if weights > 1: k = "gravity2"
        u = fbd._unit(L)
        for _ in range(4):
            hit = False
            for _, _, L2, at2, k2, ex2 in res:
                u2 = fbd._unit(L2)
                if abs(u[0] * u2[1] - u[1] * u2[0]) > 0.05: continue
                dx, dy = at2[0] - at[0], at[1] - at2[1]                            # world frame, y up
                if abs(u[0] * dy - u[1] * dx) >= 14: continue                       # side by side already
                a0, a1 = sorted((0.0, math.hypot(*L) * scale * (-1 if extra.get("push") else 1)))
                p0 = u[0] * dx + u[1] * dy; p1 = p0 + (u[0] * u2[0] + u[1] * u2[1]) * math.hypot(*L2) * scale * (-1 if ex2.get("push") else 1)
                gap = -26 if u[0] * u2[0] + u[1] * u2[1] > 0 else 4                 # same way: their labels need room too
                if min(a1, max(p0, p1)) - max(a0, min(p0, p1)) > gap: hit = True; break   # along a common stretch
            if not hit: break
            at = (at[0] + (-u[1]) * 18 * (1 if weights < 3 else -1), at[1] - u[0] * 18)
        res.append((sym, vec, L, at, k, extra))
    return res


def _box(cx, cy, tex, size=24):
    w = figlib.visible_len(figlib.translate(tex)) * size * 0.52 + 8; h = size * 1.2
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)


def _hits(box, pts):
    return sum(1 for x, y in pts if box[0] - 2 <= x <= box[2] + 2 and box[1] - 2 <= y <= box[3] + 2)


def _place(arrows, solid, width, top, bottom):
    """A label offset for each arrow (tail, tip, tex, at_tail) that keeps the labels off each other, off the arrows,
    off the body and the surfaces (`solid`: points that a label must not cover) and inside the figure: the first
    candidate with the fewest collisions, along the arrow beyond its end first (the textbook place)."""
    pts = list(solid)
    for (x1, y1), (x2, y2), *_ in arrows:
        L = math.hypot(x2 - x1, y2 - y1); k = max(2, int(L / 4))
        pts += [(x1 + (x2 - x1) * i / k, y1 + (y2 - y1) * i / k) for i in range(k + 1)]
    boxes, out = [], []
    for (x1, y1), (x2, y2), tex, at_tail in arrows:
        L = math.hypot(x2 - x1, y2 - y1) or 1; ux, uy = (x2 - x1) / L, (y2 - y1) / L
        if at_tail: ex, ey, ux, uy = x1, y1, -ux, -uy                         # a push: labelled at its tail, outwards
        else: ex, ey = x2, y2
        nx, ny = -uy, ux
        cands = [(ux * d, uy * d) for d in (24, 34, 46)] + [(ux * 10 + nx * s * d, uy * 10 + ny * s * d) for d in (22, 32, 44) for s in (1, -1)] \
              + [(-ux * L * f + nx * s * 24, -uy * L * f + ny * s * 24) for f in (0.3, 0.55) for s in (1, -1)]
        best = None
        for i, (dx, dy) in enumerate(cands):
            bx = _box(ex + dx, ey + dy, tex)
            cost = 3 * _hits(bx, pts) + 40 * sum(1 for o in boxes if not (bx[2] < o[0] or o[2] < bx[0] or bx[3] < o[1] or o[3] < bx[1]))
            cost += 200 * (bx[0] < 2 or bx[2] > width - 2 or bx[1] < top or bx[3] > bottom) + i * 0.5
            if best is None or cost < best[0]: best = (cost, dx, dy, bx)
        boxes.append(best[3]); out.append((best[1], best[2]))
    return out, boxes


def _probe(b, cx, cy, ang, scale):
    """[(size, horizontal?)] of a body's forces."""
    probe = []
    _forces(dict(b, split=False), cx, cy, ang, lambda size, horiz: probe.append((size, horiz)) or size, scale)
    return probe


LENGTHS = {}                       # the drawn length of each arrow of the last diagram (tests)


def draw(spec, fid, _frame=None):
    """The SVG of one spec (one or two bodies side by side). The physics checks of fbd.FBD run on the true sizes; a
    force much smaller than the largest is drawn at MIN_SHOWN of it (the text alternative then says so). The figure is
    drawn once on a tall canvas, then again cut to what it holds."""
    bodies = parse(spec)
    two = len(bodies) > 1
    big = max(f[1] for b in bodies for f in b["forces"])
    scale = (70 if two else 100) / big
    floor = lambda x: math.copysign(max(abs(x), MIN_SHOWN * big), x) if x else 0.0   # one linear scale, tiny ones visible
    Hfig, shift, xr = _frame or (460, 0, None)
    f = Fig(fid, Hfig, "")
    words, approx, split, ys, xs = [], False, False, [], []
    for i, b in enumerate(bodies):
        cx = (150 + 300 * i) if two else 300; cy = 230 - shift
        surf = b["surface"]; ang = surf if surf is not None else 0.0
        a_dir = None
        if b["a"] is not None:
            a_dir = (0, 0) if b["a"] in ("0", "nolla", "none") else _unit(along(b["a"], surf))
        if b["split"] and surf not in (None, 0): raise ValueError("voimakuvio: `erikseen` is for a level surface")
        hz = {True: 1.0, False: 1.0}                                                 # the scale of horizontal / vertical forces
        level = surf in (None, 0) and all(kind_of(x[0]) in ("gravity", "normal", "friction") or round(direction(x[2])) % 90 == 0
                                          for x in b["forces"])
        if level:                                                                  # one axis much weaker than the other:
            probe = _probe(b, cx, cy, ang, scale)                                  # that axis gets its own scale
            mv = max([x for x, h in probe if not h] or [0]); mh = max([x for x, h in probe if h] or [0])
            weak = min(mv, mh)
            if weak and (b["split"] or weak < MIN_AXIS * max(mv, mh)):
                hz[mh < mv] = SPLIT * max(mv, mh) / weak
        shown = lambda size, horiz=False: floor(size * hz[horiz])
        forces, faces = _forces(b, cx, cy, ang, shown, scale)
        split = split or hz[True] != hz[False]
        approx = approx or any(0 < size * hz[h] < MIN_SHOWN * big for size, h in _probe(b, cx, cy, ang, scale))   # one drawn at the floor
        true = fbd.FBD(f, scale, body=(cx, cy, W, H, ang), a_dir=a_dir)              # the physics, on the true sizes
        for sym, vec, _, at, k, extra in forces: true.force(sym, vec, at, "gravity" if k == "gravity2" else k, tex=tex_of(sym), **extra)
        axes = None
        if b["axes"] is not None:
            axes = (_unit(b["axes"]), _unit(b["axes"] + 90))
            for sym in b["comps"]: true.component(f"{sym}_x", sym, axes[0]); true.component(f"{sym}_y", sym, axes[1])
        problems = true.check()                                                    # conventions: on the drawn one
        if problems: raise ValueError(f"voimakuvio: " + "; ".join(problems))
        solid = []                                                                 # points a label must not cover
        for gx in range(-10, 11):
            for gy in range(-5, 6): solid.append(_local(cx, cy, ang, gx * W / 20, gy * H / 10))
        for face in sorted(faces):                                                 # the surfaces it touches
            fo = _face(face); sol = _rot(ang, fo[0], fo[1])
            al = (1, 0) if fo[1] else (0, 1); e = W * 0.95 if fo[1] else H * 1.4
            p1 = _local(cx, cy, ang, fo[0] * W / 2 - al[0] * e, fo[1] * H / 2 - al[1] * e)
            p2 = _local(cx, cy, ang, fo[0] * W / 2 + al[0] * e, fo[1] * H / 2 + al[1] * e)
            _surface(f, p1, p2, sol)
            solid += [(p1[0] + (p2[0] - p1[0]) * t / 30 + sol[0] * 6, p1[1] + (p2[1] - p1[1]) * t / 30 - sol[1] * 6) for t in range(31)]
            ys += [p1[1], p2[1]]; xs += [p1[0], p2[0]]
        arrows = []                                                                # (tail, tip, tex, labelled at the tail)
        LENGTHS.update({x[0]: math.hypot(*x[2]) for x in forces})
        for sym, _, vec, (px, py), k, extra in forces:
            tip = (px + vec[0] * scale, py - vec[1] * scale)
            arrows.append(((px - vec[0] * scale, py + vec[1] * scale), (px, py), tex_of(sym), True) if extra.get("push")
                          else ((px, py), tip, tex_of(sym), False))
        comps = []
        if axes:
            for sym in b["comps"]:
                sym_, vec, at = next((x[0], x[2], x[3]) for x in forces if x[0] == sym)
                for ax, c in zip(axes, "xy"):
                    kk = floor(vec[0] * ax[0] + vec[1] * ax[1]); v = (ax[0] * kk, ax[1] * kk)   # the forces' scale
                    LENGTHS[f"{sym}_{c}"] = abs(kk); comps.append((f"{sym}_{c}", sym, ax)); arrows.append((at, (at[0] + v[0] * scale, at[1] - v[1] * scale), fbd._bold_comp(f"{sym}_{c}"), False))
        motion = []                                                                # velocity and acceleration, beside the body
        v_dir = _unit(along(b["v"], surf)) if b["v"] not in (None, "0", "nolla", "none") else None
        for sym_, dir_, R in ((r"\overline{v}", v_dir, 30), (r"\overline{a}", a_dir if a_dir != (0, 0) else None, 30 + 40 * (v_dir is not None))):
            if dir_ is None: continue
            nx, ny = -dir_[1], dir_[0]
            if ny < 0 or (ny == 0 and nx < 0): nx, ny = -nx, -ny                  # on the body's upper side
            R += math.hypot(W, H) / 2
            st = (cx + nx * R - dir_[0] * 28, cy - ny * R + dir_[1] * 28)
            motion.append((sym_, dir_, st)); arrows.append((st, (st[0] + dir_[0] * 56, st[1] - dir_[1] * 56), sym_, False))
        offs, boxes = _place(arrows, solid, 600, 2 - shift, 458 - shift)          # the same in both passes
        ys += [y for bx in boxes for y in (bx[1], bx[3])] + [y for t, q, *_ in arrows for y in (t[1], q[1])] + [p[1] for p in solid]
        xs += [x for bx in boxes for x in (bx[0], bx[2])] + [x for t, q, *_ in arrows for x in (t[0], q[0])] + [p[0] for p in solid]
        d = fbd.FBD(f, scale, body=(cx, cy, W, H, ang), wrong="drawn lengths: tiny forces enlarged or own horizontal scale (checked above on the true sizes)")
        nf = len(forces)
        for j, (sym, _, vec, at, k, extra) in enumerate(forces): d.force(sym, vec, at, "other" if k == "gravity2" else k, tex=tex_of(sym), lab=offs[j], **extra)
        for j, (cs, of, ax) in enumerate(comps): d.component(cs, of, ax, lab=offs[nf + j])
        if axes:
            ox, oy = cx + (W * 0.75 if two else W * 1.5), cy - H * 1.5
            for (vx, vy), lab in zip(axes, "xy"):
                f.arrow(ox, oy, ox + vx * 36, oy - vy * 36, MUTED, 2, 10); f.tex(ox + vx * 50, oy - vy * 50, lab, "middle", MUTED)
            ys += [oy - 60, oy + 40]; xs += [ox - 40, ox + 60]
        d.draw()
        for j, (sym_, dir_, st) in enumerate(motion): d.motion(sym_, dir_, st, 56, lab=offs[len(offs) - len(motion) + j])
        words.append((surf, [(k.replace("2", ""), sym, math.degrees(math.atan2(vec[1], vec[0]))) for sym, vec, _, _, k, _ in forces], b["a"], b["v"]))
    f.label = describe(words, two, approx, split)
    if _frame is None:                                                             # again, cut to what it holds
        y0, y1 = min(ys) - 8, max(ys) + 8
        x0, x1 = max(0, min(xs) - 8), min(600, max(xs) + 8)
        return draw(spec, fid, (round(y1 - y0), round(y0), (round(x0), round(x1 - x0))))
    svg = f.svg()
    return svg.replace(f'viewBox="0 0 600 {Hfig}"', f'viewBox="{xr[0]} 0 {xr[1]} {Hfig}"', 1) if xr else svg


def _plain(sym):
    """F_mu -> Fμ, T_1 -> T1: a symbol for a screen reader."""
    base, _, sub = sym.partition("_")
    return base + {"mu": "μ"}.get(sub, sub)


def describe(words, two, approx=False, split=False):
    """The figure's text alternative in the page language, from the spec."""
    T = i18n.t; out = [T("fbd.lead_two") if two else T("fbd.lead")] + ([T("fbd.approx")] if approx else []) + ([T("fbd.split")] if split else [])
    for i, (surf, desc, a, v) in enumerate(words):
        part = [T("fbd.body_n", n=i + 1)] if two else []
        if surf not in (None, 0): part.append(T("fbd.slope", deg=f"{abs(round(surf))}"))
        for k, sym, deg in desc:
            part.append(T(f"fbd.kind_{k}", sym=_plain(sym), dir=_dir_words(deg)))
        if v not in (None, "0", "nolla", "none"): part.append(T("fbd.velocity", dir=_dir_words(along(v, surf))))
        if a not in (None, "0", "nolla", "none"): part.append(T("fbd.accel", dir=_dir_words(along(a, surf))))
        out.append(" ".join(part))
    return " ".join(out)


def render(text):
    """Replace each ```voimakuvio block of a markdown text by a token, and give the tokens' figures:
    (text, {token: svg}). The id is a hash of the spec, so the same spec draws the same figure in every language."""
    figs = {}
    def sub(m):
        spec = m.group(1); fid = "fbd-" + hashlib.sha1(spec.encode()).hexdigest()[:8]
        tok = f"FBDTOKEN{len(figs)}X"; figs[tok] = draw(spec, fid)
        return f"\n\n{tok}\n\n"
    return FENCE.sub(sub, text), figs


def restore(html_text, figs):
    for tok, svg in figs.items():
        html_text = re.sub(rf"(?:<p>)?{tok}(?:</p>|<br\s*/?>)?", lambda m, svg=svg: f'<div class="fig fbd">{svg}</div>', html_text)
    return html_text


# ------------------------------------------------------------------------------------------------ the check
STEP = re.compile(r"\*\*(Voimakuvio|Force diagram|Free-body diagram):\*\*")


def missing(text):
    """The "Voimakuvio" steps of a text (a solution) with no drawn diagram after them, before the next step."""
    out = []
    for m in STEP.finditer(text):
        nxt = re.search(r"\n\*\*[^*\n]+:\*\*|\n<!-- vaihe -->|\n### |\n## |\Z", text[m.end():])
        body = text[m.end(): m.end() + (nxt.start() if nxt else len(text))]
        if "```voimakuvio" not in body and "<svg" not in body and "figure" not in body: out.append(text[m.start(): m.start() + 80])
    return out


def sources():
    """Every text that can hold a model solution: exercise solutions, lessons, inquiry and Sovella files."""
    for lang in i18n.languages():
        base = ROOT / "content" / lang
        if not base.is_dir(): continue
        yield from sorted(base.rglob("solutions.md"))
        yield from sorted(base.rglob("lesson.md"))
        yield from sorted(base.rglob("inquiry.json"))


def check():
    import json
    bad = 0; drawn = 0
    for p in sources():
        raw = p.read_text()
        text = raw if p.suffix == ".md" else "\n".join(_strings(json.loads(raw)))
        for frag in missing(text):
            bad += 1; print(f"{p.relative_to(ROOT)}: a Voimakuvio step without a drawn diagram: {frag!r}")
        for m in FENCE.finditer(text):
            try: draw(m.group(1), "check"); drawn += 1
            except Exception as e: bad += 1; print(f"{p.relative_to(ROOT)}: voimakuvio does not draw: {e}")
    print(f"{drawn} force diagrams drawn" + (f", {bad} problems" if bad else ", every Voimakuvio step has its diagram"))
    return bad


def _strings(node):
    if isinstance(node, str): yield node
    elif isinstance(node, dict):
        for v in node.values(): yield from _strings(v)
    elif isinstance(node, list):
        for v in node: yield from _strings(v)


def _add(text, specs, k):
    """text with a diagram after each of its Voimakuvio steps that has none, taking specs from k on: (text, k)."""
    out, i = [], 0
    for m in STEP.finditer(text):
        end = text.find("\n\n", m.end()); end = len(text) if end < 0 else end    # the end of the step's paragraph
        line = text.find("\n**", m.end())
        if 0 <= line < end: end = line                                             # (or of its line, in solutions.md)
        nxt = re.search(r"\*\*[^*\n]+:\*\*", text[end:])
        if "```voimakuvio" in text[end: end + (nxt.start() if nxt else len(text))]: continue
        if k >= len(specs): raise SystemExit(f"more Voimakuvio steps than specs ({len(specs)})")
        out.append(text[i:end] + "\n```voimakuvio\n" + specs[k].strip() + "\n```"); i = end; k += 1
    return "".join(out) + text[i:], k


def insert(specs_file):
    """Put the diagrams of a JSON file {"<path under content/fi>": [spec, ...]} after the Voimakuvio steps of that
    file in every language, in order (a step that already has its diagram keeps it and takes no spec). The k-th spec
    goes to the k-th step without a diagram in each language, so the languages must have the same steps. In a JSON
    file only the strings that change are re-encoded, so the file keeps its layout."""
    import json
    todo = json.loads(pathlib.Path(specs_file).read_text())
    for rel, specs in todo.items():
        for spec in specs: draw(spec, "check")                                    # every spec draws before any file changes
        for lang in i18n.languages():
            p = ROOT / "content" / lang / rel
            if not p.exists(): continue
            raw = p.read_text(); k = 0
            if p.suffix == ".json":
                def sub(m):
                    nonlocal k
                    val = json.loads(m.group(0))
                    if not STEP.search(val): return m.group(0)
                    new, k = _add(val, specs, k)
                    return json.dumps(new, ensure_ascii=False) if new != val else m.group(0)
                new = re.sub(r'"(?:[^"\\]|\\.)*"', sub, raw)
                json.loads(new)
            else: new, k = _add(raw, specs, 0)
            if k != len(specs): raise SystemExit(f"{p.relative_to(ROOT)}: {k} steps without a diagram, {len(specs)} specs")
            p.write_text(new); print(f"{p.relative_to(ROOT)}: {k} diagrams")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "insert":
        insert(sys.argv[2]); sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        p = pathlib.Path(sys.argv[2]); text = p.read_text()
        if p.suffix == ".json":
            import json; text = "\n".join(_strings(json.loads(text)))
        rel = p.resolve().relative_to(ROOT / "content") if (ROOT / "content") in p.resolve().parents else pathlib.Path(p.name)
        out = ROOT / "preview" / ("fbd-" + "-".join(rel.with_suffix("").parts) + ".html"); out.parent.mkdir(exist_ok=True)   # one per file
        figs = []
        for i, m in enumerate(FENCE.finditer(text)):
            try: figs.append(draw(m.group(1), f"fbd-{i}"))
            except ValueError as e: print(f"diagram {i + 1}: {e}"); figs.append(f"<pre>{html.escape(str(e))}</pre>")
        out.write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
                       '<link rel="stylesheet" href="../site/vendor/katex/katex.min.css"><link rel="stylesheet" href="../site/site.css">'
                       '<script src="../site/vendor/katex/katex.min.js"></script><script src="../site/vendor/katex/contrib/auto-render.min.js"></script>'
                       '<body style="max-width:640px;margin:auto">' + "".join(f"<div class='fig fbd' style='border:1px solid #ccc;margin:8px'>{s}</div>" for s in figs)
                       + '<script>renderMathInElement(document.body,{delimiters:[{left:"$",right:"$",display:false}]})</script>')
        print(f"wrote {out.relative_to(ROOT)}: {len(figs)} diagrams")
    else:
        sys.exit(1 if check() else 0)
