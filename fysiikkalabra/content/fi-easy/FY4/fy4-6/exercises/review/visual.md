VERDICT: FAIL
CONTENT-HASH: eca9e2a3fca85018

## Blocking
- [Major] exercises/solutions.md, Sijoitus with `F_\text{max}` (tile fy4-6 #2, 390 and 1280 px) — the row is broken after a multiplication dot (`10\,\text{kg}\cdot \\ &9{,}81…`): the page shows `F_max = 0,60 · 10 kg·` and under it, flush left, `9,81 m/s² · cos 35° = 48,2 N`, which reads as a separate, false equation; at 1280 px the first row is even indented past the second — break before the operator: `&= 0{,}60\cdot 10\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\ &\quad\cdot\cos 35^\circ \\ &= 48{,}2\,\text{N}` (no row may end in `\cdot`).

## Polish

## Checked
- batch delta review: re-broken calculation chains judged in the contact sheets fi-easy-390-01…27 (all) and fi-easy-1280-03, 05, 06, 10, 18, 19, 20; rows, alignment at the relation, clipping, punctuation and the surrounding sentence checked; hash unchanged from start to end.
