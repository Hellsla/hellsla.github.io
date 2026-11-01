VERDICT: PASS
CONTENT-HASH: a079620513e19e92

Pedagogy re-review of fy14-fusion-society (2026-11-01) after commit 04ac2449. The page was rebuilt, served on port 8775 and tested in Playwright at 390 px.

## Earlier findings
- Polish 1 is resolved. The correct options of `find-error` (72), `check-1` (62) and `check-3` (57) are now no longer than their distractors. `pred-fuel` and `pred-waste` are still longer than the next option by one character, which is harmless.
- Polish 2 is resolved. `pred-waste` now says "Remember *Inside ITER*, or reason from the neutron".
- Polish 3 is resolved. The reflection has sentence starters.
- Polish 4 is resolved. The timing in `teacher.md` makes check 4 usually homework.

## Blocking
None.

## Polish
1. The society unit still contains the old prediction answers of the debate: ITER's cost and USD 4.48 billion in the *Uncertainties* section. This no longer matters, because the debate now predicts other facts. Keep it that way: the debate's new predictions (the public share of private money and the origin of Commonwealth Fusion Systems) must not be added to this unit.

## Checked
- In the browser, both predictions lock on *Answer* with no feedback and with the "read the theory section" message. They stay closed through Energy, the table, Claims and the sort. They open with the committed option's own feedback at *theory-main*.
- All four model answers stay closed with an empty answer and with 5 characters, and open after an answer of the student's own.
- CLIL: there is a word bank and sentence starters for every pair and writing task. The balanced evaluation task is intact.
- There are no console errors, no KaTeX errors, no raw `$` or `**`, and no horizontal scroll at 390 px.

## Shared issues
- The reflection says "the data does not support your prediction" for theory-revealed predictions. This is already known.
