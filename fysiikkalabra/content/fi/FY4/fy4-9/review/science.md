VERDICT: PASS
CONTENT-HASH: 25b95920e4cf479d

## Blocking

## Polish
- lesson.md:490 vs :551 — F_ka is defined as |Δp|/Δt, a magnitude, but the example's F_ka = m(v − v0)/Δt is signed ("Voima on positiivinen"). This was carried over from round 2. — Say once that the force's direction comes from the sign of Δp.
- sim-spec.md — "F = kc" is a magnitude, while model.js, sim.js and the sim's calc box use F_x = −kc. This was carried over from round 2. — Write F_x = −kc, or "suuruus kc, vasemmalle".
- review/shots/fy4-9-fig-3-390.png (23:41) — the screenshot is older than the lesson (00:02). It still shows the old positive F graph with its axis at the bottom. — Re-take the shots so the next reviewer sees the current figure.

## Checked
- Round-2 blocking item fixed. lesson.md:387 and the check-3 model now say "Alustan voima on (tätä) kokonaisvoimaa painon verran suurempi, mutta sekin pienenee, kun pysähtymisaika pitenee". en and fi-easy say the same; fi-easy splits it into two sentences. This is right: N = |Δp|/Δt + G, with G/N ≈ 2 % on hard ground and ≈ 26 % on the mat (70 kg, Δt ≈ 0,015 s and 0,25 s). Nothing that says "suurin osa" or "most of" is left.
- pysaytys figure (fi/en/fi-easy, same geometry). I parsed the polylines. The time axis is at F_x = 0 at the top (y = 72), and the F_x axis runs from 0 to −100 N. Hard: peak −80,0 N, end 0,0394 s, area −2,009 N·s. Soft: peak −20,0 N, end 0,157 s, area −1,998 N·s. Both agree with the aria-label's −2,0 N·s.
- Sim graph (Playwright, soft spring bumper, 1,0 kg, 2,0 m/s). The axis label reads F_x (N) and the axis is at 0 at the top. The curve lies below the axis and its shaded area is shown as I = −4,00 N·s. The readout gives Δt = 0,3142 s, F_max = 20,0 N, v = −2,00 m/s and Δp = −4,00 kg·m/s, all matching analytic SHM. Nothing is cut off.
- Arrows: blue v and purple p both point left after the bounce. Red F is drawn only while F_x < 0, so it disappears after the crushable stop.
- Bumper models (no rebound when crushed, ideal spring) agree across model.js, the sim boxes, sim-spec and lesson-answers.
- `node tests/models/fy4-9.test.js`: 616 checks pass.
- Signs are the same throughout: the sim and model boxes, pred-1/2, exp-1/2 options and feedback, virhe, the Kaava rebound (Δp = −2mv, magnitude 2mv), the summary and the exit ticket.
- I recomputed every number with my own formulas (π/2·√(m/k), v√(mk), −mv, 870 N, 145 N, 80 N, 12 m/s, 1,5 m/s, −4,0, 113 N). All match lesson-answers.py.
- Exactly one option is correct in each item. Each experiment varies only its own parameter, and simState gives every measured key.
- The content hash was the same at the start and at the end.
