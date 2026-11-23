VERDICT: PASS
CONTENT-HASH: cf7a8a854854967f
SCOPE: delta wording from 424e9d97bbd2962e base a2442fe

## Blocking

## Polish
- content/en/FY6/fy6-5/exercises/solutions.md:200 — a full stop is still missing after "$630\,\text{V}\,\Omega$", before "The denominator".

## Checked
- Hash cf7a8a854854967f at the start and at the end.
- The delta is one row in fy6-5-L1-02. The opening $\Sigma U = 0$ is now $\sum \Delta V = 0$, which is how the lesson writes the voltage law. The rest of the chain, $U - U_1 - U_2 = 0$ and $U_2 = U - U_1$, is unchanged and correct.
- L1-02 recomputed: $12.0\,\text{V} - 4.5\,\text{V} = 7.5\,\text{V}$. This agrees with answers.py.
- L3-04 Formula (line 198) matches the Finnish version:
  - the loop rows $R_1 I_1 + R_2 I_2 = U_1$ and $R_3 I_3 + R_2 I_2 = U_2$ follow from $\sum \Delta V = 0$, as the Principle states;
  - the node-equation substitution gives $I_2 = (U_1R_3 + U_2R_1) : D$, which is correct.
- L3-04 recomputed: $I_2 = 0.30$ A, $I_1 = 0.20$ A, $I_3 = 0.10$ A; the energy balance is 3.3 W = 3.3 W.
