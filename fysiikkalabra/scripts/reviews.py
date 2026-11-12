"""Review state of a lesson and of its exercise set: one content hash each, three reviews each, no status fields.

  python scripts/reviews.py hash <id> [--exercises] [--lang en]   the content hash (reviewers put it in their report)
  python scripts/reviews.py status [<id>]              reviewed | legacy | draft of the lesson and its exercises
  python scripts/reviews.py legacy <id>                write review/legacy.md: prototype content the teacher keeps visible
  python scripts/reviews.py scope <id> [--exercises]   per reviewer: none, delta or full, from what changed since its PASS
  python scripts/reviews.py carry <id> [--exercises]   record that a reviewer's PASS carries over a change it need not see
  python scripts/reviews.py approve-figures <id> …     record that the teacher approved the lesson's figures as drawn now
  python scripts/reviews.py carry-item investigation|sovella|koe|unit|guide <id> [--lang en]
                                             the same carry for an investigation, a unit or a TVT guide (its id), a
                                             Sovella set or an example exam (the course, FY4): only over figures the
                                             teacher approved as drawn
  python scripts/reviews.py approve-presentation <sim.js> [<base-ref>]   show a simulation file's change since <base-ref>
                                             (default origin/main) and, when it only places or draws, record it for the
                                             teacher's approval (docs/presentation-only.tsv)
  python scripts/reviews.py impact [<ref>]   which lessons a change since <ref> (default origin/main) touches, and
                                             which review each needs; shared simulations count for every user
  python scripts/reviews.py verify           CI: every lesson's state; exit 1 on a malformed report or an invalid carry
                                             or a visual baseline row that was added after the baseline was written
  python scripts/reviews.py baseline         what still awaits its first visual review (the visual baseline, below)
  python scripts/reviews.py baseline init    write docs/visual-baseline.tsv once, from what both reviewers passed

Three independent reviewers (teacher's brief 2026-10-31): science (physics and mathematics), pedagogy (learning) and
visual (visual & editorial: figures, graphs, mathematical typography, Finnish, presentation; `.claude/agents/
visual-editorial-reviewer.md`, `docs/EDITORIAL_QUALITY_STANDARD.md`). Each writes review/<name>.md for the same hash.

The visual gate and its baseline. Publication needs all three PASS reports once VISUAL_GATE is on. Content that
both other reviewers had passed when the gate was switched on was never seen by a visual reviewer, and requiring a
visual PASS of it at once would empty the site, while writing PASS reports for it would claim a review nobody made.
So `baseline init` wrote one row per such part (kind, language, id, part, the content hash it had) into
docs/visual-baseline.tsv; a row stands in for the visual PASS of exactly that hash. It is no review: `status`
says "visual baseline", `baseline` lists every part still on it, and a visual FAIL report (an audit) leaves the
row in force, so auditing never unpublishes. When the content changes, the row no longer matches: a change the
visual reviewer need not see (tests, comments, a translation's copied force diagrams, …; RULES' third column
`none`) is carried over by a carry row from the baseline hash like any carry, checked by `verify`; any other
change needs a genuine visual PASS, in full, since the rest of the part was never visually reviewed. Rows are only
ever removed: `verify` fails on a row that the file's first commit did not have. The exercise set's fallback
(published_exercises) treats a baseline hash as the visual PASS of that version, so unreviewed exercise edits never
replace the exercises published before. Investigations, TVT guides, units, Sovella sets and example exams
(`item_status`) have one carry only: over figures the teacher approved as drawn (`carry-item`, teacher 2026-11-11);
otherwise a report or a baseline row counts for its exact hash only.

Two parts are reviewed apart (teacher 2026-10-28, README "Exercises"): the *lesson* (its texts, simulation, figures
and lesson-answers.py, reports in review/) and its *exercises* (exercises/exercises.json, exercises/solutions.md and
answers.py, reports in exercises/review/), so writing exercises never stales the lesson's reviews and the lesson
never stales theirs. Everything below holds for each part with its own files, hash and reports; `--exercises`
picks the exercise set. Before the split one hash covered both (PARTS "all"); a PASS on such a hash still counts
when the commit that holds it has the same files as now, moved but unchanged (category "split", below).

A part is *reviewed* when review/science.md, review/pedagogy.md and review/visual.md all start with `VERDICT: PASS`
and carry the current CONTENT-HASH, or a hash whose PASS carries over to the current one (below); the visual one
may be the visual baseline (above). It is *legacy* when
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

Added exercises (teacher 2026-11-12). When the only change to an exercise set since a reviewer's PASS is that whole
exercises were added, or an exercise was replaced by a new one (its id removed and another added, or the same id with
its text and its solution rewritten), the category is "added-exercise" alone and all three reviewers review a delta
(`added_exercises`): every exercise present in both versions is identical in exercises.json (same level, same order
among the others, same core mark) and in its solutions.md section, solutions.md has nothing else changed, answers.py
prints the same value for every id but the added and removed ones, and every other changed source belongs to the
added exercises only (the drawing code of a figure no surviving exercise refers to, a translation's figure words only
added, a picture no surviving exercise shows). Anything else, or anything that cannot be read, falls back to the
classification above. The delta packet gives each reviewer the added and removed exercises in full and a list of the
whole set; its PASS names what it covered on line 3 (`SCOPE: delta added-exercise from <hash> base <commit>`), and
`verify` re-derives that claim from git history (`verify_scopes`). Content still on the visual baseline gets its
first visual review in full as before.

Translated exercise sets (teacher 2026-11-12). The physics, numbers, answers, units and tolerances of an exercise set are
the same in every language, so the science review of a translation (content/en/, content/fi-easy/; `--exercises --lang`)
carries over from the Finnish set's: `scope` gives the science reviewer mode `none`, category "translation-of-passed",
when (1) the Finnish exercise set has a science PASS (its own, or carried over) for its current hash, (2) the
translation's own science report is no verdict on its current hash (a PASS needs nothing; a FAIL is never overridden),
and (3) the translation is numerically equivalent to the Finnish set (`translation_differs` is None): the same exercise
ids in the same levels and order, the same core exercises; in every exercise the same keys and list lengths, identical
id, level, kind, core, unit, tolerance, figure, lookup, correct and true marks (choices, statements, order and reasons by
position) and every other non-text value (a numeric answer, a data table's numbers); in every text (a text answer, an
option, a hint, a caption, every solutions.md section and its preamble, the same section ids in the same order) the same
formulas in the same order (check_i18n.formula_spans; whitespace dropped, `{,}` read as `.`, \text{} words kept except a
sub- or superscript label such as E_\text{sähkö} → E_\text{elec}, which must be translated one to one across the set),
the same figures and force-diagram specs, the same numbers outside the formulas, and in an option's text the same capital-letter
labels in order; the same pictures; and every entry of the translation's figures.json keeping its Finnish numbers and
formulas. answers.py and the figures' code are shared. Anything else means the usual scope. `carry` then writes the
row (reviewer science, from the Finnish hash, to the translation's hash, base `-`), `status` counts it while both
hashes are current and the Finnish science PASS holds, and `verify` re-derives the equivalence of every row in use. When
the Finnish set changes, its hash no longer matches the row: the translation's science is stale (the page keeps the
version last reviewed, published_exercises) until a new carry or a review. Pedagogy and visual review each language.
"""
import collections, datetime, difflib, functools, hashlib, html, json, os, pathlib, re, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, figcat, figlib, i18n, inquiry, kaavat

ROOT = courses.ROOT
REVIEWS = ("science", "pedagogy", "visual")      # the three independent reviewers (visual & editorial since 2026-10-31)
VISUAL = "visual"
VISUAL_GATE = True    # the activation switch of the third mandatory review (teacher's brief 2026-10-31, module docstring)
BASELINE = ROOT / "docs" / "visual-baseline.tsv"   # what was published before the gate: hash-bound, rows only ever removed
BASELINE_COLS = ["kind", "lang", "id", "part", "hash", "date"]
PRESENTATION = ROOT / "docs" / "presentation-only.tsv"      # simulation changes that only place or draw, approved diff by diff (teacher 2026-11-11)
TEACHER_FIGURES = ROOT / "docs" / "teacher-figures.tsv"   # figures the teacher approved as drawn (teacher 2026-11-10)
CONTENT = ("meta.json", "lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim.js", "sim-spec.md", "inquiry.json")
EXERCISE_CONTENT = ("exercises.json", "solutions.md", "answers.py")
LESSON_CONTENT = tuple(n for n in CONTENT if n not in EXERCISE_CONTENT) + ("lesson-answers.py",)
PARTS = {"lesson": LESSON_CONTENT, "exercises": EXERCISE_CONTENT,
         "all": CONTENT}            # the one hash of a lesson before the exercises got their own reviews (2026-10-28)
