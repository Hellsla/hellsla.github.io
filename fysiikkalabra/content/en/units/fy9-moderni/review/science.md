VERDICT: PASS
CONTENT-HASH: f5355edae2761e52
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8, -s9; older tasks s1-s7 and the intro untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
None. The three round-1 items are fixed in the en text:
- s8 d Assumptions: the activity clause is gone; it now reads "The result is also too small if the source is replaced by a stronger one or the time spent grows", after the scattering reason. Both raise the dose, so "thicker" follows.
- s8 d criterion 4: part d now asks "Also name one assumption of the model that may make the result too small, and its effect", and the criterion's examples are not the given "the dose rate is constant". Points 4 = 1+1+1+1.
- s9 c: part text "how long ago the distances between the galaxies were zero, assuming that the distances have grown at the same rate", Principle "the distances between the galaxies have grown from zero", criterion 1 "the distance d of a galaxy has grown from zero". Consistent with d and *The evolution of the universe*.

## Polish
- s8 common mistakes, part a: "μ = 16 / 20 cm = 0.80 1/cm" belongs to the old reading point (20 cm; 5.0 µSv/h); with the points now used, (0; 80) and (10; 20), the quotient error is 4 / 10 cm = 0.40 1/cm. Same leftover as in fi.
- "the same rate $v$" in the s9 c Principle mixes a rate with a velocity symbol; "the same velocity v" or "a constant rate" reads cleaner. Meaning unchanged.
- Round-1 polish taken as in fi (no grid point in the s9 text, (10 cm; 20 µSv/h) in s8 a, s9 d criterion 2 accepts another valid argument).

## Checked
- Read the en s8 and s9 tasks.json entries and solutions.md sections. Every number, unit and rounding is the same as in fi (0.14 1/cm, 6.6 µSv/h, 330 h, 2.2 mSv, 3.0 µSv/h, 23.6 -> 24 cm rounded up, 31.6 cm; 72 km/s/Mpc, 117 -> 120 Mpc, 2.33e-18 1/s, 4.29e17 s, 1.4e10 a); the fixed sentences mean what the fi ones mean. Decimal points throughout.
- The same script as for fi recomputed every value from the figures' data: all agree; results rounded to two significant figures as the data.
- Aligned calculation rows; unit fields language-neutral; part texts reveal no structure.
- practice.py check --lang en OK (9 tasks, 136 points); hash the same at start and end.
