VERDICT: PASS
CONTENT-HASH: 2193c5830d2fca7f

## Blocking

## Polish
1. solutions.md:63 — the sanity check says the weight drops about 83 % "which corresponds to the ratio 1,62 / 9,81 ≈ 1/6"; the 1/6 is what remains, not the drop — write "Kuussa paino on 1,62 / 9,81 ≈ 1/6 Maan painosta, joten se pienenee noin 5/6 eli 83 %".
2. solutions.md:7 — "Yksi kilogramma painaa noin 10 N, joten 4 kg painaa noin 40 N" equates mass and weight, the exact slip lesson.md:52 warns against — write "1 kg:n massan paino on noin 10 N, joten 4,0 kg:n massan paino on noin 40 N".
3. lesson.md:38-39 — the weight arrow G is drawn at x = 280, detached from the block (x 160–240), so it does not visibly act on the body — start the shaft on the block, e.g. at its centre (200, 206) with the "m" label moved aside, or at its bottom edge.

## Checked
- Hash at start and end: 2193c5830d2fca7f (unchanged); lint 0 errors, 0 warnings.
- All 12 solutions recomputed step by step; every intermediate (39,24; 48,6; 4,995; 0,5886; 1422,45 − 234,9 = 1187,55; 1,962 · 3 = 5,886; 18/9,81 ≈ 1,8349 → 6,807; 215,82/1,62 = 133,2; 9,72/9,81 = 0,991) is correct.
- Rearrangements m = G/g, m_Kuu = F/g_Kuu, reading = G/(9,81 N/kg) are correct, with consistent units (N ÷ N/kg = kg).
- Proportional-stretch ratios in L1-02, L1-04, L2-04 and exit ticket 2 (20/8,0 = 2,5 → 7,5 cm) are correct.
- Rounding happens only at the end; L3-01 carries 18/9,81 unrounded.
- answers.py follows the same routes as solutions.md (L2-03 as 145 · (9,81 − 1,62), same value).
- Sanity checks: 30 · 9,81 = 294 N; 24,8/9,81 = 2,53; 3,71/9,81 = 0,378; 133,2/22,0 = 6,06; 0,991/6,0 = 0,165 — all hold.
- lesson.md numbers: 0,1 kg → 0,981 N ≈ 1 N; 5,0 N : 2,0 cm scaling; 1177,2 → 1180 N = 1,18 kN; 445,2 → 445 N; 70 kg → 686,7 ≈ 690 N; 1,62/9,81 = 0,165 ≈ 1/6; g table values correct.
- Exit ticket 1: 29,43 → 29 N, 4,86 → 4,9 N.
- Notation G, m, g (N/kg) consistent between lesson.md and solutions.md; (voima, venymä) graph through the origin stated correctly; SVG spring and block symmetric about x = 200, all elements inside the 600×300 viewBox.
