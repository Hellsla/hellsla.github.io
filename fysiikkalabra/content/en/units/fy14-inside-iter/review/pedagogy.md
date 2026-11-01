VERDICT: PASS
CONTENT-HASH: 222bf8240799daec

Pedagogy re-review of fy14-inside-iter (2026-11-01) after the "Fixes after review" in review/developer.md (commit c6532e4f). Rebuilt, served over HTTP and tested in Playwright at 390 and 1280 px.

## Earlier findings
- **Old Blocking 1 is resolved.**
  - Learning goal 3 now reads "compare the fusion gain $Q$ with the electricity a power plant would produce …". It no longer answers the prediction.
  - `pred-gain` is a new question the student can argue about: would ITER with turbines that turn one third of the heat into electricity send net electricity to the grid?
  - It is answered by `theory-gain`: about 170 MW against a plant demand of 110–620 MW, shown in the rebuilt chart.
  - Every option has its own feedback, and the break-even distractor is handled honestly (170 MW > the 110 MW minimum, but < the 620 MW peaks, and nothing between pulses).
- **Polish 2–4 are done.**
  - `pred-heat` options give each part's function without hinting at the answer, and the correct option is not the longest.
  - The `pair-gain` criterion is fixed.
  - `teacher.md` makes the *Fuel* reading and the tritium task the default homework.
- Both predictions lock with no feedback. They open at `theory-machine` and `theory-gain`.
- All 3 model answers stay closed until the student writes.
- No console errors and no `.katex-error`.

## Polish (not blocking)
1. `pred-gain`: before the reveal, the student cannot know ITER's own power demand. The prompt could add one neutral sentence for the justification, such as "Think about what else the plant needs power for (magnets, cooling, heating systems)". This invites reasoning without giving a number.

## Re-check 2026-11-01: photographs
Poloidal field coil photo ends the parts list it illustrates; its caption matches the text ("shape the plasma and hold it in place") and adds no answer to the vocabulary match. No lesson ids, no ×, British spelling.
