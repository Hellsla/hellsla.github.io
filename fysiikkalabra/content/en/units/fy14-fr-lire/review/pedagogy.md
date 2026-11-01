VERDICT: PASS
CONTENT-HASH: f5bc3f119dc791ac

Pedagogy re-review of fy14-fr-lire (2026-11-01), after "Fixes after review" in review/developer.md. Built with `python3 scripts/build.py`, tested in Playwright at 390 px over HTTP (port 8781).

## Earlier findings
1. **Resolved: `pred-gist` is no longer answered on the opening screen.**
   - The opening question is now open: "How much of a French news text about fusion can you understand after a few weeks of French?"
   - Learn goal 1 reads "find information in a short French news text".
   - Neither states the correct option any more. The prompt says "about 200 words".
2. **Resolved: French speaking.** A `read-aloud` `say` task with four sentences from the article asks pairs to read aloud and to compare how the look-alikes sound.
3. **Still open, Polish: option lengths.** In `pred-actuel` and `check-1`, the correct option is still the longest, by 1–2 characters. This is harmless.

## Blocking
None.

## Polish
1. The timing in teacher.md does not yet place the new read-aloud task. Give it about 4 minutes, for example taken from the 48–58 summary slot, and add it to the running-out-of-time plan.

## Checked
- **Predictions:**
  - Both predictions lock on commit, with no feedback.
  - They stay closed through Investigate.
  - Each opens with its own theory section.
- **Model answers:** all 4 `explain` tasks stay closed when empty and at 3 characters; they open after a real answer.
- **Errors:** no console errors and no `.katex-error`.
- **Progression:** the unit builds on the Cadarache and numbers units.
- **Writing:** the summary and transfer tasks have models and criteria.

## Shared issues
- None.
