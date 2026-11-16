VERDICT: PASS
CONTENT-HASH: 586285323faf3a8f
SCOPE: delta round 2, fy8-12-L2-08 after fix

## Blocking

(none)

## Polish

- The three round-1 length polishes (c five asks, d three asks, stem length) are not addressed in this diff; still optional.

## Checked

- Box answer 14 with tolerance 0.04 accepts 14.48 (exact) and 14.5, so both the rounded two-figure value and the earlier value pass; answers.py comment matches the 2-significant-figure answer.
- Solution Vastaus/Answer now states two significant figures (matches the 3,5 GHz data) and says the box also accepts 14,5.
- Comparison ratios split into two displayed lines: clearer, same numbers (6,9e5, 6,9e9).
- Units J s and 24 h typeset consistently in task and solution; no pedagogical change.
- Method: delta, diff only.
