VERDICT: PASS
CONTENT-HASH: a160a51a52b7e3ef
Review of the recognition chart (queue 9c) and the term change against the version passed at 62a144b4944a81b5; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- A: aria-label ends 'pinta- ala' (stray space inside the word, read aloud as two words); write 'pinta-ala'.
- B: pill \Delta x = \frac{v_0+v}{2}t has small \frac type (about 11 px at 360 px); use (v_0+v)t/2 or (v_0+v)/2 \cdot t inline.

## Checked
- Opened docs/figures/fy9-tunnistus/fy9-liike-fi-360.png: 7 rows (x(t) … pinta-ala); no label clipped, overlapping or cramped, white on #1a4d2e pills legible, pill style, spine, start box and spacing identical to the other units' charts, all labels LaTeX (upright names, italic symbols).
- ARIA_KARTTA in lessons/units/fy9-liike/figures.py read against every row: Finnish, complete, same rows in same order, matches the chart.
- Diff: teacher.md 'käsitekartta' -> 'tunnistuskaavio' and the figure code; remaining diff lines (unit.md text) read for wording and term consistency.
