VERDICT: PASS
CONTENT-HASH: 44d102baf5907a2c
SCOPE: delta added-exercise from 38935656dc0691fb base 8f23aa7ae3bd

## Blocking
(none)

## Polish
(none)

## Checked
- Delta: only the added exercise fy6-16-L2-09 judged; the rest unchanged per `reviews.py added_exercises`.
- Figure talo-ex (figures.py): steps 2 / 5 / 7 / 3 kW for 18–19 / 19–20 / 20–21 / 21–22 h, every step on a 1 kW gridline and every edge on an hour line; the description gives the same values; no energy or cost written.
- Physics: constant power in each hour, so W = ΣP_i Δt (area under the (t, P) graph) and cost K = aW — correct.
- Recomputed: W = (2 + 5 + 7 + 3) kW · 1.0 h = 17 kWh; K = 0.16 €/kWh · 17 kWh = 2.72 € = answers.py; 2.7 € is 0.7 % off, inside the 2 % tolerance.
- Conversion c/kWh → €/kWh right; formula stated symbolically before substitution; rounding reason given.
- Reasonableness check real: mean power 4.3 kW lies between the smallest and largest step; magnitude (17 kWh in an evening for a house) realistic.
- Scope: electric energy and its cost (FY6 power and household energy, applied chapter).
