VERDICT: FAIL
CONTENT-HASH: f66de27277e0e818

Pedagogy review of fy14-photoelectric (2026-11-01), against docs/fy14/writing-guide.md §1, §2, §8 and docs/inquiry.md.

## Blocking

1. **Prediction 1 is answered before the student predicts.** `inquiry.json` `hook` says the bright red lamp frees no electrons "even after many minutes", and the violet lamp frees them "at once". The `> **Why**` line and the hero figure show the same thing. Then `pred-red` asks what bright red light does. Both wrong options ("electrons start to leave", "after a delay") are ruled out by the text the student has just read, so there is nothing to argue about and Experiment 1 cannot refute anything.
   *Fix:* keep the hook (it is the puzzle) and replace `pred-red` with a prediction the hook does not answer, tested by `exp-stop`. Example: "Violet light frees electrons from sodium. You change the wavelength from $500\ \text{nm}$ to $300\ \text{nm}$. What happens to the stopping voltage?" Options: grows / stays the same, because the intensity is the same (the wave model, as in the Puzzle table) / falls, because shorter waves carry less energy / stays the same, because the metal is the same. Use `reveal: {"after": "exp-stop", "min": 3}` and quote model values in each option's feedback (for example $0.40\ \text{V}$ at $450\ \text{nm}$ and $1.77\ \text{V}$ at $300\ \text{nm}$). Move the red-light reasoning into the `herata` stage as a short pair discussion of the hook question.

## Polish

2. `inquiry.json` `find-error`: the correct option is 162 characters and carries the full correction. The others are 37–92 characters, so the length gives the answer away. Shorten it to "The photon energy is in joules, but the work function is in electronvolts." and move the numbers ($2.48\ \text{eV}$, $0.34\ \text{eV}$) into its feedback. In the core path the correct option is longest in 3 of 7 choices (`pred-bright`, `check-3`, `find-error`), which is acceptable once this one is fixed.
3. `inquiry.json` `check-explain`: this is the hardest speaking and writing task, but it has no language support nearby. The word bank is far above, in Investigate. Add a short sentence-starter box to the prompt or to `text` just before it, for example: "I agree / I disagree, because …", "One red photon has only …, but …", "A more powerful laser means …, not …", "Instead, I would use …, because …".
4. Workload. `teacher.md` gives Theory summary 15 minutes. In that time students read the Puzzle, Key idea, Formula and stopping-voltage text (about 900 words of B1–B2 physics English), do the vocabulary match, read three biographies and complete the reflection. For many groups this is too much. Make the biography reading part of the optional `people-task` (or homework) in `inquiry.json` and `teacher.md`, or move `theory-people` behind `optional: true`, so the core path fits 75 minutes.
5. `inquiry.json` `french-corner`: the tip for *la lumière* compares the French *u* with "German *ü*". These students are Finnish, so say "the Finnish *y*", as `fy14-fr-bonjour` does. The tip for *un électron*, "*uh-nay-lek-TRON*", hides the nasal vowel of *un*. Write "a nasal *un*, then link the *n*: *un‿électron*". Use the same respelling style as the French unit (Finnish-based, for example *fre-KÃS*), not a mix of English-based and Finnish-based respellings.
6. `inquiry.json` `pred-red` feedback for the "delay" option (if the option is kept elsewhere): the simulation cannot show time, so say plainly that the model has no time axis and that real experiments show no delay (Lenard). As written, "however long you wait" suggests that the student watched.
7. `teacher.md` "Timing": say what to do with pairs that finish Investigate early (the optional find-error task, or plotting Experiment 1 for caesium) and what to cut if Investigate runs over (the second experiment's third row, or the French corner as homework).

## Checked, no finding
- Sequence: Think about it → Predict → Investigate → Theory summary → Apply → Check, with a reflection back to the predictions.
- In the browser (Playwright, 1280 px): after commit, `pred-bright` shows no feedback ("Feedback appears when you have made the measurements"). Its feedback opens only after two rows of `exp-intensity`. The model values match the feedback ($6.0 \to 18.0\ \text{nA}$, $0.740\ \text{eV}$). An empty `explain` keeps its model answer closed. No console errors.
- The experiments control their variables (only intensity, or only wavelength with $U$ as the response).
- The feedback repairs misconceptions (wave model, delay, J/eV mixing, slope versus intercept, current versus stopping voltage).
- The conclusion has a word bank, sentence starters, a pair role split, a model answer and observable criteria. The English is B1–B2 with bold key terms. The worked example is staged and complete.
- `teacher.md` is concrete (timing, organisation, demo, assessment criteria, difficulties, extensions).
