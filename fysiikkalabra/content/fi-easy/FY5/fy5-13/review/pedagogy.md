VERDICT: PASS
CONTENT-HASH: 40981c5ecada8e6f

## Blocking

## Polish
- lesson.md Ydinajatus / inquiry.json ennuste-1, koe-1 — "silmukka" (kaksi silmukkaa) is used in the prediction and exercises but the text only defines "kupu" (hook says "kaari") — add one clause "silmukka eli kupu ja sen vieressä olevat solmut" at the first use, since this is the S2 version.
- inquiry.json koe-1 intro "Laske solmut myös kuvasta" and the sim readout "Solmuja 1, kupuja 1" at 50 Hz — it is not said whether the fixed ends count (model answer counts them: 2, 3, 4) — say "päät mukaan lukien".
- lesson.md "Aalto ja sen heijastus" — the paragraph is about 125 words and holds reflection, superposition and the definition; split off the last three sentences (seisova aalto) as their own paragraph.
- inquiry.json ennuste-1 — the prompt gives f1 = 100 Hz and the loop count, so the answer follows from "puolet lyhyempi aalto" alone; fine as a prediction, but ennuste-2 (odd multiples) is the one that really tests the model, keep it as the key prediction.
- inquiry.json hook — "heilutustahti" and "kaari" are not tied to the later vocabulary (taajuus, silmukka); the "pohdi" item does tie them, but it is optional.

## Checked
- Path: prerequisites (v = f lambda, reflection, superposition) cover the lesson; opening question is answered by koe-1 and the conclusion; slot goals (standing waves, string and air-column eigenfrequencies) met, nothing extra.
- Both experiments can refute their predictions (2x vs 1.5x/0.5x; 2f1 vs 3f1) and the peak/trough values emerge from the model, not from the formula.
- Workload fits an hour: two predictions, two experiments, one optional third, retrieval/reflect/error items optional.
- Sim capture at 390 px: picture, graph and key values visible, explanations in closed boxes, lead under 30 words.
- Figures (pipes capture): legible, L conditions printed beside each row, colour not alone; the pipe figure shows theory only, no task answer.
- Worked example staged in seven steps, symbolic before numbers, with reasonableness check.
- Concept and calculation checks have misconception distractors with repairing feedback; the explain criteria are observable and match the prompt.
- Exit ticket tests the core idea (n loops/nodes; open vs closed pipe).
- Finnish: no wrong term found; oktaavi and pääkorjaus explained at first use.
