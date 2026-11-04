"""Käsitetakomo links (teacher 2026-11-03: "integroi nykyinen Käsitetakomo osaksi Ruukkilabraa mahdollisimman kevyesti").

  python scripts/concept_cards.py check      validates concept-cards.json against the card data (also run by the build)

Käsitetakomo, the concept flashcards, stays where it is: `kasitetakomo.html` and its content `kasitetakomo-data.js`
in the repository root (beside fysiikkalabra/). It is never copied into the site. Ruukkilabra only links to it:
  - the front page: one link to the card app (its course menu);
  - each module page whose course has cards: "Kertaa tämän moduulin käsitteet" -> `?kurssi=<COURSE>`, the course's
    topic menu (no cards are started);
  - a lesson, only when `concept-cards.json` names card topics for it: "Kertaa luvun käsitteet" ->
    `?kurssi=<COURSE>&aihe=<id>[,<id>]`, which starts those topics' cards.
Topic ids are the permanent `id` fields of the topics in kasitetakomo-data.js. The mapping is the only place that
pairs a chapter with cards; no lesson text names them. A missing card file (a test copy of the project) turns the
links off; an unknown course, topic or lesson is an error in the build and in CI.
"""
import functools, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

MAP = ROOT / "concept-cards.json"
DATA = ROOT.parent / "kasitetakomo-data.js"
APP = "kasitetakomo.html"           # beside fysiikkalabra/: from site/ it is ../../kasitetakomo.html
TOPIC_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


@functools.lru_cache(maxsize=None)
def cards():
    """{COURSE: {"open": bool, "topics": [ids]}} read from kasitetakomo-data.js (a JS literal, read by pattern, not run).
    Empty when the file is missing."""
    if not DATA.is_file(): return {}
    text = DATA.read_text(encoding="utf-8")
    body = text.split("window.KORTIT", 1)[-1]
    out = {}
    for m in re.finditer(r'\{ id:"(FY\d+)"(, kesken:true)?, nimi:"[^"]*", aiheet:\[(.*?)(?=\n\{ id:"FY\d+"|\n\];)', body, re.S):
        out[m.group(1)] = {"open": not m.group(2), "topics": re.findall(r'\n  \{ id:"([^"]+)", nimi:"', m.group(3))}
    return out


@functools.lru_cache(maxsize=None)
def mapping():
    return json.loads(MAP.read_text(encoding="utf-8")) if MAP.is_file() else {}


def errors():
    """Every problem in the mapping and the topic ids: [] when all is well (or when there are no cards to link)."""
    data = cards()
    if not data: return []
    curriculum = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
    errs = []
    seen = {}
    for code, c in data.items():
        for t in c["topics"]:
            if not TOPIC_ID.fullmatch(t): errs.append(f"kasitetakomo-data.js: topic id {t!r} in {code} is not lowercase-with-hyphens")
            if t in seen: errs.append(f"kasitetakomo-data.js: topic id {t!r} is in {seen[t]} and {code}")
            seen[t] = code
    for code, lessons in mapping().get("lessons", {}).items():
        if code not in data: errs.append(f"concept-cards.json: {code} has no cards in kasitetakomo-data.js"); continue
        if not data[code]["open"]: errs.append(f"concept-cards.json: {code} is marked kesken in kasitetakomo-data.js")
        slots = {l["id"] for l in curriculum.get(code, {}).get("lessons", [])}
        for lid, topics in lessons.items():
            if lid not in slots: errs.append(f"concept-cards.json: {lid} is not a lesson of {code} in curriculum.json")
            if not topics: errs.append(f"concept-cards.json: {lid} names no topics (leave the lesson out instead)")
            for t in topics:
                if t not in data[code]["topics"]: errs.append(f"concept-cards.json: {lid}: topic {t!r} is not a {code} topic in kasitetakomo-data.js")
            if len(set(topics)) != len(topics): errs.append(f"concept-cards.json: {lid} names a topic twice")
    return errs


def href(up, code, topics=()):
    """The link from a page in site/ (up = "" ) or site/<lang>/ (up = "../") to the card app."""
    q = f"?kurssi={code}" + (f"&amp;aihe={','.join(topics)}" if topics else "") if code else ""
    return f"{up}../../{APP}{q}"


def module_link(code, T, up):
    """The module page's section, or "" when the course has no cards (or they are marked kesken)."""
    c = cards().get(code)
    if not c or not c["open"]: return ""
    return (f'<h2>{T("cards.title")}</h2><p>{T("cards.module_lead")}</p><ul class="lessons practice-link concept-cards"><li class="live">'
            f'<a href="{href(up, code)}">{T("cards.module_link")}</a></li></ul>')


def lesson_link(code, lid, T, up):
    """The lesson's small link, or "" when concept-cards.json names no topics for it."""
    topics = mapping().get("lessons", {}).get(code, {}).get(lid)
    if not topics or not cards().get(code, {}).get("open"): return ""
    return f'<p class="concept-link"><a href="{href(up, code, topics)}">{T("cards.lesson_link")}</a></p>'


if __name__ == "__main__":
    if sys.argv[1:] != ["check"]: sys.exit(__doc__)
    errs = errors()
    print("\n".join(errs) or f"concept cards: {sum(len(v) for v in mapping().get('lessons', {}).values())} chapters linked, "
          f"{sum(len(c['topics']) for c in cards().values())} topics in {len(cards())} courses")
    sys.exit(1 if errs else 0)
