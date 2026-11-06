VERDICT: PASS
CONTENT-HASH: d53a1ac4e99ef2e0

## Blocking

## Polish

## Checked
- Round 2: commit 4ff432a8f changed only the feedback of the Rivi 3 and Rivi 4 options of L2-08. exercises.json is the only fy5-2 file the commit touched; answers.py and solutions.md are unchanged.
- Rivi 3 feedback: the chain is now two short formulas, $160\,\text{N}\cdot 1{,}5\,\text{m} = 240\,\text{Nm}$ and $40\,\text{N}\cdot 1{,}0\,\text{m} = 40\,\text{Nm}$, with the total 280 Nm in words. The arithmetic is right and agrees with the student's row 3 and the solution. Each formula fits under 300 px by a text estimate (no render).
- Rivi 4 feedback (round-1 Polish fixed): it now names a mistake about row 4 itself, leaving the can's weight out of the sum because the can is outside support B. That mistake is coherent. Row 4, $N_\text{A} = G + G_\text{p} - N_\text{B} = 60\,\text{N}$, is correct with row 3's value, as the feedback says.
- There is still exactly one wrong row (row 2, $r_\text{p}$ should be 3,0 m). The correct values are $N_\text{B} = 180\,\text{N}$ and $N_\text{A} = 20\,\text{N}$, and the check about B sums to 0.
- answers.py was run again; its asserts pass and every answer is inside tolerance. The rest of the set is as in round 1 (PASS).
