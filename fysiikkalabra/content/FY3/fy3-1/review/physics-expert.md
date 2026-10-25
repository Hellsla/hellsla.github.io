VERDICT: PASS
CONTENT-HASH: 4190301a25fb39da

Round 4 review of fy3-1. Lint 0/0, check_latex OK (8 fragments), test_sims PASS. The domain hash was the same at the start and at the end.

## Blocking
(none)

## Polish
1. sim.js:93–95 — Still open from round 3: the "asteikko 0–X N" line is centred above the chart (y ≈ 58), but the full-scale tick is at the left of the axis (sim.js:79, y = 90). — Optionally print "X N" next to the tick.

## Checked
- Round-3 polish applied correctly: lesson.md:22 now names mass and size, not mass alone, so the Uranus counter-example no longer applies. exit-ticket.json:11 quotes "vesi painaa", which matches the 1,5 kg of water.
- lesson.md:38: 1,62/9,81 = 0,165 ≈ 0,17 ≈ 1/6 and links back to the opening question correctly. lesson.md:43–50: 1177 ≈ 1180 N, 445 N, 687 ≈ 690 N. The bathroom scale divides by 9,81 m/s², so it reads about 1/6 on the Moon.
- G = mg, with g as putoamiskiihtyvyys in m/s² and 1 N = 1 kg·m/s² deferred to FY4. N/kg appears in no domain file and not in tests/sims/fy3-1.json. The glossary entry is correct: 9,81 m/s², and 1 kg weighs 9,81 N.
- New L1-04 (4,0 N → 2,5 cm, so 6,0 cm → 9,6 N): answers.py:11, exercises.json and solutions.md:25–31 agree, and the 2,4× sanity check is correct.
- Exit ticket 1 now names the Moon–body interaction, which is correct and keeps weight as a measure of interaction, not a cause of motion. Exit ticket 1 gives 29 N → 4,9 N, ticket 2 gives 7,5 cm and ticket 3 gives 14,7 ≈ 15 N.
- answers.py: every line uses the right formula, conversion (60 g → 0,060 kg) and ratio, and its output matches exercises.json within tolerance.
- solutions.md: the reasoning holds in all 12 solutions. The ≈ marks are now on the rounded values only (L2-01, L3-01, L3-02, L3-03), and the exact products (48,6, 1422,45, 5,886) keep "=".
- Hand recomputation of L1-04, L3-01 and L3-02 (output below).
- sim.js is unchanged: G = m·g exactly, and the stretch and the arrow are purely proportional on the fixed 2480 N scale, as sim-spec.md says.

## Python output
```
fy3-1-L1-01 39.24 39 N relerr=0.0061
fy3-1-L1-02 6.0 6.0 cm relerr=0.0000
fy3-1-L1-03 48.6 49 N relerr=0.0082
fy3-1-L1-04 9.6 9.6 N relerr=0.0000
fy3-1-L1-05 62.0 62 N relerr=0.0000
fy3-1-L2-01 4.9949 5.0 kg relerr=0.0010
fy3-1-L2-02 0.5886 0.59 N relerr=0.0024
fy3-1-L2-03 1187.55 1190 N relerr=0.0021
fy3-1-L2-04 5.886 5.9 N relerr=0.0024
fy3-1-L3-01 6.8073 6.8 N relerr=0.0011
fy3-1-L3-02 133.2222 133 kg relerr=0.0017
fy3-1-L3-03 0.9908 0.99 kg relerr=0.0008
L1-04 by hand: k=4.0/2.5=1.60 N/cm; F(6.0 cm)=9.60 N
L3-02 by hand: F=215.82 N; m_Kuu=133.22 kg
L3-01 by hand: m=1.8349 kg; G_Mars=6.807 N
lesson: Kuu/Maa=0.1651; 120*9.81=1177.2; 120*3.71=445.2; 70*9.81=686.7
exit: 29.43 4.86 7.50 14.715
sanity: L2-03 share 0.835; L1-03 Earth 294.3; Jup/Maa 2.528
test_sims: PASS preview/fy3-1
```
