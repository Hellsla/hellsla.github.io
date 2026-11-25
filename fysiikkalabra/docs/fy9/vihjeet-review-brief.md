# FY9 — delta review: hints on the long tasks (work queue 11c, teacher 2026-11-25)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial) and the unit.

## What changed
Each written part of the unit's long tasks (`content/<lang>/units/<id>/sovella/tasks.json`, the unit page's Tehtävät)
gained `hints`: at most three texts, shown under the part by the same hint component as on a short numeric task
(`scripts/practice.py` `_card`, `inquiry.hints_html`; labels "Vihje 1: ohjaava kysymys", "Vihje 2: mikä yhteys",
"Vihje 3: välivaihe"; closed hints of a part on one row, `templates/site.css` `ol.parts>li>.hints`). Nothing else in
the unit changed: task texts, answers, rubrics, solutions, figures and the rest of the page are as reviewed.
The diff: `git diff origin/main -- content/fi/units/<id> content/fi-easy/units/<id> content/en/units/<id>` (ignore
`review/`). The unit was reviewed in full before (its `review/<role>.md`); judge only the hints and what they touch.

## What to judge
- Science: each hint is correct physics and mathematics for its part and agrees with that part's rubric, model
  solution (`sovella/solutions.md`) and answer: same model, same symbols, same sign conventions, same values and
  conversions (recompute any number a hint states). A hint must not state the part's final answer. Numbers with units
  are LaTeX; decimal comma in fi and fi-easy, decimal point in en. The fi-easy and en hints say the same physics as fi.
- Pedagogy: the ladder works for a 16–19-year-old who is stuck: hint 1 a guiding question that points at the idea
  without naming the formula, hint 2 the relation or representation, hint 3 one intermediate step that still leaves
  work to do. No hint gives the part away or makes the rubric's points free; a hint for an evaluation or design part
  guides the reasoning and does not dictate the conclusion. fi-easy: shorter sentences, a difficult word explained
  (NOTES.md §12), nothing of the physics dropped.
- Visual & editorial: build `python3 scripts/build.py <id>` → `preview/<id>.html`, `preview/fi-easy/<id>.html`,
  `preview/en/<id>.html`; look at the Tehtävät cards at 390 and 1280 px (Playwright: `scripts/_browser.py`) with
  hints closed and open: the row of closed hints, an open hint's box, formulas (none clipped, none to be scrolled),
  no overflow, the card in reading order, language (Finnish, selkeä suomi, English) and typography of the new texts.

## Output
For each language write `content/<lang>/units/<id>/review/<science|pedagogy|visual>.md` (overwrite your role's
previous report), starting exactly
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id> --lang <lang>>
```
(or FAIL; no SCOPE line). Then numbered findings, Blocking first, then Polish, each with the task part (for example
s3 b, hint 2), the language and a concrete replacement text, in under 500 words per report. Edit nothing else and do
not commit. A problem in a shared file goes under "Shared issues". Report back in under 150 words.
