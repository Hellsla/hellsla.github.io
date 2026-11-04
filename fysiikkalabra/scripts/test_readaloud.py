"""Read aloud (templates/readaloud.js, teacher 2026-11-03: "ääneenluku", "näyttää missä kohtaa tekstiä mennään", and the
progress bar brief: one Kuuntele / Tauko button at the right end of the stage bar).
Usage: python scripts/test_readaloud.py [site] [page ...]

Static, every page of the site built from templates/lesson.html (lessons, Sovella itsenäisesti, investigations, TVT
guides, course units) in every language: readaloud.js is loaded and the page's string block carries lang "speech".
In a browser, with a stand-in for the browser's voice (speechSynthesis is replaced by a script that reports every
word and ends each sentence; a headless browser has no voices), on one lesson per language, a TVT guide, an
investigation and a course unit (or the pages named):
  - one Kuuntele button (text and icon, aria-pressed) at the right end of the stage bar, in the page's language, and
    nothing is spoken before it is pressed; without a voice for the page's language there is no button
  - formulas are spoken as words (lang "speech"): a fixed set of TeX gives the expected Finnish and English; a formula
    with data-speech is spoken as written there
  - a lesson reads only Pohdinta and Teoriatiivistelmä, and no task, hint, model answer or solution in them; other
    pages read from the title; a closed box, a hidden worked-example step, a figure and a simulation are never read;
    the block being read is marked and the sentence and the word are highlighted (CSS Custom Highlight API), and the
    stage being read is marked in the bar
  - the best voice of the language is used (neural, Google or enhanced before an old desktop voice; teacher
    2026-11-03 "the quality in chrome seems really awful") when the device's voice reads
  - Tauko pauses and Kuuntele continues; a click on a stage moves the reading there (to the next stage that is read,
    paused, when that stage is not read); the speed menu (0,8 / 1 / 1,25) sets the rate; Esc stops
  - at 360, 768 and 1280 px the bar fits the window (no horizontal scroll), its controls are at least 40 px high;
    under 600 px Kuuntele is the icon only (its name in aria-label) with the menu arrow in the same pill, and at least
    two stage chips of a lesson show beside it (teacher 2026-11-04, UI fix 2)
  - on a phone-sized window (or with Save-Data, or without WebGPU) the device's voice is the default: Kuuntele speaks
    with it and nothing of the neural model is fetched; the menu offers the better voice (lang js.ra_better), and the
    download starts only when it is chosen (teacher 2026-11-04, UI fix 1)
The neural voice itself is checked with the real model from Hellsla/ruukkilabra-models (UI fix 3): a local clone
(FL_MODELS_DIR, or ruukkilabra-models beside this repository) when there is one, else its GitHub Pages copy; that check
is skipped, and says so, when neither can be reached.
Exit status 1 on any failure."""
import functools, http.server, json, os, re, sys, threading, pathlib, urllib.request
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
    speak(u) { spoken.push(u.text); (window.__rate = window.__rate || []).push(u.rate); (window.__voice = window.__voice || []).push(u.voice && u.voice.name); this.q = u; const words = [...u.text.matchAll(/\S+/g)]; let k = 0;
      const tick = () => { if (this.q !== u) return;
        if (k < words.length) { u.onboundary && u.onboundary({ name: 'word', charIndex: words[k].index, charLength: words[k][0].length }); k++; this.t = setTimeout(tick, window.__wordMs || 5); }
        else { this.q = null; u.onend && u.onend({}); } };
      this.t = setTimeout(tick, 5); },
    pause() {}, resume() {} };
  Object.defineProperty(window, 'speechSynthesis', { value: synth, configurable: true }); window.SpeechSynthesisUtterance = U;
  window.flTtsEngine = 'browser';   // these checks use the device-voice path; the neural voice has its own check below
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
            lesson = pg.evaluate("!!document.querySelector('main section.stage#herata, main section.stage#selita')")   # a lesson or a course unit
            expect(f"{tag}: one Kuuntele button, in this language, with an icon", start.count() == 1 and T("js.ra_listen") in start.inner_text()
                   and start.locator("svg").count() == 1 and start.get_attribute("aria-pressed") == "false"
                   and start.get_attribute("aria-label") == T("js.ra_listen"), start.count())
            if w < 600 and pg.locator("nav.toc .toc-tools").count():
                pill = pg.evaluate("""(() => { const s = document.querySelector('.ra-start'), m = document.querySelector('.ra-more'), t = document.querySelector('nav.toc'),
                    sp = s.querySelector('span').getBoundingClientRect(), a = s.getBoundingClientRect(), b = m.getBoundingClientRect(), tools = t.querySelector('.toc-tools').getBoundingClientRect();
                    const chips = [...t.querySelectorAll(':scope > a')].filter(c => { const r = c.getBoundingClientRect(); return r.left >= t.getBoundingClientRect().left - 1 && r.right <= tools.left + 1; }).length;
                    return { icon: sp.width <= 1 && a.width <= 48, joined: Math.abs(b.left - a.right) < 1.5, chips, n: t.querySelectorAll(':scope > a').length }; })()""")
                # a lesson's numbered stage chips: at least two beside the button; a TVT guide's or an investigation's
                # long section names: at least one
                expect(f"{tag}: under 600 px Kuuntele is the icon only, the menu arrow in the same pill, {'two stage chips' if lesson else 'a chip'} beside it",
                       pill["icon"] and pill["joined"] and pill["chips"] >= (min(2, pill["n"]) if lesson else 1), pill)
            if w == 1280:
                expect(f"{tag}: the button is at the right end of the stage bar", pg.evaluate("""(() => { const t = document.querySelector('nav.toc'), b = document.querySelector('.ra-start');
                    if (!t) return true; const tools = t.querySelector('.toc-tools'); return !!tools && tools.contains(b) && t.lastElementChild === tools
                      && Math.abs(t.getBoundingClientRect().right - b.parentElement.getBoundingClientRect().right) < 24; })()"""))
                expect(f"{tag}: nothing spoken before the button", pg.evaluate("window.__spoken.length") == 0)
                key = "en" if lang == "en" else "fi"
                if page == targets[0] or lang == "en" and page.startswith("en/fy3"):
                    for tex, want in TEX[key]:
                        got = pg.evaluate("t => flSpeech.tex(t)", tex)
                        expect(f"{lang}: {tex} is spoken as \"{want}\"", got == want, got)
                blocks = pg.evaluate("flSpeech.blocks()")
                expect(f"{tag}: the page has text to read", len(blocks) > 3, len(blocks))
                if lesson:
                    outside = pg.evaluate("""() => flSpeech.elements().filter(e => !e.closest('#herata, #selita')
                        || e.closest('.activity:not(.act-hook):not(.act-theory), details.opt, details.answer, details.hint, .hints, .feedback, .sol-step, .example, form, fieldset'))
                        .map(e => e.textContent.trim().slice(0, 40))""")
                    expect(f"{tag}: only Pohdinta and Teoriatiivistelmä are read, no task, hint, model answer or solution", not outside, outside[:3])
                    first = re.sub(r"\s+", " ", pg.evaluate("document.querySelector('#herata h2').textContent.replace(/^\\s*\\d+/, '')")).strip()
                    expect(f"{tag}: the reading starts at Pohdinta", bool(blocks) and blocks[0].startswith(first), [first, blocks[:1]])
                else:
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
                said = pg.evaluate("""() => { const k = [...document.querySelectorAll('main .katex')].find(k => flSpeech.elements().some(e => e.contains(k)));
                    if (!k) return null; const s = document.createElement('span'); s.setAttribute('data-speech', 'sigma F on yhtä kuin m kertaa a');
                    k.replaceWith(s); s.append(k); return flSpeech.blocks().some(t => t.includes('sigma F on yhtä kuin m kertaa a')); }""")
                if said is not None: expect(f"{tag}: a formula with data-speech is spoken as written there", said)
            start.click(); pg.wait_for_timeout(120)
            pg.evaluate("window.__wordMs = 300")
            pg.wait_for_timeout(400)
            st = pg.evaluate("""() => ({ pressed: document.querySelector('.ra-start').getAttribute('aria-pressed'), text: document.querySelector('.ra-start').innerText,
                 on: !!document.querySelector('main .ra-on'), sent: CSS.highlights.has('ra-sentence'), word: CSS.highlights.has('ra-word'), n: window.__spoken.length,
                 stage: (() => { const a = document.querySelector('nav.toc a[aria-current]'), on = document.querySelector('main .ra-on'); if (!a || !on) return true;
                   const inAny = [...document.querySelectorAll('nav.toc a[href^="#"]')].some(x => document.getElementById(x.getAttribute('href').slice(1))?.contains(on));
                   const t = document.getElementById(a.getAttribute('href').slice(1)); return !inAny || !!t && t.contains(on); })(),
                 sw: document.documentElement.scrollWidth, iw: window.innerWidth,
                 low: [...document.querySelectorAll('.ra-start, .ra-more')].filter(e => e.offsetParent).filter(e => e.getBoundingClientRect().height < 40).length,
                 out: [...document.querySelectorAll('.ra-start, .ra-more')].filter(e => { const r = e.getBoundingClientRect(); return r.left < 0 || r.right > innerWidth; }).length })""")
            expect(f"{tag}: reading starts (Tauko, aria-pressed), the block is marked, the sentence and word are highlighted and the stage being read is marked",
                   st["pressed"] == "true" and T("js.ra_pause") in st["text"] and st["on"] and st["sent"] and st["word"] and st["n"] >= 1 and st["stage"], st)
            expect(f"{tag}: the bar fits the window, controls at least 40 px", st["sw"] <= st["iw"] and st["low"] == 0 and st["out"] == 0, st)
            if w == 1280:
                best = "Google UK English Female" if lang == "en" else "Microsoft Noora Online (Natural) - Finnish (Finland)"
                used = pg.evaluate("window.__voice.slice(-1)[0]")
                expect(f"{tag}: the best voice is chosen, not the old desktop voice", used == best, used)
                pg.click(".ra-start"); pg.wait_for_timeout(150)
                paused = pg.evaluate("[document.querySelector('.ra-start').getAttribute('aria-pressed'), document.querySelector('.ra-start').innerText, window.__spoken.length]")
                pg.wait_for_timeout(400)
                expect(f"{tag}: Tauko stops the voice and the button says Kuuntele", paused[0] == "false" and T("js.ra_listen") in paused[1]
                       and pg.evaluate("window.__spoken.length") == paused[2], paused)
                said = pg.evaluate("window.__spoken.slice(-1)[0]")
                pg.click(".ra-start"); pg.wait_for_timeout(100)
                expect(f"{tag}: Kuuntele continues from the same sentence", pg.evaluate("window.__spoken.slice(-1)[0]") == said)
                pg.click(".ra-more"); pg.wait_for_timeout(100)
                menu = pg.evaluate("""() => { const m = document.querySelector('.ra-menu'); return { open: !m.hidden, rates: [...m.querySelectorAll('.ra-speeds input')].map(i => i.value),
                    voice: !m.querySelector('.ra-voice').hidden, expanded: document.querySelector('.ra-more').getAttribute('aria-expanded'), inBar: !!document.querySelector('nav.toc .ra-speeds') }; }""")
                expect(f"{tag}: the menu opens with the speeds 0,8 / 1 / 1,25 (not in the bar), no voice menu without the neural voice",
                       menu["open"] and menu["rates"] == ["0.8", "1", "1.25"] and not menu["voice"] and menu["expanded"] == "true" and not menu["inBar"], menu)
                pg.locator(".ra-speeds label").nth(2).click(); pg.wait_for_timeout(150)
                expect(f"{tag}: speed 1,25 is used", pg.evaluate("window.__rate.slice(-1)[0]") == 1.25, pg.evaluate("window.__rate.slice(-3)"))
                pg.keyboard.press("Escape"); pg.wait_for_timeout(50)
                expect(f"{tag}: Esc closes the menu first", pg.evaluate("document.querySelector('.ra-menu').hidden && document.querySelector('.ra-start').getAttribute('aria-pressed') === 'true'"))
                if lesson:
                    pg.click('nav.toc a[href="#selita"]'); pg.wait_for_timeout(300)
                    h = re.sub(r"\s+", " ", pg.evaluate("document.querySelector('#selita h2').textContent.replace(/^\\s*\\d+/, '')")).strip()
                    got = pg.evaluate("window.__spoken.slice(-6)")
                    expect(f"{tag}: a click on Teoriatiivistelmä moves the reading there", any(x.strip().startswith(h) for x in got)
                           and pg.evaluate("!!document.querySelector('#selita .ra-on')"), [h, got])
                    if pg.locator('nav.toc a[href="#tutki"]').count():
                        pg.click('nav.toc a[href="#herata"]'); pg.wait_for_timeout(200)
                        pg.click('nav.toc a[href="#tutki"]'); pg.wait_for_timeout(200)
                        st2 = pg.evaluate("[document.querySelector('.ra-start').getAttribute('aria-pressed'), !!document.querySelector('#selita .ra-on')]")
                        expect(f"{tag}: a click on a stage that is not read pauses at the next stage that is", st2 == ["false", True], st2)
                pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
                st = pg.evaluate("[document.querySelector('.ra-start').getAttribute('aria-pressed'), !!document.querySelector('.ra-on'), CSS.highlights.has('ra-sentence')]")
                expect(f"{tag}: Esc stops and clears the marks", st == ["false", False, False], st)
            expect(f"{tag}: no script errors", not errs, errs[:3])
            pg.close()
    # no voice for the page's language: no button
    if targets:
        pg = b.new_page(viewport={"width": 1280, "height": 800})
        pg.add_init_script(MOCK.replace("getVoices() { return [", "getVoices() { return [{ name: 'Test fr', lang: 'fr-FR' }]; return ["))
        pg.goto(BASE + targets[0]); pg.wait_for_timeout(400)
        expect(f"{targets[0]}: without a voice for the page's language there is no Kuuntele button", pg.evaluate("!document.querySelector('.ra-start') || !document.querySelector('.ra-start').offsetParent"))
        pg.close()
    b.close()

