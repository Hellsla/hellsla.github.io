VERDICT: PASS
CONTENT-HASH: d5bc25b33d24fba8
ROUND: 2

## Blocking

## Polish
- exercises.json:124 (L2-02, an existing task): still "käämin läpi kulkeva magneettivuo". Fix: "yhden kierroksen läpi", as in L1-08 and L2-07 now.
- solutions.md L2-05 c): "voima on molemmissa sama, mutta vauhti on pienempi, joten jarruttaa voimakkaammin samalla vauhdilla" uses F ∝ v (or at least F increasing with v), but the task does not state that. Fix: add "kun jarruttava voima kasvaa vauhdin mukana".

## Checked
- All round-1 Polish items are done. L2-04: the out-of-range clause was dropped. L1-08 and L2-07 now say "yhden kierroksen" flux. L2-07 says "keskimääräinen induktiojännite" in the text and in the Periaate. L3-04 c) now asks for the (t, v) graph.
- L3-05 new data (1,00/0,80/0,50/0,25 mm): the sheets are now below the skin depth (about 0,7 mm at 50 Hz, borderline at 1,00 mm), and the task states the thin-sheet condition. P/d² = 1,21; 1,19; 1,24; 1,17, so k = 1,201 W/mm² and P(0,35 mm) = 0,147 W → 0,15 W, within tolerance. d) now compares with 0,35 mm: (1,0/0,35)² = 8,2, which is right.
- L2-05: t̄ = 7,32 s, P = 26,8 mW; F:v = 1,44 against 0,78 N·s/m. The 3,3 s difference is far above the ±0,3 s spread.
- L3-04: the new explanation of the 6 % gap (the curvature of a central difference) is right. The exact model gives 2,79 against a tangent of 2,61 m/s².
- L2-07: e·Δt has a mean of 0,1046 V·s, so ΔΦ = 0,349 mWb. c) is answered in the solution.
- L1-06 and L1-07: the options were reordered and shortened. Exactly one option is correct, the distractors are still wrong, and the feedback is unchanged and right.
- I recomputed all new answers in one script, and they agree with answers.py: L1-08 6,0 V; L2-05 26,8 mW; L2-07 0,349 mWb; L3-04 2,65 m/s²; L3-05 0,147 W.
- Hash unchanged at start and end.
