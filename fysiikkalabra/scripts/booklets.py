"""Vihkot (teacher 2026-11-07): the printable A5 books of the courses on one page vihkot.html in every language, linked
from the header of every page.

booklets/<COURSE>-<lang>.pdf are the books scripts/print_book.py writes with --publish (the theory and worked examples
of a course, a QR code per chapter to its web page); booklets/booklets.json records each one's pages, size and date.
build.py copies the PDFs to site/vihkot/ and renders the page: the books of the page's language, for fi-easy the
Finnish ones where it has none of its own.
  python scripts/booklets.py        check that booklets.json and the PDFs agree
"""
import json, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

PAGE = "vihkot.html"
DIR = ROOT / "booklets"
INDEX = DIR / "booklets.json"
PUBLISHED = "vihkot"          # site/vihkot/<COURSE>-<lang>.pdf
FALLBACK = {"fi-easy": "fi"}  # a language without books of its own shows these


def esc(s): return _h.escape(str(s), quote=True)


def load():
    """{"FY1-fi": {"course": "FY1", "lang": "fi", "pages": 104, "bytes": 2424539, "date": "2026-11-07"}, ...}"""
    return json.loads(INDEX.read_text()) if INDEX.is_file() else {}


def record(course, lang, pdf, pages, date):
    """Called by print_book.py --publish: copies the book in and records it."""
    DIR.mkdir(exist_ok=True)
    dst = DIR / f"{course}-{lang}.pdf"
    dst.write_bytes(pathlib.Path(pdf).read_bytes())
    idx = load()
    idx[f"{course}-{lang}"] = {"course": course, "lang": lang, "pages": pages, "bytes": dst.stat().st_size, "date": date}
    INDEX.write_text(json.dumps(dict(sorted(idx.items(), key=lambda kv: (int(kv[1]["course"][2:]) if kv[1]["course"][2:].isdigit() else 99, kv[0]))),
                                ensure_ascii=False, indent=1) + "\n")
    return dst


def books(lang):
    """The books shown on the page in `lang`, in course order: (course, file name, entry, own language?)."""
    idx = load()
    out = []
    for e in idx.values():
        if e["lang"] == lang:
            out.append((e["course"], f'{e["course"]}-{lang}.pdf', e, True))
    if lang in FALLBACK:
        have = {c for c, *_ in out}
        out += [(e["course"], f'{e["course"]}-{e["lang"]}.pdf', e, False) for e in idx.values()
                if e["lang"] == FALLBACK[lang] and e["course"] not in have]
    return sorted(out, key=lambda b: int(b[0][2:]) if b[0][2:].isdigit() else 99)


def size_text(n, lang):
    mb = n / 1e6
    s = f"{mb:.1f}"
    return (s if lang == "en" else s.replace(".", ",")) + (" MB" if lang == "en" else " Mt")


def body(T, lang, titles, icon):
    """The page's <main> content. titles = {course: title in this language}; icon(course) -> the module's icon <img>."""
    rows = ""
    for course, name, e, own in books(lang):
        meta = T("booklets.meta", pages=e["pages"], size=size_text(e["bytes"], lang))
        rows += (f'<li class="booklet">{icon(course)}<div class="booklet-text"><h2 class="booklet-title">'
                 f'<span class="mod-code">{esc(course)}</span> {esc(titles.get(course, course))}</h2>'
                 f'<p class="booklet-meta">{esc(meta)}</p></div>'
                 f'<a class="booklet-get" href="{PUBLISHED}/{name}" download type="application/pdf">'
                 f'{esc(T("booklets.download"))}<span class="visually-hidden"> {esc(course)}</span></a></li>')
    lst = f'<ul class="booklets">{rows}</ul>' if rows else f'<p class="booklets-none">{esc(T("booklets.none"))}</p>'
    return (f'<h1>{esc(T("site.booklets"))}</h1><p class="lead">{esc(T("booklets.lead"))}</p>' + lst
            + f'<h2 class="booklets-h">{esc(T("booklets.print_h"))}</h2>'
            + "".join(f'<p>{esc(p)}</p>' for p in (T("booklets.print_1"), T("booklets.print_2"))))


def check():
    errs = []
    idx = load()
    for key, e in idx.items():
        f = DIR / f"{key}.pdf"
        if key != f'{e["course"]}-{e["lang"]}': errs.append(f"{key}: key does not match course and lang")
        if not f.is_file(): errs.append(f"{key}: {f.name} missing")
        elif f.stat().st_size != e["bytes"]: errs.append(f"{key}: size {f.stat().st_size} but booklets.json says {e['bytes']}")
    for f in DIR.glob("*.pdf") if DIR.is_dir() else []:
        if f.stem not in idx: errs.append(f"{f.name}: not in booklets.json")
    return errs


if __name__ == "__main__":
    errs = check()
    print("\n".join(errs) if errs else "booklets: ok")
    sys.exit(1 if errs else 0)
