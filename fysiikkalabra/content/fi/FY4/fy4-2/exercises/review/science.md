VERDICT: PASS
CONTENT-HASH: 8b72ddfd68744298

## Blocking

## Polish
- solutions.md:110 (L3-02): "kilometreina" should be "kilometreinä" (carried from round 2).
- solutions.md:60 (L2-01): 5 m/s² is called "tavallinen voimakas jarrutus kuivalla tiellä". A full stop on dry asphalt reaches about 7–9 m/s², so "reipas jarrutus" fits better (carried).
- answers.py:266 (L3-03): the code uses `0.50` while the task now gives 0,500 s. The value is the same; writing `0.500` would match the data.

## Checked
- Round-2 blocker resolved: L3-03 now gives $t = 0{,}500\,\text{s}$ in both the task and the solution, so −1,76 m/s with three significant figures is justified by the data, and the stored answer equals it.
- I recomputed all 12 answers with my own formulas in one script: 3,125; 1,5; 11,04; 1,0; 180; 40; 4,0; 11,47 ($v_0^2/2g$); 1,610; 2,190 (other root −0,56 s); 1162,5; −1,76. All match exercises.json and answers.py.
- Answers rounded to the data's significant figures all lie within the 2 % tolerance. The largest gap is 3,1 against 3,125, which is 0,8 %.
- L2-02: the tangent to x = ½·1,0·t² at t = 4 s passes through (2 s; 0) and (6 s; 16 m), slope 4,0 m/s. L1-04: (0; 2,0) to (5,0; 7,0) gives 1,0 m/s².
- L3-03: v = B + 2At is read correctly from the fit. The apex is at 0,32 s, so the ball is falling at 0,500 s and the negative sign is correct. a = −9,72 m/s² is close to −g.
- L3-01: the whole flight is treated as one motion with a = −g. The rise-plus-fall check (0,82 s + 1,37 s) is a real check.
- L1-05, L2-01 and L3-02 state that the motion does not reverse before they equate distance with displacement or area.
- Every solution is symbolic first, has the conversions it needs (72 km/h = 20 m/s) and ends with a meaningful reasonableness check.
- Conditions are stated: small air resistance, no atmosphere on the Moon, uniform acceleration or braking.
