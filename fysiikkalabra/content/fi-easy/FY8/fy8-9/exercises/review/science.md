VERDICT: PASS
CONTENT-HASH: b196e1775b45499b

## Blocking

## Polish
- lessons/FY8/fy8-9/answers.py:21 — comment says "0,6943 mg -> 0,694 mg"; the code (and exercises.json, solutions.md) give 0,69526 → 0,695 mg — fix the comment.
- lessons/FY8/fy8-9/answers.py:27 — comment says "6,96 %"; computed value is 6,9725 % → 6,97 % — fix the comment.

## Checked
- All numbers in exercises.json and solutions.md match the passed Finnish source token for token.
- Recomputed with own formulas: L1 92,82 MBq, 16,29 %, 0,02303 1/a, 13,34 kBq, 24,0 h; L2 1,0003·10⁻⁶ 1/s, 7,294·10¹⁴, 777,2 MBq, 0,6953 mg; L3 7957 a, 5,046 min (5,45 min without background), 6,972 %. All agree with exercises.json and answers.py output.
- L2-02 mass check ≈ 0,29 µg correct; L2-01 0,91⁸ ≈ 0,47 check correct.
- Conditions stated where used: no new radon (L1-02), constant background (L3-02), daughters not counted (L3-03), constant C-14 fraction in a living plant (L3-01).
- Each solution solves symbolically before substituting; conversions (d → s, a → d, 2 h 30 min → 150 min) correct.
- Significant figures follow the limiting datum (37 kBq → 2 figures in L2-02).
- Easy-language rewrites keep the physics; no new claims.
