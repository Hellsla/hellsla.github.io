VERDICT: PASS
CONTENT-HASH: 67ed4e67f89dc96b
SCOPE: delta md-paragraphs,numbers,reflow,typography from bb52b416609e298b base 64d4935

## Blocking

## Polish
- solutions.md (L3-03) — the Kaava block writes $f_\text{valo} = c/\lambda$ but no row for $f_\text{q}$, which is given. That is correct, but one clause ("$f_\text{q}$ on annettu") would make it read as complete.

## Checked
- `git diff a7ec649ae6 -- exercises/ answers.py figures.py`: only solutions.md changed. exercises.json, answers.py and figures.py are unchanged, so the answers, units and tolerances are the ones passed before.
- I compared every solution field by field, with whitespace normalised: only the **Kaava** fields changed. Every other field differs only by blank-line paragraph splits.
- Every new Kaava block starts from $E = hf$ or $P = \tfrac{N}{t} \cdot hf$ and $f = \tfrac{c}{\lambda}$, as the lesson's *Kaava: Laserin fotonit* does. Then comes the derived form, and then the unknown is solved in symbols.
- I checked the algebra. L1-03 $\lambda = hc/(E_2-E_1)$. L2-01 $\eta = \lambda_\text{p}/\lambda_\text{L}$. L2-02 $N_\text{r}/N_\text{v} = \lambda_\text{r}/\lambda_\text{v}$. L2-04 $P = Nhc/(\lambda t)$. L3-02 $\tfrac{N_\text{v}}{t} = P\lambda_\text{p}/(2hc)$. L3-03 $c/(\lambda f_\text{q})$. L3-04 $\eta_\text{q} = P_\text{L}\lambda_\text{L}/(P_\text{p}\lambda_\text{p})$ and $P_\text{pak} = \tfrac{N_\text{L}}{t}(hf_\text{p} - hf_\text{L})$. L3-05: the ratio step $\tfrac{\Delta P_\text{L}}{\Delta P_\text{p}} = \tfrac{\Delta N_\text{L}}{\Delta N_\text{p}} \cdot \tfrac{\lambda_\text{p}}{\lambda_\text{L}}$ inverts correctly to $\cdot\,\lambda_\text{L}/\lambda_\text{p}$. L3-06 $P_\text{X}/P_\text{Y}$. All are correct.
- Each Sijoitus still substitutes into the last symbolic form of its Kaava block. The numbers are unchanged.
- Notation is the same as the lesson's ($E_2 - E_1$, $\tfrac{N}{t}$, $hf$).
- The hash was 67ed4e67f89dc96b at the start and at the end.
