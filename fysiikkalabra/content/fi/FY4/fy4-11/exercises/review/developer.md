VERDICT: DONE

Round 1, exercises (fi, en, fi-easy): one new data task (teacher's brief FY4-A1) and three proofreading fixes (work queue 18).

- `lessons/FY4/fy4-11/answers.py`: new block for `fy4-11-L2-10` (Liikenneturva's stopping distance calculator, read 16.11.2026): every number of the solution, asserts that the model reproduces the app's rounded values; answer 69,4 km/h. No existing line changed.
- `exercises.json` (three languages): `fy4-11-L2-10` appended to level 2, kind data/graph/model/reasoning, parts a)–e), source link, answer 69.397…, km/h, tolerance 0.03. The date is written "16. marraskuuta 2026" because the lint reads "16.11." as a decimal point.
- `solutions.md` (three languages): complete dated example solution for L2-10 (source facts named, s_j derived from the definition of deceleration and the triangle area, model limits). Fixes: L2-05 "kahden tai kolmen numeron"; L3-05 answer $18\,\text{kN}$, two significant figures as in the speed change 4,5 m/s; L3-06 answer $11\,\text{kN}$ (computed 10,5 kN), justification rewritten. `answer` fields 18.0 and 10.5 unchanged; tolerances accept 18 and 11.

Checks: lint 0 errors (L2-10 length warning, 968 words: five parts), check_solutions ok, check_i18n clean for fy4-11, check_lesson all ok, layout 360 and 352 px ok.
