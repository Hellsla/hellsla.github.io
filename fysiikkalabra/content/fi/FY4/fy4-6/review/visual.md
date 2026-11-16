VERDICT: PASS
CONTENT-HASH: 92b3cd17a26857e0

## Blocking

## Polish
- [Minor] inquiry.json:479 (tile fy4-6 #8, 390 px) — the restored inline `N = 20 kg · 9,81 m/s² · cos 20° ≈ 184 N` is cut at the right edge on a phone exactly as on main (`≈ 184 N` lost) — keep it on the clipped-formula list; when re-broken, break before the operator (`\\ &\quad\cdot\cos 20^\circ`).
- [Minor] inquiry.json (tile #0, 390 px) — the mean is broken inside the bracket (`(0,347 + 0,357 / + 0,347 + 0,352) : 4`) with the continuation flush left — indent the continuation row with `\quad`.

## Checked
- delta round 2: opened fi-390-01, fi-1280-01 (all tiles of this part at 390 and 1280 px); no row ends in an operator, every continuation row starts with its operator or relation, chains aligned, nothing new clipped; the restored formula(s) confirmed identical to origin/main (inline, on the known clipped-formula list); hash unchanged from start to end.
