VERDICT: PASS
CONTENT-HASH: 934ed52fd84979e7
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from 39cdae8624fc0e8c base b5600a6

## Blocking
- none

## Polish
- exercises/solutions.md:15 (and the other parallel chains) — the chain starts from "$\Sigma I = 0$" and then writes $I = I_1 + I_2$. That holds only with signed currents (in positive, out negative). The lesson's wording "the sum of the currents in equals the sum of the currents out" ($\Sigma I_\text{in} = \Sigma I_\text{out}$, as fy6-5 now writes it) would be the same law with no hidden sign convention (C, not blocking).
- exercises/solutions.md:110 — in display LaTeX, "$R_1 / 2$" could be $\tfrac{R_1}{2}$ like the rest of the chain (style).

## Checked
- Every new Formula chain in the diff derived again: the parallel sums from the current law plus $U = RI$ give $1/R = \sum 1/R_k$, the series chains from the voltage law give $R = R_1 + R_2$, the lamp resistor gives $R_\text{s} = (U - U_\text{L})/I$, the unknown branch $R_2 = U/(I - U/R_1)$, and the mixed circuit $I_3 = R_{23}U/(R_3(R_1 + R_{23}))$. Each final symbolic form matches the substitution below it.
- The quadratic chain $R_1(R_\text{s} - R_1) = R_\text{r}R_\text{s}$ leads to the right roots, 150 Ω and 100 Ω.
- Heater ratio: $R_\text{series} = 2R_1$ and $R_\text{parallel} = R_1/2$ give a ratio of 4, which is correct.
- One script recomputed all 19 answers and every intermediate number in the diff (24, 110 and 20 Ω, 4.787 mA, 35 Ω, 1.32 kΩ, 50 mA, 60, 102.1, 198 and 40.4 Ω, 36 mA, 463.8 Ω, 1.32 %, 500 mA). All agree with answers.py.
- The paragraph splits only re-cut the text. No number, sign or unit changed.
- exercises.json: only the "example data" marker was removed from the captions (teacher-approved), plus one reflow. The data and answers are unchanged.
- Notation and laws stay within FY6 (resistor connections, Kirchhoff's laws).
- Content hash checked at the start and at the end.
