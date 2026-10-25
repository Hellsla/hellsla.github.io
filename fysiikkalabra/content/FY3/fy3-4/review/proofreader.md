VERDICT: PASS
CONTENT-HASH: fcba3a0523db34af

## Blocking
(none)

## Polish
- glossary.json — "kokonaispaine" is used throughout (lesson, sim, solutions, exercises) but has no entry; consider adding one (not a language defect).
- solutions.md L1-03 Järkevyys — "vastaa vajaata kahta ilmanpainetta" is correct but heavy; "on vajaa kaksi ilmanpainetta" would read lighter. Optional.

## Diff
```diff
```
(empty: round 2 diff is applied; the round-3 sim.js change needs no language fix)

## Checked
- Round 3: only sim.js changed since my round-2 PASS (hash e15a6538eb0006e3 -> fcba3a0523db34af); lesson.md, exercises.json, solutions.md, exit-ticket.json, sim-spec.md unchanged and not re-judged beyond the hash.
- sim.js Finnish strings re-read in full: "Näytä vain ylipaine", note text (line 35), "Syvyys h", "Tiheys ρ", "Hydrostaattinen paine ρgh", "Kokonaispaine p = p₀ + ρgh", "kertaa ilmanpaine", "Kuvaajan asteikko 0–", "ylipaine ρgh (kPa)", "paine p (kPa)", "ilma, p₀ = 101 kPa"; spelling, decimal comma (fi()), minus sign and thin-space-free kPa/m usage correct.
- Liquid names (bensiini, vesi, merivesi, Kuolleenmeren vesi): correct spelling and capitalisation.
- New placement code: the short label "p₀" is the symbol alone, the same as the lesson text uses and the readout defines ("p₀ = 101 kPa"); no terminology or meaning problem when the long form shortens.
- Terminology matches glossary.json (paine, hydrostaattinen paine, ilmanpaine, ylipaine, tiheys); no "N voimalla" slips.
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Hash unchanged at start and end of review.
