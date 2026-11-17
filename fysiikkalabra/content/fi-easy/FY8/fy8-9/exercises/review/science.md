VERDICT: PASS
CONTENT-HASH: f7903aada0819615
SCOPE: delta added-exercise from a4254015fd08611c base 5b3ca4f81c77

## Blocking

## Polish
- lessons/FY8/fy8-9/figures.py (pa_points description) — the description still says "Pisteet ovat samat kuin tehtävän taulukossa", which points to the Sovella task's table. L2-09 has no table. — Drop that sentence or reword it.
- content/fi-easy/FY8/fy8-9/exercises/exercises.json (L2-10 `tolerance` 0.03) — this accepts 0.136–0.144 1/h, which is T½ 4.81–5.10 h. A reading of 5.2 h would give 0.13 and be marked wrong. This is acceptable because 360 kBq at 5.0 h lies on a grid line. — Optionally use 0.05.

## Checked
- The hash was f7903aada0819615 at the start and at the end. I judged only L2-09 and L2-10. Their numbers, tolerances and solution steps match the Finnish version, and the S2 version drops no step.
- Fixed since round 1: the L2-09 tolerance is 0.02, which accepts 69.4–72.3 s and excludes 73.75 s, the answer without background subtraction. The solution now gives that answer as 73,7 s, which is correct.
- Fixed since round 1: the L2-10 check now uses (1/2)^(1/5,0) = 0.8706 left each hour (about 13 % decays) and 0.8706^5 = 0.500. I recomputed both.
- Fixed since round 1: the reason for three significant figures has been corrected, and the answers.py comment now says 70,85 → 70,9 s.
- I recomputed L2-09: 200 s · ln 2 / ln(375/53) = 70.851 s, and answers.py gives 70.850976. log2(375/53) = 2.82 halvings, so the "≈ 71 s" check holds.
- I recomputed L2-10: ln 2 / 5.0 h = 0.13863 1/h → 0.14, and answers.py gives 0.138629. Two significant figures fit the 5.0 h reading, and no unit conversion is needed.
- The principle "nettopulssimäärä noudattaa samaa lakia kuin aktiivisuus" is correct. In both solutions the unknown is solved symbolically first, and both stay within the FY8 decay-law scope.
