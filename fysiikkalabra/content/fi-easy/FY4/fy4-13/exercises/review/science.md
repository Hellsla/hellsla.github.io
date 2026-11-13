VERDICT: PASS
CONTENT-HASH: 496c2894012706cc
SCOPE: delta added-exercise from 32606fe51d18f6ad base 81db4a6fd727
Mode: delta (added figure tasks fy4-13-L2-09 and L3-06, Selkeä suomi against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Polish
- content/fi-easy/FY4/fy4-13/exercises/solutions.md:463 — the answer is written 1,21 kg (three figures) but the sentence says two figures (same in fi) — write 1,2 kg with the two-figure reason, or keep 1,21 and say why a third figure is kept; in fi as well.

## Checked
- Script comparison with content/fi/FY4/fy4-13: same ids, levels, kinds, answers, units, tolerances, figure, fbd and every number in text and solutions (fi-easy only splits sentences; one clause on a ≈ g/5 dropped from L3-06's check, no physics lost).
- karry-vt-points: least-squares slope through the origin 14,65/7,5 = 1,95 m/s², same as the far-point reading.
- L2-09: frictionless track, only T₁ horizontal, T = m₁a = 0,80 · 1,95 = 1,56 N; the hanging mass rightly not needed; diagram G₁ = N = 7,85 N, T₁ = 1,56 N.
- L3-06: m₂g = (m₁ + m₂)a gives m₁ = m₂(g/a − 1) = 1,21 kg; T = 2,36 N < m₂g = 2,94 N with the right reason (net force on the falling weight points down); diagrams consistent, T₂ shorter than G₂. Reading a = 2,0 m/s² gives 1,17 kg, inside 4 %.
- answers.py `within` checks pass; the other answers are unchanged from the passed set.
- Hash unchanged at start and end.
