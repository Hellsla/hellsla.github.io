VERDICT: PASS
CONTENT-HASH: 753f6c76a98443bb
Review of the recognition chart (queue 9c) and the term change against the version passed at 0944d5d3eb93fbe8; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- A: aria-label has double spaces (line-join artefacts after 'mikä', 'kertaa', 'jännite', 'suhde'); harmless to screen readers, tidy for cleanliness.

## Checked
- Opened docs/figures/fy9-tunnistus/fy9-magnetismi-valo-fi-360.png: 9 rows (F_M … hilayhtälö); no label clipped, overlapping or cramped, white on #1a4d2e pills legible, pill style, spine, start box and spacing identical to the other units' charts, all labels LaTeX (upright names, italic symbols).
- ARIA_KARTTA in lessons/units/fy9-magnetismi-valo/figures.py read against every row: Finnish, complete, same rows in same order, matches the chart.
- Diff: teacher.md 'käsitekartta' -> 'tunnistuskaavio' and the figure code; remaining diff lines (unit.md text) read for wording and term consistency.
