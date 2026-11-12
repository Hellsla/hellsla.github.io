"""Jaksopohja (teacher 2026-11-12): one folder layout, one registry and one set of helpers for every study unit outside
the physics modules FY1–FY14 (Ahjo, Kilparobotiikka, LUMA-tutor, Droonilab and whatever comes next), so that updating
one is the same work as updating another.

  jaksot/<id>/jakso.json           the unit in Finnish. Its first key is the same in every unit:
                                     "jakso": {"id": <the folder's name>, "status": "live" | "planned",
                                               "theme": "ahjo" | "kiviruukki" | "ruukkilabra"}
                                   (and "course": "<CODE>" where the unit's first page is the page of a course of
                                   local-courses.json: its title block, photos and students' accounts come from there)
                                   a planned unit also has "front": {"icon", "title", "text"}: its greyed row on the
                                   front page (the icon is a code of module_icons.ICONS). The rest of the file is the
                                   unit's own content. Ahjo, Kilparobotiikka and LUMA-tutor have a page module
                                   each (ahjo.py, kilparobo.py, lumatutor.py) for what only they have. A unit
                                   without one is written as "pages" (below) and needs no code; a planned unit
                                   has neither.
  jaksot/<id>/kohteet/             one file per item of the unit: a guide, a workshop, a project. A new item is a
                                   new file.
  jaksot/<id>/<lang>/jakso.json    the same in another language, with the same "jakso" header; a language without
  jaksot/<id>/<lang>/kohteet/      the file shows the Finnish one, item by item.
  jaksot/<id>/<lang>/…             other translated files of the unit (a figure's texts).

A unit without a page module (the generic pages, pages()): "title", "front" (its row on the front page) and
  "pages": [{"file": "<id>.html" for the first, "<id>-<name>.html" after it, "title", "nav" (its name in the unit's
             menu), "lead", "blocks": [...]}]
  a block is {"type", "id", "title", "lead" (optional)} and by its type:
    "teksti"   "text": [paragraphs]
    "lista"    "items": [lines]; "ordered": true numbers them (steps)
    "kortit"   "cards": [{"title", "text", "href" (optional, a page of the site)}], or "from": "kohteet": one card per
               file of kohteet/ ({"id", "title", "text", "status": "valmis" | "idea" | "luonnos", "order"}); a card that
               is not valmis shows its status in words ("ui": {"status": {"idea": …, "luonnos": …}})
    "linkit"   "links": [{"title", "href" (a page of the site) or "url" (https, opens in a new tab)}]
  The pages use the components Kilparobotiikka's pages are built of (site.css kr-head, kr-nav, kr-cards, kr-steps), in
  the unit's theme. A translation has the same files, ids, types and links.

This module is the only place that knows the layout: a unit's page module asks it for its files. It also holds the
helpers the page modules had each written for themselves (the line icon, the comparison of a translation's structure
with the source's, the list of a file's links).

Usage: python scripts/jaksot.py        list the units and check their headers"""
import json, re, sys, pathlib, html as _h
from urllib.parse import quote
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

DIR = ROOT / "jaksot"
FILE = "jakso.json"
ITEMS = "kohteet"
STATUSES = ("live", "planned")
THEMES = ("ahjo", "kiviruukki", "ruukkilabra")


def _rel(f):
    """A file's name in messages: from the folder that holds jaksot/."""
    return pathlib.Path(f).relative_to(DIR.parent)


def ids():
    """The units, in the order of their folders' names."""
    return sorted(p.name for p in DIR.iterdir() if (p / FILE).is_file()) if DIR.is_dir() else []


def source(jid): return DIR / jid / FILE


def data_file(jid, lang=i18n.SOURCE):
    """The unit's file in `lang`, or the Finnish one where the language has none."""
    f = DIR / jid / lang / FILE
    return f if lang != i18n.SOURCE and f.is_file() else source(jid)


def translations(jid):
    """The unit's files in the other languages that have one."""
    return sorted(p for p in (DIR / jid).glob(f"*/{FILE}"))


def load(jid, lang=i18n.SOURCE):
    return json.loads(data_file(jid, lang).read_text()) if source(jid).is_file() else None


def item_dir(jid, lang=i18n.SOURCE):
    return DIR / jid / ITEMS if lang == i18n.SOURCE else DIR / jid / lang / ITEMS


def item_file(jid, name, lang=i18n.SOURCE, fallback=True):
    """An item's file in `lang`; with fallback the Finnish one where the language has none; None if there is neither."""
    for f in ([item_dir(jid, lang) / name] if lang != i18n.SOURCE else []) + ([item_dir(jid) / name] if fallback or lang == i18n.SOURCE else []):
        if f.is_file(): return f
    return None


def item_files(jid, pattern, lang=i18n.SOURCE):
    """{stem: path} of the unit's items matching `pattern`: the Finnish set, each in `lang` where that file exists."""
    return {f.stem: item_file(jid, f.name, lang) for f in sorted(item_dir(jid).glob(pattern))}


