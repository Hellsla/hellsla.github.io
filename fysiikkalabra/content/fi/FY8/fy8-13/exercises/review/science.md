VERDICT: PASS
CONTENT-HASH: 6c515bafbae4fe34

## Blocking

## Polish
- exercises.json L2-03, L3-02; answers.py docstring — the radon figure 4,1 mSv/a at 94 Bq/m³ and "STUK 2023" could not be verified here (stuk.fi not reachable); search results give radon "noin 4 mSv" in STUK-A263 (2020). Check against STUK's current page; the answers (13 and 19 mSv) do not change at 2 significant figures if 4,0 is used (12,8 → 13; 18,8 → 19).
- exercises.json L1-03 — 3,2 µSv/h at cruise altitude is plausible (typical 2–5 µSv/h at Finnish latitudes) but not sourced; consider "esimerkiksi" or a source.
- exercises.json L2-01 — a diagnostic thyroid study gives mostly gamma (Tc-99m, I-123); beta absorption in the thyroid fits I-131 therapy. Physics correct (C); wording could say "radiojodihoidossa" or keep as a model case.

## Checked
- All 12 answers recomputed with my own formulas in one script; all match answers.py and exercises.json (2,0; 6,0; 16; 7,5; 8,0; 1,2; 4,17; 13,09; 30; 5,0; 19,25; 0,74).
- Units and tolerances fit 2–3 significant figures; rounding reasons name the limiting data.
- Inverse-square tasks state point source / no air attenuation (L1-04) or the lesson's model.
- Half-value-layer tasks use whole numbers of layers; L2-04 solved symbolically with log2 first.
- L3-03 correctly weights the alpha lung dose by w_T and the uniform gamma dose by Σw_T = 1.
- Radon tasks state the proportionality and equal-occupancy assumptions.
- w_R and w_T values match ICRP 103 and the lesson.
- Reasonableness checks are real checks (chains of halvings, L2-02 back-substitution 24 µSv/h · 4,2 h).
