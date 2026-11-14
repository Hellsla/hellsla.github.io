"""Headless check of the text in every simulation's picture on a short laptop screen (teacher 2026-11-14,
docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md). Usage: python scripts/test_sim_text.py [page-id ...]

At 1366×650 the picture narrows to about 384 px (site.css .lab-side .sim-canvas), and a sketch that sizes its text by the
width of #sim-root drew it at about 7 px. templates/sim-embed.js now gives the sketch the picture's width, so the text
grows as it does on a phone. A page passes when every label the sketch draws over the canvas (.sim-tex, the KaTeX layer)
is at least MIN_PX on the screen, none leaves the canvas and no two overlap. One line per page, as test_sims.py:
PASS|FAIL <site|preview>/<page>, details on failure. test_sims.py and check_layout.py stay at 800 and 900 px high."""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
from courses import ROOT
import i18n
only = set(sys.argv[1:])
OUT = ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"
VIEW = {"width": 1366, "height": 650}
MIN_PX = 10

JS = """() => {
  const c = document.querySelector('#sim-root canvas'); if (!c) return {err: 'no canvas'};
  c.scrollIntoView({block: 'center'});
  const cb = c.getBoundingClientRect(), out = [], boxes = [];
  for (const el of document.querySelectorAll('#sim-root .sim-tex')) {
    if (el.style.visibility === 'hidden' || el.style.display === 'none') continue;
    const r = el.getBoundingClientRect(); if (!r.width) continue;
    const t = (el.textContent || '').trim().slice(0, 24), px = parseFloat(getComputedStyle(el).fontSize);
    out.push({t, px});
    boxes.push({t, x0: r.left, y0: r.top, x1: r.right, y1: r.bottom});
  }
  const bad = [];
  for (const b of boxes) if (b.x0 < cb.left - 1 || b.y0 < cb.top - 1 || b.x1 > cb.right + 1 || b.y1 > cb.bottom + 1) bad.push(`"${b.t}" leaves the picture`);
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) { const a = boxes[i], b = boxes[j];
    if (a.x0 < b.x1 - 1 && b.x0 < a.x1 - 1 && a.y0 < b.y1 - 1 && b.y0 < a.y1 - 1) bad.push(`"${a.t}" overlaps "${b.t}"`); }
  return {width: Math.round(cb.width), labels: out, bad};
}"""

fails = 0
with sync_playwright() as pw:
    b = launch(pw)
    for f in sorted(OUT.glob("*.html")) + [f for lang in i18n.languages()[1:] for f in sorted((OUT / lang).glob("*.html"))]:
        if only and f.stem not in only: continue
        if 'id="sim-root"' not in f.read_text(): continue
        key = f"{OUT.name}/{f.relative_to(OUT).with_suffix('').as_posix()}"
        page = b.new_page(viewport=VIEW); errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(f.as_uri())
        page.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()")
        try: page.wait_for_function("window.simState !== undefined", timeout=15000)
        except Exception: pass
        page.wait_for_timeout(1500)
        r = page.evaluate(JS); page.close()
        bad = list(errors) + ([r["err"]] if "err" in r else [])
        if "err" not in r:
            small = sorted({(l["t"], round(l["px"], 1)) for l in r["labels"] if l["px"] < MIN_PX}, key=lambda x: x[1])
            bad += [f'"{t}" is {p} px (under {MIN_PX})' for t, p in small[:6]] + r["bad"][:6]
            note = f"{len(r['labels'])} labels, picture {r['width']} px, smallest {min([l['px'] for l in r['labels']] or [0]):.1f} px"
        else: note = ""
        print(("PASS " if not bad else "FAIL ") + key + (" " + note if note else ""))
        for x in bad: print("     " + x)
        fails += bool(bad)
sys.exit(1 if fails else 0)
