VERDICT: PASS
CONTENT-HASH: c4613d821092c131

## Blocking

## Polish
- My earlier polish items (lesson.md:209 long straight wires, check-1 feedback wording, lesson-answers.py:39 comment) are untouched by this diff and still stand.

## Checked
- Delta review against my PASS at 304ecd496a987db8: the only change (commit c85fdffb) is inquiry.json:255, the "Etsi virhe" prompt, whose aligned product row is split so that "\quad \cdot 0,866" stands on its own row. No number, symbol or unit changed.
- The split rows still read as one product: F = I l B cos 30° = 5,0 A · 0,20 m · 0,30 T · 0,866 ≈ 0,26 N. I recomputed it: 5,0 · 0,20 · 0,30 · 0,866 = 0,2598 N → 0,26 N, the student's intended (wrong-model) result. The correct value with sin 30° is 0,15 N. Both agree with the options and the feedback I passed.
- The deliberate error (cos in place of sin, angle between wire and field) is unchanged, so the item still has exactly one correct option.
- Hash fy7-4 at start and end: c4613d821092c131 (unchanged).
