VERDICT: PASS
CONTENT-HASH: eda4ea09580287e0

## Blocking

## Polish
- inquiry.json:257 — the conclusion no longer asks whether efficiency changed with running time, so koe-1 (only t varied) is not explicitly closed; koe-2 and prediction 3 still cover time-independence, so not blocking — fix: optionally add "Muuttuiko se, kun aika muuttui?" back to the prompt only if the teacher wants the control stated in the conclusion.
- inquiry.json:396 — "Ei osu." is colloquial for a student reader — fix: "Ei pidä paikkaansa."

## Checked
- Koe 1 intro: now says the simulation computes the energies from a typical efficiency given as input; the model/measurement distinction is clearer, no answer disclosed.
- Conclusion explain: prompt, model answer and criteria are consistent (3 criteria all match the model answer; model values labelled; the model's constant-efficiency assumption stated).
- Radiator distractor "noin 50 %": a real misconception (all heat is loss); feedback names why (heat is the radiator's purpose) and repairs it without just restating the answer.
- The new distractor no longer overlaps with the "alle 100 %" claim; the other three options and their feedback are unchanged and still distinct.
- Hash re-run at end: unchanged (eda4ea09580287e0).
