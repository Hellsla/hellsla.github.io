VERDICT: PASS
CONTENT-HASH: 58c9cf965e5f11f7

## Blocking

## Polish
- assets/sims/fy8/fy8-11/sim.js:138,181 — the canvas labels "reaktorin sydän" and "sukupolvi g" are Finnish on the English page (seen in shot fy8-11-sim-1280.png); the rest of the UI is translated — translate them through `__()` like the other labels (language, not physics).
- inquiry.json tarkistus-2 figure fy8-11/sidosenergia-luku — its aria-label is still Finnish (packet screenshot list #20) — translate the label.

## Checked
- Every number of lesson.md, inquiry.json, exit-ticket.json and the exercises matches the Finnish source one to one (scripted comparison, decimal comma normalised): no number was changed in translation.
- Recomputed with my own formulas: worked example Q = 0.1860220 u · 931.5 = 173.28 MeV, 0.079 % of the mass; D-T 17.59 MeV; per nucleon 3.5 vs 0.85 MeV (ratio 4.2); 1 g U-235 = 8.2·10^10 J = 3.42 t coal.
- Sim model rerun (mulberry32, seed 1000(series+2)+7): koe 1 N20 = 39 387 / 934 / 7 at s = 0/25/50 %; koe 2 N = 1000, 1437, 1987, 3264; 1.04^30 = 3.24; ln1000/ln1.04 = 176 generations.
- ITER siirto 1.77·10^20 1/s, both mistakes (1 773 351 eV-as-MeV, 0.156 fission energy), 1.5 mg of D-T; tarkistus-2 236·0.9 = 212 MeV and its 0.9 / 106 mistakes.
- Hook: 1600 MW electric from coal at 40 %, 24 MJ/kg → 14 400 t/day.
- Definitions (binding energy per nucleon, multiplication factor, critical, moderator, delayed neutrons 0.65 %, residual heat 6 % → 1–2 %) translated correctly and as in the glossary.
- Mechanisms preserved: Coulomb barrier and tunnelling for fusion, void/temperature feedback of water, decay heat from fission products, electrons cancelling when ΣZ is conserved.
- Every choice item has exactly one correct option; distractor feedback correct; model answers (johtopaatos, keskustelu, tarkistus-3) agree with the theory; Cs/Sr 30 a → 1/1000 in 300 a.
- Exercises: see exercises/review/science.md (all 12 answers recomputed and agree).
