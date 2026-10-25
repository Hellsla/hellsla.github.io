"""Phone-width layout check of built lesson pages. Usage: python scripts/check_layout.py [lesson-id] [--width 360] [--site]

Opens each page in preview/ (or site/) at a phone viewport and reports every element that is wider
than its box: display formulas (.katex-display), tables, inline SVG figures and the page itself.
A display formula that scrolls sideways on a phone is a web-designer FAIL, so writers run this
before review (NOTES.md section 1). Exit status 1 if anything overflows."""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
ROOT = pathlib.Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith("--")]
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 360
args = [a for a in args if a != str(width)]
only = args[0] if args else None
OUT = ROOT / "site" if "--site" in sys.argv else ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # --site: the published pages (CI)

JS = """() => {
  const out = [];
  const el = document.scrollingElement;
  if (el.scrollWidth > el.clientWidth + 1) out.push({what: 'page', over: el.scrollWidth - el.clientWidth, text: ''});
  for (const d of document.querySelectorAll('.katex-display')) {
    if (d.scrollWidth > d.clientWidth + 1) {
      const ann = d.querySelector('annotation');
      out.push({what: 'formula', over: d.scrollWidth - d.clientWidth, text: ann ? ann.textContent.slice(0, 90) : ''});
    }
  }
  for (const t of document.querySelectorAll('table')) {
    if (t.closest('#sim-root')) continue;
    const box = t.parentElement;
    if (t.scrollWidth > box.clientWidth + 1) out.push({what: 'table', over: t.scrollWidth - box.clientWidth, text: t.innerText.slice(0, 60)});
  }
  for (const s of document.querySelectorAll('main svg')) {
    const r = s.getBoundingClientRect();
    if (r.right > document.documentElement.clientWidth + 1) out.push({what: 'svg', over: Math.round(r.right - document.documentElement.clientWidth), text: s.getAttribute('aria-label') || ''});
  }
  return out;
}"""

bad = 0
with sync_playwright() as pw:
    b = launch(pw)
    for page_file in sorted(OUT.glob("*.html")):
        lid = page_file.stem
        if only and lid != only: continue
        if lid == "index" or "-" not in lid: continue
        page = b.new_page(viewport={"width": width, "height": 800})
        page.goto(page_file.as_uri())
        page.wait_for_timeout(400)
        found = page.evaluate(JS)
        page.close()
        hard = [f for f in found if f['what'] != 'table']   # tables scroll sideways by design (NOTES 1)
        if hard:
            bad += 1
            print(f"FAIL {OUT.name}/{lid} at {width} px")
            for f in found:
                print(f"  {f['what']:8} {f['over']:4} px too wide  {f['text']}" + ("  (warning: scrolls)" if f['what'] == 'table' else ""))
        else:
            print(f"OK   {OUT.name}/{lid} at {width} px" + (f"  ({len(found)} wide table, scrolls)" if found else ""))
    b.close()
sys.exit(1 if bad else 0)
