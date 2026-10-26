VERDICT: PASS
CONTENT-HASH: f47ddab1dae0b8c2

## Blocking

## Polish
- lesson.md:324 — the scene figure says the stretches are drawn to scale and the Moon's is a sixth of the Earth's, but the drawn spring lengths are 144 px and 44 px (ratio 3,3); this holds only with an unshown rest length of 24 px — mark the unloaded spring end on both sides so the 6:1 stretch is visible, or drop "mittakaavassa" (carried from round 1).

## Checked
- Round 2: the only lesson change since cb4b8f4 is inquiry.json:190, conclusion model answer now "esimerkiksi Kuussa 1,62 m/s² ja Jupiterissa 24,8 m/s²"; values match the g table, 10 kg → 16,2 N and 248 N, ×2,53 vs Earth.
- G = mg with g in m/s², force only as a measure of interaction, inside the FY3 scope note.
- g table (1,62; 3,71; 9,81; 24,8 m/s²); 70 kg → 686,7 N ≈ 690 N; worked example 1177,2 N and 445,2 N, symbolic first.
- answers.py unchanged since round 1: all 12 answers matched my own formulas, rounding within tolerance 0,02.
- solutions.md unchanged: unknowns isolated before substitution, sanity checks right.
- Figures unchanged: force–extension 0,40 cm/N to scale; weight–mass slopes match g values; forcemeter labelled schematic.
- Simulation unchanged: G = m·g, stretch, arrow and pointer on one fixed scale; damping comment matches code; model box states assumptions.
- inquiry.json: predictions (×3 at fixed g; mass constant, weight ×2,53 on Jupiter); exp-1 varies m at fixed body, exp-2 varies body at fixed m; simState carries m, g, G.
- Calibration 1,6 cm/N → 3,5 N; siirto 72,7 N; check-2 8,8 m/s²; exit ticket 29 N → 4,9 N, 7,5 cm, 15 N.
