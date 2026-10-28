---
description: Add, rewrite or fix one lesson's exercises without the lesson text (exercise packets, the exercise set's own reviews) and open a draft pull request
argument-hint: <lesson-id> <what to do, e.g. "3 more level-2 tasks on mixing water"> [--warn 150000] [--limit 250000]
model: sonnet
effort: medium
---
Work on the exercises of lesson $ARGUMENTS. Work in `fysiikkalabra/` (`cd fysiikkalabra` first): every path below is relative to it. The exercise set (`content/fi/<course>/<id>/exercises/`: `exercises.json`, `solutions.md`, and `lessons/<course>/<id>/answers.py`) has its own hash and its own two reviews (`exercises/review/`, README "Exercises", teacher 2026-10-28), so this run never touches the lesson's files or reviews, and the lesson stays on the site while the new exercises wait for review: the page keeps the exercises last reviewed. You coordinate; the agents work from packets. Read only the scripts' output and the agents' reports; never open a packet, the lesson text or an exercise file yourself.

**Routing** as in `/lesson` (`.claude/commands/lesson.md`): the developer Sonnet medium (Opus medium only for physics the course has not used before, or after a Sonnet attempt failed the checks twice or a science review found physics errors in its work), the science reviewer Opus medium, the pedagogy reviewer Sonnet medium; pass `model` and `effort` on every Agent call and say in the PR which model ran each step and why. An agent's prompt is one line naming its packet: `Read <path printed by review_packet.py> and follow it. Lesson: <id>. Exercises: <the task in the teacher's words>. Mode: <mode>. Round: <n>.` For a fix, add `Polish to fix: <ids, or none>.` and, after a failed check, the failing lines.

**Budget.** Warning 150 000 and hard limit 250 000 unless `--warn`/`--limit` say otherwise, counted like `/lesson` (the sum of the agents' final context sizes). Past the hard limit, stop safely: commit what exists and open the draft PR with a "Kesken" section.

**Counts.** The levels hold the course's counts (CLAUDE.md "Exercise levels", `curriculum.json` `exercise_levels`), and the lint fails on any other count. If the task asks for more tasks than that, stop before step 1 and tell the teacher the counts need changing first.

1. `python scripts/review_packet.py <id> --role developer --exercises`, then the developer. The packet lists the course's figures from `docs/figures/catalog.json` (NOTES.md §11): a task that needs a picture reuses one by id or a variant of it; after any figures.py change run `python scripts/figcat.py build` and commit the catalog.
2. `python scripts/check_lesson.py <id>` (lint with the complete-solution rules, LaTeX, build, layout with every solution open at 360, 768 and 1280 px). On FAIL run the developer with `--role developer --exercises --fix` and the failing lines; at most twice.
3. `python scripts/screenshot.py <id>`, then `python scripts/reviews.py scope <id> --exercises`. A reviewer whose mode is `none` is not run: `python scripts/reviews.py carry <id> --exercises`. For the others `python scripts/review_packet.py <id> --role science --exercises` / `--role pedagogy --exercises` and the two reviewers in parallel. Then `python scripts/reviews.py status <id>`.
4. If the exercises are `reviewed`: go to 6. ESCALATE and FAIL as in `/lesson` step 4 (classify A/B/C, the developer `--exercises --fix` names the A and B Polish items), then from step 2. At most three review rounds.
5. Commit after each round's reviews and before a fix: `git add content lessons && git commit -m "fysiikkalabra: <id> exercises round <n>"`.
6. Finish: `python scripts/usage.py collect <id> --round <n>`, `python scripts/build.py --all`, `python scripts/build.py`, commit `site/` and the reviews, push the branch `claude/exercises-<id>`, and open or update the draft pull request: **Tehtävät** (id, what was added or changed, level by level); **Tarkistukset** (the last `check_lesson.py` lines, the exercise verdicts with hashes, carried-over reviews and why, CI link); **Kierrokset**; **Kulutus** (`python scripts/usage.py report <id>` and the model of each step); **Vaikutus** (`python scripts/reviews.py impact origin/main`: it must name only `<id> exercises`); **Avoimet kohdat**. Merging is the teacher's publication decision: never merge, never push to `main`.

**Many lessons.** For exercise work on several lessons, run this command per lesson; when the reviews are all delta reviews of the same kind, one reviewer of each kind may take them together as in `/lesson` "Batch".

**Learning loop** as in `/lesson`: a recurring, testable finding gets a check (`lint_lesson.py`, `check_solutions.py`) with a test; otherwise one dated line in `NOTES.md`.
