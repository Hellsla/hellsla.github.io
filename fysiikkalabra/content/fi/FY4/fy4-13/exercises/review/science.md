VERDICT: PASS
CONTENT-HASH: 654329c358771fa4
SCOPE: delta added-exercise from 6f0e928ad88d259e base 81db4a6fd727

## Blocking

## Polish
- content/fi/FY4/fy4-13/exercises/solutions.md (L3-06 Vastaus a) — the line says "$m_1 \approx 1{,}21\,\text{kg}$, kaksi merkitsevää numeroa", but 1,21 has three figures. Write $1{,}2\,\text{kg}$ (calculated 1,21 kg). The tolerance of 4 % accepts both.
- solutions.md L2-09 and L3-06 Kuvaajan lukeminen — the slope is still taken from the raw point (2,0; 3,9) and the origin. Say that the point is read off a line drawn through the origin and the points. Carried over from round 1.

## Checked
- The round-1 blocking finding is fixed. L3-06 now has a hanging mass of 0,30 kg and a cart of 1,21 kg, so L2-09 (cart 0,80 kg) no longer gives away L3-06's answer, and L3-06 b's tension (2,36 N) is not L2-09's answer (1,56 N).
- One figure fits both setups: m₂/(m₁ + m₂) = 0,30/1,51 ≈ 0,199 g, and 0,80 kg needs m₂ ≈ 0,20 kg for the same ratio. Both give a ≈ 1,95 m/s², as the figure shows.
- Recomputed L3-06: m₁ = m₂(g/a − 1) = 0,30 kg · (9,81/1,95 − 1) = 1,209 kg. Reading a between 1,9 and 2,0 m/s² gives 1,17 to 1,25 kg, inside ±4 %. b) T = 2,36 N < m₂g = 2,94 N, and the reasoning (the hanging mass accelerates down, so m₂g − T = m₂a > 0) is right.
- The force-diagram numbers have been updated: G₁ = N = 11,86 N, T₁ = T₂ = 2,358 N, G₂ = 2,943 N. T₂ is drawn shorter than G₂, and a points down for the hanging mass. They agree with the motion.
- L2-09 unchanged: T = m₁a = 0,80 kg · 1,95 m/s² = 1,56 N, answer 1,6 N.
- I recomputed both answers in one script, beside python -I answers.py. They agree with exercises.json (1.6 and 1.21).
- Hash 654329c358771fa4 at the start and at the end.
