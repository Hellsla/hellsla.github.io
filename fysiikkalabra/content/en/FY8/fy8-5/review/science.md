VERDICT: PASS
CONTENT-HASH: e43ea85aaa4a9edf

Follow-up review of the fix commit 2c31ff041 (delta from e6a225e13958a986, whose full review is kept below). Change: inquiry.json:6 `learn[1]`.

## Blocking

None.

## Polish
- inquiry.json:110 (sim lead, student-facing) and :3 contribution: "how random hits build up an orbital" — better "build up the picture of an orbital" (C).
- Common misconception and :217 criterion: "the boundary of an orbital is an agreed probability boundary" — "the boundary drawn in an orbital picture" would match the definition (C).
- Check 1: "usually 90 %" in the correct option would match the lesson's "chosen probability".

## Checked
- Earlier blocking item resolved: "interpret an orbital as a quantum state of the electron and its picture as a region inside which the electron is detected with a chosen probability" — matches Key idea (:274) and Summary (:1442).
- Consistency: grep of orbital definitions — no remaining sentence defines the orbital itself as the region; check 1 feedback ("An orbital is drawn as a probability boundary") speaks of the drawing.
- Definition: orbital = quantum state (allowed standing wave) that sets the detection probabilities; 90 % region an agreed illustration; consistent with Summary, the 2p remark, check 1 and check 4.
- Recomputed: example $1.889\,\text{eV}$, $656\,\text{nm}$; 1s 90 % radius $0.141\,\text{nm}$, most probable $0.053\,\text{nm}$; 2s peak $0.277$, 2p peak $0.212\,\text{nm}$, 90 % extents $0.483\,\text{nm}$; prediction 1 σ ≈ 0.95 pp; transfer 2700 (mistakes 5400, 3000); error item 18; check 3 $10.2\,\text{eV}$ (mistakes 17.0, 3.4). All agree with lesson-answers.py.
- Nodes, shell table, Pauli, filling order, C/N configurations, 3d→2p and 3s→2p: correct.
- Every choice has exactly one correct option; experiments lock all but the varied parameter; sim model box states the projection.
- Hash at start and end: 7406cfab104a02b5.

## Follow-up (uncommitted edit, hash 7406cfab104a02b5 → e43ea85aaa4a9edf)
- Change: inquiry.json:6 learn[1] shortened to "interpret an orbital as a quantum state of the electron and its picture as a region of chosen detection probability."
- Physics unchanged: the orbital is still the quantum state, and only its picture is the region; "region of chosen detection probability" is the same claim as the lesson's "a region inside which the electron is detected with a chosen probability" (lesson.md:1442), check 1 feedback (:321) and the explain criterion (:401). No new sentence defines the orbital itself as a region.
- Polish (C): the compressed phrase could be read as a region of equal probability density; the Summary and check 1 fix the meaning, so nothing is needed.
- No other diff in the hash. Blocking: none. Hash e43ea85aaa4a9edf at start and end.
