VERDICT: PASS
CONTENT-HASH: dc9814a88f645ab7

## Blocking

## Polish
- lesson.md:159 — "kuitu viivästyttää signaalia hieman enemmän kuin pelkkä matka antaisi odottaa": the delay is 1,47 times the vacuum time (5,74 ms against 3,91 ms in siirto), so "hieman" understates it. Write "noin puolitoista kertaa niin kauan kuin tyhjiössä". This was raised in round 1 and not taken. It is not blocking.
- inquiry.json:58, 322, 326 — the feedback says "Kokonaisheijastus vaatii". Every other place now says "kokonaisheijastuminen" (the glossary term) — change these three to match.
- lesson.md:131 (fibre figure) — the zigzag meets the wall at about 70°, but the label says α > α_r, and α_r is about 80,6° for 1,48/1,46. The caption says the figure is not to scale, so this is a C simplification (taste). A flatter zigzag would match the label.

## Checked
- Round-1 fixes: lesson-answers.py dia-inc1 = 38,0 now matches the figure (facet atan(98,5 : 126) = 38,0°). The water figure is ray-traced: hits at 30,1°, 48,8° and 65,0°, refraction 41,6°, and the arcs lie on the rays.
- One script recomputed every number in lesson-answers.py with my own formulas, and all of them agree: 41,7°, 80,57°, α 83,26/80,59/79,93/70,25°, α_r 42,51/63,98/71,08/80,57°, θ limit 14,03°, koe-2 leak at n2 > 1,393, siirto 5,743 ms and its three mistake values, 40,6°, 69,98° and 20,02°, exit 38,7°.
- Diamond figure: the diamond reflects totally at 38° and at 65,9°, then exits through the crown at about 13°. The glass refracts out at 67,4°, as drawn.
- The graph is to scale: the three points and the curve were checked.
- Predictions: each has exactly one correct option. Every distractor's feedback is right. With air around the core, α ≥ 47,5° > 42,5° for every θ.
- koe-1 and koe-2 each vary one parameter and lock the other. simState gives alpha and alphar. sim.js implements the stated model, and the model box states its limits: brightness is not computed and the end-face reflection is not drawn.
- Worked example: 7 steps, solved symbolically first, 3 sig figs, and a real check.
- Data: 1550 nm; 0,2 dB/km gives half power at 15 km; repeaters every 50–100 km; C-Lion1 1172 km (Cinia, 2016).
- The condition n1 > n2 and the mechanism read the same in the theory, summary, check-1, exit ticket and glossary. The content stays within FY7.