MODES = ("none", "delta", "full")
FBD_SPEC = re.compile(r"(?:\n|\\n)```voimakuvio(?:\n|\\n).*?```", re.S)   # a drawn force diagram's spec (scripts/fbdspec.py), raw or in JSON
RULES = {                       # category: (science, pedagogy, visual)
    "typography":     ("none",  "none", "delta"),   # a formula re-set without a change of meaning (spacing, \\dfrac/\\frac, {,}, \\left/\\right): the visual reviewer looks
    "tests":          ("none",  "none", "none"),    # tests/sims assertions added or tightened: test_sims.py checks them
    "comments":       ("none",  "none", "none"),    # comment or blank lines in simulation code or answers.py
    "style":          ("none",  "delta", "delta"),   # colours, strokes, fonts, classes in a figure; a simulation's sim.css
    "label-position": ("none",  "delta", "delta"),   # a figure label moved by at most 40 units, its text unchanged
    "relocated":      ("none",  "delta", "delta"),   # the sim activity's text moved word for word into its lead and boxes (inquiry.json)
    "objective-form": ("none",  "delta", "delta"),
    "notation":       ("none",  "none", "delta"),    # a vector symbol rewritten \\mathbf{F} / \\vec{F} → \\overline{F}, nothing else (teacher 2026-10-29)
    "force-diagram":  ("delta", "none", "delta"),    # a ```voimakuvio spec added to a step, drawn by fbdspec.py; the text unchanged (teacher 2026-10-30)
    "force-diagram-copy": ("none", "none", "none"),  # a translation's force-diagram specs, identical to the reviewed Finnish ones (check_i18n.py)
    "level-policy":   ("none",  "none", "none"),    # the chapter's own "Taso 1 riittää …" sentence deleted, nothing else: the template says which exercises are core (teacher 2026-10-31)
    "chapter-ref":    ("none",  "none", "none"),    # a reference "(luku *<title>*)" follows a chapter's new title, which is a current title (teacher 2026-10-29)   # a learning goal (inquiry.json learn) rephrased to complete "Tällä tunnilla opit", same symbols and numbers (teacher 2026-10-29)
    "section-name":   ("delta", "delta", "delta"),   # a section heading given or changed its name, key unchanged (## Kaava: Lämpömäärä)
    "wording":        ("delta", "delta", "delta"),   # prose without a number, formula, symbol or unit
    "numbers":        ("full",  "delta", "delta"),   # a changed line carries a number, formula, symbol or unit
    "answers":        ("full",  "delta", "none"),   # an exercise answer, unit or tolerance; answers.py code
    "tests-weakened": ("full",  "none", "none"),    # a simulation assertion removed or loosened
    "levels":         ("delta", "full", "delta"),    # an exercise's level or id
    "structure":      ("delta", "full", "delta"),    # headings, stages, display blocks; inquiry stage, type, reveal, sections
    "objectives":     ("delta", "full", "delta"),    # meta goals or prerequisites
    "experiment":     ("full",  "full", "delta"),    # inquiry correct option, initial/locked/vary/measure, numeric answer, mistakes
    "simulation":     ("full",  "full", "delta"),    # simulation code or images (the lesson's or a shared folder it uses)
    "figure":         ("full",  "full", "delta"),    # figure geometry or text; a picture file
    "photo":          ("none",  "none", "delta"),    # a licensed photograph beside the text (figure.unit-photo, assets/pics/<course>/photos.json): illustration only, never a task (teacher 2026-11-01 FY14, 2026-11-03 FY1–FY3)
    "illustration":   ("none",  "delta", "delta"),   # an illustration (data-fig="hero" or "scene"): no text, no physics claim (teacher 2026-10-26)
    "core-mark":      ("none",  "none", "none"),    # an exercise or lesson activity marked core (`"core": true`) or unmarked, nothing else: the module's core path as a whole is reviewed in docs/core-path/ (teacher 2026-11-05)
    "paragraphs":     ("none",  "none", "none"),    # a task text cut into paragraphs (a blank line, "\\n\\n" in the JSON string), its words unchanged: build.exercise_text renders them, check_layout checks them (teacher 2026-11-04)
    "presentation-only": ("none", "none", "delta"),  # a simulation's code changed only in where or how it draws (an axis name, a label's place), the exact change approved in docs/presentation-only.tsv: the visual reviewer looks, test_sims.py runs
    "formula-names": ("none",  "none", "none"),    # FY9 formulas given the names of docs/fy9/kaavanimet.tsv (```kaavat), nothing else changed (teacher 2026-11-12)
    "teacher-figure": ("none",  "none", "none"),    # a figure the teacher approved as drawn (docs/teacher-figures.tsv, its exact Finnish SVG), its words in a translation, a task given it by "figure": the layout is check_layout's (teacher 2026-11-10)
    "split":          ("none",  "none", "none"),    # passed as one lesson before the split; this part's files moved, unchanged (answers.py: line for line)
    "figure-words-added": ("none", "none", "none"),   # a translation's figures.json only gained entries (a new figure variant for a task); every existing entry as it was (teacher 2026-11-12)
    "added-exercise": ("delta", "delta", "delta"),   # whole exercises added or replaced, every other exercise of the set as it was passed (added_exercises; teacher 2026-11-12)
}
WHY = {"core-mark": "exercises or activities marked core or unmarked, nothing else", "paragraphs": "a task text cut into paragraphs, its words unchanged", "photo": "a licensed illustration photograph added, moved or recaptioned", "typography": "formulas re-set (spacing, fraction style, decimal comma) or a symbol set as maths, or blank lines, without a change of meaning", "tests": "simulation tests added or tightened", "comments": "comments only", "style": "figure or sim styling only",
       "label-position": "a figure label nudged, text unchanged", "wording": "wording without numbers or symbols",
       "relocated": "the sim's text moved word for word into its lead and boxes",
       "chapter-ref": "a chapter reference follows that chapter's new title",
       "level-policy": "the chapter's own level-policy sentence (\"Taso 1 riittää …\") deleted, nothing else",
       "notation": "vector symbols rewritten with an overline, nothing else",
       "force-diagram-copy": "the Finnish force-diagram specs copied unchanged into the translation",
       "force-diagram": "force diagrams drawn from a spec beside their Voimakuvio steps (fbdspec.py), the text unchanged",
       "objective-form": "learning goals rephrased to complete their heading, symbols and numbers unchanged", "section-name": "a section named after its law",
       "numbers": "a changed line carries a number, formula, symbol or unit", "answers": "an answer, unit, tolerance or answers.py changed",
       "tests-weakened": "a simulation assertion removed or loosened", "levels": "an exercise level or id changed",
       "structure": "headings, stages, display blocks or inquiry structure changed", "objectives": "meta goals or prerequisites changed",
       "experiment": "an experiment setup, correct option or numeric answer in inquiry.json changed",
       "simulation": "the simulation's code changed", "figure": "a figure or picture changed",
       "illustration": "the illustrations only",
       "teacher-figure": "figures the teacher approved as drawn (docs/teacher-figures.tsv)",
       "formula-names": "formula names the teacher approved (docs/fy9/kaavanimet.tsv)",
       "presentation-only": "a simulation's drawing only, the change approved in docs/presentation-only.tsv",
       "split": "the exercises moved to their own folder, every file as it was passed (answers.py split line for line)",
       "figure-words-added": "the translation's figures.json only gained entries for a new figure (every existing entry unchanged)",
       "added-exercise": "whole exercises added or replaced, every other exercise of the set unchanged",
       "translation-of-passed": "a translation of the Finnish exercise set, its numbers, answers and formulas the same: the Finnish set's science PASS for its current hash carries over (teacher 2026-11-12)"}
# Not a RULES category: "translation-of-passed" is never found by `changes`; `scope` grants it to the science reviewer of a
# translated exercise set alone (module docstring, "Translated exercise sets"); pedagogy and visual review each language.


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


# ------------------------------------------------------------------ the visual baseline (teacher's brief 2026-10-31)
_baseline_cache = {}


def baseline_rows():
    """The rows of docs/visual-baseline.tsv: content that both reviewers had passed when the visual review became
    mandatory, each bound to the content hash it had then. Written once by `reviews.py baseline init`."""
    if not BASELINE.is_file(): return []
    key = BASELINE.stat().st_mtime_ns
    if key not in _baseline_cache:
        lines = [l for l in BASELINE.read_text().splitlines() if l.strip() and not l.startswith("#")]
        _baseline_cache.clear(); _baseline_cache[key] = [dict(zip(BASELINE_COLS, l.split("\t"))) for l in lines[1:]]
    return _baseline_cache[key]


def baseline_hashes(kind, lang, iid, part="-"):
    return {r["hash"] for r in baseline_rows() if (r["kind"], r["lang"], r["id"], r["part"]) == (kind, lang, iid, part)}


def gate():
    """The reviews publication needs: all three once VISUAL_GATE is on (a visual baseline row stands in for the visual
    PASS of unchanged content), science and pedagogy before."""
    return REVIEWS if VISUAL_GATE else REVIEWS[:2]


def item_status(kind, iid, lang, folder, h):
    """The state of an investigation, a TVT guide, a unit, a Sovella set or an example exam: reviewed when every
    reviewer of the gate passed this hash, the visual one or a baseline row for exactly this hash. The one carry
    such a part has is over figures the teacher approved (`carry-item`, "Item carry" below; teacher 2026-11-11)."""
    reports = {}
    for name in REVIEWS:
        r = report(folder, name)
        reports[name] = "missing" if r is None else r[0] if r[1] == h else "stale"
        if r and r[0] == "PASS" and r[1] != h and carried(folder, name, r[1], h): reports[name] = "PASS"   # item carry, below
    bl = baseline_hashes(kind, lang, iid)
    base = reports[VISUAL] != "PASS" and (h in bl or any(carried(folder, VISUAL, b, h) for b in bl))
    ok = all(reports[n] == "PASS" or (n == VISUAL and base) for n in gate())
    return {"state": "reviewed" if ok else "draft", "hash": h, "reports": reports, "baseline": base}


def _visual_baseline(folder, h, part):
    """(True, carry categories or None) when the visual requirement of this part is met by the baseline: a row for
    hash h, or a row for an earlier hash with a carry row (reviewer visual) over changes the visual reviewer need not
    see; (False, None) otherwise."""
    bl = baseline_hashes("lesson", courses.lang_of(folder), folder.name, part)
    if h in bl: return True, None
    c = next((c for b in bl if (c := carried(folder, VISUAL, b, h, part))), None)
    return (True, c["categories"]) if c else (False, None)


def status(folder, part="lesson"):
    """{'state': reviewed|legacy|draft, 'hash': ..., 'reports': {name: PASS|FAIL|stale|missing}, 'carried': {name: categories},
    'baseline': bool} of the lesson or of its exercise set (which has no legacy state)."""
    h = content_hash(folder, part)
    reports, carry = {}, {}
    for name in REVIEWS + (("legacy",) if part == "lesson" else ()):
        r = report(folder, name, part)
        if r is None: reports[name] = "missing"
        elif r[1] == h: reports[name] = r[0]
        elif name != "legacy" and r[0] == "PASS" and (c := carried(folder, name, r[1], h, part)):
            reports[name] = "PASS"; carry[name] = c["categories"]
        else: reports[name] = "stale"
        if name == "science" and part == "exercises" and reports[name] in ("missing", "stale") and translation_row(folder, h):
            reports[name] = "PASS"; carry[name] = TRANSLATED    # the Finnish set's science PASS (teacher 2026-11-12)
    base = False
    if reports[VISUAL] != "PASS":
        base, cats = _visual_baseline(folder, h, part)
        if cats: carry[VISUAL] = cats
    ok = all(reports[n] == "PASS" or (n == VISUAL and base) for n in gate())
    state = "reviewed" if ok else "legacy" if reports.get("legacy") == "PASS" else "draft"
    return {"state": state, "hash": h, "reports": reports, "carried": carry, "baseline": base}


def describe(folder, part=None):
    """`fy3-6: reviewed (...); exercises: reviewed (...)`, or one part's half."""
    def one(p):
        s = status(folder, p)
        why = ", ".join(f"{n}={v}" + (" (visual baseline)" if n == VISUAL and s["baseline"] else "")
                        + (f" (carried over: {s['carried'][n]})" if n in s["carried"] else "")
                        for n, v in s["reports"].items() if not (n == "legacy" and v == "missing") and not (n == VISUAL and v == "missing" and not s["baseline"] and not VISUAL_GATE))
        return f"{s['state']} ({why or 'no reports'})"
    if part: return f"{folder.name}{' exercises' if part == 'exercises' else ''}: {one(part)}"
    return f"{folder.name}: {one('lesson')}; exercises: {one('exercises')}"


def published_exercises(folder):
    """Where the page takes the exercise set from: the working tree when its reviews are current; otherwise the
    newest commit whose exercise set both reviewers passed (each report's hash, or one its PASS carries over to), so
    the lesson keeps the exercises last reviewed while new ones wait for review; None when no version was reviewed."""
    s = status(folder, "exercises")
    if s["state"] == "reviewed": return WorkTree()
    passed, ex = {}, carries(folder, "exercises")
    for name in gate():
        r = report(folder, name, "exercises")
        froms = {r[1]} if r is not None and r[0] == "PASS" else set()
        froms |= _passed_before(folder, name)          # versions this reviewer passed earlier: still passed, though it has since judged a newer one
        if name == VISUAL: froms |= baseline_hashes("lesson", courses.lang_of(folder), folder.name, "exercises")   # published before the visual gate
        if name == "science" and courses.lang_of(folder) != i18n.SOURCE:   # versions carried from a Finnish set its science reviewer passed
            fi = courses.translation(folder, i18n.SOURCE); r_fi = report(fi, name, "exercises")
            fi_passed = _passed_before(fi, name) | ({r_fi[1]} if r_fi and r_fi[0] == "PASS" else set())
            fi_passed |= {c["to"] for c in carries(fi, "exercises") if c["reviewer"] == name and c["from"] in fi_passed}
            froms |= {c["to"] for c in ex if c["reviewer"] == name and c["categories"] == TRANSLATED and c["from"] in fi_passed}
        if not froms: return None
        passed[name] = froms | {c["to"] for c in ex if c["reviewer"] == name and c["from"] in froms}
    log = (git("log", "--format=%H", "-n", "80", "--", courses.exercise_dir(folder).relative_to(ROOT).as_posix(), folder.relative_to(ROOT).as_posix(),
               courses.lesson_rel(folder, "answers.py"), *figure_paths(folder)) or "").split()
    for c in log:
        hs = {hash_at(c, folder, "exercises"), hash_at(c, folder, "all")}
        if all(hs & passed[n] for n in gate()): return Commit(c)
    return None


def _passed_before(folder, name, part="exercises", n=40):
    """The hashes of the PASS reports this reviewer wrote for `part` in the last n commits of its report file: a version
    it passed stays passed after it reviews a newer one (the exercise set's fallback, e.g. science and pedagogy have
    passed new exercises the visual reviewer has not seen yet)."""
    rel = (review_dir(folder, part) / f"{name}.md").relative_to(ROOT).as_posix(); out = set()
    for c in (git("log", "--format=%H", "-n", str(n), "--", rel) or "").split():
        lines = (git("show", f"{c}:./{rel}") or "").splitlines()[:3]
        if lines and lines[0].strip() == "VERDICT: PASS":
            out |= {l.split(":", 1)[1].strip() for l in lines if l.startswith("CONTENT-HASH:")}
    return out


