VERDICT: PASS
CONTENT-HASH: 29511f4151251bcf

## Blocking
(none)

## Polish
- lesson.md:175-182 (and Tiivistelmä last bullet) — the "Todellinen kantaverkko on kolmivaiheinen" section brings in pääjännite, pätöteho, tehokerroin $\cos\varphi$ and $\sqrt{3}$, which the prerequisites do not teach and the slot goals do not need. It is too hard for fi-easy and breaks the two-conductor model the student has just learned — fix: cut it to two sentences ("Todellinen verkko on kolmivaiheinen; $400\,\text{kV}$ on vaihejohtimien välinen jännite. Periaate on sama.") and drop the formula.
- inquiry.json ennuste-dc — the prediction (muuntaja + akku) is never tested: the sim only models transmission, so it is answered by reading theory, not by evidence. Also the transformer ratio $N_1 : N_2$ is only a readout in the sim, not something the student varies — fix: say in the reveal's pending text that this prediction is settled by the theory (or add a short thought experiment), and keep the ratio work in the example and exercises.
- lesson.md:232 — "Siirtojännite on johtimien ja maan tai johtimien keskinäinen jännite" mixes the real network with the two-conductor model — fix: "Siirtojännite on johtimien välinen jännite."
- lesson.md:365 — the "scene" illustration (phone charger) sits after the Tiivistelmä, away from the charger paragraph at line 150 — fix: move it next to that paragraph.
- inquiry.json hook — it asks two questions (why not the generator voltage, how can voltage be changed) and the reflect that revisits them is optional; the second is answered only in theory — fix: shorten to one question, or make reflect part of the core path.

## Checked
- Learning path: induction (fy7-7) → transformer → power conservation → I²R loss → high voltage; hook answered by the explain in the investigation; no extra goals other than the 3-phase section above.
- Prediction 2 can be refuted: the experiment gives 24, 6.0, 1.5 MW, and every wrong option's feedback cites those model values and names the misconception (U²:R, linear).
- Variable control in koe-1: P and l locked, only U varied, min 3, values given as model values.
- Explain criteria are observable and match the prompt; the model answer carries the numbers.
- Worked example: 7 stages, one step each, units, sig. figs. and sanity check with power. 1980 turns and 81,82 A verified. It is not repeated in the Sovella task (tuulipuisto: 300 A, 720 kW verified).
- Etsi virhe and the numeric mistakes (U²:R, RI, MW/kW) are real mistakes with repairing feedback; hints go from principle to numbers.
- Exit ticket tests both core ideas (turns ratio, I² dependence).
- Finnish: case after number+unit correct throughout (20 kV:n, 110 kV:iin, 230 V:ksi, 2 %:a); glossary terms used correctly.
- Not checked: no page captures exist (the packet says none yet), so legibility, the phone layout and the 1280 px layout are not judged here (visual review). Exercises are outside this review.
