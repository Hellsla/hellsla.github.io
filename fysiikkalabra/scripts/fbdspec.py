"""Force diagrams written as a short spec inside a text, drawn by scripts/fbd.py at build time (teacher 2026-10-30:
a model solution whose step is "Voimakuvio" shows a drawn force diagram, never one described in words).

A solution step (exercises/solutions.md, an inquiry task's solution, a Sovella solution) puts the diagram right after
its "**Voimakuvio:**" sentence as a fenced block; the block is the same in every language (symbols and numbers only):

    ```voimakuvio
    pinta 0              the contact surface's angle in degrees (0 level, 30 a slope rising to the right, -30 to the
                         left); leave it out when nothing supports the body (hanging, falling, a lift's rope)
    G 118                the weight, from the centre, straight down (N, or any unit used for every force)
    N 118                the normal force, from the contact surface, perpendicular to it (needs pinta)
    F_mu 30 vasen        friction along the surface, from a bottom corner: vasen | oikea | ylös | alas (ylös = up the slope)
    F 40 30              any other force: its size and direction in degrees (0 right, 90 up) or a word
    F 40 0 työntö        a push: the arrow ends on the body (a hand pushing a box)
    T 40 90              a rope's tension, from the outline, along the rope
    F_v 20 ylös          air resistance; F_n buoyancy (noste); F_j a spring; other symbols are "other" forces
    a oikea              the acceleration's direction (a word or degrees; 0 alone: the body does not accelerate):
                         drawn beside the body in orange and used to check that the forces sum that way
    akselit 0            the x-y axes (x at this angle); `komponentit G` draws G's components on them, dashed
    ---                  a second body of a coupled system (each body gets its own diagram, side by side)
    ```

The diagram is drawn to scale, with the conventions and physics checks of fbd.FBD (weight from the centre, normal force
from the contact surface and perpendicular to it, friction from the surface along it, tension along its rope, the sum
of the forces along the acceleration, components separate and dashed): a spec that breaks one is a build error, so a
wrong diagram never reaches the page. `python scripts/fbdspec.py check` finds every "Voimakuvio" step without a drawn
diagram (CI) and renders every spec; `python scripts/fbdspec.py show <file>` writes the diagrams of one file to
preview/fbd.html for a look."""
import hashlib, html, math, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fbd, figlib, i18n
from figlib import Fig, MUTED, INK

ROOT = pathlib.Path(__file__).resolve().parents[1]
FENCE = re.compile(r"```voimakuvio\n(.*?)```", re.S)
WORDS = {"oikea": 0, "right": 0, "vasen": 180, "left": 180, "ylös": 90, "up": 90, "alas": 270, "down": 270}
KIND = [(r"^G(_|$)", "gravity"), (r"^N(_|$)", "normal"), (r"^F_(\\?mu|μ)", "friction"), (r"^T(_|$)", "tension"),
        (r"^F_v(_|$)", "drag"), (r"^F_n(_|$)", "buoyancy"), (r"^F_j(_|$)", "spring")]
W, H = 120, 70                     # the body rectangle (figure units)


def kind_of(sym):
    return next((k for pat, k in KIND if re.search(pat, sym)), "applied")


def tex_of(sym):
    """G -> \\overline{G}, F_mu -> \\overline{F}_{\\mu}, T_1 -> \\overline{T}_{1}, F_v -> \\overline{F}_{\\text{v}}."""
    base, _, sub = sym.partition("_")
    sub = {"mu": r"\mu", "μ": r"\mu", "v": r"\text{v}", "n": r"\text{n}", "j": r"\text{j}"}.get(sub, sub)
    return rf"\overline{{{base}}}" + (f"_{{{sub}}}" if sub else "")


