VERDICT: PASS
CONTENT-HASH: 30e34ca50690ea4b
SCOPE: delta md-paragraphs,numbers,reflow,typography from c55461f4fa2a8ea8 base 64d4935

## Blocking

## Polish
- exercises/solutions.md (L1-10, raja-aallonpituus) — the Kaava block goes from $f_0 = \tfrac{c}{\lambda_0}$ straight to $\lambda_0 = \tfrac{hc}{W}$. Add the row $\tfrac{hc}{\lambda_0} = W$ as the L2-01 block does.
- exercises/solutions.md (L3-03) — the row $E = E_1 + k(f - f_1)$ uses a bare $E$ where the first row has $E_\text{k,max}$. Use one symbol.
- Earlier polish items (the ±10 nm reading accuracy in L2-10, the source of 544 nm, the answers.py comment) are still open. They were not part of this change.

## Checked
- Hash 30e34ca50690ea4b at the start and the end. The diff was read on disk with `git diff 64d4935`. Only solutions.md changed: the Kaava steps became aligned derivations, and some paragraphs were split. exercises.json and answers.py are unchanged.
- Every new Kaava block starts from a basic law ($E = hf$, $c = f\lambda$, $hf = W + E_\text{k,max}$, $P = NE$, $I = N_\text{e}e$, $E_\text{k} = \tfrac{1}{2}mv^2$, $P = IA$, $E = Pt$). Each derives the same final formula as before, and each step is algebraically right.
- L2-05: $U_\text{s} = \tfrac{h}{e}f - \tfrac{W}{e}$, so the slope is $\tfrac{h}{e}$. L2-07: the slope equals $h$ in eV/Hz, and $W = hf_0 = kf_0$. Both are right.
- L3-04 and L3-05: the photon, electron and current relations are right, and $\eta$ and $I$ follow from them.
- One script recomputed 13 answers with my own formulas. All of them match answers.py to five significant figures.
- The split paragraphs keep every claim and number word for word.
