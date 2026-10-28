VERDICT: PASS
CONTENT-HASH: ba0823c1b322100e

## Blocking

## Polish
- content/fi/FY3/fy3-9/exercises/solutions.md:29 — L1-03's reasonableness check says the real pressure stays "hieman pienemmäksi" because the fast expansion cools the air; for a near-adiabatic expansion it is about 15 % lower (430 kPa·(2/3)^1,4 ≈ 244 kPa vs 287 kPa) — say "selvästi pienemmäksi" or drop the size word.
- content/fi/FY3/fy3-9/exercises/exercises.json — several values with units are plain text ("30,0 ml", "101 kPa", "2800 m³", "2,0 cm³", "250,0 kPa") while others are inline LaTeX; make them uniform.

## Checked
- All 12 answers recomputed with my own formulas from the task texts (Boyle, V/T and p/T in kelvins, p = p₀ + ρgh, gauge → absolute → gauge, cylinder length ∝ volume); all agree with answers.py and exercises.json. L2-03: least-squares slope 2,009 J and mean of pV 2,002 J both round to 2,0 J, inside the 5 % tolerance.
- Every task states its model's assumptions (fixed amount of gas, constant T or p or V, soft balloon at constant pressure, Boyle assumed at 300 bar, bubble air not dissolving, negligible hose volume).
- Gauge vs absolute pressure handled correctly in L3-02 and L3-03, and the solution explains why the gauge reading cannot go into p₁/T₁ = p₂/T₂.
- L3-01 uses the guardrail's exact safety wording ("Noustessa ei saa koskaan pidättää hengitystä: hengitetään normaalisti koko nousun ajan").
- L2-01's remark on real air at 300 bar (pV ≈ 10 % above ideal, about 1,8 m³) points the right way; 40 min of breathing at 50 l/min is realistic.
- Significant figures justified by the real limiting datum in each solution (L2-02 kelvin difference to whole degrees; L3-03 subtraction to 0,1 cm).
- Reasonableness checks are real checks: pV equal before and after, Celsius alternatives shown to be absurd, freezer lid force 7 kN.
- Physics inside FY3 (hydrostatic pressure from the chapter *Paine ja hydrostaattinen paine*); notation as in the brief.
- Hash identical at start and end.
