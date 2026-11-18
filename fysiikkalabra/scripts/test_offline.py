#!/usr/bin/env python3
"""Offline use: the service worker (templates/sw.js, templates/offline.js; work queue 17a PR 1, teacher 2026-11-15).
Usage: python scripts/test_offline.py [site]

The built site is served over http on localhost (a service worker needs https or localhost), then in a browser:
  - the page registers the worker and, after the first visit, works offline: text, KaTeX, the simulation and a
    task's answer check; a page never visited fails with the browser's own error page
  - a visited page opens offline with or without a query (?ratkaisut=1)
  - online the newest page wins (network first): a changed page replaces the cached one, offline shows the change
  - the read-aloud model (models/) and recordings (audio/) are never cached; the model's own cache survives
  - a new worker replaces the old one and removes the caches of an older schema, leaving fl-tts-supertonic3-v1
  - the emergency switch (templates/sw-kill.js published as sw.js) unregisters the worker and empties its caches
  - installable site (17a PR 2): a manifest per language folder (start page, scope, three icons of the right pixel size) linked from every page;
    navigator.storage.persist() is asked for once, after the first fl:attempt and not before, and never in Firefox (it would prompt)
  - the files are written: site/sw.js and site/offline.js at the root, every page of every language loads offline.js
Exit status 1 on any failure."""
import functools, http.server, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright, Error as PwError

SITE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "site")
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


# files
expect("site/sw.js is at the root and has no placeholder left", (SITE / "sw.js").is_file() and "__FL_BUILD__" not in (SITE / "sw.js").read_text())
expect("site/offline.js is at the root", (SITE / "offline.js").is_file())
missing = [str(p.relative_to(SITE)) for p in SITE.rglob("*.html") if "vendor" not in p.relative_to(SITE).parts
           and "<main" in p.read_text(errors="ignore") and "offline.js" not in p.read_text(errors="ignore")
           and p.relative_to(SITE).parts[0] not in ("laskuri", "tyokalut")]   # the standalone tools are single files, not the site's pages
expect("every page with the shared header or the lesson template loads offline.js", not missing, missing[:5])

# manifest and icons (17a PR 2)
import json, struct
for d in [SITE] + [x for x in sorted(SITE.iterdir()) if x.is_dir() and (x / "index.html").is_file() and x.name not in ("vendor", "sims", "pics", "brand", "laskuri", "tyokalut")]:
    try: m = json.loads((d / "manifest.webmanifest").read_text())
    except (OSError, ValueError): m = None
    nm = d.name if d != SITE else "root"
    expect(f"{nm}: manifest.webmanifest exists with its front page as start_url and its folder as scope",
           bool(m) and (d / m["start_url"]).is_file() and m["scope"] == "./" and m["display"] == "standalone" and m["name"] and m["short_name"], m)
    ok = bool(m) and {(i["sizes"], i["purpose"]) for i in m["icons"]} == {("192x192", "any"), ("512x512", "any"), ("512x512", "maskable")}
    for i in (m["icons"] if m else []):
        f = (d / i["src"]).resolve(); w, h = struct.unpack(">II", f.read_bytes()[16:24]) if f.is_file() else (0, 0)
        ok = ok and f"{w}x{h}" == i["sizes"]
    expect(f"{nm}: the manifest's icons exist at their stated size, one of them maskable", ok)
    pages = [x for x in d.glob("*.html") if "<main" in x.read_text(errors="ignore") and x.name != "404.html"]
    nolink = [x.name for x in pages if 'rel="manifest" href="manifest.webmanifest"' not in x.read_text(errors="ignore")]
    expect(f"{nm}: every page links the manifest", not nolink, nolink[:5])

OVERRIDE = {}


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header("Cache-Control", "no-store"); super().end_headers()
    def do_GET(self):
        path = self.path.split("?")[0]
        if path in OVERRIDE:
            body, ctype = OVERRIDE[path]
            self.send_response(200); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
            self.end_headers(); self.wfile.write(body); return
        super().do_GET()


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Handler, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{srv.server_address[1]}/"

lid = next((p.stem for p in sorted(SITE.glob("fy*-*.html")) if 'class="check"' in p.read_text() and "sim-embed.js" in p.read_text()), None)
other = next((p.name for p in sorted(SITE.glob("fy*-*.html")) if p.stem != lid), None)
if not lid or not other:
    print("FAIL no lesson page with a task check and a simulation"); sys.exit(1)

def ev(expr, tries=8):
    """pg.evaluate that survives the page navigating under it (the worker taking control can reload the page: 'Execution context was
    destroyed'): wait for the page to settle and run it again."""
    for i in range(tries):
        try:
            return pg.evaluate(expr)
        except PwError as e:
            if i == tries - 1 or not re.search(r"context was destroyed|navigation|Target (page|closed)", str(e)): raise
            try: pg.wait_for_load_state("load", timeout=10000)
            except PwError: pass
            pg.wait_for_timeout(250)


def until(expr, tries=60):
    """Poll a promise-valued expression in the page; wait_for_function does not await an async function."""
    for _ in range(tries):
        try:
            if ev(expr): return True
        except PwError: pass                                    # the page reloaded under us
        pg.wait_for_timeout(250)
    return False


