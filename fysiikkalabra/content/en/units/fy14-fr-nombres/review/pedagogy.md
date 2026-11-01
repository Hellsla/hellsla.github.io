VERDICT: PASS
CONTENT-HASH: 205540ba7c16d868

Pedagogy re-review of fy14-fr-nombres (2026-11-01), after "Fixes after review" in review/developer.md. Built with `python3 scripts/build.py`, tested in Playwright at 390 px over HTTP (port 8781).

## Earlier findings
1. **Resolved: pair listening is now real.**
   - Tables A and B use `say` with `"hide": true`. With a French voice available, the page shows only *Show the text* and the *Listen* buttons; the French, the meaning and the respelling stay hidden.
   - The instruction tells the listener not to open the text before *Check*.
   - Item B5 (84 €) is now in `fx-match-heardA`.
2. **Resolved: the feedback maths renders correctly.** I answered every item wrong in `match-numbers`, both listening matches and the receipt gap fill. No raw `$` and no KaTeX errors.
3. **Resolved: option length in `notice`.** The correct option is shortened to 28 characters, against 29–36.

## Blocking
None.

## Polish
1. When the browser has no French voice, `say` shows the text, and teacher.md says the speaker then reads aloud. The listener's own device then still shows the lines. Add one line to teacher.md: in that case, the listener closes the page or uses only the speaker's device.

## Checked
- **Predictions:**
  - Both predictions lock on commit, with no feedback.
  - They stay closed through Investigate.
  - Each opens with its own theory section.
- **Model answers:** all 3 `explain` tasks stay closed when empty and at 3 characters; they open after a real answer.
- **Errors:** no console errors and no `.katex-error`.
- **Progression:** the unit follows on from the pilot.
- **Pair work:** the market role-play has a real information gap.
- **Timing:** the 75-minute plan adds up, with plans for fast pairs and for running out of time.
- **Option lengths:** balanced.

## Shared issues
- None.
