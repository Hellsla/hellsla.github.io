VERDICT: PASS
CONTENT-HASH: 6c831d112eb86c2a

## Blocking

## Polish
- content/fi-easy/FY8/fy8-11/figures.json — has no entry for the tarkistus-2 figure fy8-11/sidosenergia-luku (docs/figures/catalog.json: fi-easy "missing 1"), so the standard-Finnish description is used; it is correct physics, but add a plain-Finnish version like the other figures (language, not physics).

## Checked
- Round-1 polish done: lesson.md:613–615 the literal `\n\n` is now a real paragraph break; the two paragraphs keep 12 g/kWh CO2-ekv., 1,5 % of coal, IPCC 2014, OL3 2005 → 2023, as in the Finnish source.
- assets/sims/fy8/fy8-11/sim.js:138,181 labels now from lang keys; fi-easy.json gives "reaktorin sydän" and "sukupolvi g", identical to the old literals; model and `simState` unchanged.
- Scripted comparison against content/fi: every number of lesson.md, inquiry.json, exit-ticket.json, SVG aria-labels and figures.json matches.
- Sim experiments (koe 1 N20 = 39 387 / 934 / 7; koe 2 1000, 1437, 1987, 3264) and round-1 recomputations (173,28 MeV, 17,59 MeV, 3,5 vs 0,85 MeV/nukleoni) unaffected by the changes.
