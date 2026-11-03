VERDICT: DONE

Draft, round 1. `check_lesson.py fy8-1`: every line ok.

- `meta.json`: glossary adds *elektronivoltti*.
- `lesson.md`: Miksi + hero (UV vs red lamp on zinc electroscopes); Ydinajatus (phenomenon, wave model vs observations as a list, photon E = hf, electronvolt by substitution); Kaava: Fotonin energia (E = hf = hc/λ, hf = W + E_k,max, f₀, λ₀, Millikan line); staged example (405 nm on sodium, 0,78 eV); misconception; summary. Figures: `ilmio`, `energia` (to scale), `kuvaaja` (E_k,max–f for Na and Zn).
- `inquiry.json`: hook, optional retrieval (c = fλ), two predictions (bright red light; doubled intensity), sim, three experiments (650 nm vary I; 405 nm vary I; vary λ with a numeric λ₀ question), conclusion, theory, reflect, example, error spotting, transfer task (photomultiplier λ₀), exercises, three checks, exit ticket.
- `exercises/`: 5/4/3 with complete solutions; `answers.py`, `lesson-answers.py` compute every number.
- New sim `assets/sims/fy8/fy8-1/sim.js` (photons, electrons, to-scale energy panel, narrow stacked layout, adapter), texts in `lang/fi.json` `sims.fy8-1`, 46 assertions in `tests/sims/fy8-1.json`, `sim-spec.md`.
- `glossary.json`: fotoni, kvantti, valosähköinen ilmiö, irrotustyö, Planckin vakio, elektronivoltti.

Lint warnings left on purpose: spectral light colours outside the palette (FY8 rule: real colours).
