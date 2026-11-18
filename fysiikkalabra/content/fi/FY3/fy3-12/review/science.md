VERDICT: PASS
CONTENT-HASH: 2ffd1ae3f9d1f45d

## Blocking

## Polish
- lesson-answers.py defines g = 9.81 but never uses it. Remove it.

## Checked
batch delta review: the Kertaa ΔU = Q + W choice changed to a ground layer that gives off 4,0 kJ as heat and receives 1,0 kJ. I recomputed ΔU = 1,0 − 4,0 + 0 = −3,0 kJ. The prompt now states W = 0 and "eikä olomuoto muutu", so a falling temperature follows; without that, freezing could hold the layer at 0 °C. Exactly one option is correct (−3,0 kJ, temperature falls). The other three feedbacks are right. "Energy is conserved" is answered with the layer's own change, and the energy "siirtyy lämpönä ympäristöön ja kasvattaa sen sisäenergiaa", which follows the guardrail that a body has internal energy, not heat. The −4,0 kJ option misses the heat received, and the +3,0 kJ option has the sign wrong. The edits to the exit ticket, the Etsi virhe and fridge prompts and the example's knowns only add LaTeX units and split one paragraph, and their numbers are unchanged. I recomputed them: exit ticket 0,20 · 50 · 30 = 300 W, window 1,0 · 1,5 · 30 = 45 W, fridge 0,30 · 4,0 · 16 W · 24 h = 0,461 kWh (stored 0,461). The new lesson-answers.py gives −3,0.
