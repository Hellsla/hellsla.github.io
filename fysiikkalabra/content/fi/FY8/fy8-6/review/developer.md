VERDICT: DONE

Draft of *LEDin valo ja Planckin vakion mittaaminen*; check_lesson.py all ok at 360/768/1280 px.

- `lesson.md`: Ydinajatus (bands, energy gap, electron–hole photon hf ≈ E_g, threshold voltage, LED / laser diode / lamp spectra), Kaava: Kynnysjännite ja fotonin energia (eU_k ≈ hf = hc/λ, U_k from the I–U graph, h = ek from the (f, U_k) fit, intercept explained), staged example (h from two points of a fitted line), two misconceptions, summary.
- `figures.py`: hero, vyot, spektrit, iu, sovitus, task-only ryhma (catalog rebuilt). Lint warns only on real spectral colours (FY8 convention).
- `inquiry.json`: hook, retrieval, two predictions, sim, koe-1 (six LEDs at 2,20 V), koe-2 (red LED I–U, U_k by extrapolation), conclusion, interpret (six U_k, Graphical Analysis Pro fit → h), reflect, example, Etsi virhe (intercept), transfer (IR LED λ), three checks (one figure task), exit.
- `assets/sims/fy8/fy8-6/sim.js` + `lang/fi.json` sims.fy8-6 + `tests/sims/fy8-6.json` (30 assertions): LED circuit with meters and a (U, I) graph, not animated (no speed control).
- `exercises/`, `answers.py`, `lesson-answers.py`, `exit-ticket.json`, `sim-spec.md`; glossary: valodiodi, laserdiodi, kynnysjännite, energia-aukko.
