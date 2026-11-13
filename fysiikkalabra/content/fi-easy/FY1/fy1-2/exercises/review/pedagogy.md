VERDICT: PASS
CONTENT-HASH: 06e2bb3f719a5f7d

## Blocking

## Polish
- solutions.md (fy1-2-L1-10, Vastaus) — the lesson's rule gives as many figures as the least precise factor (here four), so the solution has to justify the departure; it does, but by a physical caveat. Consider one plain sentence: "Pyöristetään kolmeen merkitsevään numeroon, koska etäisyys on keskiarvo eikä tarkka matka."
- exercises.json fy1-2-L1-10 — the Moon light-travel time still repeats fy1-1-L1-07 (earlier note, optional).

## Checked
- Diff only: answer 1.282 -> 1.28 in exercises.json, solutions.md and answers.py (round(...,2)); all three agree.
- 3,844e8 / 2,998e8 = 1,282 s, so 1,28 s is the correct rounding to three significant figures.
- Tolerance 0.04 (about 3 %) accepts both 1,28 and a student's unrounded 1,282; no student answer is wrongly refused.
- The solution keeps all steps: formula, conversion km -> m, substitution showing 1,282 s ≈ 1,28 s, sanity check.
- The task text is unchanged (situation, formula, conversion hint, question last), so earlier findings still hold.
- The teacher's decision for three significant figures is recorded in the solution with a reason.
- Hash at start and end: 06e2bb3f719a5f7d.
