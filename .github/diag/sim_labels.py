"""Diagnostics for a simulation whose KaTeX labels overlap on the CI machine but not elsewhere (fy1-1, 2026-11-11).

  python ../.github/diag/sim_labels.py fy1-1        (run in fysiikkalabra/, after python scripts/build.py --all)

Runs scripts/test_sims.py itself, unchanged on disk: this script reads its source, adds reporting to it in memory and
executes it with the given page ids. Nothing about what the test accepts changes: the same pages, widths, control
combinations, frames, tolerances and messages. Added: for the first overlapping label pairs their texts, boxes, font
sizes, the width the label was laid out with (simState.labels) against the width it is drawn with, the view and the
frame; the browser, Playwright, viewport, device scale factor and fonts; and a screenshot of the simulation taken
when the sweep reports the overlap (DIAG_DIR, default ./diag). The sweep of a width stops at its first overlap, so
that the screenshot shows that state; test_sims.py as CI runs it goes on. If test_sims.py changes so that a patch
below no longer applies, this script stops with an assertion instead of reporting something else.
"""
import json, os, pathlib, subprocess, sys

ROOT = pathlib.Path.cwd()
SRC = ROOT / "scripts" / "test_sims.py"
DIAG_DIR = pathlib.Path(os.environ.get("DIAG_DIR", "diag")).resolve()
DIAG_DIR.mkdir(parents=True, exist_ok=True)
src = SRC.read_text(encoding="utf-8")


def patch(old, new):
    global src
    assert src.count(old) == 1, f"scripts/test_sims.py changed: expected exactly one\n{old}"
    src = src.replace(old, new)


# 1. the sweep (JavaScript in the page): record the overlapping pair and stop this width's sweep there
patch("  const bad = []; let states = 0, hasBoxes = false, hasTex = false;\n",
      """  const bad = []; let states = 0, hasBoxes = false, hasTex = false;
  const diag = [];
  const one = (e, R, k) => { const r = e.getBoundingClientRect(), S = window.simState || {}, lay = (Array.isArray(S.labels) ? S.labels : []).filter((a) => a && a.s === e.__s);
    const size = parseFloat(e.style.fontSize) / k;
    return { text: e.__s, box: { left: +(r.left - R.left).toFixed(2), top: +(r.top - R.top).toFixed(2), width: +r.width.toFixed(2), height: +r.height.toFixed(2) },
      fontSizeCss: e.style.fontSize, computedFont: getComputedStyle(e).fontSize + ' ' + getComputedStyle(e).fontFamily.slice(0, 40), cachedWidthCss: e.__w, color: e.style.color,
      katexFont: (() => { const q = e.querySelector('.katex .mord, .katex'); return q ? getComputedStyle(q).fontFamily.slice(0, 60) : null; })(),
      laidOut: lay.map((a) => ({ x0: +a.x0.toFixed(2), x1: +a.x1.toFixed(2), y0: +a.y0.toFixed(2), y1: +a.y1.toFixed(2), widthSketch: +(a.x1 - a.x0).toFixed(2), widthCssExpected: +((a.x1 - a.x0) * k).toFixed(2) })),
      sketchTextSize: +size.toFixed(3), measuredNowSketch: window.flSimTextWidth ? +window.flSimTextWidth(e.__s, size).toFixed(2) : null,
      measuredNowCssExpected: window.flSimTextWidth ? +(window.flSimTextWidth(e.__s, size) * k).toFixed(2) : null }; };
  const record = (c, a, b, cv, R) => { const k = cv.clientWidth / 600, S = window.simState || {};
    diag.push({ combo: c, state: states, canvas: { clientWidth: cv.clientWidth, clientHeight: cv.clientHeight, width: cv.width, height: cv.height, cssPerSketch: +k.toFixed(4) },
      viewport: [innerWidth, innerHeight], dpr: devicePixelRatio, simRootWidth: root.clientWidth,
      view: { L: S.L, target: S.tavoite, nVis: S.nVis, visible: S.nakyvat }, labelsDrawn: root.querySelectorAll('.sim-tex').length,
      fontsLoaded: [...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family + ' ' + f.weight + ' ' + f.style).join('; '),
      fontsNotLoaded: [...document.fonts].filter((f) => f.status !== 'loaded' && /KaTeX/.test(f.family)).map((f) => f.family + ' ' + f.weight + ' ' + f.style + ' ' + f.status).join('; '),
      a: one(a, R, k), b: one(b, R, k) });
    if (window.simAdapter && window.simAdapter.pause) { try { window.simAdapter.pause(); } catch (e) { /* the screenshot then shows a later frame */ } } };
""")
patch("""bad.push(`${where} "${B[i][0].__s}" overlaps "${B[j][0].__s}"`); }""",
      """{ bad.push(`${where} "${B[i][0].__s}" overlaps "${B[j][0].__s}"`); if (!diag.length) record(c, B[i][0], B[j][0], cv, R); } }""")
