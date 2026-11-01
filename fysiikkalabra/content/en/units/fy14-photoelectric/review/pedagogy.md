VERDICT: PASS
CONTENT-HASH: 32f7650573683cf9

Pedagogy re-review of fy14-photoelectric (2026-11-01), after the "Fixes after review" in review/developer.md. Page rebuilt with `python3 scripts/build.py fy14-photoelectric` and tested in Playwright at 390 px.

## Earlier findings: all resolved
- Old Blocking 1 is resolved. `pred-red` has been replaced by `pred-stop` (stopping voltage from 500 to 300 nm), and nothing on the page before it answers it. The hook, the Why line and the hero compare red with violet only. In the browser, `pred-stop` locks on commit with no feedback, stays closed after 2 rows of `exp-stop`, and opens at row 3 with the committed option's feedback. The model values match the feedback: at 300 nm the current is still 0.14 nA at 1.76 V and reaches 0 at 1.78 V.
- The old red-light question is now a pair discussion (`hook-discuss`) with sentence starters, a model answer and criteria. Its model answer stays closed until the student has written something.
- Polish 2–7 are done:
  - the `find-error` options are balanced;
  - `check-explain-help` gives sentence starters for the last task;
  - the biographies are optional;
  - the French corner uses the Finnish *y* and a nasal, linked *un électron*, in one respelling style shared with fy14-fr-bonjour;
  - the simulation's model box says the model has no time axis;
  - `teacher.md` has plans for fast pairs and for running out of time.
- No console errors.

## Polish (not blocking)
1. `inquiry.json`, answer lengths: the correct option is now the longest (often by only a few characters) in 5 of 8 choices: `review`, `pred-bright` (tied), `find-error`, `check-1` and `check-3`. A student who always picks the longest option still scores well. Shorten two of them, for example `check-1` to "Only the dim ultraviolet one, at once." and `review` to "Each packet is larger.", or lengthen one distractor in each.
2. `inquiry.json` `hook-discuss` model answer: it presents the "pieces of light" idea as the answer before the student predicts with `pred-stop`. This is acceptable as hypothesis → prediction → test. It would be better to show it as one of two ideas, adding a second model sentence in the spirit of the wave model ("Or maybe violet light simply carries more energy per second …"), so that the prediction stays open.
3. Shared file, not this unit: the reflection list in `templates/inquiry.js` joins the scenario and the question without a space. This is already noted in developer.md.
