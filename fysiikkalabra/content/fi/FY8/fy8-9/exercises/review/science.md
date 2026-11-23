VERDICT: PASS
CONTENT-HASH: b05067dea6428416
SCOPE: delta (work queue 8g, Kaava steps of the model solutions)

## Blocking

## Polish
- solutions.md (L2-05, L2-06, L3-02, L3-03) — a display block is followed directly by ", missä …" or ", kun $A_0$ supistuu", so the comma opens a new line on the page. This is layout and language, not physics.

## Checked
- `git diff a7ec649ae6`: only solutions.md changed (13 Kaava fields). exercises.json, answers.py and figures.py are unchanged, so the answers and tolerances are the ones passed before.
- I compared every field with whitespace normalised. Nothing changed outside the Kaava fields.
- L1-03 and L2-01: the derivation goes from $N = N_0e^{-\lambda t}$ with $N = N_0/2$ at $t = T_{1/2}$ to $\lambda T_{1/2} = \ln 2$. It is correct and within the scope note (both forms of the law).
- L1-08, L2-05, L3-01, L3-02, L2-09: the step from $(\tfrac12)^{t/T}$ to $\ln(X_0/X) = \tfrac{t}{T}\ln 2$ is correct. L2-05 and L2-09 keep the background subtracted ($R$ net, $y - B$).
- L2-02 $N = AT_{1/2}/\ln 2$ is correct. L2-04: $m = N m_\text{ydin}$ makes $m \propto N$ explicit, which is correct. L2-06 $R(2T_{1/2}) = R_0/4$ is correct.
- L3-03: the equal initial activities $A_0$ cancel, as before. L3-04: two-time ratio of component 2, correct.
- L3-05: $\lambda_\text{eff} = \lambda_\text{fys} + \lambda_\text{bio}$ gives $1/T_\text{bio} = 1/T_\text{eff} - 1/T_\text{fys}$. This is correct; the old text had stated it as a difference.
- The substitutions are unchanged, and each uses the last symbolic form.
- The hash was b05067dea6428416 at the start and at the end.
