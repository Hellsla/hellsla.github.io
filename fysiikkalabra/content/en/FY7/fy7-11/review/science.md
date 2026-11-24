VERDICT: PASS
CONTENT-HASH: 89ecbe627862e284

## Blocking
None.

## Polish
- lesson.md, figure theta-graph aria-label: "red light (n = 1.332)" while the text and the curve use $n = 1.3315$; write 1.3315 for consistency.

## Checked
- Full review (reason: sim.js change). The diff since the last PASS only removes the sim's legend line `selite`; its content ("dashed lines: surface normals and extended incident ray") is in the inquiry `howto`. No physics changed.
- One script recomputed every number from the task data with my own formulas: crown speeds 198 111 / 196 053 km/s; worked example 34.88°, 34.47°, Δ 0.41°; water red 2.25·10⁸ m/s; rainbow max θ 42.30° (α 59.5°) red, 40.63° violet; secondary 50.5° / 53.5°; θ(90°) = 14.7°; Sun 30° → 12°; exit ticket 42° − 50° < 0.
- koe-1 (crown, α₁ = 50°): δ_r/δ_v/Δδ at A = 30…70° = 19.41/19.94/0.53 … 38.44/39.83/1.40 … 54.90/59.35/4.45; prediction feedback and conclusion model answer agree; flint 3.92°, water 0.85°.
- koe-2 (crown, A = 60°): δ_r 40.0° at 40°, min 38.43° at 49°, 50.25° at 80°; the one correct option and both distractor feedbacks right.
- Simulation: ported its vector-Snell geometry to Python; deviations equal δ = α₁ + α₄ − A to 1e-12, sign positive; Cauchy fits reproduce the table (1.5143/1.5302, 1.3315/1.3431); flint 1.6150/1.6499 at 656/405 nm (plausible for F2). Scan of all slider settings: no ray reaches the base; TIR only where n sin α₃ > 1, drawn reflected and stated in the model box. Both experiments' settings keep all colours exiting, so dP, dV, dd in simState are valid.
- Numeric tasks: siirto β 40.573°/40.150°, Δx = 25.40 mm (2 sf answer within 2 %); mistakes 0.0254, 11.23 (sin), 3464 (no refraction) right. tarkistus-2 Δv = 1945.9 km/s, 1.95·10³ km/s; mistake 2000 lies outside tolerance.
- Find-the-error: 60/1.5302 = 39.2°, correct 34.5°, multiply → 91.8°; feedbacks right.
- n-graph points to scale (N-BK7 405–656 nm, 436 and 546 nm values correct); theta-graph peak (59.4°, 42.3°) and end 14.7° to scale.
- Rainbow mechanism, antisolar geometry, observer figure (upper drop red, its violet above the eye; lower drop violet, its red to the ground), drop figure (violet exits at smaller angle), Alexander's dark band, normal dispersion stated for water and glass: correct.
- Prism angle relations derived correctly, condition "ray can leave" stated; exit ticket on parallel pane right; check-1 one correct option, distractor feedbacks right.
