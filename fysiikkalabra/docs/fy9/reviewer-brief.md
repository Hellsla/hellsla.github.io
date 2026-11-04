# FY9 — brief for a unit reviewer (science, pedagogy, or visual & editorial)

Work in `fysiikkalabra/`. Your prompt names your role and the unit to review.

## Read first
1. Your role file: `../.claude/agents/<science-reviewer|pedagogy-reviewer|visual-editorial-reviewer>.md`. A FY9
   unit is a Finnish lesson of the exam review course. Judge it by the same standard as a FY1–FY8 chapter.
2. `docs/FY9_PLAN.md` (the course and the lesson form table) and `docs/fy9/developer-brief.md` (the rules the
   developer followed; they are part of the standard). Also read `docs/EDITORIAL_QUALITY_STANDARD.md` and
   `docs/physics-guardrails.md`.

## For each unit
- Sources: `content/fi/units/<id>/` (unit.json, unit.md, inquiry.json, teacher.md, exit-ticket.json, sovella/tasks.json,
  sovella/solutions.md, review/developer.md) and `lessons/units/<id>/` (figures.py, sovella/answers.py, sovella/figures.py).
- Build: `python3 scripts/build.py <id>` → `preview/<id>.html`. Browser: Playwright with `scripts/_browser.launch(pw)`.
  Open every hint, solution, model answer and rubric yourself.
- Science: recompute every number in ONE Python call with your own formulas (answers.py can agree with its solution
  and still use the wrong model). Check each law's conditions, the rounding justification, units and the
  reasonableness checks. The physics must stay inside FY1–FY8 as the chapters teach it.
- Pedagogy: Is it a review, i.e. does it connect ideas across chapters and avoid re-teaching one chapter? Are the
  tasks original and exam-like, with no formula given away? Check the task counts against the plan table, the
  quality of feedback per misconception, option lengths, the skills and chapter links (named, never ids), the
  rubrics (observable criteria, points sum), the 75-minute plan, and the progression from short to long tasks.
- Visual & editorial: captures at 390 and 1280, figures at print quality, LaTeX everywhere, colours (force red,
  velocity blue, acceleration orange), tables at narrow widths, Finnish language.
- Originality: if a task looks like a known YTL or textbook task (same situation and numbers), it is Blocking.

## Output
Write `content/fi/units/<id>/review/<science|pedagogy|visual>.md`, starting exactly
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id>>
```
(or FAIL). Then give numbered findings, Blocking first, then Polish, each with the file, the place and a concrete fix,
in under 600 words. Do not edit anything else and do not commit. Problems in shared files go under "Shared issues".
Report back in under 150 words.