def lang_file(jid, name, lang):
    """Another translated file of the unit (jaksot/<id>/<lang>/<name>), or None; the Finnish has none."""
    f = DIR / jid / lang / name
    return f if lang != i18n.SOURCE and f.is_file() else None


def header(jid, lang=i18n.SOURCE):
    d = load(jid, lang)
    return (d or {}).get("jakso") or {}


def planned(lang=i18n.SOURCE):
    """The front page rows of the planned units: [{icon, title, text}], in the order of ids()."""
    out = []
    for jid in ids():
        d = load(jid, lang)
        if d.get("jakso", {}).get("status") == "planned" and d.get("front"): out.append(dict(d["front"]))
    return out


def validate(icons=()):
    """Errors in the units' headers: the same header in every unit and in every translation of it."""
    errs = []
    for jid in ids():
        where = f"jaksot/{jid}/{FILE}"
        try: d = json.loads(source(jid).read_text())
        except Exception as e: errs.append(f"{where}: {e}"); continue
        h = d.get("jakso")
        if not isinstance(h, dict): errs.append(f'{where}: no "jakso" header'); continue
        if next(iter(d)) != "jakso": errs.append(f'{where}: "jakso" is the file\'s first key')
        if h.get("id") != jid: errs.append(f'{where}: jakso.id is {h.get("id")!r}, the folder is {jid!r}')
        if h.get("status") not in STATUSES: errs.append(f"{where}: jakso.status is one of {STATUSES}")
        if h.get("theme") not in THEMES: errs.append(f"{where}: jakso.theme is one of {THEMES}")
        if set(h) - {"course"} != {"id", "status", "theme"}: errs.append(f"{where}: the header has id, status and theme, and course where the unit's first page is a course page of the registry; nothing else")
        front = d.get("front")
        if h.get("status") == "planned":
            if not (isinstance(front, dict) and set(front) == {"icon", "title", "text"} and all(isinstance(v, str) and v for v in front.values())):
                errs.append(f'{where}: a planned unit has "front": icon, title and text')
            elif icons and front["icon"] not in icons: errs.append(f"{where}: front.icon {front['icon']!r} is not in module_icons.ICONS")
        for f in translations(jid):
            name = _rel(f)
            try: t = json.loads(f.read_text())
            except Exception as e: errs.append(f"{name}: {e}"); continue
            if f.parent.name not in i18n.languages(): errs.append(f"{name}: {f.parent.name} is not a language of the site")
            if t.get("jakso") != h: errs.append(f"{name}: its header differs from {where}")
            if h.get("status") == "planned" and isinstance(front, dict) and (set(t.get("front", {})) != set(front) or t["front"].get("icon") != front.get("icon")):
                errs.append(f"{name}: front has the same keys and icon as {where}")
        for p in (DIR / jid).iterdir():
            if p.is_dir() and p.name != ITEMS and p.name not in i18n.languages():
                errs.append(f"jaksot/{jid}/{p.name}/: a unit's folders are {ITEMS}/ and a language's code")
        errs += validate_pages(jid)
    return errs


# --- a unit written as pages of blocks: its pages from jakso.json alone -------------------------------------------------
# The blocks are the parts Kilparobotiikka's pages were first built of (teacher's brief 2026-11-09), lifted here on
# 2026-11-12 so that any unit can use them; site.css styles them (kr-*, ahjo-sec, ahjo-nav) in the unit's theme.
#   common to every block: "type"; a block that is a section also has "id", "title" and an optional "lead"
#   teksti        "text": [paragraphs]; optional "box": {"id", "title", "steps": [...], "note"}; optional "class"
#   lista         "items": [lines]; "ordered": true numbers them; optional "list_class", "class"
#   kortit        "cards": [{"title", "text", "icon"?, "href"?}] or "from": "kohteet"; optional "variant" (a class of the
#                 grid), "list" (lines under the cards) and "list_class"
#   linkit        "links": [{"title", "href" | "url"}]
#   pikavalikko   "title" (read aloud only), "items": [{"q", "href"}]: numbered quick answers
#   nyt           "text", "phase" (0 or a phase's number of the unit's kausi block), "updated" (d.m.yyyy)
#   kokemukset    "past_h", "past": [{"id", "title", "text", "photos"?}], "experiences_h", "upcoming_h", "upcoming",
#                 "upcoming_links": the course's photos and its students' accounts come from the course registry
#   sarakkeet     "cols": [{"title", "href", "items"}], "note"
#   johdanto      "text"; "notice": {"icon", "text", "href", "link"}: no heading
#   polku         "stages": [{"id", "title", "goal", "topics", "note"?, "practice", "mentor", "show", "links", "inner"?,
#                 "refs": [chapter ids]}]: an index and one section per stage
#   ohjelinkit    "guides": [{"title", "url", "text"}], "note"
#   kausi         "phases": [{"title", "text", "questions", "output"}], "note"
#   paivakirja    "questions", "template": [lines], "template_name", "where", "notebook", "notebook_link",
#                 "more", "more_link": {"title", "href"} (shown where that page is built)
#   periaate      "text": one sentence set apart
#   rinnakkain    "blocks": [two blocks side by side]
#   kappale       "text", "class"
#   taidot        "skills": [{"title", "signs", "evidence"}], "how", "note", "after"
#   varoitukset   "draft", "stop"
#   roolit        "roles": [{"who": "mentor" | "teacher", "items"}], "note"
#   turva-aiheet  "topics": [{"id", "icon", "title", "do", "teacher"}]
#   loppulinkit   "text", "link": {"title", "href"} (shown where that page is built), "links": [{"title", "url"}]
BLOCKS = ("teksti", "lista", "kortit", "linkit", "pikavalikko", "nyt", "kokemukset", "sarakkeet", "johdanto", "polku", "ohjelinkit",
          "kausi", "paivakirja", "periaate", "rinnakkain", "kappale", "taidot", "varoitukset", "roolit", "turva-aiheet", "loppulinkit")
