# Fysiikkalabra — house rules for every agent

## What this repo is
A static teaching site for Finnish upper-secondary physics and maths (LOPS 2021).
Content is data: one folder per lesson under `content/<course>/<lesson-id>/`.
`scripts/build.py` renders folders into `site/`. This repository serves GitHub Pages from its root, so `site/` goes live only once it is committed (see README, "Publishing").

## Audience and language
- Students aged 16–19. Assume they are smart but meeting the idea for the first time.
- Site language: Finnish. Agent prompts and reports may be in English.
- Use Finnish physics terminology from `glossary.json`. When a term is missing, add it there, do not invent synonyms.

## Physics and maths conventions
- SI units only; write units upright with a thin space: `9,81 m/s²`. Decimal comma in Finnish text, decimal point in JSON.
- g = 9,81 m/s². Three significant figures in final answers unless the data has fewer.
- Vectors in bold in LaTeX (`\mathbf{F}`), magnitudes plain (`F`).
- Every formula in a lesson appears in display LaTeX once, with symbols named the first time.
- Every exercise has a numeric or short-text `answer`, a `unit`, and a `tolerance`.

## Exercise levels
- Level 1: direct use of one formula, values given. 5 problems.
- Level 2: two steps or one unit conversion or one rearrangement. 4 problems.
- Level 3: reasoning, combining two ideas, or an unfamiliar context. 3 problems.
- No exercise repeats the worked example with different numbers.

## Lesson folder (the only files agents may write)
```
meta.json          id, course, title, goals, prerequisites, glossary, sim, status
lesson.md          theory: motivating question, core idea, formula, worked example, misconception, summary
exercises.json     three levels, see schema in README
solutions.md       given / wanted / formula / substitution with units / answer / sanity check
exit-ticket.json   3 quick checks
sim.js             optional p5.js simulation exposing window.simState
sim-spec.md        one paragraph describing the sim, written by the human
review/            one <agent>.md report per reviewer, overwritten on each run
```

## Review protocol
- Reviewers never edit lesson files. They write `review/<agent>.md` with `VERDICT: PASS` or `VERDICT: FAIL` on the first line, then numbered findings with file and line.
- Producers may only write the files named in their agent definition.
- The orchestrator stops and reports to the human after two consecutive FAILs on the same lesson.
- `status` in `meta.json` moves `draft → reviewed` only by the human.

## Gold standard
`content/_gold/` is the reference lesson. Match its tone, length and structure. When in doubt, read it again.

## Never
- Never publish or commit on your own; the human commits.
- Never fetch or copy exam questions from YTL or textbooks; write original problems.
- Never add tracking, logins or forms that collect student data.
- Never depict real people in generated images.
