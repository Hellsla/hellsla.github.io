"""Role-specific packet, so an agent starts from what its role needs and nothing else.

  python scripts/review_packet.py <id> --role science|pedagogy|visual|developer [--fix] [--exercises] [--lang en]
  python scripts/review_packet.py <investigation | tvt-guide | COURSE-sovella> --role visual [--lang en]
  python scripts/review_packet.py <id> --role science|pedagogy --audit     a full packet for /quality-audit --deep (report review/audit-<role>.md)
  python scripts/review_packet.py --batch <id>,<id>,... --role science|pedagogy|visual [--lang en]

Writes review/packet-<role>.md (with --exercises exercises/review/packet-<role>.md) and prints its path, mode and size. The orchestrator never reads it: the agent's prompt
is one line naming the file ("Read content/FY4/fy4-1/review/packet-science.md and follow it. Lesson: fy4-1. Mode: full.").
CLAUDE.md, the house rules, reaches every agent by itself (Claude Code attaches it, at the latest when the agent reads
a file of the project), so no packet repeats it; NOTES.md sections are included where the role needs them.

Every packet: the lesson's course with its LOPS 2019 goals, central contents and scope notes from curriculum.json,
the lesson's slot (goals, prerequisites with their titles, glossary terms), its asset folders, and the deterministic
check results. Reviewer packets are *full* (every file the role judges, figure bodies collapsed for pedagogy, the
screenshot list), *delta* (the previous report and the diff since the version the reviewer passed) or *none* (the
change is outside the reviewer's judgement; `reviews.py carry` records it), as `reviews.py scope` decides. The
developer packet carries the writing rules and, to draft, the reference lesson and the course's existing simulations
(reuse before creating); to fix, the two reports and the lesson's file list: the developer opens the files a finding
names, which it must read before editing anyway.

A *batch* packet (review-batch/packet-<role>.md, git-ignored) gathers the delta reviews of many lessons for one reviewer
run, when each change is small and of the same kind (a law named, a sim text moved into its boxes, figures recoloured):
one agent start and one set of rules instead of one per lesson. Each lesson keeps its own report and hash; a lesson
whose change needs a full review, or none, is left out and named.

An *exercise* packet (`--exercises`, teacher 2026-10-28, README "Exercises") is about the exercise set alone: its
reviews, hash and scope are its own (`reviews.py ... --exercises`). In place of the lesson's files it carries the
**exercise brief**: what of the lesson an exercise writer or reviewer needs (the formula sections, the worked example
not to repeat, the misconception, the summary; figure bodies left out) and the current exercises, so no agent reads
the lesson text, the inquiry or the simulation to work on exercises.

A *visual* packet (teacher 2026-10-31, `.claude/agents/visual-editorial-reviewer.md`) holds what the visual &
editorial reviewer judges and nothing else: the standard's dimensions 7–10 and severities, NOTES.md §1 and the figure
and readability items of §3 and §8, the glossary terms, the check results, the source text with every figure body
collapsed to a marker, a figure inventory (file and lines, kind, section, description, LaTeX labels), the whole
screenshot list with whether it is current for this hash (`screenshot.py --if-stale` reuses unchanged captures), and
in a delta review the previous visual report, the changed files and the diff. Never simulation code, answers.py or
another chapter. Investigations, TVT guides and Sovella sets get the same packet of their own files."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n
from reviews import ROOT, find_lesson, content_hash, scope, review_dir, SVG_LINE

SVG = re.compile(r"(<svg\b[^>]*>).*?(</svg>)", re.S)
LESSON_FILES = ("meta.json", "lesson.md", "inquiry.json", "exercises.json", "solutions.md", "answers.py", "lesson-answers.py", "exit-ticket.json", "sim-spec.md", "sim.js")
EXERCISES = ("exercises.json", "solutions.md", "answers.py")


def sections(path, *names):
    """The named '## ' sections of a markdown file."""
    if not (ROOT / path).exists(): return ""
    text = (ROOT / path).read_text(); out = []
    for name in names:
        m = re.search(rf"^## {re.escape(name)}.*?(?=^## |\Z)", text, re.S | re.M)
        if m: out.append(m.group(0).strip())
    return "\n\n".join(out)


def items(path, section, *leads):
    """The bullet items of a NOTES.md section that start with one of the bold leads (`- **Complete solutions**`)."""
    m = re.search(rf"^## {re.escape(section)}.*?(?=^## |\Z)", (ROOT / path).read_text(), re.S | re.M)
    if not m: return ""
    found = re.findall(r"^- \*\*.*?(?=^- |\Z)", m.group(0), re.S | re.M)
    return "\n".join(b.rstrip() for b in found if any(b.startswith(f"- **{l}") for l in leads))


BRIEF_SECTIONS = ("Kaava", "Esimerkki", "Yleinen virhekäsitys", "Tiivistelmä")


def exercise_brief(folder):
    """What of the lesson an exercise writer or reviewer needs (module docstring): the lesson's formula sections with
    their symbols and conditions, the worked example (which no exercise repeats), the misconception and the summary,
    figure bodies left out; then the levels the course asks for."""
    f = folder / "lesson.md"
    text = f.read_text() if f.exists() else ""
    parts = [m.group(0).strip() for m in re.finditer(r"^## (.+?)$.*?(?=^## |\Z)", text, re.S | re.M)
             if m.group(1).split(":")[0].strip() in BRIEF_SECTIONS]
    body = SVG.sub(lambda m: "<!-- figure omitted -->", "\n\n".join(parts))
    body = re.sub(r"<foreignObject.*?</foreignObject>|<(?:div|figure|figcaption)[^>]*>|</(?:div|figure|figcaption)>", "", body, flags=re.S)
    levels = courses.course(courses.course_of(folder.name))["exercise_levels"]
    return (f"\n## Exercise brief: the lesson as far as the exercises need it\nFrom `{f.relative_to(ROOT)}` "
            f"({', '.join(BRIEF_SECTIONS)}; figures left out). Use its symbols and notation; an exercise needs nothing the lesson does not teach "
            f"(Level 3 may combine it with the prerequisites or an unfamiliar context). Do not open the lesson file, inquiry.json or the simulation.\n\n"
            f"Levels in this course: {', '.join(f'{k} {v}' for k, v in levels.items())} (CLAUDE.md \"Exercise levels\"; ids `{folder.name}-L<level>-NN`).\n\n"
            f"~~~~markdown\n{body.strip()}\n~~~~\n")


def block(path, label=None, collapse_svg=False):
    if not path.is_file(): return ""
    text = i18n.resolved_sim(path) if path.suffix == ".js" else path.read_text()   # a simulation with its texts from lang/fi.json in place
    if collapse_svg: text = SVG.sub(lambda m: f"{m.group(1)}\n  <!-- figure body omitted: see the figure captures in review/shots.md -->\n{m.group(2)}", text)
    lang = {".json": "json", ".py": "python", ".js": "js", ".css": "css"}.get(path.suffix, "markdown")
    return f"\n### {label or path.name}\n```{lang}\n{text.rstrip()}\n```\n"


def sim_code(folder, meta):
    """[(label, path)] of the simulation's text files (sim.js, sim.css...), wherever the course keeps them."""
    d = courses.sim_dir(folder, meta)
    if d is None: return []
    if d[0] == "lesson": return [("sim.js", courses.lesson_file(folder, "sim.js"))]
    return [(f"{p.relative_to(ROOT).as_posix()}", p) for p in sorted(d[1].rglob("*")) if p.is_file() and p.suffix in (".js", ".css", ".json", ".md")]


