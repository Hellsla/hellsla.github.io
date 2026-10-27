"""Role-specific packet, so an agent starts from what its role needs and nothing else.

  python scripts/review_packet.py <id> --role science|pedagogy|developer [--fix]
  python scripts/review_packet.py --batch <id>,<id>,... --role science|pedagogy

Writes review/packet-<role>.md and prints its path, mode and size. The orchestrator never reads it: the agent's prompt
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
whose change needs a full review, or none, is left out and named."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses
from reviews import ROOT, find_lesson, content_hash, scope, SVG_LINE

SVG = re.compile(r"(<svg\b[^>]*>).*?(</svg>)", re.S)
LESSON_FILES = ("meta.json", "lesson.md", "inquiry.json", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim-spec.md", "sim.js")


def sections(path, *names):
    """The named '## ' sections of a markdown file."""
    if not (ROOT / path).exists(): return ""
    text = (ROOT / path).read_text(); out = []
    for name in names:
        m = re.search(rf"^## {re.escape(name)}.*?(?=^## |\Z)", text, re.S | re.M)
        if m: out.append(m.group(0).strip())
    return "\n\n".join(out)


def block(path, label=None, collapse_svg=False):
    if not path.is_file(): return ""
    text = path.read_text()
    if collapse_svg: text = SVG.sub(lambda m: f"{m.group(1)}\n  <!-- figure body omitted: see the figure captures in review/shots.md -->\n{m.group(2)}", text)
    lang = {".json": "json", ".py": "python", ".js": "js", ".css": "css"}.get(path.suffix, "markdown")
    return f"\n### {label or path.name}\n```{lang}\n{text.rstrip()}\n```\n"


def sim_code(folder, meta):
    """[(label, path)] of the simulation's text files (sim.js, sim.css...), wherever the course keeps them."""
    d = courses.sim_dir(folder, meta)
    if d is None: return []
    if d[0] == "lesson": return [("sim.js", folder / "sim.js")]
    return [(f"{p.relative_to(ROOT).as_posix()}", p) for p in sorted(d[1].rglob("*")) if p.is_file() and p.suffix in (".js", ".css", ".json", ".md")]


