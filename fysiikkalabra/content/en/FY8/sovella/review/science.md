VERDICT: PASS
CONTENT-HASH: 3f80e0d04abbed1e

## Blocking
None.

## Polish
- s3 d: "can no longer distinguish" is borderline at about $2.7\sigma$; $36\,\text{cm}$ is extrapolated; accept both $0.23$ and $0.27\,\mu\text{Sv/h}$ (carried from round 2).

## Checked
- Round 3, delta only. Hash 3f80e0d04abbed1e at the start and the end.
- `git diff eeea213043` over content/{fi,en,fi-easy}/FY8/sovella and lessons/FY8/sovella, without review/ files: the only change is one line in solutions.md, the fy8-s3 a table header. `$Rr^2\ (10^{3}\,\text{cm}^2/\text{min})$` became `$Rr^2\ (10^{3}\,\tfrac{\text{cm}^2}{\text{min}})$`. The unit is the same ($10^3\,\text{cm}^2/\text{min}$), and it is still correct for $R$ in $1/\text{min}$ times $r^2$ in $\text{cm}^2$. The table values are unchanged. answers.py, tasks.json and the rubrics are unchanged.
- The round-2 judgement stands for everything else.
