"""Read aloud (templates/readaloud.js, teacher 2026-11-03: "ääneenluku", and "näyttää missä kohtaa tekstiä mennään").
Usage: python scripts/test_readaloud.py [site] [page ...]

Static, every page of the site built from templates/lesson.html (lessons, Sovella itsenäisesti, investigations, TVT
guides, course units) in every language: readaloud.js is loaded and the page's string block carries lang "speech".
In a browser, with a stand-in for the browser's voice (speechSynthesis is replaced by a script that reports every
word and ends each sentence; a headless browser has no voices), on one lesson per language, a TVT guide, an
investigation and a course unit (or the pages named):
  - the Kuuntele button is under the title in the page's language, and nothing is spoken before it is pressed
  - formulas are spoken as words (lang "speech"): a fixed set of TeX gives the expected Finnish and English
  - reading goes block by block in page order; the title is read first; a closed box, a hidden worked-example step,
    a figure and a simulation are not read; the block being read is marked and the sentence and the word are
    highlighted (CSS Custom Highlight API)
  - the best voice of the language is used (neural, Google or enhanced before an old desktop voice; teacher
    2026-11-03 "the quality in chrome seems really awful"), the voice menu lists the language's voices best first and
    a voice chosen there is used
  - pause and continue, next and previous sentence, Esc stops and hides the bar
  - at 360, 768 and 1280 px the bar fits the window (no horizontal scroll), its controls are at least 40 px high
Exit status 1 on any failure."""
import functools, http.server, json, re, sys, threading, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n
from _browser import launch

args = sys.argv[1:]
SITE = ROOT / (args.pop(0) if args and (ROOT / args[0]).is_dir() else "site")
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


expect("readaloud.js is published", (SITE / "readaloud.js").is_file())
missing, nospeech, count = [], [], 0
for f in sorted(SITE.rglob("*.html")):
    h = f.read_text()
    if 'class="toc"' not in h or "lesson.js" not in h: continue          # built from lesson.html
    count += 1
    if not re.search(r'<script src="(?:\.\./)*readaloud\.js(?:\?[^"]*)?"></script>', h): missing.append(f.relative_to(SITE).as_posix())
    m = re.search(r'<script id="fl-strings" type="application/json">(.*?)</script>', h, re.S)
    if not m or '"speech"' not in m.group(1): nospeech.append(f.relative_to(SITE).as_posix())
expect(f"{count} pages built from lesson.html load readaloud.js", not missing and count > 0, missing[:10])
expect("every such page carries lang \"speech\"", not nospeech, nospeech[:10])

# a stand-in voice: reports each word as a boundary, then ends the sentence; records what was spoken
MOCK = r"""(() => {
  const spoken = []; window.__spoken = spoken;
  class U { constructor(t) { this.text = t; this.lang = ''; this.rate = 1; } }
  const synth = { paused: false, q: null, t: 0,
    getVoices() { return [{ name: 'Microsoft Heidi Desktop - Finnish', lang: 'fi-FI', default: true }, { name: 'Microsoft Noora Online (Natural) - Finnish (Finland)', lang: 'fi-FI' },
      { name: 'Microsoft Hazel Desktop - English (Great Britain)', lang: 'en-GB' }, { name: 'Google UK English Female', lang: 'en-GB' }, { name: 'Google US English', lang: 'en-US' },
      { name: 'Test fr', lang: 'fr-FR' }]; },
    addEventListener() {}, cancel() { this.q = null; clearTimeout(this.t); },
    speak(u) { spoken.push(u.text); (window.__voice = window.__voice || []).push(u.voice && u.voice.name); this.q = u; const words = [...u.text.matchAll(/\S+/g)]; let k = 0;
      const tick = () => { if (this.q !== u) return;
        if (k < words.length) { u.onboundary && u.onboundary({ name: 'word', charIndex: words[k].index, charLength: words[k][0].length }); k++; this.t = setTimeout(tick, window.__wordMs || 5); }
        else { this.q = null; u.onend && u.onend({}); } };
      this.t = setTimeout(tick, 5); },
    pause() {}, resume() {} };
  Object.defineProperty(window, 'speechSynthesis', { value: synth, configurable: true }); window.SpeechSynthesisUtterance = U;
})();"""

