"""Review state of a lesson and of its exercise set: one content hash each, two reviews each, no status fields.

  python scripts/reviews.py hash <id> [--exercises] [--lang en]   the content hash (reviewers put it in their report)
  python scripts/reviews.py status [<id>]              reviewed | legacy | draft of the lesson and its exercises
  python scripts/reviews.py legacy <id>                write review/legacy.md: prototype content the teacher keeps visible
  python scripts/reviews.py scope <id> [--exercises]   per reviewer: none, delta or full, from what changed since its PASS
  python scripts/reviews.py carry <id> [--exercises]   record that a reviewer's PASS carries over a change it need not see
  python scripts/reviews.py impact [<ref>]   which lessons a change since <ref> (default origin/main) touches, and
                                             which review each needs; shared simulations count for every user
  python scripts/reviews.py verify           CI: every lesson's state; exit 1 on a malformed report or an invalid carry

Two parts are reviewed apart (teacher 2026-10-28, README "Exercises"): the *lesson* (its texts, simulation, figures
and lesson-answers.py, reports in review/) and its *exercises* (exercises/exercises.json, exercises/solutions.md and
answers.py, reports in exercises/review/), so writing exercises never stales the lesson's reviews and the lesson
never stales theirs. Everything below holds for each part with its own files, hash and reports; `--exercises`
picks the exercise set. Before the split one hash covered both (PARTS "all"); a PASS on such a hash still counts
when the commit that holds it has the same files as now, moved but unchanged (category "split", below).

A part is *reviewed* when review/science.md and review/pedagogy.md both start with `VERDICT: PASS` and carry
the current CONTENT-HASH, or a hash whose PASS carries over to the current one (below). It is *legacy* when
review/legacy.md does (a prototype lesson published before the two-review pipeline, kept visible by the
teacher's approval of the migration PR until it is reworked). Anything else is a *draft*: the build leaves it
out of site/ and warns if it was on the live site.

The hash covers what the reviewers judge: the lesson files, tests/sims/<id>.json, the simulation folder the lesson
uses (assets/sims/<course>/<name>/, so a change there stales every lesson that uses it) and the pictures its text
refers to. Formatting is normalised (`normalized`): line endings, trailing whitespace, blank-line runs and JSON
layout do not change it. Build scripts, templates and the course config are not content: changing them never
stales a review; CI re-runs every check and rebuilds every page instead.

What changed decides who must look again (`scope`, rules in RULES). Each changed line since the version a
reviewer passed is put in a category: a number, a formula, an answer, the simulation's code, a figure, an
experiment's setup, the structure, the objectives, wording, a figure's colours or a label nudged a few units, a
comment, a test, the formula section given its law's name (`## Kaava` → `## Kaava: Lämpömäärä`), the sim activity's
text moved word for word between its lead and its boxes (Käyttöohje, Mallin oletukset, Laskennan selitys). The reviewer's mode is the strictest any category asks of it: `full`, `delta` (its previous
report and the diff), or `none`. `none` is for changes outside its judgement: comments, tightened simulation
tests, and for the science reviewer a figure's style or a label moved without new text (check_layout.py checks
those). `carry` then writes review/carry.tsv (date, reviewer, from-hash, to-hash, base commit, categories), and
`status` counts that PASS for the new hash. CI (`verify`) re-derives every carry that is in use from git history
and fails if the change was not what the row says. A reviewer whose last verdict was FAIL always reviews in full.
"""
import datetime, difflib, functools, hashlib, json, os, pathlib, re, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, figcat, i18n, inquiry

ROOT = courses.ROOT
REVIEWS = ("science", "pedagogy")
CONTENT = ("meta.json", "lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim.js", "sim-spec.md", "inquiry.json")
EXERCISE_CONTENT = ("exercises.json", "solutions.md", "answers.py")
LESSON_CONTENT = tuple(n for n in CONTENT if n not in EXERCISE_CONTENT) + ("lesson-answers.py",)
PARTS = {"lesson": LESSON_CONTENT, "exercises": EXERCISE_CONTENT,
         "all": CONTENT}            # the one hash of a lesson before the exercises got their own reviews (2026-10-28)
