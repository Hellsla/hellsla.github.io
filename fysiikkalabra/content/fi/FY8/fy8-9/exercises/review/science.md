VERDICT: FAIL
CONTENT-HASH: 2661f89128265fc3

## Blocking
- content/fi/FY8/fy8-9/exercises/exercises.json:374 (L2-09 `tolerance`) — A, assessment: relative 0.05 accepts 67.3–74.4 s, so it accepts the result without background subtraction (73.7 s), which is the very error the task targets. The counts are given in the text, so no reading spread needs allowing for — use 0.02 (69.5–72.3 s) and adjust solutions.md:255 ("so the tolerance is wider").
- content/fi/FY8/fy8-9/exercises/solutions.md:260 (L2-09, Järkevyys) — A, number: 200 s · 0.69315 / ln(380/58) = 138.63 s / 1.8797 = 73.7 s, not 73.9 s — write $73{,}7\,\text{s}$.
- content/fi/FY8/fy8-9/exercises/solutions.md:271 (L2-10, Järkevyys) — A/B: "about 14 % decay each hour" treats λΔt as the share decayed over a finite interval, which holds only when λΔt ≪ 1 (here 0.139). The true share is 1 − (1/2)^(1/5.0) = 12.9 %, and 0.86^5 = 0.47 comes only from that approximation. Fix: "each hour (1/2)^(1/5.0) ≈ 0.871 is left (about 13 % decays), and 0.871^5 ≈ 0.50", or check e^(−0.1386 · 5.0) = 0.500.

## Polish
- content/fi/FY8/fy8-9/exercises/solutions.md:259 (L2-09) — the reason for three figures is wrong: 5 has one, 58 has two, and both are "about" values. Give the right reason (the counts are given values), or give 71 s.
- lessons/FY8/fy8-9/answers.py:331 — the comment says "-> 70,8 s", but the answer is 70.9 (70.851).
- fy8-9/pa-points description — "samat kuin tehtävän taulukossa" refers to the Sovella task's table. This exercise has none.

## Checked
- Hash 2661f89128265fc3 at the start and the end. I judged only L2-09 and L2-10.
- Figure data (lesson-answers.py `counts`): simulated with T½ = 69.54 s and a background of 0.5 1/s · 10 s = 5 per 10 s, which matches the task. PA_Y at 0 s is 380 and at 200 s is 58, which match the task.
- L2-09 recomputed: 200 · ln 2 / ln(375/53) = 70.851 s (answers.py 70.851), 1.9 % from the true 69.5 s. Readings of 370–390 and 55–61 give 68–74 s.
- L2-09: the background is subtracted before the logarithm, T½ is solved symbolically, and the 2.8-halvings check is right.
- L2-10: A0 = 720 kBq, T = 5.0 h. 360 kBq at 5.0 h lies on the 1 h grid. λ = ln 2/5.0 h = 0.1386 1/h → 0.14 (answers.py 0.138629). Two figures from 5.0 h. Units 1/h with no conversion. Inside scope.
