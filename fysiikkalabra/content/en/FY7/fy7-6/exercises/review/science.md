VERDICT: PASS
CONTENT-HASH: bcba5280a01c2a67
SCOPE: full (round 2)

## Blocking

## Polish
- solutions.md:731 (fy7-6-L3-05 Principle) — round-1 item not changed (the fi source, solutions.md:181, says the same): "When the resistance stays the same, the power grows as the square of the voltage". This is not true for a sheet, because a thinner sheet also narrows the current paths and raises their resistance. The conclusion is right — fix: "the induced voltage is smaller and the narrow current paths have more resistance, so the currents and the loss fall sharply".
- exercises.json:503 (fy7-6-L3-06) — round-1 item not changed (fi has "Samaan alumiiniputkeen" too): "the same aluminium tube" points back to L2-09 — fix: "an aluminium tube" or "the tube of the graph".
- solutions.md:779 (fy7-6-L3-06) — the claim that "a lighter 20 g magnet would fall more slowly" with the same k holds only for a magnet of the same strength and size — add "equally strong".

## Checked
- L1-06 fixed: the answer and the correct option now say "tries to keep the flux unchanged". The feedback and solutions.md:565–566 agree, there is exactly one correct option, and every distractor's feedback is right.
- All 16 numeric answers recomputed in one script with my own formulas. Each matches answers.py and exercises.json within tolerance: L1-01 0.392 N, L1-03 100.8 kJ, L1-04 73.6 mW, L1-08 6.0 V, L2-01 29.4 mW, L2-02 0.20 A, L2-03 0.151 m/s, L2-04 4.17 MW, L2-05 26.8 mW, L2-07 0.349 mWb, L2-09 100 mW, L3-01 0.0727 K, L3-03 0.60 N, L3-04 2.65 m/s², L3-05 0.147 W, L3-06 0.276 m/s.
- The brake-task figure is unchanged in its numbers: the line is F = 1.6 N·s/m · v and the point at 0.25 m/s is 0.402 N. It gives the 0.40 N and the slope 1.6 N·s/m the solutions read from it, and it does not give the answer away.
- L2-05: thin-tube mean 4.0 s; F : v is 1.44 and 0.78 N·s/m; the 3.3 s difference is far larger than the scatter.
- L3-04: the central difference 2.8 m/s² is a bit larger than the tangent value, which is right for a concave curve. L3-05: ratios 1.17–1.24, and (1.0/0.35)² = 8.2.
- The Lenz directions in L1-02, L2-02, L2-06 and L2-08 (both stages) and the energy-conservation arguments are right.
- Conditions are stated: Q = cmΔT with no heat loss and no change of state, the penetration-depth condition in L3-05, and other resistances ignored in L1-03 and L3-03.
- Energy is "converted into internal energy" throughout. Units, significant-figure reasons and scope (FY7 induction, F = IlB) are right.
- Hash identical at start and end.
