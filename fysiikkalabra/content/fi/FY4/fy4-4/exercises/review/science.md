VERDICT: PASS
CONTENT-HASH: 751013725298ea15

## Blocking

## Polish
- exercises.json L2-07 (new task): the physics is the same as L2-03 (a crane lowers a load that slows down, and T = m(g + a)). The error-analysis framing makes it a different exercise, but whether the set needs both is for pedagogy to judge.
- exercises.json L3-05: the plan asks for a "(t, a)-hissikuvaaja", but the task gives a table plus text. A (t, a) graph would match the plan.

## Checked
- Round 2: the round-1 items are fixed. L2-07 was replaced, L2-06 now answers a) and b) in its Vastaus, and L1-08 now asks for the snowmobile's mass only.
- I recomputed all 20 answers in one script. All match answers.py (run with `python3 -I`) and the solutions.
- L1-07: 170 g = 0,17 kg, so 68 N. L1-08: 0,60 kN = 600 N, so 400 kg. Both now have a real conversion step.
- L2-06 (row 2,35 changed to 2,4): a fit through the origin gives F = 1,208 N (answer 1,2, tol 0,04). The products ma lie between 1,17 and 1,24 N.
- L2-07 (new): the slab moves down and slows, so a points up. T = 820·(9,81 + 1,20) = 9028 N. The student's 7,06 kN = 820·8,61 is right for the wrong sign. The rendered diagram (T > G, a up, v down drawn separately) is right. Three significant figures fit 1,20 m/s².
- L2-05, L3-04, L3-05 have not changed: m = 0,498 kg, F_μ = 1,19 N from the fit, N = 634 N.
- L1-06 (MC): one correct option, and every distractor's feedback is right.
- Scope: FY4.4 only; kinematics from fy4-2 appears at level 3 only.
- The hash was the same at the start and at the end.
