VERDICT: PASS
CONTENT-HASH: 34d62791171a8af6

## Blocking

## Polish
- inquiry.json:342 (data, solution) — the closing equation reads $x = 4\,\text{m} + 1{,}5\,\text{m/s} \cdot t$ while the figure and the substitution use 4,1 m; writing 4,1 m would match exactly (the "noin" keeps it correct as is).
- assets/sims/fy4/fy4-1/sim.js:52 — playback-pace select still labelled "Nopeus (toisto)" in a velocity lesson; "Toiston tahti" cannot be taken for the carts' velocity.
- lesson.md:58 — round-trip figure says "ei mittakaavassa" although its km axis is to scale; harmless.

## Checked
- Round-2 blockers fixed: hint 1 (inquiry.json:324) now says the line does not pass through all points, which is true (it meets 19,1 m at 10 s but misses e.g. 4,2 m at 0 s); the solution reads (10 s; 19,1 m), on the drawn line x = 4,1 m + 1,5 m/s · t, and gives v = (19,1 m − 4,1 m)/10 s = 1,5 m/s exactly, inside the 0,03 tolerance.
- Hints 2–3 (line ends near 19 m, Δx ≈ 15 m) and the mistake feedback (19,1 m/10 s; Δx = 19,1 m − 4,2 m) stay consistent with the figure and data.
- git diff since round 2: only those two strings in inquiry.json changed; inquiry.json parses. Everything else carried forward from round 2: all 12 exercise answers and every inquiry number recomputed and matching; least squares 1,494 m/s, 4,10 m; mistake values 1,9, 1,3, 0,67 reproduce their errors.
- SVG scales (displacement, round trip, slope triangle, jogger, robot points and line, E's path), formulas, conditions, scope, vector notation, symbolic-first solutions, realistic magnitudes — unchanged since round 2.
- Sim: x = x₀ + vt and the case-4 piecewise motion match every cited model value; limits stated; experiments lock tapaus, vary t, keys xA/x2 exist.
- Hash identical at start and end.
