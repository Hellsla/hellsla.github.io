"""The solution editor under the exercises (templates/lesson.js part 6, teacher 2026-11-01: Abitti's own Digabi
rich-text-editor, "Kirjoita ratkaisu" / "Kopioi ratkaisu", for L'Math). Usage: python scripts/test_writepad.py [site] [page ...]

Static, every published lesson in every language: lesson.js marks the exercises it serves by `#exercises li[id]`, so
every exercise the build writes must be such an <li> with its p.task, and the vendored editor files must be there.
In a browser, on one lesson per language (or the pages named) served over http://localhost (the clipboard needs a
secure page):
  - one "Kirjoita ratkaisu" per exercise, in this language, before the exercise's answer and model solution; the
    answer box, Tarkista and the answer/solution boxes are still there and the check still answers
  - nothing of the editor is loaded before the first click (no vendor/digabi request), and it is loaded once
  - the editor opens under the exercise; text and a formula (Ctrl+E) are typed, the formula becomes an image with
    its LaTeX in alt; "Kopioi ratkaisu" puts the editor's HTML and a plain-text copy (formula as \\( LaTeX \\)) on the
    clipboard, and pasting that HTML into another exercise's editor (the same editor as in Abitti) gives back an
    editable formula with the same LaTeX
  - Vastaus and Näytä ratkaisu are buttons on the exercise's top row beside the Ydintehtävä tag, and open their
    boxes in place (teacher 2026-11-01)
  - at 360, 768 and 1280 px the open editor fits the exercise: no horizontal scroll, buttons at least 40 px high
And on the Sovella itsenäisesti page of every course in every language (teacher 2026-11-01, "myös Sovella"): one
button per task, inside its task card before the model answer, the editor opens and the copy works, and at 360 and
1280 px the open editor fits the card.
And the solutions kept on this device (templates/padstore.js, phase 2): a solution comes back after a reload, two
exercises keep their own, a restored formula is still an editable formula, a pasted picture survives, the versioned
backup file exports and imports, Poista ratkaisu / Poista kaikki delete, a damaged record and a full or forbidden
storage are reported instead of "Tallennettu", the copy still works, and no request but GET for the site's files.
And a pasted picture's size (teacher 2026-11-06): a click on it shows Pieni / Keskikoko / Iso / Alkuperäinen and a corner
handle, at 360 and 1280 px; the size given is saved and comes back after a reload.
Exit status 1 on any failure."""
import functools, http.server, re, sys, threading, pathlib
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


VENDOR = ["rich-text-editor-bundle.js", "tex-svg.js", "mathquill.css", "fonts/Symbola.woff2", "fonts/Symbola.woff"]
expect("the editor files are published in vendor/digabi/", all((SITE / "vendor/digabi" / f).is_file() for f in VENDOR),
       [f for f in VENDOR if not (SITE / "vendor/digabi" / f).is_file()])

pages = {}   # lang -> [page names with exercises]
for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    for f in sorted(out.glob("*.html")):
        h = f.read_text()
        m = re.search(r'id="exercises"(.*?)(?=<section|<div class="stage|</main>)', h, re.S)
        if not m or "<li" not in m.group(1): continue
        items = re.findall(r'<li id="[^"]+"[^>]*>(?:<span class="ex-num"><span class="visually-hidden">[^<]*</span>[^<]*</span>)?(?:<span class="ex-core[^"]*">[^<]*</span>)*<p class="task"', m.group(1))   # the running number "6-3" first (build.py number_label)
        tasks = m.group(1).count('class="task"')
        if tasks: pages.setdefault(lang, []).append(f.relative_to(SITE).as_posix())
        if len(items) != tasks:
            expect(f"{lang} {f.name}: every exercise is an <li id> with its p.task", False, f"{len(items)} of {tasks}")
        nums = re.findall(r'<li id="[^"]+"[^>]*\bdata-num="([^"]+)"', m.group(1))   # running numbers "luku-tehtävä" (teacher 2026-11-04)
        if tasks and f.stem.startswith("fy") and f.stem[2:].split("-")[0].isdigit():
            import courses as _c, json as _j
            slots = [l["id"] for l in _j.loads((SITE.parent / "curriculum.json").read_text())[_c.course_of(f.stem)]["lessons"]]
            want = [f"{slots.index(f.stem) + 1}-{k}" for k in range(1, len(nums) + 1)]
            if not nums or nums != want: expect(f"{lang} {f.name}: exercises numbered {want[:1]}…{want[-1:]} over every level", False, str(nums))
for lang in pages:
    expect(f"{lang}: {len(pages[lang])} published lessons have exercises", True)

