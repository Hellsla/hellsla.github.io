VERDICT: FAIL
CONTENT-HASH: 0441b780ef94694f

## Blocking
- [Blocker] The simulation canvas has Finnish left: the potential graph's horizontal axis label reads "kohta" in sim-390, sim-1280 and every experiment capture. It is hard-coded in assets/sims/fy6/fy6-5/sim.js line 201 (`lab('$\\text{kohta}$', 598, ...)`), not read from lang/en.json. Not fixed here (assets/ is off limits). Needs a `__('...')` key (e.g. sims.fy6-5.akseli = "point") in sim.js and in lang/fi.json, en.json, fi-easy.json, then recapture.

## Polish
(none) Figures 1–6, the table headings, the select values ("point A", "source's negative terminal") and the experiment tables are English.

## Checked
- Contact sheets 1–3 (all 36 first captures), sim-1280, exp-koe-1-390-1: no overflow, maths renders, figures fit at 390 px, fig-6 axis says "point".
- Sim legend "Blue: potential, darker is higher. Purple: current. Black lead at the zero point." is 14 words (limit 15).
- No Finnish in headings, figures or experiment tables; only the sim canvas "kohta" above.
