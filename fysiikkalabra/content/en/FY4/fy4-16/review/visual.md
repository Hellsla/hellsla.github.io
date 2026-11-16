VERDICT: PASS
CONTENT-HASH: 157ba72a70aa58b3

## Blocking

## Polish
- [Minor] inquiry.json (tile fy4-16 #18, 390 px) — the row is broken inside a short bracket (`(9,81 / − 1,20) m/s²`) — break before `\cdot` instead so the bracket stays whole.
- [Minor] inquiry.json (tile #0) — `10,4 + 49,6 = 16,5 / + 43,5` splits a two-term sum at 390 px — keep `= 16,5 + 43,5` on one row.
- [Minor] inquiry.json:266 and :282 — the two restored inline formulas (`mgh = … · 125 m`, `|ΔE_mek| = …`) stay over-wide on a phone as on main — keep on the clipped-formula list; break before the operator when redone.

## Checked
- delta round 2: opened en-390-02, en-390-03, en-390-04, en-1280-01, en-1280-02, en-1280-03 (all tiles of this part at 390 and 1280 px); no row ends in an operator, every continuation row starts with its operator or relation, chains aligned, nothing new clipped; the restored formula(s) confirmed identical to origin/main (inline, on the known clipped-formula list); hash unchanged from start to end.
