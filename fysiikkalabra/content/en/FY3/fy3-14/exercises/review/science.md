VERDICT: PASS
CONTENT-HASH: 9b3f1bcfcda5b9bf
SCOPE: delta added-exercise from 4c569087682acfc2 base 81db4a6fd727

## Blocking
(none)

## Polish
- content/en/FY3/fy3-14/exercises/exercises.json (fy3-14-L2-09) — "Not all the ice has time to melt" can read as a time limit, while the reason is that the water's heat is not enough (20 kJ < 60 kJ). Optional: "Not all the ice melts." Language only; the physics in the solution is right.

## Checked
- fy3-14-L2-09 (new situation: the extra heat needed): bars 25, 5 and 60 kJ on a 5 kJ grid; energy conservation in an insulated container stated in the task; heat left for melting 25 - 5 = 20 kJ < 60 kJ, so ice remains at 0 °C (guardrail boundary case right); extra heat 60 - (25 - 5) = 40 kJ, as answers.py.
- L2-09 reasonableness: 20/60 = 1/3 of the ice melts, 2/3 remain, so 40 kJ = 2/3 of the melting heat; a real check. The 2 % tolerance fits values read exactly from grid lines.
- Figure energy-bars: the bars end at 25, 5 and 60 kJ as the solution reads them; the description gives the same and not the answer.
- fy3-14-L1-09 (new situation: an 80 g block already at 0 °C): no warming term needed, Q = s m = 333 kJ/kg * 0.080 kg = 26.64 kJ, answer 27 kJ; the solution explains the 334 vs 333 kJ/kg difference (under 1 %, inside the 4 % tolerance); the 25 K drink-cooling check is right (26.6 / (4.19 * 0.25) = 25.4 K).
- Solutions complete: given, principle, symbolic formula first, conversions, substitution, rounding reason, check.
- Scripted comparison with the Finnish exercises.json: all 23 exercises have the same answers, units, tolerances, figures and task-text numbers; every answers.py value within its tolerance.
- Hash identical at start and end.
