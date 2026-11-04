VERDICT: PASS
CONTENT-HASH: eab7c7c57617b167
Round: 3

## Blocking

## Polish
- exercises.json:163 (L2-06) — `answer` is 11.2, but solutions.md:164 gives 11 µSv/h as the answer (2 sf). The 3 % tolerance accepts both. — Optionally store 11 so that the answer box and the solution say the same.
- solutions.md:186 (L3-04 c) — Treating syksy, talvi and kevät as the heating season is a fair simplification (C). The official measurement period (about November–April) is shorter, so the 313 is a model estimate. — Optionally write "noin" or "tämän aineiston mukaan" before the 313.
- L3-04 b) still repeats the proportional radon scaling of L2-03 and L3-02. Parts c) and d) carry the level-3 weight, which is acceptable.

## Checked
- Round 2 visual item (L2-05): resolved for the physics. The row label is now "Muu luonnon säteily" (exercises.json:145). The task text lists what it contains: soil and building materials, cosmic radiation and the body's own radioactive substances. This matches STUK-A263 (about 1,1 mSv). The answer is still 4,0 / 5,9 = 67,8 % → 68 %, and the solution's Annettu uses the same label.
- Round 2 pedagogy item (L3-04 c): resolved. (300 + 380 + 260) / 3 = 313,3 Bq/m³ > 300, which follows from the table. The annual mean of 270 < 300 is still stated correctly, the factor 380 / 270 = 1,4 is correct, and the measurement practice (heating season, ≥ 2 months, on the safe side) is unchanged.
- The last commit 47331a4a7 changes only these two places. Nothing else in exercises.json, solutions.md or answers.py changed.
- Full recompute in one script, with my own formulas and against answers.py: all 19 numeric answers agree and are within tolerance (L2-03 12,77 → 13, rel 1,8 %; L3-05 2,357 → 2,4). A log-linear fit of the L3-05 table gives d½ = 3,99 cm ≈ 4,0 cm.
- L1-06 still has exactly one correct option, and every feedback is right.
- Counts are 8/7/5 and the levels match the plan.
- The hash eab7c7c57617b167 was the same at the start and at the end.