MODES = ("none", "delta", "full")
RULES = {                       # category: (science, pedagogy)
    "tests":          ("none",  "none"),    # tests/sims assertions added or tightened: test_sims.py checks them
    "comments":       ("none",  "none"),    # comment or blank lines in simulation code or answers.py
    "style":          ("none",  "delta"),   # colours, strokes, fonts, classes in a figure; a simulation's sim.css
    "label-position": ("none",  "delta"),   # a figure label moved by at most 40 units, its text unchanged
    "relocated":      ("none",  "delta"),   # the sim activity's text moved word for word into its lead and boxes (inquiry.json)
    "objective-form": ("none",  "delta"),
    "chapter-ref":    ("none",  "none"),    # a reference "(luku *<title>*)" follows a chapter's new title, which is a current title (teacher 2026-10-29)   # a learning goal (inquiry.json learn) rephrased to complete "Tällä tunnilla opit", same symbols and numbers (teacher 2026-10-29)
    "section-name":   ("delta", "delta"),   # a section heading given or changed its name, key unchanged (## Kaava: Lämpömäärä)
    "wording":        ("delta", "delta"),   # prose without a number, formula, symbol or unit
    "numbers":        ("full",  "delta"),   # a changed line carries a number, formula, symbol or unit
    "answers":        ("full",  "delta"),   # an exercise answer, unit or tolerance; answers.py code
    "tests-weakened": ("full",  "none"),    # a simulation assertion removed or loosened
    "levels":         ("delta", "full"),    # an exercise's level or id
    "structure":      ("delta", "full"),    # headings, stages, display blocks; inquiry stage, type, reveal, sections
    "objectives":     ("delta", "full"),    # meta goals or prerequisites
    "experiment":     ("full",  "full"),    # inquiry correct option, initial/locked/vary/measure, numeric answer, mistakes
    "simulation":     ("full",  "full"),    # simulation code or images (the lesson's or a shared folder it uses)
    "figure":         ("full",  "full"),    # figure geometry or text; a picture file
    "illustration":   ("none",  "delta"),   # an illustration (data-fig="hero" or "scene"): no text, no physics claim (teacher 2026-10-26)
    "split":          ("none",  "none"),    # passed as one lesson before the split; this part's files moved, unchanged (answers.py: line for line)
}
WHY = {"tests": "simulation tests added or tightened", "comments": "comments only", "style": "figure or sim styling only",
       "label-position": "a figure label nudged, text unchanged", "wording": "wording without numbers or symbols",
       "relocated": "the sim's text moved word for word into its lead and boxes",
       "chapter-ref": "a chapter reference follows that chapter's new title",
       "objective-form": "learning goals rephrased to complete their heading, symbols and numbers unchanged", "section-name": "a section named after its law",
       "numbers": "a changed line carries a number, formula, symbol or unit", "answers": "an answer, unit, tolerance or answers.py changed",
       "tests-weakened": "a simulation assertion removed or loosened", "levels": "an exercise level or id changed",
       "structure": "headings, stages, display blocks or inquiry structure changed", "objectives": "meta goals or prerequisites changed",
       "experiment": "an experiment setup, correct option or numeric answer in inquiry.json changed",
       "simulation": "the simulation's code changed", "figure": "a figure or picture changed",
       "illustration": "the illustrations only",
       "split": "the exercises moved to their own folder, every file as it was passed (answers.py split line for line)"}


FIGURE_TEXTS = {"lesson": ("inquiry.json", "exit-ticket.json"), "exercises": ("exercises.json",)}   # texts whose "figure": "<id>" the hash follows


def find_lesson(lid): return courses.find_lesson(lid)


def figure_paths(folder):
    """figures.py of every figure the lesson's texts refer to by id (another chapter's too), for git log."""
    texts = " ".join(courses.lesson_file(folder, n).read_text() for n in FIGURE_TEXTS["lesson"] + FIGURE_TEXTS["exercises"]
                     if courses.lesson_file(folder, n).is_file())
    return sorted({figcat.code_rel(f) for f in figcat.refs_in(texts) if figcat.code_rel(f)})


def normalized(text, name):
    """Formatting-free view of a content file that cannot hide a change of meaning: JSON is re-serialised
    canonically (same data, same hash); in text only line endings, trailing whitespace and runs of blank lines are
    dropped. Indentation and the spaces inside a line stay, because they carry meaning in Python, Markdown
    (nested lists, code blocks), LaTeX (`\\text{}`) and JavaScript strings."""
    if name.endswith(".json"):
        return json.dumps(json.loads(text), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    out = []
    for l in text.replace("\r\n", "\n").split("\n"):
        l = l.rstrip()
        if l == "" and out and out[-1] == "": continue
        out.append(l)
    while out and out[-1] == "": out.pop()
    return "\n".join(out)


def git(*args, binary=False):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=not binary)
    return r.stdout if r.returncode == 0 else None


LEGACY = re.compile(r"^(?:content/fi|lessons)/([^/]+/[^/]+/.+)$")
MOVED = re.compile(r"^(content/[^/]+/[^/]+/[^/]+)/exercises/(exercises\.json|solutions\.md)$")   # in the lesson folder until 2026-10-28


def review_dir(folder, part="lesson"):
    """review/ of the lesson, exercises/review/ of its exercise set."""
    return (folder if part == "lesson" else courses.exercise_dir(folder)) / "review"


class Source:
    lang = i18n.SOURCE                               # the language whose lang/<lang>.json fills a simulation's texts
    def source(self, rel, binary=False):
        """What the reviews judge of a file: a simulation's JavaScript with its texts from lang/fi.json put back in
        place (i18n.resolve_js), so moving a text to the language file changes nothing here, while changing it there
        changes the lesson like any other content change; every other file as it is."""
        if rel.startswith("figure:"): return figcat.slice_of(rel[7:], self.read)   # the code that draws a referenced figure
        data = self.read(rel, binary)
        if data is None or binary or not rel.endswith(".js"): return data
        lang = self.read(f"lang/{self.lang}.json")
        try: table = json.loads(lang) if lang else {}
        except json.JSONDecodeError: table = {}
        return i18n.resolve_js(data, i18n.sim_strings(i18n.sim_key(rel), table=table))


class WorkTree(Source):
    """Reads a lesson's sources from the working tree (paths relative to ROOT)."""
    def read(self, rel, binary=False):
        f = ROOT / rel
        if not f.is_file(): return None
        return f.read_bytes() if binary else f.read_text()
    def files(self, reldir):
        d = ROOT / reldir
        return sorted(p.relative_to(ROOT).as_posix() for p in d.rglob("*") if p.is_file()) if d.is_dir() else []


