"""Kokeelliset tutkimukset: experimental investigations, one canonical page each (teacher's brief 2026-10-30,
docs/PORTAL_ARCHITECTURE.md, docs/FY10_PLAN.md).

  python scripts/investigations.py check              validate every investigation (CI)
  python scripts/investigations.py hash <id>          the content hash a reviewer puts in its report
  python scripts/investigations.py status             reviewed | draft of every investigation
  python scripts/investigations.py figures <id> [--check]   lessons/tutkimukset/<id>/figures.py into investigation.md

An investigation is not a lesson of a course: it may serve several courses and modules without being copied.

  content/<lang>/tutkimukset/<id>/investigation.json   metadata: title, question, description, courses (codes of
        local-courses.json or curriculum.json), modules, learn (2–3 goals completing "Tässä tutkimuksessa opit"),
        variants [{id, title, physics F1–F3, experiment E1–E3}], modes (O, OO, I), prerequisites, equipment, safety,
        source. A prerequisite is {kind: physics|experiment|tvt, level: essential|helpful|extension, why} with either
        target (a lesson id: linked where published, else named with its module) or text + missing (no page yet).
  content/<lang>/tutkimukset/<id>/investigation.md     the student text: `## ` sections; `::: tuki O OO` … `:::`
        is guidance shown only in those working modes (one page, no copies per mode); `[[apua:<lesson id>|label]]`
        is a just-in-time help link, linked only where the chapter is published; `<svg data-fig="name"></svg>`
        is filled from figures.py.
  content/<lang>/tutkimukset/<id>/teacher.md           public teacher guidance (never answers or anything confidential)
  content/<lang>/tutkimukset/<id>/review/              science.md and pedagogy.md, as a lesson's
  lessons/tutkimukset/<id>/figures.py                  the figures (scripts/figlib.py)

build.py publishes site/<id>.html when both reviews PASS for the current hash (preview otherwise), and the page of
each course in `courses` lists it: the course refers to the investigation, it never holds a copy.
"""
import hashlib, importlib.util, json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
DIR = "tutkimukset"
TEXTS = ("investigation.json", "investigation.md", "teacher.md")
KINDS = ("physics", "experiment", "tvt")
LEVELS = ("essential", "helpful", "extension")
MODES = ("O", "OO", "I")
esc = lambda s: _h.escape(str(s), quote=True)


def folder(iid, lang=i18n.SOURCE): return ROOT / "content" / lang / DIR / iid
def code_folder(iid): return ROOT / "lessons" / DIR / iid


def ids(lang=i18n.SOURCE):
    base = ROOT / "content" / lang / DIR
    return sorted(p.name for p in base.iterdir() if (p / "investigation.json").is_file()) if base.is_dir() else []


def load(iid, lang=i18n.SOURCE): return json.loads((folder(iid, lang) / "investigation.json").read_text())


