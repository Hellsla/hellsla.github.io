VERDICT: PASS
CONTENT-HASH: b761e81118edf191
Mode: full, round 1 (hash identical at start and end)

## Blocking
- none

## Polish
- lesson.md:288 (figure `greenhouse`) — one infrared photon enters the CO₂ molecule and two leave; only the aria-label says they are alternative directions — mark them as alternatives in the picture.
- assets/sims/fy8/fy8-2/sim.js:99–101 — canvas labels `-1{,}51`, `-3{,}40`, `-13{,}6` are literal decimal commas, so the English canvas shows −1,51 and the readout −1.51 — format them with `tx()`.
- lesson.md, sim, exercises — the red edge of visible light is 750 nm (sim, 1.7–3.3 eV), 720 nm (figure scales) and 780 nm (solution L3-04) — use one limit.
- lessons/FY8/fy8-2/lesson-answers.py (comments at `ex-J`, `ex-eV`) — 3,1037e-19 J and 1,9374 eV should read 3,1039e-19 J and 1,9375 eV.

## Checked
- Every number recomputed in one script with own formulas: worked example 1.9375 eV → 1.94 eV; retrieval 1.91 and 3.02 eV; Balmer 656, 486, 434, 410 nm (gaps 170, 52, 24 nm), 7→2 397 nm; Lyman 122, 103, 97, 95, 94 nm; visible 1.65–3.26 eV; find-the-mistake 1.05e-25 "m", 3.028e-19 J, 656 nm; transfer 0.722 eV (mistake 9.92 eV); check 2 2.27 eV (mistakes 3.64, 0.44); CO₂ 0.083 eV.
- Definitions and conditions: the exact-difference rule carries its limits (line width, ionisation); absorption only from populated states; the Sun's dark 656 nm line explained by its hot atmosphere; re-emission in all directions. No A or B finding.
- Figures to scale: `spectra` 1 px/nm with lines at 410, 434, 486, 656 nm; `levels` 21.98 px/eV, six levels in place; `fluorescence` 55.9 px/eV for 3.40 and 2.38 eV.
- Simulation code: E_n = −13.6 eV/n², λ = hc/ΔE with the lesson's constants, n_u > n_l enforced, `dE` and `lam` in simState; limits stated in the model box.
- Experiments: each locks mode and n_l (2, then 1) and varies only n_u; adapter keys exist.
- Assessment: one correct option per choice, distractors wrong, feedback right; lamp figure shows 405, 436, 546, 577/579 nm, so only mercury matches.
- Greenhouse box, summary and exit ticket agree with the theory.
- The packet states check_lesson.py had not been run, so there were no lint physics warnings to judge.
