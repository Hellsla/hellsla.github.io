"""Course units: the lessons of a school-specific course written in its own language (teacher's brief 2026-11-01,
FY14 Road to Fusion; docs/FY14_PLAN.md). A unit is not a national lesson (curriculum.json) and not an
investigation: it belongs to one local course, is written in the course's language (FY14: English, with French),
and is published only in that language's folder of the site (site/en/ for English). The course page of every
language lists the units and links to them there.

  python scripts/units.py check              validate every unit (CI)
  python scripts/units.py hash <id>          the content hash a reviewer puts in its report
  python scripts/units.py status             reviewed | draft of every unit
  python scripts/units.py figures <id> [--check]   lessons/units/<id>/figures.py into unit.md

A unit reuses the lesson's inquiry stages (scripts/inquiry.py, docs/inquiry.md: Think about it → Predict →
Investigate → Theory summary → Apply → Check your understanding) and the lesson template, so it looks and behaves
like every other chapter. What a history, language or lab unit needs beyond those activity types are the course's
own components (assets/units/<course>/, units/<course>/units.js: matching, ordering, sorting, gap fills, French
pronunciation, videos, the timeline, the map and the explorers), placed in the text as
`<div class="fx" data-fx="<kind>" ...>` with their data in a `<script type="application/json">` inside the element.

  content/<lang>/units/<id>/unit.json    id, course (a code of local-courses.json), chapter (its number in the
        course's chapters), title, description (one sentence), kind (one of KINDS), minutes (the planned class time),
        subjects (physics, english, french), sim (optional: "<course slug>/<name>", a folder of assets/sims/ with
        sim.js and strings.json), sources [{title, url, checked: "YYYY-MM-DD", note?}] (shown as "Sources and
        verification" at the end of a preview, never on the published page; every fact that may change carries a checked date), media
        [{file, title, creator, source, licence, licence_url?}] (credits of every photograph and video used)
  content/<lang>/units/<id>/unit.md      the text: `# Title`, `> **Why** …` (the opening question), the opening
        illustration (`<svg data-fig="hero">`), then `## ` sections that inquiry.json places with "theory"
        activities (a section placed nowhere goes to the Theory summary)
  content/<lang>/units/<id>/inquiry.json the activities by stage, exactly as a lesson's (validated by inquiry.py)
  content/<lang>/units/<id>/teacher.md   teacher guidance (in previews only, not on the published page): timing, organisation, assessment criteria; never
        answers to graded work or anything confidential
  content/<lang>/units/<id>/review/      science.md, pedagogy.md and visual.md, as a lesson's
  lessons/units/<id>/figures.py          the figures (scripts/figlib.py), optional
  content/<lang>/units/<id>/sovella/     optional: the unit's own exam-style task set in the Sovella itsenäisesti format
        (tasks.json, solutions.md; answers.py and figures.py in lessons/units/<id>/sovella/), checked by practice.py
        under the key units/<id>, part of the unit's hash and reviews, shown last on the page as its Tehtävät (FY12)

The content hash covers the four texts, figures.py, the simulation folder and every course asset the text refers
to (units/<course>/data/…, units/<course>/pics/…), so a changed data file or photograph needs a new review like
changed text. build.py publishes site/<lang>/<id>.html when all three reviews PASS for the current hash (preview
otherwise), and the course page lists it under its chapter.
"""
import hashlib, importlib.util, json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
DIR = "units"
TEXTS = ("unit.json", "unit.md", "inquiry.json", "teacher.md")
KINDS = ("physics", "history", "clil", "french", "lab", "explorer", "review")   # review: a lesson of the exam review course FY12
SUBJECTS = ("physics", "english", "french")
ASSET_REF = re.compile(r"""(?:src=\\?["']|data-src=\\?["']|\]\()(units/[a-z0-9]+/[^"'\\)\s]+)""")   # also inside inquiry.json, where quotes are \"
esc = lambda s: _h.escape(str(s), quote=True)


def folder(uid, lang): return ROOT / "content" / lang / DIR / uid
def code_folder(uid): return ROOT / "lessons" / DIR / uid
def asset_source(ref): return ROOT / "assets" / ref     # units/fy14/data/x.json -> assets/units/fy14/data/x.json


def languages():
    """The languages that have units (a course's units are written in one language)."""
    return [l for l in i18n.languages() if (ROOT / "content" / l / DIR).is_dir()]


def ids(lang):
    base = ROOT / "content" / lang / DIR
    found = [p.name for p in base.iterdir() if (p / "unit.json").is_file()] if base.is_dir() else []
    return sorted(found, key=lambda u: (load(u, lang).get("chapter", 99), load(u, lang).get("order", 99), u))


