"""Lukuvinkit: a reading list of books on physics beyond the textbook (teacher 2026-11-03), one page lukuvinkit.html
in every language, linked from the header of every page.

content/fi/lukuvinkit.json is the source: the page texts and the books in their order (title, url, author, language,
level, loan, text, courses). A translation content/<lang>/lukuvinkit.json has the same keys and, under "books", the
same number of entries in the same order holding only its own language, level and text; titles, authors, links,
courses and the loan marks always come from the Finnish file. A language without a file (fi-easy) shows the Finnish.
The list is one ordered list with no subheadings (teacher's brief); a book with "loan": true gets the small tag
"Lainattavissa Laurilta".
  python scripts/reading_tips.py        validate the files
"""
import json, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

PAGE = "lukuvinkit.html"
BOOK_KEYS = {"title", "url", "author", "language", "level", "loan", "text", "courses"}
TEXT_KEYS = ("language", "level", "text")
SOURCE = ROOT / "content" / "fi" / "lukuvinkit.json"   # a copy of the project without it (a test's) builds no page


def esc(s): return _h.escape(str(s), quote=True)


def load(lang="fi"):
    """The page's data in one language: the Finnish file with a translation's texts laid over it."""
    src = json.loads(SOURCE.read_text())
    f = ROOT / "content" / lang / "lukuvinkit.json"
    if lang == "fi" or not f.is_file(): return src
    tr = json.loads(f.read_text())
    out = dict(src, **{k: v for k, v in tr.items() if k != "books" and not k.startswith("_")})
    out["books"] = [dict(b, **{k: t[k] for k in TEXT_KEYS if k in t}) for b, t in zip(src["books"], tr["books"])]
    return out


def check():
    errs = []
    src = json.loads(SOURCE.read_text())
    for i, b in enumerate(src["books"], 1):
        if set(b) != BOOK_KEYS: errs.append(f"fi book {i}: keys {sorted(set(b) ^ BOOK_KEYS)}")
        if not str(b.get("url", "")).startswith("https://"): errs.append(f"fi book {i}: url must be https")
    for f in sorted((ROOT / "content").glob("*/lukuvinkit.json")):
        d = json.loads(f.read_text()); lang = f.parent.name
        for k in ("title", "subtitle", "description", "intro", "list_lead", "loan_note", "books"):
            if k not in d: errs.append(f"{lang}: missing {k}")
        if lang != "fi":
            if len(d.get("books", [])) != len(src["books"]): errs.append(f"{lang}: {len(d.get('books', []))} books, the Finnish has {len(src['books'])}")
            for i, t in enumerate(d.get("books", []), 1):
                if set(t) - set(TEXT_KEYS): errs.append(f"{lang} book {i}: only {', '.join(TEXT_KEYS)} are translated, not {sorted(set(t) - set(TEXT_KEYS))}")
    return errs


def body(T, lang):
    """The page's <main> content."""
    d = load(lang)
    items = ""
    for b in d["books"]:
        tag = f'<p class="book-loan">{esc(T("site.reading_loan"))}</p>' if b["loan"] else ""
        facts = "".join(f'<div><dt>{esc(T("site.reading_" + k))}</dt><dd>{esc(v)}</dd></div>'
                        for k, v in (("language", b["language"]), ("level", b["level"]), ("courses", b["courses"])))
        items += (f'<li class="book"><h2 class="book-title"><a href="{esc(b["url"])}" rel="noopener">{esc(b["title"])}</a></h2>'
                  f'<p class="book-author">{esc(b["author"])}</p>{tag}<p class="book-text">{esc(b["text"])}</p>'
                  f'<dl class="book-facts">{facts}</dl></li>')
    return (f'<span class="eyebrow">{esc(d["subtitle"])}</span><h1>{esc(d["title"])}</h1>'
            + "".join(f'<p class="{"lead" if i == 0 else "reading-intro"}">{esc(p)}</p>' for i, p in enumerate(d["intro"]))
            + f'<p class="reading-list-lead">{esc(d["list_lead"])}</p>'
            + f'<p class="reading-loan-note"><span class="book-loan">{esc(T("site.reading_loan"))}</span> {esc(d["loan_note"])}</p>'
            + f'<ol class="books">{items}</ol>')


if __name__ == "__main__":
    errs = check()
    print("\n".join(errs) if errs else "lukuvinkit: ok")
    sys.exit(1 if errs else 0)
