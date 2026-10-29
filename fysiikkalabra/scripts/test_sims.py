"""Headless check of every built simulation. Usage: python scripts/test_sims.py [lesson-id]

A sim passes when the page loads with no console errors, window.simState exists after 1.5 s, every assertion in
tests/sims/<id>.json holds (|expr - expected| <= tol * max(1, |expected|); "setup" is JS run before the expression;
the assertions are written against the Finnish page, so a page in another language gets the load and the sweep),
and the generic sweep passes: at 360, 390 and 1280 px every combination of each slider's min/mid/max, each select
option and each checkbox state is set, two frames are drawn, and then every number in simState must be finite and,
when the sim exposes label boxes (simState.labels = [{s, x0, y0, x1, y1}, ...] in canvas coordinates), no label may
leave the canvas (600×400, or 600 wide and taller when the sim stacks its panels on a narrow screen) or overlap
another one. Sims without label boxes get the finiteness sweep only, with a
note. The KaTeX labels sim-embed.js draws over the canvas (p.text of a $…$ string) are checked the same way from the
page: each stays inside the canvas and none overlaps another. One line per sim; details only on failure."""
import json, sys, pathlib, itertools
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
import i18n
only = sys.argv[1] if len(sys.argv) > 1 else None
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
      const cw = root.querySelector('canvas'), dpr = window.devicePixelRatio || 1;   // 600×400, or taller when a sim stacks its panels on a phone (2026-10-29)
      const W = cw ? cw.width / dpr : 600, H = cw ? cw.height / dpr : 400;
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
        if only and lid != only: continue
        if 'id="sim-root"' not in page_file.read_text(): continue   # a lesson page with a simulation, wherever its sim.js lives
        page = b.new_page(viewport={"width": 1280, "height": 900})   # fresh page: no leftover listeners
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
        bad = []
        if state is not None:
            for c in checks:
                if c.get("setup"): page.evaluate(c["setup"]); page.wait_for_timeout(200)
                got = page.evaluate(c["expr"])
                if got is None or abs(got - c["expected"]) > c.get("tol", 0.01) * max(1, abs(c["expected"])):
                    bad.append(f"{c['expr'][:160]} = {got} (expected {c['expected']})")
        page.close()
        sweep_ok, sweep_note, sweep_bad = sweep(b, page_file) if state is not None else (True, "", [])
        ok = not errors and state is not None and not bad and sweep_ok
        fails += not ok
        print("PASS" if ok else "FAIL", f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()}", "no simState (p5 not loaded?)" if state is None else ("assertions on the Finnish page" if translated else f"{len(checks)} assertions") + f", {sweep_note}")
        for line in errors[:3] + bad + sweep_bad: print("     " + line)
    b.close()
sys.exit(1 if fails else 0)
