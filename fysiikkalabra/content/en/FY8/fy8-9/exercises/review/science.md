VERDICT: PASS
CONTENT-HASH: 5956ef5842dcecd2

## Blocking

## Polish
- answers.py:fy8-9-L2-04 comment "0,6943 mg -> 0,694 mg" and fy8-9-L3-03 comment "6,96 %" are stale: the code gives 0.6953 mg and 6.972 %, matching exercises.json (0.695, 6.97) and solutions.md; fix the comments only.

## Checked
- Recomputed all 12 answers independently: 92.82 MBq, 16.29 %, 0.02303 1/a, 13.34 kBq, 24.0 h, 1.0003e-6 1/s, 7.294e14, 777.2 MBq, 0.6953 mg, 7957 a, 5.046 min, 6.972 % — all within tolerance and agree with answers.py.
- answers.py uses the right physics (decay law, λ = ln 2/T½, A = λN, m ∝ N, background subtracted before the ratio).
- L3-02: net rates 790 → 200; without subtraction 5.45 min, as the reasonableness says.
- L3-03: shares computed with both half-lives in days (Cs 10 994 d); daughter decays excluded as stated.
- L2-02: Am-241 mass ≈ 0.29 µg, consistent with "about 0.3 µg"; L1-04 λ(Co-60) = 4.17e-9 1/s matches T½ = 5.27 a.
- Every solution symbolic first, conversions shown, rounding justified by the limiting datum; reasonableness checks are real checks.
- No scope beyond FY8 central contents (decay law, activity).