def header(folder, role, mode, part="lesson"):
    meta = json.loads((folder / "meta.json").read_text())
    lid = folder.name; c = courses.course(courses.course_of(lid)); s = courses.slot(lid)
    titles = {l["id"]: l["title"] for k in courses.codes() for l in courses.curriculum()[k].get("lessons", [])}
    gl = {e["term"]: e for e in json.loads((ROOT / "glossary.json").read_text())}
    terms = [gl[t] for t in meta.get("glossary", []) if t in gl]
    checks = (folder / "review/checks.txt").read_text().strip() if (folder / "review/checks.txt").exists() else "(check_lesson.py has not been run)"
    bullets = lambda xs: "\n".join(f"- {x}" for x in xs)
    out = (f"# Packet: {lid} — {meta['title']} ({c['code']} {c['title']})\n"
           + (f"Part: **exercises** (the exercise set `{courses.exercise_dir(folder).relative_to(ROOT)}/` and `answers.py`, reviewed apart from the lesson).\n" if part == "exercises" else "")
           + f"Role: **{role}**. Mode: **{mode}**. Content hash now: `{content_hash(folder, part)}`.\n"
           f"House rules: `CLAUDE.md` (in your context; if it is not, read `{(ROOT / 'CLAUDE.md').relative_to(ROOT)}` first). This packet adds what CLAUDE.md does not hold.\n\n"
           f"## Course {c['code']}: {c['title']} (LOPS 2019, {c.get('op', '?')} op, {c.get('type', '')})\n"
           f"Source: {courses.curriculum().get('_source', {}).get('modules', 'docs/lops2019/')}.\n\n**Tavoitteet**\n{bullets(c.get('tavoitteet', []))}\n\n"
           f"**Keskeiset sisällöt**\n{bullets(c.get('keskeiset_sisallot', []))}\n")
    if c.get("kokeet"): out += f"\n**Kokeellisuus**\n{bullets(c['kokeet'])}\n"
    if c.get("scope_notes"): out += f"\n**Scope of {c['code']}**\n{bullets(c['scope_notes'])}\n"
    if c["exercise_levels"] != courses.DEFAULT_LEVELS: out += f"\n**Exercise counts in {c['code']}**: {c['exercise_levels']}\n"
    pre = [f"{p} {titles.get(p, '(not in curriculum.json)')}" for p in meta.get("prerequisites", [])]
    out += (f"\n## Lesson slot {lid}\nGoals:\n{bullets(meta.get('goals', []) or s.get('goals', []))}\n"
            f"Prerequisites: {'; '.join(pre) or 'none'}\n"
            f"\n## Glossary terms of this lesson (glossary.json)\n" + "\n".join(f"- **{t['term']}**: {t['definition']}" for t in terms) + "\n"
            + (f"Not yet in glossary.json (the developer adds each, with a definition): {', '.join(t for t in meta.get('glossary', []) if t not in gl)}\n"
               if any(t not in gl for t in meta.get("glossary", [])) else ""))
    d = courses.sim_dir(folder, meta); users = courses.deps().get(d[2], []) if d and d[0] != "lesson" else []
    sim_line = ("none" if d is None else f"`{courses.lesson_file(folder, 'sim.js').relative_to(ROOT)}` (lesson folder, FY3 layout)" if d[0] == "lesson"
                else f"`{d[1].relative_to(ROOT)}/` ({d[0]}; used by {', '.join(users) or lid})")
    if part == "lesson":
        out += (f"\n## Assets\nSimulation: {sim_line}. Pictures folder of the course: `{c['paths']['pics'].relative_to(ROOT)}/` "
                f"(text refers to `pics/{c['slug']}/<file>`); pictures this lesson uses: {', '.join(courses.pic_refs(folder)) or 'none'}.\n")
    out += f"\n## Deterministic checks (already run: do not repeat them)\n```\n{checks}\n```\n"
    return out, meta


def shots(folder, role, part="lesson"):
    f = folder / "review" / "shots.md"
    if not f.exists(): return "\n## Screenshots\n(none yet: the orchestrator runs python scripts/screenshot.py first)\n"
    rows = [l for l in f.read_text().splitlines() if l.startswith("| review/")]
    if part == "exercises": rows = [l for l in rows if "exercises" in l.split("|")[1]]      # the exercise levels, closed and with solutions open
    elif role == "science": rows = [l for l in rows if re.search(r"-(fig-\d+|sim|exp-[^|]*)-\d+", l)]   # what carries physics: figures, the sim, experiments
    return ("\n## Screenshots (open only what your questions need, with the Read tool; paths relative to the lesson folder)\n"
            "| file | shows | px | ≈ tokens |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")


def guardrails():
    """The physics guardrails (docs/physics-guardrails.md, teacher 2026-10-28): every science reviewer and developer packet."""
    g = ROOT / "docs/physics-guardrails.md"
    return "\n## Physics guardrails (docs/physics-guardrails.md)\n" + g.read_text().split("\n", 1)[1] + "\n" if g.exists() else ""


def force_rules(lid):
    """The force-diagram standard (docs/force-diagrams.md, teacher 2026-10-29) for a lesson whose curriculum entry plans
    force-diagram practice ("fbd"): its writer and both reviewers judge every diagram against it."""
    g = ROOT / "docs/force-diagrams.md"
    try: plan = next(l.get("fbd") for l in courses.course(courses.course_of(lid)).get("lessons", []) if l["id"] == lid)
    except StopIteration: plan = None
    if not plan or not g.exists(): return ""
    return (f"\n## Force diagrams (docs/force-diagrams.md)\nThis lesson's plan: {', '.join(plan)} (\"fbd\" tags on its tasks; "
            "`python3 scripts/coverage.py FY4 --check` fails while a planned skill has no task). Every force figure is drawn with scripts/fbd.py.\n"
            + g.read_text().split("\n", 1)[1] + "\n")


