"""Figure helpers for lesson figures (NOTES.md §3): textbook-quality inline SVG with every label in LaTeX.

A lesson keeps the source of its figures in `figures.py` in its folder; `python scripts/figures.py <id>` writes each
figure into lesson.md in place of the `<svg data-fig="<name>" ...>...</svg>` block of the same name, so lesson.md
stays the page's single source and the figure code stays editable. Coordinates are in the 600-unit-wide viewBox.

    from figlib import Fig, Axes, INK, MUTED, HEAT, WATER
    def force_extension():
        f = Fig("fy31-graph", 340, "Kuvaaja mittakaavassa: ...")
        ax = Axes(f, (96, 286), (548, 40), x=(0, 12), y=(0, 5), xticks=[0, 2.5, 5, 10], yticks=[1, 2, 4],
                  xlabel=r"F\\ (\\text{N})", ylabel=r"x\\ (\\text{cm})")
        ax.line([(0, 0), (11, 4.4)], INK)
        for p in [(2.5, 1), (5, 2), (10, 4)]: ax.guide(*p); ax.point(*p)
        f.tex(400, 230, r"\\text{suora origon kautta}")
        return f.svg()
    FIGURES = {"force-extension": force_extension}

Labels: `Fig.tex(x, y, tex, anchor)` puts a KaTeX label whose box is centred vertically on y; anchor start | middle |
end says whether x is its left edge, centre or right edge (like SVG text-anchor). Words go in \\text{}.

Languages: figures.py is written once, in Finnish. For another language `python scripts/figures.py <id> --lang en`
calls set_language() first with content/en/<COURSE>/<id>/figures.json, {Finnish text: translation}: the words of
every \\text{} and every figure's description (Fig label) are looked up there, and the decimal comma {,} becomes the
language's decimal sign. Formulas, symbols and numbers stay as figures.py draws them.
"""
import html, math, re

INK, MUTED, RULE, RULE_LIGHT, WHITE = "#1f2933", "#6b7480", "#c9c2b2", "#e3dccb", "#ffffff"
GLASS, WATER_LIGHT, WATER = "#eef5f9", "#a9d1f0", "#2f74b5"
SAND_LIGHT, SAND, SAND_DARK, GRAIN = "#f1dfb5", "#d9b26a", "#e9c98a", "#a97a35"
HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT = "#ffc078", "#e8590c", "#c92a2a", "#f2a69c", "#1971c2", "#d0e6fb"
ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE = "#c4ccd4", "#8a96a3", "#6c757d", "#b8622d", "#a5d8ff", "#4f8fbf"
GOOD, GOOD_LIGHT = "#2b8a3e", "#b2f2bb"
PAPER = "#f6f1e6"   # the warm paper behind a chapter's opening illustration (Fig(..., hero=True))


TEXTS = {}          # Finnish text -> the text in the language being drawn (set_language)
DECIMAL = "{,}"     # a number's decimal sign in LaTeX: {,} in Finnish
UNITS = set("kg g mg m s N J K Pa kPa MPa kJ MJ W kW Wh kWh h min cm mm km l dl ml dm mol Hz °C".split()) | {""}   # the same in every language
MISSING = []        # Finnish texts drawn without a translation (figures.py reports them)


def set_language(texts, decimal=","):
    global TEXTS, DECIMAL
    TEXTS, DECIMAL = dict(texts), "{,}" if decimal == "," else decimal; MISSING.clear()


def translate(text, tex=True):
    """A label in the language being drawn: in LaTeX the contents of each \\text{} and the decimal comma, a plain
    description as a whole. In Finnish it is the text as it is."""
    if not TEXTS and DECIMAL == "{,}": return text
    def word(t):
        if t.strip() not in UNITS and t not in TEXTS and re.search(r"[A-Za-zÄÖÅäöå]{2,}", t) and t not in MISSING: MISSING.append(t)
        return TEXTS.get(t, t)
    if not tex: return word(text)
    text = re.sub(r"(\\(?:text|mathrm|textsf|textbf)\{)([^{}]*)\}", lambda m: m.group(1) + word(m.group(2)) + "}", text)
    return text.replace("{,}", DECIMAL)


def n(v):
    """A coordinate on a half pixel at most, without trailing zeros."""
    v = round(v * 2) / 2
    return str(int(v)) if v == int(v) else f"{v:.1f}"


