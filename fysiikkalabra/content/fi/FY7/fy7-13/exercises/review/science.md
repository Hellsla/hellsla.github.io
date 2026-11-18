VERDICT: FAIL
CONTENT-HASH: a1006c29d32623aa

## Blocking
- solutions.md:75 (fy7-13-L2-03) — A: the rewritten Kaava lost the step that solves the grating equation for $d$. It lists $d\sin\theta = k\lambda$ and $d = 1\,\text{mm} : N$, then goes to $N = 1\,\text{mm} : d$, but the Sijoitus uses $d = \lambda : \sin\theta$, which the Kaava never writes. The old version had $d = k\lambda : \sin\theta$, so the rewrite removed the symbolic solving it was meant to add. Fix: add the rows $d = \dfrac{k\lambda}{\sin\theta}$ and $N = \dfrac{1\,\text{mm}}{d} = \dfrac{1\,\text{mm} \cdot \sin\theta}{k\lambda}$.

## Polish
- solutions.md:224 (L3-05) — $x = \dfrac{2x}{2}$ is still an identity row (as in the previous report); say in words that the maximum is half of the measured distance $2x$ from the hole.
- solutions.md:55, 142 — $k\lambda = d\sin\theta < d$ is right only because $\sin\theta < 1$ for a maximum that reaches the screen; that is already in the Periaate, so this is fine as it stands.

## Checked
- Delta: only Kaava steps rewritten as aligned blocks (L1-05, L1-06, L2-03, L2-04, L2-05, L2-06, L1-07, L1-08, L2-05 graph, L3-01, L3-04, L3-05, L1-10, L2-11, L2-12), plus paragraph splits; no number, answer, unit or tolerance changed.
- Every other rewritten Kaava starts from $d\sin\theta = k\lambda$ (with $d = 1\,\text{mm} : N$ and $\tan\theta = x : L$ where needed) and solves for the asked quantity; algebra right: $x = L\tan(\sin^{-1}(k\lambda/d))$, $\lambda_3 = 2\lambda_2/3$, $\lambda = ad$ from the slope, $N = \sin\theta/(k\lambda)$.
- Recomputed in one script: 16,28 cm, 595,5 lines/mm, 9,39 cm, 466,7 nm, 1,599 µm, 532,6 nm, 32,14°, $d/\lambda = 4{,}24$, 532,3 nm, 630 nm, 250 lines/mm: all unchanged and right.
- Split model answers keep every sentence and number.
- Hash a1006c29d32623aa at the start and at the end.
