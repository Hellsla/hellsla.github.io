VERDICT: PASS
CONTENT-HASH: 27dde45fa6e89ceb

## Blocking
None.

## Polish
- [Minor] exercises.json task text, capture fi-390-09 #3 — the punctuation after the lifted student calculation is not drawn into the formula's last row: a lone "`.`" starts the next line alone (390 and 1280 px). Fix: let the build attach trailing punctuation in a task `text` as it already does in solutions and feedback, or put it inside the last row (`…\end{aligned}$$` → `… . \end{aligned}$$`). No new review round needed.

## Checked
- batch delta review: re-broken chains in solutions.md/exercises.json (reflow only); opened fi-390-09, fi-390-10 (390 px only); rows break at relations/operators, equals signs aligned, nothing clipped, sentence around each lifted formula reads naturally.
