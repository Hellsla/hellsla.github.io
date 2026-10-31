VERDICT: FAIL
CONTENT-HASH: 1f38648415996384

## Blocking
- inquiry.json check-2 `solution`, Principle — "$pV = NkT$" uses k, which the lesson never defines (the lesson works with n, R and $N_A$) — a student who could not solve the task meets an unexplained symbol. Fix: derive the ratio from $p \propto NT/V$ (the lesson's own result, shown in the paine-ja-tekijat figure and the Formula section), or write "$pV = nRT$ with $n \propto N$" and drop k.

## Polish
- lesson.md Key idea ("the temperature in kelvins is directly proportional to the mean kinetic energy of the particles") — mean kinetic energy is FY4 per the FY3 scope; and nothing in the investigation uses it. Fix: "the particles move faster the higher the temperature in kelvins", as the figures already show.
- inquiry.json workload — the core path has about ten Tutki items (3 weighing items, pred-1, sim, two experiments, taulukko, laske-r, conclusion), close to a full lesson before Sovella and the checks. Fix: mark `taulukko` optional (it repeats what exp-1/exp-2 and laske-r already show) and keep `laske-r`.
- inquiry.json hook/pred-1 — the opening question about the balloons has no committed prediction before the weighing data; pred-1 is a deduction after the data, so "Return to your predictions" in reflect shows a prediction made with the evidence in hand. Fix: move a short "same number of particles?" choice before `punnitus`, or retitle pred-1 as a deduction and keep only pred-n in reflect.
- inquiry.json exp-2 — the T-proportionality is never predicted or measured on its own; the student infers it from one cross-experiment row (N = 100 at 600 K versus 300 K). Acceptable, but a one-row justification for the hint "the pressure doubled" is thin; the explicit sentence in hint 1 could ask the student to write the ratio first.
- inquiry.json lahtolippu / exit-ticket.json — the exit ticket tests the calculation skill only; the lesson's core idea (same p, V, T gives same n, whatever the gas) is tested only in the optional check-3. Fix: add a second exit question on it or make check-3 non-optional.

## Checked
- Learning path follows the slot goal (equation of state, solving for a quantity); weighing then simulation then theory, answer to the opening question withheld until the student has the data.
- pred-n can be refuted by exp-1 (hit counts and pressure per N); each wrong option's feedback repairs its misconception; locked parameters and the minimum of 2 rows are set.
- Worked example is staged one step per stage, with unit conversion and reasonableness; it differs from the exercises and siirto.
- Misconception-based distractors in check-1 and check-c2 (Celsius doubling, percentage of degrees) are good; mistakes[] values in laske-r and siirto match real unit errors.
- Explain criteria in johtopaatos and check-3 are observable and match the prompts; model values and invented weighing data are labelled.
- Figures: not checked visually; no captures were supplied (packet says none yet), so legibility at 360 and 1280 px and the sim's behaviour when moved are unverified.
- Finnish and the exercises/ set are out of scope for this English packet.
