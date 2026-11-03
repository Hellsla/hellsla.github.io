VERDICT: PASS
CONTENT-HASH: 40102459c35f36e5

## Blocking
(none)

## Polish
- lesson.md: the English adds "(one cycle)" after "one full oscillation"; harmless gloss, kept.

## Checked
- Translation review of *Periodic motion* (en) against the three-PASS Finnish chapter: lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json, sim labels lang/en.json sims.fy5-7 (incl. the new lbl_malli "model"; sim.js change is a label only, physics untouched).
- Every number per paragraph and per JSON string compared mechanically with the Finnish: identical, decimal point throughout, no `{,}` left.
- Physics terms: period, frequency, amplitude, displacement, equilibrium position, phase, hertz, radian mode, undamped/sinusoidal; T = 2π/B, f = 1/T, x = A sin(2πt/T) and C = π/2 meaning (extreme position at release) all as in the Finnish.
- Every prediction's correct option, feedback values (d = 0.13/3.70/1.85 cm, N = 6/3, f = 1.25/0.625 Hz), koe-3 solution (T_best = 2.20 s → 2.2 s), Sovella (3.8 cm), Tarkista (0.56 Hz), interpret-a-fit model (0.800 s, 1.25 Hz) unchanged in meaning.
- Fixed: experiment `names.aineisto` was the Finnish "aineisto" (shown as "Kept constant: aineisto") → "data set"; activity Extra: phase "weight of a pendulum" → "bob" (consistent with task 2).
