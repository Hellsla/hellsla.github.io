VERDICT: PASS
CONTENT-HASH: 47e70a6d03eb853b

## Blocking

## Polish
- inquiry.json:60 — pred-1 feedback counts the rope's vertical component among "kolme voimaa" (step 7). — "kaksi voimaa ja narun voiman pystykomponentti".
- inquiry.json:504, 508 — check-3: `fbd_representation` says the handle force goes "kahvan kiinnityskohdasta" (the model correctly ends it there), and `fbd_magnitudes` asks for dashed components that `malli-tyonto` does not draw. — Write "alkaa tai päättyy kiinnityskohtaan", and add dashed F_x or drop the clause.
- lesson.md:60 — step 3 says every arrow "lähtee" from its point of application. The ceiling's N in `suunnat` ends there, which only line 278 allows. — Add the push exception to step 3.
- sim.js:139 (edited during review) — push mode is now fine, but in pull mode with components on, F_y's label lands on N's arrowhead (rendered at 30°). — Put the label on the left only for a push. tests/sims/fy4-5.json lost the on-load defaults assertion. — Keep it without the `malli` clause.
- review/shots predate 2d2daf3b (captions say "pisteenä"), and site/sims still holds the old point-model sim. — Regenerate and rebuild.

## Checked
- All PNGs follow the four rules: rectangle body, red F, blue v, orange a, friction from a contact corner, pictorial situation pictures. No text, label or sim string mentions a point model.
- Arrow lengths: tilanne N + T_y = G. rinne (25°): N = G cos α, F_μ = G sin α, and N ⊥ slope. lamppu: T = G. Balloon: N points down and ends on the top surface, and F_noste = G + N.
- esimerkki is to scale (G, N 71,8 N, T 80 N at 35°, F_μ 30 N, components). a = 2,96 m/s², recomputed.
- Lift options: a has N > G (correct), b has N = G, c has a red v drawn as a force, and d has N < G. Each distractor has exactly one error, and its feedback names it.
- virhe: F is the only error. malli-tyonto: N 147,7 N, F_μ = F_x = 52 N, and the push ends at the back corner.
- Sim (rendered from assets): the sled is a rectangle, G is at the centre, N is on the bottom face, a pull starts at the front corner and a push ends at the back corner. N = 146,2 N (pull, 30°) and 260,5 N (push, 40°).
- I recomputed all inquiry numbers and mistake values in one script, and they agree.
