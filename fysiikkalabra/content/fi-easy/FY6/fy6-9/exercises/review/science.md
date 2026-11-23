VERDICT: PASS
CONTENT-HASH: 754be9e49009ab18

## Blocking
- none

## Polish
- none

## Checked
- Full review of the fi-easy set: exercises.json (20 tasks), solutions.md, lessons/FY6/fy6-9/answers.py.
- Recomputed every answer with my own formulas (Q = It, W = UQ, loop law U_lat − RI − R_sI − E = 0, W = R_sI²t): L1-01 2.0 Ah; L1-02 10 800 C; L1-03 468 Wh; L1-04 16 h; L1-05 4.0 Ah; L1-08 5.2 h; L2-01 5.0 A; L2-02 0.20 Ω; L2-03 97.5 min; L2-04 84 %; L2-05 9.32 Wh (trapezoids); L2-06 1.5 Wh; L2-07 0.40 Ω (least squares 2.5 A/V; fitted line gives 1.52 A and 5.52 A at the read points); L2-08 61.05 Wh; L2-09 4.2 h, 504 Wh = 1.81 MJ; L3-01 1.28; L3-02 33.3 %; L3-03 3.24 kJ; L3-04 77.45 %, R_s = 0.10 Ω, E = 3.75 V at both currents; L3-05 7.12 h (lower bound 6.0 h, upper 8.6 h). All agree with exercises.json and answers.py; rounded final answers stay inside the tolerances.
- Figures fy6-9/ex-current and ex-current2 (figures.py): the plotted steps are the values read in the solutions.
- Notation: the loop law is written ΣΔV = 0 and then U_lat − RI − R_sI − E = 0, the same equation, symbols (U_lat, R, R_s, E) and loop direction as the lesson's charging-circuit section; ΣΔV = 0 is the form of the Kirchhoff chapter.
- Physics: current inside the battery runs + to − while charging and − to + while discharging (L1-07 correct option and feedback); chemical energy share EIt vs. losses (U_lat − E)It (L2-06); unit reasoning V·Ah = Wh (L1-09, every distractor wrong and its feedback right); internal energy then heat wording follows the guardrail; nominal voltage and the L2-09 c) reasons (R_sI² losses, falling current as E rises, CV phase) are correct; L2-09 d) presents no invented source claims.
- Every multiple-choice task has exactly one correct option.
- Content hash checked at the start and at the end.
