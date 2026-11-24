VERDICT: PASS
CONTENT-HASH: 704b4f14fe8576b4
SCOPE: delta answers,comments,numbers,reflow,structure,teacher-figure,typography,wording from 2dbe4b29223aeaef base 8f23aa7

## Blocking

## Polish
- solutions.md fy7-10-L2-09 Answer — "accurate to about $0.2^\circ$" understates the effect of reading the line: a reading uncertainty of $\pm 0.005$ in each of the two $\sin\alpha_1$ values gives $\Delta k \approx 0.02$ and about $\pm 0.3^\circ$ in $\alpha_2$ (the fitted line itself gives $k = 1.49$, $\alpha_2 = 22.6^\circ$). The same wording is in the Finnish set. Fix: "about $0.3^\circ$", or drop the figure. This does not affect the answer check: the $3\,\%$ tolerance accepts both $22.5^\circ$ and $22.6^\circ$.
- Figure `fy7-10/fit` description — it gives no values of the line, so a reader who cannot see the figure cannot do L2-09. This is a property of the shared figure, not of this delta.

## Checked
- Hash `704b4f14fe8576b4` identical at start and end.
- New L1-09: air to water at $52.0^\circ$, MAFY $n = 1.333$: $\alpha_2 = 36.239^\circ$ recomputed = answer `36.2391`; tolerance $0.02$ fits three figures; the solution is complete and correct, and its reasonableness check is a real one.
- New L2-09: I re-ran the least-squares fit from `FIT_A1`/`FIT_A2`: $k = 1.4895$, $b = -0.004$, the line at $0.20$ gives $0.294$ and at $0.60$ gives $0.890$ (answers.py comment correct). Reading $0.30$ and $0.90$ is fair at a $0.1$ grid; $n = 1.50$ gives $\alpha_2 = 22.481^\circ$ = answer. It reads the slope from line points, not raw points (guardrail), and acrylic $1.49$ is a sound table value.
- answers.py: both new lines compute the physics in the task text; the outputs match exercises.json.
- en and fi: ids, answers, tolerances, figure and lookup of both new tasks identical; the en solutions translate the fi ones faithfully, with the same numbers.
- Formula chains re-derived: plastic $n_2 = n_1\sin\alpha_1/\sin\alpha_2$, $v = c/n_2$ ($1.4986$, $2.002\cdot10^{8}\,\text{m/s}$); $\Delta t = (n-1)d/c = 34.67\,\text{ps}$; $\sin\alpha_2 = v_2\sin\alpha_1/v_1$ ($34.249^\circ$); $\lambda = \lambda_0/n = 416.4\,\text{nm}$ (with $v_0 \approx c$ stated in the Principle); apparent depth $\alpha_1 = \arctan(h'\tan\alpha_2/d)$, $n = n_2\sin\alpha_2/\sin\alpha_1$. All correct, with numbers unchanged.
- The "(example data)" caption was removed from both tables, as the house rule says (no provenance badge); none of this data is presented as a real source.
- The protractor figure (teacher-approved) still shows $\alpha_1 = 50^\circ$ and $\alpha_2 = 30^\circ$ as the task needs.
