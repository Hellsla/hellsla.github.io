VERDICT: PASS
CONTENT-HASH: 2018749175b6d30f
SCOPE: delta added-exercise from ba420448372c48ee base 81db4a6fd727

## Blocking
(none)

## Polish
(none)

## Checked
- fy3-3-L1-10: T = theta + 273.15 with the MAFY boiling point of N2, -196 °C, gives 77.15 K, answer 77 K; the real value -195.8 °C (77.4 K) is inside the 4 % tolerance; liquid nitrogen at its boiling point at normal pressure is the right physics.
- fy3-3-L2-08 (new question: temperature at 100 kPa): constant volume and linearity are stated in the task; slope from the far-apart points (0; 75) and (100; 102.5) is 0.275 kPa/°C, theta = (100 - 75)/0.275 = 90.9 °C.
- Independent check: my least-squares fit of the five points gives slope 0.276 kPa/°C, intercept 75.1 kPa and theta = 90.2 °C; linear interpolation between (75; 96) and (100; 102.5) gives 90.4 °C. All are inside the 8 % tolerance (84–98 °C as the solution says), and the tolerance covers the reading error of about 1 kPa on the 25 kPa grid.
- The reasonableness check (between 75 and 100 °C, nearer 100) is a real check and agrees with the data; the answer to two figures is justified by the reading precision.
- Figure extrapolation-points: points and grid as the solution reads them; description lists the points but not the answer.
- Solutions complete: given, principle, symbolic solution first, conversions, substitution, rounding reason, check.
- Scripted comparison with the Finnish exercises.json: all 23 exercises have the same answers, units, tolerances, figures and numbers in the task texts. Every answers.py value is within its tolerance.
- Hash identical at start and end.
