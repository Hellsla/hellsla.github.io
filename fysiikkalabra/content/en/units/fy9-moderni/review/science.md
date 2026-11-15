VERDICT: PASS
CONTENT-HASH: b83853149096e7fe
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- C: s7 c answer gives two significant figures "because the initial temperature of the water is an estimate"; the task states 20 C, so the simpler reason is the two-figure temperature difference 80 K.

## Checked
- Item 18: s6 "Yleisiä virheitä" now says electrical power instead of thermal power; it matches s6 b, where the mass change is calculated from P_th * t.
- s7 recomputed with my own formulas: b 1.537 and 1.10 MJ (54 % of 2.05 MJ), inverse 0.651; c 335 200 J/kg, 9.397 kg; d 3.15 : 300 = 1.05 %, 2.05 : 300 = 0.68 %, 1.05 MJ of electricity = 0.35 % of 300 MJ; e mass change 3.50e-11 kg = 35 ng. All agree with tasks.json, the solution and answers.py (practice.py check OK).
- Physics: Q = cm dT without vaporisation is stated as the model; the system boundary (fuel against whole facility) is the right principle for d; e explains the surplus with the decrease in mass and binding, energy conserved. The 300 MJ figure is marked in the task and the source note as not from the article. Everything is solvable with the given data and FY2, FY3 and FY8 content.
- Rubric points add up (2, 3, 4, 3, 3). Hash the same at the start and the end.
