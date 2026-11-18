VERDICT: PASS
CONTENT-HASH: 15261a26498e83ce
SCOPE: delta (unit notation 1/min -> min⁻¹, paragraph splits in solutions.md)

## Blocking

## Polish
- exercises/solutions.md (fy8-12-L1-07, Järkevyys) — the edited sentence now has $\text{min}^{-1}$ for the rates per minute but keeps $\tfrac{1}{\text{s}}$ for the rates per second ($27$, $1{,}5$). The values are correct, but the two notations sit in one sentence. For consistency it could use $\text{s}^{-1}$.
- exercises/solutions.md (L2-09 / tuntematon solutions) — these keep "pulssia/min" where L1-07 and L3-02 now use $\text{min}^{-1}$. This is physically equivalent and not an error. Optionally unify the notation.

## Checked
- The hash was 15261a26498e83ce at the start and the end.
- I compared the whole diff word for word after mapping $\tfrac{1}{\text{min}}$ to $\text{min}^{-1}$ and collapsing whitespace. The old and new texts are identical. The only changes are the unit notation and blank lines or paragraph splits, so no number, formula, sign or claim changed.
- exercises.json L1-07 (line 80) and L2-09 (line 339) now have the unit `min⁻¹`. It is the same dimension as 1/min, so it is a correct unit for a count rate. The task text of L1-07 asks for the same unit.
- I recomputed the answers myself. L1-07: $1215/0{,}75\,\text{min} - 90\,\text{min}^{-1} = 1530\,\text{min}^{-1}$, which matches the stored 1530. L2-09: $800\cdot(1/2)^{30/12} = 141{,}42$, which matches the stored 141,4. Their tolerances are unchanged.
- I also recomputed the solutions touched by the reflow: L3-02 gives $34{,}99\,\text{mm}$, so 35 mm. L1-01 gives $18{,}90\,\%$. The tuntematon thickness gives $67{,}73\,\text{mm}$, rounded up to 68 mm on the safe side. All three agree with the solutions.
- answers.py is unchanged, and its comments agree with the new unit.
- The paragraph splits in L3 model answers (shield comparison, beta/gamma identification, RIVM a/c/d, attenuation data d, photon interactions) keep each causal step intact and in order.