# Which element makes the page scroll sideways (CI 2026-11-13: the listed elements past the window are mostly inside scroll boxes and
# cannot be the cause). Used only when a check has already failed: hide each element past the window in turn and keep those whose
# hiding shortens the page's scrollWidth, with their ancestors' position/overflow/left/right/width, and the toolbar's own box.
CULPRITS_JS = """() => { const sw = () => document.documentElement.scrollWidth - innerWidth, base = sw(), out = [];
    const brief = (n) => { const cs = getComputedStyle(n), b = n.getBoundingClientRect();
        return n.tagName.toLowerCase() + '.' + String(n.getAttribute('class') || '').slice(0, 24) + ' ' + cs.position + ' ox=' + cs.overflowX + ' L' + Math.round(b.left) + ' R' + Math.round(b.right) + ' W' + Math.round(b.width); };
    for (const x of [...document.querySelectorAll('body *')].filter(x => x.getBoundingClientRect().right > innerWidth + 0.5).slice(0, 120)) {
        const d = x.style.display; x.style.display = 'none'; const s = sw(); x.style.display = d;
        if (s < base && out.length < 6) { const chain = []; for (let n = x; n && n !== document.documentElement && chain.length < 7; n = n.parentElement) chain.push(brief(n)); out.push({ drops_to: s, chain }); } }
    const tb = document.querySelector('.rich-text-editor-toolbar-root > div');
    return { base, html: document.documentElement.className, toolbar: tb ? brief(tb) : null, toolbar_parents: tb ? (() => { const o = []; for (let n = tb.parentElement; n && n !== document.documentElement && o.length < 12; n = n.parentElement) { const cs = getComputedStyle(n); if (cs.containerType !== 'normal' || cs.contain !== 'none' || cs.transform !== 'none' || cs.filter !== 'none' || cs.willChange !== 'auto') o.push(brief(n) + ' ct=' + cs.containerType + ' contain=' + cs.contain); } return o; })() : null, culprits: out }; }"""

