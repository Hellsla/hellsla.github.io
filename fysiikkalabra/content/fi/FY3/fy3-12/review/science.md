VERDICT: FAIL
CONTENT-HASH: b845352d0b689a84

## Blocking
- **A (definition), `inquiry.json` `pr-tasapaino`, feedback of the first distractor.** "Pois siirtyvä energia on lämpönä ympäristössä" describes heat as something stored in the surroundings. This contradicts the lesson and fy3-5: heat is energy in transfer, and a body has no heat. Suggested fix: "Pois siirtyvä energia siirtyy lämpönä ympäristöön, jonka sisäenergia kasvaa."

## Polish
- "lämpötila laskee" holds only while the layer does not change state: freezing moist soil stays at 0 °C while its internal energy falls. On a winter night the layer is usually frozen already, so this is a fair simplification. "(olomuoto ei muutu)" in the prompt would close the gap.

## Checked
batch delta review: the new retrieval choice `pr-tasapaino` is recomputed: ΔU = (1,0 − 4,0) kJ + 0 = −3,0 kJ, the only correct option. The distractors are wrong and their feedback numbers right: "pysyy samana" confuses conservation, −4,0 kJ ignores the heat received, and +3,0 kJ has the wrong sign. The choice does not reveal Ennuste 1 (back radiation) or Ennuste 2 (a new balance after the CO₂ step). The exit ticket gives 0,20 · 50 · 30 = 300 W. The transfer task's answer is unchanged: 0,30 · 4,0 · 16 W · 24 h = 0,461 kWh. The other edits are LaTeX units and a paragraph split. lesson-answers.py agrees with my own values.
