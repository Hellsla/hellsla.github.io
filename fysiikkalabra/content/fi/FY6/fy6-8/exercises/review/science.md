VERDICT: PASS
CONTENT-HASH: 1f8f2c834b1f80dc

## Blocking

## Polish
- exercises/solutions.md:119 (L3-03) — the rounding reason names the measured voltages, but the resistances 2,0 Ω and 6,0 Ω (2 s.f.) limit I₁ and I₂ and so the term R_s I₁ = 0,40 V. 1,60 V is defensible because the 0,40 V term is good to about 0,01 V; say that, or give 1,6 V.
- exercises/solutions.md:49 (L1-05) — "kahden merkitsevän numeron tarkkuudella, koska arvo luetaan 0,5 A:n ruudukolta": the reading uncertainty is about 0,1 A (part of a grid step), and that is what sets 3,0 A. Name it that way.

## Checked
- All 12 answers recomputed in one script with my own formulas (L3-01 by node analysis of the two branches, not R_s/2; L1-04 by 1/R sum; L1-05 by the slope of the given points): all match answers.py and exercises.json within the relative tolerance 0,02.
- Rounded answers a student would give (33 A, 0,32 A, 10,4-type roundings) stay inside the relative tolerance.
- ex-graph figure: the line is U = 4,5 V − 1,5 Ω · I through the four points (0,40; 3,9) … (1,60; 2,1), dashed to (0; 4,5) and (3,0; 0), on the 0,5 A grid line. The description gives the points but not the intercept, so it does not give the answer away. The extrapolation condition is stated in the solution.
- Physics of each task: series E and R_s add, the reversed cell enters as −E₁ with its R_s still added (L3-02: 1,5 V : 4,75 Ω), parallel identical cells E and R_s/n, U = RI = E − R_s I.
- The data are realistic: NiMH 0,040 Ω, 4,5 V flat battery about 1 Ω, new AA 1,60 V.
- Every solution is complete: given, asked, principle, symbolic formula before substitution, conversions, answer with rounding reason, a real check. L2-03 has an energy balance 1,5 W + 3,0 W = 4,5 W, and L3-01 checks the equal terminal voltage in both branches.
- Notation is the same as the brief: E, R_s, R_s1, I_k, U. Energy wording: "muuttuu pariston sisäenergiaksi", never "lämmöksi".
- All tasks are inside FY6 and the brief's lesson. The tasks state their assumptions (lamp resistance constant, same E and R_s in both measurements, wire resistance neglected).
