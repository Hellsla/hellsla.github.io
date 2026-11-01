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
        items = re.findall(r'<li id="[^"]+"[^>]*>(?:<span class="ex-core">[^<]*</span>)?<p class="task"', m.group(1))
        tasks = m.group(1).count('class="task"')
        if tasks: pages.setdefault(lang, []).append(f.relative_to(SITE).as_posix())
        if len(items) != tasks:
            expect(f"{lang} {f.name}: every exercise is an <li id> with its p.task", False, f"{len(items)} of {tasks}")
for lang in pages:
    expect(f"{lang}: {len(pages[lang])} published lessons have exercises", True)

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
            const b = li.querySelector(':scope > .pad-open'), a = li.querySelector(':scope > details.answer'), s = li.querySelector(':scope > details.solution'), f = li.querySelector(':scope > form.check');
            return b && [a, s, f].every(x => !x || (b.compareDocumentPosition(x) & 4)) && (!f || (b.nextElementSibling.classList.contains('pad') && (b.nextElementSibling.compareDocumentPosition(f) & 4))); })""")
        expect(f"{page}: the button and editor come after the task and before its answer box, answer and model solution (write first, then check)", order)
        head = pg.evaluate("""() => [...document.querySelectorAll('#exercises li[id]')].every(li => {
            const h = li.firstElementChild, t = h && [...h.querySelectorAll('.ex-toggle')], d = [...li.querySelectorAll(':scope > details.answer, :scope > details.solution')];
            return h && h.classList.contains('ex-head') && t.length === d.length && t.every((b, i) => b.getAttribute('aria-controls') === d[i].id && b.textContent === d[i].querySelector('summary').textContent)
                && (!li.querySelector('.ex-core') || h.contains(li.querySelector('.ex-core'))) && d.every(x => !x.open && x.querySelector('summary').offsetHeight === 0); })""")
        expect(f"{page}: Vastaus and Näytä ratkaisu are buttons in the exercise's top row beside its tag (teacher 2026-11-01)", head)
        tg = pg.locator("#exercises li[id] .ex-toggle").first
        tg.scroll_into_view_if_needed(); tg.click()
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
                         small: [...li.querySelectorAll('.pad-open,.pad-copy')].filter(b => b.getBoundingClientRect().height < 40).length }; }""", li.get_attribute("id"))
            expect(f"{page} {w} px: the open editor fits the exercise, no horizontal scroll, buttons 40 px", m["scroll"] <= 0 and m["inside"] and not m["small"], m)
            if w in (360, 1280):
                li.locator(".pad").scroll_into_view_if_needed()
                shot = ROOT / "preview" / "writepad"; shot.mkdir(parents=True, exist_ok=True)
                li.screenshot(path=str(shot / f"{page.replace('/', '_')}-{w}.png"))
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
            const card = s.querySelector(':scope > .task-card'), b = card && card.querySelector(':scope > .pad-open'), r = card && card.querySelector(':scope > details.reveal');
            return b && b.textContent && r && (b.compareDocumentPosition(r) & 4); })""")
        expect(f"{page}: one '{T('js.pad_write')}' per task ({n}), in its card before the model answer", n > 0 and ok and pg.locator(".pad-open").count() == n)
        card = pg.locator("section.practice-task[id] > .task-card").first
        card.locator(".pad-open").scroll_into_view_if_needed(); card.locator(".pad-open").click()
        card.locator(".rich-text-editor").wait_for(timeout=20000)
        pg.keyboard.type("a) "); pg.keyboard.press("Control+e"); pg.keyboard.type("P=UI"); pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
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
    b.close()
srv.shutdown()
print("FAILURES:", fails) if fails else print("all ok")
sys.exit(1 if fails else 0)
