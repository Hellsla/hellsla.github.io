VERDICT: PASS
CONTENT-HASH: 6baa2111c76a816f
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- unit.md Ydinajatus: "Liikkuvaan varaukseen ja virtajohtimeen se kohdistaa voiman, kun liike tai virta ei ole kentän suuntainen": the condition is now stated and agrees with the formula map's perpendicular component.
- s7 a part text: the added sentence about the precision of the source's figures points to the conclusion criterion (c − v is smaller than the rounding of 26 659 m and 11 245 1/s, so its size cannot be concluded; a particle with mass stays below c). No number changed: v = 11 245 · 26 659 m/s = 2,9978e8 m/s, v/c = 0,99996.
- s7 d conclusion criterion: the sentence about the protons' total mass is removed, so the criterion asks only what d asks (ratio 4,357e8 J / 5,787e5 J = 753). The mass remark stays in the solution as a reasonableness note (6,7e-13 kg, below a nanogram: right).
- `python scripts/practice.py check units/fy9-magnetismi-valo`: OK (7 tasks, 110 points). Hash equal at start and end.
