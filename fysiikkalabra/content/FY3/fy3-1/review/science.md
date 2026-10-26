VERDICT: PASS
CONTENT-HASH: 5f7710680179315c

## Blocking

## Polish
- lesson.md:324 — the scene figure says the stretches are drawn to scale and the Moon's is a sixth of the Earth's, but the drawn spring lengths are 144 px and 44 px (ratio 3,3); this holds only with an unshown rest length of 24 px — mark the unloaded spring end (a dashed line or tick) on both sides so the 6:1 stretch is visible, or drop "mittakaavassa".

## Checked
- G = mg with g in m/s², 1 N = 1 kg·m/s² deferred to FY4; force only as a measure of interaction, inside the FY3 scope note (no Newton's laws, no vectors).
- g table (1,62; 3,71; 9,81; 24,8 m/s²) and the 1/6 and 0,38 ratios; 70 kg → 686,7 N ≈ 690 N; the bathroom-scale explanation.
- Worked example symbolic first: 1177,2 N ≈ 1,18 kN and 445,2 N, sanity check right.
- answers.py recomputed in one script: all 12 answers match my own formulas; rounding to the data's significant figures stays inside tolerance 0,02.
- solutions.md: every unknown isolated before substitution (L1-02/04 proportionality, L2-03 m(g₁−g₂), L3-03 scale reading L·g_Maa/g_Mars = 68,75 kg), sanity checks numerically right (1420 N, 235 N, 83 %, 2,6×).
- Figures: force–extension line 0,40 cm/N through (2,5; 1,0), (5,0; 2,0), (10; 4,0) and its end point; weight–mass slopes 9,82 / 3,72 / 1,63 / 24,8 m/s² from pixels; forcemeter figure labelled "ei mittakaavassa", x vs 2x brackets consistent.
- Simulation: G = m·g, stretch, arrow and ruler pointer all proportional to G on one fixed 2480 N scale, ruler ticks on the same scale; bars on the current mass's Jupiter scale, stated on canvas and in the readout; damping comment (ω = 10 s⁻¹, ζ = 0,55) matches the code; model box states its assumptions.
- inquiry.json: prediction answers (×3 at fixed g; mass constant, weight ×2,53 on Jupiter) and every feedback number (98,1 / 294 / 196 / 248 N); exp-1 locks body and varies m, exp-2 locks m and varies body, simState carries m, g, G; conclusion model answer calls the values model values.
- Calibration table 1,6 cm/N → 3,5 N, distractor 9,0 N = 5,6·1,6; siirto 72,7 N and its mistakes 19,44 / 117,72 / 7,41; check-2 8,8 m/s² with mistakes 0,114 and 44,9.
- Exit ticket: 29 N → 4,9 N, 7,5 cm, 15 N.
