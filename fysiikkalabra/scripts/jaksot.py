"""Jaksopohja (teacher 2026-11-12): one folder layout, one registry and one set of helpers for every study unit outside
the physics modules FY1–FY14 (Ahjo, Kilparobotiikka, LUMA-tutor, Droonilab and whatever comes next), so that updating
one is the same work as updating another.

  jaksot/<id>/jakso.json           the unit in Finnish. Its first key is the same in every unit:
                                     "jakso": {"id": <the folder's name>, "status": "live" | "planned",
                                               "theme": "ahjo" | "kiviruukki" | "ruukkilabra"}
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
        if set(h) != {"id", "status", "theme"}: errs.append(f"{where}: the header has id, status and theme, nothing else")
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


# --- a unit without a page module: its pages from jakso.json alone -----------------------------------------------------
BLOCKS = ("teksti", "lista", "kortit", "linkit")
ITEM_STATUSES = ("valmis", "idea", "luonnos")
FILE_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\.html")
esc = lambda s: _h.escape(str(s), quote=True)


def generic(d): return isinstance(d, dict) and isinstance(d.get("pages"), list)


def cards_of(jid, lang=i18n.SOURCE):
    """The unit's items for a "kortit" block: every kohteet/*.json in `lang` (the Finnish as fallback), in their order."""
    return sorted((json.loads(f.read_text()) for f in item_files(jid, "*.json", lang).values()), key=lambda x: (x.get("order", 0), x["id"]))


def _block(jid, d, b, lang):
    ui = d.get("ui", {})
    lead = f'<p class="ahjo-sec-lead">{esc(b["lead"])}</p>' if b.get("lead") else ""
    if b["type"] == "teksti": inner = "".join(f"<p>{esc(p)}</p>" for p in b["text"])
    elif b["type"] == "lista":
        tag, cls = ("ol", ' class="kr-steps"') if b.get("ordered") else ("ul", "")
        inner = f"<{tag}{cls}>" + "".join(f"<li>{esc(x)}</li>" for x in b["items"]) + f"</{tag}>"
    elif b["type"] == "kortit":
        cards = cards_of(jid, lang) if b.get("from") == ITEMS else b["cards"]
        def card(c):
            tag = (f' <span class="ahjo-tag">{esc(ui.get("status", {}).get(c["status"], c["status"]))}</span>' if c.get("status", "valmis") != "valmis" else "")
            if c.get("href"):
                return (f'<li class="kr-card kr-link-card"><a href="{esc(c["href"])}"><span class="kr-card-t">{esc(c["title"])}</span>'
                        f'<span class="kr-card-x">{esc(c["text"])}</span></a></li>')
            return f'<li class="kr-card"><h3>{esc(c["title"])}{tag}</h3><p>{esc(c["text"])}</p></li>'
        inner = '<ul class="kr-cards">' + "".join(card(c) for c in cards) + "</ul>"
    else:
        def link(l):
            if l.get("url"):
                return (f'<a href="{esc(l["url"])}" rel="external noopener" target="_blank">{esc(l["title"])}'
                        f'<span class="visually-hidden"> ({esc(ui.get("external", "avautuu uuteen välilehteen"))})</span></a>')
            return f'<a href="{esc(l["href"])}">{esc(l["title"])}</a>'
        inner = "<ul>" + "".join(f"<li>{link(l)}</li>" for l in b["links"]) + "</ul>"
    return (f'<section class="ahjo-sec kr-sec" id="{esc(b["id"])}" aria-labelledby="h-{esc(b["id"])}"><h2 id="h-{esc(b["id"])}">{esc(b["title"])}</h2>'
            + lead + inner + "</section>")