TEX = {
    "fi": [(r"F = m \cdot a", "F on m kertaa a"), (r"Q = cm\Delta T", "Q on c m delta T"),
           (r"9{,}81\,\text{m/s}^2", "9,81 metriä per sekunti toiseen"), (r"72\,\text{km/h}", "72 kilometriä tunnissa"),
           (r"\overline{F}_{\mu}", "vektori F myy"), (r"2{,}5\,\text{m}^3", "2,5 kuutiometriä"),
           (r"c = 4190\,\frac{\text{J}}{\text{kg}\cdot{}^\circ\text{C}}", "c on 4190 joulea per kilogramma per celsiusaste"),
           (r"20\,^\circ\text{C}", "20 celsiusastetta"), (r"p = \frac{F}{A}", "p on F jaettuna A"), (r"1{,}18\,\text{kN}", "1,18 kilonewtonia"),
           (r"3{,}0 \cdot 10^{8}\,\text{m/s}", "3,0 kertaa 10 potenssiin 8 metriä sekunnissa"), (r"12\,000\,\text{J}", "12000 joulea")],
    "en": [(r"F = m \cdot a", "F equals m times a"), (r"9.81\,\text{m/s}^2", "9.81 metres per second squared"),
           (r"2.5\,\text{m}^2", "2.5 square metres"), (r"E = 3.6\,\text{kWh}", "E equals 3.6 kilowatt hours")],
}


def pick(pattern, lang_dir=""):
    for f in sorted((SITE / lang_dir).glob(pattern)):
        h = f.read_text()
        if "readaloud.js" in h: return f.relative_to(SITE).as_posix()
    return None


