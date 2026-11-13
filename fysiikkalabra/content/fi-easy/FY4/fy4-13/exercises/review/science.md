VERDICT: PASS
CONTENT-HASH: 61fb5159a4f74408
SCOPE: delta added-exercise from 32606fe51d18f6ad base 81db4a6fd727
## Blocking

## Polish

## Checked
- Round-1 polish fixed: solutions.md:463 L3-06 now answers $m_1 \approx 1{,}2\,\text{kg}$ with the two-figure reason (0,30 kg and the read acceleration), same as fi:463; stored 1.21 with 4 % tolerance accepts 1,2.
- Points from figures.py (0;0), (0,5;1,0), (1,0;2,0), (1,5;2,9), (2,0;3,9): far-point slope 1,95 m/s², origin fit Σtv/Σt² = 14,65/7,5 = 1,95 m/s² (recomputed).
- L2-09: frictionless track, only T₁ horizontal; T = m₁a = 0,80 · 1,95 = 1,56 N → 1,6 N; hanging mass rightly not needed; diagram G₁ = N = 7,85 N.
- L3-06: m₂g = (m₁ + m₂)a, m₁ = 0,30(9,81/1,95 − 1) = 1,21 kg; T = 2,36 N < m₂g = 2,94 N with the right reason (net force on the falling weight points down); diagram values 11,86 N, 2,358 N, 2,943 N consistent, T₂ shorter than G₂; check a = 2,943/1,509 = 1,95 m/s².
- Light inextensible string and light frictionless pulley stated, so equal T and a on both bodies, as in the brief.
- All 23 tasks: answer, unit, tolerance, figure, data and correct options equal the Finnish set; answers.py agrees.
- Hash unchanged at start and end.
