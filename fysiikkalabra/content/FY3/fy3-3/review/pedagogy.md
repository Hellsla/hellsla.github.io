VERDICT: PASS
CONTENT-HASH: 0aaf01ed9efec6be

## Blocking
(none)

## Polish
- sim canvas and DOM readout (sim-390, lab-1280) — "T = 300 K", "V = 1,0 dm³", "Paine p ≈ 106", "Lämpötila T", the thermometer labels and the experiment table's p/v/θ headers stay plain interface text beside maths-rendered T and V in the intro and table; per NOTES.md §1 this awaits the teacher — fix when decided: render the readout symbols as maths.
- exp-1 capture at 390 px — right after "Aseta alkutila" the readout says "Paine p ≈ 0" (theory 100) until the counter fills; a student may read it as a result — fix: show "–" or "mitataan…" for the first 1,5 s, or add "odota pari sekuntia" under the readout.
- lesson.md example table at 390 px — the last column (100 °C, 137 kPa) is still cut off, yet step 2 uses it; no scroll cue — fix: shrink the table font at 360 px or add a scroll cue.
- inquiry.json exp-1/exp-2 "Mittaukset" table — header row mixes italic maths (T, V, θ) with monospace plain text (v (suht.), p mitattu) — fix: use maths for all symbols, e.g. $p$ mitattu.
- lesson.md under fig 3 — "alaasteikko", "Yläasteikko" — fix: "ala-asteikko", "ylä-asteikko".

## Checked
- New speed control (Nopeus) and the two info boxes ("Mallin oletukset", "Laskennan selitys") are closed by default, distinct in content, and the calc box states that speed does not change the measured pressure; the old duplicate box is gone.
- Activity texts and experiment intros: v, T, V, $\theta$ now maths; Alkutila/Vakiona/Muutetaan line reads correctly at 390 and 1280 px.
- Added "ja lämpötila pysyy samana" in the micro-model paragraph makes the volume argument correct (collisions more frequent, not harder).
- siirto solution remark (122 kPa vs 101 kPa outside, lid bulges out) is correct and consistent with the answer.
- Learning path unchanged: hook, retrieval, three refutable predictions, two single-variable experiments, theory, reflection, staged example, error spotting, transfer, exercises, checks, exit ticket; opening question answered only after commitment.
- Figures 1–4 unchanged since round 1 (labelled, colour never alone); chapter names, layout at 390 and 1280 px fine (lab view puts experiments beside the sim).
- Exercises L1–L3 and exit ticket unchanged and sound; solutions in LaTeX.
