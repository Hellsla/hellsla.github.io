VERDICT: FAIL
CONTENT-HASH: 8e99d0c59ea3fbba

Pedagogy review of fy14-sun-puzzle (2026-11-01). Page built with `python3 scripts/build.py fy14-sun-puzzle` and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, and there are no console errors and no raw `$`.

## Blocking
1. `inquiry.json` `review` (stage *Think about it*, before the predictions): the feedback of the correct option says "Right: the missing mass left as energy, $E = \Delta m \cdot c^2$. Today you see why this solved one of the great puzzles of the 19th century."
   - The hook has just named that puzzle: what keeps the Sun shining.
   - So the page tells the student that the mass defect is the answer, one screen before `pred-models` asks "Which of these explanations could keep the Sun shining for billions of years?".
   - The prediction is no longer open (developer brief: "any component placed before a prediction must not show or state its answer").
   - Fix: end the feedback after the first sentence, or replace the second with a neutral one such as "Keep this in mind for later in the lesson."

## Polish
2. `inquiry.json` `find-error`: the correct option (59 characters) is 34 % longer than the longest distractor (44). Shorten it to "Only $0.7\ \%$ of the fused mass becomes energy." or lengthen a distractor.
3. `inquiry.json` `check-explain` model: it writes $E = mc^2$, while the unit uses $E = \Delta m \cdot c^2$ throughout. Use the same form, because the point of the lesson is that only the *lost* mass becomes energy.
4. `inquiry.json` `check-2` and `check-3`: both are calculations, and `check-3` (twice the fuel, twice the time) is very easy. Consider making `check-3` test an assumption in both directions. For example: "The core started with only about $70\ \%$ hydrogen. How does this change the estimate?" Use distractors for "longer" and "no change".

## Shared issues
None found for this unit.

## Checked
- Predictions:
  - `pred-coal` and `pred-models` lock on commit with no feedback.
  - They open with `theory-candidates` and `theory-key`.
  - `pred-coal` is tested by the student's own calculation (`power-data`, 5350 years).
- The hero (rock layers, fossil, Sun) and the Why line give nothing away.
- The model answers of `kelvin-debate` and `check-explain` stay closed until the student writes.
- The staged worked example has all seven stages and states its assumptions.
- The historical investigation works well: data → primary source → ordering the story → a pair discussion about conflicting evidence. This is a genuine source-based inquiry.
- Theory is about 510 words.
- Word bank and sentence starters at both writing tasks.
- The French corner compares *u* with the Finnish *y*.
- `teacher.md` is realistic, and it has plans for fast pairs and for running out of time.