# The models (UI fix 3): a local clone of Hellsla/ruukkilabra-models, served here, or its GitHub Pages copy.
MODELS_URL = "https://hellsla.github.io/ruukkilabra-models/"
mdir = pathlib.Path(os.environ.get("FL_MODELS_DIR") or ROOT.parent.parent / "ruukkilabra-models")
MBASE = None
if (mdir / "supertonic3-v1/manifest.json").is_file():
    class Cors(Quiet):                       # another origin here, as GitHub Pages it sends Access-Control-Allow-Origin: *
        def end_headers(self): self.send_header("Access-Control-Allow-Origin", "*"); super().end_headers()
    msrv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Cors, directory=str(mdir)))
    msrv.handle_error = lambda *a: None       # a page closed during a download: a broken pipe, not a failure
    threading.Thread(target=msrv.serve_forever, daemon=True).start()
    MBASE = f"http://127.0.0.1:{msrv.server_address[1]}/"
else:
    try:
        with urllib.request.urlopen(MODELS_URL + "supertonic3-v1/manifest.json", timeout=15) as r:
            if r.status == 200: MBASE = MODELS_URL
    except Exception: pass
NPAGE = pick("fy3-6.html") or (targets[0] if targets else None)
MODEL_FILES = "supertonic3-v1/"

