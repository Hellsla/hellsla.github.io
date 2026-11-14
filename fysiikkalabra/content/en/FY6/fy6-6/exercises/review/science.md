VERDICT: PASS
CONTENT-HASH: 7520b3a6aa4c65ec
SCOPE: delta added-exercise from e256d772fd4b7515 base c7f5e91173b0

## Blocking
- none

## Polish
- exercises/solutions.md fy6-6-L2-09 Answer — "three significant figures, because the values are read exactly from the gridlines": the durations are given as 3.0, 5.0, 4.0 min (two figures) and the task says 12 min; "780 kJ ≈ 7.8 · 10² kJ, two significant figures like the durations" would match the data better. The tolerance 0.02 accepts either.

## Checked
- fy6-6-L2-09 recomputed: E = 2000 W · 180 s + 1000 W · 300 s + 500 W · 240 s = 360 kJ + 300 kJ + 120 kJ = 780 kJ; answers.py and exercises.json agree; unit kJ, tolerance 0.02.
- Figure fy6-6/ex-pt (figures.py): steps (0–3, 2000 W), (3–8, 1000 W), (8–12, 500 W) with vertical joins; gridlines 500 W and 1 min, so every value lies on a gridline; ends at 12 min as the task asks; no energy shown; description gives the same values.
- Physics: E = Pt per constant-power step and the sum (area under the (t, P) graph); a resistive hob plate turns the electrical energy into internal energy of the plate, as the task says.
- Conversions min → s correct; average power 780 kJ : 720 s = 1.08 kW lies between 0.5 and 2.0 kW: a real check.
- Solution complete (given, principle with condition "power constant", symbolic sum, conversions, substitution with units, rounding, check).
- Inside FY6 central contents (electric power and Joule's law); builds on FY2 energy.
- Content hash checked at start and end.
