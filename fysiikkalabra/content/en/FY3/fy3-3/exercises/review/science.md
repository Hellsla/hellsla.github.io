VERDICT: PASS
CONTENT-HASH: 622d819e7af597e2
SCOPE: delta added-exercise from ba420448372c48ee base 89bcb63b7431
Round: 1
Mode: delta

## Blocking
(none)

## Polish
- content/en/FY3/fy3-3/exercises/solutions.md (fy3-3-L2-08, Answer) — stated accepted range 53–56 °C differs from the 4 % tolerance (52.3–56.7 °C); harmless, same in the Finnish — align the range with the tolerance in both languages if touched.

## Checked
- fy3-3-L1-10: T = theta + 273.15 with N2 boiling point -196 °C -> 77.15 K; 77 K accepted; MAFY value (-195.8 °C) within tolerance.
- fy3-3-L2-08: constant-volume linearity is stated as an assumption in the task; end-point slope 0.275 kPa/°C -> 54.5 °C; my least-squares fit gives 54.0 °C (and -272 °C intercept), both inside tolerance.
- Figure fy3-3/extrapolation-points: points also given in the text and description; no line, no answer given away.
- Solutions complete (seven parts), symbolic before substitution, rounding reason right.
- answers.py lines equal my recomputation; numbers, unit, tolerance and figure identical to the passed Finnish.
- Hash identical at start and end.
