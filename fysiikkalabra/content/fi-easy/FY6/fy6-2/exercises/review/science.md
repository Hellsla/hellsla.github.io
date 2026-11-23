VERDICT: PASS
CONTENT-HASH: 9e36ae77fccc1465
SCOPE: delta wording from e0d944a8c7421a99 base 0e8231e

## Blocking

## Polish
- solutions.md:25, :175, :187 — the symbol $s$ still means three things: the relative error limit, the half-range scatter estimate and the relative decrease. Fix: use distinct symbols, or name each one in words in its row.

## Checked
- Hash at the start and at the end: 9e36ae77fccc1465, unchanged.
- The diff removes only the labels $\Sigma U = 0$ and $\Sigma I = 0$ in L2-04 and L3-04. My previous polish item is resolved, and no number or other symbol changed.
- L2-04 now starts from $U_\text{paristo} = U_\text{m} + U_\text{lamppu}$. This is the basic equation the Periaate says in words. The chain with $I \approx 0$ is right.
- L3-04: the rows $U_0 = U_1 + U$ and $I_1 = I_2 + I_\text{m}$ are justified in words in the Periaate. The derivation to $U = U_0 / (1 + R_1/R_2 + R_1/R_\text{m})$ is right.
- Recomputed: $5{,}714\,\text{V}$, $4{,}76\,\%$ and $0{,}0486\,\text{V}$. All three agree with the solution.
