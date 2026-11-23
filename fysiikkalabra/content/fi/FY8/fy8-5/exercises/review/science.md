VERDICT: PASS
CONTENT-HASH: 5a2a6d8880fe81c5
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography from 599e18e38085bad0 base 64d4935

## Blocking

## Polish
- exercises/solutions.md (the orbital-boundary counting tasks) — the new probability symbol $P$ ($P_\text{ulko}$, $P = p_{90} - p_{50}$) adds a second name for what the data calls $p$. Writing $k = (1 - p)N$ straight from "the expected count is the probability times $N$" would need no new symbol.

## Checked
- Hash 5a2a6d8880fe81c5 at the start and the end. `git diff 64d4935`: only solutions.md changed (Kaava blocks, split paragraphs). exercises.json, answers.py and figures.py are unchanged. The teacher-figure category concerns no line I judge.
- Ionisation from $n = 3$: $E_3 + E_\text{i} = 0$ and $E_3 = -\tfrac{13{,}6\,\text{eV}}{9}$ give $E_\text{i} = 1{,}51\,\text{eV}$. This is right.
- Shell counting: $N_n = 2n^2$ gives $N_\text{ulko} = N - 2 - 8$. This is right for the configuration the task gives.
- The transition blocks ($E_\text{f} = hf$, $c = f\lambda$, $E_\text{f} = \Delta E$) end at the same formulas as before.
- Balmer fit: $E_\text{f} = E_n - E_2 = 13{,}6\,\text{eV}\left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)$, so the slope against $\tfrac{1}{4} - \tfrac{1}{n^2}$ is $13{,}6\,\text{eV}$. This is right.
- String: $L = m\tfrac{\lambda}{2}$ and $v = f\lambda$ give $40\,\text{Hz}$, $80\,\text{Hz}$ and $120\,\text{Hz}$, unchanged.
- Na: $\tfrac{hc}{2{,}10\,\text{eV}} = 590\,\text{nm}$ and $\tfrac{hc}{5{,}14\,\text{eV}} = 241\,\text{nm}$. Both recomputed.
- The split paragraphs (orbital not an orbit, the 90 % boundary, shielding) keep every claim.
