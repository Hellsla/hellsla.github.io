VERDICT: PASS
CONTENT-HASH: 42492e47d1fafc99
Round: 3

Round 3 checks the last commit (`git show HEAD -- content/fi/FY3`), which touches only the fy3-4 L3-05 Järkevyys line; the rest is covered by the round-2 PASS.

## Blocking
- none

## Polish
- exercises.json:74 (L1-07): carried over. Third plain ρgh task at level 1 after L1-02 and L1-05; acceptable.

## Checked
- The round-2 Polish on L3-05 Järkevyys is resolved. "122,6 · 3 ≈ 367,9", "· 5 ≈ 613,1", "· 7 ≈ 858,4" now use ≈. Recomputed: 122,625 kN · 3 = 367,875, · 5 = 613,125, · 7 = 858,375, which round to 367,9 / 613,1 / 858,4, and 122,6 · 3 = 367,8 is within rounding of 367,9, so ≈ is correct.
- The change is consistent with Vastaus (F4 = 858 kN, F4 : F1 = 7,0), part c) (sum 1962 kN = 98,1 kPa · 20,0 m²) and the answer 858,4 kN in the task. No numbers changed.
- The hash was the same at the start and at the end.
