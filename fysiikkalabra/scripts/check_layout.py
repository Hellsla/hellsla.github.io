"""Phone-width layout check of built lesson pages. Usage: python scripts/check_layout.py [lesson-id] [--width 360]

Opens each page in preview/ (or site/) at a phone viewport and reports every element that is wider
than its box: display formulas (.katex-display), tables, inline SVG figures and the page itself.
A display formula that scrolls sideways on a phone is a web-designer FAIL, so writers run this
before review (NOTES.md section 1). Exit status 1 if anything overflows.

--dir site|preview picks the folder (default: preview if built, else site; CI passes --dir site).
tests/layout-known.json lists overflows that are known and accepted for now, as {"<lesson>": ["<start of the
formula's LaTeX>", ...]}. They are printed as KNOWN and do not fail the run; any other overflow does.
Widths depend on the installed fonts (the CI runner's are wider than a sandbox's), so an entry that does not overflow
on this machine is only a NOTE, not a failure. Remove an entry when the lesson is fixed."""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
ROOT = pathlib.Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith("--")]
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 360
args = [a for a in args if a != str(width)]
folder = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else None
args = [a for a in args if a != folder]
only = args[0] if args else None
OUT = ROOT / (folder or ("preview" if (ROOT / "preview" / "index.html").exists() else "site"))
KNOWN = {}
if (ROOT / "tests/layout-known.json").exists():
    KNOWN = {k: list(v) for k, v in json.loads((ROOT / "tests/layout-known.json").read_text()).items() if not k.startswith("_")}

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
used = set()
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
        for f in hard:
            f['known'] = any(f['what'] == 'formula' and f['text'].startswith(k) and not used.add((lid, k))
                             for k in KNOWN.get(lid, []))
        if any(not f['known'] for f in hard):
            bad += 1
            print(f"FAIL {OUT.name}/{lid} at {width} px")
            for f in found:
                print(f"  {f['what']:8} {f['over']:4} px too wide  {f['text']}" + ("  (warning: scrolls)" if f['what'] == 'table' else "")
                      + ("  KNOWN (tests/layout-known.json)" if f.get('known') else ""))
        elif hard:
            print(f"KNOWN {OUT.name}/{lid} at {width} px: " + ", ".join(f"{f['what']} +{f['over']} px" for f in hard) + " (tests/layout-known.json)")
        else:
            print(f"OK   {OUT.name}/{lid} at {width} px" + (f"  ({len(found)} wide table, scrolls)" if found else ""))
    b.close()
if not only:
    for lid, texts in KNOWN.items():
        for k in texts:
            if (lid, k) not in used:
                print(f"NOTE tests/layout-known.json: {lid} '{k[:40]}' does not overflow here (font dependent, or fixed: then remove the entry)")
sys.exit(1 if bad else 0)
