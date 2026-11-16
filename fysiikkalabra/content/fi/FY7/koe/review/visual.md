VERDICT: PASS
CONTENT-HASH: 6d4426affade3fc5

## Blocking
(none)

## Polish
- [Major, may wait: known, listed issue, work queue 5d] shots/FY7-koe-stage-osa-3-390-5.png (task 6 c, Sijoitus; solutions.md:305-306) — at 390 px the rows "1,728 MW · 4000 h = 6912 MWh", "0,0571 MW · 4000 h = 228,5 MWh" and "= (6912 MWh − 228,5 MWh) · 50 €/MWh = 334 200 €" are clipped. I confirmed it in the capture. It may wait because the rows are in docs/clipped-formulas.tsv (FY7-koe, lines 60-62), the fix is the separate re-break PR of item 5d (own PR, no other content changes), the lines are not part of this change, and the clipped step's result still shows in Vastaus and Järkevyys. Do it in 5d; a new visual look is needed after the re-break.
- [Minor] fig-3 / fig-12 — markers and error bars are small at 390 px; make them a little larger.
- [Minor] osa-2-390-4 (task 2 b, Järkevyys) — the unit fraction 1/(T²·m²/V) = V/(T²m²) is tiny in its display box; set it larger or inline.
- [Minor] fig-6 — the t-axis numbers sit at the bottom of the plot, not on the axis; ticks on the axis would be clearer.

## Checked
- top-390, fig-1, fig-3, fig-6, fig-12 (graphs: quantities, units, ticks, labelled points fine); fig-2, 4, 5 and 14 (inline formulas render and read).
- stage-osa-1-390-1, osa-2-390-1, osa-2-390-4, osa-2-390-12, osa-3-390-1, osa-3-390-5; page-1280-5 (opened model answer, wide layout).
- Not opened: the contact sheets and the other page-390/1280 parts. The verdict rests on this sample.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
