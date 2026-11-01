VERDICT: PASS
CONTENT-HASH: d2bb84b94122e667

Pedagogy re-review of fy14-fr-cafe (2026-11-01), after "Fixes after review" in review/developer.md. Built with `python3 scripts/build.py`, tested in Playwright at 390 px over HTTP (port 8781).

## Earlier findings
1. **Resolved: `pred-bill` is no longer given away.**
   - The `think` model and its criteria no longer mention the bill or paying.
   - Learn goal 3 now reads "pay, thank and hold a whole café conversation", which does not name asking for the bill.
   - `pred-bill` is reframed ("finished ten minutes ago, the waiter has not brought the bill"). Its four options are 32–37 characters, so the correct one is not the longest.
2. **Resolved: the role cards are private.**
   - The four cards are separate closed boxes, *Customer only* and *Waiter only*.
   - The surprise starters (*je ne mange pas de viande*, *il n'y a plus de …*) are on the cards, not in the shared box.
   - The **Reacts** criterion can now be met honestly.
3. **Resolved: `check-1` options are balanced.**

## Blocking
None.

## Polish
None.

## Checked
- **Predictions:**
  - Both predictions lock on commit, with no feedback.
  - They stay closed through Investigate.
  - Each opens with its own theory section.
- **Model answers:** all 3 `explain` tasks stay closed when empty and at 3 characters; they open after a real answer.
- **Errors:** no console errors and no `.katex-error`.
- **Speaking support:** support fades from the dialogue, through cues, to private role cards.
- **Prices:** every total matches the menu.
- **Timing:** the 75-minute plan adds up.

## Shared issues
- None.

## Re-check 2026-11-01: photographs
Edited: the café photo sat between the lead-in sentence and its numbered list of steps; moved it directly under the heading. Caption is simple English and fits the topic. No lesson ids, no ×, British spelling.
