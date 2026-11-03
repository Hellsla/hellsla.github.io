VERDICT: PASS
CONTENT-HASH: 1fbeee1ab1b2405e

## Blocking

## Polish

## Checked
- Recomputed all 12 answers with own formulas: L1 2,0 mGy; 6,0 mSv; 15 µSv; 7,5 µSv/h; 8,0 µSv/h. L2 1,2 mSv; 4,17 → 4,2 h; 12,8 → 13 mSv; 30 mm. L3 +5,0 µSv; 18,9 → 19 mSv; 0,74 mSv. answers.py matches.
- L1-03 (changed): "noin 3 µSv/h" × 5,0 h = 15 µSv; solution correctly calls it an order-of-magnitude estimate; 15 µSv/5,9 mSv < 0,3 %.
- Puoliintumispaksuus $d_{1/2}$ used consistently in L1-05, L2-04, L3-01 and answers.py.
- STUK-A263 figures: radon 4,0 mSv at 94 Bq/m³, others 5,9 − 4,0 = 1,9 mSv (L3-02) consistent with the source.
- Conditions stated: point source, no air attenuation, proportionality of radon dose to concentration, uniform whole-body gamma (ΣwT = 1) in L3-03.
- Significant figures and reasonableness checks sound in every solution.
