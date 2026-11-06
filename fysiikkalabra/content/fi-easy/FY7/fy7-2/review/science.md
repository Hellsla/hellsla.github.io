VERDICT: PASS
CONTENT-HASH: 36f1e76b61ba6c02

Delta re-review. Only figures.json gained four entries (descriptions of the exercise option figures `fy7-2/pick-*`, force diagram of the electron, field into the page); lesson.md, inquiry.json and exit-ticket.json are unchanged since the earlier PASS.

## Blocking

None.

## Polish
- lesson.md:275 — "Säde on kääntäen verrannollinen varaukseen ja kenttään" → "varauksen suuruuteen $|q|$ ja kenttään", to match $r = mv/(|q|B)$.
- inquiry.json `pohdi`, `tarkistus-4`, `siirto` keep $r = mv:(qB)$ and $qvB$ for positive ions only (correct); "(positiivinen ioni, $|q| = q$)" would match the lesson's convention.

## Checked
- Diff read: the 18 earlier figures.json entries are byte-identical; the four new keys are used only by exercises/exercises.json (grep: no `pick-` in lesson.md, inquiry.json or exit-ticket.json), so the lesson's text and figures are unaffected.
- Rendered the lesson (fi-easy, `screenshot.py fy7-2 --lang fi-easy --if-stale`): the formula diagrams (force on positive/negative particle, circular path with tangent velocity and central force, r(v) graph 10.4/20.9 cm, mass spectrometer with selector, direction-of-force check) show the same physics as before and as the descriptions say; the three photos are unchanged.
- Earlier recomputations (proton 3.2e-14 N, 5.2 cm, example 3.00e5 m/s, 20.0 u, Ne-22 27.4 cm, koe-2 24/48 fN, transfer 0.225 T, exit 3.0e5 m/s) carry over: no number or symbol changed.
- The new exercise descriptions themselves belong to the exercise-set review, not to this lesson review.
- Hash at start and end: 36f1e76b61ba6c02.
