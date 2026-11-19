VERDICT: FAIL
CONTENT-HASH: 7567454d13d89d12

## Blocking
- content/en/FY1/fy1-3/inquiry.json:545 (check-2 solution, Answer) — A: the new rounding "$2.1\,\%$, two significant figures, because the data has three" contradicts the lesson's own rule and has no basis. lesson.md:454 and :586 round the error estimate to one figure (two only if its first figure is 1), and the worked example (lesson.md:544) gives the relative uncertainty "two significant figures like the error estimate". Here the error estimate is $0.05\,\text{s}$, one figure, first figure 5, so the lesson's rule gives $2\,\%$. The reason given is also not a valid rule: three-figure data would mean three figures by the house rule, not two, and the limiting datum of $\Delta t/\bar t$ is $\Delta t$ (from the difference $0.10\,\text{s}$), not the raw times. The same sentence is in content/fi/FY1/fy1-3/inquiry.json:545 ("koska lähtöarvoissa on kolme"). — Fix: go back to "$2\,\%$, one significant figure like the error estimate $0.05\,\text{s}$ (calculator value $2.08\,\%$)" in every language. If the change was made so that $2$ passes the answer check, widen `tolerance` (answer 2.08) so a student's $2$ is accepted, and leave the physics alone.

## Polish

## Checked
- Recomputed: mean 2.40 s, half range 0.05 s, ε = 2.083 %; substitution and calculator value are correct.
- Rounding rule checked against lesson.md:454, :544 and :586 (en and fi): the old answer, 2 %, follows it and the new one does not.
- Content hash 7567454d13d89d12 at the start and at the end.
