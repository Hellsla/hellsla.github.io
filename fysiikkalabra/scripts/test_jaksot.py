"""Jaksopohja (scripts/jaksot.py, teacher 2026-11-12): the units outside the physics modules share one folder layout.

- The real units: every folder of jaksot/ has the common header, the three page modules find their files through
  jaksot.py, a planned unit is on the front page's planned list from its folder alone (the fixture; Droonilab was one until it became Ahjo's course Dronelabra), and no source of a
  unit is left at the old places (the project's root, content/<lang>/).
- A unit without a page module (tests/jaksot/koejakso, a fixture that is never published): its pages come from
  jakso.json alone, a card per file of kohteet/, a language falls back to the Finnish file by file, and the checks
  name a wrong header, page, block, link, item or translation.

  python scripts/test_jaksot.py"""
import copy, json, pathlib, re, shutil, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import i18n, jaksot, local_courses, module_icons
import ahjo, kilparobo, lumatutor

fails = 0
def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"  -> {detail}"))
    if not ok: fails += 1

ROOT = jaksot.ROOT

# 1. the real units
ids = jaksot.ids()
expect("the units are folders of jaksot/: Ahjo, Kilparobotiikka and LUMA-tutor among them", {"ahjo", "kilparobo", "lumatutor"} <= set(ids), ids)
expect("every unit and translation has the common header", jaksot.validate(module_icons.ICONS) == [], jaksot.validate(module_icons.ICONS))
expect("the three page modules read their unit from jaksot/", [m.SOURCE for m in (ahjo, kilparobo, lumatutor)] == [jaksot.source(j) for j in ("ahjo", "kilparobo", "lumatutor")]
       and all(m.load()["jakso"]["id"] == j for m, j in ((ahjo, "ahjo"), (kilparobo, "kilparobo"), (lumatutor, "lumatutor"))))
old = [p for p in ([ROOT / f"{n}.json" for n in ("ahjo", "kilparobo", "lumatutor")] + [ROOT / "content" / l / n for l in i18n.languages() for n in ("ahjo", "ahjo.json", "kilparobo.json", "lumatutor", "lumatutor.json")]) if p.exists()]
expect("no unit's source is left at the root or in content/<lang>/", not old, [str(p.relative_to(ROOT)) for p in old])
expect("Ahjo's guides and LUMA-tutor's workshops are items of their units", ahjo.guide_file("ahjo-arduino", i18n.SOURCE) == jaksot.item_dir("ahjo") / "ahjo-arduino.md"
       and len(lumatutor.ws_files()) == len(list(jaksot.item_dir("lumatutor").glob("*.json"))) > 0)
for lang in i18n.languages():   # Dronelabra (teacher 2026-11-12) took Droonilab's place: a course of Ahjo, planned in the registry
    rows = local_courses.planned(lang)
    d = [r for r in rows if r["icon"] == "DRONELABRA"]
    expect(f"{lang}: Dronelabra is on the planned list once, with a title and a sentence; Droonilab and Myytinmurtajat are not", len(d) == 1 and d[0]["title"] == "Dronelabra" and d[0]["text"].endswith(".")
           and not any("yytinmurtaj" in r["title"] or r["icon"] in ("MYYTIT", "DROONILAB") for r in rows), rows)
expect("Dronelabra is a course of Ahjo, not a unit of its own", "droonilab" not in ids and "dronelabra" not in ids and "DRONELABRA" in [c["code"] for c in ahjo.load()["courses"]])
expect("Dronelabra's icon is in the module icons", "DRONELABRA" in module_icons.ICONS and module_icons.file("DRONELABRA").is_file() and "MYYTIT" not in module_icons.ICONS and "DROONILAB" not in module_icons.ICONS)

# 1b. Kilparobotiikka is written as pages of blocks: its five pages are drawn by jaksot.py from jakso.json alone
kd = jaksot.load("kilparobo")
expect("Kilparobotiikka: pages of blocks, the first the course page of the registry", jaksot.generic(kd) and kd["jakso"].get("course") == kilparobo.CODE
       and [p["file"] for p in kd["pages"]] == [kilparobo.PAGE, *kilparobo.SUBPAGES] and jaksot.front_row("kilparobo") is None)
expect("Kilparobotiikka: every block is of the shared library, and the module draws nothing itself", {b["type"] for _, b in jaksot.blocks_of(kd)} <= set(jaksot.BLOCKS)
       and not re.search(r"<(?:section|div|ul|ol|p|h[1-6])\b", pathlib.Path(kilparobo.__file__).read_text()))
