VERDICT: PASS
CONTENT-HASH: 99b718d6f375af6f

## Blocking

## Polish
- exercises.json L2-01, L3-03 / answers.py docstring — I-131 8,02 d is attributed to NuDat 3, but ENSDF/NuDat gives 8,0252 d → 8,03 d; 8,02 d matches DDEP (8,0233 d). Cite DDEP or use 8,03 d (L2-01 → 0,999e-6, L3-03 → 6,99 %). Physically negligible.
- answers.py — stale comments: L1-02 "16,28 %" (is 16,29), L2-04 "0,6943 -> 0,694" (is 0,6953 → 0,695, as in exercises.json), L3-03 "6,96 %" (is 6,97) — fix the comments.
- solutions.md fy8-9-L3-02 — three significant figures justified "kuten ajassa 10,0 min", but the limiting data are the count rates 230 and background 30 (net 200, two figures); justify by those or give 5,0 min.

## Checked
- All twelve answers recomputed independently: 92,82; 16,29; 0,02303; 13,34; 24,0; 1,0003; 7,294; 777,2; 0,6953; 7957; 5,046; 6,972 — every exercises.json answer within tolerance.
- Half-lives vs ENSDF: Tc-99m 6,01 h, Rn-222 3,82 d, Cs-137 30,1 a, Co-60 5,27 a (λ 4,17e-9 1/s consistent), F-18 110 min, Am-241 433 a, C-14 5700 a correct.
- L2-02 mass check 0,29 µg right; 37 kBq realistic for a smoke detector.
- L2-04 Co-60 → Ni-60, mass proportional to N; total mass unchanged remark right.
- L3-02 background subtracted before the ratio; no-background value 5,45 min right.
- L3-03 assumption excluding daughters (Ba-137m) stated; I-131 share formula right.
- L3-01 assumption of constant C-14 fraction while living stated; symbolic log solution right.
- Every solution symbolic first, conversions (d → s, a → s, h min → min) right, reasonableness checks are real brackets.
