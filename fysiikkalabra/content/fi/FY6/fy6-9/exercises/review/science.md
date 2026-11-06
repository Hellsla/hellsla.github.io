VERDICT: PASS
CONTENT-HASH: e5c2c0ca37639b87
Round: 3. Only the fy6-9-L1-09 solution changed since round 1 (commit 72e243f47): the unit lines now read "Lausekkeen X yksikkö on …", and UQ/t is set with \tfrac inline. The physics is unchanged.

## Blocking

## Polish
- solutions.md:156 (carried over) — "Lauseke UQ/t on latauksen keskimääräinen teho" is still not exact. The lesson teaches that the charger gives more energy than the battery stores (η < 100 %). Write "akkuun varastoitumisen keskimääräinen teho", as the option's own feedback already says.
- solutions.md:152 — the line uses \tfrac for UQ/t but \dfrac for Wh/h. Use \tfrac for both, so the inline line keeps one height.

## Checked
- Hash e5c2c0ca37639b87 (the same as the packet) at start and end.
- Lines 148–154: each unit is still right. Q is Ah (charge), UQ is V·Ah = Wh (energy), UQ/t is W (power), UQt is Wh·h. Exactly one option is an energy, and the solution still agrees with the options and their feedback.
- The new wording "Lausekkeen … yksikkö on …" is correct Finnish and has the same meaning as the old lines.
- answers.py and exercises.json are unchanged since round 1, where they had no mismatch.
- I checked the formulas from the text only; the change makes nothing wider than in round 1, so I measured nothing again.
