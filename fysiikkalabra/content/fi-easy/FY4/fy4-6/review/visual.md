VERDICT: FAIL
CONTENT-HASH: 47dfebdb880ee830

## Blocking
- [Major] inquiry.json:479 (tile fy4-6 #10, 1280 px) — the chain is hand-broken after a multiplication dot (`20\,\text{kg}\cdot \\ &9{,}81…`), so the page shows `N = 20 kg·` and under it, flush left, `9,81 m/s² · cos 20° ≈ 184 N` — the second row reads as an equation of its own (a false one) and the rows are not aligned at the relation — break before the operator like every other chain: `&N \\ &= 20\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\ &\quad\cdot\cos 20^\circ \\ &\approx 184\,\text{N}` (no row may end in `\cdot`).

## Polish

## Checked
- batch delta review: re-broken calculation chains judged in the contact sheets fi-easy-390-01…27 (all) and fi-easy-1280-03, 05, 06, 10, 18, 19, 20; rows, alignment at the relation, clipping, punctuation and the surrounding sentence checked; hash unchanged from start to end.