def load(uid, lang): return json.loads((folder(uid, lang) / "unit.json").read_text())


def lang_of(uid):
    """The language a unit is written in (the one folder that holds it), or None."""
    return next((l for l in languages() if (folder(uid, l) / "unit.json").is_file()), None)


def all_units():
    """[(lang, id)] of every unit in every language."""
    return [(l, u) for l in languages() for u in ids(l)]


def texts_of(uid, lang):
    return "".join((folder(uid, lang) / n).read_text() for n in TEXTS if (folder(uid, lang) / n).is_file())


def asset_refs(uid, lang):
    """The course assets (data files, photographs) the unit's texts refer to, in order, once each."""
    return list(dict.fromkeys(ASSET_REF.findall(texts_of(uid, lang)) + [m["file"] for m in load(uid, lang).get("media", []) if m.get("file", "").startswith("units/")]))


def sim_folder(uid, lang):
    s = load(uid, lang).get("sim")
    return ROOT / "assets" / "sims" / s if s else None


def content_hash(uid, lang):
    from reviews import normalized
    h = hashlib.sha256()
    for name in TEXTS:
        p = folder(uid, lang) / name
        if p.is_file(): h.update(name.encode() + b"\0" + normalized(p.read_text(), name).encode() + b"\0")
    p = code_folder(uid) / "figures.py"
    if p.is_file(): h.update(b"figures.py\0" + p.read_bytes() + b"\0")
    sf = sim_folder(uid, lang)
    if sf and sf.is_dir():
        for f in sorted(x for x in sf.rglob("*") if x.is_file()):
            h.update(f.relative_to(ROOT).as_posix().encode() + b"\0" + f.read_bytes() + b"\0")
    for ref in asset_refs(uid, lang):
        f = asset_source(ref)
        if f.is_file(): h.update(ref.encode() + b"\0" + f.read_bytes() + b"\0")
    if has_tasks(uid, lang):                             # the unit's own task set (scripts/practice.py): reviewed with the unit
        import practice
        h.update(b"sovella\0" + practice.content_hash(task_key(uid), lang).encode() + b"\0")
    return h.hexdigest()[:16]


def task_key(uid): return f"units/{uid}"                 # practice.py's key of the unit's task set
def has_tasks(uid, lang): return (folder(uid, lang) / "sovella" / "tasks.json").is_file()


def status(uid, lang):
    """{'state': reviewed|draft, 'hash', 'reports', 'baseline'}: three reviews for the current hash (reviews.item_status)."""
    from reviews import item_status
    return item_status("unit", uid, lang, folder(uid, lang), content_hash(uid, lang))


