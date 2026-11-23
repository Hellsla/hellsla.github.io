VERDICT: PASS
CONTENT-HASH: 1d250e8158d4a046
SCOPE: delta wording from f57c156658def7ed base 0e8231e

## Blocking

## Polish
- solutions.md:25, :191, :209 — the symbol $s$ still means three things: the relative error limit (L1-03), the half-range estimate of scatter (L2-07) and the relative decrease (L3-04). Fix: use distinct symbols, or name each one in words in its row.
- solutions.md:85 — the L2-04 Kaava still uses $U_\text{lamppu} = R_\text{lamppu} I$. This is resistance notation that the brief's lesson does not teach. The Periaate already says it in words, so the row is acceptable as it stands.

## Checked
- Hash at the start and at the end: 1d250e8158d4a046, unchanged.
- The diff removes only the labels $\Sigma U = 0$ and $\Sigma I = 0$ in L2-04 and L3-04. No equation, number or symbol changed otherwise. The prior polish item on the Kirchhoff labels is resolved.
- L2-04 now opens with $U_\text{paristo} = U_\text{m} + U_\text{lamppu}$. This is the basic equation the Periaate states in words. The chain to $U_\text{m} \approx U_\text{paristo}$ with $I \approx 0$ is right.
- L3-04: the rows $U_0 = U_1 + U$ and $I_1 = I_2 + I_\text{m}$ are each justified in the Periaate in words: the same loop, and the current through $R_1$ is the sum. The derivation to $U = U_0 / (1 + R_1/R_2 + R_1/R_\text{m})$ is right.
- Recomputed: $U = 5{,}714\,\text{V}$, a decrease of $4{,}76\,\%$, and $\Delta U = 0{,}0486\,\text{V}$. All three agree with the solution.
