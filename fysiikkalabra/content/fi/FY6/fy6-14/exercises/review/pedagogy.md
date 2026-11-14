VERDICT: PASS
CONTENT-HASH: a9fa68c9a1a5eb01
SCOPE: delta added-exercise from 279de6f0ff1eeacc base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- solutions.md (fy6-14-L2-09, Järkevyys) — "kuvan paneelin suurinta tehoa ($0{,}92\,\text{W}$)" is a value the student cannot read from the figure as described; either drop the clause or say "suurin teho on suurempi, koska jännitteellä 4,6 V virta on vielä lähes 200 mA" only if the figure supports it. The first half (UI_oikosulku < 1,2 W bound) is enough.
- exercises.json (fy6-14-L2-09) — the answer sits on the near-flat part of the curve, so the reading task is easy (any reading 192–208 mA passes); fine for level 2 since the conversion mA to A and P = UI are the work, but a 5,0 V load would make the student read the bend. Optional.
- solutions.md — "kulkee $200\,\text{mA}$:n ruudukkoviivalla" while the grid is 50 mA: say that 200 mA is the fourth gridline so the reading is checkable.

## Checked
- Text only (no render) of the added fy6-14-L2-09.
- Recomputed: P = 4,0 V · 0,200 A = 0,80 W; matches answer 0,8 and 4 % tolerance (192–208 mA accepted).
- Figure ex-kenno: its description gives the start (200 mA), the flat part to about 4 V, the bend near 5 V and 6,0 V on the axis, so a reader without the picture gets the same reading; neither gives power or the answer.
- Level 2: read a graph, convert mA to A, apply P = UI; solution states the principle (panel as a DC source) and the unit conversion explicitly.
- Fits the set: L1-04 gives U and I directly, L2-06 works from a table of load measurements, L3-02 from measurement pairs; this is the one graph-read task for the panel, no repeat of the worked example.
- Finnish and units correct; unit mA kept in the read, W in the answer.
- Hash unchanged at the start and end.
