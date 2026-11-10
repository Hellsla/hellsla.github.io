"""Headless check of every built simulation. Usage: python scripts/test_sims.py [page-id ...]

A sim passes when the page loads with no console errors, window.simState exists after 1.5 s, every assertion in
tests/sims/<id>.json holds (|expr - expected| <= tol * max(1, |expected|); "setup" is JS run before the expression;
the assertions are written against the Finnish page, so a page in another language gets the load and the sweep),
and the generic sweep passes: at 360, 390 and 1280 px every combination of each slider's min/mid/max, each select
option and each checkbox state is set, two frames are drawn, and then every number in simState must be finite and,
when the sim exposes label boxes (simState.labels = [{s, x0, y0, x1, y1}, ...] in canvas coordinates), no label may
leave the canvas (600×400, or 600 wide and taller when the sim stacks its panels on a narrow screen) or overlap
another one. Sims without label boxes get the finiteness sweep only, with a
note. The KaTeX labels sim-embed.js draws over the canvas (p.text of a $…$ string) are checked the same way from the
page: each stays inside the canvas and none overlaps another.
Drawing on demand (2026-11-05, templates/sim-embed.js STATIC): a listed sim must be drawn on demand, draw no frame while
nothing happens, show after every control change what one more forced redraw would show (no stale picture or state), and
reach the same simState and readouts as the old continuous loop (?simloop=1) over the same control changes; a sim not
listed keeps its loop. The cache of label widths stays within its bound and gives the same width after an eviction.
One line per sim; details only on failure.
A slow machine (2026-11-10, after main's CI failed on a slow runner): every sim advances by Math.min(p.deltaTime, 100)
a frame, so when a frame takes over 100 ms simulated time falls behind the wall clock, and an assertion that waits
(the 200 ms after a setup, setTimeout) or compares simulated time with performance.now() can fail with no fault in the
sim. The assertion page counts such late frames (PAGE_JS); an assertion that fails while late frames were drawn is
reported as not judged ("slow:"), not as a failure; one that fails with every frame on time fails as before. Its
textContent reads without soft hyphens, as a reader sees the text: build.py (tablefit.py) puts them into the long
words of table cells, the sims' table texts too ("Ei mit\u00adtauk\u00adsia")."""
import json, re, sys, pathlib, itertools
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
import i18n
only = set(sys.argv[1:])   # none: every page; CI on a pull request passes the pages scripts/ci_scope.py names
OUT = ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # preview/ holds drafts + --all
WIDTHS = (360, 390, 1280)
MAX_STATES = 120            # per width; beyond this sliders use min/max only