class Commit(Source):
    """Reads the same sources as they were in a git commit."""
    def __init__(self, sha): self.sha = sha
    def read(self, rel, binary=False):
        """The file at rel, or, in an older commit, where it was then: before the exercise folders (2026-10-28)
        exercises.json and solutions.md sat in the lesson folder, and before the languages content/<COURSE>/<id>/
        held a lesson's texts and code together (content/fi/FY3/fy3-2/lesson.md and lessons/FY3/fy3-2/sim.js were
        content/FY3/fy3-2/), so a review passed before a move still finds the version it passed."""
        data = self._read(rel, binary)
        m = MOVED.match(rel) if data is None else None
        return self._read(f"{m.group(1)}/{m.group(2)}", binary) if m else data
    def _read(self, rel, binary):
        data = git("show", f"{self.sha}:./{rel}", binary=binary)   # ./ is relative to ROOT, not the repository
        m = LEGACY.match(rel) if data is None else None
        return git("show", f"{self.sha}:./content/{m.group(1)}", binary=binary) if m else data
    def files(self, reldir):
        out = git("ls-tree", "-r", "--name-only", "--full-name", self.sha, "--", reldir) or ""
        top = (git("rev-parse", "--show-prefix") or "").strip()
        return sorted(p[len(top):] if top and p.startswith(top) else p for p in out.split())


def entries(folder, src, part="lesson"):
    """[(name, relpath, binary)] of everything the reviews of `part` judge, as `src` sees it: the exercise set is its
    files and the pictures they refer to; the lesson is the rest. FY3 lessons keep exactly the names they had before
    simulation folders and pictures existed, so their hashes did not change ("all", the hash before the split)."""
    lid = folder.name; src.lang = courses.lang_of(folder); at = lambda n: courses.lesson_rel(folder, n)
    out = [(n, at(n), False) for n in PARTS[part]]
    texts = courses.EXERCISE_FILES if part == "exercises" else courses.LESSON_TEXTS if part == "lesson" else courses.TEXT_FILES
    refs = courses.pic_refs_in(src.read(at(n)) for n in texts)
    if part != "all":                                  # figures a task refers to by id (scripts/figcat.py): their drawing code, and their words in a translation
        for fid in figcat.refs_in(" ".join(src.read(at(n)) or "" for n in FIGURE_TEXTS[part])):
            out.append((f"figure:{fid}", f"figure:{fid}", False))
            tf = figcat.text_folder(figcat.split_id(fid)[0], src.lang) if src.lang != i18n.SOURCE else None
            if tf: out.append((f"figures.json:{fid}", (tf / "figures.json").relative_to(ROOT).as_posix(), False))
    if part == "exercises": return out + [(r, f"assets/{r}", r.lower().endswith(courses.BINARY)) for r in refs]
    out += [(f"tests/sims/{lid}.json", f"tests/sims/{lid}.json", False)]
    meta_text = src.read(at("meta.json"))
    try: meta = json.loads(meta_text) if meta_text else {}
    except json.JSONDecodeError: meta = {}
    loc = courses.sim_location(lid, meta.get("sim"), src.read(at("sim.js")) is not None)
    if loc and loc[0] != "lesson":
        out += [(f"{loc[2]}/{p[len(loc[1]) + 1:]}", p, p.lower().endswith(courses.BINARY)) for p in src.files(loc[1])]
    out += [(r, f"assets/{r}", r.lower().endswith(courses.BINARY)) for r in refs]
    return out


def hash_of(folder, src, part="lesson"):
    """The content hash of `part` as `src` sees it (None if it did not exist there)."""
    h, found = hashlib.sha256(), False
    for name, rel, binary in entries(folder, src, part):
        data = src.source(rel, binary)
        if data is None: continue
        found = True
        h.update(name.encode() + b"\0" + (data if binary else normalized(data, name).encode()) + b"\0")
    return h.hexdigest()[:16] if found else None


def content_hash(folder, part="lesson"): return hash_of(folder, WorkTree(), part)
def hash_at(commit, folder, part="lesson"): return hash_of(folder, Commit(commit), part)


def report(folder, name, part="lesson"):
    """(verdict, hash) from review/<name>.md (exercises/review/ for the exercises), or None when there is no report.
    A malformed report raises."""
    f = review_dir(folder, part) / f"{name}.md"
    if not f.exists(): return None
    lines = f.read_text().splitlines()[:3]
    verdict = lines[0].split(":", 1)[1].strip() if lines and lines[0].startswith("VERDICT:") else None
    h = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("CONTENT-HASH:")), None)
    if verdict not in ("PASS", "FAIL") or not h:
        raise ValueError(f"{f.relative_to(ROOT)}: line 1 must be `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: <hash>`")
    return verdict, h


CARRY_COLS = ["date", "reviewer", "from", "to", "base", "categories"]


def carries(folder, part="lesson"):
    f = review_dir(folder, part) / "carry.tsv"
    if not f.exists(): return []
    lines = f.read_text().splitlines()
    return [dict(zip(CARRY_COLS, l.split("\t"))) for l in lines[1:] if l.strip()]


def carried(folder, name, from_hash, to_hash, part="lesson"):
    return next((c for c in carries(folder, part) if c["reviewer"] == name and c["from"] == from_hash and c["to"] == to_hash), None)


def status(folder, part="lesson"):
    """{'state': reviewed|legacy|draft, 'hash': ..., 'reports': {name: PASS|FAIL|stale|missing}, 'carried': {name: categories}}
    of the lesson or of its exercise set (which has no legacy state)."""
    h = content_hash(folder, part)
    reports, carry = {}, {}
    for name in REVIEWS + (("legacy",) if part == "lesson" else ()):
        r = report(folder, name, part)
        if r is None: reports[name] = "missing"
        elif r[1] == h: reports[name] = r[0]
        elif name != "legacy" and r[0] == "PASS" and (c := carried(folder, name, r[1], h, part)):
            reports[name] = "PASS"; carry[name] = c["categories"]
        else: reports[name] = "stale"
    state = ("reviewed" if all(reports[n] == "PASS" for n in REVIEWS)
             else "legacy" if reports.get("legacy") == "PASS" else "draft")
    return {"state": state, "hash": h, "reports": reports, "carried": carry}


