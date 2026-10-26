VERDICT: PASS
CONTENT-HASH: af964d5101852359

## Blocking

## Polish
- inquiry.json:data question — asks the student to read a point "sovitetulta suoralta … kuvaajasta", but the figure draws only the points, not the fitted line (the text says it is "piirretty ajatuksissa"). The numbers still work (reading x ≈ 19 m at 10 s gives 1,49–1,50 m/s, inside the tolerance), but drawing the least-squares line x = 4,1 m + 1,49 m/s · t in the SVG would make the instruction literal — draw it, or say "valitse ajatuksissa sovitetulta suoralta".
- assets/sims/fy4/fy4-1/sim.js:1191 — the playback-pace select is labelled "Nopeus (toisto)" in a lesson about velocity; a student could take it for the carts' velocity — rename it "Toistonopeus" or "Toiston tahti".
- lesson.md:151 — round-trip figure says "ei mittakaavassa" although its km axis (0, 1, 2 km) is drawn to scale, harmless.

## Checked
- Recomputed all 12 exercise and 5 inquiry numeric answers in one script: all match exercises.json, inquiry.json and answers.py. The least-squares fit of the robot data gives slope 1,494 m/s, intercept 4,10 m, x(10 s) = 19,04 m, which matches the text's (0 s; 4,1 m) and (10 s; 19,0 m). Every listed mistake value reproduces the error it names.
- Formulas: v_ka = Δx/Δt, x = x₀ + vt (t from 0), with their conditions stated. They are inside "tasainen suoraviivainen liike". Vectors are bold (\mathbf{v}, Δ\mathbf{x}) and components carry the sign.
- SVG numbers checked against pixel scales: displacement (+6 m, −5 m, 40 px/m), jogger graph (to scale: 20/120/170 m at 0/40/60 s), robot data points (11,1 px/m), E's path (8 m, 4–6 s plateau).
- Worked example and all 12 solutions: unknown solved symbolically before substitution. Units, signs and magnitudes are realistic.
- Sim: x = x₀ + vt for cases 1–3 and piecewise for case 4 (path 16 m, Δx = 0). The model values in the predictions and feedback match (A 20 m, B 40 m, C +20 m, D −3 m/s, meeting at 6 s, 12 m). The limits (instant full speed, no friction) are stated.
- Experiments: tapaus locked, t varied, measured keys xA/x2 present in simState. The 0,5 s slider step reaches every suggested time.
- Every correct choice and every feedback checked: pr-nopeus, pred-1–3, exp-2, edestakainen (mean velocity 0, mean speed 1,6 m/s), virhe, check-1, exit ticket.
- Hash identical at start and end.
