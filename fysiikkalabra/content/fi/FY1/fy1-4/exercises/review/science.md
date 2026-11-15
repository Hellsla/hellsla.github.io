VERDICT: PASS
CONTENT-HASH: e4df69026a6db390

## Blocking

## Polish
- content/fi/FY1/fy1-4/exercises/solutions.md:162 — The corrected line is now arithmetically consistent: 0,83 m + 2,2 m ≈ 3,0 m. But 0,448 m/s · 5,0 s = 2,24 m, so the line's own value at 5,0 s is 3,07 m (the solution's read point), and the last measurement is 3,09 m. "≈ 3,0 m, mikä vastaa viimeistä mittausta" is true only roughly — optionally write "noin 2,24 m … ≈ 3,07 m", which matches the read point (5,0 s; 3,07 m) used two lines above.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas (two-point slopes, b = y1 − kx1, my own least-squares fits for the by-eye data tasks). All agree with exercises.json and answers.py within tolerance. L2-06: b = 0,829 m, v = 0,448 m/s; L2-07: 7,835/2,707 = 2,89; L3-04: 0,0802 mm/g over 100–500 g, residuals at 600 and 700 g are +3,5 and +12,6 mm, and inside the range |r| ≤ 0,24 mm; L3-05: 0,075/0,475 = 15,8 %, the six-point fit gives 0,51 m/s.
- L1-09 water sentence: 45 cm³ of water is 45 g, and 121,5 g / 45 g = 2,7. Correct and consistent with ρ = 2,70 g/cm³. Rounding 1,2·10² g is inside the 4 % tolerance.
- L2-06: the reason the line misses the origin (the cart was 0,83 m from the mark when the clock started) is right. The by-eye range 0,75–0,91 m matches tolerance 0,10.
- L3-01: the assumption (same speed before the clock started) is stated in the task and used in the solution. The sign reasoning is right.
- L3-02: the slopes −1,8 / −1,2 / −0,90 °C/min and the cooling mechanism (shrinking temperature difference) are correct.
- L3-03: worst-case reading error 2·0,1 is consistent. The ratio is 8,0/0,5 = 16.
- L3-04: the proportional range, the extrapolation condition and the overload explanation fit FY1 (C).
- L3-05: half the difference is the uncertainty, and "ei takaa" is stated, per the guardrails.
- Multiple choice L1-06, L1-07, L2-08: exactly one correct option each. Every distractor's feedback is right. The outlier wording follows the guardrails.
- Notation (k, b, y = kx + b, \textsf{l}), units, significant-figure reasons and scope (linear models only) are all within FY1 and the brief's lesson. The hash was the same at start and end.
