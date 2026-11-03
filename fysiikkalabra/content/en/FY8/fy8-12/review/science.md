VERDICT: PASS
CONTENT-HASH: 241fdfa610926999

## Blocking

## Polish
- assets/sims/fy8/fy8-12/sim.js:149 — the canvas label `\text{GM-putki}` is not localised, so the English page shows Finnish ("GM-putki") beside English labels — route it through `__()` like the other labels ("GM tube").
- lesson.md (Common misconception) — the same note as the Finnish review: "used in sterilisation and medicine ... not enough to change nuclei" holds for sterilisation and diagnostics; radiotherapy linacs at 15–18 MV make some photoneutrons. C at this level; if wanted, "used in sterilisation and diagnostics".

## Checked
- Every number in lesson.md (outside SVG label boxes), inquiry.json and exit-ticket.json equals the Finnish original; SVG differences are only label-box widths and text x positions, not plotted data.
- Recomputed in one script: Am-241 5,49 MeV / 34 eV = 1,61·10⁵; example d = 5,5 mm · ln 20 / ln 2 = 23,8 → 24 mm (22 mm 6,25 %, 27,5 mm 3,1 %); Al 25 mm 0,60; apron 0,5^(0,50/0,12) = 5,57 % and the mistakes 84,7 / 94,4 / 12,0; check 2: 800 → 400 at 12 mm, 200 at 24, 50 at 48.
- Prediction 1 and 2: exactly one correct option each; model values (5/550/577, 9/4/535, 590/332/175/89/57; net 586/328/171) and feedback agree; "0,29 ≈ slightly over a quarter" consistent.
- Find the mistake, concept check: one correct option each; distractor feedback right (neutral photon still interacts with electrons; alpha does not activate tissue nuclei).
- Translation keeps the definitions: ionising = single particle/photon removes an electron; ion pair; W = 34 eV > ionisation energy (excitation, electron kinetic energy); half-value thickness lets half through; net count = background subtracted.
- Conditions kept: narrow beam, photon-only law, ranges for alpha and beta, GM tube does not distinguish types and sees few gammas, model limitations (no alpha energy loss in air, no bremsstrahlung, no dead time, ideal detection) stated.
- Causality kept: dense ionisation → double-strand breaks; indirect effect through water radicals; hydrogen-rich neutron moderators (near-equal mass).
- Exit ticket: brighter light = more photons of the same energy; gamma sterilisation does not activate; neutron activation named as the main route.
- Figure alt texts and labels (figures.json) translate the same numbers (12,6 eV, 1,7–3,3 eV, 60 keV, 662 keV, 5,5/11/16,5 mm, 0,1 mm, 5 mm, 5 cm, 500 V).