def header(folder, role, mode):
    meta = json.loads((folder / "meta.json").read_text())
    lid = folder.name; c = courses.course(courses.course_of(lid)); s = courses.slot(lid)
    titles = {l["id"]: l["title"] for k in courses.codes() for l in courses.curriculum()[k].get("lessons", [])}
    gl = {e["term"]: e for e in json.loads((ROOT / "glossary.json").read_text())}
    terms = [gl[t] for t in meta.get("glossary", []) if t in gl]
    checks = (folder / "review/checks.txt").read_text().strip() if (folder / "review/checks.txt").exists() else "(check_lesson.py has not been run)"
    bullets = lambda xs: "\n".join(f"- {x}" for x in xs)
    out = (f"# Packet: {lid} — {meta['title']} ({c['code']} {c['title']})\n"
           f"Role: **{role}**. Mode: **{mode}**. Content hash now: `{content_hash(folder)}`.\n"
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
    sim_line = ("none" if d is None else f"`{(folder / 'sim.js').relative_to(ROOT)}` (lesson folder, FY3 layout)" if d[0] == "lesson"
                else f"`{d[1].relative_to(ROOT)}/` ({d[0]}; used by {', '.join(users) or lid})")
    out += (f"\n## Assets\nSimulation: {sim_line}. Pictures folder of the course: `{c['paths']['pics'].relative_to(ROOT)}/` "
            f"(text refers to `pics/{c['slug']}/<file>`); pictures this lesson uses: {', '.join(courses.pic_refs(folder)) or 'none'}.\n"
            f"\n## Deterministic checks (already run: do not repeat them)\n```\n{checks}\n```\n")
    return out, meta


def shots(folder, role):
    f = folder / "review" / "shots.md"
    if not f.exists(): return "\n## Screenshots\n(none yet: the orchestrator runs python scripts/screenshot.py first)\n"
    rows = [l for l in f.read_text().splitlines() if l.startswith("| review/")]
    if role == "science": rows = [l for l in rows if re.search(r"-(fig-\d+|sim|exp-[^|]*)-\d+", l)]   # what carries physics: figures, the sim, experiments
    return ("\n## Screenshots (open only what your questions need, with the Read tool; paths relative to the lesson folder)\n"
            "| file | shows | px | ≈ tokens |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")


def reviewer_rules(role, lid):
    what = ("1. Every formula: correct, conditions stated, inside the course's central contents and scope notes above.\n2. Units, magnitudes, signs; nothing unrealistic.\n"
            "3. answers.py: each line computes the right physics from the task text; recompute all answers in ONE python call and compare.\n"
            "4. solutions.md, every numeric task's solution and the worked example: complete (NOTES §3 Complete solutions), reasoning right, the stated principle really applies and its reason is right, unknown solved symbolically before substitution, conversions right, rounding justified, the reasonableness check a real check.\n"
            "5. Figures (SVG numbers) and the simulation code: physically correct, the sim implements the lesson's model, its limits are said, nothing misleads.\n"
            "6. inquiry.json: every correct option, every feedback's physics and numbers, each experiment's setup isolates its varied parameter."
            if role == "science" else
            "1. Learning path: a 17-year-old with only the prerequisites can follow; the opening question is answered; the slot's goals, no more.\n"
            "2. The activities fit the topic: predictions before evidence where the topic allows, an investigation, data, a graph or a model that the student acts on; no simulation or game for its own sake; workload one lesson.\n"
            "3. Lesson form: figures next to the paragraphs they explain and legible in their captures; no wall of text; staged example, one step per stage.\n"
            "4. Exercises: levels per the rubric; none repeats the example; feedback repairs misconceptions; the exit ticket tests the core idea; every solution can be followed step by step by a student who could not solve the task (the principle explained, not just named; nothing skipped).\n"
            "5. Finnish: grammar, glossary terms, case after number+unit (80 N:n voimalla), reading level; give the corrected sentence.\n"
            "6. Phone usability from the captures: nothing clipped, controls and readout understandable. The inquiry mechanics (gating, locking, "
            "reveal, option feedback, 360 px) are already tested (checks above); open the preview in Playwright only for what a capture cannot show, "
            "such as whether the simulation makes sense when you move it.")
    return (f"\n## What you judge (only this; the deterministic checks above are not repeated)\n{what}\n\n"
            f"## Report: write `review/{role}.md`, under 400 words, findings only\n"
            f"Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of python3 scripts/reviews.py hash {lid}>` run at the start and again at the end "
            f"(if it changed, the lesson was edited: redo the review). Then `## Blocking` (FAIL if and only if non-empty; each `file:line — problem — fix`), "
            f"`## Polish` (at most five, same format; language, style and taste go here, never under Blocking), `## Checked` (at most ten one-line items). "
            f"Never edit a lesson file. Read nothing the packet already gives you; investigate what the judgement needs.\n")


def packet(folder, role, fix=False):
    lid = folder.name
    if role in ("science", "pedagogy"):
        sc = scope(folder)[role]; mode = sc["mode"]
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
                if role == "science":
                    for n in ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim-spec.md"): out += block(folder / n)
                    for label, p in sim_code(folder, meta): out += block(p, label)
                else:
                    for n in ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "exit-ticket.json", "sim-spec.md"): out += block(folder / n, collapse_svg=(n == "lesson.md"))
            out += shots(folder, role) + reviewer_rules(role, lid)
    else:
        mode = "fix" if fix else "draft"
        out, meta = header(folder, role, mode)
        c = courses.course(courses.course_of(lid)); d = courses.sim_dir(folder, meta)
        has_sim = d is not None or (folder / "sim-spec.md").exists() or meta.get("sim")
        out += "\n## Rules (NOTES.md; CLAUDE.md is in your context)\n" + sections("NOTES.md", "1. Maths in LaTeX", "2. Numbers, Finnish, scope", "3. Lesson form (human decisions 2026-10-25)", "5. Inquiry sequence (teacher's brief 2026-10-25)") + "\n"
        if has_sim: out += "\n" + sections("NOTES.md", "4. Simulations and pages") + "\n"
        own = c["paths"]["sims"] / lid
        out += (f"\n## Where files go\n- lesson files: `{folder.relative_to(ROOT)}/` (meta.json, lesson.md, inquiry.json, exercises.json, solutions.md, answers.py, exit-ticket.json, sim-spec.md)\n"
                f"- simulation: " + (f"`{folder.relative_to(ROOT)}/sim.js` (this course keeps sims in lesson folders)" if c.get("lesson_folder_sims")
                                     else f"`{own.relative_to(ROOT)}/sim.js` with its own `sim.css` and images when it has them (meta.json `\"sim\": true`); "
                                          f"images load from `document.getElementById('sim-root').dataset.base`") + "\n"
                f"- tests: `tests/sims/{lid}.json`; pictures: `{c['paths']['pics'].relative_to(ROOT)}/<file>`, referred to as `pics/{c['slug']}/<file>`; new glossary terms: `glossary.json`\n")
        if fix:
            out += "\n## Findings to resolve (every Blocking item; Polish items only when the orchestrator lists them)\n"
            for n in ("science", "pedagogy"):
                f = folder / "review" / f"{n}.md"
                if f.exists(): out += f"### {n}\n```\n{f.read_text().strip()}\n```\n"
        else:
            sims = sorted(p for p in c["paths"]["sims"].iterdir() if p.is_dir()) if c["paths"]["sims"].is_dir() else []
            deps = courses.deps()
            if sims:
                out += "\n## Simulations this course already has (reuse one when its model fits: meta.json `\"sim\": \"<name>\"`; changing one re-opens the review of every lesson that uses it)\n"
                out += "\n".join(f"- `{p.relative_to(ROOT)}/` used by {', '.join(deps.get(f'sims/{c['slug']}/{p.name}', [])) or 'none'}" for p in sims) + "\n"
            out += "\n## Reference lesson (content/_gold; for the inquiry shape see content/FY3/fy3-2/inquiry.json, not to be copied mechanically)\n" + block(ROOT / "content/_gold/lesson.md")
        files = [(n, folder / n) for n in LESSON_FILES] + [(label, p) for label, p in sim_code(folder, meta) if label != "sim.js"] + [(f"tests/sims/{lid}.json", ROOT / "tests/sims" / f"{lid}.json")]
        out += "\n## The lesson's files now (open the ones your task touches; Edit needs a Read first)\n" + "\n".join(
            f"- `{p.relative_to(ROOT)}` ({p.stat().st_size} bytes)" for n, p in files if p.is_file()) + "\n"
        out += block(folder / "meta.json")
        out += ("\n## Your task\n" + ("Resolve every Blocking finding and exactly the Polish items the orchestrator lists; change nothing else, so the reviewers judge a small diff. "
                                      if fix else "Draft the lesson for its slot. Choose the activities the topic needs (an experiment on a simulation only when manipulating it reveals something; otherwise data, a graph, competing explanations or a model to build). ")
                + "When a number changes, change answers.py first. Never loosen a simulation test. "
                f"Finish with `python3 scripts/check_lesson.py {lid}` until every line is ok, then write review/developer.md (`VERDICT: DONE` or `VERDICT: BLOCKED` + reason, what changed per file, ≤ 200 words).\n")
    f = folder / "review" / f"packet-{role}.md"; f.parent.mkdir(exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


def batch_diff(diff, role):
    """The part of a lesson's diff a batch reviewer reads: restyled figure lines are counted, not shown (the pedagogy
    reviewer sees them in the captures, the science reviewer need not); the science reviewer gets only the headings."""
    keep, svg = [], 0
    for l in diff.splitlines():
        body = l[1:] if l[:1] in "+- " and not l.startswith(("+++", "---")) else None
        if body is not None and SVG_LINE.match(body):
            svg += l[:1] in "+-"; continue
        if role == "science" and body is not None and not body.startswith("## "): continue
        keep.append(l)
    return "\n".join(keep).strip() + (f"\n# ({svg // 2} figure line(s) restyled, not shown: see the captures)" if svg else "")


def batch(ids, role):
    """One delta packet for many lessons (module docstring)."""
    out = (f"# Batch packet: delta {role} review of {len(ids)} lessons\nRole: **{role}**. Mode: **delta (batch)**. House rules: `CLAUDE.md` "
           f"(in your context; if it is not, read it), in particular \"Lesson page\" (2026-10-26).\n")
    if role == "pedagogy": out += "\n" + "\n".join(l for l in sections("NOTES.md", "3. Lesson form (human decisions 2026-10-25)").splitlines() if "Figures." in l or "Textbook illustrations" in l or l.startswith("  ")) + "\n"
    out += ("\n## What you judge\nEach lesson below passed your review earlier; only its diff changed. Judge the diff in its context (the files are on disk "
            "if you need more): " + ("is the formula section named after the right law, and does nothing in the diff change the physics?"
                                     if role == "science" else
                                     "is the law's name clear to a student; does the lead of the simulation say what to do and do its boxes hold the rest under fitting names; "
                                     "do the recoloured figures read well (captures listed per lesson), with colour that carries the physics, never alone, and labels legible?")
            + " If one lesson's change cannot be judged this way, write `ESCALATE: full review needed` as line 3 of that lesson's report (verdict FAIL) and go on.\n"
            "\n## Reports: one per lesson\nFor every lesson below write `<its folder>/review/" + role + ".md`, under 250 words: line 1 `VERDICT: PASS` or "
            "`VERDICT: FAIL`, line 2 `CONTENT-HASH: <python3 scripts/reviews.py hash <id>>` (run it at the start and the end for every lesson: if it changed, "
            "that lesson was edited, redo it), then `## Blocking` (FAIL if and only if non-empty), `## Polish` (at most three), `## Checked` (one line: \"batch delta review: ...\"). "
            "Never edit a lesson file.\n")
    skipped = []
    for lid in ids:
        folder = find_lesson(lid); sc = scope(folder)[role]
        if sc["mode"] != "delta": skipped.append(f"{lid} ({sc['mode']}: {sc['why']})"); continue
        meta = json.loads((folder / "meta.json").read_text())
        out += f"\n## {lid} — {meta['title']}\nFolder `{folder.relative_to(ROOT)}`. Changed: {sc['why']} (categories: {', '.join(sc['categories'])}).\n"
        if role == "pedagogy" and (folder / "review/shots.md").exists():
            rows = [l for l in (folder / "review/shots.md").read_text().splitlines() if re.search(r"-(fig-\d+-390|fig-row-1280|sim-390)", l)]
            out += "Captures (paths relative to the lesson folder):\n" + "\n".join(rows) + "\n"
        out += f"```diff\n{batch_diff(sc['diff'], role)}\n```\n"
    if skipped: out += "\n## Not in this batch\n" + "\n".join(f"- {x}" for x in skipped) + "\n"
    f = ROOT / "review-batch" / f"packet-{role}.md"; f.parent.mkdir(exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {len(ids) - len(skipped)} lessons, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens" + (f"; not in it: {'; '.join(skipped)}" if skipped else ""))


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 4 and a[0] == "--batch" and a[2] == "--role" and a[3] in ("science", "pedagogy"): batch(a[1].split(","), a[3]); sys.exit(0)
    if len(a) < 3 or a[1] != "--role" or a[2] not in ("science", "pedagogy", "developer"): sys.exit(__doc__)
    packet(find_lesson(a[0]), a[2], fix="--fix" in a)