# A phone-sized window (teacher 2026-11-04, UI fix 1): the device's voice by default, no model fetched before the
# better voice is chosen in the menu; choosing it starts the download.
if NPAGE:
    with sync_playwright() as pw:
        b = launch(pw)
        pg = b.new_page(viewport={"width": 360, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        asked = []; pg.on("request", lambda r: asked.append(r.url) if MODEL_FILES in r.url or "/ort/" in r.url else None)
        pg.add_init_script(MOCK.replace("window.flTtsEngine = 'browser';", f"window.flTtsModelBase = {json.dumps(MBASE or MODELS_URL)};"))
        pg.goto(BASE + NPAGE); pg.wait_for_timeout(400)
        T = i18n.T(i18n.SOURCE)
        st = pg.evaluate("flSpeech.state()")
        expect(f"{NPAGE} 360px: the device's voice is the default on a phone", st["engine"] == "browser" and st["light"], st)
        pg.click(".ra-start"); pg.wait_for_timeout(300)
        expect(f"{NPAGE} 360px: Kuuntele speaks with the device's voice and fetches nothing of the model",
               pg.evaluate("window.__spoken.length") > 0 and not asked, asked[:3])
        pg.click(".ra-start"); pg.wait_for_timeout(100)
        pg.click(".ra-more"); pg.wait_for_timeout(100)
        better = pg.evaluate("(() => { const l = document.querySelector('.ra-menu .ra-better'); return l && { shown: !l.hidden && !!l.offsetParent, text: l.textContent.trim(), on: l.querySelector('input').checked, voice: !document.querySelector('.ra-voice').hidden }; })()")
        expect(f"{NPAGE} 360px: the menu offers \"{T('js.ra_better')}\", not chosen, no Nainen / Mies yet",
               bool(better) and better["shown"] and better["text"] == T("js.ra_better") and not better["on"] and not better["voice"], better)
        expect(f"{NPAGE} 360px: still nothing of the model fetched with the menu open", not asked, asked[:3])
        pg.check(".ra-better input"); pg.wait_for_timeout(1500)
        expect(f"{NPAGE} 360px: choosing the better voice starts the download and shows Nainen / Mies",
               any(MODEL_FILES + "manifest.json" in u for u in asked) and pg.evaluate("!document.querySelector('.ra-voice').hidden"), asked[:3])
        expect(f"{NPAGE} 360px: no script errors", not errs, errs[:3])
        b.close()

# The neural voice (teacher 2026-11-03: Supertonic 3, "Nainen / Mies"): the real model on the CPU (headless Chromium
# has no WebGPU, so it is chosen in the menu first), on one Finnish lesson: it loads, the first sentence is synthesised
# and played with the sentence highlighted, the menu has Nainen and Mies, and Mies gives a new synthesis of the same
# sentence.
if NPAGE and not MBASE:
    print(f"SKIP neural voice: no models in {mdir} and {MODELS_URL} cannot be reached")
if NPAGE and MBASE:
    with sync_playwright() as pw:
        b = launch(pw)
        pg = b.new_page(viewport={"width": 1280, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.add_init_script("""window.flTtsGpu = false; window.flTtsWorkers = 1; window.__bufs = []; window.flTtsModelBase = """ + json.dumps(MBASE) + """;
          const cb = AudioContext.prototype.createBuffer; AudioContext.prototype.createBuffer = function (c, n, sr) { window.__bufs.push([n, sr]); return cb.call(this, c, n, sr); };""")
        pg.goto(BASE + NPAGE); pg.wait_for_timeout(400)
        T = i18n.T(i18n.SOURCE)
        opts = pg.evaluate("[...document.querySelectorAll('.ra-voice select option')].map(o => o.textContent)")
        expect(f"neural {NPAGE}: the voice menu is {T('js.ra_female')} / {T('js.ra_male')}", opts == [T("js.ra_female"), T("js.ra_male")], opts)
        if not pg.evaluate("flSpeech.state().engine === 'neural'"):
            pg.click(".ra-more"); pg.check(".ra-better input"); pg.keyboard.press("Escape")
        pg.click(".ra-start")
        st = {}
        for _ in range(240):
            st = pg.evaluate("flSpeech.state()")
            if st["ep"] or st["failed"]: break
            pg.wait_for_timeout(500)
        expect(f"neural {NPAGE}: the model loads (on the CPU here)", st.get("ep") == "wasm" and not st.get("failed"), st)
        for _ in range(120):
            if pg.evaluate("window.__bufs.length"): break
            pg.wait_for_timeout(500)
        bufs = pg.evaluate("window.__bufs")
        expect(f"neural {NPAGE}: the first sentence is synthesised and played at 44,1 kHz, 1 to 30 s long",
               bool(bufs) and bufs[0][1] == 44100 and 44100 <= bufs[0][0] <= 30 * 44100, bufs)
        expect(f"neural {NPAGE}: the sentence being read is highlighted", pg.evaluate("CSS.highlights.has('ra-sentence') && !!document.querySelector('main .ra-on')"))
        n0 = len(bufs)
        pg.click(".ra-more"); pg.select_option(".ra-voice select", "male")
        for _ in range(120):
            if pg.evaluate("window.__bufs.length") > n0: break
            pg.wait_for_timeout(500)
        expect(f"neural {NPAGE}: Mies reads the sentence again in the male voice", pg.evaluate("window.__bufs.length") > n0 and pg.evaluate("flSpeech.state().voice") == "male")
        pg.keyboard.press("Escape")
        expect(f"neural {NPAGE}: no script errors", not errs, errs[:3])
        b.close()
srv.shutdown()
print("FAIL" if fails else "PASS", f"({fails} failures)" if fails else "")
sys.exit(1 if fails else 0)