def describe(folder, part=None):
    """`fy3-6: reviewed (...); exercises: reviewed (...)`, or one part's half."""
    def one(p):
        s = status(folder, p)
        why = ", ".join(f"{n}={v}" + (f" (carried over: {s['carried'][n]})" if n in s["carried"] else "")
                        for n, v in s["reports"].items() if not (n == "legacy" and v == "missing"))
        return f"{s['state']} ({why or 'no reports'})"
    if part: return f"{folder.name}{' exercises' if part == 'exercises' else ''}: {one(part)}"
    return f"{folder.name}: {one('lesson')}; exercises: {one('exercises')}"


def published_exercises(folder):
    """Where the page takes the exercise set from: the working tree when its reviews are current; otherwise the
    newest commit whose exercise set both reviewers passed (each report's hash, or one its PASS carries over to), so
    the lesson keeps the exercises last reviewed while new ones wait for review; None when no version was reviewed."""
    s = status(folder, "exercises")
    if s["state"] == "reviewed": return WorkTree()
    passed = {}
    for name in REVIEWS:
        r = report(folder, name, "exercises")
        if r is None or r[0] != "PASS": return None
        passed[name] = {r[1]} | {c["to"] for c in carries(folder, "exercises") if c["reviewer"] == name and c["from"] == r[1]}
    log = (git("log", "--format=%H", "-n", "80", "--", courses.exercise_dir(folder).relative_to(ROOT).as_posix(), folder.relative_to(ROOT).as_posix(),
               courses.lesson_rel(folder, "answers.py"), *figure_paths(folder)) or "").split()
    for c in log:
        hs = {hash_at(c, folder, "exercises"), hash_at(c, folder, "all")}
        if all(hs & passed[n] for n in REVIEWS): return Commit(c)
    return None


def write_legacy(folder):
    s = status(folder)                               # the lesson only: an exercise set is reviewed or not shown
    if s["state"] == "reviewed": sys.exit(f"{folder.name} is reviewed by the two-review pipeline; it needs no legacy marker")
    review = folder / "review"; review.mkdir(exist_ok=True)
    (review / "legacy.md").write_text(
        f"VERDICT: PASS\nCONTENT-HASH: {s['hash']}\n\n"
        f"Prototype lesson, published before the two-review pipeline. Kept visible by the teacher's approval of the\n"
        f"migration pull request ({datetime.date.today()}). Not reviewed by the science and pedagogy reviewers: the page\n"
        f"says so. Any content change retires this marker; the lesson then returns only after both reviews pass.\n")
    print(describe(folder))


# ------------------------------------------------------------------ what changed
SVG_LINE = re.compile(r"^\s*<(/?svg|path|line|text|rect|circle|g|polyline|polygon|ellipse|defs|stop|linearGradient|radialGradient|marker|tspan|title|foreignObject|use)\b")
STYLE_ATTR = re.compile(r'\s(?:fill|stroke|stop-color|stop-opacity|color|stroke-width|stroke-dasharray|stroke-linecap|stroke-linejoin|stroke-opacity|fill-opacity|opacity|'
                        r'font-size|font-weight|font-family|font-style|class|style|rx|ry)="[^"]*"')
POS_ATTR = re.compile(r'\s(x|y|dx|dy|width|height)="(-?[\d.]+)"')
EXPERIMENT_KEY = re.compile(r'\s*"(correct|initial|locked|vary|measure|answer|unit|tolerance|value|mistakes)"\s*:')
DESIGN_KEY = re.compile(r'\s*"(id|stage|type|reveal|after|min|sections|predictions|layout|justify|version)"\s*:')
SUBSTANTIVE = re.compile(r"[0-9]|\\\\|\$|=|[A-Za-z]_|[αβγδθλμρσωΔ°·×≈≤≥]")   # a number, LaTeX, an equation, a symbol or a unit sign


def _comment(line, py):
    s = line.strip()
    return not s or (s.startswith("#") if py else s.startswith(("//", "/*", "*", "*/")))


def _svg_pair(old, new):
    """Category of one changed figure line: style, label-position or figure."""
    a, b = STYLE_ATTR.sub("", old), STYLE_ATTR.sub("", new)
    if a == b: return "style"
    if re.match(r"\s*<(text|foreignObject|tspan)\b", old) and re.match(r"\s*<(text|foreignObject|tspan)\b", new) and POS_ATTR.sub("", a) == POS_ATTR.sub("", b):
        pa, pb = dict(POS_ATTR.findall(a)), dict(POS_ATTR.findall(b))
        if pa.keys() == pb.keys() and all(abs(float(pa[k]) - float(pb[k])) <= 40 for k in pa): return "label-position"
    return "figure"


NUM = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?")
LABEL_CALL = re.compile(r"""\b(?:lab|p\.text)\(\s*(['"`])((?:(?!\1)[^\\]|\\.)*)\1""")


def _label_args(line):
    """Spans of the position arguments (the two after the text) of each canvas label call whose text is LaTeX."""
    spans = []
    for m in LABEL_CALL.finditer(line):
        if "$" not in m.group(2): continue
        i, depth, starts = m.end(), 0, []
        while i < len(line):
            c = line[i]
            if c in "([{": depth += 1
            elif c in ")]}":
                if depth == 0: break
                depth -= 1
            elif c == "," and depth == 0:
                starts.append(i)
                if len(starts) == 3: break
            i += 1
        if len(starts) >= 2: spans.append((starts[0], starts[2] if len(starts) == 3 else i))
    return spans


def _js_label_pair(old, new):
    """True when two sim.js lines differ only in numbers inside a LaTeX label's x, y arguments, each by at most 40."""
    if NUM.sub("#", old) != NUM.sub("#", new): return False
    a, b = list(NUM.finditer(old)), list(NUM.finditer(new)); spans = _label_args(old)
    changed = [(x, y) for x, y in zip(a, b) if x.group() != y.group()]
    return bool(changed) and all(abs(float(x.group()) - float(y.group())) <= 40 and any(s <= x.start() < e for s, e in spans) for x, y in changed)


