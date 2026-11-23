VERDICT: PASS
CONTENT-HASH: 250518ce070eda9b

## Blocking
- none

## Polish
- L3-04 c): "16 A:n sulake riittää" treats the fuse as cutting at its rated current; a real fuse carries somewhat more than I_s for a long time. Within the task's model this is a level-appropriate simplification (C), not a finding.

## Checked
- Full review of the fi-easy set: exercises.json (21 tasks), solutions.md, lessons/FY6/fy6-15/answers.py.
- Recomputed every answer with my own formulas (I = P/U at 230 V, P_max = UI_s, P = RI², I = U/R with series resistances added, U_max = E_max d): L1-01 6.52 A; L1-02 2300 W; L1-03 100 mA; L1-04 4.6 mA; L1-05 51.2 W; L1-08 6.0 kV; L1-09 1.2 / 5.0 / 143.75 / 40 mA, order A, B, D, C; L2-01 480 W; L2-02 22.7 W; L2-03 3.0 cm; L2-04 15 V; L2-05 61.1 (currents 4.18, 19.2, 95.8, 255.6 mA); L2-06 pairs over 2300 W listed correctly, best pair 2200 W, 9.57 A; L2-07 115 mA; L2-08 17.39 A; L2-09 3.48 A, 19.5 A in a cable part, heating 1.48 times; L3-01 4.84; L3-02 2.27 mA; L3-03 50 mA (and 100 V between 4 m and 6 m); L3-04 ΣPΔT = 4311.7, ΣP² = 14 499.8, k = 0.2974 K/W, 20.5 A, 30 K at 16 A, 74 K at 25 A; L3-05 6.167 kΩ, week currents 0.26 / 1.9 / 5.5 / 17.0 / 41.8 mA. All agree with exercises.json and answers.py; rounded answers stay inside the tolerances.
- Figures fy6-15/ex-askel (V = 1200 V·m / r, 600 V and 400 V on gridlines) and ex-kuorma (steps 1000…4000 W, highest on a gridline) match the solutions.
- Physics: protective earthing gives the fault current a low-resistance path so the protective device trips (L1-06); class II double insulation, class I and III distractors and their feedback correct (L1-07); the fuse protects the cable, the RCD the person (L2-07); parallel loads add currents; uniform field stated wherever E = U/d is used; the computed air gap is called a lower bound; current thresholds labelled indicative; energy becomes internal energy, transferred as heat.
- Notation (I_s, E_max, R_keho, P = RI²) matches the lesson; chapter references name earlier FY6 chapters.
- Every multiple-choice task has exactly one correct option.
- Content hash checked at the start and at the end.