def parse(spec):
    """[{surface, forces: [(sym, size, deg or word, push)], a, axes, comps}] per body."""
    bodies = []
    for chunk in re.split(r"^---\s*$", spec, flags=re.M):
        b = dict(surface=None, forces=[], a=None, axes=None, comps=[])
        for raw in chunk.splitlines():
            line = raw.split("#")[0].strip()
            if not line: continue
            t = line.split()
            if t[0] == "pinta": b["surface"] = float(t[1])
            elif t[0] == "a": b["a"] = t[1]
            elif t[0] == "akselit": b["axes"] = float(t[1]) if len(t) > 1 else 0.0
            elif t[0] == "komponentit": b["comps"] += t[1:]
            else:
                if len(t) < 2: raise ValueError(f"voimakuvio: '{line}': a force needs its size")
                b["forces"].append((t[0], float(t[1].replace(",", ".")), t[2] if len(t) > 2 else None, "työntö" in t[3:] or "push" in t[3:]))
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


def direction(word, surface):
    """A direction word or degrees -> degrees (y up). Along a slope, ylös/alas/oikea/vasen follow the surface."""
    if word is None: raise ValueError("voimakuvio: give the direction (a word or degrees)")
    if word in WORDS:
        deg = WORDS[word]
        if surface not in (None, 0) and word in ("ylös", "up", "alas", "down", "oikea", "right", "vasen", "left"):
            pass
        return deg
    return float(word.replace(",", "."))


def _dir_words(deg):
    T = i18n.t
    deg %= 360
    for d, k in ((0, "right"), (90, "up"), (180, "left"), (270, "down"), (360, "right")):
        if abs(deg - d) < 1: return T(f"fbd.dir_{k}")
    return T("fbd.dir_deg", deg=f"{round(deg)}")


def draw(spec, fid):
    """The SVG of one spec (one or two bodies side by side)."""
    bodies = parse(spec)
    two = len(bodies) > 1
    big = max(f[1] for b in bodies for f in b["forces"])
    scale = (80 if two else 105) / big
    Hfig = 380
    f = Fig(fid, Hfig, "")
    words = []
    for i, b in enumerate(bodies):
        cx = (150 + 300 * i) if two else 300; cy = Hfig / 2
        surf = b["surface"]; ang = surf if surf is not None else 0.0
        a_word = b["a"]
        a_dir = None
        if a_word is not None:
            if a_word in ("0", "nolla", "none"): a_dir = (0, 0)
            else:
                deg = direction(a_word, surf); along = surf is not None and a_word in ("ylös", "alas", "up", "down") and surf != 0
                if along: deg = ang + (0 if a_word in ("ylös", "up") else 180) if ang >= 0 else ang + (180 if a_word in ("ylös", "up") else 0)
                a_dir = _unit(deg)
        d = fbd.FBD(f, scale, body=(cx, cy, W, H, ang), a_dir=a_dir)
        if surf is not None:                                                     # the surface under the body
            x1, y1 = _local(cx, cy, ang, -W * 0.95, -H / 2); x2, y2 = _local(cx, cy, ang, W * 0.95, -H / 2)
            fbd.ground(f, x1, x2, y1, angle=ang) if abs(ang) < 0.01 else f.line(x1, y1, x2, y2, MUTED, 2.5)
        desc = []
        for sym, size, word, push in b["forces"]:
            k = kind_of(sym); tx = tex_of(sym)
            if k == "gravity":
                vec, at = (0, -size), (cx, cy)
            elif k == "normal":
                if surf is None: raise ValueError(f"voimakuvio: {sym} needs `pinta`")
                nrm = (-math.sin(math.radians(ang)), math.cos(math.radians(ang)))
                vec = (nrm[0] * size, nrm[1] * size)
                at = _local(cx, cy, ang, (0.3 if ang >= 0 else -0.3) * W, -H / 2)
                d.force(sym, vec, at, "normal", surface=ang, tex=tx); desc.append((k, sym, math.degrees(math.atan2(vec[1], vec[0])))); continue
            elif k == "friction":
                if surf is None: raise ValueError(f"voimakuvio: {sym} needs `pinta`")
                t = _unit(ang)
                sgn = {"oikea": 1, "right": 1, "vasen": -1, "left": -1}.get(word)
                if sgn is None: sgn = {"ylös": 1, "up": 1, "alas": -1, "down": -1}.get(word)
                if sgn is None: raise ValueError(f"voimakuvio: {sym}: friction is vasen, oikea, ylös or alas along the surface")
                if word in ("ylös", "up", "alas", "down") and ang < 0: sgn = -sgn          # up a slope rising to the left
                vec = (t[0] * size * sgn, t[1] * size * sgn)
                at = _local(cx, cy, ang, sgn * W / 2, -H / 2)
                d.force(sym, vec, at, "friction", surface=ang, tex=tx); desc.append((k, sym, math.degrees(math.atan2(vec[1], vec[0])))); continue
            else:
                deg = direction(word, surf); u = _unit(deg); vec = (u[0] * size, u[1] * size)
                if push: at = _outline(cx, cy, ang, (-u[0], -u[1]))
                elif k == "buoyancy": at = (cx, cy - 1)  # placeholder, replaced below
                else: at = _outline(cx, cy, ang, u)
                if k == "buoyancy": at = _outline(cx, cy, ang, u)
                extra = {"rope": u} if k == "tension" else {"v_rel": (-u[0], -u[1])} if k == "drag" else {}
                d.force(sym, vec, at, k, push=push, tex=tx, **extra); desc.append((k, sym, deg)); continue
            d.force(sym, vec, at, k, tex=tx); desc.append((k, sym, 270))
        if b["axes"] is not None:
            ax = b["axes"]; ux, uy = _unit(ax), _unit(ax + 90)
            for sym in b["comps"]:
                d.component(f"{sym}_x", sym, ux); d.component(f"{sym}_y", sym, uy)
            ox, oy = cx + (W * 0.95 if not two else W * 0.75), cy - H * 1.9
            for (vx, vy), lab in ((ux, "x"), (uy, "y")):
                f.arrow(ox, oy, ox + vx * 36, oy - vy * 36, MUTED, 2, 10); f.tex(ox + vx * 50, oy - vy * 50, lab, "middle", MUTED)
        d.draw()
        if a_dir not in (None, (0, 0)):
            nx, ny = -a_dir[1], a_dir[0]
            if ny < 0 or (ny == 0 and nx < 0): nx, ny = -nx, -ny                  # beside the body, on its upper side
            R = math.hypot(W, H) / 2 + 34
            sx, sy = cx + nx * R - a_dir[0] * 30, cy - ny * R + a_dir[1] * 30
            d.motion(r"\overline{a}", a_dir, (sx, sy), 60)
        words.append((surf, desc, a_word))
    f.label = describe(words, two)
    svg = f.svg()
    return svg