def _line(fname, body, lid):
    """Category of one added or removed line that is not a figure line."""
    s = body.lstrip()
    if fname == "exercises.json":
        if s.startswith(('"answer"', '"unit"', '"tolerance"')): return "answers"
        if s.startswith(('"level"', '"id"')): return "levels"
    if fname == "inquiry.json":
        if EXPERIMENT_KEY.match(body): return "experiment"
        if DESIGN_KEY.match(body): return "structure"
    if fname == "meta.json":
        if s.startswith('"sim"'): return "simulation"
        if s.startswith(('"title"', '"glossary"')): return "wording"
        if s.startswith(('"image"', '"solutions"')): return "structure"
        if s.strip() in ("{", "}", "[", "]", "],", ""): return "comments"
        return "objectives"
    if fname.endswith(".md") and s.startswith("# "): return "wording"      # the page title, the same as meta.json "title"
    if fname.endswith(".md") and (s.startswith("## ") or "<!-- vaihe -->" in body or s.startswith("```")): return "structure"
    return "numbers" if SUBSTANTIVE.search(body) else "wording"


HERO = re.compile(r'\n*<svg\b[^>]*data-fig="(?:hero|scene)".*?</svg>\n*', re.S)


def strip_hero(text):
    """lesson.md without its illustrations (`<svg data-fig="hero">` and `"scene"`, NOTES §3) when they have no label:
    such a picture carries no text or physics claim, so changing it is the category "illustration" alone."""
    if not text: return text
    out = re.sub(r"\n{3,}", "\n\n", HERO.sub(lambda m: "\n\n" if not re.search(r"<(foreignObject|text)\b", m.group(0)) else m.group(0), text))
    return out.rstrip("\n") + "\n" if text.endswith("\n") else out.rstrip("\n")       # a picture at the end leaves no blank line


CHAPTER_REF = re.compile(r"\b((?:luku|luvussa|luvusta|luvun|luvuissa|chapter|chapters)\s+)\*([^*]+)\*", re.I)


@functools.lru_cache(maxsize=None)
def chapter_titles():
    """Every current lesson title in every language (meta.json)."""
    return frozenset(json.loads(f.read_text()).get("title", "") for f in (ROOT / "content").glob("*/*/*/meta.json"))


def _chapter_refs_renamed(old, new):
    """True when two lines differ only in the titles of chapter references and every new one is a current title."""
    blank = lambda l: CHAPTER_REF.sub(lambda m: m.group(1) + "*…*", l)
    if blank(old) != blank(new): return False
    return all(m.group(2) in chapter_titles() for m in CHAPTER_REF.finditer(new))


def classify(path, diff_lines, lid):
    """Categories of one file's unified diff (its +/- lines)."""
    if path.startswith(("figure:", "a/figure:", "b/figure:")): return {"figure"}   # a referenced figure's drawing code
    name = path.split("/")[-1]
    py, code = name.endswith(".py"), name.endswith(".js")
    binary = name.lower().endswith(courses.BINARY)
    in_sim = "/sims/" in f"/{path}" and not path.startswith("tests/")
    if binary: return {"simulation" if in_sim else "figure"}
    if in_sim and name.endswith(".css"): return {"style"}
    cats, block = set(), []
    def flush():
        rem = [l[1:] for l in block if l.startswith("-")]; add = [l[1:] for l in block if l.startswith("+")]
        if name == "lesson.md":                        # `## Kaava` → `## Kaava: Lämpömäärä`: the same section, now named
            for o in [l for l in rem if l.startswith("## ")]:
                n = next((l for l in add if l.startswith("## ") and inquiry.heading(l[3:])[0] == inquiry.heading(o[3:])[0] and l != o), None)
                if n is not None: cats.add("section-name"); rem.remove(o); add.remove(n)
        if not (code or py):                           # "(luku *Tasainen liike: s = vt*)" → the chapter's current title
            for o in list(rem):
                n = next((l for l in add if l != o and _chapter_refs_renamed(o, l)), None)
                if n is not None: cats.add("chapter-ref"); rem.remove(o); add.remove(n)
        if code and len(rem) == len(add) and rem and all(_js_label_pair(o, n) for o, n in zip(rem, add)):
            cats.add("label-position"); return       # a canvas label moved, its text unchanged: check_layout and test_sims see it
        if code or py:
            for l in rem + add: cats.add("comments" if _comment(l, py) else "answers" if py else "simulation")
            return
        svg_r = [l for l in rem if SVG_LINE.match(l)]; svg_a = [l for l in add if SVG_LINE.match(l)]
        if svg_r or svg_a:
            if len(svg_r) == len(svg_a): cats.update(_svg_pair(o, n) for o, n in zip(svg_r, svg_a))
            else: cats.add("figure")
        for l in rem + add:
            if not SVG_LINE.match(l): cats.add(_line(name, l, lid))
    for l in diff_lines:
        if l.startswith(("+++", "---")): continue
        if l.startswith(("+", "-")): block.append(l)
        else:
            if block: flush()
            block = []
    if block: flush()
    return cats


SIM_TEXT = ("text",) + tuple(k for k, _ in inquiry.SIM_INFO)


def _sentences(s): return sorted(x for x in re.split(r"(?<=[.!?])\s+", " ".join(s.split())) if x)