def _last_pass(folder, name, part="lesson", n=40):
    """The CONTENT-HASH of the newest PASS report this reviewer wrote for `part` in the last n commits of its report
    file, or None (scope after a FAIL)."""
    rel = (review_dir(folder, part) / f"{name}.md").relative_to(ROOT).as_posix()
    for c in (git("log", "--format=%H", "-n", str(n), "--", rel) or "").split():
        lines = (git("show", f"{c}:./{rel}") or "").splitlines()[:3]
        if lines and lines[0].strip() == "VERDICT: PASS":
            h = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("CONTENT-HASH:")), None)
            if h: return h
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
LABEL_CALL = re.compile(r"""\b(?:lab|label|p\.text)\(\s*(['"`])((?:(?!\1)[^\\]|\\.)*)\1""")


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
        if s.startswith(('"key_concepts"', '"term"')): return "wording"   # a glossary term (check_i18n.py), its symbols set as LaTeX
        if s.startswith('"explain"'): return "numbers" if SUBSTANTIVE.search(body) else "wording"   # Selkeä suomi "Luvun tärkeät käsitteet" (NOTES.md §12): prose
        if s.startswith(('"image"', '"solutions"')): return "structure"
        if s.strip() in ("{", "}", "},", "[", "]", "],", ""): return "comments"
        return "objectives"
    if fname.endswith(".md") and PHOTO_LINE.match(s): return "photo"       # a photograph with its alt text and caption
    if fname.endswith(".md") and s.startswith("# "): return "wording"      # the page title, the same as meta.json "title"
    if fname.endswith(".md") and (s.startswith("## ") or "<!-- vaihe -->" in body or s.startswith("```")): return "structure"
    return "numbers" if SUBSTANTIVE.search(body) else "wording"


PHOTO_LINE = re.compile(r'<figure class="unit-photo(?: wide)?"><img src="(?:pics/[a-z0-9]+|shared/pics)/[^"]+"[^>]*>(?:<figcaption>.*?</figcaption>)?</figure>\s*$')


def _is_photo(path):
    """A picture file that its folder's photos.json lists as a photograph (assets/pics/<course>/photos.json)."""
    rel = path.split("/", 1)[1] if path.startswith(("a/", "b/")) else path
    rel = rel if rel.startswith("pics/") or rel.startswith("shared/") else rel.split("assets/", 1)[-1]
    f = ROOT / "assets" / rel
    try: return f.name in json.loads((f.parent / "photos.json").read_text())
    except (OSError, json.JSONDecodeError): return False


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


LEVEL_POLICY = re.compile(   # the sentence the teacher removed from 18 chapters' exercise intros (2026-10-31), fi / fi-easy / en
    r" Taso 1 riittää perusosaamiseen[;.] [Tt]asot 2 ja 3 (?:ovat vapaaehtoisia ja syventäviä|ovat syventäviä|syventävät)(?:, joten tee ne, jos taso 1 sujuu)?\.(?: Tee ne, jos taso 1 sujuu\.)?"
    r"| Level 1 is enough for [^;\"]*; levels 2 and 3 [^.\"]*\.")


def _level_policy_removed(old, new):
    """True when the new line is the old one with its level-policy sentence deleted and nothing else changed."""
    return old != new and LEVEL_POLICY.search(old) is not None and LEVEL_POLICY.sub("", old) == new


TYPO_TOKEN = re.compile(r"\\[,;:!]|\\q?quad(?![A-Za-z])|\\(?:display|text)style(?![A-Za-z])|\\(?:left|right)(?![A-Za-z])|\\[bB]ig{1,2}[lr]?(?![A-Za-z])|~|\s+")


def _math_view(s):
    """A formula without what only sets it: spacing commands and spaces, \\dfrac/\\tfrac (as \\frac), \\mathrm (as
    \\text), {,} (as ,), \\left/\\right and \\big sizes. JSON's doubled backslashes are read as single."""
    s = s.replace("\\\\", "\\")
    s = re.sub(r"\\[dt]frac(?![A-Za-z])", r"\\frac", s)
    s = re.sub(r"\\mathrm(?![A-Za-z])", r"\\text", s)
    return TYPO_TOKEN.sub("", s.replace("{,}", ","))


def _set_view(s):
    """A line as read, whether a value or symbol is set as text or as maths: no $, no spacing commands, \\text{x} and
    \\textsf{x} as x, \\mu as µ, {,} as a comma, no spaces; ^2, \\cdot, \\theta … as the characters ², ·, θ … (SET_SYMBOLS)."""
    s = s.replace("\\\\", "\\").replace("$", "").replace("{,}", ",").replace("\\mu", "µ")
    s = re.sub(r"\\(?:text|textsf|mathrm)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[,;:!]|\s+", "", s)
    for tex, uni in SET_SYMBOLS: s = s.replace(tex, uni)          # "45 m²" and "$45\,\text{m}^2$" read alike (visual audit 2026-11-01)
    return s


SET_SYMBOLS = (("{}^\\circ", "°"), ("^\\circ", "°"), ("^{2}", "²"), ("^{3}", "³"), ("^2", "²"), ("^3", "³"), ("\\cdot", "·"),
               ("\\%", "%"), ("\\theta", "θ"), ("\\Delta", "Δ"), ("\\alpha", "α"), ("\\gamma", "γ"), ("\\eta", "η"),
               ("\\rho", "ρ"), ("\\lambda", "λ"), ("\\pm", "±"), ("\\approx", "≈"), ("-", "−"))


def _typography_pair(old, new):
    """True when two lines differ only inside their $…$ formulas, and there only in how the formula is set (_math_view):
    the words outside the maths identical, the same number of formulas."""
    if old == new: return False
    if _set_view(old) == _set_view(new):
        fa, fb = [_math_view(x).replace("\\textsf", "\\text") for x in old.split("$")[1::2]], [_math_view(x).replace("\\textsf", "\\text") for x in new.split("$")[1::2]]
        if fa == fb or (len(fa) < len(fb) and all(x in fb for x in fa)): return True   # the old formulas kept as they were ($m$ → $\\text{m}$ is a new meaning, not this)   # a symbol or a value with its unit set as maths ("82 µm" → "$82\\,\\mu\\text{m}$", "(t, s)" → "$(t, s)$", \\text{l} → \\textsf{l}), nothing else (visual audit 2026-10-31)
    if "$" not in old: return False
    a, b = old.split("$"), new.split("$")
    return len(a) == len(b) and all(x == y if i % 2 == 0 else _math_view(x) == _math_view(y) for i, (x, y) in enumerate(zip(a, b)))


JSON_STR = re.compile(r'\s*(?:"(?:[^"\\]|\\.)*": )?("(?:[^"\\]|\\.)*"),?')   # a JSON line holding one string (a key's value or a list item)


def _paragraph_pair(old, new):
    """True when two JSON lines are the same string but for paragraph breaks: read as single spaces, the new string's
    breaks give the old one (build.exercise_text renders them). The strings are decoded, so LaTeX \\nu is not a break."""
    def text(l):
        m = JSON_STR.fullmatch(l)
        try: return (l[:m.start(1)], json.loads(m.group(1))) if m else (None, None)
        except json.JSONDecodeError: return None, None
    (ko, o), (kn, n) = text(old), text(new)
    flat = lambda t: re.sub(r"[ \t]*\n[ \t\n]*", " ", t)
    return o is not None and n is not None and ko == kn and "\n" in n and flat(o) == flat(n)


def _chapter_refs_renamed(old, new):
    """True when two lines differ only in the titles of chapter references and every new one is a current title."""
    blank = lambda l: CHAPTER_REF.sub(lambda m: m.group(1) + "*…*", l)
    if blank(old) != blank(new): return False
    titles = chapter_titles()   # a JSON line carries a title's LaTeX escaped (\\Delta for \Delta)
    return all(m.group(2) in titles or m.group(2).replace("\\\\", "\\") in titles for m in CHAPTER_REF.finditer(new))


def classify(path, diff_lines, lid):
    """Categories of one file's unified diff (its +/- lines)."""
    if path.startswith(("figure:", "a/figure:", "b/figure:")): return {"figure"}   # a referenced figure's drawing code
    name = path.split("/")[-1]
    py, code = name.endswith(".py"), name.endswith(".js")
    binary = name.lower().endswith(courses.BINARY)
    in_sim = "/sims/" in f"/{path}" and not path.startswith("tests/")
    if binary and not in_sim and _is_photo(path): return {"photo"}
    if binary: return {"simulation" if in_sim else "figure"}
    if in_sim and name.endswith(".css"): return {"style"}
    cats, block = set(), []
    def flush():
        rem = [l[1:] for l in block if l.startswith("-")]; add = [l[1:] for l in block if l.startswith("+")]
        if name == "lesson.md":                        # `## Kaava` → `## Kaava: Lämpömäärä`: the same section, now named
            for o in [l for l in rem if l.startswith("## ")]:
                n = next((l for l in add if l.startswith("## ") and inquiry.heading(l[3:])[0] == inquiry.heading(o[3:])[0] and l != o), None)
                if n is not None: cats.add("section-name"); rem.remove(o); add.remove(n)
        if name.endswith(".md"):                       # a blank line added or removed (a list now builds as a list, visual audit 2026-10-31): only how the text is set
            for l in [l for l in rem + add if not l.strip()]:
                cats.add("typography"); (rem if l in rem else add).remove(l)
        if not (code or py):                           # "(luku *Tasainen liike: s = vt*)" → the chapter's current title
            for o in list(rem):
                n = next((l for l in add if l != o and _chapter_refs_renamed(o, l)), None)
                if n is not None: cats.add("chapter-ref"); rem.remove(o); add.remove(n)
            for o in list(rem):
                n = next((l for l in add if _level_policy_removed(o, l)), None)
                if n is not None: cats.add("level-policy"); rem.remove(o); add.remove(n)
            for o in list(rem):                        # a long task text given paragraph breaks, word for word the same
                n = next((l for l in add if l != o and _paragraph_pair(o, l)), None)
                if n is not None: cats.add("paragraphs"); rem.remove(o); add.remove(n)
            for o in list(rem):                        # a formula re-set, its meaning unchanged: only the visual reviewer looks
                n = next((l for l in add if _typography_pair(o, l)), None)
                if n is not None: cats.add("typography"); rem.remove(o); add.remove(n)
        dedup = lambda l: tuple(list(dict.fromkeys(x)) for x in _math_and_numbers(l))
        if name.endswith((".md", ".json")) and len(rem) == len(add) == 1 and not SVG_LINE.match(rem[0]) and dedup(rem[0]) == dedup(add[0]) \
                and not rem[0].lstrip().startswith(("#", "<", "```")) and {_line(name, rem[0], lid), _line(name, add[0], lid)} <= {"numbers", "wording"}:
            cats.add("wording"); return               # one prose line reworded, its formulas and numbers the same ("Voyager 2" is not a new number) or a repeated formula dropped (visual audit 2026-10-31)
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


def core_marks(old, new):
    """The old exercises.json or inquiry.json with each exercise's or activity's `core` mark set as in the new one, when
    that is a change (teacher 2026-11-05, "ydinpolku"); None otherwise. Whatever else changed is classified as usual."""
    try: o, n = json.loads(old), json.loads(new)
    except (json.JSONDecodeError, TypeError): return None
    if not isinstance(o, dict) or not isinstance(n, dict): return None
    def items(d):
        if isinstance(d.get("activities"), list): return [a for a in d["activities"] if isinstance(a, dict)]
        return [e for v in d.values() if isinstance(v, list) for e in v if isinstance(e, dict)]
    new_items = {e.get("id"): e for e in items(n) if "id" in e}
    changed = False
    for e in items(o):
        m = new_items.get(e.get("id"))
        if m is None or m.get("core") == e.get("core"): continue
        if "core" in m: e["core"] = m["core"]
        else: del e["core"]
        order = [k for k in m if k in e] + [k for k in e if k not in m]   # the key where the new version has it
        items_ = [(k, e[k]) for k in order]; e.clear(); e.update(items_); changed = True
    return json.dumps(o, ensure_ascii=False) if changed else None


