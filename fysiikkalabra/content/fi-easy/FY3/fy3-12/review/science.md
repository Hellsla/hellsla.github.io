VERDICT: FAIL
CONTENT-HASH: 6ca6d2b611456194

## Blocking
- **A (definition, internal consistency).** In inquiry.json, the herata retrieval's first distractor feedback says: "Pois siirtynyt energia on lämpönä ympäristössä." That treats heat as something stored in the surroundings. It goes against the guardrail that heat is energy in transfer and becomes the surroundings' internal energy, and against fy3-6's retrieval, "Kappaleessa ei ole lämpöä". Suggested: "Pois siirtynyt energia kasvattaa ympäristön sisäenergiaa: $\Delta U = Q + W$ antaa $-3{,}0\,\text{kJ}$." The Finnish (fi) version has the same sentence ("Pois siirtyvä energia on lämpönä ympäristössä"); fix both.

## Polish
- "lämpötila laskee" holds only while the layer's state of matter does not change; freezing soil water on a winter night would keep it near 0 °C. A short "(olomuoto ei muutu)" would cover it.

## Checked
batch delta review: new herata retrieval choice (gives 4,0 kJ, receives 1,0 kJ, W = 0). Recomputed: ΔU = −3,0 kJ (correct, one correct option). The −4,0 kJ and +3,0 kJ feedbacks are right. It does not reveal Ennuste 1 (back-radiation) or 2 (new balance). Typography-only prompt changes are rechecked: the exit ticket 0,20 · 50 · 30 = 300 W, the window 1,0 · 1,5 · 30 = 45 W, and the fridge 0,30 · 4,0 · 16 W · 24 h = 0,461 kWh. The worked-example split is presentation only. lesson-answers.py agrees.
