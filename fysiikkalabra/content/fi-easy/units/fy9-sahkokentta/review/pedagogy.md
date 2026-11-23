VERDICT: PASS
CONTENT-HASH: fe2ecfbd0b95d72a

## Blocking
None.

## Polish
- s4 b: "enintään kuinka pitkän ilmavälin yli sähkö lyö varmasti läpi" is logically tight but easy to misread as a safe distance. The rubric (assumptions) and the common-mistake line already say that 4 mm is a lower bound, not a safe distance, so students are repaired. Optional: "Arvioi pisin ilmaväli, jonka yli ..." would match the solution's Kysytty wording exactly.
- s4 b rubric calls the body current "ampeerien suuruinen"; the model answer gives about 1,2 A for 10 kOhm. Consistent, but it assumes the 10 kOhm path. Optional: state that assumption in the rubric line.

## Checked
- s4 b is well-posed. Text gives 12 kV to ground (20 kV phase to phase explained) and E_max = 3 MV/m, so d = U/E_max = 12 kV / 3 MV/m = 4 mm follows without naming a formula.
- Consistent across task text, rubric (concept 1, math 2, assumptions 1, transfer 1 = 5 points), solution Kysytty, model answer and the common-mistake lines (20 kV mistake, 4 mm shown as safe).
- Physics reading is coherent: in the uniform-field model a gap of 4 mm or less breaks down. Real fields near a thin conductor are stronger, so the estimate is a lower bound. The solution says exactly this.
- The a and c parts are unchanged and still fit: the bird, the touch and step-voltage reasoning, with rising demand a to c.
- Rubric points are fair and tied to what the question asks. No points go to irrelevant things.
- Unit hash matches the one in the packet.
