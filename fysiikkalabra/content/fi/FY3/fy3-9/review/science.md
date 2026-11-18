VERDICT: PASS
CONTENT-HASH: 4851f543ccf2280e

## Blocking

## Polish
- The prompt "Kuinka suuren voiman ilma kohdistaa pussin yhteen sivuun?" does not say which air. The answer, 2,0 kN, holds for either side, but the bag is not crushed because the inside air pushes back with an equal force. Writing "ulkopuolinen ilma" in the prompt, or adding one sentence about the inside air to the feedback, would prevent a student from picturing a crushing net force.

## Checked
batch delta review: the new retrieval choice `kertaus` is recomputed: F = pA = 101 000 Pa · 0,020 m² = 2020 N ≈ 2,0 kN, the only correct option, with two figures that fit 0,020 m². The distractors are wrong and their feedback right: 2,0 N leaves the pressure in kPa, 5,1 MN is p/A = 5,05·10⁶, and 2,0 kPa gives a pressure unit for a force. The choice fits the hook's crisp bag. It does not reveal Ennuste 1 (Boyle: 200 kPa), Ennuste 2 (Charles: about 60 ml) or Ennuste 3 (the hyperbola), because it holds no change of state. lesson-answers.py agrees with my own values. The lesson.md changes are presentation only.
