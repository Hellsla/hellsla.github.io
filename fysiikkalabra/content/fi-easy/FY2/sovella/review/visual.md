VERDICT: FAIL
CONTENT-HASH: 92afd240281bd811

## Blocking
- [Major] solutions.md, fy2-s1 e) *Energia*, chain "380 GWh − 252 GWh − 88 GWh ≈ 40 GWh" at 1280 px — the wide form is two rows: the first is pushed to the right, the second starts at the left edge as "−88 GWh ≈ 40 GWh" with a unary minus — it reads "minus 88 GWh is about 40 GWh" and nothing is aligned, though the whole chain fits one row — set it on one row on a wide screen; keep the three phone rows (good at 360 and 390 px).
- [Major] solutions.md, fy2-s1 e) *Päästö*, chain m = … at 1280 px — the phone breaks stay on a wide screen and are partly merged: "m = 11 g/kWh · 252" / "· 10⁶ kWh" / … / "· 10⁶ kWh ≈ 2,8 · 10³ t + 2,1 · 10³ t" / "+ 9,2 · 10³ t ≈ 1,4 · 10⁴ t" — 252 · 10⁶ kWh is cut from its power of ten, the ≈ signs stand mid-row instead of under "=", the result has no row of its own — breaks the rule "one step per row, equals signs in one column, only a phone wraps" — wide form in three rows: `m &=` the three products, `&\approx` the three masses, `&\approx` the result. On the phone keep a product whole where it fits ("11 g/kWh · 252 · 10⁶ kWh" is no wider than the row "+ 24 g/kWh · 88 · 10⁶ kWh", which fits at 360 px).

## Polish
- [Minor] solutions.md, *Hyväksytään myös* (older, also in the published version) — the four alternatives render as one paragraph with literal hyphens ("Esimerkiksi: - …"), now with formula boxes inside it — an empty line before the first "- " makes them a list.

## Checked
- review/shots/reflow-item-1.png, reflow-item-2.png (390 px, the changed solution blocks) opened at full size.
- The reflow captures are 390 px only, so I captured every display-formula block of this language's preview page (?ratkaisut=1, boxes open) at 360, 390 and 1280 px and opened the 360 and 1280 px sheets, the criterion block of reflow-item-3.png among them.
- 360 and 390 px: nothing clipped, units whole, punctuation inside the boxes, the sentence continues correctly after each box.
- Unchanged blocks not rejudged (scope: reflow only).

## Scores
illustrations 4 (no figures) · typography 2 · Finnish (Selkeä suomi) 4 · accessibility 4