# ------------------------------------------------------------------ added exercises (teacher 2026-11-12)
EXERCISE_LEVELS = ("level1", "level2", "level3")
REWRITTEN = 0.25          # a same-id exercise counts as replaced when its text and its solution each keep less than this share of words


def _exercise_items(text):
    """({id: (level, exercise)}, {level: [ids]}, data) of an exercises.json text, or None when it is not the three level
    lists of exercises with unique string ids."""
    try: d = json.loads(text)
    except (json.JSONDecodeError, TypeError): return None
    if not isinstance(d, dict) or set(d) != set(EXERCISE_LEVELS): return None
    found, order = {}, {}
    for lvl in EXERCISE_LEVELS:
        if not isinstance(d[lvl], list): return None
        order[lvl] = []
        for e in d[lvl]:
            if not isinstance(e, dict) or not isinstance(e.get("id"), str) or e["id"] in found: return None
            found[e["id"]] = (lvl, e); order[lvl].append(e["id"])
    return found, order, d


def _solution_sections(text):
    """(text before the first `## `, [(id, section)]) of solutions.md, normalized like the hash; None on a repeated heading."""
    parts = re.split(r"^## (.*)$", normalized(text or "", "solutions.md"), flags=re.M)
    secs = [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]
    return (parts[0].strip(), secs) if len({h for h, _ in secs}) == len(secs) else None


def _core(d):
    """The core exercise ids, by scripts/build.py core_ids: marked ones, or by default the first two of levels 1 and 2."""
    out = set()
    for lvl in EXERCISE_LEVELS:
        es = d[lvl]
        out |= {e["id"] for e in es if e.get("core")} if any("core" in e for e in es) else ({e["id"] for e in es[:2]} if lvl[-1] in "12" else set())
    return out


def _rewritten(a, b, sa, sb):
    """True when a same-id exercise was rewritten as a whole (a replacement that kept the id): its text and its solution
    each share less than REWRITTEN of their words with the old ones."""
    if not all(isinstance(x, str) and x for x in (a.get("text"), b.get("text"), sa, sb)): return False
    ratio = lambda x, y: difflib.SequenceMatcher(None, x.split(), y.split(), autojunk=False).ratio()
    return ratio(a["text"], b["text"]) < REWRITTEN and ratio(sa, sb) < REWRITTEN


def added_exercises(folder, old, new):
    """{'added', 'removed', 'replaced', 'kept'} (ids in page order) when the exercise set changed from `old` to `new`
    (Commit or WorkTree) only by whole exercises added or replaced (module docstring, teacher 2026-11-12); None when
    anything else changed, nothing was added, or something cannot be read: then the usual classification applies."""
    at = lambda n: courses.lesson_rel(folder, n)
    ia, ib = _exercise_items(old.source(at("exercises.json"))), _exercise_items(new.source(at("exercises.json")))
    sa, sb = _solution_sections(old.source(at("solutions.md"))), _solution_sections(new.source(at("solutions.md")))
    if not (ia and ib and sa and sb) or sa[0] != sb[0]: return None
    (A, oa, da), (B, ob, db) = ia, ib
    SA, SB = dict(sa[1]), dict(sb[1])
    canon = lambda e: json.dumps(e, sort_keys=True, ensure_ascii=False)
    replaced = []
    for i in A.keys() & B.keys():
        if canon(A[i][1]) == canon(B[i][1]) and SA.get(i) == SB.get(i) and A[i][0] == B[i][0]: continue
        if A[i][0] == B[i][0] and _rewritten(A[i][1], B[i][1], SA.get(i), SB.get(i)): replaced.append(i); continue
        return None                                    # a surviving exercise changed
    kept = [i for lvl in EXERCISE_LEVELS for i in ob[lvl] if i in A and i not in replaced]
    added = [i for lvl in EXERCISE_LEVELS for i in ob[lvl] if i not in A or i in replaced]
    removed = [i for lvl in EXERCISE_LEVELS for i in oa[lvl] if i not in B or i in replaced]
    if not added: return None                          # only removed: not this category
    ks = set(kept)
    if any([i for i in oa[lvl] if i in ks] != [i for i in ob[lvl] if i in ks] for lvl in EXERCISE_LEVELS): return None   # reordered
    if _core(da) & ks != _core(db) & ks: return None   # an insertion moved the default core marks of the others
    rest = lambda secs, ids: [(h, s) for h, s in secs if h in ks or h not in ids]   # kept exercises' and any other sections, in order
    if rest(sa[1], A) != rest(sb[1], B): return None
    ra, rb = old.source(at("answers.py")), new.source(at("answers.py"))
    if _view(ra, "answers.py", False) != _view(rb, "answers.py", False):
        va, vb = _run_answers(ra) if ra else {}, _run_answers(rb) if rb else {}
        if va is None or vb is None: return None
        if any(va.get(k) != vb.get(k) for k in set(va) | set(vb) if k not in added and k not in removed): return None
    kept_text = " ".join(canon(B[i][1]) + "\n" + SB.get(i, "") for i in kept)
    kept_figs, kept_pics = set(figcat.refs_in(kept_text)), set(courses.pic_refs_in([kept_text]))
    for name, rel, binary in sorted(set(entries(folder, old, "exercises")) | set(entries(folder, new, "exercises"))):
        if name in EXERCISE_CONTENT: continue
        x, y = old.source(rel, binary), new.source(rel, binary)
        if _view(x, rel, binary) == _view(y, rel, binary): continue
        if name.startswith("figure:"):                 # a figure's drawing code: the added exercises' own, or a surviving one's
            if name[7:] in kept_figs: return None
        elif name.startswith("figures.json:"):         # a translation's figure words: only new entries
            try: fx, fy = json.loads(x) if x else {}, json.loads(y) if y else {}
            except json.JSONDecodeError: return None
            if not (isinstance(fx, dict) and isinstance(fy, dict)) or any(k not in fy or fy[k] != v for k, v in fx.items()): return None
        elif rel == f"assets/{name}":                  # a picture
            if name in kept_pics: return None
        else: return None
    return {"added": added, "removed": removed, "replaced": replaced, "kept": kept}


# ------------------------------------------------------------------ a translated exercise set (teacher 2026-11-12)
TRANSLATED = "translation-of-passed"
EXACT_KEYS = ("id", "level", "kind", "core", "unit", "tolerance", "figure", "correct", "true", "lookup")   # identical in every language
OPTION_LISTS = ("choices", "statements", "order", "reasons")    # options compared by position, an option's text by its labels (A, B, …) too
SCRIPT_WORD = re.compile(r"([_^])(\{?)\\(text|mathrm)\{([^{}]*)\}")   # E_\text{sähkö}, x_{\text{max}}: a translated label
PROSE_NUMBER = re.compile(r"(?<!\w)\d+(?:[.,]\d+)*")
LABEL = re.compile(r"(?<![\w\\{])[A-Z](?!\w)")
MATH_OR_BLOCK = re.compile(r"<svg\b.*?</svg>|```.*?```|\$\$.*?\$\$|\$[^$\n]*\$", re.S)


def _tr_text(a, b, pairs, labels=False):
    """True when the translated text b keeps the science of the Finnish text a: the same formulas in the same order
    (check_i18n.formula_spans; whitespace dropped, {,} read as a point, \\text{} words kept except a sub- or superscript
    label, whose words go to `pairs` for the one-to-one check), the same figures (data-fig) and force-diagram specs, the
    same numbers outside the formulas (as a multiset: word order differs by language) and, in an option (`labels`), the
    same capital-letter labels in order ("Kappale B" → "Body B"; English "A" and "I" before a lowercase word are words)."""
    import check_i18n
    if not (isinstance(a, str) and isinstance(b, str)): return a == b
    def spans(s):
        out = []
        for f in check_i18n.formula_spans(re.sub(r"<svg\b.*?</svg>", "", s, flags=re.S)):
            words = []
            f = SCRIPT_WORD.sub(lambda m: (words.append(m.group(4).strip()), f"{m.group(1)}{m.group(2)}\\{m.group(3)}{{§}}")[1], re.sub(r"\s+", "", f).replace("{,}", "."))
            out.append((f, words))
        return out
    sa, sb = spans(a), spans(b)
    if [f for f, _ in sa] != [f for f, _ in sb]: return False
    for (_, wa), (_, wb) in zip(sa, sb): pairs.extend(zip(wa, wb))
    if re.findall(r'data-fig="([^"]+)"', a) != re.findall(r'data-fig="([^"]+)"', b) or FBD_SPEC.findall(a) != FBD_SPEC.findall(b): return False
    pa, pb = MATH_OR_BLOCK.sub(" ", a), MATH_OR_BLOCK.sub(" ", b)
    nums = lambda s: sorted(n.replace(",", ".") for n in PROSE_NUMBER.findall(s))
    if nums(pa) != nums(pb): return False
    lab = lambda s: [m.group(0) for m in LABEL.finditer(s) if not (m.group(0) in "AI" and re.match(r"\s+[a-z0-9]", s[m.end():]))]
    return not labels or lab(pa) == lab(pb)


def _tr_data(a, b, pairs, key=None, parent=None, labels=False):
    """True when the exercise b is the exercise a with only its texts translated, every text keeping its science
    (_tr_text): the same keys and list lengths, EXACT_KEYS and every other non-text value (a numeric answer, a data
    table's numbers) identical, the texts check_i18n translates (is_text) compared by _tr_text."""
    import check_i18n
    if isinstance(a, dict):
        return isinstance(b, dict) and set(a) == set(b) and all(
            _tr_data(a[k], b[k], pairs, k, check_i18n.value_words(key, parent), labels or k in OPTION_LISTS) for k in a)
    if isinstance(a, list):
        return isinstance(b, list) and len(a) == len(b) and all(_tr_data(x, y, pairs, key, parent, labels) for x, y in zip(a, b))
    if key in EXACT_KEYS or not check_i18n.is_text(key, a, parent): return type(a) == type(b) and a == b
    return _tr_text(a, b, pairs, labels and key == "text")   # an option's own words carry its label; its feedback may name others


def translation_differs(folder, fi=None, tr=None):
    """None when the translated exercise set (`folder`, a content/<lang>/ lesson) is numerically equivalent to the Finnish
    one (module docstring, "Translated exercise sets"); otherwise why not, in a few words. `fi`, `tr`: the Sources the two
    are read from (the working tree by default)."""
    fi, tr = fi or WorkTree(), tr or WorkTree()
    tr.lang = courses.lang_of(folder); fi.lang = i18n.SOURCE
    src = courses.translation(folder, i18n.SOURCE)
    at = lambda f, n: courses.lesson_rel(f, n)
    ia, ib = _exercise_items(fi.read(at(src, "exercises.json"))), _exercise_items(tr.read(at(folder, "exercises.json")))
    if not (ia and ib): return "exercises.json cannot be read as three levels of exercises"
    (A, oa, da), (B, ob, db) = ia, ib
    if oa != ob: return "the exercise ids, levels or order differ"
    if _core(da) != _core(db): return "the core exercises differ"
    pairs = []
    for i in A:
        if not _tr_data(A[i][1], B[i][1], pairs): return f"{i}: a number, formula, answer or setting differs"
    sa, sb = _solution_sections(fi.read(at(src, "solutions.md"))), _solution_sections(tr.read(at(folder, "solutions.md")))
    if not (sa and sb) or [h for h, _ in sa[1]] != [h for h, _ in sb[1]]: return "solutions.md has other sections"
    if not _tr_text(sa[0], sb[0], pairs): return "the text before the first solution differs"
    for (i, x), (_, y) in zip(sa[1], sb[1]):
        if not _tr_text(x, y, pairs): return f"the solution of {i}: its formulas or numbers differ"
    fwd, back = {}, {}
    for x, y in pairs:
        if fwd.setdefault(x, y) != y or back.setdefault(y, x) != x: return f"a subscript label is translated two ways (\\text{{{x}}} / \\text{{{y}}})"
    texts = lambda s, f: [s.read(at(f, n)) for n in courses.EXERCISE_FILES]
    if courses.pic_refs_in(texts(fi, src)) != courses.pic_refs_in(texts(tr, folder)): return "the pictures differ"
    for name, rel, _ in entries(folder, tr, "exercises"):
        if not name.startswith("figures.json:"): continue
        try: words = json.loads(tr.read(rel) or "{}")
        except json.JSONDecodeError: return f"{rel} cannot be read"
        if not isinstance(words, dict) or not all(_tr_text(k, v, []) for k, v in words.items()): return f"{rel}: a figure's words carry other numbers or formulas"
    return None


