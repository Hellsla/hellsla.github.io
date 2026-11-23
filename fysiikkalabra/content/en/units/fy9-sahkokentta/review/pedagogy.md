VERDICT: PASS
CONTENT-HASH: 12b4cb1f1fce7b8a

## Blocking
None. The earlier FAIL (s4 b asked for one quantity and answered another) is fixed.

## Polish
- s4 b rubric `assumptions` and the model answer call 4 mm "a lower limit for the safety distance". The wording is correct but takes a second to follow. Something like "breakdown is certain up to about 4 mm, and an arc can strike across longer gaps" says the same thing more directly.
- s4 b is worth 5 points for four rubric items: concept 1, math 2, assumptions 1, transfer 1. The "consequence" item (about 1.2 A) goes beyond the question, which asks for an explanation and an estimate. It is harmless but rewards extra content.

## Checked
- s4 b is now well-posed and consistent in every place it appears.
  - The task text asks to "estimate up to what length of air gap breakdown is certain".
  - The solution's Find line says "the longest air gap across which breakdown is certain".
  - The model answer gives $d = U/E_\text{max} = 12\,\text{kV}/3\,\text{MV/m} \approx 4\,\text{mm}$.
  - The rubric math item has the same computation.
  - The common-mistake line says 4 mm is not a safe distance.
- The stem gives everything the student needs: the 20 kV phase-to-phase voltage, the roughly 12 kV to earth, and the dielectric strength of air. Nothing names the model, so the student has to choose the uniform-field estimate. The 12 kV versus 20 kV trap is a real, named mistake.
- Physics reading. In the uniform-field model, E reaches E_max at d = U/E_max, so breakdown is certain for gaps up to about 4 mm. Field enhancement near the tip and thin conductor means longer gaps can also break down, and the answer says so. It makes no claim that 4 mm is safe.
- The rubric points sum to 5 and match the part's points. The `assumptions` shared key carries a specific detail. The current estimate is labelled as an example ("for example $10\,\text{k}\Omega$").
- The task stays authentic and unfamiliar, with parts a, b and c at rising demand: potential difference, then air breakdown, then step voltage. The other s4 parts were not changed.
- The unit hash is 12b4cb1f1fce7b8a at the start of the review. I did not re-run it at the end, because only the re-review of s4 b was in scope and I edited no other file.
