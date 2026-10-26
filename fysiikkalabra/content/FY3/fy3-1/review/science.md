VERDICT: PASS
CONTENT-HASH: 590742e6e82795d0

## Blocking

## Polish
- sim.js:1053 — the drawn settling oscillation has the same ω = 10 1/s for every mass and body (a real spring-mass system would oscillate more slowly with a larger m); harmless since it is drawing only and simState holds the rest values — optionally say "animaatio" in sim-spec.md or leave as is.
- lesson.md:182 — tick 2,5 N sits at 87,5 px while the scale is 35,1 px/N (0,25 px off); invisible, no fix needed unless figures.py is touched anyway.

## Checked
- Full review, hash 590742e6e82795d0 at start and end.
- answers.py and all 12 exercise answers recomputed independently with my own formulas: all match (39,24; 6,0; 48,6; 9,6; 62; 4,995; 0,5886; 1187,55; 5,886; 6,807; 133,2; 68,75 → rounded answers right).
- solutions.md (new LaTeX): every unknown solved symbolically before substitution; units carried; sanity checks numerically right (1420 N / 235 N, 83 %, 0,38, 2,6-fold).
- Worked example: 1177,2 N ≈ 1,18 kN, 445,2 N, ratio 0,38; symbolic first.
- lesson.md prose: 70 kg ≈ 690 N, 1,62/9,81 ≈ 0,17, table g values, bathroom-scale reasoning, 1 N = 1 kg·m/s² deferred to FY4; Newton's laws and motion stay out (scope respected).
- Figure "forcemeter": extensions 50 px vs 100 px (x, 2x) and arrows 36 px vs 72 px (G, 2G); labelled not to scale.
- Figure "force-extension" (to scale): x ticks 35 px/N, y 44 px/cm; points (2,5; 1,0), (5,0; 2,0), (10; 4,0) on the line through the origin.
- Figure "weight-mass" (to scale): at 100 kg Maa 981 N, Mars 371 N, Kuu 162 N at the drawn end points; Jupiter line leaves the frame at 44 kg ≈ 1100 N, consistent with 24,8 m/s².
- inquiry.json: every correct option and feedback number recomputed (6,0 km; 98,1/294/196 N; 248 N, 2,53×; 3,5 N and 8,96; 4,905 N; 72,7 N and mistakes 19,44/117,72/7,41; 8,8, 0,114, 44,9); exp-1 locks body and varies m, exp-2 locks m and varies body; simState gives m, g, G; screenshot of exp-2 reads 98,1 N at Maa, 248 N at Jupiter.
- sim.js: G = m g, stretch and arrow purely proportional to G on one fixed 2480 N scale, ruler in kN on the same scale, bars scaled to m·24,8; model limits stated; exit ticket 29 N / 4,9 N, 7,5 cm, 15 N right.
