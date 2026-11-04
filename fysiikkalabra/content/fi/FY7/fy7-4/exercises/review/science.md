VERDICT: PASS
CONTENT-HASH: a3578858afaf37ff

## Blocking

## Polish
- fy7-4-L2-02 (solutions.md, answers.py): the drawn line goes through (5,0 A; 1,50 g), which gives B = 0,0736 → 0,074 T. An exact least-squares fit through the origin of the five plotted points gives a slope of 0,2995 g/A, so B = 0,0734 → 0,073 T. The two values straddle the rounding boundary. The tolerance (3 %) accepts both, so nothing needs to change. If you want a cleaner case, nudge one point so that the least-squares slope rounds to 0,300 g/A.

## Checked
- Round-1 blocking items are fixed. The Earth's field is now 53 µT at 74° (WMM2025), and L3-03 has been recomputed to 1,813 kA → 1,8 kA in exercises.json, solutions.md and answers.py. "Kompassin mukaan itä–länsi" and "magneettiseen pohjoiseen" now make the wire perpendicular to the horizontal component.
- I recomputed all twelve answers in one script with my own formulas: 0,24 N; 0,193 → 0,19 N; 0,10 T; 1,019 → 1,0 N; 3,0 A; 3,2 mN; 0,0736 → 0,074 T; 30°; 18 m/s²; 2,354 → 2,4 A; −266,7 → −270 N; 1,813 → 1,8 kA. They agree with exercises.json and answers.py.
- L3-02: the new sign rule (attract +, repel −) and the answer −270 N are consistent in the task, the solution and answers.py.
- L1-04 geometry: a wire along the magnetic meridian lies in B's vertical plane, so the angle between them equals the inclination, 74°. The Järkevyys estimate (about 1 kg/m, about 1000 N) is now realistic.
- Directions: in L3-03 an eastward current × the northward H gives a force up, and the vertical component gives a horizontal force. In L3-01 the current direction is chosen so the force points up, and reversing it gives a tension of 2mg. In L2-01 parallel currents attract.
- Figure balance-points: it gives every value the task needs, its description carries the same data, and it shows no B or slope.
- Reasonableness checks: the equivalent masses (25 g, 100 g, 0,3 g, 36 g, 27 kg) and the comparisons are correct.
- Conversions, the symbolic solution before substitution, and rounding to the limiting datum are right in all twelve solutions.
- Scope and notation match the lesson brief (F = I l B sin α, B₁ = μ0 I₁ : (2πr), μ0 in Vs/(Am)). Every two-wire task meets l ≫ r.
