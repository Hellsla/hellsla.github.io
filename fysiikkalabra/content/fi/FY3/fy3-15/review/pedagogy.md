VERDICT: PASS
CONTENT-HASH: 11fdfd0b3fe68e5d

## Blocking

## Polish
- inquiry.json pred-1 feedback (wrong options) — says "Tutki-osan taulukko näyttää, kuinka paljon vaiheet todella häviävät", but the table holds only efficiencies and the task asks one loss (248 MW) — fix: "Tutki-osassa lasket vaiheiden häviöt" or let the task ask for the boiler loss too, so the prediction is compared stage against stage.
- lesson.md (Kaava, P_L = c q_m ΔT) — the step from Q = cmΔT to power (divide by t, q_m = m/t) is skipped, and the formula is not used in the inquiry — fix: add one sentence "Teho on lämpömäärä aikayksikköä kohti: P = Q/t = c m ΔT / t."
- inquiry.json johtopaatos prompt — three questions in one (stage, cogeneration, hydro) — fix: split into short numbered parts so the criteria map one to one.
- lesson.md end of Tiivistelmä — the "scene" (radiator) figure follows a bullet list it does not explain — fix: place it beside the cogeneration paragraph or drop it.
- inquiry.json hook — "jäähdytysvesi on lämpimämpää" nudges toward the answer before pred-1; acceptable, but a neutral phrasing would keep the prediction open.

## Checked
- Path: hook, retrieval (optional), two refutable predictions, three data tasks (one optional), explain, theory, reflect, example, error spotting, transfer, checks, exit ticket. The opening question is answered at the end; slot goals met, no extra topics. Workload is about one lesson.
- Predictions are refutable: the tables give 248 MW of 300 MW total, and a 40 MW drop in electricity against 232 MW of heat. Wrong-option feedback names the misconception (sum or mean instead of product, Bea's equal trade-off, Daniel's pressure claim).
- No answer disclosed before commitment: theory sits after Tutki; pred feedback only after answering.
- Figures (captures at 390 px): Sankey, stacked graph, bar chart and condenser are legible, to scale, colour never alone; alt texts give the data without the answer to the predictions.
- Worked example: seven stages, one step each, symbols first, unit stage, reasonableness and balance check; it does not repeat the inquiry tasks (600 MW, 0,910/0,440/0,950).
- Etsi virhe (mean vs product) and the transfer task (boiler improvement, 8,6 MW) have repairing hints and mistake feedback.
- Check 1 and 2 use misconception distractors (non-comparable denominators, heat-engine limit); the explain criteria are observable and match the prompt.
- Exit ticket tests the core idea (product, not sum or mean).
- Finnish reads cleanly; glossary terms (hyötysuhde, hukkalämpö, yhteistuotanto, lauhdevoimalaitos) are used consistently; energy is not said to "turn into heat".
- Exercises not judged (reviewed apart). Hash unchanged at the end.
