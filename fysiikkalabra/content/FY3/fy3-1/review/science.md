VERDICT: PASS
CONTENT-HASH: 904c78c89b385b5a

## Blocking

## Polish
- sim.js:1020 — the drawn settling oscillation has the same ω = 10 1/s for every mass and body (a real spring–mass system oscillates more slowly with a larger m); drawing only, simState holds the rest values — optionally say "animaatio" in sim-spec.md, or leave as is.

## Checked
- Full review; hash 904c78c89b385b5a at start and end. Diff since round 1 (0bbacb9..HEAD): exercises.json, exit-ticket.json, inquiry.json (interpret table header, check-2 prompt) and sim.js ruler only — every number, unit and formula is identical before and after the conversion to inline maths (24,8; 1,62; 9,81; 3,71; 2,5 · 3,0 cm = 7,5 cm; 1,5 kg · 9,81 m/s² ≈ 15 N; (50 kg, 440 N)).
- answers.py and all 12 exercise answers recomputed with my own formulas: 39,24; 6,0; 48,6; 9,6; 62; 4,995; 0,5886; 1187,55; 5,886; 6,807; 133,2; 68,75 — all match, rounded answers within tolerance.
- solutions.md and worked example: unknown solved symbolically before substitution; 1177,2 N / 445,2 N, ratio 0,38; sanity checks right.
- lesson.md: 70 kg ≈ 690 N, 1,62/9,81 ≈ 0,17, g table, bathroom-scale reasoning; scope stays at G = mg (no Newton's laws).
- Figures: forcemeter x/2x and G/2G; force-extension to scale (35 px/N, 44 px/cm, points on line through origin, 2,5 N tick now exact); weight-mass end points 981/371/162 N at 100 kg, Jupiter consistent with 24,8 m/s².
- inquiry.json: 6,0 km; 98,1/294 N, +196 N; 248 N; 3,5 N (wrong 8,96); 4,905 N; 72,7 N with mistakes 19,44/117,72/7,41; 8,8 m/s² with mistakes 0,114/44,9 — all recomputed. exp-1 locks body, varies m; exp-2 locks m, varies body; simState gives m, g, G.
- sim.js newton ruler: ticks at y0 + 190·F/2480 on the same fixed scale as the spring stretch, labels 0–2500 N every 500 N, unit "N"; screenshot at 10 kg on Maa: pointer ≈ 7,5 px below 0, matching 98,1 N. Bars and readout unchanged.
- Exit ticket: 29 N / 4,9 N, 7,5 cm, 15 N right.
