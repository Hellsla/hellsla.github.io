VERDICT: PASS
CONTENT-HASH: 569e2236e4eed0be

Physics-expert re-review of fy3-1 after publication: bar chart rescaled to the current mass, answers.py added, proofreader wording applied. Lint: 0 errors, 0 warnings. Domain hash 569e2236e4eed0be at start and at end (unchanged).

## Blocking
(none)

## Polish
1. sim-spec.md:1 — "Siksi jousi venyy ja palkit kasvavat näkyvästi, kun massaa kasvatetaan" is out of date. With full height = m · 24,8 N the bar heights do not depend on m (Kuu 14,4 px, Mars 32,9 px, Maa 87,0 px, Jupiter 220 px for every mass). Only the value labels and the printed scale change. The test note in tests/sims/fy3-1.json already says this. — Human to reword, e.g. "Siksi jousi venyy ja nuoli pitenee näkyvästi, kun massaa kasvatetaan; palkit näyttävät painojen suhteen, ja palkkien lukemat kasvavat massan mukana."
2. sim.js:3 — The comment "spring stretch, weight arrow and bar heights are all proportional to G" holds for the bars only at a fixed mass, across bodies. — Say "bar heights proportional to G at the current mass".
3. sim.js:9, sim-spec.md:1 — The 2 px minimum bar height can no longer take effect (smallest bar 1,62/24,8 · 220 = 14,4 px). This is harmless. — Optionally drop it from the comment and the spec.

## Checked
- lesson.md: G = mg with g in N/kg, the spring proportionality condition, the calibration and the g table (1,62 / 3,71 / 9,81 / 24,8) are correct and stay within FY3 scope (no Newton's laws, no vectors).
- lesson.md:45, 76 (proofreader edits): "Jupiterissa pilvien yläpinnan tasoa" and "lukema muuttuu, kun sama kappale viedään toiseen paikkaan" are both physically correct.
- lesson.md numbers: 120 · 9,81 = 1177,2 ≈ 1180 N; 120 · 3,71 = 445,2 N; 70 · 9,81 = 686,7 ≈ 690 N; 1,62/9,81 = 0,165 (about a sixth).
- answers.py: each line uses the right formula and conversion (60 g = 0,060 kg; m = G/g; same mass gives weight ∝ g; same force gives m = F/g; the scale reading is G/9,81). The g dict matches the lesson table. Every answer is within its tolerance.
- Hand recomputation of three answers: L2-04 0,20 · 9,81 · 3 = 5,886 N; L3-01 (18/9,81) · 3,71 = 6,807 N; L3-03 6,0 · 1,62/9,81 = 0,991 kg.
- solutions.md: the reasoning is correct, including the reworded sanity checks for L2-01 and L2-02 (the weight of 1 kg is about 10 N, the weight of 100 g is about 1 N).
- exit-ticket.json: 29 N and 4,9 N; 7,5 cm; 690 N are all correct.
- sim.js: G = m·g. stretch/G = 0,076613 px/N and arrow/G = 0,044355 px/N on a fixed scale. Bars: bar/G is the same for all four bodies at each m, and chartFull = m · 24,8 N matches the printed scale label.
- scripts/test_sims.py fy3-1: PASS.

## Python output
```
fy3-1-L1-01 39.24 39 N relerr=0.0061
fy3-1-L1-02 6.0 6.0 cm relerr=0.0000
fy3-1-L1-03 48.6 49 N relerr=0.0082
fy3-1-L1-04 1.5 1.5 cm relerr=0.0000
fy3-1-L1-05 62.0 62 N relerr=0.0000
fy3-1-L2-01 4.9949 5.0 kg relerr=0.0010
fy3-1-L2-02 0.5886 0.59 N relerr=0.0024
fy3-1-L2-03 1187.55 1190 N relerr=0.0021
fy3-1-L2-04 5.886 5.9 N relerr=0.0024
fy3-1-L3-01 6.8073 6.8 N relerr=0.0011
fy3-1-L3-02 133.2222 133 kg relerr=0.0017
fy3-1-L3-03 0.9908 0.99 kg relerr=0.0008
L2-04 by hand: G=0.20*9.81=1.9620 N; stretch x3 -> 5.8860 N
L3-01 by hand: m=18/9.81=1.8349 kg; G_Mars=6.8073 N
L3-03 by hand: G=6.0*1.62=9.720 N; reading=0.9908 kg
m=1 chartFull=24.8 N bars px= [14.37, 32.91, 87.02, 220.0] bar/G px/N= [8.871, 8.871, 8.871, 8.871]
m=10 chartFull=248.0 N bars px= [14.37, 32.91, 87.02, 220.0] bar/G px/N= [0.8871, 0.8871, 0.8871, 0.8871]
m=40 chartFull=992.0 N bars px= [14.37, 32.91, 87.02, 220.0] bar/G px/N= [0.2218, 0.2218, 0.2218, 0.2218]
m=100 chartFull=2480.0 N bars px= [14.37, 32.91, 87.02, 220.0] bar/G px/N= [0.0887, 0.0887, 0.0887, 0.0887]
smallest bar (Kuu) = 14.37 px > 2 px floor
stretch/G = 0.076613 px/N, arrow/G = 0.044355 px/N (fixed)
lesson: 120*9.81=1177.2 120*3.71=445.2 70*9.81=686.7 1.62/9.81=0.1651
exit: 3*9.81=29.43 3*1.62=4.86 20/8*3=7.50
```