def _translation_from(folder):
    """(Finnish exercise hash, Finnish folder) when the Finnish exercise set of this translated lesson has a science
    PASS (its own or carried over) for its current hash; None otherwise, and for the Finnish lesson itself."""
    if courses.lang_of(folder) == i18n.SOURCE: return None
    src = courses.translation(folder, i18n.SOURCE)
    if not (courses.exercise_dir(src) / "exercises.json").is_file(): return None
    s = status(src, "exercises")
    return (s["hash"], src) if s["reports"]["science"] == "PASS" else None


def translation_row(folder, h):
    """The carry row (science, TRANSLATED) that counts for this translated exercise set at hash h: its `to` is h, its
    `from` the Finnish set's current hash, which the Finnish science reviewer passed, and the translation's own science
    report is no verdict on h (its PASS needs no carry; its FAIL is never overridden). verify_carries re-derives the
    equivalence of every row in use; status trusts the hashes only."""
    rep = report(folder, "science", "exercises")
    if rep is not None and rep[1] == h: return None
    fi = _translation_from(folder)
    return fi and next((c for c in carries(folder, "exercises") if c["reviewer"] == "science" and c["categories"] == TRANSLATED
                        and c["from"] == fi[0] and c["to"] == h), None)


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


def test_change(rel, base, now=None):
    """'tests' when every assertion of the base version is still there, as strict; 'tests-weakened' otherwise. `now`:
    where the new version is read (the working tree by default)."""
    try:
        old = json.loads(git("show", f"{base}:./{rel}") or "[]"); new = json.loads((now or WorkTree()).read(rel) or "[]")
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


VECTOR = re.compile(r"\\(?:mathbf|vec)\{([A-Za-z])\}")


# ------------------------------------------------------------------ figures the teacher approved (teacher 2026-11-10)
# "en tiedä miksi arviointeja pitäisi suorittaa jos vain kuva vaihdetaan. kuvat olen itse hyväksynyt" and "täysin uudet
# kuvat voi tarkistaa asettelun osalta, mutta nekään eivät pedagogista tai fysikaalista arviota tarvitse": a figure whose
# Finnish drawing, exactly as it is now, has a row in docs/teacher-figures.tsv is the category "teacher-figure", which
# no reviewer must see (check_layout.py checks the page it sits on). The row holds the hash of the rendered Finnish SVG,
# so any later change to the drawing, or to the shared style it is drawn with, needs a new approval or the reviews.

ITEM_CODE = ("tutkimukset", "tvt", "units")       # lessons/<dir>/<id>/figures.py of the parts figcat does not list


def _item_figures(oid):
    """figures.py of an investigation, guide or unit `oid` (they are not in the figure catalog), or None."""
    if oid.endswith("-sovella"):                       # the task set of a unit: lessons/units/<unit>/sovella/figures.py
        f = ROOT / "lessons" / "units" / oid[:-8] / "sovella" / "figures.py"
        if f.is_file(): return f
    return next((ROOT / "lessons" / d / oid / "figures.py" for d in ITEM_CODE if (ROOT / "lessons" / d / oid / "figures.py").is_file()), None)


def _own_language(code):
    """Put figlib in the state a figures.py draws in: Finnish decimal comma, or the decimal sign the file itself sets at
    import (the units of an English course: `figlib.set_language({}, ".")`). figlib keeps that state for the process,
    so without this a figure's drawing would depend on which figures were drawn before it."""
    m = re.search(r'^figlib\.set_language\(\{\}, "(.)"\)', code or "", re.M)
    figlib.set_language({}, m.group(1) if m else ",")


def figure_hash(fid):
    """Hash of figure `fid` as figures.py draws it now in Finnish (what an approval row names)."""
    figlib.set_language({}, ",")                       # the Finnish drawing, whatever was drawn before in this process
    try: svg = figcat.render(fid)
    except KeyError:
        oid, name = fid.split("/", 1); f = _item_figures(oid)
        if f is None: raise
        fn = figcat.module(str(f.parent)).FIGURES[name]
        _own_language(f.read_text()); svg = fn()
    return hashlib.sha256(svg.encode()).hexdigest()[:16]


@functools.lru_cache(maxsize=None)
def teacher_figures():
    """{figure id: set of approved hashes} from docs/teacher-figures.tsv."""
    out = collections.defaultdict(set)
    if TEACHER_FIGURES.is_file():
        for l in TEACHER_FIGURES.read_text().splitlines():
            c = l.split("\t")
            if len(c) >= 3 and not l.startswith(("#", "date\t")): out[c[1]].add(c[2])
    return out


@functools.lru_cache(maxsize=None)
def approved(fid):
    """True when figure `fid`, as the working tree draws it, is one the teacher approved."""
    rows = teacher_figures().get(fid)
    if not rows: return False
    try: return figure_hash(fid) in rows
    except Exception: return False


def approve_figures(lid):
    """Append a row for every figure of lesson `lid` (its figures.py, as drawn now) that has none for its current drawing."""
    rows = teacher_figures(); folder = find_lesson(lid)
    mod = figcat.module(str(courses.code_dir(folder)))
    new = [(f"{lid}/{name}", figure_hash(f"{lid}/{name}")) for name in getattr(mod, "FIGURES", {})]
    new = [(fid, h) for fid, h in new if h not in rows.get(fid, set())]
    if not TEACHER_FIGURES.is_file():
        TEACHER_FIGURES.write_text("# Figures the teacher approved as drawn (teacher 2026-11-10; scripts/reviews.py \"figures the teacher approved\").\n"
                                   "# One row per approved drawing: the hash of its Finnish SVG (reviews.py figure_hash). Written by\n"
                                   "# `python scripts/reviews.py approve-figures <id>` only after the teacher has seen and approved the figures.\n"
                                   "date\tfigure\thash\n")
    with TEACHER_FIGURES.open("a") as f:
        for fid, h in new: f.write(f"{datetime.date.today()}\t{fid}\t{h}\n")
    teacher_figures.cache_clear(); approved.cache_clear()
    print(f"{lid}: {len(new)} figure(s) recorded as approved")


# ------------------------------------------------------------ item carry (teacher 2026-11-11, "laajenna kevyt hyväksyntä")
# A lesson's reviews carry over a figure the teacher approved as drawn (above). An investigation, a unit, a TVT guide,
# a Sovella set and an example exam had no carry at all, so one redrawn figure took the page off the site until three new reviews. Now their
# PASS (or visual baseline row) carries over exactly one kind of change: the drawing of figures that have a row in
# docs/teacher-figures.tsv for their current drawing. `carry-item` writes review/carry.tsv (the lesson's columns) when
# item_view() of the commit that held the passed version equals item_view() of the working tree: every text with the
# approved figures' SVGs taken out, the other code as it is, and each not-approved figure as figures.py of that
# version draws it. So anything a reader sees outside the approved figures is what the reviewers passed, and a change
# to a helper that moves another figure, or to the shared figure library, does not carry. `verify` re-derives it.
ITEM_KINDS = ("investigation", "sovella", "koe", "unit", "guide")


def _item(kind, iid):
    """(module, key, owner id of its figures) of an item: its script's own folder, hash and texts."""
    if kind == "investigation":
        import investigations as m; return m, iid, iid
    if kind == "unit":
        import units as m; return m, iid, iid
    if kind == "guide":
        import guides as m; return m, iid, iid
    if kind in ("sovella", "koe"):
        import practice as m
        key = iid if kind == "sovella" or m.is_exam(iid) else iid + m.EXAM
        return m, key, f"{courses.slug(m.course_of(key))}-{kind}"
    raise SystemExit(f"carry-item: kind must be one of {', '.join(ITEM_KINDS)}")


def _figure_free(folder, code_folder, texts, code_names, oid, src, names=frozenset()):
    """The texts with the approved figures of owner `oid` taken out, the other code as it is, each not-approved figure as
    drawn; a .md text as kaavat.review_view sees it, so formula names in `names` (approved by the teacher) carry too."""
    rel = lambda p: p.relative_to(ROOT).as_posix()
    md = lambda n, t: kaavat.review_view(t, names) if n.endswith(".md") else t
    out = [(n, md(n, normalized(_strip_approved_svgs(src.read(rel(folder / n)) or "", oid), n))) for n in texts]
    for n in code_names:
        code = src.read(rel(code_folder / n))
        if n != "figures.py" or not code: out.append((n, code or "")); continue
        mod = type(sys)("figures_at_commit"); mod.__file__ = str(code_folder / n)   # a figures.py may read files beside it
        exec(compile(code, n, "exec"), mod.__dict__); figs = mod.FIGURES
        out.append((n, sorted(figs)))
        for name in sorted(figs):
            if approved(f"{oid}/{name}"): continue
            _own_language(code); out.append((f"figure {name}", hashlib.sha256(figs[name]().encode()).hexdigest()))
    return out


def item_view(kind, iid, lang, src):
    """What an item's reviews judge apart from its teacher-approved figures, as `src` (WorkTree or Commit) has it. A
    unit's own task set is reviewed with the unit: the same view of it, its figures owned by "<unit>-sovella"."""
    m, key, oid = _item(kind, iid)
    names = frozenset(kaavat.approved(key, lang)) if kind == "unit" else frozenset()
    out = _figure_free(m.folder(key, lang), m.code_folder(key), m.TEXTS, getattr(m, "CODE", ("figures.py",)), oid, src, names)
    if kind == "unit" and m.has_tasks(key, lang):
        import practice
        tk = m.task_key(key)
        out += [("sovella", _figure_free(practice.folder(tk, lang), practice.code_folder(tk), practice.TEXTS, practice.CODE, f"{key}-sovella", src))]
    return out


def _item_base(kind, iid, lang, frm):
    """The newest commit whose version of the item has hash `frm`, or None."""
    m, key, _ = _item(kind, iid)
    paths = [p.relative_to(ROOT).as_posix() for p in (m.folder(key, lang), m.code_folder(key))]
    for c in (git("log", "--format=%H", "-n", "80", "--", *paths) or "").split():
        if m.content_hash(key, lang, read=Commit(c).read) == frm: return c
    return None


def item_carry(kind, iid, lang=i18n.SOURCE):
    """Write review/carry.tsv rows of an item for every reviewer whose PASS holds over teacher-approved figures."""
    m, key, oid = _item(kind, iid)
    folder, h = m.folder(key, lang), m.content_hash(key, lang)
    rows, now, added = carries(folder), None, []
    for name in REVIEWS:
        rep = report(folder, name)
        frm = rep[1] if rep and rep[0] == "PASS" else next(iter(sorted(baseline_hashes(kind, lang, key))), None) if name == VISUAL else None
        if frm is None: print(f"{name}: no earlier PASS, review needed"); continue
        if frm == h or carried(folder, name, frm, h): print(f"{name}: already current"); continue
        base = _item_base(kind, iid, lang, frm)
        if base is None: print(f"{name}: the version it passed is not in git history, review needed"); continue
        now = now or item_view(kind, iid, lang, WorkTree())
        if item_view(kind, iid, lang, Commit(base)) != now: print(f"{name}: more than teacher-approved figures and formula names changed, review needed"); continue
        cat = item_category(kind, iid, lang, base)
        rows.append({"date": str(datetime.date.today()), "reviewer": name, "from": frm, "to": h, "base": base[:12], "categories": cat})
        added.append(name); print(f"{name}: carried over ({'; '.join(WHY[c] for c in cat.split(','))})")
    if added:
        (folder / "review").mkdir(exist_ok=True)
        (folder / "review" / "carry.tsv").write_text("\t".join(CARRY_COLS) + "\n" + "".join("\t".join(r[c] for c in CARRY_COLS) + "\n" for r in rows))
    print(f"{lang}/{key}: {m.status(key, lang)['state']}")