def exercise_rules(role, lid):
    """What a reviewer of the exercise set judges, and where its report goes."""
    what = ("1. Every task's physics: the right law for the situation, its conditions met, data realistic (units, magnitudes, signs), inside the course's central contents and scope notes above and what the brief's lesson teaches.\n"
            "2. answers.py: each line computes the right physics from the task text; recompute all answers in ONE python call and compare; `unit` and `tolerance` fit the data's significant figures.\n"
            "3. solutions.md: every solution complete (NOTES §3 Complete solutions), the stated principle really applies and its reason is right, the unknown solved symbolically before substitution, conversions right, rounding justified by the really limiting datum, the reasonableness check a real check.\n"
            "4. Notation and symbols the same as in the brief's lesson.\n"
            "5. docs/physics-guardrails.md (below): terms, a law\'s conditions, exact boundary cases, assumptions stated in the task, safety statements; the solutions say what the brief\'s lesson says; an answer that agrees with its solution can still use the wrong model."
            if role == "science" else
            "1. Levels per the rubric (CLAUDE.md \"Exercise levels\" and the counts above); none repeats the worked example in the brief; together they practise the slot's goals, no more.\n"
            "2. Each task: the situation first, the question last as its own sentence; everyday contexts a 17-year-old recognises; the data needed and no trap the lesson did not prepare.\n"
            "3. Every solution can be followed step by step by a student who could not solve the task (the principle explained, not just named; nothing skipped).\n"
            "4. Finnish: grammar, glossary terms, case after number+unit (80 N:n voimalla), reading level; give the corrected sentence.\n"
            "5. Phone usability of the exercise captures listed above: nothing clipped, a long calculation still readable at 360 px.")
    return ((guardrails() if role == "science" else "") + force_rules(lid) + f"\n## What you judge (only the exercise set; the deterministic checks above are not repeated)\n{what}\n\n"
            f"## Report: write `exercises/review/{role}.md` (in the lesson folder), under 400 words, findings only\n"
            f"Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of python3 scripts/reviews.py hash {lid} --exercises>` run at the start and again at the end "
            f"(if it changed, the exercises were edited: redo the review). Then `## Blocking` (FAIL if and only if non-empty; each `file:line — problem — fix`), "
            f"`## Polish` (at most five, same format; language, style and taste go here, never under Blocking), `## Checked` (at most ten one-line items). "
            f"Never edit a lesson or exercise file. Read nothing the packet already gives you; never open lesson.md, inquiry.json or the simulation.\n")


def reviewer_rules(role, lid, both=False):
    what = ("1. Definitions: every scientific term used correctly and the same as in the earlier chapters (docs/physics-guardrails.md).\n"
            "2. Physical models: the law fits the situation, its assumptions and limits are stated where it is used, inside the course's central contents and scope notes above.\n"
            "3. Causality: each explanation names the actual mechanism, not a label (why the pressure rises, where the energy goes).\n"
            "4. Quantitative correctness: equations, dimensions, units, magnitudes, signs; answers.py and lesson-answers.py compute the right physics from the task text (recompute all answers in ONE python call with your own formulas: an answer that agrees with its solution can still use the wrong model); solutions.md, every numeric task's solution and the worked example complete (NOTES §3 Complete solutions), unknown solved symbolically first, conversions right, rounding justified by the really limiting datum, the reasonableness check a real check; figures' numbers and the simulation code implement the lesson's model.\n"
            "5. Pedagogical simplifications: a simplification is kept when it suits the level (C); one that leaves a wrong picture, or is stated as universal though true only under a condition, is a finding (A or B, guardrails).\n"
            "6. Internal consistency: the lesson agrees with itself (theory, summary, goals, sim boxes, captions) and with the chapters it builds on; the lint's `physics [...]` warnings above are judged, not ignored.\n"
            "7. Assessment correctness: in inquiry.json every correct option is right and exactly one is right where one is asked for, every distractor is really wrong and its feedback says why correctly, each experiment's setup isolates its varied parameter, model answers and the exit ticket say what the theory says.\n"
            "Report substantive issues, not rewrites of style. Classify each Blocking item A (error) or B (unstated condition)."
            if role == "science" else
            "1. Learning path: a 17-year-old with only the prerequisites can follow; the opening question is answered; the slot's goals, no more.\n"
            "2. The activities fit the topic: predictions before evidence where the topic allows, an investigation, data, a graph or a model that the student acts on; no simulation or game for its own sake; workload one lesson.\n"
            "3. Lesson form: figures next to the paragraphs they explain and legible in their captures; no wall of text; staged example, one step per stage.\n"
            "4. Exercises: levels per the rubric; none repeats the example; feedback repairs misconceptions; the exit ticket tests the core idea; every solution can be followed step by step by a student who could not solve the task (the principle explained, not just named; nothing skipped).\n"
            "5. Finnish: grammar, glossary terms, case after number+unit (80 N:n voimalla), reading level; give the corrected sentence.\n"
            "6. Phone usability from the captures: nothing clipped, controls and readout understandable. The inquiry mechanics (gating, locking, "
            "reveal, option feedback, 360 px) are already tested (checks above); open the preview in Playwright only for what a capture cannot show, "
            "such as whether the simulation makes sense when you move it.")
    return ((guardrails() if role == "science" else "") + force_rules(lid) + f"\n## What you judge (only this; the deterministic checks above are not repeated)\n{what}\n\n"
            f"## Report: write `review/{role}.md`, under 400 words, findings only\n"
            f"Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of python3 scripts/reviews.py hash {lid}>` run at the start and again at the end "
            f"(if it changed, the lesson was edited: redo the review). Then `## Blocking` (FAIL if and only if non-empty; each `file:line — problem — fix`), "
            f"`## Polish` (at most five, same format; language, style and taste go here, never under Blocking), `## Checked` (at most ten one-line items). "
            f"Never edit a lesson file. Read nothing the packet already gives you; investigate what the judgement needs.\n"
            + (f"\n## Second report: the exercise set\nThe exercises (`exercises/exercises.json`, `exercises/solutions.md`, `answers.py`) are reviewed apart from the lesson "
               f"(README \"Exercises\") and need a review too, so judge them in this run and write a second report, `exercises/review/{role}.md`, in the same format: "
               f"line 2 `CONTENT-HASH: <python3 scripts/reviews.py hash {lid} --exercises>`, findings about the exercise set only. `review/{role}.md` then holds "
               f"the findings about everything else. A finding about both goes in both.\n" if both else
               "\nThe exercise set (exercises/, answers.py) is reviewed apart from the lesson and is not yours to judge here.\n"))


