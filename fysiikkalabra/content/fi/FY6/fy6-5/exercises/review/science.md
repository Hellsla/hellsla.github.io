VERDICT: PASS
CONTENT-HASH: 098f88de6ba5c331

## Blocking

## Polish
- solutions.md (fy6-5-L2-02, Vastaus): "resistanssit on annettu kahden numeron tarkkuudella" — 200 Ω and 400 Ω do not show their significant figures. Fix: give the two figures as the course convention for such data, or cite 12,0 V and state the answer to the precision of the data.

## Checked
- The round-1 blocker is fixed: L3-03 now places the 20 Ω resistor between the plus pole and the lamps, asks for the junction between them and states ideal source and wires; +1,8 V is then the only reading.
- The round-1 polish is fixed: L1-04 Järkevyys is now a real magnitude check; L2-03 and L3-03 state the ideal source (L1-02, L2-02, L3-01 depend only on the terminal voltage, so C).
- All 12 answers recomputed in one script with my own formulas (L3-02 via R_tot = 12 V : 0,20 A = 60 Ω, so R23 = 20 Ω, R3 = 30 Ω; L3-03 via the voltage divider 9,0 V − 7,2 V): 1,2 A; 7,5 V; 8,0 V; 6,0 V; 4,0 V; 3,5 V; 8,0 V; 0,50 A; 60 Ω; −9,0 V; 30 Ω; 1,8 V. All agree with exercises.json and answers.py within tolerance.
- ex-graph: 0 → 9 → 7 → 3 → 0 V on 1 V gridlines, R2 between B and C, drops 2 + 4 + 3 = 9 V; the description carries the same values. ex-branch (6,0 V, 20 Ω ∥ 30 Ω, ammeter in the main wire) and ex-branch2 (12 V, 0,20 A, 40 Ω, 60 Ω ∥ ?) give every needed value and no answer.
- Every solution states the principle, solves symbolically first, converts mA → A correctly, gets the signs right (L1-03, L3-01, L3-03) and back-substitutes in Järkevyys.
- L3-03's "remaining lamp brighter" follows from constant resistance, which the task states.
- Notation (V_A, U_AB, ΔV, R I) matches the lesson's Kaava; scope stays within one junction and FY6 contents.
