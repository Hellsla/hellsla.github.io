VERDICT: PASS
CONTENT-HASH: 431cbd39d2ee23a0

## Blocking
None.

## Polish
- tasks.json fy6-s1 d, `uncertainty` detail: "Ääriviivojen kulmakertoimet poikkeavat toisistaan 0,08 Ω" does not match the ± that follows. Each extreme line differs from the fitted line by 0,08 Ω, so the two lines differ from each other by 0,16 Ω. Write "poikkeavat sovitetusta suorasta". The result ±0,08 Ω is right.
- answers.py does not compute the drift rate 0,005 V/min or the carriers' drift speed of about 0,07 mm/s. Both values are right. This is shared with fi.

## Checked
- Round-1 item fixed: s1 d uses *ajautumisnopeus* for the charge carriers, kept apart from *ryömintä*. "Noin 0,07 mm/s" is right: I recomputed 0,074 mm/s for copper, 0,5 A and 0,5 mm².
- s4 a now gives three figures (14,9 J), which fits 300 V and 330 µF. s4 c gives two, limited by 1,0 ms.
- One script recomputed every number with my own formulas. All agree with tasks.json, the solutions and answers.py:
  - s1: fit −1,194 V/A and 4,598 V, largest residual 0,020 V; 0,50 A, 2,0 W, 0,30 W, 13,0 %, 4,0 V; ±0,08 Ω and 0,06 Ω.
  - s2: 2,5 A, 10,0 V, 16,7 + 8,3 + 5,0 = 30 W; without B: 1,76 A, 10,6 V, 18,7 W, 2,49 W; with C: 2,0 Ω, 4,29 A, 8,57 V, 14,7 W.
  - s3: 1,8·10⁻⁷ N, weight 2,2 %, 0,10 of breakdown strength, 13,4 m/s by both methods, kinetic energy 13,9 % of the work, 3,24·10⁻⁹ N (0,82 times the weight).
  - s4: 14,85 J, 7,99 J, 6,86 J, 46,2 % against a 27 % voltage drop, 26,4 A, 6,9 kW, 0,30 A.
- Every Kaava step starts from a basic law and is solved in symbols before substituting.
- The model conditions are stated: constant lamp resistances, a uniform field, no weight or drag in s3 b, point charges, an idealised body current, a simplified fuse time.
- The energy guardrail holds.
- The scope is FY6: no exponential discharge and no capacitor connections.
- Each part's rubric points add up to its points. Each criterion asks only what the task gives. The accepted alternatives match the tolerances. The invented data is labelled.
