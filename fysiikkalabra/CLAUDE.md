# Fysiikkalabra — house rules for every agent

## What this repo is
A static teaching site for Finnish upper-secondary physics and maths (LOPS 2019, in force since 2021).
Content is data: one folder per lesson under `content/<course>/<lesson-id>/`.
`scripts/build.py` renders reviewed lessons into `site/`, which is committed and served by GitHub Pages at `hellsla.github.io/fysiikkalabra/site/`. Previews of drafts (`build.py <id>` or `--all`) go to the git-ignored `preview/`.

## Scope
- `curriculum.json` is generated from the LOPS 2019 module descriptions; `docs/lops2019/` holds the official text (MAOL module guide with scope clarifications, OPH transversal competences). Grep it when unsure whether something belongs to a module.
- Stay inside a module's central content unless the human says otherwise. Examples: FY3 treats force only as a measure of interaction and work as W = Fs; Newton's laws, vectors and the liikeyhtälö are FY4.

## Notes
- Read `NOTES.md` before drafting or reviewing a lesson. It holds the LaTeX rules and other lessons learned. Add a line there whenever a mistake costs a review round, and a check to `scripts/lint_lesson.py` whenever the rule can be checked mechanically.
- `python scripts/lint_lesson.py <id>` runs before any reviewer. Reviewers do not repeat what it reports.

## Audience and language
- Students aged 16–19. Assume they are smart but meeting the idea for the first time.
- Site language: Finnish. Agent prompts and reports may be in English.
- Use Finnish physics terminology from `glossary.json`. When a term is missing, add it there, do not invent synonyms.

## Physics and maths conventions
- SI units only; write units upright with a thin space: `9,81 m/s²`. Decimal comma in Finnish text, decimal point in JSON.
- g = 9,81 m/s², and g is always written in m/s² (never N/kg). Three significant figures in final answers unless the data has fewer.
- Vectors in bold in LaTeX (`\mathbf{F}`), magnitudes plain (`F`).
- Every formula in a lesson appears in display LaTeX once, with symbols named the first time.
- Every exercise has a numeric or short-text `answer`, a `unit`, and a `tolerance`. Write the data with the significant figures the answer should have (`4,0 kg`), and choose the tolerance so a student rounding to those figures is inside it.
- `meta.solutions` is `first` (default: the first solution of each level is published), `all` or `none`.

## Human decisions on lesson form (2026-10-25, apply to every lesson, new and old)
1. **Visualise, do not only write.** Theory is not a wall of paragraphs. `## Ydinajatus` has at least one inline SVG figure and `## Kaava` at least one (diagram, graph, energy-flow or particle picture), placed next to the paragraph it explains; no paragraph runs over about 120 words. A lesson has at least two figures.
2. **Solve symbolically first, then substitute.** In every worked example and every solution, first solve the equation for the unknown with symbols only, then substitute the values *with their units*, then compute. Never put numbers into an equation and solve afterwards.
3. **Simulations are visually rich, not slider-rich.** Do not add sliders for show. Spend the effort on the picture: realistic objects, shading or gradients, motion, colour that carries meaning (temperature, pressure), clear labels and a legend. Keep the existing controls.
4. **Worked examples are detailed and staged.** The solution under `## Esimerkki` is written in display LaTeX in 3–6 stages separated by lines `<!-- vaihe -->`; the page reveals them one at a time ("Näytä seuraava vaihe"). Each stage has a bold lead-in (e.g. **Kaava ratkaistuna.**, **Sijoitus.**, **Järkevyys.**) and one step of the reasoning.
See NOTES.md section 4 for how to write each of these. The lint checks what it can.

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
solutions.md       given / wanted / formula / substitution with units / answer / sanity check (rendered on the page per meta.solutions)
answers.py         the Python that computes every answer; the gate re-runs it against exercises.json
exit-ticket.json   3 quick checks
sim.js             optional p5.js simulation exposing window.simState
sim-spec.md        one paragraph describing the sim, written by the human
review/            one <agent>.md report per reviewer, overwritten on each run
```

## Review protocol
- Reviewers never edit lesson files. They write `review/<agent>.md` with `VERDICT: PASS` or `VERDICT: FAIL` on the first line, `CONTENT-HASH: <value of python scripts/gate.py --hash <id> --for <agent>>` on the second, then `## Blocking` findings (FAIL if and only if there are any), `## Polish` and `## Checked`, each finding with file and line. Under 400 words. Spelling, style and taste are never blocking.
- Each reviewer has a domain, the files it judges (`DOMAINS` in `scripts/gate.py`). Its hash covers only those, so after a fix only the reviewers whose files changed run again.
- Producers may only write the files named in their agent definition.
- The orchestrator runs the lint, then the proofreader (its diff is applied first), then the other reviewers in parallel, then the fixer on any FAIL, and repeats for at most three rounds, re-running only stale reviewers. It logs each round with `python scripts/gate.py <id> --log-round` and commits once per round. Only if the third round still fails, or the fixer is blocked, does it stop and report to the human.
- `status` in `meta.json` moves `draft → reviewed` only through the publication gate (`python scripts/gate.py <id> --publish`, run by the publisher agent). The gate opens only when every required reviewer has `VERDICT: PASS` for the CURRENT hash of its files and the structure, lint, `answers.py`, LaTeX, build and simulation checks pass. Any later edit changes the hash and closes the gate again; CI runs `gate.py --verify` to catch it. Nobody edits status or hash fields by hand, agents never do.
- `templates/` (CSS, JS, page template) is site-wide and outside every reviewer's domain: a change there is reviewed by the human in the pull request through the rebuilt `site/` diff. CI rebuilds `site/` and fails if the committed copy differs, and checks every published page at 360 px.
- To change a published lesson, run `python scripts/gate.py <id> --reopen` first. Its live page then stays exactly the reviewed render (verified by hash) while the source is revised, and only a new pass through the gate replaces it.

## Gold standard
`content/_gold/` is the reference lesson. Match its tone, length and structure. When in doubt, read it again.

## Never
- Never publish on your own. The orchestrator commits once per review round and the publisher commits and pushes a gate-approved lesson, both to the working branch only. Nobody pushes to `main` or merges pull requests without the human.
- Never copy exam questions from YTL or textbooks into lessons; write original problems. Exam files may be studied for patterns only, stored in the git-ignored `docs/exams/` (see NOTES.md, section 3).
- Never add tracking, logins or forms that collect student data.
- Never depict real people in generated images.
