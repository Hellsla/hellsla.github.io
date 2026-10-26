"""Review state of a lesson: one content hash, two reviews, no status fields.

  python scripts/reviews.py hash <id>        the lesson's content hash (reviewers put it in their report)
  python scripts/reviews.py status [<id>]    reviewed | legacy | draft for one lesson or all, with the reason
  python scripts/reviews.py legacy <id>      write review/legacy.md: prototype content the teacher keeps visible
  python scripts/reviews.py scope <id>       per reviewer: none, delta or full, from what changed since its PASS
  python scripts/reviews.py carry <id>       record that a reviewer's PASS carries over a change it need not see
  python scripts/reviews.py impact [<ref>]   which lessons a change since <ref> (default origin/main) touches, and
                                             which review each needs; shared simulations count for every user
  python scripts/reviews.py verify           CI: every lesson's state; exit 1 on a malformed report or an invalid carry

A lesson is *reviewed* when review/science.md and review/pedagogy.md both start with `VERDICT: PASS` and carry
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
import datetime, difflib, hashlib, json, os, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, inquiry

ROOT = courses.ROOT
REVIEWS = ("science", "pedagogy")
CONTENT = ("meta.json", "lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim.js", "sim-spec.md", "inquiry.json")
MODES = ("none", "delta", "full")
RULES = {                       # category: (science, pedagogy)
    "tests":          ("none",  "none"),    # tests/sims assertions added or tightened: test_sims.py checks them
    "comments":       ("none",  "none"),    # comment or blank lines in simulation code or answers.py
    "style":          ("none",  "delta"),   # colours, strokes, fonts, classes in a figure; a simulation's sim.css
    "label-position": ("none",  "delta"),   # a figure label moved by at most 40 units, its text unchanged
    "relocated":      ("none",  "delta"),   # the sim activity's text moved word for word into its lead and boxes (inquiry.json)
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
}
WHY = {"tests": "simulation tests added or tightened", "comments": "comments only", "style": "figure or sim styling only",
       "label-position": "a figure label nudged, text unchanged", "wording": "wording without numbers or symbols",
       "relocated": "the sim's text moved word for word into its lead and boxes", "section-name": "a section named after its law",
       "numbers": "a changed line carries a number, formula, symbol or unit", "answers": "an answer, unit, tolerance or answers.py changed",
       "tests-weakened": "a simulation assertion removed or loosened", "levels": "an exercise level or id changed",
       "structure": "headings, stages, display blocks or inquiry structure changed", "objectives": "meta goals or prerequisites changed",
       "experiment": "an experiment setup, correct option or numeric answer in inquiry.json changed",
       "simulation": "the simulation's code changed", "figure": "a figure or picture changed"}


def find_lesson(lid): return courses.find_lesson(lid)


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


class WorkTree:
    """Reads a lesson's sources from the working tree (paths relative to ROOT)."""
    def read(self, rel, binary=False):
        f = ROOT / rel
        if not f.is_file(): return None
        return f.read_bytes() if binary else f.read_text()
    def files(self, reldir):
        d = ROOT / reldir
        return sorted(p.relative_to(ROOT).as_posix() for p in d.rglob("*") if p.is_file()) if d.is_dir() else []


class Commit:
    """Reads the same sources as they were in a git commit."""
    def __init__(self, sha): self.sha = sha
    def read(self, rel, binary=False): return git("show", f"{self.sha}:./{rel}", binary=binary)   # ./ is relative to ROOT, not the repository
    def files(self, reldir):
        out = git("ls-tree", "-r", "--name-only", "--full-name", self.sha, "--", reldir) or ""
        top = (git("rev-parse", "--show-prefix") or "").strip()
        return sorted(p[len(top):] if top and p.startswith(top) else p for p in out.split())


