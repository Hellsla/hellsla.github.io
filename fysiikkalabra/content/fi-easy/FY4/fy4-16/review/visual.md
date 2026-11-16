VERDICT: FAIL
CONTENT-HASH: 8549ac0f21453008

## Blocking
- [Major] inquiry.json:282 (tile fy4-16 #3) and :266 (tile #2) — rows broken after a multiplication dot (`9{,}81\,\text{m/s}^2\cdot \\ &125\,\text{m}`); at 1280 px the page shows the row `125 m = 95 647,5 J` under `|ΔE_mek| = 78,0 kg · 9,81 m/s²·`, i.e. a row that reads as metres equal to joules, and at 390 px `125 m` stands flush left as if a new line began — break before the operator: `&= 78{,}0\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\ &\quad\cdot 125\,\text{m} \\ &= 95\,647{,}5\,\text{J}` in both places (no row may end in `\cdot`).

## Polish
- [Minor] inquiry.json:156 and :329 — needless breaks inside short groups (`16,5 / + 43,5`, `(9,81 / − 1,20) m/s²`); keep each group on one row.

## Checked
- batch delta review: re-broken calculation chains judged in the contact sheets fi-easy-390-01…27 (all) and fi-easy-1280-03, 05, 06, 10, 18, 19, 20; rows, alignment at the relation, clipping, punctuation and the surrounding sentence checked; hash unchanged from start to end.
