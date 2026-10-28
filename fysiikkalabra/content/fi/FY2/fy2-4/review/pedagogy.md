VERDICT: PASS
CONTENT-HASH: 3d657337f41168ea

## Blocking

## Polish
1. inquiry.json koe-1 (simulaatio, lukemat) — the sim readout and canvas print "Hyötysuhde (tyypillinen arvo) η = 25 %" while the student is asked to compute η from the table, so the answer is on screen before the work (the prediction is already committed, so not blocking). Fix: in experiments leave η off the readout (keep P_a, P_h, E), or ask for something the readout does not show (e.g. P_h in kW, or the share lost).
2. inquiry.json kertaus, third option feedback — "saisit tehon muutosnopeuden" is not what 40 : 30 means. Fix: "Jaoit tehon ajalla. Tulos ei ole energia: teho on jo energia jaettuna ajalla, joten energia saadaan kertomalla teho ajalla."
3. inquiry.json ennuste-1 — the hint ("muista Pohdinnan kuuma hehkulamppu") now links to the hook, but nothing gives a scale for 25 % vs 60 %; the table of typical η in lesson.md comes after. Acceptable as a guess to correct; optionally name the lamp's 5 % only after the reveal (already done in feedback).
4. Workload — still hook, retrieval, ennuste-1, koe-1, conclusion, Etsi virhe, transfer, exercises, two checks and the exit ticket on the core path; ennuste-2, koe-2, reflect and check 3 are optional. About one lesson; fine.

## Checked
- Round-1 polish done: ennuste-2/koe-2 optional and feedback says the model assumes constant η (reason E = P · t); 100 % conversion sentence rewritten (0,30 · 100 % = 30 %); sim canvas labels now LaTeX at readable size; ennuste-1 has the hot-lamp hint.
- Path: Pohdinta question answered by Ydinajatus, the lamp figure and the pair figure; prerequisite Teho retrieved; no FY3 content (no chain, no heat engine).
- Figures 1 and 2 at 390 px: print quality, LaTeX labels, colour plus text (valo/lämpö), arrow widths to scale, placed right after their paragraphs; figure 1 beside its paragraph at 1280.
- No text wall; table fits 360 px; example has seven stages, symbols before numbers, units, significant-figure reason, double check.
- Sim at 390 and 1280 px: picture, controls, readout clear; three explanation boxes closed; koe-1 locks device and P_o, varies t; sticky beside the experiments at 1280.
- Experiment reveal after 3 rows; mistake feedback repairs wrong ratio and 0,25 vs 25 %.
- Etsi virhe, transfer (MJ to W, hints, solution) and the three checks have model answers; exit ticket tests share, P vs η and loss is not vanishing.
- Finnish: glossary terms consistent, chapter names not ids, "tasolla/tehon" cases correct, decimal comma, \cdot and colon for division.
- Exercises not judged (reviewed apart). Hash unchanged at end: 3d657337f41168ea.
