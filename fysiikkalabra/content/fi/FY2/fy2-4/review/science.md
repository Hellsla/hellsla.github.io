VERDICT: PASS
CONTENT-HASH: 893ac0f1037abe61
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only

## Blocking
- none

## Polish
- none

## Checked
- Hashes recomputed with scripts/reviews.py at start and end; all six match the brief.
- Sim "model": losses defined as the energy not ending up as the defined useful output (correct definition, 1); "mostly thermal energy in many devices" is a correctly hedged claim (2, 3); solar panel: part of the incoming radiant energy is reflected, so reflection is no longer called heat (the reported error is gone).
- Experiment 1 model: 60 kW x 10 s = 600 kJ, 25 % -> 150 kJ, 20 s -> 1200/300 kJ, 15/60 = 25 %, remainder 75 % (recomputed); "losses, mostly heat" is right for a petrol engine (exhaust, coolant, friction).
- Read the surrounding paragraph in the source file: the new sentences fit the model text and its stated conditions (constant efficiency, constant power).
- Guardrail "Energy, heat and efficiency": "lämpöenergia"/"heat" for the losses is allowed in FY2, and these passages do not conflict with it.
- fi, en and fi-easy say the same thing.