def describe(words, two):
    """The figure's text alternative in the page language, from the spec."""
    T = i18n.t; out = [T("fbd.lead_two") if two else T("fbd.lead")]
    for i, (surf, desc, a) in enumerate(words):
        part = [T("fbd.body_n", n=i + 1)] if two else []
        if surf not in (None, 0): part.append(T("fbd.slope", deg=f"{abs(round(surf))}"))
        for k, sym, deg in desc:
            part.append(T(f"fbd.kind_{k}", sym=sym.replace("_", " ").replace("mu", "μ"), dir=_dir_words(deg)))
        if a not in (None, "0", "nolla", "none"): part.append(T("fbd.accel", dir=_dir_words(direction(a, surf) if a not in ("ylös", "alas", "up", "down") or not surf else (surf if a in ("ylös", "up") else surf + 180))))
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
        html_text = re.sub(rf"(?:<p>)?{tok}(?:</p>|<br\s*/?>)?", f'<div class="fig fbd">{svg}</div>', html_text)
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
    for lang in i18n.LANGS if hasattr(i18n, "LANGS") else ("fi", "en", "fi-easy"):
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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        p = pathlib.Path(sys.argv[2]); text = p.read_text()
        if p.suffix == ".json":
            import json; text = "\n".join(_strings(json.loads(text)))
        out = ROOT / "preview" / "fbd.html"; out.parent.mkdir(exist_ok=True)
        figs = [draw(m.group(1), f"fbd-{i}") for i, m in enumerate(FENCE.finditer(text))]
        out.write_text('<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="../site/vendor/katex/katex.min.css">'
                       '<body style="max-width:640px;margin:auto">' + "".join(f"<div style='border:1px solid #ccc;margin:8px'>{s}</div>" for s in figs))
        print(f"wrote {out.relative_to(ROOT)}: {len(figs)} diagrams")
    else:
        sys.exit(1 if check() else 0)
