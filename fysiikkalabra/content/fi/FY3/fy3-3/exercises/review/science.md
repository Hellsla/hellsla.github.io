VERDICT: PASS
CONTENT-HASH: d88a831999bf6f9a

## Blocking

## Polish
- solutions.md fy3-3-L1-05 (and L1-03) — the rounding reason "kaksi merkitsevää numeroa kuten arvossa 2,7 K" applies the multiplication rule to a sum; L1-01 and L2-01 in the same set correctly use the decimal-place rule ("täysinä asteina"). By that rule the answer is −270,5 °C. The tolerance accepts both; make the reason consistent (e.g. "yhden desimaalin tarkkuudella kuten 2,7 K" with −270,5 °C, or say the house 2-s.f. convention is used).
- solutions.md fy3-3-L2-04 — Vastaus "4,00 kertaa" while exercises.json/answers.py give 4.0; choose one.
- solutions.md fy3-3-L2-03 — "Kuvaajan lukeminen" refers to a graph the task does not show; "kun pisteet piirretään kuvaajaan" would match the task text.

## Checked
- Recomputed all twelve answers in one script with my own formulas: 294 K, 77 °C, −196 °C, 25 K, −270 °C, 60 °C, 101,6 → 102 kPa, 86,9 → 87 kPa, 3,996 → 4,0, 320,8 → 321 kPa, 127,05 → 127 °C, −126,6 → −127 °C; answers.py prints the same values.
- Every proportionality task states its condition in the task (rigid closed vessel / tyre not leaking and same volume; "suoraan verrannollinen kelvinlämpötilaan"); L2-02 and L2-03 state the linear assumption.
- Data realistic: the 90,0 → 123 kPa and 110 → 137 kPa pairs match p ∝ T to within 0,2 %; 300 kPa absolute tyre pressure plausible; N₂ 77,4 K, CMB 2,7 K, Moon 100 K/400 K correct.
- L3-03 uses "mean kinetic energy ∝ T" with the dilute-gas condition named in the solution, as in the lesson.
- Each solution complete (given/asked, principle, symbolic form, conversions, substitution, rounding reason, reasonableness check); distractor checks (Celsius ratios 700 kPa, 36 °C, 10 °C) recomputed and right.
- Units and tolerances (0,02) fit the data's precision; notation T, θ, 273,15 as in the lesson.
- Extrapolation in L2-03 says it goes beyond the measured range and is cross-checked against p ∝ T (86,7 kPa).
