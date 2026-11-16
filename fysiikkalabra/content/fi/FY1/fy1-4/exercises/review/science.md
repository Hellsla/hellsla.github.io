VERDICT: PASS
CONTENT-HASH: 72a265bfa9067748
SCOPE: delta added-exercise fy1-4-L2-09 (work queue 19), round 2

## Blocking

## Polish
- content/fi/FY1/fy1-4/exercises/exercises.json:343 — The task asks for data "tunnin välein", but the fallback table and the solution's "Annettu" use 2 h steps (carried over from round 1; recorded in the PR) — optionally "tunnin tai kahden tunnin välein".

## Checked
- Hash 72a265bfa9067748 at the start and at the end.
- Round-1 Blocking fixed: solutions.md:237 now gives 22,4 °C at 16 h. My recomputation: T(16) = 7,2 °C + 1,5167 °C/h · 10 h = 22,37 °C, which rounds to 22,4 °C.
- I recomputed the other model values again and they still agree: T(8) = 10,2 °C, T(10) = 13,3 °C, T(0) = −1,9 °C, and the difference inside the interval is at most 0,2 °C.
- answers.py gives 1.516667, which matches the key 1.517 with a tolerance of 0,03. Two significant figures is right (ΔT = 9,1 °C; the 6 h span is exact).
- Nothing else in the exercise changed since round 1. The physics, scope, labelling of the invented data and the mechanism in d) stay as judged then.
