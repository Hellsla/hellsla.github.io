VERDICT: PASS
CONTENT-HASH: 5ba40612c9cadfb9

## Blocking

(none)

## Polish

1. lesson.md worked example, stage "Reasonableness" — one paragraph of about 170 words holding three ideas (copper match, 24.6 vs 24.5 and its causes, heat capacities of water and metal). The teacher's rule is one thing per paragraph, at most about 120 words, in stages too — split into two or three paragraphs. The Key idea's first paragraph (about 140 words) is also over the limit: split after "…proportional both to the change in temperature and to the mass".
2. inquiry.json `siirto` — the numeric answer is `29.1` (tolerance 0.02) but the solution gives "29 kg, two significant figures" ($29.09\,\text{kg}$). Make the shown answer and the solution agree (29 kg with data of two figures).
3. inquiry.json `check-c2` repeats the lesson's Common misconception example exactly (1.0 kg at 80 °C into 3.0 kg at 20 °C, answer 35 °C), so it tests recall of the text, not the concept. Change the masses or temperatures (for example 2.0 kg at 70 °C into 0.50 kg at 10 °C). It also duplicates the idea of prediction 2.
4. Slot goal "calorimetric measurement": both experiments only predict a final temperature, and the sim computes it from the weighted-mean formula. The student determines an unknown c only in the worked example and `tarkistus-2`. Consider an optional experiment 3 where the object's c is hidden and the student infers it from the recorded T, which is the actual calorimetric measurement and the use of a formula with several terms.
5. inquiry.json `kertaus` (optional) — the retrieval uses a copper object in water, not the beach of the Pohdinta phenomenon (teacher 2026-11-13: retrieval belongs to its phenomenon). Move it to the beach (sand and water both receive energy as heat from the Sun).

## Checked

- Path from fy3-5 prerequisites (heat as transfer, conservation of energy) to Q = cmΔT, then the equilibrium temperature, is followable. The opening question is answered only in Teoria and the reflection.
- Predictions: both can be refuted by the experiments, the varied parameter is single and the others are locked. Each wrong option's feedback names the evidence and the misconception, and the wording still makes sense when the box is reopened.
- The conclusion's model answer matches what the experiments give, and its criteria are observable.
- The Teoria derivation starts from Q given out = Q received, then Q = cmΔT, then solves T symbolically; the weighted-mean reading is useful.
- The worked example has seven stages, each one step; the substitution chains start with the quantity they compute.
- Figures (390 px captures: water-sand, calorimeter): the figure is legible, with the colour (red ΔT bar) backed by the labels, and the temperature rises are drawn to scale.
- Sim at 390 px: the controls and readout are understandable, and the text sits behind Käyttöohje, Mallin oletukset and Laskennan selitys.
- The error-spotting item has a real, common error (the signs when solving) and each distractor feedback repairs its own misconception.
- The exit ticket tests the core idea (Q = cmΔT, and why c decides the rise); the checks have misconception-based distractors.
- The workload is one lesson, and the optional items are marked.
