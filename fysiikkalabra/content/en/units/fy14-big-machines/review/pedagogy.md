VERDICT: PASS
CONTENT-HASH: 01a45cca341ca829

Pedagogy re-review of fy14-big-machines (2026-11-01), after commit 3ed55db3. I rebuilt the page and tested it in Playwright at 390 px. `pred-heat` opens at `theory-heating` and `pred-budget` at `theory-oil` (the budget chart). Model answers stay closed until the student writes. No console errors.

## Earlier findings: all resolved
1. `learn[0]` no longer rules out a `pred-heat` distractor.
2. The Why line is now one question.
3. `machines` is now a real data task. The student reads the major and minor radius for each machine with its start year, and links the growth in size to "a bigger plasma keeps its heat longer" and to who could pay. The distractors (smaller with better magnets, same size, only the cost grew) each get feedback that sends the student back to the numbers.
4. The options of `review`, `pred-heat` and `check-1` are re-balanced.

## Blocking
None.

## Polish
1. `machines`: the feedback says JET's plasma volume is "more than twenty times PLT's". Ask the student to estimate this with $V \approx 2\pi R \cdot \pi a^2$ (the volume of a ring-shaped tube) as an optional extension, so that the claim is something the student checks, not reads.
