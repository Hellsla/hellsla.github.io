VERDICT: PASS
CONTENT-HASH: a06061f1b4a8852f
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography,wording from 04d9947faaf13eb6 base 64d4935

## Blocking

## Polish
- exercises/solutions.md (L2, $\lambda_\text{max}$) — the block goes from $\lambda_\text{max} = \tfrac{c}{f_\text{min}}$ straight to $\tfrac{hc}{\Delta E_\text{min}}$. Add the row $f_\text{min} = \tfrac{\Delta E_\text{min}}{h}$.
- exercises/solutions.md (L3-03) — $E_2$ means the second photon's energy here, but in the rest of the chapter $E_2$ is an energy level. A name like $E_\text{f,2}$ avoids the clash.

## Checked
- Hash a06061f1b4a8852f at the start and the end. `git diff 64d4935`: solutions.md has new Kaava blocks and split paragraphs. exercises.json only drops ", esimerkkiaineisto" from five table captions. answers.py is unchanged.
- The captions without the provenance word follow the house rule. The tables are still clearly a task's data: the Hg and H lines are real values, and the model atom is named as a model.
- The derivations are right: $hf = \Delta E$ with $c = f\lambda$ gives $\lambda = \tfrac{hc}{\Delta E}$; ionisation from level 2 gives $hf = 0 - E_2$; absorption gives $E_\text{y} = E_2 + \tfrac{hc}{\lambda}$.
- Fluorescence: $p = \tfrac{Q}{E_\text{abs}} = 1 - \tfrac{E_\text{fl}}{E_\text{abs}} = 1 - \tfrac{\lambda_\text{abs}}{\lambda_\text{fl}}$ is right.
- Violet and green lines from the same upper level: $E_\text{viol} - E_\text{vihr} = E_\text{a,vihr} - E_\text{a,viol}$ follows from the two emission equations.
- The six-line task: $E_1 = E_3 - (E_3 - E_1)$ and $\lambda_6 = \tfrac{hc}{E_1} = 1127\,\text{nm}$ are unchanged.
- The split paragraphs keep every claim and number.
