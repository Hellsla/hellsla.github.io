VERDICT: PASS
CONTENT-HASH: b761e81118edf191
Mode: full, round 1 (hash identical at start and end)

## Blocking
- none

## Polish
- lesson.md:288 (figure `greenhouse`) — one infrared photon goes into the CO₂ molecule and two come out; only the aria-label says they are alternative directions, so the picture can be read as one photon in, two out — draw one of them dashed or say "one of the possible directions" in a visible label.
- assets/sims/fy8/fy8-2/sim.js:99–101 — the canvas labels `-1{,}51`, `-3{,}40`, `-13{,}6` are literal decimal commas, so the English page shows −1,51 on the canvas and −1.51 in the readout — format them with `tx()` like the readout.
- lesson.md / sim / exercises — the red edge of visible light is 750 nm in the sim and the 1.7–3.3 eV range, 720 nm on the spectrum figures' scale and "over 780 nm" in solution L3-04 — one limit, or say that the edge is not sharp.
- lessons/FY8/fy8-2/lesson-answers.py (comments `ex-J`, `ex-eV`) — the comments say 3,1037e-19 J and 1,9374 eV; the values are 3.1039e-19 J and 1.9375 eV as the lesson shows.

## Checked
- Every number recomputed in one script with own formulas (h, c, e of the course): worked example 3.1039e-19 J = 1.9375 eV → 1.94 eV; retrieval 1.91 and 3.02 eV; Balmer 656, 486, 434, 410 nm (gaps 170, 52, 24 nm), 7→2 397 nm; Lyman 122, 103, 97, 95, 94 nm; visible 1.65–3.26 eV; find-the-mistake 1.05e-25 "m", 3.028e-19 J, 656 nm; transfer 3.0617 − 2.3396 = 0.722 eV (mistake 9.92 eV, share 23.6 %); check 2 2.27 eV (mistakes 3.64 and 0.44); CO₂ 15 µm 0.083 eV; fluorescence figure 3.40 and 2.38 eV.
- Definitions and conditions: exact-difference rule carries its two limits (finite line width, ionisation); absorption only from populated states; the Sun's dark Hα explained by the hot atmosphere's n = 2 population; re-emission in all directions, the line darker, not black. No A or B finding.
- Figures to scale: `spectra` 1 px/nm, lines at 410, 434, 486, 656 nm; `levels` 21.98 px/eV, all six levels in place; `fluorescence` 55.9 px/eV for both arrows.
- Simulation code: E_n = −13.6 eV/n², λ = hc/ΔE with the lesson's constants; n_u > n_l enforced; simState gives `dE` and `lam`; readout values equal the text's. Limits (no brightness, one atom, levels as given data) are stated in the model box.
- Experiments: koe-1 locks mode and n_l = 2, koe-2 mode and n_l = 1, each varies only n_u; adapter keys `tila`, `na`, `ny` exist.
- Assessment: one correct option in each choice; every distractor is wrong and its feedback names the right reason; lamp-spectrum figure shows 405, 436, 546, 577/579 nm, so mercury is the only match.
- Greenhouse box: absorption, transfer by collisions, re-radiation in all directions; within the optional thematic link.
- Exit ticket and summary agree with the theory.
- The packet states check_lesson.py had not been run; no lint physics warnings were available to judge.