def content_hash(iid, lang=i18n.SOURCE):
    from reviews import normalized
    h = hashlib.sha256()
    for name in TEXTS:
        p = folder(iid, lang) / name
        if p.is_file(): h.update(name.encode() + b"\0" + normalized(p.read_text(), name).encode() + b"\0")
    p = code_folder(iid) / "figures.py"
    if p.is_file(): h.update(b"figures.py\0" + p.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def status(iid, lang=i18n.SOURCE):
    """{'state': reviewed|draft, 'hash', 'reports': {science|pedagogy: PASS|FAIL|stale|missing}}"""
    from reviews import report, REVIEWS
    h = content_hash(iid, lang); reports = {}
    for name in REVIEWS:
        r = report(folder(iid, lang), name)
        reports[name] = "missing" if r is None else r[0] if r[1] == h else "stale"
    return {"state": "reviewed" if all(v == "PASS" for v in reports.values()) else "draft", "hash": h, "reports": reports}


def check(iid, lang=i18n.SOURCE):
    """Error lines: required fields, known kinds, levels and modes, course codes and lesson ids that exist, help
    links to lessons, mode blocks closed, figures in place, unique id across lessons."""
    import local_courses
    errs = []; d = load(iid, lang); where = f"{DIR}/{iid}"
    cur = {k: v for k, v in json.loads((ROOT / "curriculum.json").read_text()).items() if not k.startswith("_")}
    lessons = {l["id"] for m in cur.values() for l in m.get("lessons", [])}
    if d.get("id") != iid: errs.append(f"{where}: id {d.get('id')!r} is not the folder name")
    if iid in lessons or iid.upper() in cur: errs.append(f"{where}: the id of a lesson or module")
    for f in ("title", "question", "description", "learn", "variants", "modes", "prerequisites", "courses"):
        if not d.get(f): errs.append(f"{where}: no {f}")
    if not 2 <= len(d.get("learn", [])) <= 3: errs.append(f"{where}: learn has 2–3 goals")
    for c in d.get("courses", []):
        if c not in cur and c not in local_courses.load(): errs.append(f"{where}: course {c} is in neither curriculum.json nor local-courses.json")
    for v in d.get("variants", []):
        if not re.fullmatch(r"F[123]", v.get("physics", "")) or not re.fullmatch(r"E[123]", v.get("experiment", "")):
            errs.append(f"{where}: variant {v.get('id')} needs physics F1–F3 and experiment E1–E3 (safety is assessed apart)")
    errs += [f"{where}: unknown mode {m}" for m in d.get("modes", []) if m not in MODES]
    for p in d.get("prerequisites", []):
        if p.get("kind") not in KINDS or p.get("level") not in LEVELS: errs.append(f"{where}: prerequisite {p} kind/level")
        if "target" in p and p["target"] not in lessons: errs.append(f"{where}: prerequisite target {p['target']} is not a lesson")
        if "target" not in p and not (p.get("text") and p.get("missing")): errs.append(f"{where}: a prerequisite without a target needs text and missing")
        if not p.get("why"): errs.append(f"{where}: prerequisite without why")
    md = (folder(iid, lang) / "investigation.md").read_text()
    for t in re.findall(r"\[\[apua:([\w-]+)", md):
        if t not in lessons: errs.append(f"{where}: help link to {t}, not a lesson")
    opens = re.findall(r"^::: tuki ([A-Z ]+)$", md, re.M); closes = re.findall(r"^:::$", md, re.M)
    if len(opens) != len(closes): errs.append(f"{where}: {len(opens)} '::: tuki' blocks but {len(closes)} ':::' ends")
    errs += [f"{where}: '::: tuki {o}' names an unknown mode" for o in opens if any(m not in MODES for m in o.split())]
    if re.search(r'<svg data-fig="[^"]*"></svg>', md): errs.append(f"{where}: empty figure: run investigations.py figures {iid}")
    if "\\vec" in md or "\\mathbf" in md: errs.append(f"{where}: vectors are \\overline{{F}} (teacher 2026-10-29)")
    return errs


def figures(iid, write=True):
    """Fill every <svg data-fig="name"> of investigation.md from figures.py; returns True when it was up to date."""
    spec = importlib.util.spec_from_file_location("figures", code_folder(iid) / "figures.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    md = folder(iid) / "investigation.md"; text = md.read_text(); new = text
    for name, fn in mod.FIGURES.items():
        pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
        if not pat.search(new): print(f"no <svg data-fig=\"{name}\"> in investigation.md"); continue
        svg = fn()
        if "data-fig=" not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
        new = pat.sub(lambda m: svg, new, count=1)
    if write and new != text: md.write_text(new)
    return new == text


def _chapter(lid, T, chapters, published):
    """A lesson as a link where this language published it, else its title and module named as coming."""
    code, title = chapters[lid]
    if f"{lid}.html" in published: return f'<a href="{lid}.html">{esc(title)}</a> <span class="inv-mod">({code})</span>'
    return f'{esc(title)} <span class="inv-mod">({code}, {T("investigation.not_published")})</span>'


def render(iid, lang, T, md, chapters, published):
    """(body html, toc html) of the investigation page. md renders markdown with maths; chapters: lesson id ->
    (module, title) in this language; published: the page names this language built."""
    d = load(iid, lang); f = folder(iid, lang)
    text = (f / "investigation.md").read_text()
    def help_link(m):
        lid, label = m.group(1), m.group(2)
        code, _ = chapters[lid]
        inner = f'<a href="{lid}.html">{esc(label)}</a>' if f"{lid}.html" in published else f'{esc(label)} ({code}, {T("investigation.not_published")})'
        return f'<span class="inv-help">{T("investigation.need_help")} → {inner}</span>'
    text = re.sub(r"\[\[apua:([\w-]+)\|([^\]]+)\]\]", help_link, text)
    blocks = []
    def tuki(m):
        blocks.append(f'<div class="inv-tuki" data-modes="{m.group(1).strip()}">{md(m.group(2))}</div>')
        return f"\n\nTUKIBLOCK{len(blocks) - 1}X\n\n"
    text = re.sub(r"^::: tuki ([A-Z ]+)\n(.*?)^:::$", tuki, text, flags=re.S | re.M)
    html = md(text)
    html = re.sub(r"<p>TUKIBLOCK(\d+)X</p>", lambda m: blocks[int(m.group(1))], html)
    sections = re.split(r"(?=<h2>)", html)
    intro, rest = sections[0], sections[1:]
    toc = []
    def anchor(h): return re.sub(r"[^a-z0-9äö]+", "-", h.lower()).strip("-").replace("ä", "a").replace("ö", "o")
    body_parts = []
    for s in rest:
        h = re.match(r"<h2>(.*?)</h2>", s).group(1); a = anchor(re.sub(r"<[^>]+>", "", h)); toc.append((a, re.sub(r"<[^>]+>", "", h)))
        body_parts.append(f'<section class="inv-section" id="{a}">' + s.replace("<h2>", f'<h2 id="h-{a}">', 1) + "</section>")
    # the opening: goals, levels and the working mode, then what the student needs
    learn = "".join(f"<li>{esc(g)}</li>" for g in d["learn"])
    levels = "".join(f'<li><strong>{esc(v["title"])}</strong>: {T("investigation.level_physics")} {v["physics"]} · '
                     f'{T("investigation.level_experiment")} {v["experiment"]}</li>' for v in d["variants"])
    modes = "".join(f'<label class="inv-mode"><input type="radio" name="inv-mode" value="{m}"{" checked" if i == 0 else ""}>'
                    f'<span><strong>{T("investigation.mode_" + m)}</strong> {T("investigation.mode_" + m + "_text")}</span></label>'
                    for i, m in enumerate(d["modes"]))
    prereq = ""
    for kind in KINDS:
        items = ""
        for p in [p for p in d["prerequisites"] if p["kind"] == kind]:
            what = _chapter(p["target"], T, chapters, published) if "target" in p else f'{esc(p["text"])} <span class="inv-mod">({esc(p["missing"])})</span>'
            items += (f'<li><span class="inv-level inv-level-{p["level"]}">{T("investigation.prereq_" + p["level"])}</span> {what}'
                      f'<span class="inv-why">{md(p["why"])[3:-4]}</span></li>')
        if items: prereq += f'<h3>{T("investigation.kind_" + kind)}</h3><ul class="inv-prereq">{items}</ul>'
    kit = ("<h3>" + T("investigation.equipment") + "</h3><ul>" + "".join(f"<li>{esc(x)}</li>" for x in d.get("equipment", [])) + "</ul>"
           + "<h3>" + T("investigation.safety") + '</h3><ul class="inv-safety">' + "".join(f"<li>{esc(x)}</li>" for x in d.get("safety", [])) + "</ul>")
    opening = (f'<div class="inv-learn"><h2 id="h-tavoitteet">{T("investigation.learn")}</h2><ul>{learn}</ul>'
               f'<h3>{T("investigation.levels")}</h3><ul class="inv-levels">{levels}</ul><p class="inv-levels-note">{T("investigation.levels_note")}</p></div>'
               f'<fieldset class="inv-modes"><legend>{T("investigation.choose_mode")}</legend>{modes}</fieldset>'
               f'<section class="inv-section" id="tarvitset"><h2 id="h-tarvitset">{T("investigation.needs")}</h2>{prereq}{kit}</section>')
    toc = [("tarvitset", T("investigation.needs"))] + toc
    teacher = f / "teacher.md"
    tail = (f'<details class="inv-teacher" id="opettajalle"><summary>{T("investigation.teacher")}</summary>{md(teacher.read_text())}</details>'
            if teacher.is_file() else "")
    # teacher guidance closes the page and stays out of the students' stage navigation
    body = f'<article id="teoria" class="investigation">{intro}{opening}{"".join(body_parts)}{tail}</article>'
    return body, "".join(f'<a href="#{a}">{esc(t)}</a>' for a, t in toc)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        errs = [e for lang in i18n.languages() for iid in ids(lang) for e in check(iid, lang)]
        errs += [f"{DIR}/{iid}: figures differ from figures.py (investigations.py figures {iid})" for iid in ids() if not figures(iid, write=False)]
        print("\n".join(errs) or f"{len(ids())} investigation(s) ok"); sys.exit(1 if errs else 0)
    if cmd == "hash": print(content_hash(sys.argv[2], sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else i18n.SOURCE))
    if cmd == "status":
        for lang in i18n.languages():
            for iid in ids(lang): print(lang, iid, status(iid, lang))
    if cmd == "figures":
        ok = figures(sys.argv[2], write="--check" not in sys.argv)
        print("figures up to date" if ok else ("figures differ" if "--check" in sys.argv else "figures written")); sys.exit(0 if ok or "--check" not in sys.argv else 1)
