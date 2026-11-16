VERDICT: PASS
CONTENT-HASH: 3ce1b534cce6a362
SCOPE: delta added-exercise fy1-2-L2-08 (work queue 19), round 1

## Blocking
- none

## Polish
- none

## Checked
- This review covers fy1-2-L2-08 only (a new exercise, judged in full). The hash was 3ce1b534cce6a362 at the start and at the end.
- I recomputed it myself: Δm/m = 10⁻⁶ kg / 1 kg = 10⁻⁶, which is 10⁻⁴ % = 0,0001 %. 25 µg gives 2,5·10⁻⁶ %. 1 mg / 25 µg = 40. answers.py prints 0.0001, which matches exercises.json (unit %, tolerance 0,02).
- The significant figures (one, from 1 mg) are right. The conversions mg → kg and µg → kg are right. The formula is stated in symbols before the substitution. The reasonableness check (one millionth of the mass) is a real check.
- I checked the BIPM pages (fetched 2026-11-16). The 1889 platinum-iridium prototype and the forty copies are there. So is the 1946 verification, which found the copies diverging, and the third verification of 1989–1991, with a median difference of about 25 micrograms. The reasons given for the new definition are long-term stability and more use to modern science. The current definition fixes h = 6,626 070 15·10⁻³⁴ J s, together with the definitions of the metre and the second. All of this matches the model answers a), b) and c).
- a) says the drift could not be attributed to any one prototype, because the IPK was 1 kg by definition. That is correct, and it is the standard argument.
- d) correctly separates the exactness of a definition from measurement uncertainty, without misusing any measurement terms. The physics and the scope are FY1 (SI system).
