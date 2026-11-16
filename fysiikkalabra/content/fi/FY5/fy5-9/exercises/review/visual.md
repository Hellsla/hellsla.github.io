VERDICT: FAIL
CONTENT-HASH: dd52f502ff1212e4

## Blocking
- [Major] solutions.md fy5-9-L2-04, Sijoitus (own capture at 1280 px, wide form from 700 px) — the wide form shows `A² − x² = (0,100 m)²` on row 1 and `− (0,0500 m)² = 0,00750 m²,` on row 2: the result's equals sign stands mid-row, out of the column of the first, and row 2 reads at a glance as its own equation, though the whole difference fits one row — against "one equation on one row when it fits; every = in one column" (teacher 2026-11-13) — `mathlayout.join_wide` takes the continuation row `&- (0{,}0500\,\text{m})^2` for a bare left side and joins the `=` row to it. Fix: write the continuation as `\\ &\quad - (0{,}0500\,\text{m})^2` (tried with join_wide: wide gives `A² − x² = (0,100 m)² − (0,0500 m)²` and `= 0,00750 m²` under it; the phone keeps three rows), or make join_wide never join a relation to a row that starts with `\cdot`, `+` or `-`.

## Polish
- [Minor] fy5-9-L2-07 Järkevyys — the parenthesis is now two inline formulas, so on a phone the line breaks before `= 23,5 N/m)`; a break at a relation, fine as it is.

## Checked
- Delta: L2-04 Sijoitus, L2-06 Järkevyys (`2π√(0,300 : 20,14) s = 0,767 s` lifted to a display row), L2-07 Järkevyys, opened with ?ratkaisut=1 on the preview of this hash; own element captures at 390 and 1280 px (scratchpad v/M-fy5-9-390.png, M-fy5-9-1280.png, vis789/L204-390.png, L204-1280.png).
- 390 px: L2-04 three rows with `=` in one column and the `−` row as continuation; L2-06 display row fits with its comma; nothing clipped, page scrollWidth 390.
- 1280 px: L2-06 and L2-07 read well; L2-04 defect above.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
