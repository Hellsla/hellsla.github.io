VERDICT: PASS
CONTENT-HASH: 8a721a86e7a34235
Round: 2 (commit 57a66480d changed only the new task fy6-2-L2-08; round-1 Polish item on 0,033 A is resolved: marked "välitulos, noin 0,03 A").

## Blocking

## Polish

## Checked
- Hash 8a721a86e7a34235 at start and end.
- answers.py run against exercises.json: all 16 numeric answers agree within tolerance (one python call).
- Changed 200 mA chain recomputed: 0,010 · 140 mA + 0,2 mA = 1,6 mA; 10 A range 0,0328 A ≈ 0,03 A; ratio about 20. Row 3 is still the only wrong line, and `answer` matches.
- The no-error option "Päättelyssä ei ole virhettä" and the task sentence now agree; its feedback no longer asserts an error, only points to the error-limit calculation, and stays correct physics.
- Reworded wrong-row feedback ("Jos pidät riviä virheellisenä, ajattelet ehkä …") keeps the same, correct reasons: ammeter in parallel → short circuit, start range vs final range, a reading that does not fit the 2 V range gives OL.
- The wrong row is still the lesson's warned mistake (largest range always best); everything used (Δx = p·x + n·r, OL, smallest fitting range) is taught in this lesson.
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 262 px, the changed chain 252 px, under 300 px. Page not rendered; the rest from text.