targets = args or [p for p in (pick("fy3-6.html"), pick("fy3-6.html", "en"), pick("fy3-6.html", "fi-easy"),
                                 pick("tvt-*.html"), pick("fy10-*.html"), pick("fy14-*.html", "en")) if p]

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_address[1]}/"

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = launch(pw)
    for page in targets:
        lang = page.split("/")[0] if "/" in page else i18n.SOURCE
        T = i18n.T(lang)
        for w in (1280, 768, 360):
            pg = b.new_page(viewport={"width": w, "height": 800})
            errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.add_init_script(MOCK)
            pg.goto(BASE + page); pg.wait_for_timeout(400)
            tag = f"{page} {w}px"
            start = pg.locator(".ra-start")
            expect(f"{tag}: one Kuuntele button, in this language", start.count() == 1 and T("js.ra_listen") in start.inner_text(), start.count())
            if w == 1280:
                expect(f"{tag}: the button is under the title", pg.evaluate("(() => { const h = document.querySelector('main h1'); return !h || h.nextElementSibling === document.querySelector('.ra-bar'); })()"))
                expect(f"{tag}: nothing spoken before the button", pg.evaluate("window.__spoken.length") == 0)
                key = "en" if lang == "en" else "fi"
                if page == targets[0] or lang == "en" and page.startswith("en/fy3"):
                    for tex, want in TEX[key]:
                        got = pg.evaluate("t => flSpeech.tex(t)", tex)
                        expect(f"{lang}: {tex} is spoken as \"{want}\"", got == want, got)
                blocks = pg.evaluate("flSpeech.blocks()")
                expect(f"{tag}: the page has text to read", len(blocks) > 3, len(blocks))
                h1 = pg.evaluate("(document.querySelector('main h1')||{}).textContent || ''")
                first = re.sub(r"\s+", " ", h1).strip().split(" ")[0]
                if first: expect(f"{tag}: the title is read first", bool(blocks) and blocks[0].startswith(first), [first, blocks[:1]])
                leaked = pg.evaluate("""() => flSpeech.elements().filter(e => {
                    for (let d = e.closest('details:not([open])'); d; d = d.parentElement && d.parentElement.closest('details:not([open])'))
                      if (!d.querySelector(':scope > summary')?.contains(e)) return true;
                    return !!e.closest('[hidden], svg, #sim-root');
                  }).map(e => e.textContent.trim().slice(0, 40))""")
                expect(f"{tag}: no text from a closed box, hidden step, figure or simulation is read", not leaked, leaked[:3])
                tex_left = [x for x in blocks if "\\" in x or "$" in x]
                expect(f"{tag}: no TeX or $ is read out", not tex_left, tex_left[:3])
            start.click(); pg.wait_for_timeout(120)
            pg.evaluate("window.__wordMs = 300")
            pg.wait_for_timeout(400)
            st = pg.evaluate("""() => ({ dock: !document.querySelector('.ra-dock').hidden, on: !!document.querySelector('main .ra-on'),
                 sent: CSS.highlights.has('ra-sentence'), word: CSS.highlights.has('ra-word'), n: window.__spoken.length,
                 sw: document.documentElement.scrollWidth, iw: window.innerWidth,
                 r: document.querySelector('.ra-dock').getBoundingClientRect().toJSON(),
                 low: [...document.querySelectorAll('.ra-dock button, .ra-dock select')].filter(e => e.offsetParent).filter(e => e.getBoundingClientRect().height < 40).length })""")
            expect(f"{tag}: reading starts, the bar shows, the block is marked and the sentence and word are highlighted",
                   st["dock"] and st["on"] and st["sent"] and st["word"] and st["n"] >= 1, st)
            expect(f"{tag}: the bar fits the window, controls at least 40 px", st["sw"] <= st["iw"] and st["r"]["left"] >= 0 and st["r"]["right"] <= st["iw"] and st["low"] == 0, st)
            if w == 1280:
                best = "Google UK English Female" if lang == "en" else "Microsoft Noora Online (Natural) - Finnish (Finland)"
                used = pg.evaluate("window.__voice.slice(-1)[0]")
                expect(f"{tag}: the best voice is chosen, not the old desktop voice", used == best, used)
                opts = pg.evaluate("[...document.querySelectorAll('.ra-voice select option')].map(o => o.value)")
                expect(f"{tag}: the voice menu lists this language's voices, best first", len(opts) >= 3 and opts[0] == "" and opts[1] == best, opts)
                other = opts[-1]
                pg.select_option(".ra-voice select", other); pg.wait_for_timeout(80)
                expect(f"{tag}: a voice chosen from the menu is used", pg.evaluate("window.__voice.slice(-1)[0]") == other, pg.evaluate("window.__voice.slice(-1)[0]"))
                pg.select_option(".ra-voice select", ""); pg.wait_for_timeout(80)
                n0 = pg.evaluate("window.__spoken.length")
                pg.click(".ra-dock .ra-main"); pg.wait_for_timeout(150)
                paused = pg.evaluate("[document.querySelector('.ra-start').getAttribute('aria-pressed'), window.__spoken.length]")
                pg.wait_for_timeout(400)
                expect(f"{tag}: pause stops the voice", paused[0] == "false" and pg.evaluate("window.__spoken.length") == paused[1], paused)
                pg.click(".ra-dock .ra-main"); pg.wait_for_timeout(100)
                said = pg.evaluate("window.__spoken.slice(-1)[0]")
                pg.click(f'.ra-dock .ra-btn[aria-label="{T("js.ra_next")}"]'); pg.wait_for_timeout(100)
                nxt = pg.evaluate("window.__spoken.slice(-1)[0]")
                pg.click(f'.ra-dock .ra-btn[aria-label="{T("js.ra_prev")}"]'); pg.wait_for_timeout(100)
                back = pg.evaluate("window.__spoken.slice(-1)[0]")
                expect(f"{tag}: continue repeats the sentence, next and previous move by one", nxt != said and back == said, [said, nxt, back])
                pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
                st = pg.evaluate("[document.querySelector('.ra-dock').hidden, !!document.querySelector('.ra-on'), CSS.highlights.has('ra-sentence')]")
                expect(f"{tag}: Esc stops, hides the bar and clears the marks", st == [True, False, False], st)
            expect(f"{tag}: no script errors", not errs, errs[:3])
            pg.close()
    b.close()
srv.shutdown()
print("FAIL" if fails else "PASS", f"({fails} failures)" if fails else "")
sys.exit(1 if fails else 0)