def relocated(old, new):
    """The old inquiry.json with each sim activity replaced by its new version where only its text moved, word for
    word, between the visible lead and the boxes (text, howto, model, calc); None when nothing moved that way."""
    try: o, n = json.loads(old), json.loads(new)
    except (json.JSONDecodeError, TypeError): return None
    new_acts = {a.get("id"): a for a in n.get("activities", []) if isinstance(a, dict)}
    rest = lambda a: {k: v for k, v in a.items() if k not in SIM_TEXT}
    words = lambda a: _sentences(" ".join(a.get(k) or "" for k in SIM_TEXT))
    moved = False
    for i, a in enumerate(o.get("activities", [])):
        b = new_acts.get(a.get("id")) if isinstance(a, dict) else None
        if b and a != b and a.get("type") == b.get("type") == "sim" and rest(a) == rest(b) and words(a) == words(b):
            o["activities"][i] = b; moved = True
    return json.dumps(o, ensure_ascii=False) if moved else None


def _math_and_numbers(s):
    """The formulas ($…$) and the numbers of a text, in order: what a grammatical rephrasing must keep."""
    return re.findall(r"\$[^$]*\$", s), re.findall(r"\d+(?:[.,]\d+)?", re.sub(r"\$[^$]*\$", " ", s))


def objective_form(old, new):
    """The old inquiry.json with `learn` replaced by the new one when only the goals' wording changed (the same
    number of goals, each keeping its formulas and numbers: "Osaat laskea … $P = E : t$" → "laskemaan … $P = E : t$");
    None otherwise. The grammar itself is checked by scripts/objectives.py, the meaning by the pedagogy reviewer."""
    try: o, n = json.loads(old), json.loads(new)
    except (json.JSONDecodeError, TypeError): return None
    a, b = o.get("learn"), n.get("learn")
    if not (isinstance(a, list) and isinstance(b, list)) or a == b or len(a) != len(b): return None
    if not all(isinstance(x, str) and isinstance(y, str) and _math_and_numbers(x) == _math_and_numbers(y) for x, y in zip(a, b)): return None
    o["learn"] = b
    return json.dumps(o, ensure_ascii=False)


def test_change(rel, base):
    """'tests' when every assertion of the base version is still there, as strict; 'tests-weakened' otherwise."""
    try:
        old = json.loads(git("show", f"{base}:./{rel}") or "[]"); new = json.loads((ROOT / rel).read_text()) if (ROOT / rel).exists() else []
    except json.JSONDecodeError: return "tests-weakened"
    key = lambda a: (a.get("expr"), a.get("setup", ""))
    now = {key(a): a for a in new}
    for a in old:
        b = now.get(key(a))
        if b is None or b.get("expected") != a.get("expected") or b.get("tol", 0.01) > a.get("tol", 0.01): return "tests-weakened"
    return "tests"


def _view(data, rel, binary):
    """What a diff compares: the same normalisation as the hash (JSON one key per line in the author's key order)."""
    if data is None: return None
    if binary: return hashlib.sha256(data).hexdigest()
    if rel.endswith(".json"):
        try: return json.dumps(json.loads(data), indent=1, ensure_ascii=False)
        except json.JSONDecodeError: return data
    return normalized(data, rel)


ANSWERS = ("answers.py", "lesson-answers.py")


def _code_lines(text):
    """The lines of an answers file that compute something: no module docstring, comment or blank line."""
    out, doc = [], None
    for i, l in enumerate(text.splitlines()):
        s = l.strip()
        if doc is None and s and not s.startswith("#"):
            doc = s[:3] if s.startswith(('"""', "'''")) else ""
            if doc and (s.count(doc) >= 2 and len(s) > 3): doc = ""; continue
            if doc: continue
        elif doc:
            if doc in s: doc = ""
            continue
        if s and not s.startswith("#"): out.append(l.rstrip())
    return out


def _run_answers(text):
    """{id: value} that an answers file prints, or None when it does not run."""
    with tempfile.TemporaryDirectory() as d:
        f = pathlib.Path(d) / "answers.py"; f.write_text(text)
        r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True, cwd=d, timeout=60)
    try: return json.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else None
    except (json.JSONDecodeError, IndexError): return None


def split_from(old, new):
    """True when `new` is a part of the answers file `old` taken line for line (answers.py and lesson-answers.py when
    the exercises got their own folder, 2026-10-28): every line that computes something is a line of the old file,
    and every value it prints is the value the old file printed for that id. Comments and the docstring may differ."""
    if not old or not new: return False
    have = {l.rstrip() for l in old.splitlines()}
    if not all(l in have for l in _code_lines(new)): return False
    a, b = _run_answers(old), _run_answers(new)
    return a is not None and bool(b) and all(k in a and a[k] == v for k, v in b.items())


