# Fysiikkalabra

A digital textbook for Finnish upper-secondary physics (LOPS 2019): theory, p5.js simulations and exercises,
written and reviewed with Claude Code agents, served by GitHub Pages from the committed `site/` folder at
`https://hellsla.github.io/fysiikkalabra/site/`. House rules for agents: `CLAUDE.md`; writing rules: `NOTES.md`.

## Quick start
```bash
cd fysiikkalabra
pip install markdown playwright && playwright install chromium
python scripts/check_lesson.py fy3-9     # lint, LaTeX, preview build, simulation tests, 360 px layout, review state
python scripts/build.py fy3-9            # preview/fy3-9.html (git-ignored), any lesson
python scripts/build.py --all            # preview/ with every lesson, drafts included (what CI tests)
python scripts/build.py                  # site/ from the lessons whose reviews are current (atomic; commit it)
python scripts/reviews.py status         # reviewed | legacy | draft for every lesson, and why
python scripts/test_reviews.py           # tests of the publishing rule
```
If the pip `playwright` version does not match the installed browser: `PW_CHROMIUM=/path/to/chrome python scripts/test_sims.py`.

Inside Claude Code, `/lesson fy3-9` runs one lesson through the pipeline: the **developer** (Sonnet) writes or
fixes, `check_lesson.py` must pass, the **science-reviewer** (Opus) and the **pedagogy-reviewer** (Sonnet) judge it
independently, fixes and re-reviews for at most three rounds, then a pull request with a teacher summary and the
token usage. Agents live in `.claude/agents/`, the command in `.claude/commands/`.

## The publishing rule
`scripts/reviews.py` decides what is on the site: a lesson is **reviewed** when `review/science.md` and
`review/pedagogy.md` both say `VERDICT: PASS` with the lesson's current `CONTENT-HASH`. The hash ignores only
line endings, trailing whitespace, blank-line runs and JSON layout; any other edit stales both reviews. A **legacy**
lesson (`review/legacy.md`, written by `reviews.py legacy <id>` in the migration) was published before the
pipeline and stays visible, labelled as a prototype, until a content edit retires the marker. Everything else
is a **draft** and never reaches `site/`.

Merging a pull request is the teacher's publication decision. CI (`.github/workflows/fysiikkalabra-ci.yml`)
lints every lesson, builds all previews, runs the review tests, the simulation tests and the LaTeX check,
rebuilds `site/` and fails if the committed copy differs, and checks every published page at 360 px. A lesson
whose reviews went stale is left out of the build with a WARNING (a CI annotation), never silently.

## Libraries
p5.js 1.9.4 and KaTeX 0.16.11 are vendored in `templates/vendor/` and copied to `site/vendor/` on build; fonts
are self-hosted. Pages and headless tests work without a CDN.

## Curriculum
`curriculum.json` covers FY1–FY8 with module goals, central contents and a proposed lesson-slot list per
module, generated from the LOPS 2019 texts in `docs/lops2019/`. The reference lesson is `content/_gold/`.

## Exercise schema
```json
{ "id": "fy3-2-L2-03", "level": 2, "text": "...", "answer": 2.0, "unit": "m/s²", "tolerance": 0.05 }
```
`answers.py` in the lesson folder computes every answer and prints `{id: value}`; the lint compares it with
`exercises.json`. The page checks a typed answer within `tolerance` in the browser; nothing is stored or sent.
`meta.solutions` (`first`, `all`, `none`) decides which worked solutions are rendered.