def fi(v, digits=None):
    """A number for a LaTeX label: decimal comma as {,}, true minus."""
    s = f"{v:.{digits}f}" if digits is not None else (f"{v:g}" if not float(v).is_integer() else str(int(v)))
    return s.replace(".", DECIMAL)


def visible_len(tex):
    """A rough count of the characters KaTeX draws, for the label box (the layout check measures the real one)."""
    t = re.sub(r"\\(?:text|mathrm|textsf|mathbf)\{([^{}]*)\}", r"\1", tex)
    t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", lambda m: max(m.group(1), m.group(2), key=len), t)
    t = re.sub(r"\\[a-zA-Z]+", "x", t)
    return len(re.sub(r"[{}^_\\ ]", "", t)) + t.count("\\ ") * 0.3


class Fig:
    def __init__(self, fid, height, label, width=600, size=24, hero=False, anim=False):
        """hero: the chapter's opening illustration, 1200 wide, full column width under the Miksi question (site.css .fig-hero).
        anim: an animated figure (work queue 8f, pilot fy3-8): the drawing is the still, and the groups that vibrate()
        opens move only by the CSS of site.css "Animated figures", which runs while lesson.js part 7b plays it."""
        self.fid, self.w, self.h, self.label, self.size, self.hero = fid, width, height, translate(label, tex=False), size, hero
        self.anim = anim
        self.defs, self.body = [], []
        self._open, self._kf = [], []          # the closers end() writes, and the @keyframes motion() generated

    # drawing
    def add(self, s): self.body.append(s); return self
    def defs_add(self, s): self.defs.append(s); return self

    def line(self, x1, y1, x2, y2, color=INK, w=2, dash=None, cap="butt"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return self.add(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{color}" stroke-width="{w:g}" stroke-linecap="{cap}"{d}/>')

    def path(self, d, fill="none", stroke=None, w=2, extra=""):
        s = f' stroke="{stroke}" stroke-width="{w:g}"' if stroke else ""
        return self.add(f'<path d="{d}" fill="{fill}"{s} stroke-linejoin="round"{(" " + extra) if extra else ""}/>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=2, rx=0, extra=""):
        s = f' stroke="{stroke}" stroke-width="{sw:g}"' if stroke else ""
        r = f' rx="{rx:g}"' if rx else ""
        return self.add(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}"{r} fill="{fill}"{s}{(" " + extra) if extra else ""}/>')

    def circle(self, cx, cy, r, fill=INK, stroke=None, sw=2):
        s = f' stroke="{stroke}" stroke-width="{sw:g}"' if stroke else ""
        return self.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r:g}" fill="{fill}"{s}/>')

    def arrow(self, x1, y1, x2, y2, color=INK, w=3, head=14):
        """A straight arrow from (x1, y1) to the tip (x2, y2): a shaft and a filled head (NOTES 3)."""
        import math
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * head, y2 - uy * head
        hw = head * 0.45
        self.line(x1, y1, bx + ux, by + uy, color, w)
        return self.path(f"M{n(x2)},{n(y2)} L{n(bx - uy * hw)},{n(by + ux * hw)} L{n(bx + uy * hw)},{n(by - ux * hw)} Z", fill=color)

    def block_arrow(self, x1, y1, x2, y2, fill, shaft=16, head=34, headlen=28):
        """A wide filled arrow (energy or heat flow, a force with a width that means its size)."""
        import math
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        px, py = -uy, ux
        bx, by = x2 - ux * headlen, y2 - uy * headlen
        pts = [(x1 + px * shaft / 2, y1 + py * shaft / 2), (bx + px * shaft / 2, by + py * shaft / 2), (bx + px * head / 2, by + py * head / 2),
               (x2, y2), (bx - px * head / 2, by - py * head / 2), (bx - px * shaft / 2, by - py * shaft / 2), (x1 - px * shaft / 2, y1 - py * shaft / 2)]
        return self.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", fill=fill)

    def vibrate(self, amp, phase=0.0, period=2.0):
        """Open a group that vibrates horizontally about where it is drawn, ±amp figure units, one cycle in `period`
        seconds, `phase` a fraction of the cycle (0.5: the opposite way); close it with end(). Still unless played."""
        assert self.anim, "vibrate() needs Fig(..., anim=True)"
        return self.add(f'<g class="fa-vib" style="--fa-a:{amp:g}px;--fa-t:{period:g}s;--fa-d:{-phase * period:g}s">')

    def end(self):
        """Close the group the last vibrate(), oscillate(), travel(), drift(), orbit() or collide() opened."""
        return self.add(self._open.pop() if self._open else "</g>")

    # shared animation primitives (work queue 8f, all CSS: no script loop, no canvas). Each opens a group; draw what
    # moves, then end(). The group is drawn where it stands in the still: every cycle starts and ends there (the
    # keyframes are relative to the drawn position, 0 at t=0), so the still is the same SVG as without anim and
    # playing, pausing, reduced motion and print never jump. site.css "Animated figures" runs `.fa-k` while
    # lesson.js part 7b has marked the figure .is-playing.
    def motion(self, frames, period, start=0.0, rotate_about=None, clip=None):
        """The generic primitive: frames = [(t, dx, dy, rot_deg, opacity), ...] with t in 0..1 of one cycle (the first
        frame at t=0 is the drawn position: dx=dy=rot=0, opacity 1; the last at t=1 the same for a loop), the
        transform relative to the drawn position. start: a fraction of the cycle the animation is already into when
        played (a negative delay, for a travelling pulse drawn mid-way: its frames then begin where it is drawn).
        rotate_about: (cx, cy) the centre of the rotation, figure units. clip: (x, y, w, h) a window the moving
        content is cut to (a wave leaving the picture)."""
        assert self.anim, "animation primitives need Fig(..., anim=True)"
        name = f"fa-{self.fid}-{len(self._kf)}"
        steps = []
        for fr in frames:
            t, dx, dy, rot, op = tuple(fr) + (None, 0, 0, 0, 1)[len(fr):]
            q = lambda v: f"{v:.2f}".rstrip("0").rstrip(".") if abs(v) > 5e-3 else "0"      # n() rounds to half a pixel: too coarse for a path
            tf = f"translate({q(dx)}px,{q(dy)}px)" + (f" rotate({q(rot)}deg)" if rot else "")
            steps.append(f"{round(t * 100, 3):g}%{{transform:{tf};opacity:{op:g}}}")
        self._kf.append(f"@keyframes {name}{{{''.join(steps)}}}")
        org = f";transform-origin:{n(rotate_about[0])}px {n(rotate_about[1])}px;transform-box:view-box" if rotate_about else ""
        g = (f'<g class="fa-k" style="--fa-n:{name};--fa-t:{period:g}s;--fa-d:{-start * period:g}s{org}">')
        if clip:
            cid = f"{name}-clip"
            self.defs_add(f'<clipPath id="{cid}"><rect x="{n(clip[0])}" y="{n(clip[1])}" width="{n(clip[2])}" height="{n(clip[3])}"/></clipPath>')
            self.add(f'<g clip-path="url(#{cid})">'); self._open.append("</g></g>")
        else:
            self._open.append("</g>")
        return self.add(g)

    def oscillate(self, amp, phase=0.0, period=2.0, axis="x", samples=24):
        """Sinusoidal vibration along "x" or "y", d(t) = amp·sin(2π(t/T + phase)) − amp·sin(2π·phase): about a centre
        amp·sin(2π·phase) away from where the group is drawn, so any phase starts at the drawn position. For the
        points of a travelling wave (phase = −x/λ), and for the projection of an orbit (see orbit_phase)."""
        a0 = amp * math.sin(2 * math.pi * phase)
        fr = []
        for i in range(samples + 1):
            t = i / samples
            d = amp * math.sin(2 * math.pi * (t + phase)) - a0
            fr.append((t, d if axis == "x" else 0, d if axis == "y" else 0, 0, 1))
        return self.motion(fr, period)

    def travel(self, dx, period, dy=0.0, start=0.0, clip=None):
        """A travelling wave or pulse: the group moves dx (and dy) figure units in `period` seconds, linearly, then
        starts again. A periodic wave drawn longer than its window (clip) with dx = one wavelength repeats exactly:
        the curve is the same after one period, so the wave seems to travel and no point of the rope moves along it.
        A single pulse: dx = the distance the pulse runs, start = the fraction of that run it is already into where
        it is drawn (the loop then starts where it is drawn and jumps back to its source at the end). Mark one
        particle of the medium (oscillate) so the reader sees the matter stay."""
        return self.motion([(0, 0, 0, 0, 1), (1, dx, dy, 0, 1)], period, start, clip=clip)

    def orbit(self, cx, cy, period=4.0, clockwise=False):
        """The group turns once about (cx, cy) in `period` seconds, counter-clockwise on the screen unless clockwise.
        Draw the moving point (and its radius) inside; a label that must stay upright goes outside the group."""
        sign = 1 if clockwise else -1
        fr = [(i / 8, 0, 0, sign * 45 * i, 1) for i in range(9)]
        return self.motion(fr, period, rotate_about=(cx, cy))

    def project(self, R, theta0, period=4.0, axis="x", clockwise=False):
        """The projection of orbit()'s point on the x or y axis: simple harmonic motion with amplitude R, the same period
        and phase. theta0 is the orbit point's start angle in degrees (counter-clockwise from +x, as in a textbook).
        Draw the projected point at x = cx + R·cos θ0 (axis x) or y = cy − R·sin θ0 (axis y)."""
        th = math.radians(theta0) / (2 * math.pi)
        if not clockwise: amp, ph = (R, th + 0.25) if axis == "x" else (-R, th)
        else: amp, ph = (-R, -(th + 0.25)) if axis == "x" else (R, -th)
        return self.oscillate(amp, ph, period, axis)

    def drift(self, x0, y0, box, vx, vy, period, radius=0.0):
        """A particle bouncing about in box = (left, top, right, bottom) between elastic walls (angle of incidence =
        angle of reflection), starting from (x0, y0) with the velocity (vx, vy) figure units per second. The path is
        closed: it must return to the start with the same velocity after `period` seconds (drift_track checks and
        raises), so choose speeds with bounce_speed(). `radius` keeps the particle's edge, not its centre, in the box."""
        return self.motion(drift_track(x0, y0, box, vx, vy, period, radius), period)

    def collide(self, tracks_frames, period, start=0.0):
        """One body of a collision: frames from collision_frames(). Hold at the end, then fade out and back in at the
        start; the still is the 'before' picture."""
        return self.motion(tracks_frames, period, start)

    def styles(self):
        """The generated @keyframes of this figure, written into its <defs> by svg()."""
        return "<style>" + "".join(self._kf) + "</style>" if self._kf else ""

    def tex(self, x, y, tex, anchor="start", color=INK, size=None, w=None, bg=False):
        """A LaTeX label centred vertically on y; x is its left edge, centre or right edge (anchor). bg puts the
        figure's white under the label, for a label that sits on gridlines."""
        size = size or self.size; tex = translate(tex)
        tall = re.search(r"\\d?frac|\\sqrt|\\sum|\\int", tex)
        h = round(size * (2.4 if tall else 1.2))            # about the rendered height: check_layout.py measures the box
        w = w or round(visible_len(tex) * size * 0.52 + 8)
        x0 = x if anchor == "start" else x - w / 2 if anchor == "middle" else x - w
        just = {"start": "flex-start", "middle": "center", "end": "flex-end"}[anchor]
        style = f"display:flex;align-items:center;justify-content:{just};height:100%;font-size:{size:g}px" + (f";color:{color}" if color != INK else "")
        return self.add(f'<foreignObject x="{n(x0)}" y="{n(y - h / 2)}" width="{n(w)}" height="{h}" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="{style}">{f'<span style="background:{WHITE};padding:0 5px;border-radius:3px">${tex}$</span>' if bg else f'${tex}$'}</div></foreignObject>')

    def svg(self, name=None):
        cls = " ".join(c for c, on in (("fig-hero", self.hero), ("fig-anim", self.anim)) if on)
        attrs = (f' data-fig="{name}"' if name else "") + (f' class="{cls}"' if cls else "")
        defs = f"\n  <defs>{self.styles()}{''.join(self.defs)}</defs>" if (self.defs or self._kf) else ""
        body = "\n  ".join(self.body)
        return (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.label, quote=True)}"{attrs} '
                f'style="max-width:100%;font-size:{self.size}px">{defs}\n  {body}\n</svg>')


