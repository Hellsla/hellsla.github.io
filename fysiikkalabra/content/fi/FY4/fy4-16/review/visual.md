VERDICT: PASS
CONTENT-HASH: 5274dfc8bb22bb00

## Blocking
None.

## Polish
- [Minor] inquiry.json hint and solution (`mgh`, `|ΔE_mek|`), capture fi-390-24 / fi-1280-18 #2, #3 — the row ends with a dangling `\cdot` and the continuation `125\,\text{m}` starts without an operator, left of the `=` column; at 1280 px the rows are joined into a stepped two-row formula. Every other chain in FY4 starts the row with the operator. Fix: `… \\ &\cdot 125\,\text{m}` (as fy4-7 `E_p`). No new review round needed.

## Checked
- batch delta review: re-broken chains in lesson.md/inquiry.json (reflow only); opened fi-390-24, fi-390-25, fi-390-26 and fi-1280-18, fi-1280-20; rows break at relations/operators, equals signs aligned, nothing clipped, sentence around each lifted formula reads naturally.
