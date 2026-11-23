VERDICT: PASS
CONTENT-HASH: a55f5a63698fbd03
SCOPE: delta md-paragraphs,numbers,reflow,typography from 2d131b382d63c27b base 64d4935

## Blocking

## Polish
- exercises/solutions.md (the single-photon double-slit task, line ~297) — the block uses $\tfrac{N}{t}$ as the photon rate and then $t = \tfrac{5000}{r}$ as the total time. The symbol $t$ means two things. Writing $\dot N$ or $t_\text{mittaus}$ would separate them. This clash was there before the change.

## Checked
- Hash a55f5a63698fbd03 at the start and the end. `git diff 64d4935`: only solutions.md changed (Kaava blocks and split paragraphs). exercises.json and answers.py are unchanged.
- Compton energy balance: $hf = hf' + E_\text{k}$ with $f = \tfrac{c}{\lambda}$ and $f' = \tfrac{c}{\lambda'}$ gives $E_\text{k} = \tfrac{hc}{\lambda} - \tfrac{hc}{\lambda'}$ and $\lambda' = \tfrac{hc}{hc/\lambda - E_\text{k}}$. Both are right.
- Photon rate: $P = \tfrac{N}{t}\,hf$ gives $\tfrac{N}{t} = \tfrac{P\lambda}{hc}$. The detection rate $r$, the time and the photon spacing $d = \tfrac{c}{N/t}$ are unchanged and right.
- The electron momentum by the cosine law and the share of $m_\text{e}c^2$ are unchanged.
- The split answers (the $\sqrt{n}$ scatter, single photons with no collisions, which-path information destroying the fringes) keep every claim.