def figures_used(folder, role, names=("exercises.json",)):
    """The figures the tasks show by id (scripts/figcat.py): the description and what it gives away for every role, the
    code that draws it (its data) for the science reviewer. Never an SVG body: the captures show the drawing."""
    import figcat
    ids = figcat.refs_in(" ".join(courses.lesson_file(folder, n).read_text() for n in names if courses.lesson_file(folder, n).is_file()))
    if not ids: return ""
    cat = {f["id"]: f for f in figcat.load()["figures"]}
    out = "\n## Figures the tasks show (by id; scripts/figcat.py)\n"
    for fid in ids:
        f = cat.get(fid) or {"description": "(not in the catalog: python scripts/figcat.py build)", "reuse": "?"}
        out += f"- `{fid}` ({f.get('kind', '?')}; reuse: {f['reuse']}): {f['description']}\n"
        if role == "science":
            out += f"```python\n# {figcat.code_rel(fid)}\n{figcat.slice_of(fid, lambda r: (ROOT / r).read_text())}\n```\n"
    if role != "developer":
        out += ("Check that the figure gives every value the task needs, that its description gives the same information to a reader "
                "who cannot see it, and that neither gives the answer away.\n")
    return out


def figures_available(folder):
    """What a writer of tasks may show (scripts/figcat.py): the course's figures that carry information, one line each,
    and how to refer to one or make a task variant of it. The catalog, not lesson.md or an SVG, is where to look."""
    import figcat
    code = courses.course_of(folder.name)
    lines = [l for l in figcat.find([], course=code) if " illustration " not in l and " unmanaged " not in l]
    return ("\n## Figures you can show in a task (docs/figures/catalog.json; reuse before drawing)\n"
            "Refer to one with `\"figure\": \"<id>\"` in the task. A figure marked `reveals: …` shows a result: make a variant from the same data "
            "in that lesson's figures.py (`\"<name>-points\": lambda: <name>(fit=False)` or a small function, with a description that lists the data, "
            "not the answer; README \"Figures in tasks\"). `python scripts/figcat.py show <id>` prints one figure's entry and its code; "
            "`python scripts/figcat.py find <words> --course FY3` searches. Do not open lesson.md, published HTML or SVG bodies to look for figures.\n"
            "```\n" + "\n".join(lines) + "\n```\n")


def exercise_packet(folder, role, fix=False):
    """The packet of the exercise set (module docstring): reviewers judge exercises.json, solutions.md and answers.py
    from the exercise brief; the developer writes or fixes them from it."""
    lid = folder.name; ex = courses.exercise_dir(folder)
    files = ("exercises.json", "solutions.md", "answers.py")
    if role in ("science", "pedagogy"):
        sc = scope(folder, "exercises")[role]; mode = sc["mode"]
        out, meta = header(folder, role, mode, "exercises")
        if mode == "none":
            out += (f"\n## No review needed\nSince the version you passed only this changed: {sc['why']} (categories: {', '.join(sc['categories'])}). "
                    f"It is outside your judgement (scripts/reviews.py RULES); `python scripts/reviews.py carry {lid} --exercises` records that your PASS carries over.\n")
        else:
            out += exercise_brief(folder)
            if mode == "delta":
                prev = (review_dir(folder, "exercises") / f"{role}.md").read_text()
                out += (f"\n## Delta review\nYou passed this exercise set earlier (report below). Since then only the diff below changed ({sc['why']}). "
                        f"Judge the diff in its context (the current files are on disk if you need more). If the change cannot be judged reliably this way, "
                        f"write `ESCALATE: full review needed` as line 3 of your report (verdict FAIL) and stop.\n\n### Your previous report\n```\n{prev.strip()}\n```\n"
                        f"### Changes since the version you passed\n```diff\n{sc['diff'].strip()}\n```\n")
            else:
                if sc["why"] != "no earlier PASS": out += f"\n## Full review\nReason: {sc['why']}.\n"
                out += "\n## The exercise set\n" + "".join(block(courses.lesson_file(folder, n)) for n in files if role == "science" or n != "answers.py")
            out += figures_used(folder, role) + shots(folder, role, "exercises") + exercise_rules(role, lid)
    else:
        mode = "fix" if fix else "write"
        out, meta = header(folder, role, mode, "exercises")
        out += ("\n## Rules (NOTES.md; CLAUDE.md is in your context)\n" + sections("NOTES.md", "1. Maths in LaTeX", "2. Numbers, Finnish, scope") + "\n\n"
                + items("NOTES.md", "3. Lesson form (human decisions 2026-10-25)", "Symbolic first", "Complete solutions", "Every language version") + "\n" + guardrails() + force_rules(lid))
        out += exercise_brief(folder) + figures_used(folder, role) + figures_available(folder)
        out += (f"\n## Where files go\n- `{ex.relative_to(ROOT)}/exercises.json` (schema: README \"Exercise schema\") and `{ex.relative_to(ROOT)}/solutions.md` (one `## <id>` block each)\n"
                f"- `{courses.lesson_rel(folder, 'answers.py')}`: the exercises' answers, one commented line per step, printing `{{id: value}}`\n"
                f"- never the lesson's files (lesson.md, inquiry.json, exit-ticket.json, meta.json, lesson-answers.py, figures, the simulation): a finding about those goes in your report as \"not fixable here\"\n")
        if fix:
            out += "\n## Findings to resolve (every Blocking item; Polish items only when the orchestrator lists them)\n"
            for n in ("science", "pedagogy", "visual"):
                f = review_dir(folder, "exercises") / f"{n}.md"
                if f.exists(): out += f"### {n}\n```\n{f.read_text().strip()}\n```\n"
            out += "\n## The exercise set's files (open the ones a finding names; Edit needs a Read first)\n" + "\n".join(
                f"- `{courses.lesson_rel(folder, n)}` ({courses.lesson_file(folder, n).stat().st_size} bytes)" for n in files if courses.lesson_file(folder, n).is_file()) + "\n"
        else:
            out += "\n## The exercise set now (keep every id that exists; new tasks get the next free number of their level)\n" + "".join(block(courses.lesson_file(folder, n)) for n in files)
        out += ("\n## Your task\n" + ("Resolve every Blocking finding and exactly the Polish items the orchestrator lists; change nothing else, so the reviewers judge a small diff. "
                                      if fix else "Write the exercises your prompt asks for (new tasks, or the whole set for a new lesson), each with its complete solution; none repeats the worked example or another task. ")
                + "Compute every answer in answers.py first. "
                f"Finish with `python3 scripts/lint_lesson.py {lid}` and `python3 scripts/check_solutions.py {lid}` until neither reports an error, "
                f"then write exercises/review/developer.md (`VERDICT: DONE` or `VERDICT: BLOCKED` + reason, what changed per file, ≤ 200 words).\n")
    out = lang_commands(folder, out)
    f = review_dir(folder, "exercises") / f"packet-{role}.md"; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


def lang_commands(folder, out):
    """A translation's packet: its reviews.py commands name its language (README "Languages")."""
    lang = courses.lang_of(folder)
    if lang == courses.SOURCE_LANG: return out
    return re.sub(rf"(reviews\.py (?:hash|scope|carry) {re.escape(folder.name)}(?: --exercises)?)(?! --lang)", rf"\1 --lang {lang}", out)


