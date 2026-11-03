VERDICT: DONE

Drafted the chapter *Atomiydin ja radioaktiivinen hajoaminen*; `check_lesson.py fy8-8` is all ok.

- `lesson.md`: Ydinajatus covers nucleons, Z, N and A, isotopes, why nuclei decay (the N–Z chart), alpha, beta-minus, beta-plus and gamma decay, and nuclear energy levels with the Co-60 → Ni-60 gamma spectrum as the analogue of atomic levels. `## Kaava: Hajoamisyhtälöt` has the four decay equations, conservation of A and Z, and E_γ = E_y − E_a, λ = hc/E_γ. The staged example is Cs-137 β⁻ with the 661,7 keV gamma. Nuclide data is cited as NNDC NuDat 3 (ENSDF) in the text.
- `figures.py`: 7 figures (hero smoke detector, isotopes, chart, decays, levels, shifts, task figure spectrum).
- `inquiry.json`: hook, an optional retrieval item, 2 predictions (α and β⁻ changes), the sim with the guided experiment koe-1 (U-238 series), a conclusion, an interpret task on the Co-60 gamma spectrum (numeric), theory, a reflection, an error-spotting item, a transfer task (U-235 → Pb-207) and 3 checks.
- New sim `assets/sims/fy8/fy8-8/sim.js`: the U-238 series on a nuclide chart, with NNDC decay modes. It has 42 assertions in `tests/sims/fy8-8.json`. Its texts are in `lang/fi.json` under `sims.fy8-8`.
- Exercises 5/4/3 with complete solutions; `answers.py` and `lesson-answers.py` compute every number.
- `exit-ticket.json`: 2 questions. `glossary.json`: added nukleoni, isotooppi, alfahajoaminen and gammasäteily.
