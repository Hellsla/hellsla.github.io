VERDICT: FAIL
CONTENT-HASH: 3965ec0c72c40709

## Blocking
- [Major] inquiry.json, Laskutehtävä "kansi", Sijoitus (own capture at 1280 px, wide form from 700 px) — the wide form reads `x = 4,0 cm` on row 1 and `· sin(2π · 0,50 Hz · 0,40 s) = 4,0 cm · sin 1,257` on row 2: the first row looks like a finished (false) equation, and the second equals sign stands mid-row, out of the column of the others, although the card has room for `x = 4,0 cm · sin(…)` on one row — against "one equation on one row when it fits; every = in one column" (teacher 2026-11-13) — `mathlayout.join_wide` takes the continuation row `&\cdot \sin(…)` for a bare left side and joins the next `=` row to it. Fix: write the continuation in the house form `\\ &\quad \cdot \sin(2\pi \cdot …)` (tried with join_wide: wide gives `x = 4,0 cm · sin(…)` on one row and each further `=` on its own row, the phone form keeps its rows), or make join_wide never join a relation to a row that starts with `\cdot`, `+` or `-`.

## Polish
(none)

## Checked
- Delta: the one re-broken chain (Testaa ja arvioi, Laskutehtävä, Sijoitus), solution opened with ?ratkaisut=1 on the preview of this hash; own element captures at 390 and 1280 px (scratchpad v/M-fy5-7-390.png, M-fy5-7-1280.png).
- 390 px: five rows, equals signs in one column, continuation row starts with `·`, nothing clipped, page scrollWidth 390, no formula scrolls.
- 1280 px: defect above; rows 3–4 aligned, units upright, decimal comma.
- Packet capture fy5-7-open-exercises-L3-1280-2.png for the card layout around an opened solution: intact.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
