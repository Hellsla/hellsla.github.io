VERDICT: PASS
CONTENT-HASH: c4613f28acbcb79a

Pedagogy review of fy14-secret-fusion (2026-11-01). I built the page and tested it in Playwright at 390 px. Both predictions lock when the student commits and show no feedback. `pred-secret` opens at `theory-war` and `pred-zeta` at `theory-zeta`. Model answers stay closed until the student writes. No console errors, no raw `$`.

## Blocking
None.

## Polish
1. **Engagement, `pred-zeta` / `theory-zeta`.** The best story in the unit is revealed by reading, not by evidence the student works with. Add a small data `interpret` before `theory-zeta`: neutron counts forward and backward along the tube, with the current one way and then reversed (for example 70/30 and then 30/70). Let the student conclude, and reveal `pred-zeta` after that task. This turns the reading into an investigation the student does.
2. **`inquiry.json` `pred-secret`.** The prompt asks for "the most important reason". The correct option gives only the neutron reason, but the reading and the Key idea put the weapons physics first. Change the correct option to cover both, for example "It was too close to bomb physics and bomb fuel." Keep it within ±30 % of the distractors' length.
3. **`sort-claims`.** The item "A fusion device makes neutrons that could be used to make bomb fuel." → *motive* labels a physical fact as a motive. Rewrite it as "Governments fear that fusion neutrons could make bomb fuel."
4. **Workload, `teacher.md` 64–75 min.** Three checks, the transfer paragraph, the summary and the French corner do not fit in 11 minutes. In the time plan, move the transfer task (`check-write`) to homework, or drop `find-error` from the class plan.
5. **Option lengths.** The correct option is now the shortest in `pred-secret`, `check-1` and `check-3`. Lengthen one correct option so that the shortest option is not a reliable clue.

## Checked
The Why line and the hero (a fence and a padlock) do not answer either prediction. The jigsaw has a role for each of the four, a word bank and sentence starters, and every explain task has starters. The biographies are optional. The numeric task has a full model solution with mistake feedback. `teacher.md` has plans for fast pairs and for running short of time. The French tips compare with Finnish *y*. The unit covers the brief's 1920s–1950s points: Richter, the pinches, Spitzer, Tamm and Sakharov, ZETA and Geneva 1958.

## Shared issues
- `scripts/inquiry.py:376` puts the `pair` note *after* the textarea, and places `<div class="wordbank">` inside `<p class="task">`, which is invalid HTML. Render the pair note before the textarea and use a `div` for the task. `writing-guide.md` §1 says "there is no `pair` field", but the renderer supports one: update the guide.
- No photographs yet (the photo pass). The chapter needs them to be as engaging as the brief asks.