def item_category(kind, iid, lang, base):
    """What a carried item change was: "formula-names" when the named formulas of its texts changed, "teacher-figure"
    when anything else did (approved figures), both when both did."""
    m, key, oid = _item(kind, iid)
    names_at = lambda src: [kaavat.names_of(src.read((m.folder(key, lang) / n).relative_to(ROOT).as_posix()) or "") for n in m.TEXTS if n.endswith(".md")]
    cats = []
    if names_at(Commit(base)) != names_at(WorkTree()): cats.append("formula-names")
    if _figures_differ(kind, iid, lang, base): cats.append("teacher-figure")
    return ",".join(cats or ["teacher-figure"])


def _figures_differ(kind, iid, lang, base):
    """Whether an item's approved figures differ between `base` and the working tree (the SVGs or figures.py)."""
    m, key, oid = _item(kind, iid)
    texts = lambda src: [src.read((m.folder(key, lang) / n).relative_to(ROOT).as_posix()) or "" for n in m.TEXTS]
    svgs = lambda src: [x.group(0) for t in texts(src) for x in SVG_BLOCK.finditer(t)]
    code = lambda src: src.read((m.code_folder(key) / "figures.py").relative_to(ROOT).as_posix())
    return svgs(Commit(base)) != svgs(WorkTree()) or code(Commit(base)) != code(WorkTree())


def verify_item_carries(kind, iid, lang):
    """Errors for an item's carry rows in use: the base must hold the passed version, and nothing but approved figures may differ."""
    m, key, _ = _item(kind, iid)
    folder, h, errs = m.folder(key, lang), m.content_hash(key, lang), []
    for name in REVIEWS:
        rep = report(folder, name)
        froms = [rep[1]] if rep and rep[0] == "PASS" and rep[1] != h else sorted(baseline_hashes(kind, lang, key) - {h}) if name == VISUAL and not (rep and rep[0] == "PASS") else []
        c = next((x for f in froms if (x := carried(folder, name, f, h))), None)
        if not c: continue
        what = f"{lang}/{key}: carry of {name}"
        if git("rev-parse", "--verify", "-q", f"{c['base']}^{{commit}}") is None: errs.append(f"{what} names commit {c['base']}, not in history (CI needs fetch-depth: 0)"); continue
        if m.content_hash(key, lang, read=Commit(c["base"]).read) != c["from"]: errs.append(f"{what}: commit {c['base']} does not hold hash {c['from']}"); continue
        if item_view(kind, iid, lang, Commit(c["base"])) != item_view(kind, iid, lang, WorkTree()): errs.append(f"{what} covers more than figures and formula names the teacher approved")
    return errs


def items(lang):
    """[(kind, id)] of every item of a language that can carry."""
    import investigations, practice, units, guides
    return [("investigation", i) for i in investigations.ids(lang)] + [("sovella", c) for c in practice.courses_with(lang)] + \
           [("koe", c) for c in practice.exams(lang)] + [("unit", u) for u in units.ids(lang)] + [("guide", g) for g in guides.ids(lang)]


SVG_BLOCK = re.compile(r'<svg\b[^>]*\bdata-fig="([^"]+)".*?</svg>', re.S)
FIG_REF_LINE = re.compile(r'^\s*"figure":\s*"([^"]+)",?$')


def _strip_approved_svgs(text, oid):
    """lesson.md with each approved figure's SVG reduced to a placeholder naming it."""
    if not text: return text
    return SVG_BLOCK.sub(lambda m: f'<svg data-fig="{m.group(1)}" data-approved=""></svg>' if approved(f"{oid}/{m.group(1)}") else m.group(0), text)


def _approved_texts(oid):
    """The Finnish words drawn in the approved figures of owner `oid` (what figures.json translates)."""
    try: mod = figcat.module(str(figcat.owner(oid)[0]))
    except Exception: return ""
    return html.unescape("\n".join(figcat.render(f"{oid}/{n}") for n in getattr(mod, "FIGURES", {}) if approved(f"{oid}/{n}")))


def _strip_approved_translations(old, new, oid):
    """(old, new) figures.json views without the entries of approved figures' words and without entries dropped since
    old (a translation of a text no longer drawn: check_i18n.py fails a drawn text left without one)."""
    try: a, b = json.loads(old), json.loads(new)
    except (TypeError, json.JSONDecodeError): return old, new
    drawn = _approved_texts(oid)
    keep = lambda d, other: {k: v for k, v in d.items() if not (k in drawn) and (other is None or k in other)}
    a2, b2 = keep(a, b), keep(b, None)
    return json.dumps(a2, indent=1, ensure_ascii=False), json.dumps(b2, indent=1, ensure_ascii=False)


def _strip_approved_refs(text):
    """exercises.json view without the "figure" lines naming approved figures, trailing commas dropped (a key added
    last moves the comma of the line before it)."""
    if not text: return text
    return "\n".join(l.rstrip(",") for l in text.splitlines() if not ((m := FIG_REF_LINE.match(l)) and approved(m.group(1))))


def _approved_change(rel, a, b, oid):
    """(a, b, taken): the views with the approved figures' part of the change taken out, and whether there was one."""
    if rel.endswith("/lesson.md"):
        a2, b2 = _strip_approved_svgs(a, oid), _strip_approved_svgs(b, oid)
        return a2, b2, (a2, b2) != (a, b)
    if rel.endswith("/figures.json") and a and b:
        a2, b2 = _strip_approved_translations(a, b, rel.split("/")[-2])
        return a2, b2, (a2, b2) != (a, b)
    if rel.endswith("/exercises.json") and a and b:
        refs = lambda t: [l.strip().rstrip(",") for l in t.splitlines() if (m := FIG_REF_LINE.match(l)) and approved(m.group(1))]
        if refs(a) == refs(b): return a, b, False
        return _strip_approved_refs(a), _strip_approved_refs(b), True
    return a, b, False


# A simulation's change that only places or draws (teacher 2026-11-11: an axis name or a label moved is no reason for a
# full science and pedagogy review). Two things must both hold, or the change is "simulation" as before:
#   1. presentation_only(old, new): every changed line of code is drawing or placing. A changed line may call the canvas
#      text and shape functions, Math, the sim's lab() and helpers with a name of at most three letters (X, Y, tx, tj);
#      it may declare new local names; it may not assign to anything else, define or return from a function, touch
#      simState, the adapter, the controls, events, time, randomness, window or document, or call any other function.
#      A name it declares must be new to the file, unless the same declaration stood on a removed line.
#   2. docs/presentation-only.tsv has a row with the hashes of exactly this file before and after. The row is written by
#      `reviews.py approve-presentation`, which prints the diff; the teacher approves it by merging the pull request
#      that carries the row. Any later edit of the file changes its hash, and the row no longer applies.
# The visual reviewer still looks (delta), and test_sims.py checks the labels and the sim's assertions as always.
PRES_FORBID = re.compile(r"simState|simAdapter|defineSimAdapter|deltaTime|frameCount|millis\(|Math\.random|create[A-Z]\w*\(|addEventListener|"
                         r"\bfunction\b|\breturn\b|\bwindow\b|\bdocument\b|localStorage|\+\+|--|=>|\bnew\b|\bawait\b|\bwhile\b")
PRES_CALLS = {"text", "textSize", "textWidth", "textAlign", "textStyle", "textAscent", "textDescent", "line", "rect", "triangle", "ellipse", "circle",
              "arc", "quad", "point", "stroke", "noStroke", "strokeWeight", "fill", "noFill", "push", "pop", "lab", "if", "for"}
PRES_ASSIGN = re.compile(r"(?<![=!<>])=(?!=)")
PRES_STRING = re.compile(r"`[^`]*`|'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\"")


def _pres_code(line):
    """A line of JavaScript without its strings and its trailing comment."""
    return re.sub(r"//.*$", "", PRES_STRING.sub('""', line)).strip()


def _pres_declared(stmt):
    """The names a `const` or `let` statement (or a `for (const x of …` head) declares; None when it is neither."""
    m = re.match(r"(?:for\s*\(\s*)?(?:const|let)\s+(.*)$", stmt, re.S)
    if not m: return None
    depth, names, part = 0, [], ""
    for ch in m.group(1) + ",":                       # split at the commas outside brackets
        if ch in "([{": depth += 1
        elif ch in ")]}": depth -= 1
        if ch == "," and depth <= 0:
            n = re.match(r"\s*([A-Za-z_$][\w$]*)\s*(?:=|\bof\b|$)", part)
            if not n: return None
            names.append(n.group(1)); part = ""
        else: part += ch
    return names


def presentation_only(old, new):
    """True when the change from `old` to `new` (a simulation's JavaScript) only places or draws: see the rule above."""
    if old is None or new is None or old == new: return False
    rem, add = [], []
    for l in difflib.ndiff(old.splitlines(), new.splitlines()):
        if l.startswith("- "): rem.append(_pres_code(l[2:]))
        elif l.startswith("+ "): add.append(_pres_code(l[2:]))
    if [c for c in rem if c] == [c for c in add if c]: return False   # the code is the same (comments only): the category "comments" covers that
    stmts = lambda code: [x.strip() for x in re.split(r"[;{}]", code) if x.strip()]
    removed = {x for c in rem for x in stmts(c)}
    old_names = set(re.findall(r"[A-Za-z_$][\w$]*", PRES_STRING.sub('""', old)))
    for code in rem + add:
        if PRES_FORBID.search(code): return False
        for call in re.finditer(r"(?:\b(p|Math)\s*\.\s*)?\b([A-Za-z_$][\w$]*)\s*\(", code):
            owner, name = call.groups()
            if owner == "Math" or (owner == "p" and name in PRES_CALLS) or (owner is None and (name in PRES_CALLS or len(name) <= 3)): continue
            return False
    for code in add:
        for st in stmts(code):
            names = _pres_declared(st)
            if names is None:
                if PRES_ASSIGN.search(st) or re.search(r"[-+*/%]=", st): return False
            elif st not in removed and any(n in old_names for n in names): return False
    for code in rem:                                     # a removed line may not take state with it either
        for st in stmts(code):
            if _pres_declared(st) is None and (PRES_ASSIGN.search(st) or re.search(r"[-+*/%]=", st)): return False
    return True


def _pres_hash(text):
    return hashlib.sha256((text or "").encode()).hexdigest()[:16]


@functools.lru_cache(maxsize=None)
def presentation_rows():
    """{(file, hash before, hash after)} from docs/presentation-only.tsv."""
    rows = set()
    if PRESENTATION.is_file():
        for l in PRESENTATION.read_text().splitlines():
            c = l.split("\t")
            if len(c) >= 4 and not l.startswith(("#", "date")): rows.add((c[1], c[2], c[3]))
    return rows


def presentation_approved(rel, a, b):
    """The change of the simulation file `rel` from text `a` to text `b` only draws, and exactly this change is recorded.
    `a` and `b` are the file as written (Source.read), the same for every language version."""
    return rel.endswith(".js") and (rel, _pres_hash(a), _pres_hash(b)) in presentation_rows() and presentation_only(a, b)


def presentation_change(old, new, rel):
    """presentation_approved() of the file `rel` between two states of the project (Commit, WorkTree), read as written.
    Source.source() puts a language's texts into a simulation's __('key') calls, so the same change of sim.js would
    have another hash in every language version (fi, en, fi-easy); the JavaScript all of them run is the file itself."""
    return rel.endswith(".js") and presentation_approved(rel, old.read(rel), new.read(rel))