def pages(jid, lang=i18n.SOURCE):
    """[(file, title, lead, body HTML)] of a unit written as "pages", in `lang`."""
    d = load(jid, lang)
    if not generic(d): return []
    menu = [(p["file"], p.get("nav") or p["title"]) for p in d["pages"]]
    out = []
    for p in d["pages"]:
        nav = ("" if len(menu) < 2 else f'<nav class="ahjo-nav kr-nav" aria-label="{esc(d["title"])}"><ul>'
               + "".join(f'<li><a href="{f}"{" aria-current=" + chr(34) + "page" + chr(34) if f == p["file"] else ""}>{esc(t)}</a></li>' for f, t in menu) + "</ul></nav>")
        head = (f'<header class="kr-head"><p class="ahjo-eyebrow">{esc(d["title"])}</p><h1>{esc(p["title"])}</h1>'
                f'<p class="lead">{esc(p["lead"])}</p></header>')
        out.append((p["file"], p["title"], p["lead"], head + nav + "".join(_block(jid, d, b, lang) for b in p["blocks"])))
    return out


def front_row(jid, lang=i18n.SOURCE):
    """{icon, title, text, href} of a live generic unit's row on the front page, or None."""
    d = load(jid, lang)
    if not generic(d) or d["jakso"].get("status") != "live" or not d.get("front"): return None
    return dict(d["front"], href=d["pages"][0]["file"])


def validate_pages(jid, taken=()):
    """Errors in a generic unit's pages and items. taken: the site's other page names, which a unit may not reuse."""
    d = json.loads(source(jid).read_text()); where = f"jaksot/{jid}/{FILE}"; errs = []
    if not generic(d): return errs
    if not d.get("title"): errs.append(f"{where}: a unit with pages has a title")
    if not isinstance(d.get("front"), dict) or set(d["front"]) != {"icon", "title", "text"}: errs.append(f'{where}: a unit with pages has "front": icon, title and text')
    files = [p.get("file") for p in d["pages"]]
    if not files: errs.append(f"{where}: pages is empty")
    for k, p in enumerate(d["pages"]):
        pw = f"{where} pages[{k}]"
        f = p.get("file") or ""
        if not FILE_RE.fullmatch(f) or not (f == f"{jid}.html" if k == 0 else f.startswith(f"{jid}-")): errs.append(f"{pw}: file is {jid}.html for the first page and {jid}-<name>.html after it, lower case")
        if f in taken or files.count(f) > 1: errs.append(f"{pw}: the page name {f} is already in use")
        for key in ("title", "lead"):
            if not p.get(key): errs.append(f"{pw}: no {key}")
        ids = [b.get("id") for b in p.get("blocks", [])]
        if not ids: errs.append(f"{pw}: no blocks")
        for b in p.get("blocks", []):
            bw = f"{pw} block {b.get('id')!r}"
            if b.get("type") not in BLOCKS: errs.append(f"{bw}: type is one of {BLOCKS}"); continue
            if not re.fullmatch(r"[a-z][a-z0-9-]*", b.get("id") or "") or ids.count(b.get("id")) > 1: errs.append(f"{bw}: id is lower case and its own on the page")
            if not b.get("title"): errs.append(f"{bw}: no title")
            need = {"teksti": "text", "lista": "items", "linkit": "links"}.get(b["type"])
            if need and not (isinstance(b.get(need), list) and b[need]): errs.append(f"{bw}: {need} is a list with something in it")
            if b["type"] == "kortit":
                if b.get("from") == ITEMS:
                    if not list(item_dir(jid).glob("*.json")): errs.append(f"{bw}: from {ITEMS}, but jaksot/{jid}/{ITEMS}/ has no .json file")
                elif not (isinstance(b.get("cards"), list) and b["cards"] and all(c.get("title") and c.get("text") for c in b["cards"])): errs.append(f'{bw}: cards with title and text, or "from": "{ITEMS}"')
            for l in b.get("links", []) if b["type"] == "linkit" else []:
                if not l.get("title") or bool(l.get("href")) == bool(l.get("url")) or (l.get("url") and not l["url"].startswith("https://")):
                    errs.append(f"{bw}: a link has a title and either href (a page of the site) or an https url")
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
            same = lambda x: [(p["file"], [(b.get("type"), b.get("id"), b.get("from"), b.get("ordered"), [(l.get("href"), l.get("url")) for l in b.get("links", [])],
                                           [c.get("href") for c in b.get("cards", [])]) for b in p.get("blocks", [])]) for p in x["pages"]]
            if same(t) != same(d): errs.append(f"{name}: files, block types, ids and links stay as in {where}")
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
