VERDICT: PASS
CONTENT-HASH: f628c9c4d2493275

## Blocking
(none)

## Polish
- exercises.json:265 — kytkentä C (three 330 Ω in parallel) repeats L1-05 and B/A resemble L1-02/L2-04; swap C for a new sub-circuit if the set should not reuse its numbers.
- solutions.md:197 — the last paragraph ("Jos rivin ... unohtaa kääntää") lists 0,0076 and 0,0091 without saying what they are; add "summat 1 : R" and show that D, E and A are not affected.
- exercises.json:265 — the stem says "Laske ... ja järjestä"; the prompt then repeats the order sentence; keep one.

## Checked
- Order type: direction stated (pienimmästä suurimpaan); five distinct values 110, 132, 150, 265, 550 - recomputed all, correct.
- Warned mistake (forgetting to invert 1 : R) swaps B and C, as the solution says; the near values 132 and 150 force an actual calculation.
- Single resistor E and the mixed circuit D are covered by the lesson (Sekakytkentä); no figure needed, text description unambiguous.
- Solution explains principle for series, parallel, mixed; formula lines at most 182 px.
- Finnish: "330 Ω:n vastuksen", "kahden rinnan kytketyn" correct.
- Text only (no renders: packet screenshots were empty; I measured widths of the model-solution formulas with KaTeX in Chromium at 17 px, 390 px viewport).
