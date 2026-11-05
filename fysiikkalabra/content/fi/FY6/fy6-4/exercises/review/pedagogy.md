VERDICT: PASS
CONTENT-HASH: 0bbb7ef633d3e151

## Blocking

## Polish
- exercises.json L2-06 vs L3-04 — same scenario twice (R_1 in series with two parallel resistors, one branch open, found from meter readings; L2-06 even gets R_23 ≈ R of one resistor) — change L2-06's fault, e.g. R_2 and R_3 wired in series instead of in parallel (U_23 = 6,0 V, I = 18 mA, R_23 = 333 Ω), so the two tasks test different diagnoses.
- exercises.json L2-05 a) — comparing the calculated and measured value with ±1,5 % ignores that the calculated one also carries the readings' errors — add to the solution one sentence: "myös laskettu arvo on epävarma, joten ero 0,4 % on selvästi virherajan sisällä".
- exercises.json L1-08 — solving 1 : R_x = 1 : R − 1 : R_1 needs fraction algebra, harder than the other level 1 tasks and close to L2-03 (unknown parallel resistor) — keep, but the solution's common denominator step (5 − 2) : 180 deserves one line explaining where 180 comes from (lcm of 36 and 90).
- solutions.md L2-07 Vastaus — "40 Ω, mutta laskennassa 40,4 Ω" contradicts the answer field 40,4 — write "R_x ≈ 40 Ω (laskimen arvo 40,4 Ω)".
- solutions.md L3-05 — the elimination for series (only 100 and 390 can be below 470) is good; add "yksi kutakin" as the reason 390 + 100 is the only series pair, so the student sees why the pair 390 + 390 is not allowed.

## Checked
- Counts 8/7/5 and kinds match docs/exercise-bank/FY6.md (smallest R MC, "parallel raises R" misconception MC, unknown parallel R, measured vs calculated with ±1,5 %, wiring error from meters, 180 Ω vs 125 Ω, E12 selection for 470 Ω).
- Recomputed: L1-08 60 Ω; L2-05 1013 Ω and 102,1 Ω; L2-06 198 Ω (fault: one branch open, 30 mA); L2-07 24,13 Ω and 40,4 Ω; L3-04 125 Ω, 180 Ω, 36 mA; L3-05 463,8 Ω and 1,32 %, and every other pair is worse. All match answer fields.
- L1-06 and L1-07: one correct option, each distractor a known misconception (series for lowest, "more resistors, more resistance") with repairing feedback.
- L3-05 search is complete (series: only 100 + 390; parallel: smaller resistor must exceed 470 Ω) and E12 values are real.
- L3-04 identifies the faulty resistor from the ammeter table (R_3 at 0,0 mA) and verifies with 180 Ω.
- Every new solution has principle, units, substitution and a sensible-result step.
- Finnish and case after number+unit correct (9,0 V:n, 110 Ω:n).
- L3-04 capture at 1280 px readable, nothing clipped; no 360 px exercise captures listed.
