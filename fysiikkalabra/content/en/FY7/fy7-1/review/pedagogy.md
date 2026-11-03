VERDICT: FAIL
CONTENT-HASH: 509c09404476f503

## Blocking
- inquiry.json:129,141,200,212 (also `"magneetti"` keys at 137, 208) — untranslated Finnish shown to the student: the "Initial state / Kept constant" box of both experiments reads "magneetti: north pole towards the east, Earth's field: mukana" (exp-1) and "Earth's field: pois" (exp-2), and the keep-constant list says "magneetti" (shots #49, #55). The English reader gets an unintelligible parameter name and value — fix: names `"magneetti": "magnet"`; values `"1": "on"` and `"0": "off"` (the sim's own selects already say "on").

## Polish
- inquiry.json (exp-1 conclusion, johtopaatos) / lesson.md Key idea — the main finding of experiment 1, that a magnet's field drops about tenfold when the distance doubles (faster than 1/r²) because the two poles nearly cancel, is never stated in the theory or the Summary; it appears only in feedback and solutions. Add one sentence to "The poles of a magnet" or the Summary, so the Tutki result is consolidated.
- inquiry.json:johtopaatos prompt asks "why the effect weakens", but the criteria and model answer explain only that the Earth's field takes over, not why the magnet's field falls; either reword the prompt ("what the needle does farther away") or add a pole-cancellation criterion.
- inquiry.json:prior — prerequisites are listed as none in the slot, yet the lesson needs vector addition and tan/sin/cos (FY4/FY6 chapters). The optional "kertaus" covers only the Pythagorean sum; add a one-line trig reminder at "Combining magnetic fields".
- Workload: more than an hour if the optional items are done; the inclination components go beyond the slot goals, consider making them optional.

## Checked
- Opening question answered (hook, reflect); concepts taught before use.
- Predictions are arguable, refutable by exp-1 and exp-2; no option feedback discloses the answer before reveal; options carry misconception-repairing feedback.
- Variable control: exp-1 locks φ, magnet, Earth; exp-2 locks r, magnet, Earth; model values (30.0, 9.1, 2.9 µT; 65°, 33°, 12°) agree with the formulas.
- Worked example is 7 staged steps; numbers verified (17.9 µT, 22.7 µT); siirto (37.6°) and its three wrong values (55.0, 59.0, 52.4) are real mistakes.
- check-2 figure is needed, description gives the same data without naming the poles; check-1 and check-3 test the polar/domain concepts, criteria observable.
- Figures legible at 390 and 1280 px; sim and readout usable on a phone.
- Exit ticket tests direction of field, units, no-crossing; answers correct.
- Exercise set is judged in exercises/review/pedagogy.md.
