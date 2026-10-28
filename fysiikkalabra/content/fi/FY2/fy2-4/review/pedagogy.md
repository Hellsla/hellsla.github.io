VERDICT: PASS
CONTENT-HASH: 3d76e58b5c55fcf6

## Blocking

## Polish
1. inquiry.json koe-1 and the sim readout — the readout still prints "Hyötysuhde (tyypillinen arvo) η = 25 %", so the share asked (E_h : E_o = 75 %) follows as 100 % − 25 % without the table. Fix: hide η in the readout while an experiment is active, or ask for something the readout lacks (e.g. E_h in kJ at t = 10 s from P_h · t).
2. inquiry.json ennuste-1/koe-1 — the sim takes 25 % as input, so the experiment cannot refute the guess; it only shows that E_a : E_o stays constant. The text says this honestly ("simulaatio ei mittaa sitä"), so not blocking. Fix (optional): add one line to the reflect prompt that the 25 % comes from data, not from the simulation.
3. inquiry.json ennuste-1 prompt — the hint sentence ends in a second question ("Kuumenevatko … ajossa?") after the main question, so the question is not last. Fix: put the hint before "Kuinka suuri osa …?".
4. lesson.md "Hyötysuhde kertoo hyödyn osuuden" — the first paragraph is dense (about 90 words, four claims). Fix: split off "Sähkölämmittimessä …" under its own short ### subheading or into the following sentence of the table intro.
5. inquiry.json koe-2 is optional and its numeric result (5 %) is given in the question; acceptable as an optional extension, no change needed.

## Checked
- Path: Pohdinta question (where the lamp energy goes, how to measure goodness) is answered by Ydinajatus, figure 1 and the pair figure; Teho is retrieved first; goals η = E_a/E_o = P_a/P_o met; no FY3 content (no chain of efficiencies, no heat engine).
- Figures 1 and 2 at 390 px: print quality, LaTeX labels, colour plus text (valo/lämpö), arrow widths to scale, placed right after their paragraphs; figure beside paragraph at 1280.
- Table of typical η labelled as typical rounded values; fits 360 px; bensiinimoottori caveat stated.
- Worked example: seven stages, symbols before numbers, unit conversions, significant-figure reason, double check; does not repeat the exercises.
- Sim at 390 and 1280 px: picture, controls, readout clear; Käyttöohje, Mallin oletukset, Laskennan selitys closed; koe-1 locks device and P_o, varies t; sim sticky beside experiments at 1280.
- Predictions: ennuste-1 wrong options each repair their misconception; ennuste-2 (optional) reasoning-based and honest about the model's constant η.
- Etsi virhe, transfer task (MJ to W, three hints, solution), three checks and exit ticket test share versus power and loss is not vanishing; solutions complete.
- Workload: core path hook, retrieval, one prediction, one experiment, conclusion, error, transfer, exercises, two checks, exit ticket: about one lesson.
- Finnish: glossary terms consistent, chapter names not ids, case after number+unit correct, decimal comma, \cdot and colon for division.
- Exercises not judged (reviewed apart). Hash unchanged at end: 3d76e58b5c55fcf6.
