VERDICT: PASS
CONTENT-HASH: c17d5c9f35598a17
SCOPE: delta md-paragraphs,numbers,typography from 44f3a0f5513f3d73 base 64d4935

## Blocking

## Polish
- exercises/solutions.md (the Å task, line ~293) — the Kaava step is still one inline chain while every other one is an aligned block. This is form, not physics.

## Checked
- Hash c17d5c9f35598a17 at the start and the end. `git diff 64d4935`: only solutions.md changed (Kaava blocks and split paragraphs). exercises.json and answers.py are unchanged.
- The transition blocks are right: each starts from $hf = E_\text{y} - E_\text{a}$ and $c = f\lambda$ and ends at the same formula as before ($\lambda = \tfrac{hc}{E_5 - E_2}$, $E_n = E_2 + \tfrac{hc}{\lambda}$, $n = \sqrt{\tfrac{13{,}6\,\text{eV}}{-E_n}}$, $E_\text{k} = \tfrac{hc}{\lambda} - E_\text{ion}$).
- L2-05: from $hf = E_n - E_2$ with $E_n = -\tfrac{E_\text{ion}}{n^2}$, I get $f = \tfrac{E_\text{ion}}{4h} - \tfrac{E_\text{ion}}{h}\cdot\tfrac{1}{n^2}$. The slope against $\tfrac{1}{n^2}$ is $-\tfrac{E_\text{ion}}{h}$, so $E_\text{ion} = -hk$, as the Periaate says.
- Ionisation from level $m$: $hf_\text{ion} = 0 - E_m$ with $E_m = -\tfrac{13{,}6\,\text{eV}}{m^2}$ gives $f_\text{ion} = \tfrac{13{,}6\,\text{eV}}{m^2 h}$. This is right.
- The Lyman source: $\lambda_\text{L} = \tfrac{hc}{E_\text{y} - E_1} = 97{,}25\,\text{nm}$ is unchanged.
- The split paragraphs keep every claim and number. The Bohr model and the $n^2$ misconception text are unchanged.
