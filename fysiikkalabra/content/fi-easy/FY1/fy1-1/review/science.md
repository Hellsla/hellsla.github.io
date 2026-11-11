VERDICT: PASS
CONTENT-HASH: eee3497ff21144ab

## Blocking

## Polish
- lesson.md:272 — the aria-label of the object-types figure says "Jokainen askel akselilla on kymmenkertainen koko", but the ticks are two powers of ten apart (labels $10^{4}$, $10^{8}$, … every four), so one tick interval is a 100-fold step — say "jokainen kymmenpotenssi on kymmenkertainen koko" or name the 2-decade tick spacing.
- inquiry.json:115 (`howto`) — "Lähennä/Loitonna muuttavat näkymän leveyden kymmenesosaksi tai kymmenkertaiseksi": in the code (`goTo(ceil(L)-1)`, `goTo(floor(L)+1)`) the buttons go to the next whole power of ten, so from $10^{-9{,}4}\,\text{m}$ the view goes to $10^{-10}\,\text{m}$, not $10^{-10{,}4}\,\text{m}$. Say "siirtää näkymän seuraavaan kymmenpotenssiin".
- sim-spec.md — it gives the visibility range as "1/2000 – 3", while the `calc` box gives "1/1000–3". The code reaches 50 % opacity at $d/W \approx 1/1200$, so `calc` is right. Align the spec.

## Checked
- Delta (round 2): lang/fi-easy.json:1078 `sims.fy1-1.o_proxima` "Proxima Centauri" → "etäisyys Proxima Centauriin". The new label is correct. The OBJ value $4{,}0\cdot10^{16}\,\text{m}$ is the Sun–Proxima distance ($4{,}24$ light-years $= 4{,}01\cdot10^{16}\,\text{m}$), not the star's size. The drawing `DRAW.proxima` is a dashed line from the Sun to the star, so the label now names what is drawn. It matches lang/fi.json and check-1 ("Proxima Centaurin etäisyys"). No experiment uses this object. The content hash is unchanged (lang texts are outside it) and the diff in the packet was empty, so nothing else changed.
- From round 1, still valid: one script recomputed every number in the lesson and inquiry.json next to lesson-answers.py. Exp-1 gives 5, exp-2 gives 8, exp-3 gives −4, siirto gives $12\,732\,\text{km}$, check-2 gives $57\,917$ and the example gives $6{,}47\cdot10^{4}$. All agree.
- Each experiment's start state gives the object its intro names (`mainObj`). `kohdeExp = round(log10 m)` is the same as the $\sqrt{10}$ magnitude rule.
- The physical values are right: the Sgr A* horizon, the Coulomb/gravity ratio for two protons ($10^{36}$), the observable universe, the Milky Way, the heliopause, the Oort cloud and the sim OBJ sizes. The to-scale axes in the figures are right too.
- Interactions, Tunnista, the observable universe, the exit ticket and the check-3 model answers are correct. Exactly one option is right in each choice. The scope is within the FY1 brief.
