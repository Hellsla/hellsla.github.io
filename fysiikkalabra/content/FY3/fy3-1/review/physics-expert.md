VERDICT: PASS
CONTENT-HASH: 1cddd4ad3d506bd2

Round 2 review of fy3-1 after the round-1 fixes. Lint 0/0. Domain hash unchanged from start to end.

## Blocking
(none)

## Polish
1. sim.js:78, 93–94 — The new line "asteikko 0–X N" sits at the top of the y axis (BARS.y), but X = m · 24,8 N is the height of the Jupiter bar, 220 px of the 250 px axis. Read literally, the axis top would be 1,14 · X. No ticks, and the Jupiter label shows X, so no wrong weight is read. — Either end the y axis at BARS.y + 30 (the full-scale height), or draw a short tick there and print the scale line beside it.
2. solutions.md:47 — "Yhden kilogramman paino" mixes mass and weight in a lesson that teaches the difference. The number is right. — "1 kg:n massan paino on noin 10 N", as in the reworded L1-01 line.

## Checked
- lesson.md: G = mg with g in N/kg, the spring proportionality ("kun jousta ei venytetä liikaa"), the calibration, and the g table (1,62 / 3,71 / 9,81 / 24,8) are correct. Everything stays within FY3 scope: no Newton's laws, no vectors.
- lesson.md numbers: 120 · 9,81 = 1177,2 ≈ 1180 N; 120 · 3,71 = 445,2 N; 70 · 9,81 = 686,7 ≈ 690 N; 1,62/9,81 = 0,165 (about a sixth).
- answers.py: every line uses the right formula and conversion, the g dict matches the table, and every answer is within its tolerance (output below).
- Hand recomputation of L2-03, L3-02 and L3-03 (below).
- solutions.md:7, :63 (reworded): 1 kg → about 10 N → 4,0 kg about 40 N is correct. The drop of 1 − 1,62/9,81 = 0,835 is "noin 5/6 eli 83 %", which matches 1187,55/1422,45.
- solutions.md: reasoning correct in all 12 (L3-03 scale measures force; L3-02 fixed force, m = F/g).
- exit-ticket.json: 29 N and 4,9 N; 7,5 cm; 690 N are all correct.
- sim.js: G = m·g exactly. Stretch and arrow are purely proportional on a fixed scale. Bar height / G is equal across bodies at every m. Readout "asteikko … paino Jupiterissa" = m · 24,8 N is correct.
- sim.js:4 comment and sim-spec.md now describe the bars correctly; the 2 px floor is a harmless safeguard (smallest bar 14,4 px).
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
L2-03 by hand: G_Maa=1422.45 G_Kuu=234.90 diff=1187.55 N; frac=0.8349
L3-02 by hand: F=215.82 N; m_Kuu=133.22 kg
L3-03 by hand: G=9.720 N; reading=0.9908 kg
m=1   chartFull=24.8   bars px=[14.37, 32.91, 87.02, 220.0] bar/G=8.871 (all four)
m=10  chartFull=248.0  bars px=[14.37, 32.91, 87.02, 220.0] bar/G=0.8871 (all four)
m=100 chartFull=2480.0 bars px=[14.37, 32.91, 87.02, 220.0] bar/G=0.0887 (all four)
Jupiter bar 220 px of 250 px axis; axis top would be 1.136 x chartFull
stretch/G=0.076613 px/N arrow/G=0.044355 px/N
lesson: 1177.2 445.2 686.7 0.1651  exit: 29.43 4.86 7.5
```
