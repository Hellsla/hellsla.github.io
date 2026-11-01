VERDICT: FAIL
CONTENT-HASH: 4f300b7cb4a81aa3

Pedagogy review of fy14-atom-models (2026-11-01). Read unit.md, inquiry.json, teacher.md, developer.md and the hero and Predict captures. Page rebuilt and tested in Playwright at 390 px.

Browser check: both predictions lock on commit with no feedback. `pred-gold` opens at *Key idea*, after the gold-foil section, the paths task and the spectra. `pred-jump` opens at *Bohr's quantum atom*. Model answers stay closed until the student writes. There are no console errors.

The path is well chosen: Thomson's atom, the gold-foil surprise, line spectra, then Bohr. Other strengths:
- The red-line photon energy is measured data that the student works on.
- `check-explain` bridges well to the Coulomb barrier of fusion.
- CLIL support is good: a word bank and starters for both written tasks, a vocabulary match, and a French corner.

## Blocking
1. `inquiry.json` `pred-gold`: the prompt marks correct reasoning as wrong. It says "Imagine that Thomson's model is how you picture the atom. What do you expect …?" A student who reasons correctly from that premise picks "All pass through, each turned by a tiny angle at most". That option's own feedback says "This is what Thomson's model predicts", yet it is marked wrong. The student is punished for doing what was asked. Fix: change the prompt to "In 1909 Thomson's model was the best picture of the atom. What do you think Geiger and Marsden actually saw when …?" Then open the feedback of the "All pass through" option with "That is what Thomson's model predicts, and what everyone expected. The experiment showed something else: …".
2. `inquiry.json` `review` (in Think about it, just before the predictions) gives away `pred-jump`. Its feedback states the two facts that decide `pred-jump`: a shorter wavelength means a larger photon energy, and brightness means more photons, not bigger ones. So the prediction becomes recall of the task just before it. Fix: move `review` into Investigate as the first activity before `red-line`, where it prepares the calculation. Alternatively, swap its content for a prior-knowledge question that does not compare colours, for example converting $E = hf$ for one wavelength.

## Polish
1. `inquiry.json` `compare-spectra` model: "Glowing hydrogen gas, whereas, gives …" misuses *whereas*, a word that the criteria and teacher.md set as a target. Fix: "The hot filament gives a continuous spectrum …, whereas glowing hydrogen gas gives a line spectrum …".
2. `inquiry.json` `red-line` says "Keep the answer: you will compare it with Bohr's model", but no task asks for that comparison. Fix: add to `back-to-predictions` or to a hint of `blue-line`: "Check that $E_3 - E_2$ gives your $1.89\ \text{eV}$."
3. The worked example (closest approach) does not model learning goal 3 (a wavelength from a jump), which the student meets in `blue-line` with only the formula section. This is acceptable because `blue-line` has hints and a full solution. Teacher.md could point weaker students to that solution after their first attempt.
4. Option lengths: in `pred-gold`, `find-error` and `check-3` the correct option is the longest, by 1–2 characters. Fix: trim one word from each correct option.

## Shared issues
- As for fy14-classical-limits: in `templates/inquiry.js` a section that is merely touched by the viewport counts as seen.
