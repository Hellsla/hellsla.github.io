VERDICT: PASS
CONTENT-HASH: dfd86936dde13656

Pedagogy re-review of fy14-fr-cadarache (2026-11-01), after "Fixes after review" in review/developer.md. Built with `python3 scripts/build.py`, tested in Playwright at 390 px over HTTP (port 8781).

## Earlier findings
1. **Resolved: `pred-who` is now arguable.** The prompt asks the student to use the names as clues and to give a reason, and `justify` is on.
2. **Resolved: the role cards are private.** Cards A–D are separate closed boxes: *Visitor only*, *Receptionist only* and *Researcher only*.
3. **Still open, Polish: the CEA/CNRS section is still fact-dense.** It is acceptable. The detail sits in the theory, the timing allows 12 minutes, and the running-out-of-time plan says to read the culture quickly.

## Blocking
None.

## Polish
None new.

## Checked
- **Predictions:**
  - Both predictions lock on commit, with no feedback.
  - They stay closed through Investigate.
  - Each opens with its own theory section.
- **Model answers:** all 3 `explain` tasks stay closed when empty and at 3 characters; they open after a real answer.
- **Errors:** no console errors and no `.katex-error`.
- **Option lengths:** balanced. The correct option is never the longest.
- **Timing:** the 75-minute plan adds up.
- **Direction check:** a second pair follows the directions on the plan.

## Shared issues
- None.

## Re-check 2026-11-01: photographs
ITER-from-a-distance photo ends the CEA/ITER section and gives a real view before the Provence section; the caption answers none of the ITER checks. No lesson ids, no ×, British spelling.