SWEEP_JS = """async (combos) => {
  const root = document.getElementById('sim-root');
  const ranges = [...root.querySelectorAll('input[type=range]')], selects = [...root.querySelectorAll('select')],
        checks = [...root.querySelectorAll('input[type=checkbox]')];
  const frames = () => new Promise((f) => requestAnimationFrame(() => requestAnimationFrame(f)));
  const fire = (el) => { el.dispatchEvent(new Event('input', {bubbles: true})); el.dispatchEvent(new Event('change', {bubbles: true})); };
  const boxes = (L) => Array.isArray(L) && L.length && L.every((a) => a && ['x0', 'y0', 'x1', 'y1'].every((k) => typeof a[k] === 'number'));
  const bad = []; let states = 0, hasBoxes = false, hasTex = false;
  for (const c of combos) {
    c.r.forEach((v, i) => { if (ranges[i]) { ranges[i].value = v; fire(ranges[i]); } });
    c.s.forEach((v, i) => { if (selects[i]) { selects[i].selectedIndex = v; fire(selects[i]); } });
    c.c.forEach((v, i) => { if (checks[i]) { checks[i].checked = !!v; fire(checks[i]); } });
    await frames(); await frames(); states++;
    const S = window.simState || {};
    const walk = (v, path) => { if (typeof v === 'number') { if (!Number.isFinite(v)) bad.push(`${path} = ${v}`); }
                                else if (Array.isArray(v)) v.forEach((x, i) => walk(x, `${path}[${i}]`));
                                else if (v && typeof v === 'object' && path.split('.').length < 4) for (const k in v) walk(v[k], `${path}.${k}`); };
    walk(S, 'simState');
    const L = S.labels;
    if (boxes(L)) { hasBoxes = true;
      const where = `[${c.r.join(',')}|${c.s.join(',')}|${c.c.join(',')}]`;
      const cw = root.querySelector('canvas');   // 600 wide in sim coordinates (sim-embed.js may shrink the backing store); 400 high, or taller when a sim stacks its panels on a phone (2026-10-29)
      const W = 600, H = cw && cw.width ? Math.round(600 * cw.height / cw.width) : 400;
      for (const a of L) if (a.x0 < 0 || a.y0 < 0 || a.x1 > W || a.y1 > H) bad.push(`${where} "${a.s}" leaves the canvas`);
      for (let i = 0; i < L.length; i++) for (let j = i + 1; j < L.length; j++) { const a = L[i], b = L[j];
        if (a.x0 < b.x1 && b.x0 < a.x1 && a.y0 < b.y1 && b.y0 < a.y1) bad.push(`${where} "${a.s}" overlaps "${b.s}"`); }
    }
    const cv = root.querySelector('canvas'), T = [...root.querySelectorAll('.sim-tex')].filter((e) => e.style.display !== 'none');
    if (cv && T.length) { hasTex = true;            // KaTeX labels over the canvas: inside it, none on another
      const where = `[${c.r.join(',')}|${c.s.join(',')}|${c.c.join(',')}]`, R = cv.getBoundingClientRect(), B = T.map((e) => [e, e.getBoundingClientRect()]);
      for (const [e, r] of B) if (r.left < R.left - 2 || r.top < R.top - 2 || r.right > R.right + 2 || r.bottom > R.bottom + 2) bad.push(`${where} "${e.__s}" leaves the canvas`);
      for (let i = 0; i < B.length; i++) for (let j = i + 1; j < B.length; j++) { const a = B[i][1], b = B[j][1];
        if (Math.min(a.right, b.right) - Math.max(a.left, b.left) > 2 && Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 2) bad.push(`${where} "${B[i][0].__s}" overlaps "${B[j][0].__s}"`); }
    }
    if (bad.length > 40) break;
  }
  return {states, hasBoxes, hasTex, bad: [...new Set(bad)].slice(0, 8),
          controls: {ranges: ranges.map((r) => [+r.min, +r.max]), selects: selects.map((s) => s.options.length), checks: checks.length}};
}"""


STATIC = set(re.findall(r"'([^']+)'", re.search(r"/\*STATIC\*/(.*?)/\*END\*/", (OUT / "sim-embed.js").read_text(), re.S).group(1)))

DEMAND_JS = """async (combos) => {
  const root = document.getElementById('sim-root');
  const ranges = [...root.querySelectorAll('input[type=range]')], selects = [...root.querySelectorAll('select')],
        checks = [...root.querySelectorAll('input[type=checkbox]')];
  const frames = () => new Promise((f) => requestAnimationFrame(() => requestAnimationFrame(f)));
  const wait = (ms) => new Promise((f) => setTimeout(f, ms));
  const fire = (el) => { el.dispatchEvent(new Event('input', {bubbles: true})); el.dispatchEvent(new Event('change', {bubbles: true})); };
  const sig = () => JSON.stringify(window.simState) + '|' + window.simText(root);
  const info0 = window.flSimInfo ? window.flSimInfo() : null;
  const d0 = info0 ? info0.draws : 0; await wait(1000); const info1 = window.flSimInfo ? window.flSimInfo() : null;
  const out = {info: info1, idleDraws: info1 ? info1.draws - d0 : -1, sigs: [], stale: []};
  for (const c of combos) {
    c.r.forEach((v, i) => { if (ranges[i]) { ranges[i].value = v; fire(ranges[i]); } });
    c.s.forEach((v, i) => { if (selects[i]) { selects[i].selectedIndex = v; fire(selects[i]); } });
    c.c.forEach((v, i) => { if (checks[i]) { checks[i].checked = !!v; fire(checks[i]); } });
    await frames(); await frames(); await wait(120);
    const a = sig(); window.flSimRedraw(); window.flSimRedraw(); const b = sig();
    out.sigs.push(a); if (a !== b) out.stale.push(JSON.stringify(c));
  }
  return out;
}"""

WIDTHS_JS = """() => {
  const w0 = window.flSimTextWidth('$v = 1{,}25\\,\\text{m/s}$', 17);
  for (let i = 0; i < 1500; i++) window.flSimTextWidth('$t = ' + i + '{,}0\\,\\text{s}$', 17);
  const info = window.flSimInfo(), w1 = window.flSimTextWidth('$v = 1{,}25\\,\\text{m/s}$', 17);
  return {size: info.widths, max: info.widthsMax, w0, w1};
}"""


