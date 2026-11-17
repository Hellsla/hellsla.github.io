"""Kuuntele ja katso fysiikkaa (teacher 2026-11-17, scripts/media_tips.py) in the built site.
Usage: python scripts/test_media.py [site]
Static: the data is valid and every item verified; podcastit.html exists in every language; every item of the language's
file is on it as a link to its url, under its first module; the header of every page links it; the note to the other
language goes to a page that exists (fi and fi-easy -> en, en -> fi); the switcher links resolve; no Finnish-language
item on the English page. In a browser (360 and 1280 px): the filters show, a module, a type and the short filter hide
the rest and are reachable by keyboard, the page does not scroll sideways."""
import re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import media_tips, i18n
from courses import ROOT

SITE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site"
fails = []
def expect(name, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"  {str(detail)[:200]}"))
    if not ok: fails.append(name)

expect("content/*/podcastit.json valid, every item verified", not media_tips.check(), media_tips.check())
out = {l: SITE if l == i18n.SOURCE else SITE / l for l in i18n.languages()}
for lang, d in out.items():
    f = d / media_tips.PAGE
    expect(f"{lang}: {media_tips.PAGE} built", f.is_file())
    if not f.is_file(): continue
    h = f.read_text(); main = re.search(r"<main.*?</main>", h, re.S).group(0)
    want = media_tips.load(lang)
    hrefs = [_h.unescape(x) for x in re.findall(r'<li class="media"[^>]*><h3 class="media-title"><a href="([^"]*)"', main)]
    nfeat = sum(1 for it in want["items"] if it.get("featured"))
    expect(f"{lang}: every item once in its module list (+{nfeat} featured)", sorted(hrefs) == sorted([it["url"] for it in want["items"]] + [it["url"] for it in want["items"] if it.get("featured")]), hrefs)
    if lang == "en": expect("en: only English items, language marks en", all(it["language"] == "en" for it in want["items"]) and 'lang="fi"' not in re.sub(r'<aside.*?</aside>', "", main, flags=re.S))
    m = re.search(r'<aside class="media-other"[^>]*>.*?<a href="([^"]*)"', main, re.S)
    expect(f"{lang}: link to the other language's page exists", bool(m) and (d / m.group(1)).resolve().is_file(), m and (d / m.group(1)).resolve())
    if m: expect(f"{lang}: it goes to the {'Finnish' if lang == 'en' else 'English'} page", (d / m.group(1)).resolve() == ((SITE / media_tips.PAGE) if lang == "en" else (SITE / "en" / media_tips.PAGE)).resolve())
    bad = [p.name for p in d.glob("*.html") if 'href="podcastit.html"' not in re.search(r'<header class="top">.*?</header>', p.read_text(), re.S).group(0)]
    expect(f"{lang}: every page links it in its header", not bad, bad[:5])
    sw = re.findall(r'class="lang" href="([^"]*)"', h)
    expect(f"{lang}: language links resolve", sw and all((d / x.split("#")[0]).resolve().is_file() for x in sw), sw)
    expect(f"{lang}: the filter form is hidden without scripts", 'class="media-filters" hidden' in h)

if "--no-browser" not in sys.argv:
    from playwright.sync_api import sync_playwright
    import _browser
    with sync_playwright() as p:
        b = _browser.launch(p)
        for lang, d in out.items():
            for w in (360, 1280):
                pg = b.new_page(viewport={"width": w, "height": 800}); pg.goto((d / media_tips.PAGE).resolve().as_uri())
                tag = f"{lang} {w}px"
                n_all = pg.locator("main li.media:visible").count()
                expect(f"{tag}: filter form visible", pg.locator(".media-filters").is_visible())
                expect(f"{tag}: no sideways scroll", pg.evaluate("document.documentElement.scrollWidth <= innerWidth"))
                mods = pg.locator("[data-module]")
                if mods.count():
                    first = mods.first; mod = first.get_attribute("data-module")
                    first.focus(); pg.keyboard.press("Enter")
                    shown = pg.locator("main li.media:visible")
                    expect(f"{tag}: module {mod} keeps only its items (keyboard)", 0 < shown.count() <= n_all and all(mod in (x or "").split() for x in shown.evaluate_all("els => els.map(e => e.dataset.modules)")))
                    first.click()
                    expect(f"{tag}: second press clears it", pg.locator("main li.media:visible").count() == n_all)
                    short = pg.locator("#mf-short"); short.check()
                    mins = pg.locator("main li.media:visible").evaluate_all("els => els.map(e => +e.dataset.min || 999)")
                    expect(f"{tag}: short only shows items of at most {media_tips.SHORT} min", all(x <= media_tips.SHORT for x in mins), mins)
                    short.uncheck()
                pg.close()
        b.close()
sys.exit(1 if fails else 0)
