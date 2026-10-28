VERDICT: FAIL
CONTENT-HASH: 74b0725cf058af36

Delta review over the audit's PASS (d88a831999bf6f9a): L2-03 replaced by figure task extrapolation-points.

## Blocking
- exercises.json:68 (fy3-3-L2-03) — solutions.md:75 says a by-eye line giving 45–50 kPa is accepted, but tolerance 0,05 on 47,5 accepts only 45,1–49,9 kPa. The grid is 25 kPa, and the last point (102,5 kPa) lies only 1/10 of a cell above the 100 kPa line. Reading it as 100 kPa, which is reasonable, gives slope 0,25 kPa/°C and 50 kPa, and that answer is rejected. Fix: tolerance 0.06 (44,7–50,4 kPa); no wrong method lands there.
## Polish
- The middle points (82, 89, 96 kPa) are not on gridlines and can only be estimated on a 25 kPa grid; the solution rightly uses only the end points.
## Checked
- Recomputed: k = (102,5 − 75)/100 = 0,275 kPa/°C, p(−100 °C) = 75 − 27,5 = 47,5 kPa; Kelvin check 75 · 173,15/273,15 = 47,54 kPa; answers.py 47,5.
- Figure extrapolation-points: points are 75·T/273,15 rounded (81,9/88,7/95,6/102,5), physically consistent for constant volume; axis reaches −150 °C; description lists the points, not the extrapolated value.
- Task states the linearity assumption beyond the measured range (guardrail: extrapolation is justified and stated); 48 kPa with two significant figures is justified.
