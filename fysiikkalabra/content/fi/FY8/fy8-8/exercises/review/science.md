VERDICT: PASS
CONTENT-HASH: ac689ba1a6a22e54
SCOPE: delta (work queue 8g, Kaava steps of the model solutions)

## Blocking

## Polish
- The round-1 polish items (the reasons for the figure counts in L3-06 and L2-09) are still open. They were not part of this change.

## Checked
- `git diff a7ec649ae6`: only solutions.md changed. exercises.json and answers.py are unchanged, so the answers and tolerances are the ones passed before.
- I compared every field with whitespace normalised. Only the Kaava fields of L1-04, L2-01, L2-03, L3-02, L3-05 and L3-06 changed. All other differences are paragraph splits.
- Each block starts from $E_\gamma = hf$ and $c = f\lambda$, where needed from the level difference $E_\gamma = E_\text{y} - E_\text{a}$, and derives $\lambda = hc/E_\gamma$. This matches the lesson's formula and symbols.
- L2-03: the ratio $E_\gamma/E_\text{v} = E_\gamma\lambda/(hc)$ is correct. L3-02: $\lambda_\text{min} = hc/E_\text{max}$ is correctly tied to the largest energy.
- L3-06: the level sums $E_\text{B} = E_\text{A} + E_{\text{B}\to\text{A}}$ and $E_\text{C} = E_\text{B} + E_{\text{C}\to\text{B}}$ are correct, and $\lambda = c/f = hc/E_\text{C}$ is correct. The substitution is unchanged (0,49487 pm).
- The hash was ac689ba1a6a22e54 at the start and at the end.
