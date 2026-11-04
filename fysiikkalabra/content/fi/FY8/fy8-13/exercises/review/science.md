VERDICT: PASS
CONTENT-HASH: b81e54ad228f16ca
Round: 2

## Blocking

## Polish
- exercises.json:163 (L2-06) — `answer` is 11.2, but solutions.md:164 now gives 11 µSv/h as the answer (2 sf). The 3 % tolerance accepts both. — Optionally store 11 so that the answer box and the solution say the same.
- exercises.json:145 (L2-05) — The table cell "Muu luonnon säteily (maaperä ja rakennusaineet, kosminen säteily, kehon omat radioaktiiviset aineet)" is long. Visual should check it at 360 px. The physics is right.
- L3-04 b) still repeats the proportional radon scaling of L2-03 and L3-02. Parts c) and d) carry the level-3 weight, which is acceptable.

## Checked
- Round 1 Blocking A (L2-05 STUK split): resolved. The rows are radon 4,0, other natural 1,1 and medical 0,8 mSv, sum 5,9. This matches STUK-A263 (0,45 + 0,33 + 0,36 ≈ 1,1; medical 0,76) and fy8-14's natural 5,1 mSv. The answer is still 67,8 % → 68 %, and solutions.md and answers.py are updated.
- Round 1 Blocking B (L3-04 c, radon practice): resolved. The task and the model answer now explain the stack effect, say that the official measurement is made in the heating season (≥ 2 months) and is on the safe side, and give a heating-season estimate of about 310–380 Bq/m³ > 300, so correction is recommended. The annual mean of 270 is correctly stated as below the reference level. "ei saa" is gone.
- Round 1 Polish resolved: L2-06 now gives 2 sf; the L3-05 heading is "Taulukon lukeminen" and the "graph" kind is gone; the chest X-ray is 0,10 mSv in both fy8-13-L1-08 and fy8-14-L2-05.
- L1-06: the options were reordered and reworded. There is still exactly one correct option, and every feedback is right.
- I recomputed all new answers with my own formulas: L1-07 0,20; L1-08 1,69; L2-05 67,8; L2-06 11,21; L2-07 7,0; L3-04 58,75 (b 9,19); L3-05 2,357. All are within tolerance and agree with answers.py.
- Counts are 8/7/5 and there are no duplicates. The levels match the plan.
- The hash b81e54ad228f16ca was the same at the start and at the end.
