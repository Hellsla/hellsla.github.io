VERDICT: PASS
CONTENT-HASH: b8ad0d8a294d0e11

Delta review over the audit's PASS (eddc57610d8a36e9): L2-02 (tank line from two given points) replaced by a by-eye fit and extrapolation on fy1-4/scatter-points; LaTeX in L1-03.

## Blocking
(none)
## Polish
- solutions.md:64 — "eikä minkään kahden pisteen kautta" reads as a rule that a fit may not pass through two points; the guardrail only forbids choosing two points to define it. Write "eikä valittujen kahden pisteen kautta".
## Checked
- Figure: the six CART points (1; 0,6) … (6; 2,9) on a 1 s × 0,5 m grid to 9 s and 4,5 m; same data as the lesson's scatter; no line shown; description lists points only.
- Recomputed at t = 8,0 s: least squares k = 0,480 m/s, b = 0,053 m → 3,89 m; through origin 3,94 m; lesson line 0,5t → 4,0 m; line through first and last point 3,82 m. Tolerance 0,08 → 3,59…4,21 m accepts all, rejects 2,9 m (no extrapolation).
- Solution's two points read off the fitted line (0; 0,0) and (6,0; 2,9), slope 0,483 → 3,87 ≈ 3,9 m; range 3,6…4,2 m stated; extrapolation flagged as less certain; 2 sig. figs justified.
- L1-03 LaTeX only: (10 − 4,0)/0,60 = 10 vrk.
