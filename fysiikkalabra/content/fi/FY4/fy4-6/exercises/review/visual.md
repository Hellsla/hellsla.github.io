VERDICT: PASS
CONTENT-HASH: f628d4dfd9e1cfaf

## Blocking
None.

## Polish
- [Minor] solutions.md Sijoitus (`F_max = 0,60 · 10 kg · 9,81 m/s² · cos 35°`), capture fi-390-07 / fi-1280-05 #2 — the row ends with a dangling `\cdot` and the continuation `9{,}81\,\text{m/s}^2\cdot\cos 35^\circ` starts without an operator, left of the `=` column; at 1280 px the rows are joined into a stepped two-row formula. Every other chain in FY4 starts the row with the operator. Fix: `… \\ &\cdot 9{,}81\,\text{m/s}^2\cdot\cos 35^\circ` (as fy4-7 `E_p`). No new review round needed.

## Checked
- batch delta review: re-broken chains in solutions.md/exercises.json (reflow only); opened fi-390-07, fi-390-08 and fi-1280-05, fi-1280-06; rows break at relations/operators, equals signs aligned, nothing clipped, sentence around each lifted formula reads naturally.
