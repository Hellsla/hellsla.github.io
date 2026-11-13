VERDICT: PASS
CONTENT-HASH: 78ee8836595b68b1
SCOPE: delta added-exercise from daa6fc4f95361ced base 81db4a6fd727

## Blocking
(none)

## Polish
- content/en/FY3/fy3-13/exercises/solutions.md fy3-13-L2-10 Principle — "The points are on a straight line"; L2-09 and the data say "almost on a straight line". The task's stated assumption covers it; align the wording in both languages if touched.
- content/en/FY3/fy3-13/exercises/exercises.json fy3-13-L1-09 — a 4 % tolerance on an exact table value accepts about -262 to -284 °C; harmless, same in the Finnish.

## Checked
- fy3-13-L2-09 (zero point now calculated from the slope): k = (102.5 - 75)/(100 - 0) = 0.275 kPa/°C, theta_0 = 0 - 75/0.275 = -272.7 °C, as answers.py. The solution says rightly that the axis (to -150 °C) does not reach zero pressure, so the zero is calculated, not read.
- L2-09 independent check: my least-squares fit of the five points gives k = 0.276 kPa/°C and theta_0 = -272.1 °C; the 5 % tolerance (-259 to -286 °C) is consistent with the stated uncertainty of about ten degrees or more from 1 kPa readings (slope about 4-5 % uncertain).
- L2-09 conditions: rigid closed container (constant V and n) stated; extrapolation beyond the measured range named and justified by the near-straight line (guardrail on extrapolation).
- fy3-13-L2-10: theta = 200 - 273.15 = -73.15 °C, p = 75 + 0.275 * (-73.15) = 54.88 kPa; linearity outside the range is stated in the task; -73 °C lies on the drawn axis, so the by-eye range 53-57 kPa is fair and inside the 5 % tolerance; p proportional to T check 75 * 200/273.15 = 54.9 kPa is real.
- fy3-13-L1-09: T = theta + T_0 with T_0 = 273.15 K gives theta_0 = -273.15 °C; the statement that no temperature is below absolute zero is correct.
- Solutions complete: given, principle, symbolic solution first, conversions, substitution, rounding reason, check.
- Scripted comparison with the Finnish exercises.json: all 24 exercises have the same answers, units, tolerances, figures and task-text numbers; every answers.py value within its tolerance.
- Hash identical at start and end.
