VERDICT: FAIL
CONTENT-HASH: ed31b144d397cb3e

Pedagogy review of fy14-inside-iter (2026-11-01). Built and tested in Playwright over HTTP at 390 and 1280 px:
- `pred-heat` and `pred-gain` lock on commit with no feedback;
- `pred-heat` opens at `theory-machine`, `pred-gain` at `theory-gain`;
- all 3 model answers stay closed until the student writes;
- the explorer works at 390 px;
- no console errors and no `.katex-error`.

## Blocking
1. **`pred-gain` is answered before it is asked.**
   - The learning goal shown above the predictions, "explain why scientific gain is **not electricity** or commercial viability", rules out the 500 MW and 450 MW options.
   - The prior unit has already taught that "ITER makes no electricity" (fy14-iter-project `find-error`, `check-1`), and this unit lists it as prior knowledge.
   - So the prediction tests recall, not reasoning.
   - Fix, two parts:
     - (a) Reword the goal as "compare the fusion gain $Q$ with the electricity a power plant would produce, and explain what else commercial viability needs".
     - (b) Replace the question with one the student can argue about and that the bar chart answers. For example: "Suppose ITER had turbines that turn one third of its 500 MW of heat into electricity. Would it send net electricity to the grid?" Options: yes, about 450 MW / yes, about 170 MW / about break-even / no, it would still use more than it makes. The text and the chart (170 MW < over 300 MW) reveal the answer.

## Polish
2. `pred-heat` names parts the student has not met yet (divertor, cryostat), so it is a guess. Add a short function to each option, for example "the divertor, where the plasma edge is led onto the wall at the bottom" or "the cryostat, the outer vacuum tank". Do not add wording that points to the answer.
3. `pair-gain` criterion 3: "so it needs more than $Q > 1$" is garbled. Write "so it needs a $Q$ far above 1".
4. Workload: in one lesson the student does the 13-part explorer, the worked example, a 7-step numeric task, a theory summary of about 1,000 words and 4 checks. That is at the limit. `teacher.md` already makes the *Fuel* reading homework when time is short. Consider marking `theory-fuel` + `tritium` as the default homework.

## Checked
- The worked example is staged in 7 steps and the numeric solution is complete.
- The mistake feedback in `tritium` covers the per-second error, the deuterium mass and a unit slip.
- Checks 1–3 target real misconceptions: breakeven vs ignition, inverted and added ratios, gain vs viability. The correct option is not the longest.
- The brief's list is covered: magnets, central solenoid, vessel, heating, divertor, tritium cycle, radiation protection, $Q$, $Q = 1$, $Q = 10$, gain vs electricity, gain vs commercial viability.
- Word bank and sentence starters are given for the pair task and `check-explain`.
- The French corner is present.

## Shared issues
- None new. The `file:` captures of data components are already reported.
