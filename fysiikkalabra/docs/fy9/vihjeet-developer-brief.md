# FY9 — brief for writing the hints of one unit's long tasks (work queue 11c)

One unit per session and per pull request, after 11c PR 1 (#855: the shared `hints` support) is on `main`. Work in
`fysiikkalabra/`. The model is `content/fi/units/fy9-liike/sovella/tasks.json` (teacher 2026-11-25: the hint style
approved, "1 yes"); copy its form, never its text. `fy9-harjoituskoe` gets no hints (teacher 2026-11-25).

## What you write (only this)
`"hints"` on every written part (`calc`, `word`, `graph`) of `content/<lang>/units/<id>/sovella/tasks.json`, in `fi`,
`fi-easy` and `en`, placed right after the part's `text`. Nothing else of the unit changes: no task text, answer,
criterion, solution or figure. No shared file.

## The ladder (three hints; fewer only when a third would give the part away)
1. **Ohjaava kysymys.** A question that points at the idea or at what to look at, without naming the formula.
2. **Mikä yhteys.** The relation or representation: the law in the form and symbols of the part's own rubric and model
   solution (`sovella/solutions.md`), with the unit's MAFY name where the unit's theory names it.
3. **Välivaihe.** One intermediate step (a conversion, the condition to write, the point to read) that still leaves
   work to do.

Rules:
- Never the part's final answer, and never a sentence that makes a rubric point free: a hint for an evaluation,
  explanation or design part guides the reasoning as a question and does not state the conclusion.
- Same model, sign convention, symbols and values as the part's rubric and solution; recompute every number a hint
  states. A later part may refer to an earlier part's result ("a-kohdan aika"), never restate its value.
- House conventions as everywhere: every number with its unit in LaTeX, decimal comma in fi and fi-easy and decimal
  point in en, vectors with an overline, chapter names never ids, terms from `glossary.json`.
- One to three sentences per hint. fi-easy: shorter sentences, a difficult word explained at first use (NOTES.md §12),
  the same formulas; `practice.py check` compares the formulas of the three languages.

## Checks before any review
`python3 scripts/practice.py check units/<id>` in each language, `python3 scripts/units.py check`,
`python3 scripts/build.py <id>`, `python3 scripts/check_layout.py <id> --width 360` (then 390, 768, 1280).

## Reviews
The three reviewers, each for the three languages, from `docs/fy9/vihjeet-review-brief.md` (delta: only the hints).
The unit must be `reviewed` in every language it was reviewed in before (`python3 scripts/units.py status`), or its
page leaves the site.