def packet(folder, role, fix=False, audit=False):
    lid = folder.name
    if role in ("science", "pedagogy"):
        sc = scope(folder)[role]; mode = sc["mode"]
        if audit:                                      # /quality-audit --deep: a fresh full assessment that never replaces the gate's report
            sc = dict(sc, mode="full", why="quality audit (docs/EDITORIAL_QUALITY_STANDARD.md): a fresh full assessment; your PASS report stays as it is"); mode = "full"
        out, meta = header(folder, role, mode)
        if mode == "none":
            out += (f"\n## No review needed\nSince the version you passed only this changed: {sc['why']} (categories: {', '.join(sc['categories'])}). "
                    f"It is outside your judgement (scripts/reviews.py RULES); `python scripts/reviews.py carry {lid}` records that your PASS carries over.\n")
        else:
            if (folder / "inquiry.json").exists(): out += "\n" + sections("NOTES.md", "5. Inquiry sequence (teacher's brief 2026-10-25)") + "\n"
            if mode == "delta":
                prev = (folder / "review" / f"{role}.md").read_text()
                out += (f"\n## Delta review\nYou passed this lesson earlier (report below). Since then only the diff below changed ({sc['why']}). "
                        f"Judge the diff in its context; the rest of the lesson is as you approved it (the current files are on disk if you need more context). If the change cannot be judged reliably this way, "
                        f"write `ESCALATE: full review needed` as line 3 of your report (verdict FAIL) and stop.\n\n### Your previous report\n```\n{prev.strip()}\n```\n"
                        f"### Changes since the version you passed\n```diff\n{sc['diff'].strip()}\n```\n")
            else:
                if sc["why"] != "no earlier PASS": out += f"\n## Full review\nReason: {sc['why']}.\n"
                both = scope(folder, "exercises")[role]["mode"] == "full"   # a new lesson: one reviewer run judges both parts, two reports
                names = [n for n in ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "answers.py", "lesson-answers.py", "exit-ticket.json", "sim-spec.md")
                         if (both or n not in EXERCISES) and (role == "science" or not n.endswith(".py"))]
                for n in names: out += block(courses.lesson_file(folder, n), courses.lesson_rel(folder, n) if n in EXERCISES[:2] else None, collapse_svg=(role == "pedagogy" and n == "lesson.md"))
                if role == "science":
                    for label, p in sim_code(folder, meta): out += block(p, label)
            rules = reviewer_rules(role, lid, mode == "full" and both and not audit)
            if audit:
                dims = "1 and the physics of 6" if role == "science" else "2, 3, 4, 5 and 6"
                rules = rules.replace(f"write `review/{role}.md`", f"write `review/audit-{role}.md` (an audit report: it never replaces review/{role}.md)") + (
                    f"\nEnd the audit report with `## Scores`: dimensions {dims} of docs/EDITORIAL_QUALITY_STANDARD.md, 1–5 each with a one-line reason, "
                    f"and classify every finding Critical, Major or Minor (the standard's severities) as well as A/B where your rules ask for it.\n")
            out += shots(folder, role) + rules
    else:
        mode = "fix" if fix else "draft"
        out, meta = header(folder, role, mode)
        c = courses.course(courses.course_of(lid)); d = courses.sim_dir(folder, meta)
        has_sim = d is not None or courses.lesson_file(folder, "sim-spec.md").exists() or meta.get("sim")
        out += "\n## Rules (NOTES.md; CLAUDE.md is in your context)\n" + sections("NOTES.md", "1. Maths in LaTeX", "2. Numbers, Finnish, scope", "3. Lesson form (human decisions 2026-10-25)", "5. Inquiry sequence (teacher's brief 2026-10-25)") + "\n"
        if has_sim: out += "\n" + sections("NOTES.md", "4. Simulations and pages") + "\n"
        out += guardrails() + force_rules(lid)
        own = c["paths"]["sims"] / lid
        out += figures_available(folder)
        import assessment                              # the chapter's checks, figure tasks, exit ticket and repeats (NOTES.md §11)
        out += "\n## Assessment audit of this chapter (scripts/assessment.py)\n```\n" + json.dumps(assessment.chapter(folder), ensure_ascii=False) + "\n```\n"
        out += (f"\n## Where files go\n- lesson texts: `{folder.relative_to(ROOT)}/` (meta.json, lesson.md, inquiry.json, exit-ticket.json); the exercise set: `{courses.exercise_dir(folder).relative_to(ROOT)}/` (exercises.json, solutions.md)\n"
                f"- code: `{courses.code_dir(folder).relative_to(ROOT)}/` (answers.py: the exercises' answers; lesson-answers.py: the numbers of the lesson text and the inquiry; figures.py; sim-spec.md)\n"
                f"- simulation: " + (f"`{folder.relative_to(ROOT)}/sim.js` (this course keeps sims in lesson folders)" if c.get("lesson_folder_sims")
                                     else f"`{own.relative_to(ROOT)}/sim.js` with its own `sim.css` and images when it has them (meta.json `\"sim\": true`); "
                                          f"images load from `document.getElementById('sim-root').dataset.base`") + "\n"
                f"- tests: `tests/sims/{lid}.json`; pictures: `{c['paths']['pics'].relative_to(ROOT)}/<file>`, referred to as `pics/{c['slug']}/<file>`; new glossary terms: `glossary.json`\n")
        if fix:
            out += "\n## Findings to resolve (every Blocking item; Polish items only when the orchestrator lists them)\n"
            for n in ("science", "pedagogy", "visual"):
                f = folder / "review" / f"{n}.md"
                if f.exists(): out += f"### {n}\n```\n{f.read_text().strip()}\n```\n"
        else:
            sims = sorted(p for p in c["paths"]["sims"].iterdir() if p.is_dir()) if c["paths"]["sims"].is_dir() else []
            deps = courses.deps()
            if sims:
                out += "\n## Simulations this course already has (reuse one when its model fits: meta.json `\"sim\": \"<name>\"`; changing one re-opens the review of every lesson that uses it)\n"
                out += "\n".join(f"- `{p.relative_to(ROOT)}/` used by {', '.join(deps.get(f'sims/{c['slug']}/{p.name}', [])) or 'none'}" for p in sims) + "\n"
            out += "\n## Reference lesson (content/_gold; for the inquiry shape see content/fi/FY3/fy3-2/inquiry.json, not to be copied mechanically)\n" + block(ROOT / "content/_gold/lesson.md")
        files = [(n, courses.lesson_file(folder, n)) for n in LESSON_FILES] + [(label, p) for label, p in sim_code(folder, meta) if label != "sim.js"] + [(f"tests/sims/{lid}.json", ROOT / "tests/sims" / f"{lid}.json")]
        out += "\n## The lesson's files now (open the ones your task touches; Edit needs a Read first)\n" + "\n".join(
            f"- `{p.relative_to(ROOT)}` ({p.stat().st_size} bytes)" for n, p in files if p.is_file()) + "\n"
        out += block(folder / "meta.json")
        out += ("\n## Your task\n" + ("Resolve every Blocking finding and exactly the Polish items the orchestrator lists; change nothing else, so the reviewers judge a small diff. "
                                      if fix else "Draft the lesson for its slot. Choose the activities the topic needs (an experiment on a simulation only when manipulating it reveals something; otherwise data, a graph, competing explanations or a model to build). ")
                + "When a number changes, change answers.py first. Never loosen a simulation test. "
                f"Finish with `python3 scripts/check_lesson.py {lid}` until every line is ok, then write review/developer.md (`VERDICT: DONE` or `VERDICT: BLOCKED` + reason, what changed per file, ≤ 200 words).\n")
    out = lang_commands(folder, out)
    f = folder / "review" / f"packet-{role}.md"; f.parent.mkdir(exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


# ------------------------------------------------------------------ the visual & editorial reviewer (teacher 2026-10-31)
STANDARD = "docs/EDITORIAL_QUALITY_STANDARD.md"


def visual_rules():
    """What the visual reviewer applies, from the files that hold it: the standard's severity and dimensions 7–10,
    NOTES.md §1 (maths), the figure items of §3 and the writer's items of §8. CLAUDE.md is in the agent's context."""
    std = (ROOT / STANDARD).read_text() if (ROOT / STANDARD).exists() else ""
    sev = re.search(r"^\*\*Severity\*\*.*?(?=^## )", std, re.S | re.M)
    dims = [m.group(0).strip() for m in re.finditer(r"^## (?:7|8|9|10)\. .*?(?=^## |\Z)", std, re.S | re.M)]
    return (f"\n## Your standard ({STANDARD}: severity and dimensions 7–10)\n" + (sev.group(0).strip() if sev else "") + "\n\n" + "\n\n".join(dims) + "\n"
            + "\n## House rules you apply (NOTES.md)\n" + sections("NOTES.md", "1. Maths in LaTeX") + "\n\n"
            + items("NOTES.md", "3. Lesson form (human decisions 2026-10-25)", "Figures.", "Textbook illustrations", "Opening illustration", "Every label", "Graphs", "Print quality") + "\n"
            + items("NOTES.md", "8. Readability and layout (teacher's brief 2026-10-27, \"luettavuus ja taitto\")", "No text walls", "A figure goes right", "Calculations", "Task texts") + "\n")


SVG_OPEN = re.compile(r"<svg\b([^>]*)>")


def figure_inventory(paths):
    """One line per inline figure of the given text files: where it is (file and lines), its kind, the section it sits
    in, its description and its LaTeX labels; never the SVG body (the captures show the drawing)."""
    out = []
    for p in paths:
        if not p.is_file(): continue
        text = p.read_text(); head = ""
        for m in SVG.finditer(text):
            before = text[:m.start()]
            hs = re.findall(r"^#{2,3} (.+)$", before, re.M); head = hs[-1].strip() if hs else "(opening)"
            attrs = SVG_OPEN.match(m.group(0)).group(1)
            fig = re.search(r'data-fig="([^"]*)"', attrs); lab = re.search(r'aria-label="([^"]*)"', attrs)
            labels = [re.sub(r"\s+", " ", x).strip() for x in re.findall(r'class="fig-tex"[^>]*>(.*?)</div>', m.group(0), re.S)]
            a, b = before.count("\n") + 1, before.count("\n") + 1 + m.group(0).count("\n")
            out.append(f"- `{p.relative_to(ROOT)}:{a}–{b}` {('[' + fig.group(1) + '] ') if fig else ''}in “{head}”: {(lab.group(1) if lab else 'NO aria-label')[:220]}"
                       + (f" — labels: {' · '.join(labels)[:300]}" if labels else " — no labels"))
    return ("\n## Figure inventory (inline figures; the captures `fig-N-390` show them in page order)\n" + "\n".join(out) + "\n") if out else "\n## Figure inventory\n(no inline figures)\n"


def collapsed(path, label=None):
    """A text file with each figure body replaced by a marker naming its lines (the inventory has its labels)."""
    if not path.is_file(): return ""
    text = path.read_text()
    def mark(m):
        a = text[:m.start()].count("\n") + 1
        return f"{SVG_OPEN.match(m.group(0)).group(0)[:160]}… <!-- figure body omitted (lines {a}–{a + m.group(0).count(chr(10))}): see the inventory and the captures --></svg>"
    text = SVG.sub(mark, text)
    lang = {".json": "json"}.get(path.suffix, "markdown")
    return f"\n### {label or path.relative_to(ROOT)}\n```{lang}\n{text.rstrip()}\n```\n"


def shots_visual(review, current, cmd):
    """The whole screenshot list (the visual reviewer looks at everything relevant) and whether it shows this version."""
    f = review / "shots.md"
    rows = [l for l in f.read_text().splitlines() if l.startswith("| review/")] if f.exists() else []
    stamp = (review / "shots" / "stamp.txt").read_text().strip() if (review / "shots" / "stamp.txt").exists() else ""
    state = "current: they show the content hash above" if rows and stamp.startswith(current) else f"STALE or MISSING: run `{cmd}` first and use the list it writes to review/shots.md"
    return ("\n## Screenshots (" + state + "; paths relative to the folder that holds review/; contact sheets first, then the captures your judgement needs at full size)\n"
            "| file | shows | px | ≈ tokens |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")


def visual_report_rules(path, hash_cmd, both=None):
    return (f"\n## Report: write `{path}` (format and severities: .claude/agents/visual-editorial-reviewer.md), under 400 words\n"
            f"Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of {hash_cmd}>` run at the start and again at the end. "
            f"Then `## Blocking` (FAIL if and only if non-empty; `[Critical|Major] file/figure — problem — why it matters — fix`), `## Polish` (at most five `[Minor]`), "
            f"`## Checked` (the captures you opened; at most ten lines), `## Scores` (illustrations · typography · Finnish · accessibility, 1–5). "
            f"A PASS needs the captures: if you could not look, FAIL with `visual verification incomplete`. Never edit any file but your report.\n"
            + (f"\n## Second report: the exercise set\nThe exercises are reviewed apart from the lesson and need a visual review too: judge them in this run "
               f"(their captures are the `open-exercises-*` and exercise figures) and write `{both[0]}` in the same format with line 2 `CONTENT-HASH: <{both[1]}>`, "
               f"findings about the exercise set only.\n" if both else ""))


def visual_packet(folder, part="lesson"):
    """The visual & editorial reviewer's packet of a lesson or of its exercise set: the standard, the source text with
    figure bodies collapsed, the figure inventory, the screenshot list and, in a delta review, the previous report and
    the diff. No simulation code, no answers.py, no other chapter."""
    lid = folder.name; sc = scope(folder, part)["visual"]; mode = sc["mode"]
    lang_arg = "" if courses.lang_of(folder) == courses.SOURCE_LANG else f" --lang {courses.lang_of(folder)}"
    ex_arg = " --exercises" if part == "exercises" else ""
    meta = json.loads((folder / "meta.json").read_text())
    gl = {e["term"]: e for e in json.loads((ROOT / "glossary.json").read_text())}
    checks = (folder / "review/checks.txt").read_text().strip() if (folder / "review/checks.txt").exists() else "(check_lesson.py has not been run)"
    h_now = content_hash(folder, part)
    stamp_key = f"{content_hash(folder)} exercises {content_hash(folder, 'exercises')}"
    out = (f"# Packet: {lid} — {meta['title']} ({courses.course_of(lid)}, {courses.lang_of(folder)})\n"
           + (f"Part: **exercises** (`{courses.exercise_dir(folder).relative_to(ROOT)}/`, reviewed apart from the lesson).\n" if part == "exercises" else "")
           + f"Role: **visual** (visual & editorial reviewer, `.claude/agents/visual-editorial-reviewer.md`). Mode: **{mode}**. Content hash now: `{h_now}`.\n"
           f"House rules: `CLAUDE.md` (in your context; if it is not, read it). Why this mode: {sc['why']}.\n"
           f"\n## Glossary terms of this chapter (use them, consistently)\n" + "\n".join(f"- **{t}**: {gl[t]['definition']}" for t in meta.get("glossary", []) if t in gl) + "\n"
           f"\n## Deterministic checks (already run, layout and accessibility included: do not repeat them)\n```\n{checks}\n```\n")
    if mode == "none":
        out += (f"\n## No review needed\nSince the version you passed only this changed: {sc['why']} (categories: {', '.join(sc['categories'])}). "
                f"`python scripts/reviews.py carry {lid}{ex_arg}{lang_arg}` records it.\n")
    else:
        out += visual_rules()
        both = None
        if mode == "delta":
            prev = (review_dir(folder, part) / "visual.md").read_text()
            files = sorted({l[6:] for l in sc["diff"].splitlines() if l.startswith("+++ b/")} | {l[4:].split(":")[0] for l in sc["diff"].splitlines() if l.startswith("--- ") and ":" in l})
            out += (f"\n## Delta review\nYou passed this {'exercise set' if part == 'exercises' else 'lesson'} earlier (report below). Since then only the diff below changed "
                    f"({sc['why']}; categories: {', '.join(sc['categories'])}). Judge the changed text, figures and formulas in their captures, plus enough of the "
                    f"surrounding page to see the layout survived. If that cannot be done reliably, write `ESCALATE: full review needed` as line 3 (verdict FAIL) and stop.\n"
                    f"\nChanged files: {', '.join(f'`{x}`' for x in files) or '(see the diff)'}\n\n### Your previous report\n```\n{prev.strip()}\n```\n"
                    f"### Changes since the version you passed (figure bodies included; open the captures to judge them)\n```diff\n{sc['diff'].strip()}\n```\n")
        else:
            both = part == "lesson" and scope(folder, "exercises")["visual"]["mode"] == "full"
            names = ["lesson.md", "inquiry.json", "exit-ticket.json"] if part == "lesson" else []
            if part == "exercises" or both: names += ["exercises.json", "solutions.md"]
            out += "\n## The text you judge (figure bodies collapsed)\n" + "".join(collapsed(courses.lesson_file(folder, n)) for n in names)
            out += figure_inventory([courses.lesson_file(folder, n) for n in names if n.endswith(".md")])
            out += figures_used(folder, "visual", ("inquiry.json", "exit-ticket.json", "exercises.json") if (part == "exercises" or both) else ("inquiry.json", "exit-ticket.json"))
            both = (f"exercises/review/visual.md", f"python3 scripts/reviews.py hash {lid} --exercises{lang_arg}") if both else None
        out += shots_visual(folder / "review", stamp_key, f"python3 scripts/screenshot.py {lid} --if-stale")
        out += visual_report_rules(f"{'exercises/' if part == 'exercises' else ''}review/visual.md", f"python3 scripts/reviews.py hash {lid}{ex_arg}{lang_arg}", both)
    f = review_dir(folder, part) / "packet-visual.md"; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


def item_packet(iid, lang=courses.SOURCE_LANG):
    """The visual packet of an investigation, a TVT guide or a Sovella set (<COURSE>-sovella). These have no carry rows,
    so a review is full unless the visual report already passes the current hash."""
    import guides, investigations, practice
    if iid.endswith("-sovella"):
        code = iid[:-len("-sovella")]; kind, folder, st = "Sovella itsenäisesti", practice.folder(code, lang), practice.status(code, lang)
        names, hash_cmd = ["tasks.json", "solutions.md"], f"python3 scripts/practice.py hash {code}"
    elif iid in investigations.ids(lang):
        kind, folder, st = "experimental investigation", investigations.folder(iid, lang), investigations.status(iid, lang)
        names, hash_cmd = ["investigation.json", "investigation.md", "teacher.md"], f"python3 scripts/investigations.py hash {iid}"
    elif iid in guides.ids(lang):
        kind, folder, st = "TVT guide", guides.folder(iid, lang), guides.status(iid, lang)
        names, hash_cmd = ["guide.json", "guide.md"], f"python3 scripts/guides.py hash {iid}"
    else: sys.exit(f"{iid}: not a lesson, an investigation, a TVT guide or <COURSE>-sovella")
    if lang != courses.SOURCE_LANG: hash_cmd += f" --lang {lang}"
    mode = "none" if st["reports"]["visual"] == "PASS" else "full"
    out = (f"# Packet: {iid} ({kind}, {lang})\nRole: **visual** (`.claude/agents/visual-editorial-reviewer.md`). Mode: **{mode}**. Content hash now: `{st['hash']}`.\n"
           f"House rules: `CLAUDE.md` (in your context). This is not a lesson: no inquiry stages, no exercises; judge the page as the {kind} it is "
           f"(an investigation: the student's working instructions by working mode, the figures and set-up sketches, the data tables and graphs, the teacher's notes; "
           f"a guide: the screenshots of the software are the school's own and are judged for legibility and fit, not redrawn).\n")
    if mode == "none": out += "\n## No review needed\nYour PASS is for the current hash.\n"
    else:
        out += visual_rules() + "\n## The text you judge (figure bodies collapsed)\n" + "".join(collapsed(folder / n) for n in names)
        out += figure_inventory([folder / n for n in names if n.endswith(".md")])
        out += shots_visual(folder / "review", st["hash"], f"python3 scripts/screenshot.py {iid} --if-stale") + visual_report_rules(f"{folder.relative_to(ROOT)}/review/visual.md", hash_cmd)
    f = folder / "review" / "packet-visual.md"; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


def batch_diff(diff, role, headings_only=True):
    """The part of a lesson's diff a batch reviewer reads: restyled figure lines are counted, not shown (the pedagogy
    reviewer sees them in the captures, the science reviewer need not); the science reviewer gets only the headings."""
    keep, svg = [], 0
    for l in diff.splitlines():
        body = l[1:] if l[:1] in "+- " and not l.startswith(("+++", "---")) else None
        if body is not None and SVG_LINE.match(body):
            svg += l[:1] in "+-"; continue
        if role == "science" and headings_only and body is not None and not body.startswith("## "): continue
        keep.append(l)
    return "\n".join(keep).strip() + (f"\n# ({svg // 2} figure line(s) restyled, not shown: see the captures)" if svg else "")


def batch(ids, role, lang=courses.SOURCE_LANG):
    """One delta packet for many lessons (module docstring)."""
    out = (f"# Batch packet: delta {role} review of {len(ids)} lessons\nRole: **{role}**. Mode: **delta (batch)**. House rules: `CLAUDE.md` "
           f"(in your context; if it is not, read it), in particular \"Lesson page\" (2026-10-26).\n")
    if role == "science": out += guardrails()
    if role == "visual": out += visual_rules()
    if role == "pedagogy": out += "\n" + "\n".join(l for l in sections("NOTES.md", "3. Lesson form (human decisions 2026-10-25)").splitlines() if any(k in l for k in ("Figures.", "Textbook illustrations", "Opening illustration")) or l.startswith("  ")) + "\n"
    lang_arg = "" if lang == courses.SOURCE_LANG else f" --lang {lang}"
    folders = {lid: courses.find_lesson(lid, lang) for lid in ids}
    cats = {c for lid in ids for c in scope(folders[lid])[role]["categories"]}
    goals_only = cats == {"objective-form"}
    heading = ("\"In this lesson, you will learn to\" as natural English (a bare verb: \"calculate …\")" if lang == "en" else
               "\"Tällä tunnilla opit\" (a lowercase -maan/-mään verb, parallel forms: \"laskemaan … ja selittämään …\")"
               + ("; Selkeä suomi: short and plain, the key terms kept" if lang == "fi-easy" else ""))
    judge = (f"only the learning goals (`learn`) changed: each must complete the page's heading {heading}, and say the same as before: "
             "the same skill, the same demand, the same physics (NOTES.md §8 \"The opening\")." if goals_only else
             "is every claim the diff changes or adds right by the physics guardrails below, worded as the rest of the lesson and the chapters it builds on say it, and does every changed choice still have exactly one correct option with feedback that says why the others are wrong?"
             if role == "science" else
             "are the changed figures, formulas and sentences of publication quality in their captures (the standard above): legible at 390 px, consistent with the rest of "
             "the chapter, mathematical typography right, natural Finnish, nothing clipped? Open the listed captures; a review without looking cannot pass."
             if role == "visual" else
             "is the changed text clear to a 16–19-year-old, in good language, consistent with the rest of the lesson and with the tasks, feedback and solutions it touches; "
             "where the change is a law's name, a simulation's lead and boxes or recoloured figures: is the name clear, does the lead say what to do, do the figures read well (captures listed per lesson) with colour that carries the physics, never alone?")
    out += ("\n## What you judge\nEach lesson below passed your review earlier; only its diff changed. Judge the diff in its context (the files are on disk "
            "if you need more): " + judge
            + " If one lesson's change cannot be judged this way, write `ESCALATE: full review needed` as line 3 of that lesson's report (verdict FAIL) and go on.\n"
            "\n## Reports: one per lesson\nFor every lesson below write `<its folder>/review/" + role + ".md`, under 250 words: line 1 `VERDICT: PASS` or "
            "`VERDICT: FAIL`, line 2 `CONTENT-HASH: <python3 scripts/reviews.py hash <id>" + lang_arg + ">` (run it at the start and the end for every lesson: if it changed, "
            "that lesson was edited, redo it), then `## Blocking` (FAIL if and only if non-empty), `## Polish` (at most three), `## Checked` (one line: \"batch delta review: ...\"). "
            "Never edit a lesson file.\n")
    skipped = []
    for lid in ids:
        folder = folders[lid]; sc = scope(folder)[role]
        if sc["mode"] != "delta": skipped.append(f"{lid} ({sc['mode']}: {sc['why']})"); continue
        meta = json.loads((folder / "meta.json").read_text())
        out += f"\n## {lid} — {meta['title']}\nFolder `{folder.relative_to(ROOT)}`. Changed: {sc['why']} (categories: {', '.join(sc['categories'])}).\n"
        if role in ("pedagogy", "visual") and (folder / "review/shots.md").exists():
            rows = [l for l in (folder / "review/shots.md").read_text().splitlines() if re.search(r"-(fig-\d+-390|fig-row-1280|sim-390)", l)]
            out += "Captures (paths relative to the lesson folder):\n" + "\n".join(rows) + "\n"
        styling = set(sc["categories"]) <= {"style", "label-position", "section-name", "illustration", "relocated"}   # the science reviewer needs the text of any other change
        out += f"```diff\n{batch_diff(sc['diff'], role, headings_only=styling)}\n```\n"
    if skipped: out += "\n## Not in this batch\n" + "\n".join(f"- {x}" for x in skipped) + "\n"
    f = ROOT / "review-batch" / f"packet-{role}{'' if lang == courses.SOURCE_LANG else '-' + lang}.md"; f.parent.mkdir(exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {len(ids) - len(skipped)} lessons, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens" + (f"; not in it: {'; '.join(skipped)}" if skipped else ""))


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) in (4, 6) and a[0] == "--batch" and a[2] == "--role" and a[3] in ("science", "pedagogy", "visual"):
        batch(a[1].split(","), a[3], *(a[5:6] if a[4:5] == ["--lang"] else [])); sys.exit(0)
    if len(a) < 3 or a[1] != "--role" or a[2] not in ("science", "pedagogy", "visual", "developer"): sys.exit(__doc__)
    lang = a[a.index("--lang") + 1] if "--lang" in a else courses.SOURCE_LANG   # a translation is a lesson of its own (README "Languages")
    if a[2] == "visual":
        if not any(f.name == a[0] for f in courses.lessons(lang=lang)): item_packet(a[0], lang); sys.exit(0)
        visual_packet(courses.find_lesson(a[0], lang), "exercises" if "--exercises" in a else "lesson"); sys.exit(0)
    if "--audit" in a and "--exercises" not in a: packet(courses.find_lesson(a[0], lang), a[2], audit=True); sys.exit(0)
    (exercise_packet if "--exercises" in a else packet)(courses.find_lesson(a[0], lang), a[2], fix="--fix" in a)
