VERDICT: PASS
CONTENT-HASH: 0b90ff02126c7319

## Blocking

## Polish
- exercises.json:50 and :63 (L1-06, correct option) — "joiden reitit risteävät lähteen kohdalla": two back-to-back photons lie on one line through the source, so one pair does not locate it along that line. Say "joiden yhdistävä jana kulkee lähteen kautta", matching the feedback and the lesson ("monien janojen leikkauskohdat").
- exercises.json:131 (L2-05) — the plan asks for STUK doses with source and year. The task has unsourced example data, and the chest image (0,050 mSv) differs from fy8-13-L1-08 (0,10 mSv). Add "(STUK-A263, 2020)" to the 5,1 mSv (STUK: 4,0 radon + 1,1 other natural) and use one chest value in both chapters.
- solutions.md:189 (L3-05) — "kaksi merkitsevää numeroa kuten laskentataajuudessa 402" is wrong, because 402 has three figures. The limit comes from d½ read from the calibration (thickness steps 5,0 mm). The plan says "kalibrointisuora": a fit of ln R against d gives d½ 9,18 mm and d_x 12,1 mm, the same answer. The solution could mention it instead of using only the two end points (guardrails: read from the fit, not from raw points).
- exercises.json:90 (L1-08) — `kind` "concept" on a pure E = eU calculation; drop it. exercises.json:74 (L1-07) replaces the plan's "hoitoannoksen jako useaan suuntaan" with optimisation; update docs/exercise-bank/FY8.md (likewise paper → aluminium in L3-05, which is the better physics for 60 keV).
- solutions.md L2-07 Järkevyys — "1,7 mm pysäyttäisi … vain 0,44 puoliintumispaksuutta" reads oddly; write "on vain 0,44 puoliintumispaksuutta".

## Checked
- All new answers recomputed in one script: L1-08 1,28·10⁻¹⁴ J; L2-05 41,8 %; L2-06 51,1 % (decay only 125,3 MBq; effective half-life about 4,0 h, implied biological about 12 h); L2-07 25,9 mm; L3-04 10,16 mSv (A₀ 218,9 MBq); L3-05 12,10 mm (d½ 9,147 mm). All within tolerance, and answers.py matches.
- L1-06: one correct option; the distractor feedback is right (positron range in mm, charge, energy always 511 keV).
- L2-07: the error (140 keV d½ used) is exactly the planned one; n = 6,64 is right.
- L3-04: the decay correction goes the right way (injected > needed), the dose coefficient applies to the injected activity, and b) covers justification and optimisation.
- Real-world values are plausible: Tc-99m 6,01 h/140 keV; F-18 110 min; FDG 0,019 mSv/MBq (ICRP 128); Pb d½ 3,9 mm at 511 keV and 0,26 mm at 140 keV; Al d½ about 9,2 mm at 60 keV (from μ/ρ 0,278 cm²/g); Am-241 432 a/37 kBq; C-14 5700 a; natural 5,1 mSv = STUK-A263 4,0 + 1,1.
- Counts are 8/7/5; no duplicates. The "FAIL inquiry" check belongs to the lesson, not to this set.
- The hash 0b90ff02126c7319 was the same at the start and at the end.
