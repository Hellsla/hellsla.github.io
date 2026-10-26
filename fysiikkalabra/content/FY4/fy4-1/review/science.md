VERDICT: FAIL
CONTENT-HASH: cfc3c56d3cf0b6d3

## Blocking
- lesson.md:159 — The worked example's plausibility check says "2,5 m/s ≈ 9 km/h on reipas kävelyvauhti". 9 km/h is jogging; a brisk walk is about 1,5–2 m/s (5–7 km/h). This teaches students the wrong sense of size. — Make the walker a jogger ("hölkkääjä", in the question text too), or keep the walker and change the data, e.g. x₂ = 80 m → v = 1,5 m/s, x(60 s) = 110 m. Changing the data means updating the SVG, the stages and answers.py.
- solutions.md:7 — "Noin 29 km/h on hyvä kestojuoksuvauhti" is wrong: 8,0 m/s is a sprint pace. The marathon world record is about 21 km/h. — Say "pikajuoksuvauhti; 120 m:n matkalla mahdollinen".
- solutions.md:23 — "Vauhti vastaa reipasta kävelyä": 3,5 m/s = 12,6 km/h, which is a run, not a walk. — Say "vastaa hölkkää (noin 13 km/h)".
- solutions.md:63 — "kärry liikkuu kohti origoa ja sen yli" is false. The cart goes from 18 m to 3,0 m and stays on the positive side, so it never passes the origin. — Remove "ja sen yli".

## Polish
- inquiry.json:87 — typo "riippu" → "riipu".
- exit-ticket.json:7 — "Kahden kärryn" but three lines are described → "Kolmen kärryn …".

## Checked
- One script recomputed all 12 exercises and 12 inquiry numbers (fit slope 1,494 m/s, intercept 4,10 m; mistake values 1,91, 1,3, 0,67, 50, 74, 25, 37): all match answers.py and exercises.json.
- Formulas v_ka = Δx/Δt and x = x₀ + vt with their condition; signs, bold vectors; within FY4 scope.
- Worked example and all solutions are symbolic first; reasoning correct (L3-01 speed vs velocity, L3-02 meeting at 33,3 s, 50 m).
- Predictions 1–3: correct options and feedback numbers match the model (A and D meet at 6 s, 12 m).
- Experiments lock the case and vary t; simState gives xA and x2 within the drawn range.
- SVG figures are to scale (siirtymät, example graph, robot data, round trip).
- sim.js pos/vel/path are correct for all four cases; the model's limits are stated.
