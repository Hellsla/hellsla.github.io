VERDICT: PASS
CONTENT-HASH: f77ed29cd96c1d51

## Blocking

## Polish
- lesson.md Key idea ("the temperature in kelvins is directly proportional to the mean kinetic energy of the particles") — mean kinetic energy is FY4 per the FY3 scope and nothing in the investigation uses it (carried from round 1). Fix: "the particles move faster the higher the temperature in kelvins", as the figures show.
- inquiry.json workload — the core path still has about ten Tutki items (3 weighing items, pred-1, sim, two experiments, taulukko, laske-r, conclusion). Fix: mark `taulukko` optional; it repeats exp-1/exp-2 and laske-r.
- inquiry.json pred-1 / reflect — pred-1 is a deduction after the weighing data, yet reflect lists it under "your predictions". Fix: retitle it a deduction and keep only pred-n in reflect, or put a short "same number of particles?" prediction before `punnitus`.
- inquiry.json lahtolippu / exit-ticket.json — the exit ticket tests only the calculation; the core idea (same p, V, T gives same n for any gas) sits only in the optional check-3. Fix: add a second exit question on it, or make check-3 non-optional.
- Simulation English text (fy3-10-sim-390.png): decimal commas ("1,17", "1,5", "0,0 s") and "Speed: normal (0.5x)" beside a "mean over 0,0 s" reading that confuses before the first run. Fix: English decimal points; show "–" until a mean exists.

## Checked
- Round 1 blocking resolved: check-2 solution now uses p ∝ NT/V and N ∝ n; no undefined k.
- Learning path follows the slot goals (solve for a quantity from pV = nRT, gas laws combined, particle-level pressure); the balloon question is answered only after the weighing data and the student's commitment.
- pred-n is refutable by exp-1 (initial state set, T and V locked, min 2 rows); every wrong option's feedback repairs its misconception, and the closed Ennusta box reads sensibly afterwards.
- exp-2 gives a real challenge (find N for p = 1.00 at 600 K) whose result emerges from counted hits; hints and mistakes[] match real errors.
- Worked example: seven stages, one step each, with conversions and reasonableness; it differs from siirto and the exercises.
- check-1 and check-c2 distractors are misconception-based (Celsius doubling, degrees as percent); explain criteria are observable.
- Figures (#3-#7) are uncluttered, labelled and legible at 390 px; the lab at 1280 px shows sim beside the experiments; the readings table fits at 390 px.
- Phone usability: sim controls, readout and the three explanation boxes are readable at 390 px; nothing clipped.
- Exercises and Finnish are out of scope for this packet.
