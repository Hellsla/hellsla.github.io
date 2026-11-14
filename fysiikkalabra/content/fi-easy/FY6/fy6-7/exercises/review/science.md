VERDICT: PASS
CONTENT-HASH: c394b79ded28d3d9
SCOPE: delta added-exercise from 0a3ba204ab582e2e base 8f23aa7ae3bd

## Blocking
- none

## Polish
- solutions.md fy6-7-L2-08 Vastaus — "arvot luetaan 0,4 kW:n ruudukkoviivoilta": 0,2 kW lies halfway between gridlines (2,4 and 1,2 kW are on them) — say "0,2 kW on kahden viivan puolivälissä"; the effect on the cost is about ±1 %, inside the tolerance.

## Checked
- fy6-7-L1-10 recomputed: E = 1,5 kW · 2,0 h = 3,0 kWh = 3,0 · 3,6 MJ = 10,8 MJ; matches answers.py and exercises.json; rounded 11 MJ is +1,9 %, inside tolerance 0,04. The MAFY conversion 1 kWh = 3,6 MJ is exact and agrees with the brief.
- fy6-7-L2-08 recomputed: E = 2,4 · 0,5 + 1,2 · 1,0 + 0,2 · 0,5 = 2,5 kWh, K = 0,18 €/kWh · 2,5 kWh = 0,45 €; matches; unit €, tolerance 0,03.
- Figure fy6-7/dryer (figures.py): steps 2,4 / 1,2 / 0,2 kW on 0–0,5 / 0,5–1,5 / 1,5–2,0 h, gridlines 0,4 kW and 0,25 h; alt text gives the same; no energy or cost shown.
- Model: constant power per stage, E = Pt summed, K = aE without fixed fees (one appliance), as in the brief's worked example.
- Both solutions complete (principle, symbolic formula, conversions, substitution, rounding reason, check).
- Content hash checked at start and end.