targets = [p for p in (args or [pp[0] for pp in pages.values()])]

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
handler = functools.partial(Quiet, directory=str(SITE))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_address[1]}/"

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = launch(pw)
    for page in targets:
        lang = page.split("/")[0] if "/" in page else i18n.SOURCE
        T = i18n.T(lang)
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, permissions=["clipboard-read", "clipboard-write"])
        pg = ctx.new_page()
        reqs = []; errs = []
        pg.on("request", lambda r: reqs.append(r.url))
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(BASE + page); pg.wait_for_load_state("load")
        pg.evaluate("document.querySelectorAll('#exercises details.level').forEach(d => { d.open = true; })")   # the levels are closed boxes
        n_ex = pg.locator("#exercises li[id]:has(> .task)").count()
        btns = pg.locator("#exercises .pad-open")
        expect(f"{page}: one '{T('js.pad_write')}' per exercise ({n_ex})", n_ex > 0 and btns.count() == n_ex, f"{btns.count()} buttons")
        expect(f"{page}: the button's text is this language's", btns.first.inner_text().strip() == T("js.pad_write"), btns.first.inner_text())
        order = pg.evaluate("""() => [...document.querySelectorAll('#exercises li[id]')].every(li => {
            const b = li.querySelector(':scope > .pad-open, :scope > .ex-row > .pad-open'), a = li.querySelector(':scope > details.answer'), s = li.querySelector(':scope > details.solution'), f = li.querySelector(':scope > .ex-row > form.check');
            return b && [a, s, f].every(x => !x || (b.compareDocumentPosition(x) & 4)) && (!f || (b.nextElementSibling.classList.contains('pad') && (b.nextElementSibling.compareDocumentPosition(f) & 4))); })""")
        expect(f"{page}: the button and editor come after the task and before its answer box, answer and model solution (write first, then check)", order)
        row = pg.evaluate("""() => [...document.querySelectorAll('#exercises li[id]')].every(li => !li.querySelector('form.check') || li.querySelector(':scope > .ex-row > .pad-open + .pad + form.check'))
            && document.querySelectorAll('label.solved').length === 0""")
        expect(f"{page}: '{T('js.pad_write')}' and the answer box (input, unit, Tarkista) on one row; no tick 'Olen tehnyt ratkaisun' (teacher 2026-11-06)", row)
        head = pg.evaluate("""() => [...document.querySelectorAll('#exercises li[id]')].every(li => {
            const h = li.firstElementChild, t = h && [...h.querySelectorAll('.ex-toggle')], d = [...li.querySelectorAll(':scope > details.answer, :scope > details.solution')];
            return h && h.classList.contains('ex-head') && t.length === d.length && t.every((b, i) => b.getAttribute('aria-controls') === d[i].id && b.textContent === d[i].querySelector('summary').textContent)
                && (!li.querySelector('.ex-core') || h.contains(li.querySelector('.ex-core'))) && d.every(x => !x.open && x.querySelector('summary').offsetHeight === 0); })""")
        expect(f"{page}: Vastaus and Näytä ratkaisu are buttons in the exercise's top row beside its tag (teacher 2026-11-01)", head)
        tg = pg.locator("#exercises li[id] .ex-toggle").first
        tg.scroll_into_view_if_needed()
        li0 = pg.locator("#exercises li[id]:has(.ex-toggle)").first
        expect(f"{page}: Vastaus and Näytä ratkaisu stay in view, locked with the reason, until the student tries (teacher 2026-11-03)",
               tg.is_visible() and tg.is_disabled() and tg.get_attribute("aria-disabled") == "true" and li0.locator(".ex-head .lock-note").inner_text().strip() == T("js.locked_try" if li0.locator("form.check").count() else "js.locked_done"))
        if li0.locator("form.check").count(): li0.locator("form.check input").fill("1"); li0.locator("form.check button").click()
        else: li0.evaluate("(li) => li.dispatchEvent(new CustomEvent('fl:written'))")   # what the editor tells once something is written in it
        expect(f"{page}: one try opens them", not tg.is_disabled() and li0.locator(".lock-note").count() == 0)
        tp = ctx.new_page(); tp.goto(BASE + page + "?ratkaisut=1"); tp.wait_for_load_state("load")
        expect(f"{page}: ?ratkaisut=1 opens every lock for the teacher", tp.locator("#exercises [data-locked], .hints [data-locked], .ex-toggle:disabled").count() == 0 and tp.locator(".teacher-note").count() == 1)
        tp.close(); pg.bring_to_front()   # the teacher's page took the focus; the toggle event of a background tab may wait
        tg.click()
        try: pg.wait_for_function("(b) => b.getAttribute('aria-expanded') === 'true'", arg=tg.element_handle(), timeout=3000)
        except Exception: pass
        expect(f"{page}: the Vastaus button opens the answer in its place", pg.evaluate("(id) => document.getElementById(id).open", tg.get_attribute("aria-controls")) and tg.get_attribute("aria-expanded") == "true")
        tg.click()
        expect(f"{page}: nothing of the editor loads before the first click", not any("/vendor/digabi/" in u for u in reqs),
               [u for u in reqs if "/vendor/digabi/" in u])
        # the answer check is unchanged
        form = pg.locator("#exercises form.check").first
        if form.count():
            form.locator("input").fill("abc"); form.locator("button").click()
            expect(f"{page}: the answer check still answers", form.locator("output").inner_text().strip() == T("js.check_number"))
        li = pg.locator("#exercises li[id]:has(> .task)").first
        li.locator(".pad-open").scroll_into_view_if_needed(); li.locator(".pad-open").click()
        try:
            li.locator(".rich-text-editor").wait_for(timeout=20000)
        except Exception:
            expect(f"{page}: the editor opens", False, errs); ctx.close(); continue
        expect(f"{page}: the editor opens under the exercise, focused", pg.evaluate("document.activeElement && document.activeElement.classList.contains('rich-text-editor')"))
        pg.keyboard.type("v = s : t, joten "); pg.keyboard.press("Control+e"); pg.wait_for_timeout(200)
        pg.keyboard.type("v=s/t"); pg.keyboard.press("Escape"); pg.wait_for_timeout(400)
        pg.keyboard.type(" eli nopeus.")
        alt = li.locator(".rich-text-editor img").first.get_attribute("alt") if li.locator(".rich-text-editor img").count() else None
        src = li.locator(".rich-text-editor img").first.get_attribute("src") if alt else ""
        expect(f"{page}: a formula becomes an image with its LaTeX in alt, drawn in the browser", alt == "v=\\frac{s}{t}" and src.startswith("data:image/svg+xml"), (alt, src[:40]))
        expect(f"{page}: Kopioi and Poista ratkaisu beside the hide button, Tallennetut ratkaisut beside the save state (teacher 2026-11-06)",
               li.evaluate("(li) => !!li.querySelector('.ex-row > .pad-open + .pad-head > .pad-copy + .pad-delete') && !!li.querySelector('.pad > .pad-saverow > .pad-save + .pad-saved')"))
        li.locator(".pad-copy").click(); pg.wait_for_timeout(300)
        expect(f"{page}: Kopioi ratkaisu says the solution is copied", li.locator(".pad-status").inner_text().strip() == T("js.pad_copied"), li.locator(".pad-status").inner_text())
        clip = pg.evaluate("""async () => { const out = {}; for (const it of await navigator.clipboard.read()) for (const t of it.types) out[t] = await (await it.getType(t)).text(); return out; }""")
        expect(f"{page}: the clipboard has the plain text with the formula as \\( LaTeX \\)",
               clip.get("text/plain", "").replace(" ", " ") == "v = s : t, joten \\(v=\\frac{s}{t}\\) eli nopeus.", clip.get("text/plain"))
        expect(f"{page}: the clipboard has the HTML with the formula image and its LaTeX", 'alt="v=\\frac{s}{t}"' in clip.get("text/html", ""), clip.get("text/html", "")[:200])
        loaded = [u for u in reqs if "/vendor/digabi/" in u]
        li2 = pg.locator("#exercises li[id]:has(> .task)").nth(1)
        if li2.count():
            li2.locator(".pad-open").click(); li2.locator(".rich-text-editor").wait_for(timeout=10000)
            li2.locator(".rich-text-editor").click(); pg.keyboard.press("Control+v"); pg.wait_for_timeout(600)
            alt2 = li2.locator(".rich-text-editor img[data-math-image]").first.get_attribute("alt") if li2.locator(".rich-text-editor img[data-math-image]").count() else None
            expect(f"{page}: pasted into the same editor as in Abitti, the formula is an editable formula again", alt2 == "v=\\frac{s}{t}",
                   li2.locator(".rich-text-editor").inner_html()[:300])
            expect(f"{page}: the editor files load once", len([u for u in reqs if "/vendor/digabi/" in u]) == len(loaded), [u for u in reqs if "/vendor/digabi/" in u])
        for w in (360, 768, 1280):
            pg.set_viewport_size({"width": w, "height": 800}); pg.wait_for_timeout(200)
            m = pg.evaluate("""(id) => { const li = document.getElementById(id), ed = li.querySelector('.rich-text-editor'), r = li.getBoundingClientRect(), e = ed.getBoundingClientRect();
                return { scroll: document.documentElement.scrollWidth - innerWidth, inside: e.left >= r.left - 1 && e.right <= r.right + 1,
                         small: [...li.querySelectorAll('.pad-open,.pad-copy')].filter(b => b.getBoundingClientRect().height < 40).length,
                         over: [...document.querySelectorAll('body *')].map(x => [x, x.getBoundingClientRect()]).filter(([x, b]) => b.right > innerWidth + 0.5)
                             .sort((a, b) => b[1].right - a[1].right).slice(0, 12).map(([x, b]) => ({ tag: x.tagName.toLowerCase(), cls: String(x.getAttribute('class') || ''), id: x.id, width: Math.round(b.width), right: Math.round(b.right) })) }; }""", li.get_attribute("id"))
            # `over` (the elements whose right edge passes the window) only explains a failure; the condition is unchanged
            if m["scroll"] > 0: m["culprits"] = pg.evaluate(CULPRITS_JS)   # only explains the failure below
            expect(f"{page} {w} px: the open editor fits the exercise, no horizontal scroll, buttons 40 px", m["scroll"] <= 0 and m["inside"] and not m["small"], m)
            if w in (360, 1280):
                li.locator(".pad").scroll_into_view_if_needed()
                shot = ROOT / "preview" / "writepad"; shot.mkdir(parents=True, exist_ok=True)
                li.screenshot(path=str(shot / f"{page.replace('/', '_')}-{w}.png"))
        if page.split("/")[-1] == "fy1-1.html":   # fi, en and fi-easy
            # the toolbar's own box, ten openings in a row, wide then narrow (360 px) (CI 2026-11-13: it sometimes ran past the window, 455 px wide rows
            # inside it; the box is fixed to the window or, if a size container becomes its containing block, to that column)
            bad = []
            for k in range(10):
                tp = ctx.new_page(); tp.set_viewport_size({"width": 1280, "height": 800}); tp.goto(BASE + page); tp.wait_for_load_state("load")
                tp.evaluate("document.querySelectorAll('#exercises details.level').forEach(d => { d.open = true; })")
                l0 = tp.locator("#exercises li[id]:has(> .task)").first
                l0.locator(".pad-open").scroll_into_view_if_needed(); l0.locator(".pad-open").click()
                l0.locator(".rich-text-editor").wait_for(timeout=20000); tp.keyboard.type("v = s : t, joten "); tp.keyboard.press("Control+e"); tp.wait_for_timeout(100); tp.keyboard.type("v=s/t"); tp.keyboard.press("Escape"); tp.wait_for_timeout(400)
                tp.set_viewport_size({"width": 360, "height": 800}); tp.wait_for_timeout(200)   # the failing path: opened wide, then narrow
                r = tp.evaluate("""() => { const t = document.querySelector('.rich-text-editor-toolbar-root > div'), b = t && t.getBoundingClientRect();
                    return { scroll: document.documentElement.scrollWidth - innerWidth, toolbar: !!t, left: b && Math.round(b.left), right: b && Math.round(b.right), width: b && Math.round(b.width),
                             pos: t && getComputedStyle(t).position, parent: t && t.parentElement.className }; }""")
                if not (r["toolbar"] and r["scroll"] <= 0 and r["left"] >= 0 and r["right"] <= 360):
                    if r["scroll"] > 0: r["culprits"] = tp.evaluate(CULPRITS_JS)
                    bad.append((k, r))
                tp.close()
            expect(f"{page} 360 px: the editor's toolbar box stays inside the window and the page does not scroll sideways, ten openings in a row", not bad, bad)
        expect(f"{page}: no script errors", not errs, errs)
        ctx.close()
    for page in sorted(p.relative_to(SITE).as_posix() for p in SITE.glob("**/*-sovella.html")):
        lang = page.split("/")[0] if "/" in page else i18n.SOURCE
        T = i18n.T(lang)
        ctx = b.new_context(viewport={"width": 1280, "height": 900}, permissions=["clipboard-read", "clipboard-write"])
        pg = ctx.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(BASE + page); pg.wait_for_load_state("load")
        n = pg.locator("section.practice-task[id]").count()
        ok = pg.evaluate("""() => [...document.querySelectorAll('section.practice-task[id]')].every(s => {
            const card = s.querySelector(':scope > .task-card'), b = card && card.querySelector(':scope > .ex-row > .pad-open'), r = card && card.querySelector(':scope > details.reveal');
            return b && b.textContent && r && (b.compareDocumentPosition(r) & 4); })""")
        expect(f"{page}: one '{T('js.pad_write')}' per task ({n}), in its card before the model answer", n > 0 and ok and pg.locator(".pad-open").count() == n)
        card = pg.locator("section.practice-task[id] > .task-card").first
        rv = card.locator(":scope > details.reveal")
        rv.locator(":scope > summary").scroll_into_view_if_needed(); rv.locator(":scope > summary").click()
        expect(f"{page}: the model answer and rubric stay locked, in view, until the student writes a solution (teacher 2026-11-06)", rv.is_visible() and not rv.evaluate("(d) => d.open")
               and T("js.locked_done") in rv.locator(":scope > summary").inner_text() and card.locator("label.solved").count() == 0)
        tp = ctx.new_page(); tp.goto(BASE + page + "?ratkaisut=1"); tp.wait_for_load_state("load")
        expect(f"{page}: ?ratkaisut=1 opens every lock for the teacher", tp.locator("[data-locked]").count() == 0 and tp.locator(".teacher-note").count() == 1)
        tp.close(); pg.bring_to_front()
        card.locator(".pad-open").scroll_into_view_if_needed(); card.locator(".pad-open").click()
        card.locator(".rich-text-editor").wait_for(timeout=20000)
        rv.locator(":scope > summary").scroll_into_view_if_needed(); rv.locator(":scope > summary").click()
        expect(f"{page}: an empty editor keeps them locked", not rv.evaluate("(d) => d.open"))
        card.locator(".rich-text-editor").click()
        pg.keyboard.type("a) "); pg.keyboard.press("Control+e"); pg.keyboard.type("P=UI"); pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
        rv.locator(":scope > summary").click()
        expect(f"{page}: a written solution opens them", rv.evaluate("(d) => d.open")); rv.evaluate("(d) => { d.open = false; }")
        card.locator(".pad-copy").click(); pg.wait_for_timeout(300)
        clip = pg.evaluate("async () => { for (const it of await navigator.clipboard.read()) return await (await it.getType('text/plain')).text(); }")
        expect(f"{page}: the solution is copied", (clip or "").replace("\u00a0", " ") == "a) \\(P=UI\\)", clip)
        for w in (360, 1280):
            pg.set_viewport_size({"width": w, "height": 800}); pg.wait_for_timeout(200)
            m = pg.evaluate("""() => { const c = document.querySelector('section.practice-task[id] > .task-card'), e = c.querySelector('.rich-text-editor').getBoundingClientRect(), r = c.getBoundingClientRect();
                return { scroll: document.documentElement.scrollWidth - innerWidth, inside: e.left >= r.left - 1 && e.right <= r.right + 1 }; }""")
            expect(f"{page} {w} px: the open editor fits the task card, no horizontal scroll", m["scroll"] <= 0 and m["inside"], m)
        expect(f"{page}: no script errors", not errs, errs)
        ctx.close()
    # Phase 2: the solutions are kept on this device (templates/padstore.js, teacher 2026-11-01)
    page = targets[0]; lang = page.split("/")[0] if "/" in page else i18n.SOURCE; T = i18n.T(lang)
    ctx = b.new_context(viewport={"width": 1280, "height": 900}, permissions=["clipboard-read", "clipboard-write"], accept_downloads=True)
    sent = []
    ctx.on("request", lambda r: sent.append((r.method, r.url, r.post_data or "")))
    pg = ctx.new_page(); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("dialog", lambda d: d.accept())
    LI = "#exercises li[id]:has(> .task)"

    def visit():
        pg.goto(BASE + page); pg.wait_for_load_state("load")
        pg.evaluate("document.querySelectorAll('#exercises details.level').forEach(d => { d.open = true; })")

    def editor(n):
        li = pg.locator(LI).nth(n)
        if li.locator(".pad").get_attribute("hidden") is not None or not li.locator(".rich-text-editor").count():
            li.locator(".pad-open").scroll_into_view_if_needed(); li.locator(".pad-open").click()
        li.locator(".rich-text-editor").wait_for(timeout=20000)
        return li

    def saved(li):
        try:
            pg.wait_for_function("(el) => el.textContent === %s" % repr(T("js.pad_saved")).replace("'", '"'), arg=li.locator(".pad-save").element_handle(), timeout=5000)
            return True
        except Exception:
            return False

    visit()
    ids = pg.evaluate(f"[...document.querySelectorAll('{LI}')].slice(0, 2).map(li => li.id)")
    a = editor(0); a.locator(".rich-text-editor").click()
    pg.keyboard.type("Muisti A: "); pg.keyboard.press("Control+e"); pg.keyboard.type("x^2"); pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
    expect(f"{page}: a change shows '{T('js.pad_saving')}' and then '{T('js.pad_saved')}'", saved(a), a.locator(".pad-save").inner_text())
    bb = editor(1); bb.locator(".rich-text-editor").click(); pg.keyboard.type("Muisti B ")
    pg.evaluate("""async () => { const c = document.createElement('canvas'); c.width = 20; c.height = 10; const g = c.getContext('2d'); g.fillStyle = '#c00'; g.fillRect(0, 0, 20, 10);
        const blob = await new Promise(r => c.toBlob(r, 'image/png')); await navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]); }""")
    bb.locator(".rich-text-editor").click(); pg.keyboard.press("End"); pg.keyboard.press("Control+v"); pg.wait_for_timeout(600)
    expect(f"{page}: a pasted picture goes into the editor", bb.locator(".rich-text-editor img[src^='data:image/png']").count() == 1, bb.locator(".rich-text-editor").inner_html()[:200])
    saved(bb)
    visit()
    a = editor(0)
    expect(f"{page}: after reloading, the solution comes back ({T('js.pad_restored')})", "Muisti A" in a.locator(".rich-text-editor").inner_text() and a.locator(".pad-save").inner_text() == T("js.pad_restored"), a.locator(".rich-text-editor").inner_html()[:200])
    f = a.locator(".rich-text-editor img[data-math-image]")
    expect(f"{page}: the restored formula is a formula with its LaTeX", f.count() == 1 and f.first.get_attribute("alt") == "x^2")
    if f.count():
        f.first.click(); pg.wait_for_timeout(400)
        expect(f"{page}: the restored formula opens in the formula editor (still editable)", pg.locator(".mq-editable-field").count() > 0 and "x^2" in pg.locator("textarea, .math-editor-latex-field, [contenteditable]").evaluate_all("els => els.map(e => e.value || e.textContent).join(' ')"))
        pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    bb = editor(1)
    expect(f"{page}: a second exercise keeps its own solution, picture included", "Muisti B" in bb.locator(".rich-text-editor").inner_text() and "Muisti A" not in bb.locator(".rich-text-editor").inner_text()
           and bb.locator(".rich-text-editor img[src^='data:image/png']").count() == 1)
    a.locator(".pad-copy").first.click(); pg.wait_for_timeout(300)
    clip = pg.evaluate("async () => { for (const it of await navigator.clipboard.read()) return { h: await (await it.getType('text/html')).text(), t: await (await it.getType('text/plain')).text() }; }")
    expect(f"{page}: Kopioi ratkaisu still copies a restored solution (HTML and plain text)", 'alt="x^2"' in clip["h"] and "\\(x^2\\)" in clip["t"], clip)
    with pg.expect_download() as dl:
        a.locator(".pad-saved > summary").click(); a.locator(".pad-saved button").nth(0).click()
    backup = pathlib.Path(dl.value.path()).read_text()
    data = __import__("json").loads(backup)
    # on a module's page (FY1-FY8) the backup is the module's work file (palautus.js flWork, teacher 2026-11-07, test_tehty.py)
    sols = data["store"]["solutions"] if data.get("format") == "ruukkilabra-tyo" else data.get("solutions", [])
    expect(f"{page}: the backup file is versioned and holds both solutions", data.get("format") in ("ruukkilabra-tyo", "ruukkilabra-ratkaisut") and data.get("version") == 1
           and sorted(r["id"] for r in sols) == sorted(ids), {k: data.get(k) for k in ("format", "version")})
    work = data.get("format") == "ruukkilabra-tyo"
    a.locator(".pad-saved button").nth(2).click(); pg.wait_for_timeout(500)   # Poista kaikki (the dialog is accepted)
    expect(f"{page}: Poista kaikki empties the open editors", a.locator(".rich-text-editor").inner_text().strip() == "" and bb.locator(".rich-text-editor").inner_text().strip() == "")
    visit(); a = editor(0)
    expect(f"{page}: after Poista kaikki nothing comes back", a.locator(".rich-text-editor").inner_text().strip() == "")
    tmp = ROOT / "preview" / "writepad-backup.json"; tmp.parent.mkdir(exist_ok=True); tmp.write_text(backup)
    a.locator(".pad-saved > summary").click()
    if work:   # the work file is opened whole and the page reloads (palautus.js open)
        with pg.expect_navigation(): a.locator(".pad-saved input[type=file]").set_input_files(str(tmp))
        pg.evaluate("document.querySelectorAll('#exercises details.level').forEach(d => { d.open = true; })"); a = editor(0); a.locator(".pad-saved > summary").click()
    else: a.locator(".pad-saved input[type=file]").set_input_files(str(tmp)); pg.wait_for_timeout(600)
    expect(f"{page}: importing the backup brings the open editor's solution back", "Muisti A" in a.locator(".rich-text-editor").inner_text(), a.locator(".pad-status").inner_text())
    bad = ROOT / "preview" / "writepad-bad.json"; bad.write_text('{"format": "something else"}')
    a.locator(".pad-saved input[type=file]").set_input_files(str(bad)); pg.wait_for_timeout(300)
    expect(f"{page}: a file that is not a backup is refused with a message", a.locator(".pad-status").inner_text() == T("js.palautus_broken" if work else "js.pad_import_failed"), a.locator(".pad-status").inner_text())
    visit(); bb = editor(1)
    expect(f"{page}: after reloading, the imported solutions of other exercises are there too", "Muisti B" in bb.locator(".rich-text-editor").inner_text())
    a = editor(0); a.locator(".pad-delete").click(); pg.wait_for_timeout(400)
    visit(); a = editor(0); bb = editor(1)
    expect(f"{page}: Poista ratkaisu deletes one exercise's solution and keeps the others", a.locator(".rich-text-editor").inner_text().strip() == "" and "Muisti B" in bb.locator(".rich-text-editor").inner_text())
    pg.evaluate("""(id) => new Promise((ok) => { indexedDB.open('ruukkilabra-ratkaisut').onsuccess = (e) => {
        const tx = e.target.result.transaction('solutions', 'readwrite'); tx.objectStore('solutions').put({ id, html: 42 }); tx.oncomplete = ok; }; })""", ids[0])
    visit(); a = editor(0)
    expect(f"{page}: a damaged record is reported, not shown or claimed as saved", a.locator(".pad-save").inner_text() == T("js.pad_save_corrupt"), a.locator(".pad-save").inner_text())
    other = [x for x in sent if x[0] != "GET" or "Muisti" in x[1] or "Muisti" in x[2] or not x[1].startswith(BASE)]
    expect(f"{page}: no answer is sent over the network (only GET requests for the site's own files)", not other, other[:3])
    expect(f"{page}: no script errors while saving and restoring", not errs, errs)
    ctx.close()
    # a pasted picture's size (teacher 2026-11-06, "haluan pienentää kuvaa"): the bar's sizes and the corner handle,
    # kept after a reload, at a phone's and a laptop's width
    for w in (360, 1280):
        ctx = b.new_context(viewport={"width": w, "height": 900}, permissions=["clipboard-read", "clipboard-write"])
        pg = ctx.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        visit(); a = editor(0); ed = a.locator(".rich-text-editor"); ed.click(); pg.keyboard.type("Kuva: ")
        pg.evaluate("""async () => { const c = document.createElement('canvas'); c.width = 1600; c.height = 800; const g = c.getContext('2d'); g.fillStyle = '#06c'; g.fillRect(0, 0, 1600, 800);
            const blob = await new Promise(r => c.toBlob(r, 'image/png')); await navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]); }""")
        ed.click(); pg.keyboard.press("End"); pg.keyboard.press("Control+v"); pg.wait_for_timeout(600)
        img = ed.locator("img:not([data-math-image])").first
        img.click(); pg.wait_for_timeout(100)
        bar, handle = a.locator(".pad-img-bar"), a.locator(".pad-img-handle")
        labels = [T(f"js.pad_img_{k}") for k in ("small", "medium", "large", "original")]
        expect(f"{page} {w}px: a click on a pasted picture shows its size bar and corner handle", bar.is_visible() and handle.is_visible() and bar.locator("button").all_inner_texts() == labels, bar.locator("button").all_inner_texts())
        room = pg.evaluate("(e) => { const s = getComputedStyle(e); return e.clientWidth - parseFloat(s.paddingLeft) - parseFloat(s.paddingRight); }", ed.element_handle())
        bar.locator("button").nth(0).click(); pg.wait_for_timeout(100)
        expect(f"{page} {w}px: {labels[0]} makes the picture a quarter of the editor's width", abs(img.bounding_box()["width"] - room / 4) <= 2 and abs(int(img.get_attribute("width") or 0) - room / 4) <= 1, (img.get_attribute("width"), room))
        expect(f"{page} {w}px: the size bar fits the window and its buttons are at least 40 px high", pg.evaluate("document.documentElement.scrollWidth <= innerWidth")
               and bar.bounding_box()["x"] >= 0 and bar.bounding_box()["x"] + bar.bounding_box()["width"] <= w and all(bb_["height"] >= 40 for bb_ in [x.bounding_box() for x in bar.locator("button").all()]))
        h = handle.bounding_box(); x, y = h["x"] + h["width"] / 2, h["y"] + h["height"] / 2
        pg.mouse.move(x, y); pg.mouse.down(); pg.mouse.move(x + 40, y, steps=4); pg.mouse.up(); pg.wait_for_timeout(100)
        dragged = int(img.get_attribute("width") or 0)
        expect(f"{page} {w}px: dragging the corner handle makes the picture bigger", abs(dragged - (room / 4 + 40)) <= 2, (dragged, room))
        expect(f"{page} {w}px: the new size is saved", saved(a), a.locator(".pad-save").inner_text())
        visit(); a = editor(0); img = a.locator(".rich-text-editor img:not([data-math-image])").first
        expect(f"{page} {w}px: after reloading, the picture has the size it was given", img.get_attribute("width") == str(dragged), img.get_attribute("width"))
        img.click(); a.locator(".pad-img-bar button").nth(3).click(); pg.wait_for_timeout(100)
        expect(f"{page} {w}px: {labels[3]} gives the picture its own size again (at most the editor's width)", img.get_attribute("width") is None and abs(img.bounding_box()["width"] - min(room, 1600)) <= 2, img.get_attribute("width"))
        pg.locator("h1").first.click(); pg.wait_for_timeout(100)
        expect(f"{page} {w}px: a click elsewhere hides the size bar", not a.locator(".pad-img-bar").is_visible())
        if w == 1280: a.screenshot(path=str(ROOT / "preview" / "writepad-image-size.png"))
        expect(f"{page} {w}px: no script errors while resizing a picture", not errs, errs)
        ctx.close()
    # storage failure: the write throws QuotaExceededError -> an error is shown, never "Tallennettu"
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    ctx.add_init_script("IDBObjectStore.prototype.put = function () { throw new DOMException('full', 'QuotaExceededError'); };")
    pg = ctx.new_page(); visit(); a = editor(0); a.locator(".rich-text-editor").click(); pg.keyboard.type("Ei mahdu"); pg.wait_for_timeout(1500)
    expect(f"{page}: a full storage shows its error and never claims the solution is saved", a.locator(".pad-save").inner_text() == T("js.pad_save_quota"), a.locator(".pad-save").inner_text())
    ctx.close()
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    ctx.add_init_script("Object.defineProperty(window, 'indexedDB', { get() { throw new Error('blocked'); } });")
    pg = ctx.new_page(); visit(); a = editor(0); a.locator(".rich-text-editor").click(); pg.keyboard.type("Ei tallennu"); pg.wait_for_timeout(1500)
    expect(f"{page}: a browser that does not allow storage says so, and the editor still works", a.locator(".pad-save").inner_text() == T("js.pad_save_unavailable") and "Ei tallennu" in a.locator(".rich-text-editor").inner_text(), a.locator(".pad-save").inner_text())
    ctx.close()
    b.close()
srv.shutdown()
print("FAILURES:", fails) if fails else print("all ok")
sys.exit(1 if fails else 0)
