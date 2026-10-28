VERDICT: PASS
CONTENT-HASH: 1ed699cbb90173d7

## Blocking

## Polish

## Checked
- Unit-as-LaTeX commit 212c48d in exercises.json (11 lines) and solutions.md (3 lines): the numbers and number–unit pairs of every changed hunk are identical before and after (script, normalising `{,}`, `\,`, Unicode minus); e.g. −5,0 m, −24 m, −1,2 m/s keep their signs, 0–10 s / 10–20 s / 20–40 s keep their ranges. No value changed.
- All 12 answers recomputed with my own formulas: 8,0; −17; 42; 2,0; 45; 300; 5,0 min; −3,0; 16 s; 4,0 (mean speed, 12 000 m / 3000 s); 50 m (t = 33,3 s); 0,25 m/s — equal to answers.py and exercises.json, tolerances 2 %.
- L2-01: "Kysytty" now names the displacement and says the path s = vΔt is equal for one-way straight motion (round-2 polish addressed).
- L3-01 distinguishes keskivauhti from keskinopeus (0) correctly; leg speeds 5,0 and 3,3 m/s bracket 4,0.
- L3-03: segment velocities 3,0 / 0 / −1,0 m/s; their unweighted mean 0,67 correctly shown as wrong.
- Every solution symbolic first, conversions right (90 km/h = 25 m/s, 1,2 km = 1200 m, 20 min = 1200 s), rounding justified by the limiting datum, reasonableness checks real.
- Hash identical at start and end.
