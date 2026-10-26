# Fysiikkalabra

A digital textbook for Finnish upper-secondary physics (LOPS 2019): theory, p5.js simulations and exercises,
written and reviewed with Claude Code agents, served by GitHub Pages from the committed `site/` folder at
`https://hellsla.github.io/fysiikkalabra/site/`. House rules for agents: `CLAUDE.md`; writing rules: `NOTES.md`.

## Quick start
```bash
cd fysiikkalabra
pip install markdown playwright && playwright install chromium
python scripts/check_lesson.py fy3-9     # lint, LaTeX, preview build, simulation and inquiry tests, answer positions, 360 px, review state
python scripts/build.py fy3-9            # preview/fy3-9.html (git-ignored), any lesson
python scripts/build.py --all            # preview/ with every lesson, drafts included (what CI tests)
python scripts/build.py                  # site/ from the lessons whose reviews are current (atomic; commit it)
python scripts/reviews.py status         # reviewed | legacy | draft for every lesson, and why
python scripts/reviews.py impact         # which lessons this branch touches and which review each needs
python scripts/test_reviews.py           # tests of the publishing rule
python scripts/test_courses.py           # a temporary FY4 course through the whole pipeline, nothing published
python scripts/usage.py report FY3 --by agent   # tokens and cost per agent and model
```
If the pip `playwright` version does not match the installed browser: `PW_CHROMIUM=/path/to/chrome python scripts/test_sims.py`.

Inside Claude Code, `/lesson fy3-9` runs one lesson through the pipeline (orchestrated on Sonnet): the **developer**
(Sonnet; Opus only for demanding physics or a numerical model) writes or fixes, `check_lesson.py` must pass, the
**science-reviewer** (Opus) and the **pedagogy-reviewer** (Sonnet) judge it independently from packet files, fixes and
re-reviews for at most three rounds, then a draft pull request with a teacher summary and the measured token usage.
Agents live in `.claude/agents/` and the commands in `.claude/commands/` at the repository root (`../.claude/`), so a
session opened at the root, as a cloud session is, finds them; each starts by working in `fysiikkalabra/`.

## A new course
```
/new-course FY4        # scripts/new_course.py FY4: checks curriculum.json against LOPS 2019, creates the folders
/lesson fy4-1          # creates content/FY4/fy4-1/meta.json from the slot, then drafts, checks and reviews it
/lesson fy4-2
```
Everything course-specific comes from the course's entry in `curriculum.json` (LOPS goals and central contents,
lesson slots, `scope_notes`, optional `exercise_levels`); `scripts/courses.py` resolves a lesson id to its course and
folders. Lessons go to `content/FY4/<id>/`, pictures to `assets/pics/fy4/` (text refers to `pics/fy4/<file>`),
simulations to `assets/sims/fy4/<name>/` (published at `sims/fy4/<name>/`), shared assets to `assets/shared/`
(`assets/README.md`). The course page `site/FY4.html` lists the slots and links each lesson once it is reviewed.

## The publishing rule
`scripts/reviews.py` decides what is on the site: a lesson is **reviewed** when `review/science.md` and
`review/pedagogy.md` both say `VERDICT: PASS` with the lesson's current `CONTENT-HASH`. The hash covers the lesson
files, its simulation folder, its pictures and its simulation tests, and ignores only line endings, trailing
whitespace, blank-line runs and JSON layout; build scripts and templates are not content. What changed decides who
reviews again (`reviews.py scope`): a physics change needs the science reviewer in full, a learning-design change the
pedagogy reviewer, simulation code both, a figure's styling only the pedagogy reviewer, comments and tightened tests
neither; a PASS carried over such a change is recorded in `review/carry.tsv` and re-checked by CI. A **legacy**
lesson (`review/legacy.md`, written by `reviews.py legacy <id>` in the migration) was published before the
pipeline and stays visible, labelled as a prototype, until a content edit retires the marker. Everything else
is a **draft** and never reaches `site/`.

Merging a pull request is the teacher's publication decision. CI (`.github/workflows/fysiikkalabra-ci.yml`)
lints every lesson, builds all previews, runs the review and course tests, the simulation tests, every lesson's
inquiry tests, the answer-position check and the LaTeX check, verifies carried reviews from history, lists the
review impact of the branch,
rebuilds `site/` and fails if the committed copy differs, and checks every published page at 360 px. A lesson
whose reviews went stale is left out of the build with a WARNING (a CI annotation), never silently.

## Libraries
p5.js 1.9.4 and KaTeX 0.16.11 are vendored in `templates/vendor/` and copied to `site/vendor/` on build; fonts
are self-hosted. Pages and headless tests work without a CDN.

## Curriculum
`curriculum.json` covers FY1–FY8 with module goals, central contents and a proposed lesson-slot list per
module, generated from the LOPS 2019 texts in `docs/lops2019/`. The reference lesson is `content/_gold/`.

## Inquiry sequence

A lesson with `inquiry.json` is rendered as inquiry stages (Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista osaamisesi, then Tehtävät last) around the same theory, simulation, exercises and exit ticket; the page form (wide-screen columns, the closed Ennusta box, the simulation's boxes, named formula sections) is CLAUDE.md "Lesson page". Format, activity types, the simulation adapter, migration steps and tests: `docs/inquiry.md`; the teacher's brief: `docs/inquiry-spec.md`. Validate with `python scripts/inquiry.py <id>`, test with `python scripts/test_inquiry.py`.

## Exercise schema
```json
{ "id": "fy3-2-L2-03", "level": 2, "text": "...", "answer": 2.0, "unit": "m/s²", "tolerance": 0.05 }
```
`answers.py` in the lesson folder computes every answer and prints `{id: value}`; the lint compares it with
`exercises.json`. The page checks a typed answer within `tolerance` in the browser; nothing is stored or sent.
`meta.solutions` (`first`, `all`, `none`) decides which worked solutions are rendered.
