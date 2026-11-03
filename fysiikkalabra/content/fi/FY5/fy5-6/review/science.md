VERDICT: PASS
CONTENT-HASH: 2e717a4604ba3d9e

## Blocking

## Polish
- lesson.md (Milloin ympyrämalli pätee) — the 0,5 % Moon discrepancy is attributed only to the shared centre of mass. That is a fair C simplification: the two-body correction alone gives about 0,6 %, and eccentricity accounts for the rest. No change needed.

## Checked
- Round 1 blocking item fixed: koe-1 now has `tolerance` 0.001, so it accepts 7,662–7,678 km/s. That covers 7,67 and the computed 7,671 and rejects 7,60, and the 7,6 mistake feedback can now appear.
- Round 1 polish done: the stale lesson-answers.py comment is relabelled, the escape-speed remark is gone from the virhe feedback, and Painottomuus (text, figure labels, aria) now names the gravitational force $\overline{F}$, the same as the orbit figure, the sim and the model force diagram.
- The experiments' new `names` and `values` labels match their initial states (v 7,00 km/s, h 400 km, m 1000 kg and 1 kg).
- The worked example now writes γM as 3,98438·10¹⁴ m³/s². My recomputation gives v = 7659,7 m/s and T = 5570,6 s, about 92,8 min, so it stays consistent.
- One script recomputed every number again from the task data with my own formulas, and all agree: g and weight at 420 km, the data table speeds, geostationary height 35 787 km, Hubble 544 km, Mars mass 6,43·10²³ kg, the exit ticket 7,54 km/s, and the spreads of 3,3 % and 11 %.
- The sim runs checked against exact orbit calculations still agree: 7,00 km/s crashes; 7,60 gives 155 km; 7,67 gives 396 km; 7,68 gives 432 km; 8,00 gives 1700 km; T = 92,4 min; F is 8,69 N, 8,69 kN and 3,65 MN. sim.js is unchanged since round 1.
- In every choice item exactly one option is correct and each distractor's feedback is right.
- Painottomuus is explained as free fall with zero support force and never as a centrifugal force, and this is the same in the theory, the glossary, ennuste-3 and the exit ticket.
- The circular model's conditions are stated where it is used, and the content stays inside the FY5 scope (no ω, no Kepler's laws, no potential energy).
- The vr graph is to scale, and the force diagrams show only real forces, with a and v drawn beside the body.
