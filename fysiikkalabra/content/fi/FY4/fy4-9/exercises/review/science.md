VERDICT: PASS
CONTENT-HASH: cd77831d711f3f85

## Blocking

## Polish
- exercises/exercises.json:99 (L3-03) — "Kumpikin pallo on kosketuksissa seinään ajan 0,020 s": the clay ball sticks, so its contact never ends; the intended quantity is the stopping/collision time — fix: "Kummankin pallon törmäys kestää 0,020 s" (or "savipallo pysähtyy 0,020 s:ssa").
- exercises/solutions.md:59 (L2-01) — a deceleration of ≈0,51 g is firm braking rather than "tavallista jarrutusta" — fix: "vastaa reipasta jarrutusta kuivalla tiellä".

## Checked
- All 12 answers recomputed in one script with my own formulas; all equal exercises.json and answers.py (5,1; 6,0; 4,86; 6,0; 150; 6,0 kN; 6,44 kN; 1,5; 25,65; 3,0; 57,6 km/h; 60 N).
- Signs: L2-03 positive toward the wall, v = −11 m/s, |I| = 1,5 N·s pointing away from the wall; L2-04 force along motion.
- L3-01 figure ex-potku (figures.py): trapezoid 0→60 N at 0,20 s, 60 N to 0,80 s, 0 at 1,00 s → 48 N·s, matches solution.
- Conditions stated in tasks: weight neglected (L1-03, L2-02 with F/G ≈ 14 000 justified), friction/air resistance neglected (L2-01, L2-04, L3-01), only belt force horizontally (L3-02).
- Units and conversions (54 km/h = 15 m/s, 46 g, 0,50 ms, ×3,6) correct; rounding to two significant figures justified by the data.
- Reasonableness checks are real checks (L3-02 10 kN ≈ 14 × weight; L2-03 sign-error value 0,18 N·s shown too small).
- Solutions solve symbolically before substitution; impulse principle applied to the net force each time.
- L3-03 uses Newton's third law correctly to turn the wall's force on the ball into the ball's force on the wall.
- Typo fix only since review: exercises.json L3-01 "Lasta istuu pulkassa" → "Lapsi istuu pulkassa"; no other change (verified by git diff).
