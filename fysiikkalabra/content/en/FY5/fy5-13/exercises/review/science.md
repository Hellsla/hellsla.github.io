VERDICT: FAIL
CONTENT-HASH: e4bb9305f0b020d0

## Blocking
- exercises.json fy5-13-L2-02, solutions.md `## fy5-13-L2-02` — **B**. The task presents a resonance-tube measurement and takes the first resonance length as exactly $\tfrac{\lambda}{4}$, but neither the task nor the solution says that the end correction is neglected. L2-06 in the same set shows that the first length is about $0.45\,\text{cm}$ short, a 1–2 % effect that falls in the third figure of the "three significant figures" answer. The check also gets the cause backwards: "comparing two resonances … eliminates the end correction, which makes the shortest air column slightly shorter". The end correction, not the comparison, shortens the column.
  - Fix: add "Ignore the end correction of the tube." to the task and say the same in the Principle.
  - Rewrite the check: the antinode lies slightly above the mouth, so the column is a little shorter than $\tfrac{\lambda}{4}$ and the result is slightly too small; using two resonances removes this error.

## Polish
- solutions.md fy5-13-L3-02 — the reason for three figures should be that the frequencies are given to the nearest hertz, not that "$110$ has three digits".

## Checked
- One script recomputed all 19 numeric answers from the task text with my own formulas. Each one agrees with exercises.json and answers.py.
- The models are right:
  - $v/(2L)$ for strings and open tubes, $v/(4L)$ with odd $n$ for closed tubes.
  - Successive resonances differ by $f_1$ on a string (L3-02) and by $2f_1$ in a closed tube (L3-03).
  - In L2-06, $L_3 - L_1 = \lambda$, and part b) gives $e = 0.45\,\text{cm}$ with the right cause.
- Figure `kuvio-tehtava` is to scale, with four loops, five nodes and a ruler from 0 to 1.20 m. It gives L2-04 ($60.0\,\text{m/s}$) and L2-09 ($31.25\,\text{Hz}$) their data without the answer.
- L1-06, L1-07, L2-07 and L2-08: exactly one correct option each, and every distractor's feedback is right.
- L3-04: tests $f_1^2/F$ correctly and flags the extrapolation.
- L3-05: identifies the tubes from the 1:2:3 and 1:3:5 ratios and gets $331\,\text{m/s}$.
- L1-09: the MAFY-based values and the helium-voice remark are correct.
- Rounding reasons hold: L2-01 is $5.4\,\text{Hz}$ from the $7.0\,\text{m/s}$ difference; L1-08 and L1-09 have two figures.
- Scope is FY5 only.
- Hash unchanged at the end.