def approve_presentation(rel, base="origin/main", note=""):
    """Show the change of a simulation file since `base` and, when it only places or draws, add its row."""
    rel = (pathlib.Path(rel).resolve().relative_to(ROOT)).as_posix() if pathlib.Path(rel).exists() else rel
    a, b = Commit(base).read(rel), WorkTree().read(rel)   # the file as written, not a language's view of it: one row holds for every language
    print("\n".join(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), f"a/{rel}", f"b/{rel}", lineterm="", n=2)))
    if not presentation_only(a, b):
        sys.exit(f"\n{rel}: this change does more than place or draw (or is no change): it stays in the category \"simulation\" and needs the full reviews")
    row = (rel, _pres_hash(a), _pres_hash(b))
    if row in presentation_rows(): print(f"\n{rel}: this change is already recorded"); return
    if not PRESENTATION.is_file():
        PRESENTATION.write_text("# Simulation changes that only place or draw (teacher 2026-11-11; scripts/reviews.py \"presentation_only\").\n"
                                "# One row per approved change: the file and the hashes of its text before and after. Written by\n"
                                "# `python scripts/reviews.py approve-presentation <sim.js> [<base-ref>]`, which prints the diff and refuses a change\n"
                                "# that does more than draw. The teacher approves a row by merging the pull request that adds it; with the row,\n"
                                "# the science and pedagogy reviews carry over and the visual reviewer looks at the change (delta).\n"
                                "date\tfile\tbefore\tafter\tnote\n")
    with PRESENTATION.open("a") as f: f.write(f"{datetime.date.today().isoformat()}\t{rel}\t{row[1]}\t{row[2]}\t{note}\n")
    presentation_rows.cache_clear()
    print(f"\nrecorded in {PRESENTATION.relative_to(ROOT)}: {rel} {row[1]} -> {row[2]}")


def changes(folder, base, part="lesson", split=False, new=None):
    """(categories, unified diff, changed line count) of `part` between commit `base` and the working tree, over every
    source its hash covers, as the base saw them and as they are now. Formatting the hash ignores is not a change here
    either. `split`: the base's PASS was on the one hash before the split, so the category "split" applies, and when
    the base still had one answers.py for both parts, each part's answers file is compared with that file. `new`: the
    version compared with the base (the working tree by default; verify_scopes passes the commit a report was for).
    An exercise set changed only by whole exercises added or replaced is "added-exercise" alone (teacher 2026-11-12)."""
    old, new = Commit(base), new or WorkTree()
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
        if rel.startswith("figure:") and approved(rel[7:]):     # an approved figure a task refers to
            cats.add("teacher-figure"); diff.append(f"--- {rel}: drawing approved by the teacher"); continue
        if not binary and TEACHER_FIGURES.is_file():
            a2, b2, took = _approved_change(rel, a, b, folder.name)
            if took:
                cats.add("teacher-figure"); diff.append(f"--- {rel}: figures approved by the teacher")
                if a2 == b2: continue
                if rel.endswith("/lesson.md"): ra, rb = a2, b2
                a, b = a2, b2
        if rel.startswith("tests/sims/"): cats.add(test_change(rel, base, new)); diff.append(f"--- {rel}: simulation assertions changed"); continue
        if not binary and presentation_change(old, new, rel):   # where or how the sim draws, the exact change of the file approved (one row for every language): the visual reviewer sees the diff
            cats.add("presentation-only"); n += 1
            diff += list(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), f"a/{rel}", f"b/{rel}", lineterm="", n=2)); continue
        if binary: cats.add("simulation" if "/sims/" in f"/{rel}" else "photo" if _is_photo(rel) else "figure"); diff.append(f"--- {rel}: binary file {'added' if a is None else 'removed' if b is None else 'changed'}"); continue
        lines = list(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), f"a/{rel}", f"b/{rel}", lineterm="", n=2))
        if not binary and rb and FBD_SPEC.search(rb):         # drawn force diagrams: the science reviewer checks each spec
            ra2, rb2 = FBD_SPEC.sub("", ra or ""), FBD_SPEC.sub("", rb)
            if FBD_SPEC.findall(ra or "") != FBD_SPEC.findall(rb):   # a spec added or changed; unchanged specs are no change
                fi_rel = re.sub(r"^content/[^/]+/", f"content/{courses.SOURCE_LANG}/", rel)
                copy = fi_rel != rel and FBD_SPEC.findall(rb) == FBD_SPEC.findall(new.source(fi_rel) or "")
                cats.add("force-diagram-copy" if copy else "force-diagram"); ra, rb = ra2, rb2; a, b = _view(ra, rel, False), _view(rb, rel, False)
                n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines   # the specs stay in the diff
                if a != b: cats |= classify(rel, list(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), lineterm="", n=2)), folder.name)
                continue
        if not binary and ra and rb and VECTOR.search(ra):   # \\mathbf{F} → \\overline{F}: the teacher's notation, nothing else
            ra = VECTOR.sub(r"\\overline{\1}", ra); a = _view(ra, rel, False)
            if a == b: cats.add("notation"); n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        if rel.endswith("/lesson.md") and (strip_hero(a), strip_hero(b)) != (a, b):   # a label-free opening illustration
            a2, b2 = strip_hero(a), strip_hero(b)
            if HERO.findall(a or "") != HERO.findall(b or ""): cats.add("illustration")
            if a2 != b2: cats |= classify(rel, list(difflib.unified_diff((a2 or "").splitlines(), (b2 or "").splitlines(), lineterm="", n=2)), folder.name)
            n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        if rel.endswith("/figures.json") and ra and rb:   # entries only added: the words of a new figure (a task's variant); check_i18n
            try: fa, fb = json.loads(ra), json.loads(rb)   # keeps every figure already drawn fully translated, so no drawn word changes
            except json.JSONDecodeError: fa = fb = None
            if isinstance(fa, dict) and isinstance(fb, dict) and len(fb) > len(fa) and all(k in fb and fb[k] == v for k, v in fa.items()):
                cats.add("figure-words-added"); n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        if rel.endswith("/figures.json") and a and b:   # a translation's words: an illustration's description is part of the illustration
            heroes = {html.unescape(x) for s in (old.source(courses.lesson_rel(folder, "lesson.md")), new.source(courses.lesson_rel(folder, "lesson.md")))
                      for x in re.findall(r'<svg\b[^>]*data-fig="(?:hero|scene)"[^>]*aria-label="([^"]*)"', s or "")}
            keep = lambda s: "\n".join(l for l in s.splitlines() if not any(json.dumps(h, ensure_ascii=False) in l for h in heroes))
            if heroes and keep(a) == keep(b):
                cats.add("illustration"); n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
        core = core_marks(ra, rb) if rel.endswith(("exercises.json", "inquiry.json")) and ra and rb else None
        if core is not None:                           # core marks set or removed (teacher 2026-11-05); the rest as usual
            cats.add("core-mark"); ra = core; a = _view(ra, rel, False)
            if a == b: n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))); diff += lines; continue
            lines = list(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=2))
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
    if part == "exercises" and not split and diff and added_exercises(folder, old, new): cats = {"added-exercise"}   # the diff stays whole, for the packet
    return cats, "\n".join(diff), n


def passed_at(log, folder, part, h):
    """(commit, split) of the newest commit in `log` whose `part` has hash h, or whose one hash before the split was h
    (split True); (None, False) when none has."""
    for c in log:
        if hash_at(c, folder, part) == h: return c, False
        if hash_at(c, folder, "all") == h: return c, True
    return None, False


def _history(folder):
    """The last 80 commits that touched what a lesson's hashes cover (where scope looks for the version a reviewer passed)."""
    lid = folder.name; legacy = f"content/{folder.parent.name}/{lid}"     # the folder before the languages (Commit.read)
    return (git("log", "--format=%H", "-n", "80", "--", folder.relative_to(ROOT).as_posix(), courses.code_dir(folder).relative_to(ROOT).as_posix(),
                legacy, f"tests/sims/{lid}.json", "assets", f"lang/{courses.lang_of(folder)}.json", *figure_paths(folder)) or "").split()


def scope(folder, part="lesson"):
    """For each reviewer of `part`: {'mode': none|delta|full, 'base': commit|None, 'why': ..., 'diff': ..., 'categories': [...]}."""
    log = _history(folder)
    out, cache, now = {}, {}, content_hash(folder, part)
    for name in REVIEWS:
        rep = report(folder, name, part)
        if name == "science" and part == "exercises" and not (rep and rep[1] == now) and (fi := _translation_from(folder)) and translation_differs(folder) is None:
            # a translated exercise set numerically equivalent to the Finnish one, whose science PASS is current: that PASS
            # carries over (teacher 2026-11-12); `carry` writes the row, verify_carries re-derives it
            out[name] = {"mode": "none", "base": None, "from": fi[0], "why": WHY[TRANSLATED], "diff": "", "categories": [TRANSLATED]}; continue
        full = lambda why: {"mode": "full", "base": None, "from": None, "why": why, "diff": "", "categories": []}
        if rep is not None and rep[0] != "PASS":
            # a FAIL of a later round: the scope is measured from the newest version this reviewer passed, so a fix
            # round after a delta FAIL stays a delta (its packet still carries the FAIL report as the previous report);
            # without an earlier PASS it is full as before (teacher 2026-11-12, the exercise bank's added tasks)
            last = _last_pass(folder, name, part)
            if last: rep = ("PASS", last)
        if rep is None or rep[0] != "PASS":
            bl = baseline_hashes("lesson", courses.lang_of(folder), folder.name, part) if name == VISUAL else set()
            if not bl: out[name] = full("no earlier PASS"); continue
            # published before the visual gate: no visual review yet. A change it need not see carries the baseline over;
            # anything else, or no change at all, needs the first genuine visual review, of the whole part.
            frm = next((b for b in bl if b == now), None) or next(iter(sorted(bl)))
            if frm == now: out[name] = full("visual baseline: published before the visual review, not yet reviewed"); continue
            base, split = passed_at(log, folder, part, frm)
            if base is None: out[name] = full("visual baseline: the version it covers is not in git history"); continue
            if (base, split) not in cache: cache[base, split] = changes(folder, base, part, split)
            cats, diff, n = cache[base, split]
            if cats and all(RULES[c][REVIEWS.index(name)] == "none" for c in cats):
                out[name] = {"mode": "none", "base": base, "from": frm, "why": "; ".join(WHY[c] for c in sorted(cats)) + " (visual baseline carried over)", "diff": diff, "categories": sorted(cats)}
            else: out[name] = dict(full("visual baseline: the content changed since it was published, so it needs its first visual review"), categories=sorted(cats))
            continue
        if rep[1] == now:
            out[name] = {"mode": "delta", "base": None, "from": rep[1], "why": "0 changed wording line(s): the version it passed", "diff": "", "categories": []}; continue
        base, split = passed_at(log, folder, part, rep[1])
        if base is None:   # passed long ago: an earlier carry row of this reviewer names a commit that held the passed version
            for c in reversed(carries(folder, part)):
                sha = c["reviewer"] == name and c["from"] == rep[1] and (git("rev-parse", "--verify", "-q", c["base"] + "^{commit}") or "").strip()
                if sha and hash_at(sha, folder, part) == rep[1]: base = sha; break
                if sha and hash_at(sha, folder, "all") == rep[1]: base, split = sha, True; break
        if base is None: out[name] = full("the version it passed is not in git history"); continue
        if (base, split) not in cache: cache[base, split] = changes(folder, base, part, split)
        cats, diff, n = cache[base, split]
        i = REVIEWS.index(name)
        mode = max((RULES[c][i] for c in cats), key=MODES.index, default="delta")
        frm = rep[1]
        if mode == "full" and part == "exercises":
            # an exercise added in this round and passed, then fixed: measured from that PASS it is a surviving exercise
            # that changed (full); measured from an earlier version the same reviewer passed it may still be only added
            # exercises (delta). Take the lightest mode an earlier PASS of this reviewer allows (verify_scopes accepts
            # any hash the reviewer passed; teacher 2026-11-12)
            # ... and the versions its PASS was carried over to (carry.tsv `to`): a set whose figures the teacher approved
            # since the reviewer passed it holds that PASS for the carried version, and an exercise added after it is
            # measured from there (fy2-5, fy2-7 on 2026-11-12)
            carried_to = {c["to"] for c in carries(folder, part) if c["reviewer"] == name}
            for h2 in sorted((_passed_before(folder, name, part) | carried_to) - {rep[1]}):
                b2, s2 = passed_at(log, folder, part, h2)
                if b2 is None: continue
                if (b2, s2) not in cache: cache[b2, s2] = changes(folder, b2, part, s2)
                c2, d2, n2 = cache[b2, s2]
                m2 = max((RULES[c][i] for c in c2), key=MODES.index, default="delta")
                if MODES.index(m2) < MODES.index(mode): mode, base, frm, cats, diff, n = m2, b2, h2, c2, d2, n2
        strict = sorted(c for c in cats if RULES[c][i] == mode)
        why = "; ".join(WHY[c] for c in strict) if strict else f"{n} changed line(s)"
        out[name] = {"mode": mode, "base": base, "from": frm, "why": why, "diff": diff, "categories": sorted(cats)}
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
        frm = sc[name].get("from")                     # the hash its PASS (or, for visual, its baseline row) is for
        if sc[name]["mode"] != "none" or frm is None or frm == h or carried(folder, name, frm, h, part): continue
        rows.append({"date": str(datetime.date.today()), "reviewer": name, "from": frm, "to": h, "base": (sc[name]["base"] or "-")[:12],
                     "categories": ",".join(sc[name]["categories"])}); added.append(name)
    if added:
        f.parent.mkdir(exist_ok=True)
        f.write_text("\t".join(CARRY_COLS) + "\n" + "".join("\t".join(r[c] for c in CARRY_COLS) + "\n" for r in rows))
    for name in REVIEWS: print(f"{name}: {'carried over (' + sc[name]['why'] + ')' if name in added else sc[name]['mode'] + ' review needed' if sc[name]['mode'] != 'none' else 'already current'}")
    print(describe(folder, part))


