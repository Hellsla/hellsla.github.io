VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

Physics-expert review, fy3-1, round 3 (final). Hash checked at start and at end: 8fb367b0d6fd83e0 both times (unchanged).
No real physics, number, unit or scope errors. Findings below are advisory only and do not block publication.

## Checked and correct (no action)

- lesson.md:6-14 — Force as a measure of interaction, 1 N is about the weight of a 100 g apple (0,1 kg · 9,81 = 0,98 N), weight is the Earth-body interaction strength, mass is the same everywhere. All in FY3 scope (MAOL: weight, spring-balance measurement, G = mg). No Newton's laws, no weight-as-cause-of-acceleration, no vectors. The arrow in the figure is only a drawing of the direction, not vector algebra.
- lesson.md:10 — Spring proportionality: stated with the "not stretched too far" condition and the line through the origin; 5,0 N / 2,0 cm gives 10 N / 4,0 cm and 2,5 N / 1,0 cm, correct.
- lesson.md:12 — Calibration with identical small weights and doubling is correct for a linear spring (stretch proportional to number of weights, so marks 1 N, 2 N, ...).
- lesson.md:17-21 — G = mg with g in N/kg is the right FY3 reading. The softened paragraph is acceptable: it says 9,81 equals FY1's free-fall acceleration in number, that the course uses N/kg, and that the reason for the equality comes in FY4. It does not claim g is an acceleration here and does not deduce a motion law.
- lesson.md:23-28 — g table: Moon 1,62, Mars 3,71, Earth 9,81, Jupiter 24,8 N/kg (1 bar cloud-top level) are standard values. The note that the values refer to the surface (Jupiter: cloud tops) is right.
- lesson.md:45-47 — 120 · 9,81 = 1177,2 N ≈ 1180 N = 1,18 kN; 120 · 3,71 = 445,2 N ≈ 445 N. Correct.
- lesson.md:52 — 70 kg gives 686,7 N ≈ 690 N (2 s.f.). The bathroom-scale remark is correct: a scale graduated in Earth (force / 9,81 N/kg) shows 1,62/9,81 = 0,165, about a sixth, of the mass on the Moon.
- lesson.md:3, 14 — "one sixth on the Moon": 1,62 / 9,81 = 0,165. Correct.
- exercises.json L3-02 (lifting) — the lifting-force assumption is stated in the task text ("tuottaa voiman, joka on yhtä suuri kuin tämän massan paino") and so the task is well-posed without dynamics; this is also FY3-compatible (force compared, nothing accelerated).
- solutions.md — all reasoning is correct (mass fixed, G = mg at each place, proportionality for the spring, sanity checks numerically right: 294 N, 83 %, 0,38, 6,06 ratio, 2,53 ratio). No wrong reasoning found.
- exit-ticket.json — all three answers correct (29 N / 4,9 N, about a sixth; 7,5 cm; 70 kg is about 690 N).
- sim.js:12,42,43,47,48,77 — BODIES g values 1,62 / 3,71 / 9,81 / 24,8 N/kg are correct; G = m · g; stretch, arrow and bars all use the same G / G_FULL with G_FULL = 2480 N. Numerical check of the ratio stretch/G over m = 1..100 and all four bodies: constant 0,076613 px/N (min = max), so stretch is exactly proportional in simState. Arrow and bars use the same pattern. For both mass and body changes the three quantities scale together. Layout at full scale fits (spring tip 270 px, block 76 px, arrow tip 386 px, canvas 400 px).

## Advisory findings (non-blocking)

1. sim.js:68, 77 (drawing) / sim-spec.md — The drawn arrow has a 3 px floor and the drawn bars a 2 px floor, so the drawing is strictly proportional to G only for G >= 67,6 N (arrow) and G >= 22,5 N (bars). Below that the shapes do not change with G. At the default 10 kg, Moon (16,2 N) and Mars (37,1 N) show arrow 3 px and 3 px (true 0,7 and 1,7 px), and Moon/Mars bars 2 px and 3,3 px; the spring stretch is only 1,2 px vs 2,8 px. The text readout stays exact, and simState.stretch/arrow/bars hold the pure values, and the floors are documented in sim-spec.md and the code comment, so this is not a physics error. Optional fix: raise the default mass (for example to 50 kg: Moon 81 N, Mars 186 N, Earth 491 N, all above both floors) so the first view shows proportional arrow and bars, or add a one-line hint in the sim note to try large masses.
2. lesson.md:12 — Calibration uses weights "noin 1 N" to define the 1 N mark, which is mildly circular (the unit is being defined by something already measured in it). Acceptable at this level because only proportionality is used to mark 2 N, 3 N ...; optional rewording: "samanlaisia kappaleita; yhden kappaleen aiheuttama venymä merkitään yhdeksi yksiköksi (noin 1 N, jos kappaleen massa on noin 100 g)". Not required.
3. exercises.json:38, 22-24 vs lesson.md:21 — grammar only (Jupiterissa / Jupiterilla, "Jupiterissa, missä g ="); belongs to the proofreader, no physics impact.

## Python output (python3 -I, from the problem texts alone; g = 9,81 unless the task gives g or says read it from the table)

```
fy3-1-L1-01 computed=39.24 answer 39 N relerr=0.0061 OK
fy3-1-L1-02 computed=6 answer 6.0 cm relerr=0.0000 OK
fy3-1-L1-03 computed=48.6 answer 49 N relerr=0.0082 OK
fy3-1-L1-04 computed=1.5 answer 1.5 cm relerr=0.0000 OK
fy3-1-L1-05 computed=62 answer 62 N relerr=0.0000 OK
fy3-1-L2-01 computed=4.9949 answer 5.0 kg relerr=0.0010 OK
fy3-1-L2-02 computed=0.5886 answer 0.59 N relerr=0.0024 OK
fy3-1-L2-03 computed=1187.6 answer 1190 N relerr=0.0021 OK
fy3-1-L2-04 computed=5.886 answer 5.9 N relerr=0.0024 OK
fy3-1-L3-01 computed=6.8073 answer 6.8 N relerr=0.0011 OK
fy3-1-L3-02 computed=133.22 answer 133 kg relerr=0.0017 OK
fy3-1-L3-03 computed=0.99083 answer 0.99 kg relerr=0.0008 OK
exit: 3*g=29.4 3*1.62=4.86 ratio=0.165 ; 20/8*3 = 7.5 ; 70*g = 686.7
lesson: 120g=1177.2 120*3.71=445.2 70g=686.7 ; 1.62/9.81=0.1651 ; 0.1 kg apple = 0.981 N
sim (stretch px, arrow px, bar px; pure values):
Maa 10 kg: G=98.10 stretch=7.52 arrow=4.35 bar=8.70
Maa 100 kg: G=981.00 stretch=75.16 arrow=43.51 bar=87.02
Jupiter 100 kg: G=2480.00 stretch=190.00 arrow=110.00 bar=220.00
Kuu 10 kg: G=16.20 stretch=1.24 arrow=0.72 (drawn 3.00) bar=1.44 (drawn 2.00)
arrow floor G< 67.6  bar floor G< 22.5  1px stretch at G=13.05
stretch/G over m=1..100, 4 bodies: min=max=0.0766129 px/N
```

All 12 answers are within the stated tolerance (0,02) of the recomputed values, and every answer is rounded to the data's significant figures; a student using g = 9,8 stays within tolerance on all g-dependent tasks (L1-01 39,2; L2-03 1186; L3-01 6,8).

Hash at end of review: 8fb367b0d6fd83e0 (unchanged).
