VERDICT: PASS
CONTENT-HASH: 245e52b58746439a

## Blocking
None.

## Polish
- [Minor] inquiry.json solution (`N = 20 kg · 9,81 m/s² · cos 20°`), capture fi-1280-06 #10 — the row ends with a dangling `\cdot` and the continuation `9{,}81\,\text{m/s}^2` starts without an operator, left of the `=` column; at 1280 px the rows are joined into a stepped two-row formula. Every other chain in FY4 starts the row with the operator. Fix: `… \\ &\cdot 9{,}81\,\text{m/s}^2` (as fy4-7 `E_p`). No new review round needed.

## Checked
- batch delta review: re-broken chains in lesson.md/inquiry.json (reflow only); opened fi-390-07, fi-390-08 and fi-1280-05, fi-1280-06; rows break at relations/operators, equals signs aligned, nothing clipped, sentence around each lifted formula reads naturally.
