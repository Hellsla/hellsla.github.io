VERDICT: PASS
CONTENT-HASH: 3a93fa847b4b0c80
## Blocking

## Polish
- `lessons/FY3/fy3-12/lesson-answers.py` defines `g = 9.81` that nothing uses; it can go.

## Checked
batch delta review: the new retrieval choice (ground layer gives $4{,}0\,\text{kJ}$, receives $1{,}0\,\text{kJ}$, $W = 0$, no change of state) recomputed: $\Delta U = Q + W = -3{,}0\,\text{kJ}$, so internal energy falls and, with "eikä olomuoto muutu" now stated, the temperature falls (round-1 condition fixed). Exactly one correct option; the three distractors are wrong and their feedback says why (conservation vs. the layer's own balance, only the outgoing heat counted, sign error). The round-1 finding is fixed: the energy now "siirtyy lämpönä ympäristöön ja kasvattaa sen sisäenergiaa", matching the guardrail that heat is energy in transfer. The guardrail's condition on $\Delta U = Q + W$ (no change in kinetic or potential energy) is met in this situation. lesson-answers.py gives -3,0. Unchanged numbers in the retyped lines recomputed: exit ticket $300\,\text{W}$, window $45\,\text{W}$ (the student's error is still $\Delta T$), fridge $0{,}461\,\text{kWh}$ (answer 0.461). The worked example's change only splits the question into its own paragraph and adds LaTeX to the areas; its numbers are unchanged.
