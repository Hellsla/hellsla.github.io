VERDICT: FAIL
CONTENT-HASH: 9c1e5a7e224de067

## Blocking
- exercises.json:80 fy3-5-L3-01 — **B**: the task asks the student to justify that ΔU = 0 because the temperature stays constant, but "same temperature, same internal energy" holds only for an ideal gas (guardrail), and the task does not say so; the solution (solutions.md:91) brings the ideal-gas assumption in by itself, and L3-03 states it in the task — add "Ilmaa voi pitää ideaalikaasuna." to the task text.

## Polish
- solutions.md fy3-5-L2-03 — "800 J = 0,8 kJ … yksi merkitsevä numero" while the answer is 800 J; "0,8 kJ (sadan joulen tarkkuudella)" says the same more cleanly.
- fy3-5-L1-05 — the escaping air also gains kinetic energy (the jet); fine at this level (C), but "kun ilma on pysähtynyt" would make ΔU = Q + W exact.

## Checked
- Recomputed all twelve answers in one script with my own signs: 570 J, −8,4 kJ, 250 J, −500 J, −70 J, −15 J, 160 kJ, 800 J, 40 s, −18 J, 1,699 → 1,7 m, 310 J; answers.py prints the same.
- Sign convention ΔU = Q + W (Q > 0 in, W > 0 done on the system) used the same in every task, solution and answers.py, as in the lesson.
- W = Fs uses a force along the motion and an average force, as fy3-2 allows; P·t for constant power.
- L3-02: constant speed so F = mg, insulated so Q = 0; 1 kg of water would warm only 0,24 K — correct and realistic.
- L3-03 states the ideal-gas condition and explains that ΔU depends only on the end states while Q and W depend on the route.
- Data realistic (kettle 2,0 kW, 89 % kept; blender 250 W; steam engine kJ per stroke).
- Every solution complete: given/asked, principle with reason, symbolic form first, conversions, rounding reason, real balance check.
- Tolerances 0,02 fit the data's significant figures.
