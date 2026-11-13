VERDICT: PASS
CONTENT-HASH: 3c5393f407b00529
SCOPE: delta added-exercise from 734da372eebee885 base 81db4a6fd727

## Blocking
(none)

## Polish
- content/en/FY4/fy4-13/exercises/solutions.md:463 — "1.21 kg, two significant figures" shows three figures; write 1.2 kg (calculated 1.21 kg), which stays inside the 4 % tolerance (the Finnish has the same wording).

## Checked
- fy4-13-L2-09: slope of the karry-vt-points (0,0)–(2.0 s; 3.9 m/s) = 1.95 m/s²; cart alone horizontally, T = m1 a = 0.80 · 1.95 = 1.56 N → 1.6 N; hanging mass correctly not needed; force diagram (G1 = N, only T1 horizontal) agrees with the motion.
- fy4-13-L3-06: m2 g − T = m2 a and T = m1 a give m1 = m2 (g/a − 1) = 0.30 · 4.031 = 1.21 kg; T = 2.36 N < m2 g = 2.94 N, the reason (net force down on the accelerating hanging mass) is right; reading a = 2.0 m/s² gives 1.17 kg, still inside 4 %.
- Both diagrams: separate bodies, T1 = T2 for a light string and light frictionless pulley, no third-law pair on one body, acceleration not drawn as a force.
- answers.py run: every numeric answer equals exercises.json within rounding.
- Script comparison with content/fi for all 23 tasks: every field, correct flag and every number in texts and solutions.md identical.