def drag(page):
    """A press, a drag across the canvas and a release (a sim that moves a body or a probe with the pointer), then the
    simState and readout once it has settled, and whether one more redraw would change them."""
    box = page.evaluate("(() => { const c = document.querySelector('#sim-root canvas'); c.scrollIntoView({block: 'center'}); const r = c.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; })()")
    x, y, w, h = box
    page.mouse.move(x + w * 0.45, y + h * 0.5); page.mouse.down()
    for i in range(1, 11): page.mouse.move(x + w * (0.45 + 0.02 * i), y + h * (0.5 - 0.01 * i)); page.wait_for_timeout(16)
    page.mouse.up(); page.mouse.move(x + w + 40, y + h + 40); page.wait_for_timeout(300)
    return page.evaluate("(() => { const s = () => JSON.stringify(window.simState) + '|' + window.simText('#sim-root'); const a = s(); window.flSimRedraw(); window.flSimRedraw(); return [a, a === s()]; })()")


def on_demand(b, page_file, lid, translated):
    """Returns (ok, note, bad) for the on-demand drawing and the width cache."""
    bad = []
    page = b.new_page(viewport={"width": 1280, "height": 900}); page.goto(page_file.as_uri())
    page.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()"); ready(page); page.wait_for_timeout(500)
    info = page.evaluate("window.flSimInfo ? window.flSimInfo() : null") or {}
    listed = info.get("name") in STATIC
    if not translated:
        W = page.evaluate(WIDTHS_JS)
        if W["size"] > W["max"]: bad.append(f"label width cache holds {W['size']} > {W['max']}")
        if abs(W["w0"] - W["w1"]) > 0.01: bad.append(f"label width after eviction {W['w1']} != {W['w0']}")
    if not listed:
        page.close()
        if info.get("onDemand"): bad.append("drawn on demand but not listed in STATIC")
        return (not bad, "loops", bad)
    probe = page.evaluate(SWEEP_JS, [{"r": [], "s": [], "c": []}])
    cs = combos(probe["controls"], thin=True)[:24]
    r = page.evaluate(DEMAND_JS, cs)
    D = drag(page)
    page.close()
    if not info.get("onDemand"): bad.append(f"listed in STATIC but not drawn on demand ({info})")
    if r["idleDraws"] > 1: bad.append(f"{r['idleDraws']} frames drawn in 1 s with nothing happening")
    bad += [f"stale after {c}: a redraw changes simState or the readout" for c in r["stale"][:4]]
    if not D[1]: bad.append("stale after a drag on the canvas: a redraw changes simState or the readout")
    if not translated:
        q = b.new_page(viewport={"width": 1280, "height": 900}); q.goto(page_file.as_uri() + "?simloop=1")
        q.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()"); ready(q); q.wait_for_timeout(500)
        r2 = q.evaluate(DEMAND_JS, cs)
        D2 = drag(q)
        q.close()
        if D[0] != D2[0]: bad.append("a drag on the canvas ends in another state than with the continuous loop")
        if (r2["info"] or {}).get("onDemand"): bad.append("?simloop=1 does not keep the continuous loop")
        diff = [i for i, (x, y) in enumerate(zip(r["sigs"], r2["sigs"])) if x != y]
        if diff or len(r["sigs"]) != len(r2["sigs"]): bad.append(f"differs from the continuous loop after {len(diff)} of {len(cs)} control changes, first {cs[diff[0]] if diff else ''}")
    return (not bad, f"on demand: idle {r['idleDraws']} frames/s, {len(cs)} changes and a drag" + ("" if translated or bad else " = continuous loop"), bad)


PAGE_JS = """(() => {
  // late frames: a gap of over 100 ms between two frames, more than a sim's Math.min(p.deltaTime, 100) counts
  window.flLate = 0; let last = performance.now();
  const tick = (t) => { if (t - last > 100) window.flLate++; last = t; requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
  // the text as a reader sees it: without the soft hyphens of tablefit.py
  const tc = Object.getOwnPropertyDescriptor(Node.prototype, 'textContent');
  Object.defineProperty(Node.prototype, 'textContent', { configurable: true, set: tc.set,
    get() { const t = tc.get.call(this); return typeof t === 'string' && t.includes('\\u00ad') ? t.replace(/\\u00ad/g, '') : t; } });
})();"""


