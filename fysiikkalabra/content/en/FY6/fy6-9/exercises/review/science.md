VERDICT: PASS
CONTENT-HASH: 750761aac39f869c
SCOPE: delta caption-label,md-paragraphs,numbers,typography,wording from ccb98e9a17ea30ff base 5b3ca4f

## Blocking
- none

## Polish
- none

## Checked
- The charging chains start from the voltage law, $U_\text{ch} - RI - R_\text{s}I - E = 0$, with the right signs for charging (the charger drives current against $E$), and solve for $I$, $R_\text{s}$ and $R_\text{tot}$ correctly. In the graph task the slope reading $k = 1/R_\text{tot}$ follows from the rewritten linear form $I = U_\text{ch}/R_\text{tot} - E/R_\text{tot}$.
- Discharge with two currents: $E = U_\text{avg} + R_\text{s}I$ is the right terminal-voltage relation for discharge. Equating it for the two currents gives $R_\text{s} = (U_1 - U_2)/(I_2 - I_1) = 0.10\,\Omega$ and $E = 3.75\,\text{V}$, which I recomputed.
- Energy chains: $W = UQ$, $W = Pt$, $\eta = W_\text{batt}/W_\text{ch}$, the losses $W_\text{loss} = W_\text{ch} - W_\text{batt} = (U_\text{ch} - E)It = 1.5\,\text{Wh}$ and the heating $P = UI$ with $U = R_\text{s}I$ giving $R_\text{s}I^2$. All are correct.
- Recomputed with my own formulas: e-bike $t = UQ/P = 4.2\,\text{h}$, car battery $t = 2.105 + 2.353 + 2.667 = 7.125\,\text{h}$, and the step-wise energy sum. All agree with answers.py.
- The reasonableness checks that were cut from the end of a paragraph (kettle, 87.5 %, $0.25\,\Omega$ check) are still there as their own paragraphs.
- exercises.json: only "example data" was removed from four captions. The data are unchanged.
- The energy wording follows the guardrail ("becomes internal energy"). All content is inside FY6 (batteries and charging circuit).
- Content hash checked at the start and at the end.
