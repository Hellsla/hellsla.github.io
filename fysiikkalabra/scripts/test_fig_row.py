"""Test that a figure beside its text never squeezes the text (fy3-6 and fy7-14 at 1280 px, 2026-11-18).

build.py fig_rows sets a figure and the paragraph it explains as one unit, and from 62.5 rem site.css puts the two side
by side (.fig-row.side: a 38 rem text column and a 26 rem figure column). Inside the Teoria box (details.theory-box, one
reading column, about 616 px inside) the grid shared that width, the text got half of it (288 px) and its formula spilled
over; the main push-to-main smoke test does not open those pages, so main went red unseen.

Every built page that has a `.fig-row.side`, at 1280 and 1920 px with every box open:
  - a side-by-side unit's text column is at least 30 rem wide (the width fig_side assumes), wherever the unit stands;
  - a unit inside a details box stands under its text, not beside it;
  - no text column of a figure unit has content wider than itself.
Usage: python scripts/test_fig_row.py [page-id ...]"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _browser import launch
from playwright.sync_api import sync_playwright

SITE = HERE.parent / "site"
only = set(sys.argv[1:])
pages = [p for p in sorted(SITE.glob("*.html")) + sorted(SITE.glob("*/*.html"))
         if "-" in p.stem and (not only or p.stem in only) and "fig-row side" in p.read_text(encoding="utf-8")]

JS = """() => {
  const out = [];
  for (const r of document.querySelectorAll('.fig-row')) {
    if (!r.checkVisibility()) continue;
    const t = r.querySelector(':scope > .fig-text'), side = r.classList.contains('side');
    const box = r.closest('details');
    if (t.scrollWidth > t.clientWidth + 1) out.push(`text column ${t.clientWidth} px has content ${t.scrollWidth} px wide: "${t.textContent.trim().slice(0, 50)}"`);
    if (side && getComputedStyle(r).display === 'grid' && t.clientWidth < 30 * 16) out.push(`side-by-side text column only ${t.clientWidth} px: "${t.textContent.trim().slice(0, 50)}"`);
    if (box && getComputedStyle(r).display === 'grid') out.push(`a unit inside a closed-box (details) is beside its text: "${t.textContent.trim().slice(0, 50)}"`);
  }
  return out; }"""

bad = 0
with sync_playwright() as pw:
    b = launch(pw)
    page = b.new_page(viewport={"width": 1280, "height": 800})
    for f in pages:
        for width in (1280, 1920):
            page.set_viewport_size({"width": width, "height": 800})
            page.goto(f.as_uri(), wait_until="domcontentloaded")
            page.evaluate("document.fonts.ready.then(() => true)")
            page.wait_for_timeout(150)
            found = page.evaluate(JS)
            page.evaluate("document.querySelectorAll('details').forEach((d) => { d.open = true; })")
            page.wait_for_timeout(150)
            found += [x for x in page.evaluate(JS) if x not in found]
            tag = f"{f.relative_to(SITE).with_suffix('')} at {width} px"
            if found:
                bad += 1
                print(f"FAIL {tag}", flush=True)
                for x in found: print("  " + x, flush=True)
    b.close()
print(f"{'FAIL' if bad else 'ok  '} figure units on {len(pages)} pages at 1280 and 1920 px" + (f", {bad} failing" if bad else ""))
sys.exit(1 if bad else 0)
