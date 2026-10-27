"""Layout check of built lesson pages. Usage: python scripts/check_layout.py [lesson-id] [--width 360] [--site]

Opens each page in preview/ (or site/) at a viewport (360 by default; CI also runs 1280 and 1920) and reports every
element that is wider than its box: display formulas (.katex-display), inline formulas that cannot wrap (a long
\dfrac), tables, inline SVG figures and the page
itself, every text label inside an inline SVG that overlaps another label or leaves the figure (NOTES 3), and on a
wide screen a column whose content spills into its neighbour and text wider than a reading column (44rem, about
80 characters; CLAUDE.md "Lesson page"). Every <details> is opened first, so the solutions behind the
Näytä ratkaisu buttons are measured too.
A display formula that scrolls sideways on a phone is a web-designer FAIL, so writers run this
before review (NOTES.md section 1). Exit status 1 if anything overflows."""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
args = [a for a in sys.argv[1:] if not a.startswith("--")]
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 360
args = [a for a in args if a != str(width)]
only = args[0] if args else None
OUT = ROOT / "site" if "--site" in sys.argv else ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # --site: the published pages (CI)

JS = """() => {
  const out = [];
  document.querySelectorAll('details').forEach((d) => { d.open = true; });   // solutions and optional boxes are measured open
  const el = document.scrollingElement;
  if (el.scrollWidth > el.clientWidth + 1) out.push({what: 'page', over: el.scrollWidth - el.clientWidth, text: ''});
  for (const d of document.querySelectorAll('.katex-display')) {
    if (d.scrollWidth > d.clientWidth + 1) {
      const ann = d.querySelector('annotation');
      out.push({what: 'formula', over: d.scrollWidth - d.clientWidth, text: ann ? ann.textContent.slice(0, 90) : ''});
    }
  }
  for (const k of document.querySelectorAll('main .katex')) {
    if (k.closest('.katex-display, table, svg, #sim-root')) continue;
    const box = k.closest('p, li, .steps, .stage') || k.parentElement;
    const over = Math.round(k.getBoundingClientRect().right - Math.min(box.getBoundingClientRect().right, document.documentElement.clientWidth));
    if (over > 1) { const ann = k.querySelector('annotation'); out.push({what: 'formula', over, text: 'inline, cannot wrap: ' + (ann ? ann.textContent.slice(0, 70) : '')}); }
  }
  for (const t of document.querySelectorAll('table')) {
    if (t.closest('#sim-root')) continue;
    const box = t.parentElement;
    if (t.scrollWidth > box.clientWidth + 1) out.push({what: 'table', over: t.scrollWidth - box.clientWidth, text: t.innerText.slice(0, 60)});
  }
  for (const s of document.querySelectorAll('main svg')) {
    const r = s.getBoundingClientRect();
    if (r.right > document.documentElement.clientWidth + 1) out.push({what: 'svg', over: Math.round(r.right - document.documentElement.clientWidth), text: s.getAttribute('aria-label') || ''});
    const T = [...s.querySelectorAll('text'), ...s.querySelectorAll('foreignObject')].map((t) => ({t: t.textContent.trim().slice(0, 40), b: (t.querySelector('.katex, div') || t).getBoundingClientRect()})).filter((x) => x.t);
    for (const x of T) if (x.b.left < r.left - 1 || x.b.right > r.right + 1 || x.b.top < r.top - 1 || x.b.bottom > r.bottom + 1)
      out.push({what: 'svg-text', over: Math.round(Math.max(r.left - x.b.left, x.b.right - r.right, r.top - x.b.top, x.b.bottom - r.bottom)), text: `"${x.t}" leaves the figure`});
    for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) { const a = T[i].b, b = T[j].b;
      const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (ox > 1 && oy > 1) out.push({what: 'svg-text', over: Math.round(Math.min(ox, oy)), text: `"${T[i].t}" overlaps "${T[j].t}"`}); }
  }
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  for (const c of document.querySelectorAll('.act-grid > *, .lab > *, .fig-row > *, .intro-row > *'))
    if (c.scrollWidth > c.clientWidth + 1) out.push({what: 'column', over: c.scrollWidth - c.clientWidth, text: c.className});
  for (const t of document.querySelectorAll('main p, main li')) {
    if (!t.offsetParent || t.closest('#sim-root, .katex-display, table')) continue;
    const w = t.getBoundingClientRect().width;
    if (w > 44 * rem + 1) { out.push({what: 'text', over: Math.round(w - 44 * rem), text: `line length: "${t.textContent.trim().slice(0, 50)}"`}); break; }
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
