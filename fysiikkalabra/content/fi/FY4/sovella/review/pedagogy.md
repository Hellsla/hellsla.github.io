VERDICT: PASS
CONTENT-HASH: 2978c7bdbfea8fbf

Round 2 (delta review of the diff since round 1, which was PASS).

## Blocking
None.

## Polish
1. s2 d: the solution's "Mitoitus" paragraph says the brake is sized by the larger estimate, 14 m/s, while the rubric also accepts 17,2 m/s. Both are safe conclusions, but one sentence in the solution that says "or the frictionless limit 17,2 m/s is also correct" would show a student why a different answer still earns the point.
2. s2 c and d: after the rounding, the c-part and d-part solutions say "liian suuri" about 14 m/s. The margin between 13,6 and 14 is trivial, so the argument is unaffected; no change needed.
3. Round-1 polish items 3 to 7 still stand and are optional (s1 c answer field is wax A's value, s2 has no picture, s3 d is a recall item, s3 is the heaviest at 16 points). The coverage table (item 1 of round 1) should be regenerated with `python scripts/coverage.py FY4` before merging.

## Checked
- s2 geometry: the new wording (15,0 m and 180 m from the start platform to the start of the brake, and the nearly horizontal wire from the brake onwards) removes the ambiguity of "loppupää". It reads clearly, and the zero level "jarrun alkukohta, jossa nopeus mitattiin" in b matches it. The student can now see why h and s refer to the same stretch where the speed was measured.
- s2 numbers: v = 17,2 m/s is about 62 km/h, which is above the instructor's 60 km/h; 29 N; 14 m/s (13,6 unrounded). In c the "Annettu" line now gives the work 5234 J, so a student who rounded b to 29 N is not misled. The "Hyväksytään myös" section shows that 29 N gives 5220 J and 13,6 m/s again (answers.py: 13,58), so it is consistent.
- Rounding to 14 m/s: two significant figures follow from m, F_vast and the other givens, and the reason is stated in the solution and the rubric. Tolerance 0,05 covers 13,3 to 14,7, so 13,6 and 14 both pass. Rewarding the unrounded 13,6 is fair, and the point is not lost for extra digits.
- s2 d rubric: accepting both the 14 m/s sizing and the 17,2 m/s upper bound is fair, since both rest on "prepare for too large rather than too small". The point still requires a justification, so no free point.
- s3 b: same rounding (14 m/s, 13,6 accepted, 13,5 to 14 m/s tolerance). The conclusion "yli 40 km/h" holds for either value. Fair.
- s1 b: the sentence explaining the dashed G_x and G_y as auxiliary components, not extra forces, closes round 1 polish item 2. It also tells the student not to draw them, which is consistent with the "components counted twice" common mistake.
- Nothing in the changes names a model or formula in a prompt; independence and variety are unchanged.
- practice.py check: OK. Hash recomputed at the end: 2978c7bdbfea8fbf.
