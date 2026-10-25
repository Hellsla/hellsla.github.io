# Fysiikkalabra — house rules for every agent

## What this repo is
A digital textbook for Finnish upper-secondary physics (LOPS 2019): theory, simulations and exercises, one folder per lesson under `content/<course>/<lesson-id>/`. `scripts/build.py` renders the lessons whose reviews are current into `site/`, which is committed and served by GitHub Pages at `hellsla.github.io/fysiikkalabra/site/`. Previews (`build.py <id>` or `--all`) go to the git-ignored `preview/`.

## Scope
- `curriculum.json` lists the modules and lesson slots, generated from the LOPS 2019 texts in `docs/lops2019/` (MAOL module guide, OPH transversal competences). Grep the guide when unsure whether something belongs to a module.
- Stay inside a module's central content. Example: FY3 treats force only as a measure of interaction and work as W = Fs; Newton's laws, vectors and the liikeyhtälö are FY4.

## Audience and language
- Students aged 16–19, smart but meeting the idea for the first time. Site language Finnish; agent prompts and reports may be in English.
- Physics terms come from `glossary.json`; add a missing term there, do not invent synonyms.

## Physics and maths conventions
- SI units, upright with a thin space: `9,81 m/s²`. Decimal comma in Finnish text, decimal point in JSON.
- g = 9,81 m/s², always in m/s² (never N/kg). Three significant figures in final answers unless the data has fewer.
- Vectors bold in LaTeX (`\mathbf{F}`), magnitudes plain. Every formula appears once in display LaTeX with its symbols named.
- Every exercise has `answer`, `unit` and `tolerance`; the data carries the significant figures the answer should have, and a student rounding to them stays inside the tolerance. `answers.py` computes every answer.

## Lesson form (human decisions 2026-10-25, every lesson)
1. **Visualise.** `## Ydinajatus` and `## Kaava` each have at least one inline SVG figure next to the paragraph it explains; no paragraph over about 120 words.
2. **Solve symbolically first, then substitute** values with units, in the worked example and every solution.
3. **Simulations are visually rich, not slider-rich.** Keep the controls; spend the effort on the picture, motion, meaningful colour, labels, a legend.
4. **Worked examples are staged**: 3–6 stages separated by `<!-- vaihe -->` lines, each with a bold lead-in and one step; the page reveals them one at a time.
NOTES.md says how to write each; `scripts/lint_lesson.py` checks what it can.

## Exercise levels
Level 1: one formula, values given, 5 problems. Level 2: two steps or a conversion or a rearrangement, 4. Level 3: reasoning, two ideas, or an unfamiliar context, 3. None repeats the worked example.

## Lesson folder
```
meta.json          id, course, title, goals, prerequisites, glossary, sim, solutions (first | all | none)
lesson.md          Ydinajatus, Kaava, Esimerkki (staged), misconception, summary; inline SVG figures
exercises.json     three levels (schema in README)         solutions.md    given / wanted / formula / substitution / answer / check
answers.py         computes every answer                   exit-ticket.json  3 quick checks
sim.js, sim-spec.md   optional p5.js simulation exposing window.simState, and its one-paragraph spec
review/            science.md, pedagogy.md (and legacy.md on a prototype lesson); developer.md, usage.log
```

## Pipeline (three agents, one rule)
- **developer** (Sonnet) writes and fixes the lesson files and nothing else, and runs `python scripts/check_lesson.py <id>` until every check is ok.
- **science-reviewer** (Opus) and **pedagogy-reviewer** (Sonnet) are independent: each reads the lesson, not the other's report, and writes `review/<name>.md` with `VERDICT: PASS|FAIL` on line 1 and `CONTENT-HASH: <python scripts/reviews.py hash <id>>` on line 2, then `## Blocking` (FAIL if and only if non-empty), `## Polish`, `## Checked`. Reviewers never edit lesson files; language, style and taste are never blocking.
- **The rule** (`scripts/reviews.py`): a lesson is on the site when both reviews say PASS for its current content hash. The hash ignores formatting (whitespace, JSON layout), so a mechanical cleanup keeps the reviews; any other change stales both. There are no status fields and nothing to edit by hand.
- `review/legacy.md` marks a prototype lesson published before this pipeline: it stays visible, labelled as such on the page, until any content change retires the marker; then it returns only through both reviews.
- `/lesson <id>` runs the whole round: developer, checks, both reviews in parallel, fixes, at most three rounds, one commit per round, then a pull request with a teacher summary and the token usage from `review/usage.log`.
- Merging the pull request is the teacher's publication decision. CI rebuilds `site/` and fails if the committed copy differs, so shared templates and stylesheets reach the site only through a diff the teacher sees; a lesson whose reviews went stale is left out with a WARNING, never silently.

## Never
- Never push to `main`, merge a pull request, or force-push. Never edit another agent's report.
- Never copy exam questions from YTL or textbooks; write original problems.
- Never add tracking, logins or forms that collect student data. Never depict real people in generated images.
