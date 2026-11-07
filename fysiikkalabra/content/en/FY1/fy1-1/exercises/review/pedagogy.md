VERDICT: PASS
CONTENT-HASH: 67937b6a1bd4a758
Mode: delta (over the PASS at 4392cc6a514de0b2)
Round: 1

## Blocking
(none)

## Polish
- solutions.md L1-04 Reasonableness — the new text recomputes the same quotient (3.5/1.4 · 10^4) and calls it reasonable: that checks nothing. Restore an independent check, for example: "The orders of magnitude are 10^-10 m and 10^-14 m, four steps, so the ratio should be about 10^4; 2.5·10^4 is close."
- solutions.md L1-08 Answer — the new three sentences ("about ten thousand", "exactly 10^4 but does not determine the real ratio", "four steps, not four times") say the same thing twice; keep the first and the last.
- solutions.md L3-05 Conversions — the AU conversion is now only implied ("both distances are expressed in AU") and done inside the Substitution line; add "1 AU = 1.496·10^8 km" under Conversions so the student sees the step.

## Checked
- L1-06: the situation now names the conditions ("in air, from the same height at the same time"); the question is last and the observation is unambiguous; feedback ties each wrong option to the range of validity.
- L1-09: "approximately equally large" removes the false exactness; the rewritten fourth feedback explains why the assumption would fail, in plain steps (factor 400 against 39 000, a hundredth of the apparent size).
- L2-05 and L2-06: AU defined in the task; "size" replaces "diameter", which fits a human and the Milky Way; the data and the solution agree.
- figures.json description of the axis figure now gives five orders of magnitude per interval without giving any exercise answer.
- Rest of the set unchanged since the last PASS; levels 9/7/5 meet the minimums 5/4/3; solutions at 1280 px (#68, #87–#92) are followable and nothing is clipped.
