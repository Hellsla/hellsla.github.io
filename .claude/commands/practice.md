---
description: Write or rework a course's module-end "Sovella itsenäisesti" tasks (worked solutions, rubrics) from a small packet, review them and open a draft pull request
argument-hint: <COURSE> <what to do, e.g. "write the tasks" or "replace task 2 with a data task on pressure"> [--warn 120000] [--limit 200000]
model: sonnet
effort: medium
---
Work on the Sovella itsenäisesti tasks of $ARGUMENTS. Work in `fysiikkalabra/` (`cd fysiikkalabra` first). The tasks are a part of their own (README "Sovella itsenäisesti", NOTES.md §9, teacher 2026-10-28): `content/fi/<COURSE>/sovella/` (tasks.json, solutions.md, review/) and `lessons/<COURSE>/sovella/` (answers.py, figures.py). This run never touches lesson files or their reviews. You coordinate; agents work from packets, and you read only the scripts' output and the agents' reports.

**When.** Once per course, after its lessons, as part of producing the course: 2–4 tasks (FY1 about 2, later courses about 3), each 12–20 points, plus at most one `own` rubric for the course's own investigation. Fewer, better tasks; never relabel chapter exercises. **Token economy**: no lesson texts in any packet; shared criteria by key; translate only new or changed text.

**Routing** as in `/lesson`: developer Sonnet medium (Opus medium for a demanding physics model or after two failed checks), science reviewer Opus medium, pedagogy reviewer Sonnet medium. Prompt: `Read <packet path> and follow it. Course: <COURSE>. Task: <the teacher's words>. Round: <n>.`

1. `python scripts/practice.py packet <COURSE> --role developer`, then the developer.
2. `python scripts/practice.py figures <COURSE>`, `python scripts/practice.py check <COURSE>`, `python scripts/build.py <COURSE>-sovella`, `python scripts/check_layout.py <COURSE>-sovella --width 360` (and 768, 1280). On FAIL the developer fixes, at most twice.
3. `python scripts/practice.py packet <COURSE> --role science` and `--role pedagogy`, the two reviewers in parallel; then `python scripts/practice.py status`.
4. FAIL: the developer fixes the Blocking items, then from step 2; at most three rounds.
5. Finish: `python scripts/coverage.py <COURSE>`, `python scripts/build.py --all`, `python scripts/build.py`, commit content, reviews, `docs/coverage/` and `site/`, push and open or update a draft PR: **Tehtävät** (each task, its competencies and points), **Tarkistukset**, **Kattavuus** (the gaps of docs/coverage/<COURSE>.md), **Kulutus**, **Avoimet kohdat**. Merging is the teacher's decision.
