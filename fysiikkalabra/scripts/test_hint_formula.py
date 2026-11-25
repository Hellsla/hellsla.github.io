"""A long inline formula in the hint of a long task's part scrolls inside the hint box and never widens the page
(shared layout fix, 2026-11-25: fy9-sailymislait en, E_loss = 1/2 Mv^2 - 1/2 (M+m)v'^2, the page was 10 px too wide at 360 px
because the part's grid column grew with the formula). Opens the first hint of fy9-liike with a long formula put in it,
at 360, 390 and 1280 px. Usage: python scripts/test_hint_formula.py   (needs site/ or preview/ built: build.py fy9-liike)"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from playwright.sync_api import sync_playwright
from _browser import launch
ROOT = HERE.parent
page = next((p for p in (ROOT / "site" / "fy9-liike.html", ROOT / "preview" / "fy9-liike.html") if p.is_file()), None)
if not page: sys.exit("build fy9-liike first (python scripts/build.py fy9-liike)")
JS = r"""() => {
  const det = document.querySelector('ol.parts>li>.hints details'), d = det.querySelector(':scope>div'); det.open = true;
  d.innerHTML = '<p>Energy: <span style="font-size:1.05em">\\(E_{loss}=\\tfrac12 Mv^2-\\tfrac12 (M+m)v\'^2\\)</span></p>';
  renderMathInElement(d, {delimiters: [{left: '\\(', right: '\\)', display: false}]});
  return new Promise(r => setTimeout(() => {
    const k = d.querySelector('.katex'), box = d.getBoundingClientRect(), kr = k.getBoundingClientRect();
    r({doc: document.documentElement.scrollWidth, win: innerWidth, boxRight: box.right, kRight: kr.right, wide: k.classList.contains('kx-wide')});
  }, 700));
}"""
bad = []
with sync_playwright() as p:
    b = launch(p)
    for w in (360, 390, 1280):
        pg = b.new_page(viewport={"width": w, "height": 800})
        pg.goto(page.as_uri()); pg.wait_for_timeout(600)
        r = pg.evaluate(JS)
        ok = r["doc"] <= r["win"] and r["kRight"] <= r["boxRight"] + 1
        print(("ok   " if ok else "FAIL ") + f"{w} px: page {r['doc']}/{r['win']}, formula right {r['kRight']:.0f}, hint box right {r['boxRight']:.0f}, scrolls on its own line: {r['wide']}")
        if not ok: bad.append(w)
    b.close()
sys.exit(1 if bad else 0)
