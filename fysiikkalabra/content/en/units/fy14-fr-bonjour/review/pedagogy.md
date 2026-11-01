VERDICT: PASS
CONTENT-HASH: edd56ca7362d855c

Pedagogy re-review of fy14-fr-bonjour (2026-11-01), after the "Fixes after review" in review/developer.md. Page rebuilt with `python3 scripts/build.py fy14-fr-bonjour` and tested in Playwright at 390 px.

## Earlier findings: all resolved
- Old Blocking 1 is resolved:
  - `pred-greet` is now the evening hotel case (Bonsoir, monsieur), with `reveal` after `theory-tuvous`.
  - The hero has empty speech bubbles, and its aria-label gives no words.
  - Neither the hook nor the Why line answers the prediction.
- Prediction behaviour in the browser:
  - `pred-greet` and `pred-name` lock on commit with no feedback.
  - Both stay closed while the student scrolls through Investigate.
  - Both open with the committed option's feedback once *Tu or vous?* is on screen.
- Polish 2–8 are done:
  - balanced options in `notice`, `check-3` and `pred-name`;
  - `check-1` is now a transfer to *vous* for a group;
  - a `back-to-predictions` reflection asks for the answer to the Why question;
  - the French slips are fixed (*à*/*de*, the ordering hint, the *il* tip, *tu* questions with intonation, *Je vais bien* in the *vous* column);
  - the nested span is removed;
  - the timing in `teacher.md` is realistic, with check 4 as homework and a plan for running out of time;
  - the `pred-name` prompt is accurate.
- Sentence starters were also added for the Think about it pair task.
- No console errors.

## Polish (not blocking)
1. `check-3`: the correct option is still the longest, by one character (42 against 37–41). This is harmless. Elsewhere there is no length pattern.
2. Shared files, not this unit:
   - the reflection list says "You predicted: … — the data does not support …". For a language unit, a word such as "the theory" or "the evidence" would fit better than "data".
   - the missing space between the scenario and the question in `templates/inquiry.js` is already noted in developer.md.
