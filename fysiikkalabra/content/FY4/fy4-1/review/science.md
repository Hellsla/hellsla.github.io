VERDICT: PASS
CONTENT-HASH: f0c05b8f4255e26f

## Blocking

## Polish
- solutions.md:99 — "kärry on 24 m origon vasemmalla puolella" assumes that +x points right, which the task does not say. — Say "negatiivisella puolella".
- solutions.md:110 — the symbol "v_vauhti" for mean speed is an invented notation. — Write "keskivauhti = s / Δt" without a new symbol.
- inquiry.json (exp-1, exp-3) — the tolerance of 0.02 is relative to the answer. Students who read whole-metre positions off the slider at 0,5 s steps still get exactly 4,0 or −3,0, so this is fine; mentioned only as a check.
- sim.js:1141 — the playback-pace control is called "Nopeus (toisto)" in a lesson whose subject is velocity (nopeus). A student could confuse the two. — Consider "Toistotahti".

## Checked
- All 4 round-1 blockers are fixed: the example's walker is now a jogger (2,5 m/s ≈ 9 km/h), L1-01 is called a sprint pace, L1-03 is a jog of about 13 km/h, and L2-03 no longer claims the cart passes the origin. Both round-1 polish items are fixed too.
- One script recomputed all 12 exercises and the inquiry numbers independently: the least-squares fit gives slope 1,494 m/s and intercept 4,10 m, so x(10 s) = 19,0 m; v_B = 4,0 m/s; v_D = −3,0 m/s; the sledge task gives 39 m; check-2 gives 13 m; the example gives 2,5 m/s and 170 m. All match answers.py and exercises.json.
- The mistake values match their stated errors: 3000, 0,13, 130, 1,91, 1,3, 0,67, 50, 74, 5,0, 25, 37, 3,0, 30 and 40.
- The formulas v_ka = Δx/Δt and x = x₀ + vt are given with their condition (uniform motion). Signs and vector notation are consistent, and the content is within FY4 scope.
- The worked example and every solution solve symbolically before substituting. The reasoning is correct, including speed versus velocity in L3-01 and the meeting at 33,3 s and 50 m in L3-02.
- Predictions 1–3 have the right correct options, and their feedback numbers match the model (A and D meet at 6 s at 12 m). The round-trip case gives v_ka = 0 and a path of 16 m.
- Each experiment locks the case and varies t. simState exposes xA and x2, which stay within the drawn range (≤ 40 m). The exp-3 capture shows case 3 at t = 0 with x_D = 30 m.
- All 5 SVG figures are to scale: the two displacements, the slope triangle, the example graph, the robot data points (10 px/m) and the round trip.
- sim.js pos, vel and path are correct for all four cases, and case 4 is continuous at 4 s and 6 s. The model's limits (instant full speed, no friction) are stated in the sim intro and under "Lisätietoja".
- Magnitudes are realistic throughout: 8 m/s sprint, 25 m/s car, 5 m/s sledge, walkers at 1,2–1,5 m/s.
