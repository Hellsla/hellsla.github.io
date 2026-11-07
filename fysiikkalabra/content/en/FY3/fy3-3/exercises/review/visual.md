VERDICT: PASS
CONTENT-HASH: ba420448372c48ee
Mode: delta
Round: 1

## Blocking
- none

## Polish
[Minor] Feedback 'so the unit is the unit of pressure divided by the unit of temperature' is clumsy; 'so c has the unit of pressure divided by the unit of temperature'.

## Checked
- delta review 2026-11-07 round 4 (three small fixes): L1-04 substitution now $\Delta T = (45 - 20)\,\text{K} = 25\,\text{K}$, matching L2-01; the round-3 Minor note on it is resolved (source-checked, a one-line inline formula).
- delta review 2026-11-07 round 3 (fixes to round 2 findings): L2-01 now $T_2 = (288 + 45)\,\text{K} = 333\,\text{K}$ (round-2 Minor fixed); L1-04 Kaava shows the constant cancelling in slash form, L2-04 ratio has $\theta/{}^\circ\text{C} + 273.15$ above and below. Opened fy3-3-en-l3a-390 and -l3b-390: inline Kaava wraps at sensible points, the ratio display fits the card, no clipping.
- delta review 2026-11-07 round 2 (follow-up consistency edits): every Kaava now $\tfrac{T}{\text{K}} = \tfrac{\theta}{{}^\circ\text{C}} + 273.15$ (and its solved forms), every substitution $T = (\ldots + 273.15)\,\text{K}$ / $\theta = (\ldots - 273.15)\,{}^\circ\text{C}$; read all hunks in the diff and opened fy3-3-en-l2sol-390: aligned display, brackets and unit render cleanly, results unchanged.
- New task fy3-3-L1-09 at 390 px (en), own render of preview/en/fy3-3.html: task text, every option and its feedback open, solution card open; page and card have no horizontal overflow (scrollWidth equals width).
- Delta covers only the new task and its solution; surrounding exercises were not changed.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