def changes(folder, base, part="lesson", split=False):
    """(categories, unified diff, changed line count) of `part` between commit `base` and the working tree, over every
    source its hash covers, as the base saw them and as they are now. Formatting the hash ignores is not a change here
    either. `split`: the base's PASS was on the one hash before the split, so the category "split" applies, and when
    the base still had one answers.py for both parts, each part's answers file is compared with that file."""
    old, new = Commit(base), WorkTree()
    paths = sorted({(rel, b) for _, rel, b in entries(folder, old, part) + entries(folder, new, part)})
    cats, diff, n = ({"split"} if split else set()), [], 0
    before_split = split and not old.files(courses.exercise_dir(folder).relative_to(ROOT).as_posix())
    for rel, binary in paths:
        ra, rb = old.source(rel, binary), new.source(rel, binary)
        if before_split and rel.split("/")[-1] in ANSWERS:     # one answers.py then: this part's file is cut from it
            ra = old.source(courses.lesson_rel(folder, "answers.py"))
            if rb is None and rel.endswith("/lesson-answers.py"): continue   # nothing of the lesson's own was in it
            if ra != rb and split_from(ra, rb): diff.append(f"--- {rel}: taken line for line from answers.py"); continue
        a, b = _view(ra, rel, binary), _view(rb, rel, binary)
        if a == b: continue
        if rel.startswith("tests/sims/"): cats.add(test_change(rel, base)); diff.append(f"--- {rel}: simulation assertions changed"); continue
        if binary: cats.add("simulation" if "/sims/" in f"/{rel}" else "figure"); diff.append(f"--- {rel}: binary file {'added' if a is None else 'removed' if b is None else 'changed'}"); continue
        lines = list(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), f"a/{rel}", f"b/{rel}", lineterm="", n=2))
        if rel.endswith("/lesson.md") and (strip_hero(a), strip_hero(b)) != (a, b):   # a label-free opening illustration
            a2, b2 = strip_hero(a), strip_hero(b)
            if HERO.findall(a or "") != HERO.findall(b or ""): cats.add("illustration")
            if a2 != b2: cats |= classify(rel, list(difflib.unified_diff((a2 or "").splitlines(), (b2 or "").splitlines(), lineterm="", n=2)), folder.name)
            n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        goals = objective_form(ra, rb) if rel.endswith("inquiry.json") and ra and rb else None
        if goals is not None:                          # the goals rephrased; whatever else changed is classified as usual
            cats.add("objective-form"); ra = goals; a = _view(ra, rel, False)
            if a == b: n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        moved = relocated(ra, rb) if rel.endswith("inquiry.json") and ra and rb else None
        if moved is not None:                          # the moved text is "relocated"; whatever else changed is classified as usual
            cats.add("relocated"); a2 = _view(moved, rel, False)
            cats |= classify(rel, list(difflib.unified_diff(a2.splitlines(), b.splitlines(), lineterm="", n=2)), folder.name) if a2 != b else set()
        elif goals is not None: cats |= classify(rel, list(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=2)), folder.name)
        else: cats |= classify(rel, lines, folder.name)
        n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---")))
        diff += lines
    return cats, "\n".join(diff), n


def passed_at(log, folder, part, h):
    """(commit, split) of the newest commit in `log` whose `part` has hash h, or whose one hash before the split was h
    (split True); (None, False) when none has."""
    for c in log:
        if hash_at(c, folder, part) == h: return c, False
        if hash_at(c, folder, "all") == h: return c, True
    return None, False


def scope(folder, part="lesson"):
    """For each reviewer of `part`: {'mode': none|delta|full, 'base': commit|None, 'why': ..., 'diff': ..., 'categories': [...]}."""
    lid = folder.name; legacy = f"content/{folder.parent.name}/{lid}"     # the folder before the languages (Commit.read)
    log = (git("log", "--format=%H", "-n", "80", "--", folder.relative_to(ROOT).as_posix(), courses.code_dir(folder).relative_to(ROOT).as_posix(),
               legacy, f"tests/sims/{lid}.json", "assets", f"lang/{courses.lang_of(folder)}.json", *figure_paths(folder)) or "").split()
    out, cache = {}, {}
    for name in REVIEWS:
        rep = report(folder, name, part)
        if rep is None or rep[0] != "PASS": out[name] = {"mode": "full", "base": None, "why": "no earlier PASS", "diff": "", "categories": []}; continue
        if rep[1] == content_hash(folder, part):
            out[name] = {"mode": "delta", "base": None, "why": "0 changed wording line(s): the version it passed", "diff": "", "categories": []}; continue
        base, split = passed_at(log, folder, part, rep[1])
        if base is None: out[name] = {"mode": "full", "base": None, "why": "the version it passed is not in git history", "diff": "", "categories": []}; continue
        if (base, split) not in cache: cache[base, split] = changes(folder, base, part, split)
        cats, diff, n = cache[base, split]
        i = REVIEWS.index(name)
        mode = max((RULES[c][i] for c in cats), key=MODES.index, default="delta")
        strict = sorted(c for c in cats if RULES[c][i] == mode)
        why = "; ".join(WHY[c] for c in strict) if strict else f"{n} changed line(s)"
        out[name] = {"mode": mode, "base": base, "why": why, "diff": diff, "categories": sorted(cats)}
    return out


def print_scope(folder, part="lesson"):
    sc = scope(folder, part)
    for name, v in sc.items():
        print(f"{name}: {v['mode']} ({v['why']})" + (f" base={v['base'][:7]}" if v["base"] else "") + (f" categories={','.join(v['categories'])}" if v["categories"] else ""))
    return sc


def carry(folder, part="lesson"):
    """Write review/carry.tsv rows for every reviewer whose mode is none (its PASS holds for the current hash)."""
    sc, h, rows = scope(folder, part), content_hash(folder, part), carries(folder, part)
    f = review_dir(folder, part) / "carry.tsv"; added = []
    for name in REVIEWS:
        rep = report(folder, name, part)
        if sc[name]["mode"] != "none" or rep is None or rep[1] == h or carried(folder, name, rep[1], h, part): continue
        rows.append({"date": str(datetime.date.today()), "reviewer": name, "from": rep[1], "to": h, "base": sc[name]["base"][:12],
                     "categories": ",".join(sc[name]["categories"])}); added.append(name)
    if added:
        f.parent.mkdir(exist_ok=True)
        f.write_text("\t".join(CARRY_COLS) + "\n" + "".join("\t".join(r[c] for c in CARRY_COLS) + "\n" for r in rows))
    for name in REVIEWS: print(f"{name}: {'carried over (' + sc[name]['why'] + ')' if name in added else sc[name]['mode'] + ' review needed' if sc[name]['mode'] != 'none' else 'already current'}")
    print(describe(folder, part))


