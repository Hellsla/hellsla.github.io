VERDICT: PASS
CONTENT-HASH: da9ba5eb24ac7a54

All 12 solutions recomputed in Python (python3 -I): every substitution, intermediate and final value is correct; every exercises.json answer equals the solutions.md final answer; each answer is rounded to the data's significant figures and lies within 0,7 % of the unrounded exact value (largest: L1-01, 0,62 %), so a student who rounds correctly, or who gives the unrounded value, is inside the relative tolerance 0,02. check_latex.py: all LaTeX ok (7 fragments). Table g values (1,62 / 3,71 / 9,81 / 24,8 N/kg) correct. SVG labels correct (G = m g arrow pointing down, spring, m, labels in plain text). Sanity checks in solutions are numerically correct (1,62/9,81 = 0,165 ~ 1/6; 3,71/9,81 = 0,378 ~ 38 %; 83 % decrease; 2,53-fold for Jupiter). No wrong first step in any solution.

Minor, non-blocking findings:
1. lesson.md:43 vs :45 — worked example gives Earth weight to 4 sf (1177 N, from 1177,2) but Mars weight to 3 sf (445 N, from 445,2) for the same 120 kg datum; inconsistent sf — use the same precision in both, e.g. 1177 N and 445 N are both fine if the datum is read as 3 sf, but then 1177 should be 1180 N (≈ 1,2 kN) to match house rule "as many sf as data".
2. solutions.md:77 — "m = 18 N / 9,81 N/kg = 1,835 kg" shows a rounded intermediate with "=" (exact 1,8349 kg); house rule says show unrounded intermediates — write m = 18/9,81 kg ≈ 1,8349 kg, G_Mars = 18/9,81 · 3,71 N = 6,807 N (result unaffected).
3. solutions.md:37 — "62,0 N" carries 3 sf while data (2,5 kg) has 2 sf; harmless since the stated answer is 62 N.
4. lesson.md:43,45 — units use "\ " (backslash-space); NOTES.md rule 3 prefers "\," in new text. Cosmetic.