SECTIONS = ("teksti", "lista", "kortit", "linkit", "nyt", "kokemukset", "sarakkeet", "ohjelinkit", "kausi", "paivakirja", "taidot", "roolit")   # blocks with id and title
ITEM_STATUSES = ("valmis", "idea", "luonnos")
FILE_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\.html")
esc = lambda s: _h.escape(str(s), quote=True)

# 24 x 24 line icons in the text colour, decorative (the title beside each carries the meaning)
ICONS = {
    "tools": "M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-2 2-1.6-1.6L8 21.8a2 2 0 0 1-2.8-2.8l9.4-9.4L13 8l2-2zM3.5 3.5l4 4M6 3l-3 3",
    "code": "M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16",
    "ruler": "M3 16.5L16.5 3 21 7.5 7.5 21zM7 12.5l2 2M10 9.5l2 2M13 6.5l2 2",
    "flag": "M5 21V4M5 4h11l-2 4 2 4H5",
    "notebook": "M6 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6zM9 3v18M12 8h3.5M12 12h3.5",
    "path": "M5 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM19 9a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM7 17h6a3 3 0 0 0 0-6h-2a3 3 0 0 1 0-6h6",
    "calendar": "M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
    "people": "M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM3 20v-1a6 6 0 0 1 12 0v1M16 11a2.5 2.5 0 1 0 0-5M17.5 14a4.5 4.5 0 0 1 3.5 4.4V20",
    "shield": "M12 3l7 3v5c0 4.5-3 8.4-7 10-4-1.6-7-5.5-7-10V6zM9 12l2 2 4-4",
    "gear": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1",
    "battery": "M3 8h15v8H3zM18 10.5h2.5v3H18M7 10.5v3M10 10.5v3",
    "power": "M12 3v8M7 6.3a7 7 0 1 0 10 0",
    "download": "M12 4v11M7 10l5 5 5-5M5 20h14",
    "copy": "M8 8h11v12H8zM5 16V4h11",
    "ext": "M14 4h6v6M20 4l-9 9M18 14v6H4V6h6",
}


