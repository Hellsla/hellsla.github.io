"""Kuuntele ja katso fysiikkaa / Listen & Watch Physics (teacher 2026-11-17): podcasts, documentaries and videos on physics,
one page podcastit.html in every language, modelled on Kirjavinkit (scripts/reading_tips.py), linked from every header.

content/<lang>/podcastit.json is the source of a language (fi, en); a language without a file (fi-easy) shows the Finnish.
The two lists are independent productions, never translations of each other (no one-to-one pairing): every item is in the
language it is made in and carries only its own title and text. Keys of an item: id, language, title, source, url, type
(podcast | documentary | video), modules (["FY3", "FY8"]), topics, durationMinutes (null when not reliably known),
description, difficulty (optional), note (optional, e.g. an older programme), featured (optional), verified (true only when
the link was opened and the programme checked; an item that is not verified is never shown and the check fails on it).
  python scripts/media_tips.py        validate the files
"""
import json, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import page_art

PAGE = "podcastit.html"
MODULES = [f"FY{i}" for i in range(1, 9)]
TYPES = ("podcast", "documentary", "video")
SHORT = 15            # minutes: "short" is at most this long
ITEM_KEYS = {"id", "language", "title", "source", "url", "type", "modules", "topics", "durationMinutes", "description", "difficulty", "note", "featured", "verified"}
REQUIRED = {"id", "language", "title", "source", "url", "type", "modules", "topics", "durationMinutes", "description", "verified"}
PAGE_KEYS = ("title", "subtitle", "description", "intro", "featured_title", "other_lang", "items")
OTHER_KEYS = ("lead", "text", "link", "lang")   # the href comes from the build: the other language's page


def esc(s): return _h.escape(str(s), quote=True)


def load(lang="fi"):
    f = ROOT / "content" / lang / "podcastit.json"
    if not f.is_file(): f = ROOT / "content" / "fi" / "podcastit.json"
    return json.loads(f.read_text())


def source_exists(): return (ROOT / "content" / "fi" / "podcastit.json").is_file()


def check():
    errs = []
    ids = set()
    for f in sorted((ROOT / "content").glob("*/podcastit.json")):
        lang = f.parent.name; d = json.loads(f.read_text())
        for k in PAGE_KEYS:
            if k not in d: errs.append(f"{lang}: missing {k}")
        for k in OTHER_KEYS:
            if k not in d.get("other_lang", {}): errs.append(f"{lang}: other_lang.{k} missing")
        for i, it in enumerate(d.get("items", []), 1):
            w = f"{lang} item {i} ({it.get('id')})"
            if set(it) - ITEM_KEYS or REQUIRED - set(it): errs.append(f"{w}: keys {sorted(set(it) ^ ITEM_KEYS - {'difficulty', 'note', 'featured'})}")
            if it.get("id") in ids: errs.append(f"{w}: id used twice")
            ids.add(it.get("id"))
            if it.get("verified") is not True: errs.append(f"{w}: not verified, must not be in the file")
            if not str(it.get("url", "")).startswith("https://"): errs.append(f"{w}: url must be https")
            if it.get("type") not in TYPES: errs.append(f"{w}: type {it.get('type')}")
            if not it.get("modules") or set(it["modules"]) - set(MODULES): errs.append(f"{w}: modules {it.get('modules')}")
            dm = it.get("durationMinutes")
            if dm is not None and not (isinstance(dm, int) and dm > 0): errs.append(f"{w}: durationMinutes {dm}")
    return errs


def facts(it, T):
    parts = [m.replace("FY", "FY0") for m in it["modules"]] + [T("media.type_" + it["type"])]
    if it["durationMinutes"]: parts.append(T("media.minutes", n=it["durationMinutes"]))
    if it.get("difficulty"): parts.append(it["difficulty"])
    return " · ".join(parts)


def item(it, T, feat=False):
    dm = it["durationMinutes"]
    attrs = f'data-modules="{" ".join(it["modules"])}" data-type="{it["type"]}"' + (f' data-min="{dm}"' if dm else "")
    note = f'<p class="media-note">{esc(it["note"])}</p>' if it.get("note") else ""
    return (f'<li class="media" {attrs}><h3 class="media-title"><a href="{esc(it["url"])}" rel="noopener" lang="{esc(it["language"])}">{esc(it["title"])}</a></h3>'
            f'<p class="media-source">{esc(it["source"])}</p><p class="media-text">{esc(it["description"])}</p>'
            f'<p class="media-facts">{esc(facts(it, T))}</p>{note}</li>')


def body(T, lang, names, other_href):
    """The page's <main> content; names: {"FY1": course title}; other_href: the link to the other language's page."""
    d = load(lang); items = d["items"]; o = d["other_lang"]
    head = (f'<div class="page-head"><div><span class="eyebrow">{esc(d["subtitle"])}</span><h1>{esc(d["title"])}</h1></div>{page_art.svg("listen", 88)}</div>'
            + "".join(f'<p class="{"lead" if i == 0 else "reading-intro"}">{esc(p)}</p>' for i, p in enumerate(d["intro"]))
            + f'<aside class="media-other"><p><strong>{esc(o["lead"])}</strong> {esc(o["text"])} '
              f'<a href="{esc(other_href)}" hreflang="{esc(o["lang"])}">{esc(o["link"])}</a></p></aside>')
    if not items: return head
    def chips(group, labels):
        return "".join(f'<button type="button" class="media-chip" data-{group}="{k}" aria-pressed="false">{esc(v)}</button>' for k, v in labels)
    filt = (f'<form class="media-filters" hidden onsubmit="return false">'
            f'<div role="group" aria-labelledby="mf-mod"><span id="mf-mod" class="media-flabel">{esc(T("media.module"))}</span>'
            + chips("module", [(m, m.replace("FY", "FY0")) for m in MODULES if any(m in it["modules"] for it in items)]) + '</div>'
            f'<div role="group" aria-labelledby="mf-type"><span id="mf-type" class="media-flabel">{esc(T("media.type"))}</span>'
            + chips("type", [(t, T("media.type_" + t)) for t in TYPES if any(it["type"] == t for it in items)]) + '</div>'
            f'<label class="media-short"><input type="checkbox" id="mf-short" data-short="{SHORT}"> {esc(T("media.short", n=SHORT))}</label>'
            f'<p class="media-count" role="status" aria-live="polite" data-tpl="{esc(T("media.count", n="{n}"))}" data-none="{esc(T("media.none"))}"></p></form>')
    feat = [it for it in items if it.get("featured")]
    out = head + filt
    if feat:
        out += f'<section class="media-featured" id="media-featured"><h2>{esc(d["featured_title"])}</h2><ul class="media-list">{"".join(item(i, T) for i in feat)}</ul></section>'
    for m in MODULES:
        group = [it for it in items if it["modules"][0] == m]
        if group:
            out += (f'<section class="media-module" id="{m.lower()}" data-module="{m}"><h2 class="media-mod-h">{page_art.svg(m, 56)}<span>{m.replace("FY", "FY0")} · {esc(names.get(m, ""))}</span></h2>'
                    f'<ul class="media-list">{"".join(item(i, T) for i in group)}</ul></section>')
    return out + '<script src="mediafilter.js"></script>'


if __name__ == "__main__":
    errs = check()
    print("\n".join(errs) if errs else "podcastit: ok")
    sys.exit(1 if errs else 0)