def verify_carries(folder, part="lesson"):
    """Errors for carry rows in use: the change since the base must still be one this reviewer need not see."""
    errs, h, what = [], content_hash(folder, part), folder.name + (" exercises" if part == "exercises" else "")
    if part == "exercises" and (t := translation_row(folder, h)) and status(folder, part)["carried"].get("science") == TRANSLATED:
        why = translation_differs(folder)              # the hashes are bound by the row; the equivalence is re-derived here
        if why: errs.append(f"{what}: carry of science from the Finnish exercise set {t['from']}: the translation is not numerically equivalent ({why})")
    for name in REVIEWS:
        rep = report(folder, name, part)
        c = carried(folder, name, rep[1], h, part) if rep and rep[0] == "PASS" and rep[1] != h else None
        if c and c["categories"] == TRANSLATED: continue   # checked above (its `from` is a Finnish hash)
        if not c and name == VISUAL and not (rep and rep[0] == "PASS" and rep[1] == h):   # a carry of the visual baseline
            c = next((x for b in baseline_hashes("lesson", courses.lang_of(folder), folder.name, part) if b != h and (x := carried(folder, name, b, h, part))), None)
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


SCOPE_LINE = re.compile(r"SCOPE: delta ([a-z-]+(?:,[a-z-]+)*) from ([0-9a-f]{16}) base ([0-9a-f]{7,40})")


def scope_claim(folder, name, part="lesson"):
    """(categories, from-hash, base commit) a report names on its `SCOPE:` line (one of its first lines; written from an
    added-exercise delta packet, teacher 2026-11-12), ("malformed", line) for a bad one, None when it has none."""
    f = review_dir(folder, part) / f"{name}.md"
    if not f.exists(): return None
    for l in f.read_text().splitlines()[:6]:
        if l.startswith("SCOPE:"):
            m = SCOPE_LINE.fullmatch(l.strip())
            return (m.group(1).split(","), m.group(2), m.group(3)) if m else ("malformed", l.strip())
    return None


def verify_scopes(folder, part="lesson"):
    """Errors for delta PASS reports in use that name what they covered (`SCOPE: delta <categories> from <hash> base
    <commit>`): the commit must hold the version this reviewer passed before, and the change from it to the version the
    report passes must, re-derived now, still ask no more of this reviewer than a delta review (as verify_carries does
    for a carry). So a delta PASS for added exercises stands only while nothing else of the set changed."""
    errs, now, what = [], content_hash(folder, part), folder.name + (" exercises" if part == "exercises" else "")
    for name in REVIEWS:
        rep, claim = report(folder, name, part), scope_claim(folder, name, part)
        if not claim or not rep or rep[0] != "PASS": continue
        if claim[0] == "malformed": errs.append(f"{what}: {name}.md has a malformed scope line `{claim[1]}` (SCOPE: delta <categories> from <hash> base <commit>)"); continue
        _, frm, base = claim
        if rep[1] == now: target = WorkTree()
        elif carried(folder, name, rep[1], now, part):  # a carried report: the commit that held the version it passed
            c = passed_at(_history(folder), folder, part, rep[1])[0]
            if c is None: errs.append(f"{what}: {name}'s delta PASS for {rep[1]} cannot be re-derived: no commit holds that version"); continue
            target = Commit(c)
        else: continue                                 # stale, not in use
        sha = (git("rev-parse", "--verify", "-q", f"{base}^{{commit}}") or "").strip()
        if not sha: errs.append(f"{what}: {name}'s delta PASS names commit {base}, not in history (CI needs fetch-depth: 0)"); continue
        if hash_at(sha, folder, part) != frm: errs.append(f"{what}: {name}'s delta PASS: commit {base} does not hold hash {frm}"); continue
        passed = _passed_before(folder, name, part, 80) | {c["to"] for c in carries(folder, part) if c["reviewer"] == name}
        if frm not in passed: errs.append(f"{what}: {name}'s delta PASS starts from {frm}, which {name} never passed"); continue
        cats, _, _ = changes(folder, sha, part, False, target)
        i = REVIEWS.index(name)
        bad = sorted(c for c in cats if RULES[c][i] == "full")
        if bad: errs.append(f"{what}: {name}'s delta PASS covers changes that need its full review: {', '.join(WHY[c] for c in bad)}")
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


def _baseline_items():
    """[(kind, lang, id, part, folder, status)] of every part the visual gate concerns, in every language."""
    import guides, investigations, practice
    out = []
    for lang in i18n.languages():
        for f in courses.lessons(lang=lang):
            for p in ("lesson", "exercises"): out.append(("lesson", lang, f.name, p, f, lambda f=f, p=p: status(f, p)))
        out += [("investigation", lang, i, "-", investigations.folder(i, lang), lambda i=i, lang=lang: investigations.status(i, lang)) for i in investigations.ids(lang)]
        out += [("guide", lang, g, "-", guides.folder(g, lang), lambda g=g, lang=lang: guides.status(g, lang)) for g in guides.ids(lang)]
        out += [("sovella", lang, c, "-", practice.folder(c, lang), lambda c=c, lang=lang: practice.status(c, lang)) for c in practice.courses_with(lang)]
        out += [("koe", lang, c, "-", practice.folder(c, lang), lambda c=c, lang=lang: practice.status(c, lang)) for c in practice.exams(lang)]
    return out


def baseline_init():
    """Write docs/visual-baseline.tsv once: a row for every part that science and pedagogy have passed (or whose
    exercise set the site shows from an earlier commit both passed), bound to that hash. Never a PASS report."""
    global VISUAL_GATE
    if BASELINE.exists(): sys.exit(f"{BASELINE.relative_to(ROOT)} exists: the baseline is written once; rows are only ever removed")
    was, VISUAL_GATE = VISUAL_GATE, False              # what was published under the two-review rule
    rows, today = [], str(datetime.date.today())
    for kind, lang, iid, part, folder, st in _baseline_items():
        s = st()
        hashes = {s["hash"]} if s["state"] == "reviewed" else set()
        if kind == "lesson" and part == "exercises" and not hashes and isinstance(src := published_exercises(folder), Commit):
            hashes = {x for x in (hash_at(src.sha, folder, "exercises"), hash_at(src.sha, folder, "all")) if x}   # the version the page shows
        rows += [[kind, lang, iid, part, x, today] for x in sorted(hashes)]
    VISUAL_GATE = was
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE.write_text("# Visual baseline (teacher's brief 2026-10-31; scripts/reviews.py module docstring). Not reviews: what science and\n"
                        "# pedagogy had passed when the visual review became mandatory, each row valid for its content hash only.\n"
                        "# Written once by `reviews.py baseline init`; never add or edit a row (verify fails); remove rows freely.\n"
                        + "\t".join(BASELINE_COLS) + "\n" + "".join("\t".join(r) + "\n" for r in rows))
    print(f"wrote {len(rows)} baseline rows to {BASELINE.relative_to(ROOT)}")


def baseline_report():
    """Every part still on the visual baseline (published, never visually passed), and the parts whose baseline no
    longer holds (changed since; they need their first visual review before they can be published again)."""
    waiting, audited, lapsed, fallback = collections.defaultdict(list), [], [], []
    keys = {(r["kind"], r["lang"], r["id"], r["part"]) for r in baseline_rows()}
    for kind, lang, iid, part, folder, st in _baseline_items():
        if (kind, lang, iid, part) not in keys: continue
        s = st(); v = s["reports"].get(VISUAL)
        name = iid + (" exercises" if part == "exercises" else "")
        if v == "PASS": continue
        if s.get("baseline"):
            waiting[(lang, kind)].append(name)
            if v == "FAIL": audited.append(f"{lang} {kind} {name}")
        elif kind == "lesson" and part == "exercises" and isinstance(published_exercises(folder), Commit):
            fallback.append(f"{lang} {name}")             # its pages show the version passed before the edit (published_exercises)
        else: lapsed.append(f"{lang} {kind} {name}: {s['state']} (visual={v})")
    total = sum(len(v) for v in waiting.values())
    print(f"visual baseline: {total} published part(s) await their first visual review" + ("" if VISUAL_GATE else " (gate not active yet)"))
    for (lang, kind), names in sorted(waiting.items()): print(f"  {lang} {kind} ({len(names)}): {', '.join(sorted(names))}")
    if audited: print(f"audited, visual FAIL on record, still published under the baseline ({len(audited)}): " + "; ".join(audited))
    if fallback: print(f"exercise sets edited since their last review: the pages show the version published before, under its baseline row ({len(fallback)}): " + ", ".join(fallback))
    if lapsed: print(f"baseline no longer holds (content changed; a visual PASS is needed to publish) ({len(lapsed)}):\n  " + "\n  ".join(lapsed))


def verify_baseline():
    """Errors: a row the file's first commit did not have (the baseline only ever shrinks), or a malformed row."""
    if not BASELINE.is_file(): return []
    rel = BASELINE.relative_to(ROOT).as_posix(); errs = []
    for r in baseline_rows():
        if len(r) != len(BASELINE_COLS) or r["kind"] not in ("lesson", "investigation", "guide", "sovella", "koe") or not re.fullmatch(r"[0-9a-f]{16}", r.get("hash", "")):
            errs.append(f"{rel}: malformed row {r}")
    first = (git("log", "--diff-filter=A", "--format=%H", "--", rel) or "").split()
    if not first: return errs                           # not committed yet (the commit that writes it)
    orig = git("show", f"{first[-1]}:./{rel}") or ""
    have = {l for l in orig.splitlines() if l.strip() and not l.startswith("#")}
    errs += [f"{rel}: row added after the baseline was written: {l}" for l in BASELINE.read_text().splitlines()
             if l.strip() and not l.startswith("#") and l not in have]
    return errs


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
    elif a[0] == "carry-item": item_carry(a[1], a[2], globals().get("LANG", i18n.SOURCE))
    elif a[0] == "approve-figures": [approve_figures(x) for x in a[1:]]
    elif a[0] == "approve-presentation": approve_presentation(a[1], *(a[2:3] or ["origin/main"]), note=" ".join(a[3:]))
    elif a[0] == "impact": impact(a[1] if len(a) > 1 else "origin/main")
    elif a[0] == "baseline": baseline_init() if a[1:2] == ["init"] else baseline_report()
    elif a[0] == "verify":
        bad = 0
        for f in [f for lang in i18n.languages() for f in courses.lessons(lang=lang)]:
            try: print(describe(f))
            except ValueError as e: print("ERROR", e); bad += 1; continue
            for p in ("lesson", "exercises"):
                for e in verify_carries(f, p) + verify_scopes(f, p): print("ERROR", e); bad += 1
        import units as _units
        for lang in sorted(set(i18n.languages()) | set(_units.languages())):
            for kind, iid in items(lang):
                for e in verify_item_carries(kind, iid, lang): print("ERROR", e); bad += 1
        for e in verify_baseline(): print("ERROR", e); bad += 1
        sys.exit(1 if bad else 0)
    else: sys.exit(__doc__)
