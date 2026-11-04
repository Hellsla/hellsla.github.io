VERDICT: PASS
CONTENT-HASH: f73c1faf99b28bab

Round 2 (delta review of round 1 fixes; round 1 hash 5d2b5d87bf295a65). Pedagogy review of fy9-tasavirta, 2026-11-04.

## Round 1 Blocking, verified
1. **B1 Tutki source_note** (`inquiry.json`): the material and the resistivity are gone. The developer's wording still
   said "lisätty mittausjohtojen resistanssi", which answers the task's own question about the non-zero intercept; I
   shortened it to "Arvot on keksitty, ja niihin on lisätty mittausten kaltaista vaihtelua." Verified in the preview.
2. **B2 s3 source_note** (`sovella/tasks.json`): now "Luvut on laskettu mallista, ja niihin on lisätty mittausten
   kaltaista vaihtelua." No E or R_s value is shown before the task (the only 4,62… in the page is inside the model
   solution). Fixed.

## Round 1 Polish, verified
- P1 lue-kuvaaja: the prompt gives only the 3,0 V reading and asks the student to read other values; the 1,0 V value
  appears only in the feedback. Fixed.
- P2 s5 c criterion 4 and model answer: meter placement plus the meter-effect estimate. Fixed.
- P3 teacher.md 15–25 min: fallback (ready graph or intercept as homework) added. Fixed.
- P5 tarkistus-3 criterion 4: "kumpi tahansa riittää". Fixed.
- P4 not changed (potkulauta in akkuvertailu and s2; heating-wire resistivity in paahdin and s1). The developer's
  reason (deliberate repetition of W = UQ and R = ρl/A) is acceptable for a review lesson; it stays Polish.

## New problems introduced by the fixes
None. Task counts, rubric sums (6 tasks, 95 p) and the 75-minute plan are unchanged; practice.py check OK.

## Remaining Polish
1. P4 above, for a later round.