body = kilparobo.path_body(kd, lambda rid: None)
expect("Kilparobotiikka: a page's body is the unit's menu with this page marked and its blocks in order", f'<a href="{kilparobo.PATH}" aria-current="page">' in body
       and body.count('<section class="kr-stage"') == 5 and body.index('class="kr-stage-index"') < body.index('id="ohjeet"'))
expect("Kilparobotiikka: a sentence that leads to a page is left out where that page is not built", "ahjo-projektipaivakirja.html" not in kilparobo.season_body(kd)
       and "ahjo-projektipaivakirja.html" in kilparobo.season_body(kd, "ahjo-projektipaivakirja.html") and kilparobo.block(kd, "paivakirja")["more"] not in kilparobo.season_body(kd))
expect("Kilparobotiikka: the start page takes its title block from the course registry", kilparobo.hub_body(kd, '<header id="x"><p class="local-desc">kuvaus</p></header>', "", "").startswith('<header id="x"></header><nav class="ahjo-nav kr-nav"'))

# 2. a unit without a page module, in a copy of the fixture
T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-jaksot-"))
real = jaksot.DIR
try:
    shutil.copytree(ROOT / "tests/jaksot", T / "jaksot"); jaksot.DIR = T / "jaksot"
    J = "koejakso"; src = jaksot.source(J); base = json.loads(src.read_text())
    expect("fixture: the unit is valid", jaksot.validate(module_icons.ICONS) == [], jaksot.validate(module_icons.ICONS))
    pages = jaksot.pages(J)
    expect("fixture: two pages from jakso.json, the first named after the unit", [p[0] for p in pages] == ["koejakso.html", "koejakso-turvallisuus.html"])
    body = pages[0][3]
    expect("fixture: one h1, the unit's name over it, the menu marks this page", body.count("<h1>") == 1 and '<p class="ahjo-eyebrow">Koejakso</p>' in body
           and '<a href="koejakso.html" aria-current="page">Aloitus</a>' in body and '<a href="koejakso-turvallisuus.html">Turvallisuus</a>' in body)
    expect("fixture: every block is a section named by its heading, in the file's order", re.findall(r'<section class="ahjo-sec kr-sec" id="([a-z-]+)" aria-labelledby="h-\1"><h2 id="h-\1">', body) == ["mika", "nain", "tyopajat", "lisaa"])
    expect("fixture: steps are a numbered list, a lead stands under its heading", '<p class="ahjo-sec-lead">Kolme askelta.</p><ol class="kr-steps"><li>Ilmoittaudu jaksolle.</li>' in body)
    expect("fixture: one card per file of kohteet/, in their order; an idea says so in words, a ready one says nothing",
           re.findall(r'<li class="kr-card"><h3>([^<]+)(?: <span class="ahjo-tag">([^<]+)</span>)?</h3>', body) == [("Droonin kokoaminen", ""), ("Lentoreitin ohjelmointi", "idea")])
    expect("fixture: an outside link opens in a new tab and says so; a page of the site is a plain link",
           '<a href="https://www.droneinfo.fi/" rel="external noopener" target="_blank">Traficomin droonisivut<span class="visually-hidden"> (avautuu uuteen välilehteen)</span></a>' in body
           and '<li><a href="koejakso-turvallisuus.html">Turvallisuus</a></li>' in body)
    expect("fixture: a card with href is one link", '<li class="kr-card kr-link-card"><a href="koejakso.html"><span class="kr-card-t">Tähystäjä</span>' in pages[1][3])
    expect("fixture: text is escaped", "&lt;b&gt;" in jaksot._block(J, base, {"type": "teksti", "id": "x", "title": "T", "text": ["<b>"]}, i18n.SOURCE))
    expect("fixture: a live unit with pages has its row for the front page", jaksot.front_row(J) == dict(base["front"], href="koejakso.html") and jaksot.planned() == [])

    # a new item is a new file; a language falls back to the Finnish file by file
    (jaksot.item_dir(J) / "kuvaus.json").write_text(json.dumps({"id": "kuvaus", "title": "Ilmakuvaus", "text": "Kuvaat koulun pihan.", "status": "luonnos", "order": 3}, ensure_ascii=False))
    expect("fixture: a new file in kohteet/ is a new card, no code", jaksot.validate() == [] and "Ilmakuvaus <span class=\"ahjo-tag\">luonnos</span>" in jaksot.pages(J)[0][3])
    en = copy.deepcopy(base); en["title"] = "Trial unit"; en["pages"][0]["title"] = "Trial unit"
    (src.parent / "en").mkdir(); (src.parent / "en" / "jakso.json").write_text(json.dumps(en, ensure_ascii=False))
    (src.parent / "en" / "kohteet").mkdir(); (src.parent / "en" / "kohteet" / "reitti.json").write_text(json.dumps({"id": "reitti", "title": "Programming a route", "text": "You program a square.", "status": "idea", "order": 2}))
    b_en = jaksot.pages(J, "en")[0][3]
    expect("fixture: a translation shows its own texts and items, the Finnish where it has none", jaksot.validate() == [] and "<h1>Trial unit</h1>" in b_en and "Programming a route" in b_en and "Droonin kokoaminen" in b_en)
    expect("fixture: a language without the unit's file shows the Finnish", jaksot.pages(J, "fi-easy")[0][1] == "Koejakso")

    # the checks name what is wrong
    def broken(change, part, lang=None):
        f = src if lang is None else src.parent / lang / "jakso.json"; keep = f.read_text()
        d = json.loads(keep); change(d); f.write_text(json.dumps(d, ensure_ascii=False))
        errs = jaksot.validate(module_icons.ICONS); f.write_text(keep)
        return any(part in e for e in errs), errs
    for name, change, part, lang in (
        ("a header with another id", lambda d: d["jakso"].update(id="muu"), "the folder is", None),
        ("an unknown status", lambda d: d["jakso"].update(status="valmis"), "jakso.status", None),
        ("an unknown theme", lambda d: d["jakso"].update(theme="sininen"), "jakso.theme", None),
        ("an extra header field", lambda d: d["jakso"].update(owner="x"), "nothing else", None),
        ("a first page not named after the unit", lambda d: d["pages"][0].update(file="etusivu.html"), "file is koejakso.html", None),
        ("an unknown block type", lambda d: d["pages"][0]["blocks"][0].update(type="taulukko"), "type is one of", None),
        ("two blocks with one id", lambda d: d["pages"][0]["blocks"][1].update(id="mika"), "its own on the page", None),
        ("an http link", lambda d: d["pages"][0]["blocks"][3]["links"][1].update(url="http://example.org/"), "https url", None),
        ("a text block without text", lambda d: d["pages"][0]["blocks"][0].update(text=[]), "text is a list", None),
        ("a planned unit without its front row", lambda d: (d["jakso"].update(status="planned"), d.pop("front")), 'has "front"', None),
        ("an icon that is not a module icon", lambda d: (d["jakso"].update(status="planned"), d["front"].update(icon="EIOLE")), "module_icons.ICONS", None),
        ("a translation with another header", lambda d: d["jakso"].update(status="planned"), "header differs", "en"),
        ("a translation that drops a block", lambda d: d["pages"][0]["blocks"].pop(), "differs from", "en"),
        ("a translation that changes a link", lambda d: d["pages"][0]["blocks"][3]["links"][0].update(href="muu.html"), "stay as in", "en"),
    ):
        ok, errs = broken(change, part, lang)
        expect(f"fixture: {name} is reported", ok, errs)
    bad = jaksot.item_dir(J) / "huono.json"; bad.write_text(json.dumps({"id": "toinen", "title": "T", "text": "x", "status": "kesken"}))
    e = jaksot.validate(); bad.unlink()
    expect("fixture: an item whose id is not its file's name, or with an unknown status, is reported", any("id is the file's name" in x for x in e) and any("status is one of" in x for x in e), e)
    (src.parent / "kuvat").mkdir(); e = jaksot.validate(); (src.parent / "kuvat").rmdir()
    expect("fixture: a folder that is neither kohteet/ nor a language is reported", any("a unit's folders are" in x for x in e), e)
    expect("fixture: a page name the site already has is reported", any("already in use" in x for x in jaksot.validate_pages(J, taken={"koejakso.html"})))
finally:
    jaksot.DIR = real; shutil.rmtree(T, ignore_errors=True)
expect("the fixture is not a unit of the site", "koejakso" not in jaksot.ids())

print("\nall jaksot tests passed" if not fails else f"\n{fails} FAILED"); sys.exit(1 if fails else 0)
