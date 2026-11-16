VERDICT: FAIL
CONTENT-HASH: 6e37004d3da61954

## Blocking
- [Major] solutions.md fy5-7-L3-02 (task 7-18), Sijoitus (fy5-7-open-exercises-L3-1280-2.png and own capture at 1280 px) — the wide form shows `x = 15 cm` alone on row 1 and `· sin(2π · 0,75 Hz · 0,20 s) = 15 cm · sin 0,9425` on row 2: row 1 reads as a finished (false) equation and the second equals sign stands mid-row, out of the column of the others, though `x = 15 cm · sin(…)` fits one row — against "one equation on one row when it fits; every = in one column" (teacher 2026-11-13) — `mathlayout.join_wide` takes the continuation row `&\cdot \sin(…)` for a bare left side and joins the next `=` row to it. Fix: write the continuation as `\\ &\quad \cdot \sin(2\pi \cdot …)` (tried with join_wide: wide gives `x = 15 cm · sin(…)` on one row, each further `=` on its own row; the phone keeps its rows), or make join_wide never join a relation to a row that starts with `\cdot`, `+` or `-`.

## Polish
- [Minor] fy5-7-L2-04 Järkevyys — the word "ja" stands alone on a row between the two display formulas; acceptable, but one aligned block with both rows would read more calmly.

## Checked
- Delta: the three re-broken formulas (L1-03 Järkevyys, L2-04 Järkevyys, L3-02 Sijoitus), solutions opened with ?ratkaisut=1 on the preview of this hash; own element captures at 390 and 1280 px (scratchpad v/M-fy5-7-390.png, M-fy5-7-1280.png).
- L1-03, L2-04: display formulas fit at 390 px with their comma inside the box, sentence continues naturally under them; fine at 1280 px.
- L3-02 at 390 px: five rows, equals signs in one column, nothing clipped, page scrollWidth 390.
- Packet capture fy5-7-open-exercises-L3-1280-2.png: card layout around the opened solution intact.
- The caption change (esimerkkiaineisto marker removed) is the teacher's approved category; not judged here.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
