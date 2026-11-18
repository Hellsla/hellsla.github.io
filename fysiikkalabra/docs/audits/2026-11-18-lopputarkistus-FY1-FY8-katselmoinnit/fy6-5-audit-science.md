VERDICT: PASS
CONTENT-HASH: 2dde1d7403e54d9e

## Blocking

## Polish
- lesson.md:164 — "Kuvan piirissä on kaksi silmukkaa" — the lesson's own definition of *silmukka* (any closed path) gives three loops: source–R1–R2, source–R1–R3 and R2–R3. The last one gives U2 = U3 most directly. The conclusion is right, so this is imprecise, not wrong (Minor) — "kaksi lähteen kautta kulkevaa silmukkaa", or name the third loop.
- lesson.md:291 — "sisäenergiakseen" — typo for "sisäenergiaksi" (Minor).
- inquiry.json siirto / lesson.md "Lintu johdolla" — the 50 Hz line is modelled with resistance only. At 50 Hz the inductive drop over 4 cm is about 5 mV, the same order as the resistive 1,9 mV. "Millivoltteja" still holds, so this is a C simplification. Optional: "tasavirtamallissa" (Minor).

## Checked
- Recomputed in one script with my own formulas (R23, I1, U1, VB, I2, I3, koe-1 at R3 = 30/60/120 Ω, koe-3 reference shift, worked example, prediction 1, Etsi virhe sum 0,45 A, siirto 1,92 mV and its mistakes 192/1920 mV, tarkistus-2 3,0 V and 15/9, kertaus 2,0 mA and its distractors, exit ticket 0,15 A and 3,5 V). All agree with lesson-answers.py and the text.
- Kirchhoff's laws: stated with their basis (charge conservation, a unique potential at each point) and their conditions (steady currents, ideal source, ideal wires). The signs in ΣΔV = 0 are right. U_AB = V_A − V_B does not depend on the reference point.
- Figures: the junction arrows' widths are proportional to the currents (24:16:8 px). The circuit's potentials at A–F are right. The potential graph's vertical axis is to scale (20 px/V), and its rises and falls sit in the U, R1 and R2 bands.
- sim.js implements the stated model. The reference shift subtracts phi[ground] from every potential. simState gives I1, I2, I3, Vp, VA, VB, VF and U1 for the experiments. The limits are stated in Mallin oletukset, and the 1280 px capture matches.
- Experiments: koe-1 varies R3 only (U, R1 and R2 locked), koe-2 varies the probe only (reference locked) and koe-3 varies the reference only. Each isolates its parameter.
- Predictions, Etsi virhe and tarkistus-1: each has exactly one correct option, and each distractor's feedback correctly names its error.
- Energy wording follows P1 (sisäenergiaksi, joka siirtyy lämpönä). "Lämmöksi" appears only in a wrong option.
- Bird: correct mechanism (parallel branch with mV across it). The safety statement about arcing is exact.
- Worked example: solved symbolically first, two significant figures justified, and the check uses both laws.
- Within FY6 scope (vastusten kytkennät, Kirchhoffin lait, potentiaali). No later-course physics.

## Scores
- 1 Physics and mathematical correctness: 4. Every number recomputes and every model condition is stated. One loop-count imprecision and one C simplification (AC treated as DC).
- 6 (physics of models): 5. The simulation's values are called model values, its assumptions are listed, and each experiment isolates its varied parameter.
- Findings: loop count Minor; typo Minor; AC note Minor (C). No Critical or Major.
