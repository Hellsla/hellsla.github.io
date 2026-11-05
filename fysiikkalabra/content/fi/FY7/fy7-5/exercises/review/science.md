VERDICT: PASS
CONTENT-HASH: a48533fe7157ea8e
ROUND: 2

## Blocking

## Polish
- exercises.json:125 (L2-05): still open from round 1. `graph` was dropped, but the plan's "piirrä e(t) annetusta Φ(t):stä toisella N:llä" task is still missing from the set. Fix: add the e(t) drawing as part b), or update docs/exercise-bank/FY7.md.
- exercises.json:323 (L3-05): still open from round 1. Its core (Φ = pulse area ÷ N) repeats L3-03, and the plan's flip-coil task (B and inclination) was not written. Pedagogy and the plan should decide.
- lessons/FY7/fy7-5/answers.py: L1-07 still computes 2,25 while exercises.json gives 2,3 (it is inside the 0,03 tolerance, so this is not a defect). Fix: `round(..., 1)` or a comment saying the exercise rounds to 2,3.

## Checked
- Round-1 Blocking item L1-07 is resolved. The answer is 2,3 V with tolerance 0,03, the solution gives the two-figure reason from 0,90 V, and 2,25 V is still accepted.
- L2-05: the solution now lists every ΔΦ (0,98; 1,05; 0,97; 0,01; 1,21; 1,20 mWb). The steepest interval is 0,40–0,50 s, giving 1,452 V, and it notes that the whole-phase mean gives the same value. answers.py was changed to match.
- L3-04: k = 0,164 V/s from the least-squares fit through the origin, which I recomputed as 0,16434. a = 1,64 m/s² and s = 1,18 m.
- L3-05: |A_a| = NΦ, so the sign problem is gone. The trapezoid values recomputed to 0,0778 and −0,0787 mWb. The added "pinta-ala" wording in a) is right.
- L1-06 and L2-07: the options were reordered and shortened. Exactly one option is correct, and every feedback is still right. "kohtisuorassa kenttää vastaan mutta liikkuu kentän suuntaisesti" is unambiguous.
- I recomputed all eight new answers in one script, and they agree with exercises.json and answers.py: L1-07 2,25→2,3 V; L1-08 0,060 T; L2-05 1,45 V; L2-06 0,150 T; L3-04 1,64 m/s²; L3-05 0,078 mWb.
- The other diffs only add paragraph breaks or change "-" to "−" in table cells, with no change to the physics. Hash unchanged at start and end.