def bounce_speed(box_len, period, k, radius=0.0):
    """The speed along one axis that bounces a particle k times back and forth over the room (box_len − 2·radius) in
    `period` seconds and brings it home with the same velocity: v = 2·L·k/T. A different k per particle gives each its
    own speed and a different run of wall hits; k = 0 keeps it still along that axis."""
    return 2 * (box_len - 2 * radius) * k / period


def drift_track(x0, y0, box, vx, vy, period, radius=0.0):
    """The frames of a particle bouncing in box between elastic walls (a perfectly reflecting wall turns the normal
    component of the velocity round, the tangential one is kept; no collisions between the particles: the ideal gas).
    Returns motion() frames (t, dx, dy) with a frame at every wall hit, so the linear stretches between are exact.
    The path must be closed after `period` seconds (v·T a whole number of 2L, see bounce_speed) or this raises."""
    left, top, right, bottom = box
    axes = []
    for u0, v, lo, hi in ((x0, vx, left + radius, right - radius), (y0, vy, top + radius, bottom - radius)):
        L = hi - lo
        assert L > 0 and lo - 1e-9 <= u0 <= hi + 1e-9, "drift: the start is outside the room"
        turns = v * period / (2 * L)
        if abs(turns - round(turns)) > 1e-6:
            raise ValueError(f"drift: the path is not closed (v·T/2L = {turns:.4f}); use bounce_speed()")
        axes.append((u0 - lo, v, L))

    def fold(u, v, L, t):
        m = (u + v * t) % (2 * L)
        return m if m <= L else 2 * L - m
    ts = {0.0, 1.0}
    for u, v, L in axes:
        if v == 0: continue
        for j in range(-int(abs(u + v * period) // L) - 2, int(abs(u + v * period) // L) + 3):     # the walls at j·L of the unfolded line
            t = (j * L - u) / v / period
            if 1e-9 < t < 1 - 1e-9: ts.add(round(t, 9))
    fr = []
    for t in sorted(ts):
        fr.append((t,) + tuple(fold(u, v, L, t * period) - u for u, v, L in axes))
    return fr


def collision_frames(x1, x2, w1, w2, v1, v2, m1, m2, e=1.0, move=0.9):
    """Two bodies on a line, body 1 left of body 2 (centres x1 < x2, widths w1, w2, velocities v1 > v2 so they meet),
    elastic (e = 1) or with the coefficient of restitution e (0: they stick). Returns (frames1, frames2, info) for
    collide(): the bodies run towards each other for 35 % of the cycle's motion, meet, and run on with the velocities
    that momentum conservation and e give; they rest at the end (hold, fade out, back in at the start). `info` has
    both final velocities and the contact time as a fraction of the cycle (momentum before = after, checked in the
    tests). The figure is the model's own units: dx is in the figure units the bodies were given in."""
    assert v1 > v2, "the bodies must approach each other"
    gap = (x2 - w2 / 2) - (x1 + w1 / 2)
    tc = gap / (v1 - v2)                                       # model time of the contact
    u1 = ((m1 - e * m2) * v1 + (1 + e) * m2 * v2) / (m1 + m2)
    u2 = ((m2 - e * m1) * v2 + (1 + e) * m1 * v1) / (m1 + m2)
    scale = tc / 0.35                              # model seconds per whole cycle
    tcf = tc / scale
    def pos(v_before, v_after, t):
        tm = t * scale
        return v_before * tm if tm <= tc else v_before * tc + v_after * (tm - tc)
    out = []
    for vb, va in ((v1, u1), (v2, u2)):
        end = move
        fr = [(0, 0, 0, 0, 1), (tcf, vb * tc, 0, 0, 1), (end, pos(vb, va, end), 0, 0, 1),
              (0.96, pos(vb, va, end), 0, 0, 1), (0.98, pos(vb, va, end), 0, 0, 0), (0.985, 0, 0, 0, 0), (1, 0, 0, 0, 1)]
        out.append(fr)
    return out[0], out[1], {"u1": u1, "u2": u2, "contact": tcf, "model_seconds": scale}


class Axes:
    """A graph: origin and top-right corner of the plot area in figure units, data ranges, ticks with LaTeX numbers,
    gridlines on every tick, axes with filled arrowheads and the axis titles at the arrow ends (NOTES 3, Graphs)."""

    def __init__(self, fig, origin, corner, x, y, xticks, yticks, xlabel, ylabel, grid=True, xfmt=None, yfmt=None,
                 arrow_room=26, origin_label=True, x_at=None, ticks_below=False):
        self.f, (self.x0, self.y0), (self.x1, self.y1) = fig, origin, corner
        self.xr, self.yr = x, y
        X, Y = self.X, self.Y
        xa = self.y0 if x_at is None else Y(x_at)          # the time axis where the value is x_at (0 for a signed graph)
        if grid:
            for t in xticks:
                if t != x[0]: fig.line(X(t), self.y0, X(t), self.y1, RULE_LIGHT, 1.5)
            for t in yticks:
                if t != y[0] and (x_at is None or t != x_at): fig.line(self.x0, Y(t), self.x1, Y(t), RULE_LIGHT, 1.5)
        ax_end, ay_end = self.x1 + arrow_room, self.y1 - arrow_room
        if x_at is not None: fig.line(self.x0, self.y0, self.x0, xa, INK, 2.5)   # the y axis below the time axis
        fig.arrow(self.x0 - 1, xa, ax_end, xa, INK, 2.5, 13)
        fig.arrow(self.x0, (self.y0 if x_at is None else xa) + 1, self.x0, ay_end, INK, 2.5, 13)
        xf = xfmt or (lambda v: fi(v)); yf = yfmt or (lambda v: fi(v))
        for t in xticks:
            if t == x[0]: continue
            fig.line(X(t), xa, X(t), xa + 7, INK, 2)
            if xf(t) != "": fig.tex(X(t), (self.y0 + 24) if (x_at is None or ticks_below) else xa - 22, xf(t), "middle")   # above a signed graph's axis     # an empty format: a tick and gridline without a number
        for t in yticks:
            if t == y[0] and x_at is None: continue
            fig.line(self.x0 - 7, Y(t), self.x0, Y(t), INK, 2)
            if yf(t) != "": fig.tex(self.x0 - 12, Y(t), yf(t), "end")
        if origin_label and x[0] == 0 and y[0] == 0:
            fig.tex(self.x0 - 10, self.y0 + 20, "0", "end")
        # the axis titles beyond the arrow tips, where no data, tick or gridline can reach them: leave about
        # 80 units right of the x arrow and 30 above the y arrow
        fig.tex(ax_end + 6, xa, xlabel, "start") if xlabel else None
        if ylabel:
            # a graph that reaches the top of its figure has no room above the y arrow: the title then goes beside the
            # arrow tip, on white, instead of being cut by the frame (teacher 2026-11-11, illustration audit group A)
            tall = re.search(r"\\d?frac|\\sqrt|\\sum|\\int", ylabel)
            ink = fig.size * (1.05 if tall else 0.42)      # how far the glyphs reach above the label's centre line
            if ay_end - 16 - ink >= 0: fig.tex(self.x0 - 10, ay_end - 16, ylabel, "start")
            else: fig.tex(self.x0 + 14, max(ay_end + 6, ink + 3), ylabel, "start", bg=True)

    def X(self, v): return self.x0 + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.x1 - self.x0)
    def Y(self, v): return self.y0 - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.y0 - self.y1)

    def line(self, pts, color=INK, w=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{n(self.X(a))},{n(self.Y(b))}" for a, b in pts)
        return self.f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}/>')

    def curve(self, fn, a, b, color=INK, w=3, steps=120, dash=None):
        return self.line([(a + (b - a) * i / steps, fn(a + (b - a) * i / steps)) for i in range(steps + 1)], color, w, dash)

    def point(self, a, b, color=INK, r=6.5):
        return self.f.circle(self.X(a), self.Y(b), r, color, WHITE, 2)

    def guide(self, a, b, color=MUTED):
        """Dashed lines from a point to both axes, where the text reads a value off the graph."""
        self.f.line(self.X(a), self.Y(b), self.X(a), self.y0, color, 1.5, "6 5")
        return self.f.line(self.x0, self.Y(b), self.X(a), self.Y(b), color, 1.5, "6 5")

    def area(self, pts, fill, opacity=0.35):
        p = " ".join(f"{n(self.X(a))},{n(self.Y(b))}" for a, b in pts)
        return self.f.add(f'<polygon points="{p}" fill="{fill}" fill-opacity="{opacity:g}"/>')
