VERDICT: PASS
CONTENT-HASH: 43ecf04c9f072b4f
Round: 2

## Blocking

## Polish
- solutions.md:188 (L3-05) — The heading "Kuvaajan lukeminen" sits on a task that has only a table. — Use "Taulukon lukeminen", as fy8-13-L3-05 now does.
- exercises.json L1-07 / L3-05 — The deviations from the plan (optimisation instead of splitting the treatment dose across several directions; aluminium instead of paper) are still not recorded in docs/exercise-bank/FY8.md. Update the plan.

## Checked
- Round 1 had no Blocking items.
- Round 1 Polish resolved: in L1-06 the correct option and the model answer now say "yhdistävä jana kulkee lähteen kautta"; L2-05 cites STUK-A263 (2020) for 5,1 mSv; the chest image is 0,10 mSv as in fy8-13; L1-08 no longer has the "concept" kind; L2-07 now says "on vain 0,44 puoliintumispaksuutta".
- L2-05 changed: 3 · 0,010 + 2 · 0,10 + 2,0 = 2,23 mSv, which is 43,7 % of 5,1. The answer 44 % (tol 3 %) and answers.py match.
- L3-05: the new fit check is right. My least-squares fit of ln R on d gives d½ = 9,18 mm and d_x = 12,13 mm. The new reason for 2 significant figures (the ratios scatter 0,68 ± 0,01) is sound.
- L1-06: the distractors were reworded. There is still exactly one correct option, and the brems-strahlung feedback is right (the annihilation photons are always 511 keV).
- All the other new answers are unchanged and still agree with answers.py: L1-08 1,28·10⁻¹⁴ J; L2-06 51,1 %; L2-07 25,9 mm; L3-04 10,16 mSv; L3-05 12,10 mm.
- Counts are 8/7/5 and there are no duplicates. The "FAIL inquiry" check concerns the lesson, not this set.
- The hash 43ecf04c9f072b4f was the same at the start and at the end.
