---
description: Write or rework a course's Esimerkkikoe (example exam with sections, selection rules, multiple choice, worked solutions and rubrics) from a small packet, review it and open a draft pull request
argument-hint: <COURSE> <what to do, e.g. "write the exam" or "replace Osa 2 task 3 with a data task">
model: sonnet
effort: medium
---
Work on the example exam of $ARGUMENTS. Work in `fysiikkalabra/` (`cd fysiikkalabra` first). The exam is a task set of
its own, key `<COURSE>/koe` (README "Esimerkkikoe"): `content/fi/<COURSE>/koe/` (tasks.json, solutions.md, review/) and
`lessons/<COURSE>/koe/` (answers.py, figures.py). The design brief is `docs/exam-guidelines.md`; it is the only exam
material any agent reads. **Never** read, copy, paraphrase or mention a teacher's own reference exam in this run, a
packet, a review, a commit, a PR or memory.

**When.** Once per course, after its lessons and Sovella itsenäisesti are published. The same flow as `/practice`, with
the key `<COURSE>/koe` and the page id `<COURSE>-koe`:

1. `python scripts/practice.py packet <COURSE>/koe --role developer`, then the developer (Sonnet medium; Opus for a
   demanding course) writes the four files.
2. `python scripts/practice.py figures <COURSE>/koe`, `python scripts/practice.py check <COURSE>/koe`,
   `python scripts/build.py <COURSE>-koe`, `python scripts/check_layout.py <COURSE>-koe --width 360` (768, 1280).
3. `python scripts/screenshot.py <COURSE>-koe --if-stale`, then the packets `--role science` (Opus), `--role pedagogy`
   and `--role visual` (Sonnet), the reviewers in parallel; at most three rounds of fixes.
4. Before committing: list the staged files and read the staged diff; confirm no reference exam, extract or paraphrase
   is in it. Then `python scripts/build.py --all`, `python scripts/build.py`, commit, push and open a draft PR
   (**Koe** with each task, its points and competencies, **Tarkistukset**, **Luottamuksellisuus**, **Avoimet kohdat**).
   Merging is the teacher's decision.
