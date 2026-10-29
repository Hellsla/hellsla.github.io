VERDICT: FAIL
CONTENT-HASH: 945681e19d0a7f71

## Blocking
- exercises.json:98 (fy4-2-L3-03) and solutions.md:120: **A** (rounding and grading). The task gives the instant as $t = 0{,}50\,\text{s}$, which has two significant figures, so the limiting datum supports $-1{,}8\,\text{m/s}$. The solution instead keeps three figures "kuten polynomin kertoimissa". A student who correctly rounds to the data gives −1,8. That is 2,3 % from the stored −1,76, outside the 2 % tolerance, so the page marks a correct answer wrong. This breaks the CLAUDE.md rule that a student rounding to the data stays inside the tolerance. Fix (either one): write the instant as $t = 0{,}500\,\text{s}$ in the task and the solution, which keeps −1,76 and its three-figure justification; or give the answer as $-1{,}8\,\text{m/s}$ with a two-figure justification and set the tolerance to 0,03.

## Polish
- solutions.md L3-02: "kilometreina" should read "kilometreinä".
- solutions.md L2-01: the braking deceleration of 5 m/s² is called "tavallinen voimakas jarrutus kuivalla tiellä". On dry asphalt a full emergency stop reaches about 7–9 m/s², so "reipas jarrutus" would describe 5 m/s² more accurately.

## Checked
- I recomputed all 12 answers with my own formulas, and each matches exercises.json and answers.py: 3,125; 1,5; 11,04; 1,0; 180; 40; 4,0; 11,47 (v0²/2g); 1,610; 2,190; 1162,5; −1,76.
- Rounded answers against the 2 % tolerance: 3,1 (0,8 %), 11,0, 11,5, 1,61, 2,19, 1160 and 180 are all inside. L3-03 at two figures is outside (see Blocking).
- Figures (figures.py): ex-tv runs from (0; 2,0) to (5,0 s; 7,0 m/s). The ex-tangent tangent to x = ½t² at t = 4 s passes through (2 s; 0) and (6 s; 16 m), slope 4,0 m/s.
- L3-01: the negative root −0,56 s is rejected with a reason. The check by rise plus fall (0,82 s + 1,37 s, apex 3,26 m) gives 2,19 s.
- L3-02 and L1-05 state that the motion keeps one direction before treating the area or displacement as distance. L2-03 uses v = 0 at the apex with a = −g throughout.
- L3-03: v = B + 2At is read correctly from the fit, the sign is interpreted, the apex is at 0,32 s and a = −9,72 m/s² is close to −g.
- Every solution is symbolic first, states its conversions (72 km/h = 20 m/s) and has a real reasonableness check (average velocity, Moon g of 1,62 m/s², fall time on Earth 0,57 s).
- The tasks state their conditions: small air resistance, no atmosphere on the Moon, uniform acceleration or braking.