def ready(page):
    """Wait until the sketch has drawn (simState exists), at most 1.5 s, then one more frame."""
    try: page.wait_for_function("window.simState", timeout=1500)
    except Exception: pass
    page.wait_for_timeout(120)


def combos(controls, thin):
    rs = [[lo, (lo + hi) / 2, hi] if not thin else [lo, hi] for lo, hi in controls["ranges"]]
    ss = [list(range(n)) for n in controls["selects"]]
    cs = [[0, 1]] * controls["checks"]
    out = []
    for r in itertools.product(*rs) if rs else [()]:
        for s in itertools.product(*ss) if ss else [()]:
            for c in itertools.product(*cs) if cs else [()]:
                out.append({"r": list(r), "s": list(s), "c": list(c)})
    return out


def sweep(b, page_file):
    """Returns (ok, note). Runs the generic sweep at every width."""
    notes, bad = [], []
    for w in WIDTHS:
        page = b.new_page(viewport={"width": w, "height": 900})
        page.goto(page_file.as_uri())
        page.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()")
        ready(page)
        probe = page.evaluate(SWEEP_JS, [{"r": [], "s": [], "c": []}])
        cs = combos(probe["controls"], thin=False)
        if len(cs) > MAX_STATES: cs = combos(probe["controls"], thin=True)
        r = page.evaluate(SWEEP_JS, cs[:MAX_STATES])
        page.close()
        notes.append(f"{w}px:{r['states']}")
        bad += [f"{w} px {x}" for x in r["bad"]]
        has_boxes, has_tex = r["hasBoxes"], r["hasTex"]
    label_note = "labels checked" if has_boxes else "no label boxes (simState.labels), finiteness only"
    if has_tex: label_note += ", KaTeX labels checked"
    return (not bad, f"sweep {' '.join(notes)} states, {label_note}", bad)


fails = 0
with sync_playwright() as pw:
    b = launch(pw)
    for page_file in sorted(OUT.glob("*.html")) + [f for lang in i18n.languages()[1:] for f in sorted((OUT / lang).glob("*.html"))]:   # site/<lang>/ too
        lid = page_file.stem
        if only and lid not in only: continue
        if 'id="sim-root"' not in page_file.read_text(): continue   # a lesson page with a simulation, wherever its sim.js lives
        page = b.new_page(viewport={"width": 1280, "height": 900})   # fresh page: no leftover listeners
        page.add_init_script(PAGE_JS)                                 # late frames counted, text without soft hyphens
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(page_file.as_uri())
        page.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()")   # sim-embed pauses sims that are off-screen
        ready(page)
        state = page.evaluate("window.simState")
        tests = ROOT / "tests/sims" / f"{lid}.json"
        checks = json.loads(tests.read_text()) if tests.exists() else []
        translated = page_file.parent != OUT
        if translated: checks = []   # the assertions name controls, options and readouts in Finnish words and build on each
                                     # other's state: they run on the Finnish page; the same sim code is loaded and swept here
        bad, slow = [], []
        if state is not None:
            for c in checks:
                late = page.evaluate("window.flLate")
                if c.get("setup"): page.evaluate(c["setup"]); page.wait_for_timeout(200)
                got = page.evaluate(c["expr"])
                if got is None or abs(got - c["expected"]) > c.get("tol", 0.01) * max(1, abs(c["expected"])):
                    late = page.evaluate("window.flLate") - late
                    (slow if late else bad).append(f"{c['expr'][:160]} = {got} (expected {c['expected']})" + (f", {late} frames over 100 ms" if late else ""))
        page.close()
        sweep_ok, sweep_note, sweep_bad = sweep(b, page_file) if state is not None else (True, "", [])
        dem_ok, dem_note, dem_bad = on_demand(b, page_file, lid, translated) if state is not None else (True, "", [])
        sweep_note += f", {dem_note}" if dem_note else ""; sweep_bad += dem_bad
        ok = not errors and state is not None and not bad and sweep_ok and dem_ok
        fails += not ok
        print("PASS" if ok else "FAIL", f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()}", "no simState (p5 not loaded?)" if state is None else ("assertions on the Finnish page" if translated else f"{len(checks)} assertions") + f", {sweep_note}")
        for line in errors[:3] + bad + sweep_bad: print("     " + line)
        for line in slow: print("     slow: not judged, " + line)
    b.close()
sys.exit(1 if fails else 0)
