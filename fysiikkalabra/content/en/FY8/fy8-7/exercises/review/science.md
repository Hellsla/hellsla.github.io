VERDICT: PASS
CONTENT-HASH: e73b4e5e83dd72e3
Mode: full (round 1)

## Blocking
- none

## Polish
- exercises/exercises.json:319 — L3-02 asks for green photons per second but its unit is "photons" (L1-07 uses "1/s" for the same quantity) — set the unit to "1/s".
- exercises/exercises.json:337 — L3-04 c) "the thermal power turning into heat in the medium per second" doubles power/heat/per second, and solutions.md:258 says "the rest of the energy is heat" while the task says "turns into internal energy" — e.g. "the rate at which the internal energy of the medium grows (the heating power)" and the same words in Given.
- exercises/solutions.md:269 — L3-04 c) laser photon energy shown as 1.8566e-19 J; from the task's constants it is 1.8565e-19 J (the difference 1.788e-20 J and 1.44 W are right).
- exercises/solutions.md:121 — L2-03 cites "the table of quantum dots: 3.0 nm emits 530 nm", while the table of L2-05 gives 529 nm for 3.0 nm — name which table is meant (the lesson's) or use one value.

## Checked
- All 17 numeric answers recomputed from the task texts with own formulas in one script: each agrees with exercises.json and answers.py within 0.9 % (tolerances 2–6 %); a student rounding to the data's figures stays inside every tolerance.
- L2-05 and L2-06 tables: five gaps 2.551/2.344/2.164/2.063/2.010 eV, steps 0.207 and 0.053 eV, fluxes 2.039/1.571/1.636/1.973e16 1/s, order A, D, C, B, ratio 1.298.
- L3-05: least-squares fit of the five points above threshold gives slope 0.398, intercept -9.86 mW, threshold 24.8 mW, 0.524 photons per pump photon; four-level explanation of the threshold (gain against losses) is correct.
- L3-04: 9.826e19 and 8.080e19 1/s, 82.2 %, 5.0 W, quantum-defect part 1.44 W (29 %), 0.8222 x 0.912 = 0.750; "unavoidable" is justified by the photon energies.
- Choice tasks L1-06, L1-08, L2-07: exactly one correct option, each distractor wrong and its feedback right; L1-09 truth values 1 F, 2 T, 3 F, 4 F, 5 T correct, 650 nm = 1.91 eV.
- Solutions: symbolic form before substitution, conversions, rounding reason and a real reasonableness check in every numeric one; graph references (3.27e15, 2.04e15, 2.7e15 1/s per mW) recomputed.
- The packet's exercise brief was empty, so notation was judged against the set itself and the course scope, not the lesson text.
