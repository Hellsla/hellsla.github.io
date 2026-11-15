VERDICT: PASS
CONTENT-HASH: 672a5131cfaddc4d

## Blocking

## Polish
- solutions.md:210 (L3-04 c) — $5{,}8\,\%$ is the two-beam estimate $(0{,}19 + 0{,}05)^2$. With the multiple reflections it is $5{,}67\,\%$. The estimate is consistent with the amplitudes the text quotes (C). "noin $5{,}7\,\%$" or "noin $6\,\%$" would hold under both models.
- solutions.md L1-04 and L2-01 — The reasonableness checks cite the simulation's $103\,\text{nm}$ and the chapter's $200\,\text{nm}$ film. Both are arithmetically right but are not in the exercise brief. Check that the lesson still has them.

## Checked
- Round 2: the diff since round 1 is one sentence in L3-04 c (fi, fi-easy, en). The new claim is right: $5{,}8 : 2{,}0 = 2{,}9$ in the two-beam model and $5{,}67 : 2{,}006 = 2{,}8$ in the full formula, so "lähes kolminkertaisesti" holds. The fi-easy and en versions say the same. Hash identical at start and end.
- I recomputed all 18 numeric answers in one script with my own formulas: every one matches answers.py and exercises.json, and every unit and tolerance fits the data. For L2-05 and L3-05 I used least squares (slope $5{,}26$, giving $n = 1{,}315$; $\Delta x = 1{,}896\,\text{mm}$, giving $D = 12{,}42\,\mu\text{m}$). The answers in the solutions are inside the tolerances of $4\,\%$.
- L2-08: the cause of the residual reflection is correct. $|r_1| = 0{,}160$ and $|r_2| = 0{,}048$ are unequal because $1{,}38 > \sqrt{1{,}52}$. In the figure the minimum is $1{,}26\,\%$ at $497\,\text{nm}$ and bare glass is $4{,}26\,\%$, so $70{,}4\,\%$ is removed. The reading $1{,}3$ / $4{,}3$ gives $69{,}8\,\%$, inside $3\,\%$.
- L2-07: the table matches the Airy reflectance of a $97{,}83\,\text{nm}$ MgF₂ layer to every digit.
- L3-06 soap-curve: minimum at $465{,}5\,\text{nm}$, maximum at $620{,}7\,\text{nm}$, $R_\text{max} = 7{,}7\,\%$, as the solution reads. The figure does not give the thickness away.
- Phase-shift counting is right in every task: soap film, oil on water, MgF₂ (two shifts), TiO₂ on glass (one shift), and the air wedge (lower surface inverts, so the contact line is dark).
- L3-03 and L3-04: the visible orders and the $360\,\text{nm}$ thickness are right.
- L1-05: $\sqrt{n_\text{s}}$ is the equal-amplitude condition at normal incidence.
- L1-06 and L1-09: exactly one option is correct in each, and every distractor's feedback is right.
- Scope: every task stays inside FY7's light interference and the brief, at normal incidence. Every solution solves symbolically before substituting.
