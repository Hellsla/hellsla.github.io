VERDICT: PASS
CONTENT-HASH: f7ecb1340f4d3f77

Delta review over the audit's PASS (c0fb046ec7a38f96): L1-04 replaced by figure task spring-points, LaTeX units elsewhere.

## Blocking
- none
## Polish
- exercises.json L2-04 and lesson text still mix plain "1,5 cm" with LaTeX units; mechanical only.
## Checked
- L1-04 recomputed: figure points (2;1)…(10;5) give x/F = 0,5 cm/N, F = 3,5 cm / 0,5 cm/N = 7,0 N; answers.py gives 7,0.
- Figure spring-points (360 px capture and code): all five points on 1 N × 1 cm grid crossings; the description lists the points, not the ratio or the answer.
- Tolerance 0,03 accepts 6,79–7,21 N, which covers the solution's stated 6,8–7,2 N; F_1·x read off a neighbouring point gives the same value, and wrong methods (x·F, 3,5 N) are rejected.
- Significant figures: 7,0 N, two, as in 3,5 cm; solution has Kuvaajan lukeminen and all seven steps.