def check(uid, lang):
    """Error lines: required fields, a known course and chapter, the inquiry, figures in place, assets that exist,
    sources with checked dates, credits for every photograph, notation, a unique id across the site."""
    import inquiry, local_courses
    errs = []; where = f"{lang}/{DIR}/{uid}"
    try: d = load(uid, lang)
    except (OSError, ValueError) as e: return [f"{where}: unit.json: {e}"]
    cur = {k: v for k, v in courses.curriculum().items() if not k.startswith("_")}
    lessons = {l["id"] for m in cur.values() for l in m.get("lessons", [])}
    if d.get("id") != uid: errs.append(f"{where}: id {d.get('id')!r} is not the folder name")
    if uid in lessons or uid.upper() in cur: errs.append(f"{where}: the id of a lesson or module")
    if not re.fullmatch(r"[a-z]+\d+-[a-z0-9-]+", uid): errs.append(f"{where}: an id is the course slug, a hyphen and a short name (fy14-photons)")
    for f in ("title", "description", "kind", "course", "chapter", "minutes", "subjects"):
        if d.get(f) in (None, "", []): errs.append(f"{where}: no {f}")
    if d.get("kind") not in KINDS: errs.append(f"{where}: kind {d.get('kind')!r} is not one of {KINDS}")
    errs += [f"{where}: subject {s!r} is not one of {SUBJECTS}" for s in d.get("subjects", []) if s not in SUBJECTS]
    reg = local_courses.load()
    c = reg.get(d.get("course"))
    if not c: errs.append(f"{where}: course {d.get('course')!r} is not in local-courses.json")
    else:
        if c.get("language") != lang: errs.append(f"{where}: course {d['course']} is written in {c.get('language')!r}, the unit in {lang!r}")
        chs = c.get("chapters", [])
        if not (isinstance(d.get("chapter"), int) and 1 <= d["chapter"] <= len(chs)): errs.append(f"{where}: chapter {d.get('chapter')!r} is not a chapter of {d['course']} (1–{len(chs)})")
        elif uid not in [x["id"] for x in chs[d["chapter"] - 1].get("units", [])]: errs.append(f"{where}: chapter {d['chapter']} of {d['course']} does not list this unit")
    for i, s in enumerate(d.get("sources", [])):
        if not (s.get("title") and re.match(r"https://", s.get("url", "")) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", s.get("checked", ""))):
            errs.append(f"{where}: sources[{i}] needs title, an https url and checked YYYY-MM-DD")
    for i, m in enumerate(d.get("media", [])):
        if not all(m.get(k) for k in ("file", "title", "creator", "source", "licence")): errs.append(f"{where}: media[{i}] needs file, title, creator, source and licence")
    md_path = folder(uid, lang) / "unit.md"
    if not md_path.is_file(): return errs + [f"{where}: no unit.md"]
    md = md_path.read_text()
    if not re.search(r"^# .+", md, re.M): errs.append(f"{where}: unit.md starts with '# Title'")
    if not re.search(r'<svg\b[^>]*data-fig="hero"', md): errs.append(f"{where}: no opening illustration (<svg data-fig=\"hero\">, teacher 2026-10-29)")
    if re.search(r'<svg data-fig="[^"]*"></svg>', md): errs.append(f"{where}: empty figure: run units.py figures {uid}")
    allt = texts_of(uid, lang)
    if "\\vec" in allt or "\\mathbf" in allt: errs.append(f"{where}: vectors are \\overline{{F}} (teacher 2026-10-29)")
    if "×" in re.sub(r"<svg\b.*?</svg>", "", allt, flags=re.S): errs.append(f"{where}: multiplication is \\cdot, never × (teacher's rule 8)")
    for ref in asset_refs(uid, lang):
        if not asset_source(ref).is_file(): errs.append(f"{where}: asset {ref} not found (expected assets/{ref})")
    credited = {m.get("file") for m in d.get("media", [])}
    for ref in dict.fromkeys(ASSET_REF.findall(allt)):
        if re.match(r"units/[a-z0-9]+/pics/", ref) and ref not in credited: errs.append(f"{where}: photograph {ref} has no media entry (unit.json media, file {ref!r})")
    sf = sim_folder(uid, lang)
    if sf and not (sf / "sim.js").is_file(): errs.append(f"{where}: simulation {d['sim']} has no sim.js")
    inq_f = folder(uid, lang) / "inquiry.json"
    if not inq_f.is_file(): errs.append(f"{where}: no inquiry.json")
    else:
        was = i18n.t.lang; i18n.set_lang(lang)
        try: errs += [f"{where}: {e}" for e in inquiry.validate(folder(uid, lang), json.loads(inq_f.read_text()), md)]
        finally: i18n.set_lang(was)
    if has_tasks(uid, lang):                             # the unit's task set: the checks of Sovella itsenäisesti
        import practice
        errs += [f"{where}: {e}" for e in practice.check(task_key(uid), lang)]
    for kind in re.findall(r'data-fx="([\w-]+)"', allt):
        if not (ROOT / "assets" / "units" / d.get("course", "").lower() / "fx" / f"{kind}.js").is_file():
            errs.append(f"{where}: component data-fx=\"{kind}\" has no assets/units/{d.get('course', '').lower()}/fx/{kind}.js")
    for m in re.finditer(r'<div class="fx[^"]*" data-fx="[\w-]+"[^>]*>\s*<script type="application/json">(.*?)</script>', allt, re.S):
        try: json.loads(m.group(1))
        except ValueError as e: errs.append(f"{where}: component data is not JSON ({e})")
    return errs


def figures(uid, lang, write=True):
    """Fill every <svg data-fig="name"> of unit.md from figures.py; True when it was up to date (or there is none)."""
    src = code_folder(uid) / "figures.py"
    if not src.is_file() or not (folder(uid, lang) / "unit.md").is_file(): return True   # a missing unit.md is check()'s error
    spec = importlib.util.spec_from_file_location("figures", src)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    md = folder(uid, lang) / "unit.md"; text = md.read_text(); new = text
    for name, fn in mod.FIGURES.items():
        pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
        if not pat.search(new): print(f"no <svg data-fig=\"{name}\"> in unit.md"); continue
        svg = fn()
        if "data-fig=" not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
        new = pat.sub(lambda m: svg, new, count=1)
    if write and new != text: md.write_text(new)
    return new == text


def sim_block(uid, lang):
    """(sim key, strings) for the page's #fl-strings block: the simulation folder's strings.json in this language."""
    sf = sim_folder(uid, lang)
    if not sf or not (sf / "strings.json").is_file(): return None
    return json.loads((sf / "strings.json").read_text()).get(lang, {})


def tail_html(uid, lang, T, md, teacher=False):
    """The end of the page: credits of the photographs and videos, and with teacher=True (previews for reviewers
    only) the sources with the date each was checked and the teacher's notes in a closed box. The published pages
    leave both out: they are not for students (teacher 2026-11-01)."""
    d = load(uid, lang); out = ""
    if d.get("media"):
        out += (f'<section class="unit-credits" id="credits"><h2>{T("units.credits")}</h2><ul>'
                + "".join(f'<li><strong>{esc(m["title"])}</strong>. {esc(m["creator"])}. '
                          + (f'<a href="{esc(m["source"])}">{T("units.credit_source")}</a>, ' if m["source"].startswith("https://") else f'{esc(m["source"])}, ')
                          + (f'<a href="{esc(m["licence_url"])}">{esc(m["licence"])}</a>' if m.get("licence_url") else esc(m["licence"])) + "</li>"
                          for m in d["media"]) + "</ul></section>")
    if teacher and d.get("sources"):
        out += (f'<section class="unit-sources" id="sources"><h2>{T("units.sources")}</h2><p class="unit-sources-lead">{T("units.sources_lead")}</p><ul>'
                + "".join(f'<li><a href="{esc(s["url"])}">{esc(s["title"])}</a> <span class="checked">{T("units.checked", date=s["checked"])}</span>'
                          + (f'<span class="source-note">{md(s["note"])[3:-4]}</span>' if s.get("note") else "") + "</li>"
                          for s in d["sources"]) + "</ul></section>")
    t = folder(uid, lang) / "teacher.md"
    if teacher and t.is_file():
        out += f'<details class="inv-teacher unit-teacher" id="teacher"><summary>{T("units.teacher")}</summary>{md(t.read_text())}</details>'
    return out


def course_nav(uid, lang, T, published):
    """Previous / next unit in the course's order (its chapters' unit lists), published units only; the first and
    the last lead back to the course page."""
    import local_courses
    d = load(uid, lang); code = d["course"]; c = local_courses.load().get(code, {})
    seq = [x["id"] for ch in c.get("chapters", []) for x in ch.get("units", []) if f"{x['id']}.html" in published or x["id"] == uid]
    i = seq.index(uid) if uid in seq else 0
    def link(cls, rel, href, direction, name):
        return (f'<a class="{cls}" href="{href}"{f" rel={chr(34)}{rel}{chr(34)}" if rel else ""}>'
                f'<span class="dir">{direction}</span><span class="name">{esc(name)}</span></a>')
    up = (f"{code}.html", T("lesson.chapter_course", course=code))
    prev = seq[i - 1] if i > 0 else None; nxt = seq[i + 1] if i + 1 < len(seq) else None
    return (f'<nav class="chapter-nav" aria-label="{esc(T("lesson.chapter_nav"))}">'
            + (link("prev", "prev", f"{prev}.html", T("lesson.chapter_prev"), load(prev, lang)["title"]) if prev else link("prev up", "", up[0], T("lesson.chapter_up"), up[1]))
            + (link("next", "next", f"{nxt}.html", T("lesson.chapter_next"), load(nxt, lang)["title"]) if nxt else link("next up", "", up[0], T("lesson.chapter_up"), up[1]))
            + "</nav>")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    lang_arg = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else None
    if cmd == "check":
        errs = [e for l, u in all_units() for e in check(u, l)]
        errs += [f"{l}/{DIR}/{u}: figures differ from figures.py (units.py figures {u})" for l, u in all_units() if not figures(u, l, write=False)]
        print("\n".join(errs) or f"{len(all_units())} unit(s) ok"); sys.exit(1 if errs else 0)
    if cmd == "hash": u = sys.argv[2]; print(content_hash(u, lang_arg or lang_of(u)))
    if cmd == "status":
        for l, u in all_units(): print(l, u, status(u, l))
    if cmd == "figures":
        u = sys.argv[2]; ok = figures(u, lang_arg or lang_of(u), write="--check" not in sys.argv)
        print("figures up to date" if ok else ("figures differ" if "--check" in sys.argv else "figures written")); sys.exit(0 if ok or "--check" not in sys.argv else 1)
