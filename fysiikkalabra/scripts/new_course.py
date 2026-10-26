"""Initialize a course for the lesson pipeline. Usage: python scripts/new_course.py <FY4> [--check]

1. The course must be a module of curriculum.json with its LOPS 2019 data (title, tavoitteet, keskeiset_sisallot)
   and at least one lesson slot. Nothing is generated: a course without them is reported as missing and the
   script stops, because course goals come from the LOPS texts, not from a model.
2. Every LOPS item (tavoitteet, keskeiset_sisallot, temaattiset_yhteydet, kokeet) is looked up in the MAOL guide's
   text in docs/lops2019/ and every slot goal written "LOPS <code>: …" in the course's own items; what is not
   found is listed for the teacher to check (the text extraction of the two-column PDF breaks some lines).
3. Lesson slots: ids <slug>-N, unique; titles; prerequisites that exist; glossary terms missing from
   glossary.json are listed (the developer adds them when drafting the lesson, CLAUDE.md).
4. Unless --check: creates content/<CODE>/, assets/pics/<slug>/ and assets/sims/<slug>/ (each with .gitkeep) and
   writes "initialized": <date> into the course's entry in curriculum.json. Running it again only validates.
Lesson folders are not created here: /lesson <id> creates each one from its slot (courses.py init-lesson).
Exit status 1 when essential data is missing or the slots are inconsistent."""
import datetime, json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

LOPS_FIELDS = ("tavoitteet", "keskeiset_sisallot", "temaattiset_yhteydet", "kokeet")


def lops_text():
    """The MAOL guide's text as one searchable lowercase string: the two printed columns read separately, words
    broken at a line end joined again, and the raw text as well (some items are not in columns)."""
    src = courses.ROOT / courses.curriculum().get("_source", {}).get("modules", "docs/lops2019/x.pdf")
    txt_file = src.with_suffix(".txt")
    if not txt_file.exists(): return None
    raw = txt_file.read_text(); left, right = [], []
    for ln in raw.split("\n"):
        if not ln.strip(): left.append(""); right.append(""); continue
        if len(ln) - len(ln.lstrip()) >= 20: right.append(ln.strip()); continue
        parts = re.split(r"\s{3,}", ln.strip(), maxsplit=1)
        left.append(parts[0]); right.append(parts[1] if len(parts) > 1 else "")
    def norm(stream):
        s = re.sub(r"(\w)-\s+(?!ja\b|tai\b)(?=[a-zäöå])", r"\1", " ".join(stream)).replace("•", " ")   # "termodynaami- seen" -> one word; "vesi- ja" stays
        return re.sub(r"\s+", " ", s).lower()
    return " | ".join((norm(left), norm(right), norm(raw.split("\n"))))


def letters(t): return re.sub(r"[^a-zåäö]", "", t.lower())


def found(item, text, text_letters):
    """Word for word, or letter for letter when the PDF split a word at a line end without a hyphen ("törmäyk set")."""
    return re.sub(r"\s+", " ", item).strip().lower() in text or letters(item) in text_letters


