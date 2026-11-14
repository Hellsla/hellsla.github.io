VERDICT: PASS
CONTENT-HASH: 7c8b70ef0c8025aa
SCOPE: delta added-exercise from 0c40b39a97046bfa base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- solutions.md fy6-10-L2-09 (Reading the graph) — "about 0.06 mN over the fifth grid line" claims a precision a 1 mN grid cannot give (the solution itself says ±0.1 mN) — say "about 5.0–5.1 mN" and substitute 5.1 mN, or say 5.06 mN is the model value at the marked point.

## Checked
- Delta: only L1-09, L2-09, L2-10 judged; the rest unchanged per `reviews.py added_exercises`.
- L1-09: Coulomb's law between point charges; recomputed with MAFY k = 8.98755·10⁹: F = 0.2247 mN (lesson's k gives the same to 4 figures); answers.py 0.224689. The 2-sf answer 0.22 mN is 2.1 % off but is a correctly rounded value, which the page's check always accepts (half-unit rule). Repulsion stated correctly.
- L2-09: figures.py curve is k(30 nC)²/r²; at 4.0 cm F = 5.056 mN; q = r√(F/k) = 30.0 nC (answers.py 30.0126). Readings 5.0 / 5.1 / 5.5 mN give 29.8 / 30.1 / 31.3 nC, inside the 5 % tolerance. The point at 4.0 cm is drawn; the description gives the reading, not the charge.
- L2-10: figures.py A = 20·20 nC², B = 20·80 nC²; F_A(3.0 cm) = F_B(6.0 cm) = 3.995 mN, both on grid lines; q_B = q_A(r_B/r_A)² = 80 nC (answers.py 80.0); readings r_B = 5.9–6.1 cm give 77–83 nC, inside the 6 % tolerance. Same-sign condition stated in the task; k and the common 20 nC cancel correctly.
- Both curves stay inside the axes (A at 2.9 cm 4.27 mN, B at 4.4 cm 7.43 mN < 8 mN); "B above A everywhere" true since q_B > 20 nC.
- Solutions complete: symbolic solving before substitution, conversions, rounding reasons, real reasonableness checks (reverse calculation).
- Scope: Coulomb's law, FY6 central content; units nC/mN appropriate.
