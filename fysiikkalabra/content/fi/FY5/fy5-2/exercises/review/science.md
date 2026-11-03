VERDICT: PASS
CONTENT-HASH: 7dd521aba303ad6a

## Blocking

## Polish
- exercises.json:22 (fy5-2-L1-03) — the CoM is given "vaakasuunnassa" from the axle but the handles only "1,20 m:n päässä"; the solution uses 1.20 m as the moment arm of a vertical force, which needs the horizontal distance — write "vaakasuunnassa 1,20 m:n päässä" for the handles too.

## Checked
- Every answer recomputed independently (different moment points where possible): L1 1.2 m, 0.75 N, 207 N, 58.9 N, 0.60 m; L2 98.1 N, 556→560 N, 12.5°, 449→450 N; L3 3.33 m, 196 N, 1.21 m — all within 0.8 % of exercises.json and identical to answers.py.
- answers.py uses the right physics for each task (ΣM = 0 about a well-chosen point, ΣF = 0, CoM of uniform bodies at the middle).
- L2-03 tipping angle tan α = d/h correct for a uniform shelf on its front edge.
- L3-02 cable: only T sin α gives a moment about the hinge; hinge carries the remaining 19.6 N vertically, as the check says.
- L3-03: rear carrier 582.9 N, moments about the CoM balance (750 Nm each).
- Solutions: symbolic first, units, significant figures justified by the data, reasonableness checks are real checks.
- Scope within FY5 "tasapaino kiertymisen suhteen"; component use only in L3-02 as the slot's täsmennys allows.
