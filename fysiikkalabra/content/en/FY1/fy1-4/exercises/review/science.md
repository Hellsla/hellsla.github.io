VERDICT: PASS
CONTENT-HASH: 4d4f1e7d3a800203

## Blocking
- none

## Polish
- solutions.md:183 (fy1-4-L3-04) — "stretched beyond its elastic range, so the extension is no longer directly proportional" runs together the limit of proportionality and the elastic limit. A spring can stop being linear and still be elastic (C/B borderline, not blocking at FY1 level). Fix: "the load is beyond the range where the extension is proportional to the load; a spring loaded this far may also be left permanently stretched".
- exercises.json:122 (fy1-4-L1-09) — the stored answer 121.5 g has four significant figures, but the solution gives 1.2·10² g from the two-figure volume. It is inside the 4 % tolerance. Optionally store 121.5 and show 1.2·10², or say in the task how many figures to give.
- solutions.md:109 (fy1-4-L3-02) — "two significant figures, because the temperatures were measured to two figures": the limiting data are the differences 18 °C and 9 °C. Optionally justify the rounding from those differences.
- exercises.json:174, :375 — the answers are stored as 0.08 while the solutions give 0.080 mm/g. Storing 0.080 is equivalent in JSON. Only a display question.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas and fits (numpy polyfit). All match exercises.json and answers.py within tolerance (L2-04: 1.758 against the stored 1.8, inside 3 %).
- By-eye fits are bracketed by least squares: L2-02 k = 0.48 m/s, b = 0.05 m → 3.89 m. L2-05 0.0797 mm/g. L2-06 b = 0.829 m. L2-07 2.707 and 7.835 g/cm³ (Al and Fe plausible), ratio 2.89.
- L3-04: the residuals of the 100–500 g fit are at most 0.24 mm. At 600 g and 700 g they are 3.5 mm and 12.6 mm, as the solution states.
- L3-05: half-range uncertainty 0.075/0.475 = 15.8 %. The student's 32 % is double. The least-squares slope of all six points, 0.51 m/s, is inside 0.40–0.55. The guardrail wording ("estimated range, not guaranteed") is there.
- L3-03: the relative slope error scales as 1/Δx, so the ratio is 8.0/0.5 = 16. The worst-case 2·0.1 is stated.
- L3-01: the assumption of steady motion before the stopwatch was started is in the task, and the solution names the extrapolation (t < 0).
- MC L1-06, L1-07, L2-08: exactly one correct option each. Every distractor is really wrong and its feedback gives the right reason. The fitting guardrails are met: the line goes through the middle of the points, no broken line, and a point is left out only for a found gross error.
- Units and magnitudes are realistic: a sheet is 4.8 g, water 1.0 kg/l, the cyclist 9 km/h, the coffee cooling slows toward room temperature.
- Every solution has the seven parts and is solved in symbols before substitution. The conversions are right (km/min → m/s, kg/m³ → g/cm³).
- Scope: linear models and slopes only. Nothing from later courses.