def entries(folder, src):
    """[(name, relpath, binary)] of everything the reviews judge, as `src` sees it. FY3 lessons keep exactly the
    names they had before simulation folders and pictures existed, so their hashes did not change."""
    rel = folder.relative_to(ROOT).as_posix(); lid = folder.name
    out = [(n, f"{rel}/{n}", False) for n in CONTENT] + [(f"tests/sims/{lid}.json", f"tests/sims/{lid}.json", False)]
    meta_text = src.read(f"{rel}/meta.json")
    try: meta = json.loads(meta_text) if meta_text else {}
    except json.JSONDecodeError: meta = {}
    loc = courses.sim_location(lid, meta.get("sim"), src.read(f"{rel}/sim.js") is not None)
    if loc and loc[0] != "lesson":
        out += [(f"{loc[2]}/{p[len(loc[1]) + 1:]}", p, p.lower().endswith(courses.BINARY)) for p in src.files(loc[1])]
    refs = courses.pic_refs_in(src.read(f"{rel}/{n}") for n in courses.TEXT_FILES)
    out += [(r, f"assets/{r}", r.lower().endswith(courses.BINARY)) for r in refs]
    return out


def hash_of(folder, src):
    """The content hash as `src` sees the lesson (None if the lesson did not exist there)."""
    h, found = hashlib.sha256(), False
    for name, rel, binary in entries(folder, src):
        data = src.read(rel, binary)
        if data is None: continue
        found = True
        h.update(name.encode() + b"\0" + (data if binary else normalized(data, name).encode()) + b"\0")
    return h.hexdigest()[:16] if found else None


def content_hash(folder): return hash_of(folder, WorkTree())
def hash_at(commit, folder): return hash_of(folder, Commit(commit))


def report(folder, name):
    """(verdict, hash) from review/<name>.md, or None when there is no report. A malformed report raises."""
    f = folder / "review" / f"{name}.md"
    if not f.exists(): return None
    lines = f.read_text().splitlines()[:3]
    verdict = lines[0].split(":", 1)[1].strip() if lines and lines[0].startswith("VERDICT:") else None
    h = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("CONTENT-HASH:")), None)
    if verdict not in ("PASS", "FAIL") or not h:
        raise ValueError(f"{f.relative_to(ROOT)}: line 1 must be `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: <hash>`")
    return verdict, h


CARRY_COLS = ["date", "reviewer", "from", "to", "base", "categories"]


def carries(folder):
    f = folder / "review" / "carry.tsv"
    if not f.exists(): return []
    lines = f.read_text().splitlines()
    return [dict(zip(CARRY_COLS, l.split("\t"))) for l in lines[1:] if l.strip()]


def carried(folder, name, from_hash, to_hash):
    return next((c for c in carries(folder) if c["reviewer"] == name and c["from"] == from_hash and c["to"] == to_hash), None)


def status(folder):
    """{'state': reviewed|legacy|draft, 'hash': ..., 'reports': {name: PASS|FAIL|stale|missing}, 'carried': {name: categories}}."""
    h = content_hash(folder)
    reports, carry = {}, {}
    for name in REVIEWS + ("legacy",):
        r = report(folder, name)
        if r is None: reports[name] = "missing"
        elif r[1] == h: reports[name] = r[0]
        elif name != "legacy" and r[0] == "PASS" and (c := carried(folder, name, r[1], h)):
            reports[name] = "PASS"; carry[name] = c["categories"]
        else: reports[name] = "stale"
    state = ("reviewed" if all(reports[n] == "PASS" for n in REVIEWS)
             else "legacy" if reports["legacy"] == "PASS" else "draft")
    return {"state": state, "hash": h, "reports": reports, "carried": carry}


def describe(folder):
    s = status(folder)
    why = ", ".join(f"{n}={v}" + (f" (carried over: {s['carried'][n]})" if n in s["carried"] else "")
                    for n, v in s["reports"].items() if not (n == "legacy" and v == "missing"))
    return f"{folder.name}: {s['state']} ({why or 'no reports'})"


