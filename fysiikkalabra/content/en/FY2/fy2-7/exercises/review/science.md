VERDICT: PASS
CONTENT-HASH: f1594abe34d25f92
SCOPE: delta added-exercise from 308374a464834f8a base 611fb7d5c174

## Blocking
(none)

## Polish
- content/en/FY2/fy2-7/exercises/exercises.json fy2-7-L1-09, L2-09 — "A day, ..." / "A week, ..." read oddly — "In a day, ..." / "In a week, ...".
- content/en/FY2/fy2-7/exercises/solutions.md fy2-7-L2-09 — three figures justified by 250 MWh although the read shares 4 % and 9 % limit it (same in fi) — could say the shares are exact figure values.

## Checked
- L1-09: 0.040 x 500 kWh = 20 kWh = 72 MJ (1 kWh = 3.6 MJ exact).
- L2-09: fy2-7/sankey shares 4 % and 9 %; 0.09 x 250 - 0.04 x 250 = 12.5 MWh; loss as share of energy sent, as the lesson.
- check script (one run): every added answer recomputed from the task text with my own formulas, equal to answers.py and exercises.json; answer, unit, tolerance, figure and lookup identical to the reviewed Finnish; every number of the task texts and solutions identical en/fi.
- MAFY lookup values agree with docs/mafy-arvot.tsv (VERIFIED 2026-11-12).
- No scope breach, no guardrail break (A or B) found.
