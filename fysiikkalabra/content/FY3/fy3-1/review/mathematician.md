VERDICT: PASS
CONTENT-HASH: 307c0dfc144588a5
1. solutions.md:45 — minor, no action needed — intermediate 4,995 kg is 4,9949 rounded to 4 sf; the final 5,0 kg is correct and a student's 4,99 or 5,0 is within tolerance 0,02.
2. exercises.json (all 12) — no problem — every answer equals the solutions.md final answer. A student who rounds correctly to the data's sf stays inside the 0,02 relative tolerance. The largest deviation is L1-03 at 0,8 % (49 against 48,6).
3. solutions.md (all substitutions) — no problem — all 12 were recomputed in python3 -I and match. The units are consistent: kg · m/s² = N in every G = mg line, N / (m/s²) = kg in L2-01, L3-02 and L3-03, and the cm ratios are dimensionally fine.
4. exit-ticket.json:3, 11 — no problem — the answers 29 N, 4,9 N, 7,5 cm and about 690 N are correct (29,43; 4,86; 20/8 · 3,0; 686,7). Rounding is fine at 2 sf.
5. lesson.md:23-28, 45-47, 52, 57 — no problem — the g table (1,62; 3,71; 9,81; 24,8 m/s²) is consistent with the exercises. Worked example: 120 · 9,81 = 1177,2 ≈ 1180 N = 1,18 kN, and 120 · 3,71 = 445,2 ≈ 445 N. The 70 kg ≈ 690 N claim and the "about one sixth" remarks (1,62/9,81 = 0,165) hold.
6. check_latex.py — all LaTeX ok (7 fragments).
