VERDICT: FAIL
CONTENT-HASH: 8bb5e95996158b57

## Blocking
- [Major] inquiry.json, Laskutehtävä "astronautin massa", Sijoitus (own capture at 1280 px, wide form from 700 px) — the wide form shows `m_a = 1200 N/m · (1,66 s)² / 4π²` on row 1 and `− 10,0 kg = 83,76 kg − 10,0 kg` on row 2: the second equals sign stands mid-row, out of the column of the others, and row 2 reads at a glance as its own equation (−10,0 kg = …) — against "every = in one column" (teacher 2026-11-13) — `mathlayout.join_wide` takes the continuation row `&- 10{,}0\,\text{kg}` for a bare left side and joins the next `=` row to it. Fix: write the continuation as `\\ &\quad - 10{,}0\,\text{kg}` (tried with join_wide: wide gives `m_a = … − 10,0 kg` on one row and each further `=` on its own row; the phone keeps its rows), or make join_wide never join a relation to a row that starts with `\cdot`, `+` or `-`.

## Polish
(none)

## Checked
- Delta: the two re-broken chains (Pohdinta's retrieval feedback `kx = 40 N/m · 0,050 m = 2,0 N`; the astronaut task's Sijoitus), opened with ?ratkaisut=1 on the preview of this hash; own element captures at 390 and 1280 px (scratchpad v/M-fy5-9-390.png, M-fy5-9-1280.png).
- Feedback chain: two aligned rows at both widths, comma inside the box, the sentence continues under it; fine.
- Astronaut chain at 390 px: four rows, `=` in one column, the `−` row starts the continuation, fraction legible, nothing clipped, page scrollWidth 390.
- 1280 px: defect above.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
