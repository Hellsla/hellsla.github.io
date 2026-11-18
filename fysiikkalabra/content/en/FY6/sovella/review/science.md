VERDICT: PASS
CONTENT-HASH: 5e15e967d1274d52

## Blocking
None.

## Polish
- solutions.md fy6-s1 c, Principle: "Of the electric power, heat is produced both in the resistor and inside the battery" is looser than the Finnish "Sähkötehosta siirtyy lämpönä sekä vastuksessa että pariston sisällä" (FI's "siirtyy lämpönä" wording is allowed by the guardrail). Closer: "Of the electric power, part is transferred as heat in the resistor and part inside the battery; the whole power of the battery is the sum, $E I$." This is class C. The Find and Answer lines of the same part already say "transferred as heat".

## Checked
- I compared this set with the Finnish set, which has a science PASS (8067d7cd885e25ec). I normalised the decimal comma and extracted every number in order. solutions.md has 1246 numbers in both languages and tasks.json 434, and the two sequences are identical. The 9 figure descriptions in figures.json carry the same numbers as their Finnish keys.
- tasks.json: same tasks, parts, kinds and figures. Every part's `answer` (value, unit, tolerance), its points, and every criterion's key and points are identical to the Finnish ones, so the point totals and the rubric match the Finnish set. answers.py is shared, and its output agrees with the stated answers.
- fy6-s3 common-mistakes bullet: "the energy is transferred to the air, whose internal energy increases, and from there as heat to the surroundings" matches the Finnish bullet one-for-one. The "fate of the energy" step in s3 c says the same thing. Neither says that energy "turns into heat", so both follow the guardrail (P1).
- The physics wording in the solutions follows the Finnish text: the model $U = E - R_\text{int} I$, the intercept and slope reading, the cable heating that goes with $I^2$, the estimate from the rated lamp resistances, and the s2 b power balance (16.7 + 8.3 + 5.0 = 30 W). I found no sentence where the translation changes a condition, a cause or a claim.
- Units, significant-figure statements and rounding reasons match the Finnish set. practice.py check: OK.
- Hash 5e15e967d1274d52 (practice.py hash FY6 --lang en), the same at the start and the end.
