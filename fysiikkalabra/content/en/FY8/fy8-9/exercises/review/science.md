VERDICT: PASS
CONTENT-HASH: 9136b7411732c7ca
SCOPE: delta added-exercise from c0842f06ba77912b base 5b3ca4f81c77

## Blocking

## Polish
- lessons/FY8/fy8-9/figures.py (pa_points description) — the description still says "Pisteet ovat samat kuin tehtävän taulukossa", which points to the Sovella task's table. L2-09 has no table. — Drop that sentence or reword it.
- content/en/FY8/fy8-9/exercises/exercises.json (L2-10 `tolerance` 0.03) — this accepts 0.136–0.144 1/h, which is T½ 4.81–5.10 h. A reading of 5.2 h would give 0.13 and be marked wrong. This is acceptable because 360 kBq at 5.0 h lies on a grid line. — Optionally use 0.05.
- review packet — the packet's exercise brief (the en lesson extract) is empty. I checked the notation (N, N_0, T_{1/2}, λ, A, B) against the Finnish brief and it matches.

## Checked
- The hash was 9136b7411732c7ca at the start and at the end. I judged only L2-09 and L2-10. Their numbers, tolerances and solutions match the Finnish version.
- Fixed since round 1: the L2-09 tolerance is 0.02, which accepts 69.4–72.3 s and excludes 73.75 s, the answer without background subtraction. The solution now says 73.7 s, which is correct.
- Fixed since round 1: the L2-10 check now uses (1/2)^(1/5.0) = 0.8706 left each hour (about 13 % decays) and 0.8706^5 = 0.500. I recomputed both.
- Fixed since round 1: the reason for three significant figures has been corrected, and the answers.py comment now says 70,85 → 70,9 s.
- I recomputed L2-09: 200 s · ln 2 / ln(375/53) = 70.851 s, and answers.py gives 70.850976. log2(375/53) = 2.82 halvings, so the "≈ 71 s" check holds.
- I recomputed L2-10: ln 2 / 5.0 h = 0.13863 1/h → 0.14, and answers.py gives 0.138629. Two significant figures fit the 5.0 h reading, and no unit conversion is needed.
- In both solutions the law is stated, the unknown is solved symbolically first and the background is subtracted before the logarithm. Both stay within the FY8 decay-law scope.
