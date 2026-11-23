VERDICT: PASS
CONTENT-HASH: cdf30d1f28121f1a
SCOPE: delta numbers from 934ed52fd84979e7 base a2442fe

## Blocking
- none

## Polish
- content/en/FY6/fy6-4/exercises/solutions.md:110 — in display LaTeX, "$R_1 / 2$" could be $\tfrac{R_1}{2}$ like the rest of the chain (style).

## Checked
- Hash cdf30d1f28121f1a at the start and at the end.
- The delta only removes the "$\Sigma I = 0 \Rightarrow$" and "$\Sigma U = 0 \Rightarrow$" prefixes from the twelve Formula blocks. Each block now opens with the lesson's principle row ($I = I_1 + I_2$, $U = U_1 + U_2$, $U = R_1 I + R_{23} I$). My earlier Polish item about the hidden sign convention is therefore resolved, and the chapter no longer relies on Kirchhoff's laws.
- Every row that remains is unchanged algebra that I derived in the previous round. Each final symbolic form is still the one substituted below it. No Substitution, Answer or exercises.json number changed.
- answers.py (shared with fi) recomputed in one script with my own formulas: all 19 answers agree.
- No $\Sigma$ is left anywhere in solutions.md.
