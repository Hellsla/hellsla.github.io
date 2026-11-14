"""The equals signs of a calculation stand in one column, at 360 and 1280 px (teacher 2026-11-13, "aina pitäisi tasata
kaavat s.e. = kohdistettu"). Opens built pages (site/, or preview/ with --preview) and, in each calculation named below
(an aligned display block or a .eq-chain), compares the x of the leading relation sign of every row that starts with one:
they must agree within 1 px. Usage: python scripts/test_eqalign.py [--preview]"""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
OUT = ROOT / ("preview" if "--preview" in sys.argv else "site")
CASES = [("fy3-5", "110"), ("fy3-4", "117"), ("fy3-6", "1257"), ("fy3-7", "2 343")]   # a text inside the calculation
JS = """(key) => {
  const out = [];
  for (const c of document.querySelectorAll('main .katex-display, main .eq-chain')) {
    if (!c.checkVisibility() || !c.textContent.includes(key)) continue;
    // the first relation sign of each visual row: group the relation glyphs by their top, take the leftmost of each
    const rels = [...c.querySelectorAll('.mrel')].map(e => e.getBoundingClientRect()).filter(r => r.width);
    const rows = {};
    for (const r of rels) { const k = Math.round(r.top / 6); (rows[k] = rows[k] || []).push(r.left); }
    const xs = Object.values(rows).map(v => Math.min(...v));
    out.push(xs);
  }
  return out;
}"""
bad = 0
with sync_playwright() as p:
    b = launch(p)
    for width in (360, 1280):
        pg = b.new_page(viewport={"width": width, "height": 900})
        for page, key in CASES:
            pg.goto((OUT / f"{page}.html").as_uri()); pg.wait_for_timeout(1200)
            pg.evaluate("document.querySelectorAll('details').forEach(d => d.open = true); document.querySelectorAll('[hidden]').forEach(e => e.hidden = false)")
            pg.wait_for_timeout(1500)
            for xs in pg.evaluate(JS, key):
                ok = len(xs) >= 1 and max(xs) - min(xs) <= 1
                if not ok: bad += 1
                print("OK  " if ok else "FAIL", f"{page} at {width} px: relation x {[round(x) for x in xs]}")
        pg.close()
    b.close()
sys.exit(1 if bad else 0)
