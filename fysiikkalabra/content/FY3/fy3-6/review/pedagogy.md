VERDICT: PASS
CONTENT-HASH: 1f1a6b1c38646d0c

## Blocking

(none)

## Polish

1. inquiry.json simulaatio/koe-1, koe-2 — the readout and the dashed T line show the equilibrium temperature (e.g. 26,8 °C) as soon as the initial state is set, before *Upota*. The animation then adds nothing, and the "experiment" only evaluates the formula being predicted (the packet warns against this). Hide T and the Q readout until the object has been immersed, or let the student read T off the curve. Not blocking: the student has already committed to the prediction.
2. lesson.md Ydinajatus — "Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri" -> "Yksi tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri". The next sentence names a second reason (surface layer); the reflect item asks for it, so mark it clearly as "toinen syy".
3. inquiry.json hook — the hook asks a question but its text already says the sand is hotter "koska ..." nowhere, which is good; yet the water depth/surface-layer cause is only in the theory text. Consider a one-line hint in the reflect prompt ("pohdi myös, kuinka syvälle lämpö ulottuu") so the student can find it.
4. inquiry.json ennuste-1 — wrong-option feedback quotes model values (26,8 °C, 44,0 °C) in the same breath as the correct answer; fine after the reveal, but check that it appears only after koe-1 (the packet says reveal is gated, so only confirm).
5. exercises.json L2-02 — uses P = W/t; confirm fy3-5 or an earlier lesson introduced it, otherwise add "teho on energia aikayksikköä kohti" to the task text.

## Checked

- Learning path: hook -> retrieval (fy3-5) -> two refutable predictions -> sim and two controlled experiments (one variable each) -> theory -> reflect on own predictions -> example -> error-spotting -> transfer with hints -> three checks -> exit; the opening question is answered in "pohdi" and the theory. Workload is one lesson.
- Slot goals met: Q = cmΔT, calorimetric measurement (worked example, koe, tarkistus-2), solving a multi-term equation (derivation of T, error item).
- Predictions can be refuted: model values 26,8 / 44,0 °C and 40,0 / 55,0 / 63,1 °C recomputed and correct; option feedback repairs the misconception.
- Figures 1 and 2 (captures 390 px): legible, to scale, colour backed by labels; the 1280 px lab layout puts experiments beside the sim without clipping.
- Worked example staged in six steps; numbers (374,6; 383; 24,6 °C; 1257 and 75 J/K) recomputed correct; significant figures argued.
- Exercise answers L1-L3, tarkistus-2, siirto (29,1 kg), virhe item (6,6 / 30,0 °C) and exit ticket recomputed: all correct; levels progress, none repeats the example; mistake values match real slips.
- Finnish: no case or glossary errors found; terms match the glossary.
- Phone (390 px): sim, controls and readout fit; locked sliders labelled (vakio); exit ticket readable.
- Deterministic check "FAIL sims" in the packet was not re-run; the sim itself worked in the captures.
- Content hash unchanged at end of review.
