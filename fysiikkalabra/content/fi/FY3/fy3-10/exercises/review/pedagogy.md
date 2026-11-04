VERDICT: FAIL
CONTENT-HASH: 0033aa9bfd64001a

## Blocking
- exercises.json fy3-10-L3-04 (and its solution in solutions.md) — out of scope: the task defines and uses the compressibility factor Z = pV/(nRT) of a real gas, reads Z from a table at 10 and 20 bar and interpolates, and the solution explains Z < 1 by attraction between the particles. The lesson teaches only the ideal gas (pointlike particles, interactions only in collisions); it has no Z, no real-gas model and no intermolecular attraction, and the LOPS content of FY3 is the ideal-gas equation. The student cannot be expected to know what Z means or why n_real > n_ideal. Fix, either: (1) replace L3-04 with a YO-style multi-step task inside the lesson, e.g. a gas cylinder emptied in stages at changing temperature (n from p, V, T at three moments, mass used via M, how long the gas lasts at a given flow), or a data task with two measurements whose n differ and the cause is a unit or temperature error; or (2) keep the topic but first add a short, labelled "poikkeus" paragraph with Z to the lesson (and the plan line in docs/exercise-bank/FY3.md), which changes the lesson hash and needs its own review. Option (1) is cheaper.

## Polish
- L1-07 solution, Vastaus — "2,31 l ... varmin kahden numeron tarkkuudella 2,3 l" hedges between two precisions; pick one (the 98 kPa gives two figures: 2,3 l, and make the answer check accept 2,31 within 2 %). Also it is a combined-gas-law task with four conversions, light L2 work under an L1 label; acceptable.
- L2-07 — the answer is visible at a glance (B has the higher p at every V), so the data work (pV products) is optional; give the series at different volumes (A at 1,0; 2,0; 3,0; 4,0 l, B at 1,5; 2,5; 3,5 l) or ask for the temperature ratio, so the student must compute pV.
- L3-05 — c) is the same formula a third time; the level is L2-3 border. Add the question "mihin korkeuteen asti pallo kestää" with an interpolation, or ask for the lifting mass at 10 km, to make it a real multi-step YO task.
- L2-06 solution — states the read points (280 K; 115,4 cm3) and (360 K; 148,0 cm3) "luetaan suoralta"; add the line equation or its least-squares slope (0,408 cm3/K, n = 4,96 mmol) so the student can check their own line.
- L1-06 — the correct option is the longest of the four and says "koska" with the full reason; shorten it to the length of the distractors.

## Checked
- 8 new tasks all have full solutions; counts 8/7/5; kinds match the plan (MC on n, state change, error analysis, leaking tyre, slope to nR, two isotherms, real-gas table, weather balloon).
- Numbers recomputed and consistent with answers and tolerances: L1-07 2,314 l; L1-08 0,12 mol vs 1,2e-4 (factor 1000); L2-05 236,6 kPa and 5,3 %; L2-06 4,95 mmol (least squares 4,96); L2-07 pV 244 and 304; L3-04 6,014 mol, Z = 0,88, n = 6,83 mol; L3-05 105,4 mol, 7,38 m3 and 15,7 m3 at 15 km (burst before).
- L1-08 is a proper error analysis: the wrong unit is inferred from the student's own plausibility remark; all distractors have feedback that repairs a different misconception.
- L2-05 separates the temperature effect from a leak by using n = pV/RT; absolute pressure stated ("kokonaispaine"); good everyday context.
- L3-05 uses the standard-atmosphere table and gives the helium amount first; physically right, scope fine.
- Finnish and units fine; capture of fy3-10 exercise sections shows no clipping at 1280 px.