def verify_carries(folder, part="lesson"):
    """Errors for carry rows in use: the change since the base must still be one this reviewer need not see."""
    errs, h, what = [], content_hash(folder, part), folder.name + (" exercises" if part == "exercises" else "")
    for name in REVIEWS:
        rep = report(folder, name, part)
        c = carried(folder, name, rep[1], h, part) if rep and rep[1] != h else None
        if not c: continue
        if git("rev-parse", "--verify", "-q", f"{c['base']}^{{commit}}") is None:
            errs.append(f"{what}: carry of {name} names commit {c['base']}, not in history (CI needs fetch-depth: 0)"); continue
        split = hash_at(c["base"], folder, part) != c["from"]
        if split and hash_at(c["base"], folder, "all") != c["from"]: errs.append(f"{what}: carry of {name}: commit {c['base']} does not hold hash {c['from']}"); continue
        cats, _, _ = changes(folder, c["base"], part, split)
        i = REVIEWS.index(name)
        bad = [x for x in cats if RULES[x][i] != "none"]
        if bad: errs.append(f"{what}: carry of {name} covers changes it must review: {', '.join(WHY[x] for x in bad)}")
    return errs


def impact(ref):
    """Which lessons the files changed since `ref` touch, and the review each needs."""
    top = (git("rev-parse", "--show-prefix") or "").strip()
    names = set((git("diff", "--name-only", ref) or "").split()) | set((git("ls-files", "--others", "--exclude-standard") or "").split())
    names = {n[len(top):] if top and n.startswith(top) else n for n in names}
    deps, lessons, tooling, exercises = courses.deps(), set(), [], set()
    for n in sorted(names):
        if n.endswith((".gitkeep", "README.md")) and n.startswith("assets/"): continue
        m = re.match(r"(?:content/[a-z]{2,3}(?:-[a-z]+)?/[^/]+|lessons/[^/]+)/([^/]+)/", n)
        if m and "/review/" not in n:
            if "/exercises/" in n or n.endswith("/answers.py"): exercises.add(m.group(1))
            else: lessons.add(m.group(1))
            continue
        if re.fullmatch(r"lang/[a-z]{2,3}(?:-[a-z]+)?\.json", n):           # a simulation's texts: the lessons whose simulation block changed
            old, new = (git("show", f"{ref}:./{n}") or "{}"), ((ROOT / n).read_text() if (ROOT / n).exists() else "{}")
            sims = lambda t: json.loads(t).get("sims", {})
            for key in sorted(set(sims(old)) | set(sims(new))):
                if sims(old).get(key) != sims(new).get(key):
                    users = [key] if any(f.name == key for f in courses.lessons()) else deps.get(next((d for d in deps if d.endswith(f"/{key}")), ""), [])
                    lessons |= set(users); print(f"{n} sims.{key}: used by {', '.join(users) or 'no lesson yet'}")
            tooling.append(n); continue
        m = re.match(r"tests/sims/([^/]+)\.json$", n)
        if m: lessons.add(m.group(1)); continue
        m = re.match(r"assets/((?:sims/[^/]+|shared/sims)/[^/]+)/", n) or re.match(r"assets/((?:pics/[^/]+|shared/pics)/[^/]+)$", n)
        if m:
            users = deps.get(m.group(1), [])
            lessons |= set(users); exercises |= set(users) if m.group(1).startswith(("pics/", "shared/pics/")) else set()   # a picture may be in either part
            print(f"{n}: used by {', '.join(users) or 'no lesson yet'}"); continue
        if n.startswith(("scripts/", "templates/", "curriculum.json", "competencies.json", "glossary.json", ".claude/", "docs/", "site/")) or n.endswith((".md", ".yml")):
            tooling.append(n)
    if tooling: print(f"tooling, templates, config or docs ({len(tooling)} file(s)): no review; CI re-runs every check and rebuilds every page")
    for lid in sorted(lessons | exercises):
        folder = next((f for f in courses.lessons() if f.name == lid), None)
        if folder is None: print(f"{lid}: removed or not a lesson"); continue
        for part in [p for p, ids in (("lesson", lessons), ("exercises", exercises)) if lid in ids]:
            sc = scope(folder, part)
            print(f"{lid}{' exercises' if part == 'exercises' else ''}: " + "; ".join(f"{n} {v['mode']} ({v['why']})" for n, v in sc.items()))
    if not lessons and not exercises and not tooling: print(f"nothing changed since {ref}")


if __name__ == "__main__":
    a = sys.argv[1:]
    part = "exercises" if "--exercises" in a else "lesson"; a = [x for x in a if x != "--exercises"]
    if "--lang" in a:                                   # a translation: content/<lang>/<COURSE>/<id>/ (README "Languages")
        i = a.index("--lang"); LANG = a[i + 1]; del a[i:i + 2]
        find_lesson = lambda lid: courses.find_lesson(lid, LANG)
    if not a: sys.exit(__doc__)
    if a[0] == "hash": print(content_hash(find_lesson(a[1]), part))
    elif a[0] == "status": print("\n".join(describe(f) for f in ([find_lesson(a[1])] if len(a) > 1 else courses.lessons())))
    elif a[0] == "legacy": write_legacy(find_lesson(a[1]))
    elif a[0] == "scope": print_scope(find_lesson(a[1]), part)
    elif a[0] == "carry": carry(find_lesson(a[1]), part)
    elif a[0] == "impact": impact(a[1] if len(a) > 1 else "origin/main")
    elif a[0] == "verify":
        bad = 0
        for f in [f for lang in i18n.languages() for f in courses.lessons(lang=lang)]:
            try: print(describe(f))
            except ValueError as e: print("ERROR", e); bad += 1; continue
            for p in ("lesson", "exercises"):
                for e in verify_carries(f, p): print("ERROR", e); bad += 1
        sys.exit(1 if bad else 0)
    else: sys.exit(__doc__)