pg = None
with sync_playwright() as pw:
    b = launch(pw)
    ctx = b.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
    errors = []; pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(URL + f"{lid}.html"); until("navigator.serviceWorker.ready.then(() => true)")
    # seed what an older worker and the read-aloud feature would have: a stale schema cache and the model's cache
    ev("""async () => { await caches.open('fl-sw-0-old'); const t = await caches.open('fl-tts-supertonic3-v1'); await t.put('/m.bin', new Response('model')); }""")
    until("caches.keys().then(a => a.some(k => k.startsWith('fl-sw-1-static')))")
    pg.wait_for_timeout(1500)                                  # the warm-up of the files the page had already loaded
    expect("the worker is registered and controls the page after one visit",
           ev("navigator.serviceWorker.getRegistration().then(r => !!(r && r.active))"))
    ev("fetch('models/x.bin').catch(() => 0); fetch('audio/fi/x.mp3').catch(() => 0)"); pg.wait_for_timeout(500)
    keys = ev("""async () => { const o = []; for (const k of await caches.keys()) for (const r of await (await caches.open(k)).keys()) o.push(k + ' ' + r.url); return o; }""")
    expect("models/ and audio/ are never cached", not any(re.search(r"/(models|audio)/", k) for k in keys if "fl-sw-" in k), keys[:3])
    expect("the main files are cached (page, script, KaTeX, simulation library)", all(any(x in k for k in keys) for x in (f"/{lid}.html", "lesson.js", "katex.min.js", "p5.min.js")),
           [k for k in keys][:8])
    # online: a changed page wins; offline shows what was last seen
    page_bytes = (SITE / f"{lid}.html").read_bytes()
    OVERRIDE[f"/{lid}.html"] = (page_bytes.replace(b"</body>", b"<p id=\"v2\">v2</p></body>"), "text/html; charset=utf-8")
    pg.goto(URL + f"{lid}.html"); pg.wait_for_timeout(500)
    expect("online the newest page is shown (network first)", pg.query_selector("#v2") is not None)
    pg.goto(URL + f"{lid}.html?ratkaisut=1"); pg.wait_for_timeout(300)
    del OVERRIDE[f"/{lid}.html"]
    ctx.set_offline(True)
    pg.goto(URL + f"{lid}.html"); pg.wait_for_timeout(800)
    expect("offline the last seen page opens, also without the query it was cached with", pg.query_selector("#v2") is not None and pg.title() != "")
    pg.goto(URL + f"{lid}.html?simloop=1"); pg.wait_for_timeout(1500)
    expect("a query part does not stop the page from being found in the cache", pg.query_selector("main, article") is not None and pg.query_selector("#v2") is not None)
    pg.goto(URL + f"{lid}.html"); pg.wait_for_timeout(2500)
    expect("offline: KaTeX has typeset the formulas", ev("document.querySelectorAll('.katex').length") > 0)
    expect("offline: the simulation draws", ev("[...document.querySelectorAll('canvas')].some(c => c.width > 0)"),
           ev("document.querySelectorAll('canvas').length"))
    form = pg.query_selector("form.check")
    ans = form.get_attribute("data-answer")
    form.evaluate("(f, a) => { f.querySelector('input').value = a; f.requestSubmit(); }", ans.replace(".", ","))   # the form sits in a closed stage; the check itself is what is tested
    pg.wait_for_timeout(300)
    expect("offline: a task's answer check works", form.query_selector("output").get_attribute("data-state") == "ok",
           form.query_selector("output").inner_text())
    expect("offline: no script error", not errors, errors[:3])
    try:
        pg.goto(URL + other); never = False
    except PwError:
        never = True
    expect("a page never visited fails with the browser's own error page", never)
    ctx.set_offline(False)

    # a new worker: the stale schema's cache goes, the read-aloud model's cache stays
    sw = (SITE / "sw.js").read_text()
    OVERRIDE["/sw.js"] = (("// next release\n" + sw).encode(), "text/javascript")
    pg.goto(URL + f"{lid}.html")
    ev("navigator.serviceWorker.getRegistration().then(r => r.update())")
    until("caches.keys().then(a => !a.includes('fl-sw-0-old'))")
    names = ev("caches.keys()")
    expect("a new worker removes the caches of an older schema and keeps the read-aloud model's", "fl-sw-0-old" not in names and "fl-tts-supertonic3-v1" in names, names)

    # the emergency switch
    OVERRIDE["/sw.js"] = ((ROOT / "templates" / "sw-kill.js").read_bytes(), "text/javascript")
    ev("navigator.serviceWorker.getRegistration().then(r => r.update())")
    until("navigator.serviceWorker.getRegistrations().then(a => a.length === 0)")
    names = ev("caches.keys()")
    expect("the emergency switch unregisters the worker and empties its caches, leaving the read-aloud model's", names == ["fl-tts-supertonic3-v1"], names)
    # persistent storage: asked after the first attempt, once, silently; Firefox is left out
    for ua, want in (("Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0 Safari/537.36", 1), ("Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0", 0)):
        c2 = b.new_context(user_agent=ua); p2 = c2.new_page()
        p2.add_init_script("window.__persist = 0; Object.defineProperty(navigator, 'storage', {value: {persisted: () => Promise.resolve(false), persist: () => { window.__persist++; return Promise.resolve(true); }}});")
        p2.goto(URL + f"{lid}.html"); p2.wait_for_timeout(800)
        before = p2.evaluate("window.__persist")
        p2.evaluate("() => { const e = new CustomEvent('fl:attempt', {bubbles: true, detail: {id: 'x', kind: 'check', state: 'no'}}); document.body.dispatchEvent(e); document.body.dispatchEvent(e); }")
        p2.wait_for_timeout(300)
        expect(f"persist() is not asked before an attempt and {'once' if want else 'never'} after it ({'Chromium/Safari' if want else 'Firefox'})",
               before == 0 and p2.evaluate("window.__persist") == want, (before, p2.evaluate("window.__persist")))
        c2.close()
    b.close()
srv.shutdown()
print("test_offline: " + ("FAIL" if fails else "PASS")); sys.exit(1 if fails else 0)
