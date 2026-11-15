VERDICT: PASS
CONTENT-HASH: 8da6f300bc0c21fc
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 b, Järkevyys: the measured 21,2 and 21,6 kWh/100 km belong to other cars than the 75 kWh model car; the text says so, but "Se sopii silti oletuksen rajoitukseen" is weak evidence and could be dropped.

## Checked
- Item 18 hunks: inquiry.json (sledge options and feedback, 6,278 kW and 54 kJ feedback, charger solution), unit.md (energy sum, P1..P3 alignment, "Häviöt katoavat"), figure aria text, solutions s1 (fridge 1,08/1,54 = 70 %, corrected from "two thirds"), s3 d, s6 c and d, tasks.json s3 rubric. Each carries P1 correctly: internal energy, transferred to the surroundings as heat; the correct option is still the only correct one.
- s7 recomputed with own formulas: −28,89 %, −42,93 %, −45,83 %, mean 39,2 %; wrong-denominator 40,6 %; E100 = 16,67 kWh, s_k = 279 km, E100k = 26,88 kWh, factor 1,61, wrong 23,0 kWh; E/s = 600 N; ΔT 27 K and 52 K; 3,0 kW · 5,0 h = 15 kWh = 1/5 of 75 kWh; density ratio 293,15/253,15 = 1,158 (16 %). All agree with tasks.json answers, the solution and answers.py.
- s7 physics: relative difference against the stated range, energy proportional to distance, the equal-energy assumption judged in the right direction, heat flow, P = UI, R_s I^2, W = Fs, confounding of temperature with distance in d, single run in e. Points 3+4+4+2+2 = 15, criteria sums match.
- `python scripts/practice.py check units/fy9-energia`: OK (7 tasks, 105 points). Hash equal at start and end.
