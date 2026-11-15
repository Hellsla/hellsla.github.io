VERDICT: PASS
CONTENT-HASH: d8caf555a4e34ae3
Review of the recognition chart (queue 9c) and the term change against the version passed at 4fca163bc3ac2f29; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: pill \Delta x = (x_max - x_min)/2 is set as a \frac with tiny sub/superscripts (about 10 px at 360 px); write it inline with a slash and brackets like the other pills.
- C: header 'mistä tunnistan lain?' fits laws less well than methods here; 'mistä tunnistan menetelmän?' would read better (optional).

## Checked
- Opened docs/figures/fy9-tunnistus/fy9-kokeellisuus-fi-360.png: 7 rows (paras arvio … b≠0); no label clipped, overlapping or cramped, white on #1a4d2e pills legible, pill style, spine, start box and spacing identical to the other units' charts, all labels LaTeX (upright names, italic symbols).
- ARIA_KARTTA in lessons/units/fy9-kokeellisuus/figures.py read against every row: Finnish, complete, same rows in same order, matches the chart.
- Diff: teacher.md 'käsitekartta' -> 'tunnistuskaavio' and the figure code; remaining diff lines (unit.md text) read for wording and term consistency.
- Term change liikekitka -> liukukitka in the two changed lines: consistent, lepokitka kept.
- Also looked at the 1280 capture: same fixed-width chart, no overflow.
