VERDICT: PASS
CONTENT-HASH: 9ece00a460a2d407
Mode: full, round 1 (hash identical at start and end)

## Blocking

## Polish
- content/en/FY8/fy8-12/lesson.md:492 (Common misconception) — "the gamma, X-ray and electron radiation used … in medicine … its energy is not enough to change nuclei" is true for Co-60, diagnostic X-rays and sterilisation beams (≤ 10 MeV electrons, ≤ 5 MeV X-rays), but high-energy radiotherapy linacs (15–18 MV) do cause photonuclear reactions. The student-facing conclusion still holds, so this is C/B-borderline — optionally write "in sterilisation and X-ray imaging" or "at these energies".
- content/en/FY8/fy8-12/inquiry.json:64 (ennuste-1, correct option) — the alpha source behind 5 mm Al gave 9 pulses against a background mean of 4. Calling that "the level of background radiation within random variation" holds (P(N ≥ 9) ≈ 2 %), but a student who measured 3 for the background may doubt it. Optionally add "a single count of a few pulses varies a lot".

## Checked
- Every number in lesson-answers.py recomputed independently: Am-241 ion pairs 5.49 MeV/34 eV = 1.6·10⁵; alpha range 4.1 cm in air, about 0.04 mm in tissue; m_α/m_e ≈ 7294; visible 1.7–3.3 eV; water 12.6 eV.
- Cs-137 narrow-beam half-value thicknesses from my own XCOM μ/ρ: Pb 5.4–5.5 mm, Fe 12, Al 34, concrete 39, water 81 mm; concrete/lead ≈ 7. Paper d½ ≈ 100 mm at 0.8 g/cm³ is plausible.
- Beta model: μ/ρ = 17·E_max^−1.14 = 6.6 cm²/g and Katz–Penfold range 1.10 g/cm² (≈ 4 mm Al) for 2.28 MeV (Sr-90/Y-90).
- Worked example: d = 5.5 mm·ln20/ln2 = 23.8 → 24 mm (2 s.f.), symbolic first; reasonableness bracket 6.25 % / 3.1 % holds.
- Transfer task: 5.57 % → 5.6 %; the mistake values 84.7, 94.4 and 12.0 reproduced; 60 keV Pb d½ = 0.122 mm (XCOM).
- tarkistus-2 graph is drawn to scale (800·½^(d/12) on a 2 mm/50 min⁻¹ grid); 12 mm, and 24 mm as the mistake. The energia figure's log positions (12.6 eV, 60 keV, 662 keV, visible band) and vaimeneminen (½, ¼, ⅛ at 5.5/11/16.5 mm; Al 0.60 at 25 mm) are correct.
- Sim model values: the Python mirror of sim.js's mulberry32 is line-for-line equivalent (seed, two draws per slot, k reset on change). All quoted counts (5/550/577; 3/9/4/535; 590/332/175/89/57; net 586/328/171, ratios 0.56/0.29) match the means within Poisson scatter. I could not drive the sim in the browser (it did not run off-screen headless), so it was checked from the code only.
- Experiments: each one locks the controlled variables and varies one parameter; the adapter exposes lahde/aine/n; simState carries pulssit. The model limits (no air loss for alpha, ideal GM efficiency, no dead time, single-type sources, no bremsstrahlung) are stated in the model box.
- Each prediction and check has exactly one correct option, and each distractor's feedback names the right physics. The exit-ticket answers and the explain model answers are consistent with the theory and the summary.
- Photon interactions table and crossover energies (water < 0.03 MeV photoelectric, Compton 0.03–25 MeV; lead 0.5/5 MeV; pair threshold 1.022 MeV) are correct. The GM-tube mechanism and the caveat that it cannot tell types apart are correct. Radon and direct/indirect DNA damage are described correctly.
- Scope: within FY8 "ionisoivan säteilyn lajit ja biologiset vaikutukset"; doses deferred to the next chapter; no later-course physics.
