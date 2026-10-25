VERDICT: PASS
CONTENT-HASH: e15a6538eb0006e3

## Blocking
(none)

## Polish
- glossary.json — "kokonaispaine" is used throughout (lesson, sim, solutions, exercises) but has no entry; consider adding one (not a language defect).
- solutions.md L1-03 Järkevyys — "vastaa vajaata kahta ilmanpainetta" is correct but heavy; "on vajaa kaksi ilmanpainetta" would read lighter. Optional.

## Diff
```diff
```
(empty: the first-pass diff is applied and nothing else is wrong)

## Checked
- First-pass diff confirmed in lesson.md:10 (bottle holes, "koska paine kasvaa syvyyden mukana"), :12 (ilmanpaine sentence split, "Ilmanpaine ... välittyy veden kautta") and :14 ("ylipaine eli paineen ilmanpainetta suurempi osa", "Ylipaine on yläreunassa nolla"); grammar and logic correct.
- Rest of lesson.md re-read: derivation (:8), formula section, worked example (:47-53), misconception (:56), summary; spelling, decimal comma, thin-space units and case endings (12 m:n, 150 cm², 180 kg:n, 290 kN:n) correct.
- exercises.json texts (all 12): spelling, case after number-plus-unit (95 m:n, 18,0 m:n, 4,0 m:n, 1,60 m:n), "kilopascaleina/megapascaleina/kilonewtoneina" correct; numbers untouched.
- solutions.md, exit-ticket.json, sim-spec.md and sim.js Finnish strings ("Näytä vain ylipaine", "ylipaine ρgh (kPa)", "ilma, p₀ = 101 kPa", note text): correct.
- Terminology matches glossary.json (paine, pascal, hydrostaattinen paine, ilmanpaine, ylipaine, tiheys); "paino" used as a force; no "N voimalla" slips.
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Reading level suitable for 16-19-year-olds.