def validate(code):
    """(errors, notes) for the course's curriculum entry."""
    cur = courses.curriculum()
    if code not in cur: return [f"{code} is not in curriculum.json (courses: {', '.join(courses.codes())}); add its LOPS 2019 entry first"], []
    c = cur[code]; errors, notes = [], []
    for k in ("title", "tavoitteet", "keskeiset_sisallot"):
        if not c.get(k): errors.append(f"{code}: '{k}' is missing; copy it from the LOPS 2019 module text (docs/lops2019/), do not write it from memory")
    slots = c.get("lessons", [])
    if not slots: errors.append(f"{code}: no lesson slots ('lessons'); the teacher decides the sequence and titles")
    text = lops_text()
    if text is None: notes.append("docs/lops2019/*.txt not found: the LOPS items could not be checked against the source")
    else:
        tl = letters(text)
        unverified = [f"{k}: {s}" for k in LOPS_FIELDS for s in c.get(k, []) if not found(s, text, tl)]
        total = sum(len(c.get(k, [])) for k in LOPS_FIELDS)
        notes.append(f"{total - len(unverified)}/{total} LOPS items found in the MAOL guide text (docs/lops2019/)")
        notes += [f"check by hand (not found verbatim, often a PDF line break): {u}" for u in unverified]
    own = [re.sub(r"\s+", " ", s).lower() for k in ("tavoitteet", "keskeiset_sisallot", "kokeet", "temaattiset_yhteydet") for s in c.get(k, [])]
    words = lambda t: {w for w in re.findall(r"[\wåäö-]+", t.lower()) if len(w) > 3}
    anchored = lambda g: any(g in item or words(g) <= words(item) for item in own)   # a slot goal may name a part of one LOPS item
    all_ids = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    glossary = {e["term"] for e in json.loads((courses.ROOT / "glossary.json").read_text())}
    seen, missing_terms = set(), []
    for i, l in enumerate(slots):
        lid = l.get("id", "")
        if not re.fullmatch(rf"{courses.slug(code)}-\d+[a-z]?", lid): errors.append(f"{code} lessons[{i}]: id {lid!r} should be {courses.slug(code)}-<n>")
        if lid in seen: errors.append(f"{code}: lesson id {lid} appears twice")
        seen.add(lid)
        if not l.get("title"): errors.append(f"{lid}: no title")
        for p in l.get("prerequisites", []):
            if p not in all_ids: errors.append(f"{lid}: prerequisite {p} is not a lesson slot of any course")
        for g in l.get("goals", []):
            m = re.match(rf"LOPS {code}:\s*(.+)", g)
            if m and not anchored(re.sub(r"\s+", " ", m.group(1)).lower()): notes.append(f"{lid}: goal '{g}' is not part of any {code} LOPS item; check the slot against the module text")
        missing_terms += [t for t in l.get("glossary", []) if t not in glossary and t not in missing_terms]
    if missing_terms: notes.append(f"{len(missing_terms)} glossary term(s) not yet in glossary.json (added when the lesson is drafted): {', '.join(missing_terms)}")
    return errors, notes


def initialize(code):
    c = courses.course(code)
    made = []
    for d in (c["paths"]["content"], c["paths"]["pics"], c["paths"]["sims"]):
        if not d.exists(): d.mkdir(parents=True); made.append(d)
        if not any(d.iterdir()): (d / ".gitkeep").write_text("")
    if not c.get("initialized"):
        cur = json.loads((courses.ROOT / "curriculum.json").read_text())
        entry = {}
        for k, v in cur[code].items():               # keep the key order: pipeline fields before the lesson list
            if k == "lessons": entry["initialized"] = str(datetime.date.today())
            entry[k] = v
        entry.setdefault("initialized", str(datetime.date.today()))
        cur[code] = entry
        (courses.ROOT / "curriculum.json").write_text(json.dumps(cur, ensure_ascii=False, indent=2) + "\n")
        courses.curriculum.cache_clear()
        made.append("curriculum.json: initialized")
    return made


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1: sys.exit(__doc__)
    code = args[0].upper()
    errors, notes = validate(code)
    for n in notes: print("note ", n)
    for e in errors: print("ERROR", e)
    if errors: print(f"{code}: not initialized; the data above is missing or inconsistent"); sys.exit(1)
    c = courses.course(code)
    if "--check" in sys.argv:
        print(f"{code}: valid" + (f", initialized {c['initialized']}" if c.get("initialized") else ", not initialized")); sys.exit(0)
    was = c.get("initialized")
    for m in initialize(code): print("made ", m.relative_to(courses.ROOT) if isinstance(m, pathlib.Path) else m)
    c = courses.course(code)
    print(f"{code} {c['title']}: {'already initialized ' + was + ', validated' if was else 'initialized'}; {len(c.get('lessons', []))} lesson slots")
    print(f"  lessons   {c['paths']['content'].relative_to(courses.ROOT)}/<id>/       (created by /lesson <id> from the slot)")
    print(f"  pictures  {c['paths']['pics'].relative_to(courses.ROOT)}/  -> referred to as pics/{c['slug']}/<file>")
    print(f"  sims      {c['paths']['sims'].relative_to(courses.ROOT)}/<name>/  -> published at sims/{c['slug']}/<name>/")
    todo = [l["id"] for l in c.get("lessons", []) if not (c["paths"]["content"] / l["id"] / "meta.json").exists()]
    print(f"  next      /lesson {todo[0]}" if todo else "  every slot has a lesson folder")
