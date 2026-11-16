VERDICT: PASS
CONTENT-HASH: 67de3653400246d8

## Blocking

## Polish
- exercises.json:76 (fy7-5-L1-07) — The exact answer is 2,25 V, but the stored answer is 2,3 with tolerance 0.03. A student who rounds 2,25 to 2,2 (also a defensible two-figure answer) is 4,3 % off and is marked wrong, although the physics is right. — Store `"answer": 2.25`, or change the data so the result does not fall exactly on a half (e.g. 0,90 V → 0,88 V).

## Checked
- Recomputed every answer in one script with my own formulas, side by side with answers.py and exercises.json. All agree: L1-01 5,04→5,0 mWb; L1-02 3,0 V; L1-03 0,20 V; L1-04 0,36 mWb; L1-05 0,50 m/s; L1-08 0,060 T; L2-01 48 mV; L2-03 0,30 A; L2-04 75 mV; L3-01 4,23 mV; L3-02 50 µT (ΔΦ = 2BA on a half turn); L3-03 0,060 mWb.
- Figures by their figures.py data: flux-task has its steepest fall of 4,0 mWb over 0,10 s, giving 2,0 V. flux-task-2 goes from 5,0 to −3,0 mWb over 0,40 s, giving 4,0 V (the change through zero is handled correctly).
- Data tasks: L2-05 has its steepest interval at 0,40–0,50 s, giving 1,452 V. L2-06 through-origin slope gives B = 0,1498 T (a free fit gives 0,149). L3-04 gives a = 1,643 m/s² (a free fit 1,656, within 4 %) and s = 1,18 m. L3-05 by the trapezoid rule gives 0,0778 mWb and 0,0787 mWb, of opposite sign.
- L1-09 values are C 0, D 0,60, A 1,2, E 2,0 and B 3,0 V, so the order is C, D, A, E, B. The solution's wrong-path values (6,0 mV, 60 mV) are right.
- L1-06 and L2-07 each have exactly one correct option, and every distractor's feedback is physically right. L2-07: with v parallel to B the magnetic force is zero.
- L3-05 b reasoning: opposite signs because the flux grows and then shrinks, equal areas because |ΔΦ| is equal, and the narrower, higher second pulse because the magnet accelerates. All correct.
- L3-01: only the vertical field component gives an axle-directional force, and the solution says why.
- Every solution is symbolic first, its conversions are right, and its significant figures are justified by the limiting datum.
- Scope stays within Φ = BA, the induction law and e = vBl, with Ohm's law from FY6.
