VERDICT: PASS
CONTENT-HASH: c73001120d4d9bbb

## Blocking

## Polish
- content/fi/FY6/fy6-4/exercises/exercises.json:30 — L1-04 uses "toisen lampun" both for the measured lamp and for the lamp asked about, so a student can read the task as asking for 1.8 V. Better: "Jännitemittari näyttää toisen lampun yli 1,8 V. Kuinka suuri jännite on toisen, mittaamattoman lampun yli?" (solutions.md already calls the measured one "ensimmäinen").
- content/fi/FY6/fy6-4/exercises/solutions.md:119 — L3-03 gives 150 Ω to "kaksi merkitsevää numeroa", but the result is very sensitive to the data: the discriminant 62 500 − 60 000 is a small difference, so 60 ± 0.5 Ω already moves the result by about 5 Ω. One clause saying the data are taken as exact would make the rounding reason honest.

## Checked
- I recomputed all 12 answers in one script with my own formulas and compared them with answers.py: 670, 24, 1.50, 2.7, 110, 4.787→4.8, 35, 20, 1.32→1.3, 50, 4, 150. All agree, and each stored answer lies within its tolerance of the exact value (largest gap 1.5 %, for L2-04 against tolerance 0.03).
- answers.py: each line uses the right law: series sum, parallel reciprocal, Kirchhoff current sum, voltage split, and Ohm's law in each part.
- L3-01: the task-mixed figure gives 12 V, 40 Ω, 60 Ω and 120 Ω, and its topology (R2 || R3 between two nodes, in series with R1) matches the solution. The description carries the same values and does not give the answer away.
- L3-02: the heater is realistic (575 W and 2.3 kW). The ratio of 4 is derived symbolically, and the task states that the resistance does not change.
- L2-02: realistic indicator lamp, and the check through the lamp's 25 Ω closes. L2-03: the branch-current method is checked through the total resistance of 12 Ω.
- Every solution solves symbolically before substituting, converts k → Ω and A → mA correctly, and names the datum that limits the rounding.
- Notation agrees with the lesson brief: R, R1, R23, I = I1 + I2, the colon for division in prose.
- Scope: everything is within "vastusten kytkennät"; L3-03's quadratic equation is mathematics a level-3 task may use.
- The solutions make no claim that contradicts the brief, such as current being used up (L1-04 Periaate gives the energy picture).
