VERDICT: PASS
CONTENT-HASH: 07ff0780b71756eb
Round: 1 (YO-skill task)

Scope: the new task L1-09 (true/false statements, added 2026-11-05). The other 20 tasks and answers.py are unchanged since the round-2 PASS (`git show HEAD`).

## Blocking
- none

## Polish
- solutions.md L1-09 Periaate, "Eristetyssä sylinterissä $Q = 0$". The glossary's *eristetty systeemi* also excludes work, but here $W = 60\,\text{J}$. Fix: write "Lämpöeristetyssä sylinterissä", as the task text does.

## Checked
- I recomputed ΔU = Q + W = 0 + 60 J = 60 J with my own script. Statements 1 and 2 are true and 3–5 false, and the answer string matches the flags.
- The conditions are stated in the task. There is no heat exchange with the surroundings, and the air stays a gas, so a rise in U means a rise in T. The air is the system, and the work is done on it, so W > 0. The cylinder does not move, so ΔU = Q + W holds as written.
- The distractors catch the lesson's own warned mistakes. Statement 5 ("enemmän lämpöä") is the "heat is stored" mistake, statement 4 is "only heating changes U", and statement 3 confuses W with Q. Every feedback is correct and agrees with the glossary.
- The correct statements cannot be spotted by form. True and false statements are of similar length, and none is hedged.
- The task stays within fy3-5 (the first law and its signs).
- Inline formulas: the longest is $\Delta U = Q + W = 0 + 60\,\text{J} = 60\,\text{J}$, about 200 px, so it fits 300 px.
- Renders: I viewed review/shots/fy3-5-open-exercises-1280-9.png, taken after the commit. Statements 3–5 and the solution render cleanly. I judged statements 1–2 and all the feedback from the text only, and I checked no 390 px render of the solution.
- The hash was the same at the start and at the end.
