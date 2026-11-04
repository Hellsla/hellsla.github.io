VERDICT: FAIL
CONTENT-HASH: fda9f57419ebbcfb
ROUND: 2

## Blocking
- [Major] solutions.md fy6-5-L3-05 Sijoitus (open-exercises-L3-1280-8) — the c) block is duplicated: "c) $R_\text{p} = \dfrac{100\,\Omega \cdot 5{,}0\,\text{V}}{12\,\text{V} - 5{,}0\,\text{V}} = 71{,}4\,\Omega$ ja $R_\text{k} = ... = 250\,\Omega$" appears twice in a row, so the open solution shows the same chain twice — essential solution text repeated, looks like a merge slip — delete one of the two identical "c) …" paragraphs (the second, directly above "**Vastaus:**").

## Polish
- [Minor] fy6-5-L3-04 task text — a three-branch circuit with two sources and the current directions is still given only in words; a small circuit figure (P, Q, U1, U2, I1..I3) would help on a phone (carried over from round 1).
- [Minor] solutions.md fy6-5-L3-04 Sijoitus (L3-1280-6) — in the block "(21 − 40 I₂)/30 = I₂ / 21 = 70 I₂ / I₂ = 0,30 A" the first row sits higher than the next two (fraction on the left); put the equations in separate lines or align on `=` after multiplying through by 30 first.
- [Minor] fy6-5-L3-05 Sijoitus b) — "Kuormalla $100\,\Omega$ on" runs into a display block and the sentence continues in the next paragraph; one sentence before the block ("Kuormalla $100\,\Omega$ rinnakkaisresistanssi ja potentiaali ovat:") reads better.

## Checked
- Round 1 Polish: c) now set apart, b) comparison a full sentence (fixed), L3-04 dfrac chains now display blocks (fixed), L2-07 quotation now ”…” (fixed, L2-1280-8), task texts split into paragraphs (L2-05, L2-06, L3-04, L3-05).
- 1280 px captures open-exercises-L2-1280-5, -8 (L2-05, L2-07), L3-1280-5, -6, -7, -8 (L3-04, L3-05) read at full size; exercises.json diff (MC options reordered, answers unchanged) and solutions.md read; L2-05 numbers recomputed (0,20+0,15+0,24 = 0,59 A). No 390/360 px capture of exercise cards exists (only stage-exercises-390); check_layout.py fy6-5 at 360 px is OK now (the packet's "FAIL layout 360 px" does not reproduce for the chapter pages).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
