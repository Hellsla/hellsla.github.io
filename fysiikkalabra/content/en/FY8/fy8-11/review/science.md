VERDICT: PASS
CONTENT-HASH: 90710eb33ad30700

## Blocking

## Polish

## Checked
- Round-1 polish done: assets/sims/fy8/fy8-11/sim.js:138,181 now use `__('sydan_otsikko')` and `__('sukupolvi_akseli')`; en.json gives "reactor core" and "generation g"; shot fy8-11-sim-1280.png shows them in English.
- sim.js diff is the two label lines only: model, multiplication factor, RNG seeds and `simState` unchanged, so koe 1 (N20 = 39 387 / 934 / 7) and koe 2 (1000, 1437, 1987, 3264) from round 1 still hold; shot at s = 30 % shows k = 0.96, consistent with k = 1.04 at 20 % and 1.00 at 25 %.
- figures.json: the new tarkistus-2 description (fy8-11/sidosenergia-luku) translates the Finnish one exactly: A 20–240, axis 7.0–9.0 MeV, grid 10 × 0.1 MeV, maximum near A = 60 (true: Fe/Ni region), axis break stated.
- Scripted comparison against content/fi: every number of lesson.md, inquiry.json, exit-ticket.json, SVG aria-labels and figures.json matches the Finnish source (decimal comma normalised).
- tarkistus-2 still consistent with the figure: (8.5 − 7.6) MeV · 236 ≈ 210 MeV, mistakes 0.9 and 106 correct.
- Round-1 recomputations (173.28 MeV worked example, D-T 17.59 MeV, 3.5 vs 0.85 MeV per nucleon, 1 g U-235 = 3.42 t coal, ITER 1.77·10^20 1/s) untouched by the changes.
