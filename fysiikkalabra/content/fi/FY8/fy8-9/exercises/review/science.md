VERDICT: PASS
CONTENT-HASH: 54537ad9c998f1a3
SCOPE: delta added-exercise from d9ba28cfd425b32a base 5b3ca4f81c77

## Blocking

## Polish
- lessons/FY8/fy8-9/figures.py (pa_points description) — the description still says "Pisteet ovat samat kuin tehtävän taulukossa", which points to the Sovella task's table. L2-09 has no table. — Say "simuloitu esimerkkiaineisto" only, or name the data as the figure's own.
- content/fi/FY8/fy8-9/exercises/exercises.json (L2-10 `tolerance` 0.03) — this accepts 0.136–0.144 1/h, which is T½ 4.81–5.10 h. A student who reads 5.2 h from the 1 h grid and answers 0.13 is marked wrong. This is acceptable because 360 kBq at 5.0 h lies on a grid line. — Optionally use 0.05.

## Checked
- The hash was 54537ad9c998f1a3 at the start and at the end. I judged only L2-09 and L2-10.
- Fixed since round 1: the L2-09 tolerance is 0.02, which accepts 69.4–72.3 s. That excludes 73.75 s, the answer without background subtraction, which the solution now correctly gives as 73,7 s.
- Fixed since round 1: the L2-10 check now says (1/2)^(1/5,0) = 0.8706 is left each hour (about 13 % decays) and 0.8706^5 = 0.500. I recomputed both.
- Fixed since round 1: the answers.py comment now says 70,85 → 70,9 s, and the reason for three significant figures has been corrected.
- I recomputed L2-09: 200 s · ln 2 / ln(375/53) = 70.851 s, and answers.py gives 70.850976. The data hold log2(375/53) = 2.82 halvings, so the "≈ 71 s" check is right.
- I recomputed L2-10: ln 2 / 5.0 h = 0.13863 1/h → 0.14, and answers.py gives 0.138629. Two significant figures fit the 5.0 h reading, and the 1/h unit needs no conversion.
- In both solutions the law is the lesson's, the unknown is solved symbolically before substitution, and the background is subtracted before the logarithm. Both stay within the FY8 decay-law scope.
