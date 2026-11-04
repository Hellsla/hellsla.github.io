VERDICT: PASS
CONTENT-HASH: 5f3c4888687a23c4

## Blocking

## Polish
- content/fi/FY1/fy1-1/exercises/exercises.json:228 (L2-07) — the task says "pisteet asettuvat suoralle". Measured points lie on the line only approximately; the residuals here are −0,28…+0,31 mm. — Write "asettuvat likimain suoralle", in line with the fits guardrail.
- content/fi/FY1/fy1-1/exercises/exercises.json:65 (L1-06) — the new distractor "Malli on teoria, jota ei voi enää muuttaa" mixes up model and theory. The feedback refutes "unchangeable" correctly but leaves "a model is a theory" unanswered. — Add half a sentence: a theory too stays open to revision.

## Checked
- Round-1 Blocking (L2-07 uncertainty) fixed. The solution uses the guardrail's scale-reading wording. It calls 0,25 mm : 300 ≈ 0,001 mm "vain lukeman osuus" and names the other error sources, which justify two figures.
- L2-07 recomputed: the least-squares slope through the origin is 0,1019 mm, and the line gives 30,56 mm at N = 300 (the solution says 30,6). The answer 0,102 ± 5 % covers the stated range 0,097–0,107 mm. The origin has a physical reason.
- L2-05 new part: 1,0 m in the model ↔ 15,05 AU. Uranus is 4,15 AU away from it and Saturn 5,47 AU, so the answer Uranus is right. In model distances this is 127,6 cm against 63,7 cm.
- L1-06: exactly one option is correct; every distractor is wrong and its feedback is right.
- answers.py now uses the task's 1 AU = 1,496·10⁸ km. L3-05: 143,16 AU, and the comment matches the solution (23,46 AU).
- All 19 numeric answers: answers.py agrees with exercises.json, and the round-1 recomputation still holds for the unchanged tasks.
- L3-04 rewording: no physics change; N = 1,19·10⁹, and the sensitivity 1,2³ → −42 % still holds.
- The hash was the same at the start and the end.
