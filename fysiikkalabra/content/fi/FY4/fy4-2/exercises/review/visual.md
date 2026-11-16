VERDICT: PASS
CONTENT-HASH: 5e71c2281827700a

## Blocking
None.

## Polish
- [Minor] exercises.json task text, capture fi-390-03 #4 and #13 — the punctuation after the lifted student calculation is not drawn into the formula's last row: "`. Syvyys on`" and "`, kun suunta ylöspäin on positiivinen.`" starts the next line alone (390 and 1280 px). Fix: let the build attach trailing punctuation in a task `text` as it already does in solutions and feedback, or put it inside the last row (`…\end{aligned}$$` → `… .` / `, \end{aligned}$$`). No new review round needed.

## Checked
- batch delta review: re-broken chains in solutions.md/exercises.json (reflow only); opened fi-390-02, fi-390-03, fi-390-04 and fi-1280-02; rows break at relations/operators, equals signs aligned, nothing clipped, sentence around each lifted formula reads naturally.
