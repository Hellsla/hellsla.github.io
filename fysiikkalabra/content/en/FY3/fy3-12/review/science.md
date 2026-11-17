VERDICT: PASS
CONTENT-HASH: bec22c4ab3c51162

## Blocking

## Polish
- `lesson-answers.py` defines `g = 9.81` but never uses it; it can go.

## Checked
batch delta review, round 2: herata retrieval choice (ground layer gives 4.0 kJ, receives 1.0 kJ, W = 0, no change of state). Recomputed ΔU = 1.0 − 4.0 + 0 = −3.0 kJ. The temperature falls, and "no change of state" is the condition that claim needs, so it is now stated. The round-1 blocking item is fixed: the feedback now says the energy "is transferred as heat to the surroundings and increases their internal energy", which matches the guardrail (heat is energy in transfer), and the Finnish source agrees ("siirtyy lämpönä ympäristöön ja kasvattaa sen sisäenergiaa"). Exactly one option is correct. The distractors (ΔU = 0, −4.0 kJ, +3.0 kJ) are really wrong, and each one's feedback says why. lesson-answers.py gives −3.0.
