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
1. **Visualise.** `## Ydinajatus` and `## Kaava` each have at least one inline SVG figure next to the paragraph it explains; formulas and symbols inside figures are LaTeX (`foreignObject`, NOTES.md §3); no paragraph over about 120 words.
2. **Solve symbolically first, then substitute** values with units, in the worked example and every solution.
3. **Simulations are visually rich, not slider-rich.** Keep the physics controls; spend the effort on the picture, motion, meaningful colour, labels, a legend. Every animated sim has a speed control (hidas · normaali · nopea) and only labels and values on the canvas; explanations go behind a "Lisätietoja" button under it.
4. **Worked examples are staged**: 3–6 stages separated by `<!-- vaihe -->` lines, each with a bold lead-in and one step; the page reveals them one at a time.
5. **Inquiry first** (teacher's brief 2026-10-25, `docs/inquiry-spec.md`): every lesson has `inquiry.json` (`docs/inquiry.md`) that walks the student through Herätä kiinnostus → Ennusta → Tutki → Selitä → Sovella → Tarkista osaamisesi: a phenomenon, a retrieval of prior learning, a committed prediction, evidence (a guided experiment on the sim with controlled variables, or a table or figure to interpret), the model, a transfer task with hints and common-mistake feedback, three checks. Feedback is gated on commitment, never access; no answer is disclosed before the student has acted; theory stays readable on its own; the exercises stay 5/4/3.
NOTES.md says how to write each; `scripts/lint_lesson.py` checks what it can.

## Exercise levels
Level 1: one formula, values given, 5 problems. Level 2: two steps or a conversion or a rearrangement, 4. Level 3: reasoning, two ideas, or an unfamiliar context, 3. None repeats the worked example.

## Lesson folder
```
meta.json          id, course, title, goals, prerequisites, glossary, sim, solutions (first | all | none)
lesson.md          Ydinajatus, Kaava, Esimerkki (staged), misconception, summary; inline SVG figures
inquiry.json       the inquiry sequence: contribution, prior, activities by stage (format in docs/inquiry.md)
exercises.json     three levels (schema in README)         solutions.md    given / wanted / formula / substitution / answer / check
answers.py         computes every answer                   exit-ticket.json  3 quick checks
sim.js, sim-spec.md   optional p5.js simulation exposing window.simState and a defineSimAdapter() call, and its one-paragraph spec
review/            science.md, pedagogy.md (and legacy.md on a prototype lesson); developer.md, checks.txt, packet-*.md, usage.tsv
```

## Pipeline (three agents, one rule)
- Agents work from **packets** (`python scripts/review_packet.py <id> --role …`): the lesson's own curriculum slot and glossary terms, the applicable rules, the check results and the files the role judges — never `curriculum.json`, `glossary.json` or `tests/sims` as a whole. A reviewer spends at most three to five tool calls.
- **developer** (Sonnet medium; Opus medium for simulations and demanding physics) writes and fixes the lesson files (inquiry.json included) and nothing else, and runs `python scripts/check_lesson.py <id>` until every check is ok.
- **science-reviewer** (Opus medium) and **pedagogy-reviewer** (Sonnet medium) are independent: each reads the lesson, not the other's report, and writes `review/<name>.md` with `VERDICT: PASS|FAIL` on line 1 and `CONTENT-HASH: <python scripts/reviews.py hash <id>>` on line 2, then `## Blocking` (FAIL if and only if non-empty), `## Polish`, `## Checked`. Reviewers never edit lesson files; language, style and taste are never blocking.
- The science reviewer also checks the physics in every activity (predictions, feedback, experiment setups, model answers); the pedagogy reviewer also judges prerequisite alignment, reasoning quality, meaningful interaction, variable control, premature disclosure, feedback quality, accessibility and workload (`docs/inquiry.md`).
- **The rule** (`scripts/reviews.py`): a lesson is on the site when both reviews say PASS for its current content hash (inquiry.json is content). The hash ignores only line endings, trailing whitespace, blank-line runs and JSON layout, so a mechanical cleanup keeps the reviews; any other change (a space inside a line, an indentation, a word) stales both. There are no status fields and nothing to edit by hand.
- `review/legacy.md` marks a prototype lesson published before this pipeline: it stays visible, labelled as such on the page, until any content change retires the marker; then it returns only through both reviews.
- After a fix, `python scripts/reviews.py scope <id>` decides per reviewer between a **delta review** (previous report + the diff since the version it passed) and a **full** one. Delta only for wording changes that touch no number, formula, symbol, unit, figure, heading, stage, answer, objective or simulation code; the reviewer may escalate; both reviewers must still PASS the current hash.
- `/lesson <id>` runs the whole round with a configurable budget (warning 300 k, hard limit 450 k: past it the run stops safely and the draft PR says what remains), classifies findings A (science/pedagogy) / B (usability) / C (cosmetic, never a fix round), and logs every run in `review/usage.tsv` (`python scripts/usage.py report <id>` compares with the fy3-9 baseline).
- Merging the pull request is the teacher's publication decision. CI rebuilds `site/` and fails if the committed copy differs, so shared templates and stylesheets reach the site only through a diff the teacher sees; a lesson whose reviews went stale is left out with a WARNING, never silently.

## Never
- Never push to `main`, merge a pull request, or force-push. Never edit another agent's report.
- Never copy exam questions from YTL or textbooks; write original problems.
- Never add tracking, logins or forms that collect student data. Never depict real people in generated images.
