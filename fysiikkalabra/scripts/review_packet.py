"""Role-specific review packet, so an agent reads nothing from the repository on its own.

  python scripts/review_packet.py <id> --role science|pedagogy|developer [--fix]

Writes review/packet-<role>.md and prints its size. The orchestrator pastes the packet into the agent's prompt.
A reviewer packet is *full* (every file the role judges) or *delta* (its previous report, the diff since the
version it passed, and the surrounding context) as decided by `reviews.py scope`; the reviewer may escalate a
delta to a full review. The developer packet carries the writing rules; with --fix it also carries both reports.
Only what the role needs goes in: the lesson's own curriculum slot and glossary terms, the relevant sections of
CLAUDE.md and NOTES.md, never curriculum.json, glossary.json or tests/sims as a whole."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import ROOT, find_lesson, content_hash, scope

SVG = re.compile(r"(<svg\b[^>]*>).*?(</svg>)", re.S)


def sections(path, *names):
    """The named '## ' sections of a markdown file."""
    if not (ROOT / path).exists(): return ""
    text = (ROOT / path).read_text(); out = []
    for name in names:
        m = re.search(rf"^## {re.escape(name)}.*?(?=^## |\Z)", text, re.S | re.M)
        if m: out.append(m.group(0).strip())
    return "\n\n".join(out)


def file_block(folder, name, collapse_svg=False):
    f = folder / name
    if not f.exists(): return ""
    text = f.read_text()
    if collapse_svg: text = SVG.sub(lambda m: f"{m.group(1)}\n  <!-- figure body omitted: see the screenshot -->\n{m.group(2)}", text)
    lang = "json" if name.endswith(".json") else "python" if name.endswith(".py") else "js" if name.endswith(".js") else "markdown"
    return f"\n### {name}\n```{lang}\n{text.rstrip()}\n```\n"


def header(folder, role, mode):
    meta = json.loads((folder / "meta.json").read_text())
    cur = json.loads((ROOT / "curriculum.json").read_text())
    slot = next((l for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", []) if l["id"] == folder.name), {})
    gl = {e["term"]: e for e in json.loads((ROOT / "glossary.json").read_text())}
    terms = [gl[t] for t in meta.get("glossary", []) if t in gl]
    checks = (folder / "review/checks.txt").read_text() if (folder / "review/checks.txt").exists() else "(check_lesson.py has not been run)"
    return (f"# Review packet: {folder.name} — {meta['title']} ({meta['course']})\n"
            f"Role: **{role}**. Mode: **{mode}**. Content hash now: `{content_hash(folder)}`.\n\n"
            f"## Curriculum slot\n```json\n{json.dumps(slot, ensure_ascii=False, indent=1)}\n```\n"
            f"## Glossary terms of this lesson\n```json\n{json.dumps(terms, ensure_ascii=False, indent=1)}\n```\n"
            f"## Deterministic checks (already run)\n```\n{checks.strip()}\n```\n")


def reviewer_rules(role):
    what = ("1. Every formula: correct, conditions stated, inside the module's scope.\n2. Units, magnitudes, signs; nothing unrealistic.\n"
            "3. answers.py: each line computes the right physics from the task text; recompute all answers in ONE python call and compare.\n"
            "4. solutions.md and the worked example: reasoning right, unknown solved symbolically before substitution.\n"
            "5. Figures (SVG numbers) and sim.js: physically correct, the sim implements the lesson's formula."
            if role == "science" else
            "1. Learning path: a 17-year-old with only the prerequisites can follow; the opening question is answered; the slot's goals, no more.\n"
            "2. Lesson form: figures next to the paragraphs they explain and legible on the phone screenshot; no wall of text; staged example, one step per stage.\n"
            "3. Exercises: levels per the rubric (1: one formula, values given; 2: two steps or a conversion; 3: reasoning); none repeats the example; exit ticket tests the core idea.\n"
            "4. Finnish: grammar, glossary terms, case after number+unit (80 N:n voimalla), reading level; give the corrected sentence.\n"
            "5. Phone usability from the screenshots: nothing clipped, controls and readout understandable, the simulation visually rich and helpful.")
    return (f"## What you judge (only this; the deterministic checks above are not repeated)\n{what}\n\n"
            f"## Report: write `review/{role}.md`, under 400 words, findings only\n"
            f"Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of python3 scripts/reviews.py hash {{id}}>` run at the start and again at the end "
            f"(if it changed, the lesson was edited: redo the review). Then `## Blocking` (FAIL if and only if non-empty; each `file:line — problem — fix`), "
            f"`## Polish` (at most five, same format; language, style and taste go here, never under Blocking), `## Checked` (at most ten one-line items). "
            f"Never edit a lesson file. Read nothing the packet already gives you; investigate what the judgement needs.\n")


def packet(folder, role, fix=False):
    lid = folder.name
    if role in ("science", "pedagogy"):
        sc = scope(folder)[role]
        mode = sc["mode"]
        out = header(folder, role, mode)
        out += "## Conventions\n" + sections("CLAUDE.md", "Physics and maths conventions", "Lesson form (human decisions 2026-10-25, every lesson)", "Exercise levels") + "\n\n"
        if mode == "delta":
            prev = (folder / "review" / f"{role}.md").read_text()
            out += (f"## Delta review\nYou passed this lesson earlier (report below). Since then only the diff below changed ({sc['why']}). "
                    f"Judge the diff in its context; the rest of the lesson is as you approved it (the current files are on disk if you need more context). If the change cannot be judged reliably this way, "
                    f"write `ESCALATE: full review needed` as line 3 of your report (verdict FAIL) and stop.\n\n### Your previous report\n```\n{prev.strip()}\n```\n"
                    f"### Changes since the version you passed\n```diff\n{sc['diff'].strip()}\n```\n")
        else:
            if sc["why"] not in ("no earlier PASS",): out += f"## Full review\nReason: {sc['why']}.\n"
            if role == "science":
                for n in ("lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim-spec.md", "sim.js"): out += file_block(folder, n)
                shots = [p.relative_to(ROOT) for p in sorted((folder / "review").glob(f"{lid}-sim-*.png"))]
                if shots: out += "\n### Simulation screenshots (open with the Read tool when the drawing matters)\n" + "\n".join(f"- {p}" for p in shots) + "\n"
            else:
                for n in ("lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim-spec.md"): out += file_block(folder, n, collapse_svg=(n == "lesson.md"))
                shots = [p.relative_to(ROOT) for p in sorted((folder / "review").glob(f"{lid}-*.png"))]
                out += "\n### Screenshots (open with the Read tool)\n" + ("\n".join(f"- {p}" for p in shots) if shots else "(none: run python scripts/screenshot.py first)") + "\n"
        out += "\n" + reviewer_rules(role).replace("{id}", lid)
    else:
        mode = "fix" if fix else "draft"
        out = header(folder, role, mode)
        out += "## Rules\n" + sections("CLAUDE.md", "Physics and maths conventions", "Lesson form (human decisions 2026-10-25, every lesson)", "Exercise levels", "Lesson folder") + "\n\n"
        out += sections("NOTES.md", "1. Maths in LaTeX", "2. Numbers, Finnish, scope", "3. Lesson form (human decisions 2026-10-25)") + "\n\n"
        if (folder / "sim-spec.md").exists() or (folder / "sim.js").exists(): out += sections("NOTES.md", "4. Simulations and pages") + "\n\n"
        if fix:
            out += "## Findings to resolve (every Blocking item; Polish items only when the orchestrator lists them)\n"
            for n in ("science", "pedagogy"):
                f = folder / "review" / f"{n}.md"
                if f.exists(): out += f"### {n}\n```\n{f.read_text().strip()}\n```\n"
        else:
            out += "## Reference lesson (content/_gold)\n" + file_block(ROOT / "content/_gold", "lesson.md")
        for n in ("meta.json", "lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim-spec.md", "sim.js"): out += file_block(folder, n)
        out += ("\n## Your task\nEdit only the lesson folder, tests/sims/<id>.json and glossary.json. When a number changes, change answers.py first. "
                "Finish with `python3 scripts/check_lesson.py <id>` until every line is ok, then write review/developer.md (`VERDICT: DONE` or `VERDICT: BLOCKED` + reason, what changed per file, ≤ 200 words).\n")
    f = folder / "review" / f"packet-{role}.md"; f.parent.mkdir(exist_ok=True); f.write_text(out)
    print(f"{f.relative_to(ROOT)}: {mode}, {len(out.encode())} bytes ≈ {len(out.encode()) // 4} tokens")
    return mode


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 3 or a[1] != "--role" or a[2] not in ("science", "pedagogy", "developer"): sys.exit(__doc__)
    packet(find_lesson(a[0]), a[2], fix="--fix" in a)
