VERDICT: PASS
CONTENT-HASH: 91f2f1a29e235de0

## Blocking

## Polish
- lesson.md:159 — "kuitu viivästyttää signaalia hieman enemmän kuin pelkkä matka antaisi odottaa": the delay is 1,47 times the vacuum time (5,74 ms against 3,91 ms in siirto), so "hieman" understates it — write "noin puolitoista kertaa niin kauan kuin tyhjiössä". Raised before; not blocking.
- inquiry.json:58, 322, 326 — "Kokonaisheijastus vaatii" — use the glossary term "kokonaisheijastuminen" as everywhere else.

## Checked
- Round-2 change: in the graph, "vesi" now sits below-left of the dot at (183,5; 174), and "lasi" sits above-right of the dot at (228,5; 190,5). Each label is next to its own point and clear of the curve. The points are to scale (x = 96 + 265(n − 1), y = 290 − 2,378 α_r): 48,8°, 41,8° and 24,4°.
- One script recomputed every number in lesson-answers.py with my own formulas, and all of them agree: 41,7°, α_r 48,8/41,8/24,4/80,57°, sim α at θ = 0/10/14/15/30° (90/83,26/80,59/79,93/70,25°), α_r for n2 = 1,00…1,46 (42,51/54,18/63,98/71,08/80,57°), the koe-1 limit 14,03° → 14, the koe-2 leak at n2 > 1,393, siirto 5,743 ms with mistakes 3,907/2,658/0,005743, virhe 40,6°, check-2 69,98° with mistakes 20,02° and 0,9396, exit 38,7°, facet 38,0°, half power 15,1 km at 0,2 dB/km.
- With air around the core, α ≥ 47,5° > 42,5° for every θ, so the claim about the bare rod holds.
- Predictions: each has exactly one correct option, and every distractor's feedback is physically right.
- koe-1 and koe-2 each vary one parameter and lock the other. simState gives alpha and alphar.
- sim.js implements sin θ = n1 sin θ1, α = 90° − θ1, sin α_r = n2/n1, and β from n1 sin α = n2 sin β. The model box states that the dimming is not computed and that the end-face reflection is not drawn.
- Worked example: solved symbolically first, 3 sig figs justified, and a real check.
- Definitions, the n1 > n2 condition and the mechanism (total internal reflection, not a mirror) read the same in the theory, summary, checks, exit ticket and glossary. The content stays within FY7.
