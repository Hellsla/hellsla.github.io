VERDICT: PASS
CONTENT-HASH: 143f8c7de03cb4d6

## Blocking

## Polish
- solutions.md:821 (L3-03) — the solution relies on "ideaalikaasun sisäenergia riippuu vain lämpötilasta ja määrästä", but the task never calls the gas ideal — add "ideaalikaasu" to the task text.
- exercises.json L2-04 — 2,0 kJ in 40 s is 50 W of heat into a cold jug, about 3× realistic — for example Q = 1,0 kJ and ΔU = 11 kJ (t stays 40 s).

## Checked
- One script recomputed all 12 exercises (my values = answers.py = exercises.json), plus siirto 5,4 J (mistakes 6,6 and 599,4), check-2 30 J (230 and 10), virhe 160 J, the exit ticket 180 J and the example 110 J.
- ΔU = Q + W with W done on the system is consistent in the formula, figures, solutions, hints and feedback. The content is the first law only, and W = Fs and G = mg stay within the FY3 scope.
- I ran sim.js headless. Slow insulated push: W = ΔU = 40,83 J, ΔT 113,7 K, 18,8 s. Fast insulated push: 47,25 J, ΔT 131,6 K. Slow conducting push: W 35,06 J, after settling Q = −35,06 J, ΔU = 0, p/p₀ 1,33. All match pred-1, pred-2, koe-2 and the sim-spec.
- The theory behind the model holds. A 2D gas without collisions, compressed only along x: T = T₀(1+(4/3)²)/2 = 407 K and the piston pressure is 2,37 p₀. Real 0,50 g of air: adiabatic ΔT 35,8 K and W 12,8 J, isothermal W 12,1 J. C = 0,359 J/K. The speed ratios are 1/53 and 1/3,5.
- The model's limits (2D, no collisions, exaggerated heating, model values) are stated.
- koe-1 and koe-2 each lock the other parameter, and simState provides every measured key.
- Every correct option and every feedback is physically right.
- Figures 1–3 (captures): the piston and arrow directions, the hot → cold heat flow and the sign panels are correct.
- Hash identical at start and end.
