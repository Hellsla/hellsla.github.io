VERDICT: PASS
CONTENT-HASH: 90f7ef37fb4a112f

## Blocking
None.

## Polish
- s3 b: also mark the point $(2{,}0;\ 1{,}86)$ in the figure; s3 d: say that $36\,\text{cm}$ is extrapolated; s5 d: criteria 3 and 4 overlap (carried from round 2).

## Checked
- Round 3, delta only. Hash 90f7ef37fb4a112f at the start and the end.
- `git diff eeea213043` over content/{fi,en,fi-easy}/FY8/sovella and lessons/FY8/sovella, without review/ files: the only change is one line in solutions.md, the fy8-s3 a table header. `$Rr^2\ (10^{3}\,\text{cm}^2/\text{min})$` became `$Rr^2\ (10^{3}\,\tfrac{\text{cm}^2}{\text{min}})$`. The unit is the same ($10^3\,\text{cm}^2/\text{min}$), and it is still correct for $R$ in $1/\text{min}$ times $r^2$ in $\text{cm}^2$. The table values are unchanged. answers.py, tasks.json and the rubrics are unchanged.
- The round-2 judgement stands for everything else.
