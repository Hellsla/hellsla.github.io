VERDICT: PASS
CONTENT-HASH: 931d64b231b7ad76
Round: 2

Round 2: I reviewed the round-1 fixes (`git diff HEAD~1`) in the 20-task set. Round 1 had no Blocking items, so this round checks that the Polish fixes and the rewordings are correct.

## Blocking
- none

## Polish
- solutions.md:205 (L3-05 Järkevyys): "$122{,}6 \cdot 3 = 367{,}9$" is wrong by 0,1, because $122{,}6 \cdot 3 = 367{,}8$. The 367,9 comes from $122{,}625 \cdot 3 = 367{,}875$. Fix: write "$122{,}625 \cdot 3 \approx 367{,}9$" (and the same for ·5 and ·7), or compare the rounded values with "≈".
- exercises.json:74 (L1-07): carried over from round 1. This is the third plain ρgh task at level 1, after L1-02 and L1-05. It is acceptable but adds little.

## Checked
- Round-1 Polish was resolved. L3-04 Järkevyys now says correctly that the deviation covers the top 15 m and is 0,03 % in the middle layer, and that the total is 0,060 % (118/196 200). Of the 118 Pa deficit, 75 % comes from the surface layer.
- Round-1 Polish was resolved. The "Kuvaajan lukeminen" headings over tables are now "Taulukon lukeminen" (L2-05, L2-06, L3-04, L3-05), and the `graph` tag was removed from L2-05.
- Round-1 Polish was resolved. L3-05 now gives the reason for three significant figures as 15,0/20,0 m plus a strip of exactly one metre. The task text says "yhden metrin levyistä kaistaa", so this is consistent.
- L1-06 and L1-08 rewordings: each still has exactly one correct option, the answer string matches the correct choice, and the feedback is unchanged and right.
- I recomputed all eight new answers with my own formulas in one script, and they agree with answers.py and are within tolerance: L1-07 394,4 → 390 kPa; L2-05 p0 99,73 kPa (least squares 9,777 kPa/m, 99,75 kPa), ρ = 997 kg/m³; L2-06 2,943 kPa; L2-07 1,422 kPa; L3-04 0,1177 kPa, 1,2 cm vs 5,1 cm; L3-05 parts 122,6/367,9/613,1/858,4 kN, sum 1962 kN = whole strip, ratio 7,0.
- Scope is still p = F/A and p = p0 + ρgh. There are no duplicates, the levels are 8/7/5, and the set follows the plan.
- The L3 screenshot at 1280 px (part 8, after the fix commit) renders the changed L3-05 Vastaus cleanly.
- The hash was the same at the start and at the end.
