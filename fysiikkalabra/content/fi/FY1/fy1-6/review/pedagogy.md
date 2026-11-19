VERDICT: PASS
CONTENT-HASH: eed93700cddfc321

## Blocking
(none)

## Polish
- lesson.md `free-fall` figure (Ydinajatus) — it shows fall distances 4,9; 14,7; 24,5 m, but the lesson has no tool for them (s = ½gt² and area under the graph are outside FY1), so a student can only copy them and may ask where they come from — either drop the distances and keep the velocity arrows, or add one sentence "matkojen laskeminen kuuluu myöhempään kurssiin".
- inquiry.json `exp-1`, `exp-2` — in a vacuum the sim only evaluates v = gt, so these confirm the arithmetic, not the physics (the conclusion's model answer admits this); exp-3 (air) is the one whose result emerges. Optional: mark exp-2 `optional` or merge it into exp-3, which shows both mass and air in one table, and so cut the Tutki workload (three experiments x 3 rows + conclusion).
- inquiry.json `exp-3` vs lesson.md "Massa ei vaikuta putoamiseen" — the balls in exp-3 are the same size, yet the lesson explains the air effect by "kevyt ja leveä" vs "pieni ja tiheä". The student sees mass matter in air and the text never says why (same air force, smaller share of the weight). Add one sentence in the model answer: "samankokoisilla palloilla ilman vastus on yhtä suuri samalla nopeudella, raskaalla pallolla se on pienempi osa painosta" or equivalent without forces.
- inquiry.json `check-1`, `check-c2`, `virhe`, lesson.md "Yleinen virhekäsitys" and Tiivistelmä — the point "g is not a speed" and "the graph is a rising line" is made four times; per the core-path rule mark `check-c2` `optional` (the concept check `check-1` already covers the graph), and keep one exit item.
- inquiry.json `calc` of `simulaatio` — "rajanopeus" appears without being introduced anywhere in the lesson; either drop the word ("nopeus lakkaa kasvamasta") or leave it behind its closed box only. Also `pr-matka` correct feedback ends "$$…$$." (a full stop after a display block); put the full stop inside the formula or reword.

## Checked
- Opening question (does speed grow evenly, does heavy fall faster) is answered by exp-1/2/3 and the conclusion; slot goals (v = gt as linear model, experiment on masses) both met, nothing beyond FY1 scope (no s = ½gt², no forces).
- Order Pohdinta, retrieval on fy1-5 (v = s/t, same Moon scene), two predictions before evidence, sim, guided experiments with `min` 3 matching the predictions' reveal, theory, reflect, example, exercises, checks, exit ticket follows the brief.
- Predictions: wrong options each repair a named misconception and refer to the table; correct feedback names the evidence; the stem of pred-1 gives the 1 s value so the commitment is meaningful when reopened.
- Exp-1's numeric question introduces Δv/Δt before the word "kiihtyvyys"; hints are progressive; solution has all seven parts; answer 9,81 within tolerance of table-derived 9,795.
- Exp-3 numbers (10,5 and 37,5 m/s at 4 s) reproduce from the stated model (d = 0,20 m, C = 0,47, tanh form); model values are labelled as model values, the conclusion says Kokeet 1 and 2 repeat the formula.
- Example: seven stages, one step each, unit conversion explained (1 m/s = 3,6 km/h), conversion from the unrounded value, reasonableness check uses the graph; 14,715 and 52,97 are correct.
- Siirto task: g from data (3,7 m/s²), 11,1 m/s; mistakes (29,4; 22,2; 3,7) have repairing feedback; hints go from "which number is the growth per second" to the substitution.
- Exit ticket tests the core idea (v ∝ g, v = gt) and ties to the hook; 4,9 and 29 m/s and 6,06 are correct.
- Finnish: case endings after number+unit ("$1{,}0\,\text{s}$:n", "$2{,}0\,\text{s}$:ään") correct; glossary terms (putoamiskiihtyvyys, vapaa pudotus, kiihtyvyys) used consistently; reading level suits upper-secondary.
- Phone captures (contact-1: top, sim, figures, staged example, Ennusta, Tutki) at 390 px: nothing clipped, sim readout and controls legible; figures sit beside their paragraphs; no paragraph over about 120 words.
