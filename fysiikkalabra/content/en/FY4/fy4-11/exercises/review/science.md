VERDICT: PASS
CONTENT-HASH: dd6ef145574391a4
SCOPE: delta added-exercise from 696dd89d4770c31a base 81db4a6fd727

## Blocking
(none)

## Polish
- lessons/FY4/fy4-11/figures.py:233 — in ex-tv-tyyny the stop of test B at 0.150 s falls between the 0.14 s and 0.16 s grid lines, though the catalogue note says "readable at grid crossings"; reading halfway still keeps 10.5 kN inside 5 %, so not blocking — put the stop on a grid line or correct the note (fi equally).

## Checked
- fy4-11-L1-09 (MAFY rubber–asphalt, sliding 0.5–0.8, upper end used as the text says): level road, N = mg, a = mu g = 7.85 m/s², s = v0²/(2 mu g) = 22.22²/15.70 = 31.5 m; the one-figure 30 m stays inside the 5 % tolerance; the mu = 0.5 comparison (50 m) is right.
- fy4-11-L2-09: area under (t, v) of ex-tv-jarrutus: 20 m/s · 1.0 s + ½ · 20 m/s · 2.5 s = 45 m; slope 8.0 m/s² fits a dry road.
- fy4-11-L3-06: impulse principle F_avg Δt = m Δv, 70 · 15 / 0.060 = 17.5 kN, 70 · 15 / 0.150 = 7.0 kN, difference 10.5 kN; 11 kN inside the tolerance; linear v(t) gives a constant force, as stated.
- answers.py run: every numeric answer equals exercises.json.
- Script comparison with content/fi for all 24 tasks: every field, correct flag and every number in texts and solutions.md identical.
