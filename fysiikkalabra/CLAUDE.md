# Fysiikkalabra — house rules for every agent

## What this repo is
A static teaching site for Finnish upper-secondary physics and maths (LOPS 2021).
Content is data: one folder per lesson under `content/<course>/<lesson-id>/`.
`scripts/build.py` renders reviewed lessons into `site/`, which is committed and served by GitHub Pages at `hellsla.github.io/fysiikkalabra/site/`. Previews of drafts (`build.py <id>` or `--all`) go to the git-ignored `preview/`.

## Scope
- `curriculum.json` is generated from the LOPS 2019 module descriptions; `docs/lops2019/` holds the official text (MAOL module guide with scope clarifications, OPH transversal competences). Grep it when unsure whether something belongs to a module.
- Stay inside a module's central content unless the human says otherwise. Examples: FY3 treats force only as a measure of interaction and work as W = Fs; Newton's laws, vectors and the liikeyhtälö are FY4.

## Notes
- Read `NOTES.md` before drafting or reviewing a lesson. It holds the LaTeX rules and other lessons learned. Add a line there whenever a mistake costs a review round.

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
- Reviewers never edit lesson files. They write `review/<agent>.md` with `VERDICT: PASS` or `VERDICT: FAIL` on the first line, `CONTENT-HASH: <value of python scripts/gate.py --hash <id>>` on the second, then numbered findings with file and line.
- Producers may only write the files named in their agent definition.
- The orchestrator runs reviewers, then the fixer on any FAIL, and repeats for at most three rounds. Only if the third round still fails, or the fixer is blocked, does it stop and report to the human.
- `status` in `meta.json` moves `draft → reviewed` only through the publication gate (`python scripts/gate.py <id> --publish`, run by the publisher agent). The gate opens only when every required reviewer has `VERDICT: PASS` for the lesson's CURRENT content hash and the structure, LaTeX, build and simulation checks pass. Any later edit changes the hash and closes the gate again; CI runs `gate.py --verify` to catch it. Nobody edits status or hash fields by hand, agents never do.

## Gold standard
`content/_gold/` is the reference lesson. Match its tone, length and structure. When in doubt, read it again.

## Never
- Never publish or commit on your own, except the publisher agent, which commits a gate-approved lesson to the working branch. Nobody pushes to `main` or merges pull requests without the human.
- Never copy exam questions from YTL or textbooks into lessons; write original problems. Exam files may be studied for patterns only, stored in the git-ignored `docs/exams/` (see NOTES.md, section 3).
- Never add tracking, logins or forms that collect student data.
- Never depict real people in generated images.
