VERDICT: FAIL
CONTENT-HASH: 1d2219da8a5ea8a9

## Blocking
- exercises.json fy5-14-L3-05 (whole task, solutions.md fy5-14-L3-05) — near-duplicate of fy5-11-L2-05 (speed of sound from (distance, time) data with a constant device delay t0, slope from two far-apart rows, answer 343 m/s) and overlaps fy5-10-L2-07 (two-point slope of d vs Δt). The extra parts (draw the line, estimate the delay 0,42 ms) do not make it a new idea, and it is a level 2 task, not level 3. Fix: replace it with a different level-3 data/model task of this chapter, e.g. a table of the speed of sound in air at 0, 10, 20, 30 °C (331, 337, 343, 349 m/s) -> fit v = v0 + kT, predict v at -15 °C and the beat/pitch consequence for a pipe, or a spectrum + beats task; with its full solution.

## Polish
- fy5-14-L2-05 repeats the idea of old L2-04 (racing car away, 23 m/s) and L3-01 (ambulance 28 m/s); only the averaging is new. Consider a before/after-passing table (approach and recede) so it differs.
- fy5-14-L3-05 (if the idea is kept in any form) solution picks two data points as "points on the line"; points for the slope should be read from the fitted line.
- fy5-14-L2-05 Järkevyys — "vastaa kohtuullisesti" (35 Hz vs 38,5 Hz) is a weak sanity check; use the exact ratio 392/(1−30,4/340) = 430,5 Hz instead.

## Checked
- L1-06..08, L2-05..07, L3-04 recomputed: beat period 0,167 s; v_s = 30,4 m/s; f_1 = 262 Hz with harmonics 524..1309; 544 Hz vs correct 548,4 Hz (error direction "too small" is right); blood speed 0,475 m/s via f0(v+vv)/(v-vv), double Doppler explained correctly. All answers match solutions.
- Levels fit (L1 concept/one-step, L2 data/error, L3 modelling); stay within the chapter (Doppler, beats, FFT, harmonic series); no duplicate in fy5-1..13 except the item above; "graph" kind only in L3-05, which asks to draw.
- Solutions step by step; $\begin{aligned}$ blocks render correctly at 1280 px; 360 px check ok; Finnish correct.
