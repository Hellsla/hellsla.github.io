VERDICT: PASS
CONTENT-HASH: e352c445313a4f16

## Blocking

## Polish
1. sim.js canvas at 390 px (fy3-7-sim-390.png, exp-exp-1-390-1.png) — the canvas is scaled to about 55 %, so the KaTeX tick numbers (-20, 0, 1000, 2000) and the labels "sulaa 167 s" and "kiehuu 1130 s" render at roughly 7 px. "kiehuu 1130 s" is also crossed by the grey curve and its right end is clipped by a stray vertical stub. Everything on the canvas reads cleanly at 1280 px. Fix: on a narrow canvas use bigger label fonts, fewer ticks (0, 1000, 2000 and -20, 0, 100), and move the labels clear of the curve. The durations are repeated in the readout, which is why this is not Blocking.
2. sim.js readout (both widths) — six lines stay visible, including the computations "sm/P = 167 000 J/1000 W = 167 s" and the axis note "Kuvaajan aika-akseli…". CLAUDE.md Lesson page 4 puts the computation behind Laskennan selitys and keeps only key quantities visible. Fix: show "Sulaa 167 s · Kiehuu 1130 s" and move the substitution and the axis note into a closed Laskennan selitys box.
3. Sim controls at 1280 px (fy3-7-lab-1280.png) — the grid zigzags: the Massa slider sits right of the buttons, Teho is below left and Nopeus right, with labels at different heights. Align the three controls in one row or one column.
4. Experiment tools at 390 px — "Kirjaa mittaus" and the table come after the whole simulation, so the student scrolls about 700 px between moving a slider and recording. The status line "Säädä teho P" uses a plain P, and the table headers are monospace; the "latexilla kaikki" brief covers both.
5. pred-3 — the simulation only computes sm/P, so it cannot tell Aino's, Bea's and Cem's explanations apart. The feedback says so honestly, and the mass-proportional duration does rule out Aino's version. Say in the experiment intro that the model supports Bea's explanation only through the duration.

## Checked
- Path: hook, then the q = cmΔT retrieval, three predictions, a sim with two controlled experiments (min 2), theory, a reflection that returns to the opening question, then the staged example. The slot's three goals (olomuodon muutokset, ominaishöyrystymislämpö, mikromalli) are covered and nothing extra is added.
- The opening question is not answered before commitment: the hook and the lead question leave it open, and the pred-3 feedback arrives only after a choice.
- Numbers are consistent: 2260/334 is about 6,8; the ratio of 1130 s to 167 s; 0,597 kg; 2,34 MJ/kg with a 3,5 % overshoot explained in the example's reasonableness step.
- Figures 1 to 3 at 390 px are clean, labelled, and have colour with meaning. The heating curve states that its horizontal lengths are not to scale.
- The example has four stages, one step each, symbolic first. It is not repeated: L3-03 extends it with a difference method.
- Exercises: levels 5/4/3, each solved symbolically. The L1-05 curve reading and the L3-03 loss-cancelling are good transfers.
- Option feedback repairs the misconception: the virhe item and the mistakes for 27,8 and 11300 are good.
- Finnish: no case or glossary errors found (0,50 kg:aan, 2000 W:iin, 100 °C:ssa). The exit ticket tests the core idea.
- Workload: 3 predictions, 2 experiments, 3 checks and 12 exercises are heavy but one lesson's worth.
- Hash unchanged at the end. The "sims" deterministic check FAILs; I did not diagnose it (not my scope), and the developer should look.
