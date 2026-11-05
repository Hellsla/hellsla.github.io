#!/usr/bin/env python3
"""Light editorial check (teacher's brief 2026-11-04, "kevyt automaattinen toimituksellinen tarkistus").

It only reports; it never changes a text. Every finding is for a human to look at:

  stale-ref     a chapter named in italics after "luku/luvussa/…" (en "chapter", fi-easy as Finnish) that is not a
                current chapter, unit, investigation or guide title of that language (a renamed or split chapter)
  unpublished   a sentence claiming that an FY1–FY8 module or its chapters are not yet on the site
  missing-ok    an investigation prerequisite marked "missing" whose text names a chapter that exists
  bad-prereq    an investigation prerequisite id that is not a chapter in curriculum.json
  leftover      an editorial leftover in a student text (TODO, FIXME, XXX, "kesken", "lorem")

  python scripts/editorial_check.py              report everything (exit 0)
  python scripts/editorial_check.py --check      exit 1 when anything is found (CI)
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

ROOT = courses.ROOT
CONTENT = ROOT / "content"
LANGS = ("fi", "en", "fi-easy")
TEXTS = ("lesson.md", "inquiry.json", "exit-ticket.json", "exercises.json", "solutions.md", "unit.md", "investigation.md",
         "guide.md", "teacher.md", "meta.json", "investigation.json", "unit.json", "tasks.json")
REF = {"fi": re.compile(r"\b[Ll]u(?:ku|vu|vu\w+|ku\w+)\s+\*([^*\n]{3,120})\*"),
       "en": re.compile(r"\b[Cc]hapters?\s+\*([^*\n]{3,120})\*")}
UNPUBLISHED = re.compile(r"(ei(?:vät)? (?:ole )?vielä (?:valmii?n|valmiina|sivustolla|julkaistu|julkaistuja|verkossa)|"
                         r"ei ole vielä julkaistu|(?:are|is) not (?:yet )?(?:on the site|published|ready)|not yet (?:published|on the site|ready))",
                         re.I)
LEFTOVER = re.compile(r"\b(TODO|FIXME|XXX|lorem ipsum)\b|\bkesken(?:eräinen)?\b(?=[^.]*\b(?:luku|teksti|osio)\b)", re.I)


def norm(t):
    t = re.sub(r"\$[^$]*\$", "", t)                # a title's formula ("Teho: $P = …$") is often left out of a reference
    return re.sub(r"[\s:–-]+$", "", re.sub(r"\s+", " ", t)).strip().lower()


def titles(lang):
    """Every title a reference in this language may name: chapters, units, investigations, guides, Sovella."""
    out = set()
    for f in (CONTENT / lang).rglob("meta.json"):
        try: t = json.loads(f.read_text()).get("title")
        except ValueError: continue
        if t: out.add(t)
    for name in ("investigation.json", "unit.json", "guide.json"):
        for f in (CONTENT / lang).rglob(name):
            try: t = json.loads(f.read_text()).get("title")
            except ValueError: continue
            if t: out.add(t)
    for f in (CONTENT / lang).rglob("*.md"):         # a unit's or an investigation's "# Title" line
        if f.name in ("unit.md", "investigation.md", "guide.md"):
            m = re.match(r"#\s+(.+)", f.read_text())
            if m: out.add(m.group(1))
    for f in (ROOT / "local-courses.json", CONTENT / lang / "local-courses.json"):   # a local course's chapter groups
        if f.is_file(): out |= set(_titles_in(json.loads(f.read_text())))
    if lang == "fi":
        for k, v in courses.curriculum().items():
            if not k.startswith("_"): out |= {l["title"] for l in v.get("lessons", [])}
    return {norm(t) for t in out} | {norm(t.split(":")[0]) for t in out}


def _titles_in(x):
    if isinstance(x, dict):
        if isinstance(x.get("title"), str): yield x["title"]
        for v in x.values(): yield from _titles_in(v)
    elif isinstance(x, list):
        for v in x: yield from _titles_in(v)


def files(lang):
    for f in sorted((CONTENT / lang).rglob("*")):
        if f.is_file() and f.name in TEXTS and "/review/" not in f.as_posix(): yield f


def scan():
    found = []
    for lang in LANGS:
        names, rx = titles(lang), REF["en" if lang == "en" else "fi"]
        for f in files(lang):
            rel = f.relative_to(ROOT).as_posix()
            for i, ln in enumerate(f.read_text().splitlines(), 1):
                for m in rx.finditer(ln):
                    if norm(m.group(1)) not in names: found.append(("stale-ref", rel, i, m.group(1)))
                if f.name != "meta.json" and courses_named(ln) and UNPUBLISHED.search(ln):
                    found.append(("unpublished", rel, i, UNPUBLISHED.search(ln).group(0)))
                m = LEFTOVER.search(ln)
                if m and f.suffix == ".md" and not ln.lstrip().startswith("<!--"): found.append(("leftover", rel, i, m.group(0)))
    found += prereqs()
    return found


def courses_named(ln):
    return re.search(r"\bFY[1-8]\b|\b(module|moduuli|luvut|luku|luvun|chapters?)\b", ln, re.I)


def prereqs():
    """Investigation prerequisites: an id must be a chapter; a "missing" one should not name an existing chapter."""
    out, cur = [], courses.curriculum()
    ids = {l["id"]: l["title"] for k, v in cur.items() if not k.startswith("_") for l in v.get("lessons", [])}
    by_title = {norm(t): i for i, t in ids.items()} | {norm(t.split(":")[0]): i for i, t in ids.items()}
    for f in sorted((CONTENT / "fi" / "tutkimukset").glob("*/investigation.json")):
        rel = f.relative_to(ROOT).as_posix()
        for p in json.loads(f.read_text()).get("prerequisites", []):
            pid = p.get("id") if isinstance(p, dict) else p
            if pid and pid not in ids and not str(pid).startswith(("tvt-", "fy10-")):
                out.append(("bad-prereq", rel, 1, str(pid)))
            if isinstance(p, dict) and p.get("missing"):
                text = " ".join(str(v) for v in p.values() if isinstance(v, str))
                for t, i in by_title.items():
                    if len(t) > 8 and t in text.lower(): out.append(("missing-ok", rel, 1, f"{text[:80]} → {i}"))
    return out


def main(argv):
    found = scan()
    for kind, rel, line, what in found: print(f"{kind:12} {rel}:{line}  {what}")
    print(f"{len(found)} finding(s) for a human to check" if found else "editorial check: nothing found")
    return 1 if found and "--check" in argv else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