def write_legacy(folder):
    s = status(folder)
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
STYLE_ATTR = re.compile(r'\s(?:fill|stroke|stroke-width|stroke-dasharray|stroke-linecap|stroke-linejoin|stroke-opacity|fill-opacity|opacity|'
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
    if fname.endswith(".md") and (s.startswith("## ") or "<!-- vaihe -->" in body or s.startswith("```")): return "structure"
    return "numbers" if SUBSTANTIVE.search(body) else "wording"


def classify(path, diff_lines, lid):
    """Categories of one file's unified diff (its +/- lines)."""
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


def changes(folder, base):
    """(categories, unified diff, changed line count) between commit `base` and the working tree, over every source the
    hash covers, as the base saw them and as they are now. Formatting the hash ignores is not a change here either."""
    old, new = Commit(base), WorkTree()
    paths = sorted({(rel, b) for _, rel, b in entries(folder, old) + entries(folder, new)})
    cats, diff, n = set(), [], 0
    for rel, binary in paths:
        ra, rb = old.read(rel, binary), new.read(rel, binary)
        a, b = _view(ra, rel, binary), _view(rb, rel, binary)
        if a == b: continue
        if rel.startswith("tests/sims/"): cats.add(test_change(rel, base)); diff.append(f"--- {rel}: simulation assertions changed"); continue
        if binary: cats.add("simulation" if "/sims/" in f"/{rel}" else "figure"); diff.append(f"--- {rel}: binary file {'added' if a is None else 'removed' if b is None else 'changed'}"); continue
        lines = list(difflib.unified_diff((a or "").splitlines(), (b or "").splitlines(), f"a/{rel}", f"b/{rel}", lineterm="", n=2))
        moved = relocated(ra, rb) if rel.endswith("inquiry.json") and ra and rb else None
        if moved is not None:                          # the moved text is "relocated"; whatever else changed is classified as usual
            cats.add("relocated"); a2 = _view(moved, rel, False)
            cats |= classify(rel, list(difflib.unified_diff(a2.splitlines(), b.splitlines(), lineterm="", n=2)), folder.name) if a2 != b else set()
        else: cats |= classify(rel, lines, folder.name)
        n += sum(1 for l in lines if l.startswith(("+", "-")) and not l.startswith(("+++", "---")))
        diff += lines
    return cats, "\n".join(diff), n


def scope(folder):
    """For each reviewer: {'mode': none|delta|full, 'base': commit|None, 'why': ..., 'diff': ..., 'categories': [...]}."""
    rel, lid = folder.relative_to(ROOT), folder.name
    log = (git("log", "--format=%H", "-n", "80", "--", str(rel), f"tests/sims/{lid}.json", "assets") or "").split()
    out, cache = {}, {}
    for name in REVIEWS:
        rep = report(folder, name)
        if rep is None or rep[0] != "PASS": out[name] = {"mode": "full", "base": None, "why": "no earlier PASS", "diff": "", "categories": []}; continue
        if rep[1] == content_hash(folder):
            out[name] = {"mode": "delta", "base": None, "why": "0 changed wording line(s): the version it passed", "diff": "", "categories": []}; continue
        base = next((c for c in log if hash_at(c, folder) == rep[1]), None)
        if base is None: out[name] = {"mode": "full", "base": None, "why": "the version it passed is not in git history", "diff": "", "categories": []}; continue
        if base not in cache: cache[base] = changes(folder, base)
        cats, diff, n = cache[base]
        i = REVIEWS.index(name)
        mode = max((RULES[c][i] for c in cats), key=MODES.index, default="delta")
        strict = sorted(c for c in cats if RULES[c][i] == mode)
        why = "; ".join(WHY[c] for c in strict) if strict else f"{n} changed line(s)"
        out[name] = {"mode": mode, "base": base, "why": why, "diff": diff, "categories": sorted(cats)}
    return out


def print_scope(folder):
    sc = scope(folder)
    for name, v in sc.items():
        print(f"{name}: {v['mode']} ({v['why']})" + (f" base={v['base'][:7]}" if v["base"] else "") + (f" categories={','.join(v['categories'])}" if v["categories"] else ""))
    return sc


def carry(folder):
    """Write review/carry.tsv rows for every reviewer whose mode is none (its PASS holds for the current hash)."""
    sc, h, rows = scope(folder), content_hash(folder), carries(folder)
    f = folder / "review" / "carry.tsv"; added = []
    for name in REVIEWS:
        rep = report(folder, name)
        if sc[name]["mode"] != "none" or rep is None or rep[1] == h or carried(folder, name, rep[1], h): continue
        rows.append({"date": str(datetime.date.today()), "reviewer": name, "from": rep[1], "to": h, "base": sc[name]["base"][:12],
                     "categories": ",".join(sc[name]["categories"])}); added.append(name)
    if added:
        f.parent.mkdir(exist_ok=True)
        f.write_text("\t".join(CARRY_COLS) + "\n" + "".join("\t".join(r[c] for c in CARRY_COLS) + "\n" for r in rows))
    for name in REVIEWS: print(f"{name}: {'carried over (' + sc[name]['why'] + ')' if name in added else sc[name]['mode'] + ' review needed' if sc[name]['mode'] != 'none' else 'already current'}")
    print(describe(folder))


def verify_carries(folder):
    """Errors for carry rows in use: the change since the base must still be one this reviewer need not see."""
    errs, h = [], content_hash(folder)
    for name in REVIEWS:
        rep = report(folder, name)
        c = carried(folder, name, rep[1], h) if rep and rep[1] != h else None
        if not c: continue
        if git("rev-parse", "--verify", "-q", f"{c['base']}^{{commit}}") is None:
            errs.append(f"{folder.name}: carry of {name} names commit {c['base']}, not in history (CI needs fetch-depth: 0)"); continue
        if hash_at(c["base"], folder) != c["from"]: errs.append(f"{folder.name}: carry of {name}: commit {c['base']} does not hold hash {c['from']}"); continue
        cats, _, _ = changes(folder, c["base"])
        i = REVIEWS.index(name)
        bad = [x for x in cats if RULES[x][i] != "none"]
        if bad: errs.append(f"{folder.name}: carry of {name} covers changes it must review: {', '.join(WHY[x] for x in bad)}")
    return errs


def impact(ref):
    """Which lessons the files changed since `ref` touch, and the review each needs."""
    top = (git("rev-parse", "--show-prefix") or "").strip()
    names = set((git("diff", "--name-only", ref) or "").split()) | set((git("ls-files", "--others", "--exclude-standard") or "").split())
    names = {n[len(top):] if top and n.startswith(top) else n for n in names}
    deps, lessons, tooling = courses.deps(), set(), []
    for n in sorted(names):
        if n.endswith((".gitkeep", "README.md")) and n.startswith("assets/"): continue
        m = re.match(r"content/[^/]+/([^/]+)/", n)
        if m and m.group(1) != "_gold" and "/review/" not in n: lessons.add(m.group(1)); continue
        m = re.match(r"tests/sims/([^/]+)\.json$", n)
        if m: lessons.add(m.group(1)); continue
        m = re.match(r"assets/((?:sims/[^/]+|shared/sims)/[^/]+)/", n) or re.match(r"assets/((?:pics/[^/]+|shared/pics)/[^/]+)$", n)
        if m:
            users = deps.get(m.group(1), [])
            lessons |= set(users); print(f"{n}: used by {', '.join(users) or 'no lesson yet'}"); continue
        if n.startswith(("scripts/", "templates/", "curriculum.json", "glossary.json", ".claude/", "docs/", "site/")) or n.endswith((".md", ".yml")):
            tooling.append(n)
    if tooling: print(f"tooling, templates, config or docs ({len(tooling)} file(s)): no review; CI re-runs every check and rebuilds every page")
    for lid in sorted(lessons):
        folder = next((f for f in courses.lessons() if f.name == lid), None)
        if folder is None: print(f"{lid}: removed or not a lesson"); continue
        sc = scope(folder)
        print(f"{lid}: " + "; ".join(f"{n} {v['mode']} ({v['why']})" for n, v in sc.items()))
    if not lessons and not tooling: print(f"nothing changed since {ref}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == "hash": print(content_hash(find_lesson(a[1])))
    elif a[0] == "status": print("\n".join(describe(f) for f in ([find_lesson(a[1])] if len(a) > 1 else courses.lessons())))
    elif a[0] == "legacy": write_legacy(find_lesson(a[1]))
    elif a[0] == "scope": print_scope(find_lesson(a[1]))
    elif a[0] == "carry": carry(find_lesson(a[1]))
    elif a[0] == "impact": impact(a[1] if len(a) > 1 else "origin/main")
    elif a[0] == "verify":
        bad = 0
        for f in courses.lessons():
            try: print(describe(f))
            except ValueError as e: print("ERROR", e); bad += 1; continue
            for e in verify_carries(f): print("ERROR", e); bad += 1
        sys.exit(1 if bad else 0)
    else: sys.exit(__doc__)
