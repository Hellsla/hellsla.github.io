VERDICT: PASS
CONTENT-HASH: e5ad88872375678b

## Blocking
(none)

## Polish
- lesson.md (example table, 390 px capture) — the last column (θ = 100 °C, p = 137 kPa) is cut off, and step 2 "Kulmakerroin" uses exactly that value; nothing shows the table scrolls — fix: let the table wrap or shrink its font at 360 px, or show a scroll cue.
- lesson.md (fig 4 at 390 px) — tick labels and "mittaukset/ekstrapolointi" render at about 7–8 px, which is hard to read on a phone; the figure is correct in content — fix: larger font in the SVG or fewer ticks (−270, −200, 0, 100) at narrow width.
- inquiry.json exp-1/exp-2 intro, measure labels — "keskinopeus v", "T", "V" and the table headers ("θ (°C)", "v (suht.)", "p mitattu") are plain text, not maths as the 2026-10-26 rule says — fix: write $v$, $T$, $V$ in intro and use maths headers where the table renderer allows.
- lesson.md, text under fig 3 — "alaasteikko", "Yläasteikko" — fix: "ala-asteikko", "ylä-asteikko".
- sim details (390 px) — "Mallin oletukset ja selitys" and "Mallin oletukset" are two boxes saying nearly the same thing, and the thermometer's "100 K" label sits on the bulb — fix: drop one box, shift the label.

## Checked
- Figures 1–4 redrawn: labels in LaTeX-quality type, colour never alone (every colour also has a text label or line style), uncluttered; fig 3 is to scale (0/273/373 K positions match); fig 4 shows the axis at −300 °C and the dashed extrapolation to p = 0 clearly, and the text under it explains this.
- New theory figures (system boundary, micro-model) teach what the paragraph says: boundary, environment, p, V, T; arrow length = speed.
- Learning path: hook → prior retrieval → three refutable predictions → two experiments → theory → reflection → staged example (5 steps) → error-spotting → transfer with 3 hints → exercises; the opening tyre question is answered only in the reflection, after the student commits.
- Experiments isolate one variable each (V locked in exp-1, T locked in exp-2); pressure emerges from counted hits, so a prediction can be refuted; exp-2 shows v unchanged.
- Option feedback repairs misconceptions (celsius ratio, "temperature alone sets p", faster-in-small-vessel); only one speaker is right; no letters or positions are referred to.
- Exercises: L1 conversions, L2 interpolation/extrapolation/ratio, L3 proportionality in kelvins; none repeats the example; solutions in LaTeX with Annettu–Järkevyys; exit ticket tests the core idea.
- Finnish, case endings after unit (K:n, °C:seen) and chapter name instead of a lesson id are correct.
- Layout: 1280 px lab view puts the experiments beside the simulation legibly; 390 px stages and sim have no clipping apart from the Polish items above.
- Workload is at the upper limit of one hour (3 predictions, 2 experiments, 12 exercises) but acceptable.
