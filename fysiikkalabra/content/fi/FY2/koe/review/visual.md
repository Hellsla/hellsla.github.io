VERDICT: PASS
CONTENT-HASH: c60065f851f0237e
Round: 1 (work queue 5d, carry-item reflow, #612; full packet, judged on the three re-broken blocks and their surroundings)

## Blocking
- none

## Polish
- [Minor] solutions.md fy2-k6 a) Sijoitus (untouched text; page-1280-26) — at 1280 px the two inline `\dfrac` fractions fall on consecutive text rows and collide: the denominator "13 700 MW" touches the numerator "900 MW" of the row below. Both stay legible, and at 390 px the rows are clear, so it is not Critical, but it is the weakest spot of the block and the same clipped-formula family this round repairs — lift the two cases to their own rows (Kello 3 and Kello 18 each an `aligned` display, or `\tfrac` inline), with the next change to this solution.
- [Minor] solutions.md fy2-k2 c) Sijoitus (page-390-10/11, page-1280-8) — the word "hinta" stands alone on a text row and the box below opens with a bare "=", also at 1280 px where the whole chain would fit on one row — put the quantity inside the display: `\text{hinta} &= 42{,}7\,\text{kWh} \cdot …`, as the Kaava row above has it.
- [Minor] solutions.md fy2-k6 a) Kaava (page-1280-26) — the sum $P_\text{tuotanto}$ keeps its two rows at 1280 px although it fits one (the Vastaus chain beside it does rejoin on one row) — acceptable under the 2026-11-15 decision; a shared-component matter, not this text's.

## Checked
- review/shots/reflow-item-1.png (the three changed blocks at 390 px): every row inside its box, nothing clipped, `=`/`≈` in one column, the `+` continuation row indented past the `=`, terms and units whole, decimal commas, thin spaces, upright units, `\cdot`.
- FY2-koe-page-390-10, -11 (k2 b–d open), -33, -34 (k6 a–b open): the blocks in context; boxes stay inside the solution card, spacing and hierarchy intact, "…= 3500 MW," followed by "joten sähköä vietiin." reads as one sentence.
- FY2-koe-page-1280-8 and -26: the same blocks on a laptop; no overflow, reading column intact.
- contact-1, -3, -9, -11 for triage of the open page at both widths; no layout break around the changed blocks.
- Not re-inspected (outside this round's scope, passed earlier): the figure fy2-k4-bars, the opening, tasks.json texts, the other solutions. Finnish of the changed lines is unchanged apart from the row breaks.

## Scores
illustrations 4 (not re-judged) · typography 4 · Finnish 4 · accessibility 4