# a dry run (DIAG_FORCE=<state number>): record the first two labels of that state though nothing overlaps, to see the report
patch("    if (bad.length > 40) break;\n",
      "    if (!diag.length && window.__diagForce && states >= window.__diagForce && cv && T.length > 1) { const R = cv.getBoundingClientRect(); record(c, T[0], T[1], cv, R); }\n"
      "    if (bad.length > 40 || diag.length) break;\n")
if os.environ.get("DIAG_FORCE"):
    patch("""        page = b.new_page(viewport={"width": w, "height": 900})
        page.goto(page_file.as_uri())
""", f"""        page = b.new_page(viewport={{"width": w, "height": 900}})
        page.add_init_script("window.__diagForce = {int(os.environ['DIAG_FORCE'])};")
        page.goto(page_file.as_uri())
""")
patch("  return {states, hasBoxes, hasTex, bad: [...new Set(bad)].slice(0, 8),",
      "  return {diag, states, hasBoxes, hasTex, bad: [...new Set(bad)].slice(0, 8),")

# 2. the sweep (Python): print the record and take the screenshot before the page closes
patch("""        r = page.evaluate(SWEEP_JS, cs[:MAX_STATES])
        page.close()
""", """        r = page.evaluate(SWEEP_JS, cs[:MAX_STATES])
        if r.get("diag"):
            import json as _json
            _name = f"{page_file.parent.name if page_file.parent.name in ('en', 'fi-easy') else 'fi'}-{page_file.stem}-{w}"
            print(f"DIAG {_name} " + _json.dumps(r["diag"][0], ensure_ascii=False))
            print(f"DIAG {_name} env " + _json.dumps({"browser": b.version, "userAgent": page.evaluate("navigator.userAgent"), "viewport": page.viewport_size,
                                                       "dpr": page.evaluate("devicePixelRatio")}, ensure_ascii=False))
            try:
                _shot = _DIAG_DIR / f"{_name}.png"
                (page.locator("#sim").first if page.locator("#sim").count() else page).screenshot(path=str(_shot))
                print(f"DIAG {_name} screenshot {_shot.name}")
            except Exception as e: print(f"DIAG {_name} screenshot failed: {str(e)[:200]}")
        page.close()
""")

# the machine: Playwright, fonts
try:
    from importlib.metadata import version
    print("DIAG playwright", version("playwright"))
except Exception as e: print("DIAG playwright version unknown:", e)
for cmd in (["fc-match", "serif"], ["fc-match", "sans-serif"], ["fc-match", "KaTeX_Main"], ["sh", "-c", "fc-list | wc -l"], ["sh", "-c", "fc-list : family | sort -u | head -60 | tr '\\n' ';'"]):
    try: print("DIAG", " ".join(cmd), "->", subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()[:1500])
    except Exception as e: print("DIAG", " ".join(cmd), "failed:", str(e)[:120])
sys.stdout.flush()

sys.argv = [str(SRC)] + sys.argv[1:]
exec(compile(src, str(SRC), "exec"), {"__name__": "__main__", "__file__": str(SRC), "_DIAG_DIR": DIAG_DIR})
