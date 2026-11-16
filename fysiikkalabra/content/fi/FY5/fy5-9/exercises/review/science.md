VERDICT: PASS
CONTENT-HASH: b83d89918db889fd

## Blocking

## Polish
- solutions.md:150 (L2-05): "Lyhimmän heilurin arvoissa (0,20 m ja 0,90 s) on vain kaksi" reads as if only that row had two figures. The lengths 0,40, 0,60 and 0,80 m have two as well. The justification from the point (1,00 m; 2,01 s) stands. Fix: "Pituuksissa 0,20–0,80 m ja ajassa 0,90 s on vain kaksi".

## Checked
- The hash was the same at the start and at the end. Round 2 judged only `git diff 09d57eb5ac..HEAD`. Unchanged content rests on the round-1 review, which recomputed all 22 answers.
- L2-05: 2,01² / 1,00 = 4,040 s²/m and 4π²/4,04 = 9,772 m/s². Reading the slope at the (1,00 m; 2,01 s) point supports three figures. The round-1 Polish is fixed.
- answers.py:32 (L2-06): only the comment changed, and it now matches the solution: 4π²/1,96 = 20,14 N/m → 20 N/m. The stored value is unchanged.
- L2-07: T − T₀ = 2,15 − 2,006 = 0,144 s ≈ 0,14 s, two figures. Naming it as the period difference removes the clash with part b)'s t₁₀ differences, so the round-1 Polish is fixed. p = 7,17 % → 7,2 %.
- L3-05: the answer was split into a), b) and c) on their own lines. The values 0,549 s, 0,598 m/s, 1,82 cm, 0,599 m/s and 0,13 % are unchanged.