def icon(name, cls="ahjo-icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<path d="{ICONS[name]}"/></svg>')


def generic(d): return isinstance(d, dict) and isinstance(d.get("pages"), list)


def cards_of(jid, lang=i18n.SOURCE):
    """The unit's items for a "kortit" block: every kohteet/*.json in `lang` (the Finnish as fallback), in their order."""
    return sorted((json.loads(f.read_text()) for f in item_files(jid, "*.json", lang).values()), key=lambda x: (x.get("order", 0), x["id"]))


def blocks_of(d, kind=None):
    """Every block of a unit, those inside a rinnakkain too, as (page, block); kind narrows to one type."""
    out = []
    for p in d.get("pages", []):
        for b in p.get("blocks", []):
            for x in [b] + (b.get("blocks", []) if b.get("type") == "rinnakkain" else []):
                if kind is None or x.get("type") == kind: out.append((p, x))
    return out


def block(d, kind):
    """The unit's first block of a type, or None."""
    found = blocks_of(d, kind)
    return found[0][1] if found else None


def _ul(items, cls=""):
    return f'<ul{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>' + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"


def _sec(id_, title, inner, lead="", cls=""):
    return (f'<section class="ahjo-sec kr-sec{" " + cls if cls else ""}" id="{id_}" aria-labelledby="h-{id_}"><h2 id="h-{id_}">{esc(title)}</h2>'
            + (f'<p class="ahjo-sec-lead">{esc(lead)}</p>' if lead else "") + inner + '</section>')


def _ext(u, l):
    """A link to another site: marked external, opened in a new tab, and said so (with the language, where the unit's ui names it)."""
    said = ", ".join(esc(x) for x in (u.get("external", "avautuu uuteen välilehteen"), u.get("in_english")) if x)
    return (f'<a href="{esc(l["url"])}" rel="external noopener" target="_blank">{esc(l["title"])}{icon("ext", "ahjo-icon kr-ext")}'
            f'<span class="visually-hidden"> ({said})</span></a>')


def _block(jid, d, b, lang, ctx=None):
    ctx = ctx or {}
    u, t = d.get("ui", {}), b["type"]
    has = ctx.get("has") or (lambda href: True)
    if t == "teksti":
        inner = "".join(f"<p>{esc(p)}</p>" for p in b["text"])
        if b.get("box"):
            x = b["box"]
            inner += (f'<div class="kr-join" id="{x["id"]}"><h3>{esc(x["title"])}</h3><ol class="kr-steps">'
                      + "".join(f"<li>{esc(s)}</li>" for s in x["steps"]) + f'</ol><p class="kr-note">{esc(x["note"])}</p></div>')
        return _sec(b["id"], b["title"], inner, b.get("lead", ""), b.get("class", ""))
    if t == "lista":
        if b.get("ordered"): inner = '<ol class="kr-steps">' + "".join(f"<li>{esc(x)}</li>" for x in b["items"]) + "</ol>"
        else: inner = _ul(b["items"], b.get("list_class", ""))
        return _sec(b["id"], b["title"], inner, b.get("lead", ""), b.get("class", ""))
    if t == "kortit":
        cards = cards_of(jid, lang) if b.get("from") == ITEMS else b["cards"]
        def card(c):
            pic = icon(c["icon"], "ahjo-icon kr-card-icon") if c.get("icon") else ""
            tag = (f' <span class="ahjo-tag">{esc(u.get("status", {}).get(c["status"], c["status"]))}</span>' if c.get("status", "valmis") != "valmis" else "")
            if c.get("href"):
                return (f'<li class="kr-card kr-link-card"><a href="{c["href"]}">{pic}<span class="kr-card-t">{esc(c["title"])}</span>'
                        f'<span class="kr-card-x">{esc(c["text"])}</span></a></li>')
            return f'<li class="kr-card">{pic}<h3>{esc(c["title"])}{tag}</h3><p>{esc(c["text"])}</p></li>'
        inner = f'<ul class="kr-cards{" " + b["variant"] if b.get("variant") else ""}">' + "".join(card(c) for c in cards) + "</ul>"
        if b.get("list"): inner += _ul(b["list"], b.get("list_class", ""))
        return _sec(b["id"], b["title"], inner, b.get("lead", ""))
    if t == "linkit":
        def link(l):
            if l.get("url"):
                return (f'<a href="{esc(l["url"])}" rel="external noopener" target="_blank">{esc(l["title"])}'
                        f'<span class="visually-hidden"> ({esc(u.get("external", "avautuu uuteen välilehteen"))})</span></a>')
            return f'<a href="{esc(l["href"])}">{esc(l["title"])}</a>'
        return _sec(b["id"], b["title"], "<ul>" + "".join(f"<li>{link(l)}</li>" for l in b["links"]) + "</ul>", b.get("lead", ""))
    if t == "pikavalikko":
        return (f'<nav class="kr-quick" aria-labelledby="h-kr-quick"><h2 id="h-kr-quick" class="visually-hidden">{esc(b["title"])}</h2><ol>'
                + "".join(f'<li><a href="{esc(q["href"])}"><span class="kr-quick-n" aria-hidden="true">{i}</span><span>{esc(q["q"])}</span></a></li>'
                          for i, q in enumerate(b["items"], 1)) + '</ol></nav>')
    if t == "nyt":
        season = blocks_of(d, "kausi")
        phase = season[0][1]["phases"][b["phase"] - 1]["title"] if b["phase"] and season else ""
        body = (f'<p>{esc(b["text"])}</p>' if b["text"] else f'<p class="kr-empty">{esc(u["now_empty"])}</p>')
        body += (f'<p class="kr-now-phase"><strong>{esc(u["now_phase"])}</strong> <a href="{season[0][0]["file"]}#vaihe-{b["phase"]}">{esc(phase)}</a></p>' if phase else "")
        body += (f'<p class="kr-now-date">{esc(u["now_updated"])} {esc(b["updated"])}</p>' if b["text"] else "")
        return _sec(b["id"], b["title"], f'<div class="kr-now">{body}</div>')
    if t == "kokemukset":
        photos, quotes = ctx.get("photos", ""), ctx.get("quotes", "")
        past = "".join(f'<article class="kr-past" id="{p["id"]}" aria-labelledby="h-{p["id"]}"><h4 id="h-{p["id"]}">{esc(p["title"])}</h4><p>{esc(p["text"])}</p>'
                       + (photos if p.get("photos") else "") + '</article>' for p in b["past"])
        comp = (f'<h3 id="aiemmat">{esc(b["past_h"])}</h3>{past}'
                + (f'<h3 id="kokemuksia">{esc(b["experiences_h"])}</h3>{quotes}' if quotes else "")
                + f'<h3 id="tulevat">{esc(b["upcoming_h"])}</h3><div class="kr-upcoming"><p>{esc(b["upcoming"])}</p><ul>'
                + "".join(f"<li>{_ext(u, l)}</li>" for l in b["upcoming_links"]) + '</ul></div>')
        return _sec(b["id"], b["title"], comp, b.get("lead", ""))
    if t == "sarakkeet":
        cols = "".join(f'<div class="kr-ahjo-col"><h3>' + (f'<a href="{c["href"]}">{esc(c["title"])}</a>' if c["href"] else esc(c["title"])) + f'</h3>{_ul(c["items"])}</div>'
                       for c in b["cols"])
        return _sec(b["id"], b["title"], f'<div class="kr-ahjo">{cols}</div><p class="kr-note">{esc(b["note"])}</p>', b.get("lead", ""))
    if t == "johdanto":
        n = b["notice"]
        return (f'<p>{esc(b["text"])}</p><p class="notice kr-safety-first" role="note">{icon(n["icon"])}<span>{esc(n["text"])} '
                f'<a href="{n["href"]}">{esc(n["link"])}<span aria-hidden="true"> →</span></a></span></p>')
    if t == "polku":
        ref = ctx.get("ref") or (lambda rid: None)
        out = '<ol class="kr-stage-index">' + "".join(f'<li><a href="#{s["id"]}">{esc(s["title"])}</a></li>' for s in b["stages"]) + '</ol>'
        for i, s in enumerate(b["stages"], 1):
            refs = [r for r in (ref(x) for x in s["refs"]) if r]
            links = [_ext(u, l) for l in s["links"]]
            inner = [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in s.get("inner", [])]
            side = ((f'<h4>{esc(u["official"])}</h4><ul>' + "".join(f"<li>{x}</li>" for x in links) + '</ul>' if links else "")
                    + (f'<h4>{esc(u["see_also"])}</h4><ul>' + "".join(f"<li>{x}</li>" for x in inner) + '</ul>' if inner else "")
                    + (f'<h4>{esc(u["physics"])}</h4><ul>' + "".join(f'<li><a href="{href}">{esc(title)}</a></li>' for title, href in refs) + '</ul>' if refs else ""))
            out += (f'<section class="kr-stage" id="{s["id"]}" aria-labelledby="h-{s["id"]}"><header class="kr-stage-head"><span class="kr-stage-n" aria-hidden="true">{i}</span>'
                    f'<h2 id="h-{s["id"]}"><span class="kr-stage-k">{esc(u["stage_n"].replace("{n}", str(i)))}</span> {esc(s["title"])}</h2></header>'
                    f'<p class="kr-goal"><strong>{esc(u["goal"])}:</strong> {esc(s["goal"])}</p>'
                    f'<div class="kr-stage-grid"><div><h3>{esc(u["topics"])}</h3>{_ul(s["topics"])}'
                    + (f'<p class="kr-note">{esc(s["note"])}</p>' if s.get("note") else "")
                    + f'</div><div class="kr-stage-do"><div class="kr-box kr-box-practice"><h3>{esc(u["practice"])}</h3><p>{esc(s["practice"])}</p></div>'
                    f'<div class="kr-box kr-box-mentor"><h3>{icon("people")}{esc(u["mentor_tip"])}</h3><p>{esc(s["mentor"])}</p></div>'
                    f'<div class="kr-box kr-box-show"><h3>{esc(u["show"])}</h3><p>{esc(s["show"])}</p></div></div></div>'
                    + (f'<div class="kr-stage-links">{side}</div>' if side else "") + '</section>')
        return out
    if t == "ohjelinkit":
        return _sec(b["id"], b["title"], '<ul class="kr-guides">' + "".join(f'<li>{_ext(u, g)}<span>{esc(g["text"])}</span></li>' for g in b["guides"]) + '</ul>'
                    + f'<p class="kr-note">{esc(b["note"])}</p>', b.get("lead", ""))
    if t == "kausi":
        phases = '<ol class="kr-phases">' + "".join(
            f'<li class="kr-phase" id="vaihe-{i}"><h3><span class="kr-phase-n" aria-hidden="true">{i}</span>{esc(ph["title"])}</h3><p>{esc(ph["text"])}</p>'
            f'<p class="kr-phase-q"><strong>{esc(u["phase_questions"])}:</strong> {esc(" ".join(ph["questions"]))}</p>'
            f'<p class="kr-phase-o"><strong>{esc(u["phase_output"])}:</strong> {esc(ph["output"])}</p></li>' for i, ph in enumerate(b["phases"], 1)) + '</ol>'
        return _sec(b["id"], b["title"], phases + f'<p class="kr-note">{esc(b["note"])}</p>')
    if t == "paivakirja":
        txt = template_text(b)
        more = b.get("more_link")
        diary = (f'<ol class="kr-diary-q">' + "".join(f"<li>{esc(q)}</li>" for q in b["questions"]) + '</ol>'
                 f'<div class="kr-template"><pre id="kr-pohja" tabindex="0">{esc(txt)}</pre><div class="kr-template-actions">'
                 f'<button type="button" class="kr-btn" data-copy="kr-pohja" data-copied="{esc(u["copied"])}" hidden>{icon("copy")}{esc(u["copy"])}</button>'
                 f'<a class="kr-btn" href="data:text/plain;charset=utf-8,{quote(txt)}" download="{esc(b["template_name"])}">{icon("download")}{esc(u["download"])} (.txt)</a>'
                 f'<span class="kr-copied" role="status" aria-live="polite"></span></div></div>'
                 f'<p>{esc(b["where"])}</p><p>{esc(b["notebook"])} {_ext(u, b["notebook_link"])}</p>'
                 + (f'<p>{esc(b["more"])} <a href="{more["href"]}">{esc(more["title"])}<span aria-hidden="true"> →</span></a></p>' if more and has(more["href"]) else ""))
        return _sec(b["id"], b["title"], diary, b.get("lead", ""))
    if t == "periaate":
        return f'<figure class="kr-principle"><blockquote><p>{esc(b["text"])}</p></blockquote></figure>'
    if t == "rinnakkain":
        return '<div class="kr-two">' + "".join(_block(jid, d, x, lang, ctx) for x in b["blocks"]) + '</div>'
    if t == "kappale":
        return f'<p{f" class={chr(34)}{b["class"]}{chr(34)}" if b.get("class") else ""}>{esc(b["text"])}</p>'
    if t == "taidot":
        skills = '<ul class="kr-cards kr-skills">' + "".join(
            f'<li class="kr-card"><h3>{esc(k["title"])}</h3><p class="kr-signs-h">{esc(u["signs"])}</p>{_ul(k["signs"])}'
            f'<p class="kr-evidence"><strong>{esc(u["evidence"])}:</strong> {esc(k["evidence"])}</p></li>' for k in b["skills"]) + '</ul>'
        return _sec(b["id"], b["title"], skills + f'<p>{esc(b["how"])}</p><p class="kr-note">{esc(b["note"])}</p><p>{esc(b["after"])}</p>', b.get("lead", ""))
    if t == "varoitukset":
        return (f'<p class="notice" role="note"><span class="ahjo-badge planned">{esc(u["draft_badge"])}</span> {esc(b["draft"])}</p>'
                f'<p class="kr-stop" role="note">{icon("power")}<strong>{esc(b["stop"])}</strong></p>')
    if t == "roolit":
        roles = "".join(f'<div class="kr-role kr-role-{r["who"]}"><h3>{esc(u["mentor_side"] if r["who"] == "mentor" else u["teacher_side"])}</h3>{_ul(r["items"])}</div>' for r in b["roles"])
        return _sec(b["id"], b["title"], f'<div class="kr-roles">{roles}</div><p class="kr-note"><strong>{esc(b["note"])}</strong></p>')
    if t == "turva-aiheet":
        out = '<div class="kr-safety-grid">'
        for x in b["topics"]:
            out += (f'<section class="kr-safety" id="{x["id"]}" aria-labelledby="h-{x["id"]}"><h2 id="h-{x["id"]}">{icon(x["icon"])}{esc(x["title"])}</h2>{_ul(x["do"])}'
                    f'<p class="kr-teacher"><strong>{esc(u["teacher_side"])}:</strong> {esc(x["teacher"])}</p></section>')
        return out + '</div>'
    if t == "loppulinkit":
        l = b.get("link")
        return (f'<p>{esc(b["text"])}' + (f' <a href="{l["href"]}">{esc(l["title"])}<span aria-hidden="true"> →</span></a>' if l and has(l["href"]) else "") + '</p>'
                f'<p class="kr-links">{esc(u["official"])}: ' + ", ".join(_ext(u, x) for x in b["links"]) + '</p>')
    raise ValueError(f"jaksot: unknown block type {t!r}")


def template_text(b): return "\n".join(b["template"]) + "\n"


def menu(d, current):
    """The unit's own menu: its pages by their "nav" names, this page marked; nothing for a unit of one page."""
    items = [(p["file"], p.get("nav") or p["title"]) for p in d["pages"]]
    if len(items) < 2: return ""
    label = d.get("ui", {}).get("nav_label") or d.get("_course_title") or d.get("title", "")
    return (f'<nav class="ahjo-nav kr-nav" aria-label="{esc(label)}"><ul>'
            + "".join(f'<li><a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == current else ""}>{esc(t)}</a></li>' for h, t in items)
            + '</ul></nav>')


def page_body(jid, d, file, lang=i18n.SOURCE, ctx=None):
    """The body HTML of one page of a unit written as pages. ctx (all optional): "head" (the title block of a page that
    is also a course page of the registry: it stands in place of the unit's own heading), "ref" (chapter id -> (title,
    href) where the chapter is published), "has" (href -> whether that page is built), "photos", "quotes" (the
    course's, as HTML)."""
    ctx = ctx or {}
    p = next(x for x in d["pages"] if x["file"] == file)
    if ctx.get("head") is not None:
        head = re.sub(r'<p class="local-desc">.*?</p>', "", ctx["head"])   # the description is the page's meta line; the intro says it on the page
    else:
        head = (f'<header class="kr-head"><p class="ahjo-eyebrow">{esc(d.get("_course_title") or d.get("title", ""))}</p><h1>{esc(p["title"])}</h1>'
                f'<p class="lead">{esc(p["lead"])}</p></header>')
    return head + menu(d, file) + "".join(_block(jid, d, b, lang, ctx) for b in p["blocks"])


def pages(jid, lang=i18n.SOURCE, ctx=None):
    """[(file, title, lead, body HTML)] of a unit written as "pages", in `lang`."""
    d = load(jid, lang)
    if not generic(d): return []
    return [(p["file"], p.get("title", ""), p.get("lead", ""), page_body(jid, d, p["file"], lang, ctx)) for p in d["pages"]]


def front_row(jid, lang=i18n.SOURCE):
    """{icon, title, text, href} of a live generic unit's row on the front page, or None (a unit that is a course of
    the registry has its row from there)."""
    d = load(jid, lang)
    if not generic(d) or d["jakso"].get("status") != "live" or d["jakso"].get("course") or not d.get("front"): return None
    return dict(d["front"], href=d["pages"][0]["file"])


NEEDS = {   # what each block type must have (a list unless said otherwise), beyond id and title for a section
    "teksti": ("text",), "lista": ("items",), "linkit": ("links",), "pikavalikko": ("items",), "kokemukset": ("past", "upcoming_links"),
    "sarakkeet": ("cols",), "polku": ("stages",), "ohjelinkit": ("guides",), "kausi": ("phases",), "paivakirja": ("questions", "template"),
    "rinnakkain": ("blocks",), "taidot": ("skills",), "roolit": ("roles",), "turva-aiheet": ("topics",), "loppulinkit": ("links",),
}


def validate_pages(jid, taken=()):
    """Errors in a generic unit's pages and items. taken: the site's other page names, which a unit may not reuse."""
    d = json.loads(source(jid).read_text()); where = f"jaksot/{jid}/{FILE}"; errs = []
    if not generic(d): return errs
    course = d["jakso"].get("course")
    if not course:
        if not d.get("title"): errs.append(f"{where}: a unit with pages has a title")
        if not isinstance(d.get("front"), dict) or set(d["front"]) != {"icon", "title", "text"}: errs.append(f'{where}: a unit with pages has "front": icon, title and text')
    files = [p.get("file") for p in d["pages"]]
    if not files: errs.append(f"{where}: pages is empty")
    ids = []
    for k, p in enumerate(d["pages"]):
        pw = f"{where} pages[{k}]"
        f = p.get("file") or ""
        first = f"{course}.html" if course else f"{jid}.html"
        if not (f == first if k == 0 else FILE_RE.fullmatch(f) and f.startswith(f"{jid}-")): errs.append(f"{pw}: file is {first} for the first page and {jid}-<name>.html after it, lower case")
        if f in taken or files.count(f) > 1: errs.append(f"{pw}: the page name {f} is already in use")
        for key in () if course and k == 0 else ("title", "lead"):
            if not p.get(key): errs.append(f"{pw}: no {key}")
        if not p.get("blocks"): errs.append(f"{pw}: no blocks")
        here = [x for b in p.get("blocks", []) for x in [b] + (b.get("blocks", []) if b.get("type") == "rinnakkain" else [])]
        page_ids = [b.get("id") for b in here if b.get("id")] + [s.get("id") for b in here for s in b.get("stages", []) + b.get("topics", []) if isinstance(s, dict)]
        ids += page_ids
        for b in here:
            bw = f"{pw} block {b.get('id') or b.get('type')!r}"
            if b.get("type") not in BLOCKS: errs.append(f"{bw}: type is one of {BLOCKS}"); continue
            if b["type"] in SECTIONS:
                if not re.fullmatch(r"[a-z][a-z0-9-]*", b.get("id") or "") or page_ids.count(b.get("id")) > 1: errs.append(f"{bw}: id is lower case and its own on the page")
                if not b.get("title"): errs.append(f"{bw}: no title")
            for need in NEEDS.get(b["type"], ()):
                if not (isinstance(b.get(need), list) and b[need]): errs.append(f"{bw}: {need} is a list with something in it")
            if b["type"] == "kortit":
                if b.get("from") == ITEMS:
                    if not list(item_dir(jid).glob("*.json")): errs.append(f"{bw}: from {ITEMS}, but jaksot/{jid}/{ITEMS}/ has no .json file")
                elif not (isinstance(b.get("cards"), list) and b["cards"] and all(c.get("title") and c.get("text") for c in b["cards"])): errs.append(f'{bw}: cards with title and text, or "from": "{ITEMS}"')
            for l in b.get("links", []) if b["type"] == "linkit" else []:
                if not l.get("title") or bool(l.get("href")) == bool(l.get("url")) or (l.get("url") and not l["url"].startswith("https://")):
                    errs.append(f"{bw}: a link has a title and either href (a page of the site) or an https url")
            for x in [c for c in b.get("cards", []) if isinstance(c, dict)] + b.get("topics", []) + ([b["notice"]] if isinstance(b.get("notice"), dict) else []):
                if x.get("icon") and x["icon"] not in ICONS: errs.append(f"{bw}: unknown icon {x['icon']!r} (jaksot.ICONS)")
    for u in urls(d):
        if not str(u).startswith("https://"): errs.append(f"{where}: {u} is not an https address")
    seen = set()
    for f in sorted(item_dir(jid).glob("*.json")) if item_dir(jid).is_dir() else []:
        name = _rel(f)
        try: x = json.loads(f.read_text())
        except Exception as e: errs.append(f"{name}: {e}"); continue
        if x.get("id") != f.stem or x["id"] in seen: errs.append(f"{name}: id is the file's name")
        seen.add(x.get("id"))
        if not (x.get("title") and x.get("text")): errs.append(f"{name}: title and text")
        if x.get("status") not in ITEM_STATUSES: errs.append(f"{name}: status is one of {ITEM_STATUSES}")
    for f in translations(jid):
        name = _rel(f); t = json.loads(f.read_text())
        errs += [f"{name}: differs from {where} at {p}" for p in shape_diff(d, t)]
        if generic(t) and len(t["pages"]) == len(d["pages"]):
            def same(x):   # what a translation keeps: files, types, ids, links, icons, chapter references
                KEEP = ("file", "type", "id", "from", "ordered", "href", "url", "icon", "refs", "who", "phase", "variant", "class", "list_class", "photos")
                def keep(v):
                    if isinstance(v, dict): return {k: (w if k in KEEP else keep(w)) for k, w in v.items() if k in KEEP or isinstance(w, (dict, list))}
                    return [keep(w) for w in v if isinstance(w, (dict, list))]
                return keep(x["pages"])
            if same(t) != same(d): errs.append(f"{name}: files, block types, ids, links, icons and chapter references stay as in {where}")
        for g in sorted((f.parent / ITEMS).glob("*.json")) if (f.parent / ITEMS).is_dir() else []:
            src = item_dir(jid) / g.name
            if not src.is_file(): errs.append(f"{_rel(g)}: no such item in jaksot/{jid}/{ITEMS}/"); continue
            a, b = json.loads(src.read_text()), json.loads(g.read_text())
            if set(a) != set(b) or any(a.get(k) != b.get(k) for k in ("id", "status", "order")): errs.append(f"{_rel(g)}: id, status and order stay as in the Finnish file")
    return errs


# --- helpers the page modules share ----------------------------------------------------------------------------------
def icon_svg(icons, name, cls="ahjo-icon"):
    """A 24 x 24 line icon in the text colour, decorative: the text beside it carries the meaning."""
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<path d="{icons[name]}"/></svg>')


def shape_diff(a, b, path=""):
    """Where a translation's structure differs from the source's (keys, list lengths): a list of paths."""
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b): return [path or "/"]
        return [p for k in a for p in shape_diff(a[k], b[k], f"{path}/{k}")]
    if isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b): return [path]
        return [p for i, (x, y) in enumerate(zip(a, b)) for p in shape_diff(x, y, f"{path}[{i}]")]
    return []


def urls(x):
    """Every value under a key "url" in a unit's data."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k == "url": yield v
            else: yield from urls(v)
    elif isinstance(x, list):
        for v in x: yield from urls(v)


if __name__ == "__main__":
    import module_icons
    for jid in ids():
        h = header(jid)
        print(f"{jid:12} {h.get('status', '?'):8} {h.get('theme', '?'):12} items: {len(list(item_dir(jid).glob('*'))) if item_dir(jid).is_dir() else 0:3}  languages: {', '.join(f.parent.name for f in translations(jid)) or '-'}")
    e = validate(module_icons.ICONS)
    print("\n".join(e) or "jaksot OK"); sys.exit(1 if e else 0)
