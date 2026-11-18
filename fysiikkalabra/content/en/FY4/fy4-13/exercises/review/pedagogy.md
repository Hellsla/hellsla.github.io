VERDICT: PASS
CONTENT-HASH: 9a55099de436c29c

## Blocking
(none)

## Polish
1. exercises/solutions.md:203 (pulley, force on the axle) — "For the wheel $\Sigma F = 0$, so, $F_\text{axle} - 2T = 0$" has a stray comma after "so"; write "so $F_\text{axle} - 2T = 0$, that is $F_\text{axle} = 2T$".
2. exercises/solutions.md (about fifteen Formula rows) — the identical lead "Newton's second law for each body separately, $\Sigma F = ma$, with the positive direction along the motion." is correct, but in the tasks where the positive direction is up (the crates on ropes) or where one body is at rest, say which direction is positive for that task instead of the generic phrase.
3. exercises/solutions.md (the first Formula rows, e.g. "$\Sigma F = ma$. $T = ma$") — a sentence ends in a formula and the next starts with one; join with "so" ("…, $\Sigma F = ma$, and with only the tension acting $T = ma$").

## Checked
- Delta: the Kaava rewrite only; numbers, answers, ids, tasks and tolerances unchanged.
- Every Formula now starts from Newton's second law ($\Sigma F = ma$, or $\Sigma F = 0$ at rest), then the equation of each body, then adding or eliminating to the last symbolic form; the Substitution rows were not touched and still use that form.
- The measured-data tasks derive $s = \tfrac12 at^2$ before $a = 2s/t^2$, and the slope task derives $a = \frac{g}{M}\Delta m$ before reading $g = kM$.
- Paragraph splits (Principle, free-body-diagram description, Model answers) give one idea per paragraph; the added sentences ($T < m_2 g$ for an accelerating hanging mass, the equal arrows in the coupling diagram) are correct physics and add no new data.
- exercises.json: the removal of the example-data marker from captions is the teacher's approved change (2026-11-15/16); no remaining marker found in the file.
- Captures: none opened (derivation/presentation rewrite judged from the diff).
