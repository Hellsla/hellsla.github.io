VERDICT: FAIL
CONTENT-HASH: 87bf9eac2d0b59a7

## Blocking
- exercises.json:337–339 (fy7-1-L1-09, statement 4 and its feedback): B, assessment correctness. The statement is keyed true, but it says "kohti Maan magneettista etelänapaa" with no model named. The brief's lesson (Yleinen virhekäsitys, Tiivistelmä) and L1-07 say that in geomagnetism the pole near geographic north is called the *magneettinen pohjoisnapa*, and that it is a south pole only in the bar-magnet model. A student who uses the geomagnetic name can fairly mark the statement false, so its truth depends on a naming condition the item does not state. Fix: write "kohti Maan sauvamagneettimallin etelänapaa" in both the statement and its feedback, the same wording as L1-07 (solutions.md:799 already adds the geomagnetic name).

## Polish
- solutions.md L3-02: "kovassa teräksessä": a paper clip is soft rather than hard steel. "teräksessä järjestys säilyy osittain" would be more accurate, and the task's observation still holds.
- solutions.md L2-04 Järkevyys: "kuten magneetin kenttä luvun simulaatiossakin" refers to the lesson's simulation. The check would stand without it: compare with the on-axis 1/r³ value 2³ = 8.

## Checked
- I recomputed all 17 numeric answers in one script with my own formulas (tan θ = B_m : B_h, B_h = B cos I, B_v = B sin I, the Pythagorean sum of 2 or 3 components, the r₀ from the mean of B_m r³). All of them agree with exercises.json and answers.py to the stated precision.
- Every tolerance accepts the solution's rounded answer: L1-02 14 (2,1 % off, tol 3 %), L2-05 15 (3,4 %, tol 4 %), L3-03 2,0 (1,7 %), L3-05 16 (1,2 %, tol 5 %).
- L2-05 data: B_m r³ = 23 400…26 900 µT·cm³ across the table, so the falloff is consistent with 1/r³. The claim that the field is not ∝ 1/r and the ratio 7,3 ≈ 8 are right.
- L3-05: products 53,1…63,0 ·10³ µT·cm³, mean 59,1 ·10³, r₀ = 16,2 cm. The field directions are right: on the axis outside the S end the field points east, and in front of the N pole facing the compass it points south. The answer to part c is correct.
- L3-01, L1-09 statement 2: in the equatorial position the field is antiparallel to the moment (south). The result −11 µT means the needle reverses, which is right.
- L1-05: on the axis in front of the N pole, the needle's N end points away from the magnet. Correct.
- L1-06 and L1-07: exactly one option is correct. Every distractor's feedback is right physics: copper conducts better than iron and is denser.
- Figures sum-grid and incl-grid: equal x and y scales (12 px/µT in sum-grid; 5 px per µT on both axes in incl-grid). The arrow tips are at (20; 15) and (15; 50), they match the solutions' grid reading, and neither figure gives the answer away.
- Earth-field data (Kuopio, Oulu, Rovaniemi, Utsjoki, Helsinki, Longyearbyen) is realistic for the WMM, and the magnitudes and signs are plausible.
- Angle notation `^\circ` is used the same way throughout the exercises and solutions, and so is `{}^\circ\text{C}`. The unit "°" is set on every angle answer. All of it is in scope (FY7 ferromagnetism, dipole, field) and uses the lesson's notation.
