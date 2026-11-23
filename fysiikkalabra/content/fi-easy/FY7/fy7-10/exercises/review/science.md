VERDICT: PASS
CONTENT-HASH: 488bea21891a1bfc
SCOPE: delta answers,comments,md-paragraphs,numbers,reflow,structure,teacher-figure,typography,wording from 820217f747566fa9 base 8f23aa7

## Blocking

## Polish
- solutions.md:342 (L2-09 Kuvaajan lukeminen) — the fitted line of `fy7-10/fit` is at $\sin\alpha_1 = 0{,}294$ and $0{,}890$, but the solution reads $0{,}30$ and $0{,}90$ and then says the reading precision is $0{,}01$ — read $0{,}29$ and $0{,}89$ instead. The slope is $1{,}50$ either way, so the answer does not change.
- answers.py:356 — the comment gives the slope as $1{,}49$, but line 358 uses $1{,}50$, as the solution does. Say in the comment that the value read from the graph is $1{,}50$.

## Checked
- The diff showed the Kaava blocks flattened, so I read them on disk (solutions.md:65, 75, 116, 133, 187). Each is a correct aligned chain, simplified symbolically to the end: $n_2 = n_1\sin\alpha_1/\sin\alpha_2$ and $v = c/n_2$; $\Delta t = (n-1)d/c$; $\sin\alpha_2 = v_2\sin\alpha_1/v_1$; $\lambda = \lambda_0/n$ with $v_0 \approx c$ (stated); the apparent-depth chain via $\alpha_1 = \arctan(h'\tan\alpha_2/d)$.
- New L1-09 (MAFY lookup, water $1{,}333$): $\alpha_2 = 36{,}24^\circ$. It matches answers.py and the fi set, has 3 significant figures, and its check is a real one.
- New L2-09: I refitted the figure data myself. Slope $1{,}489$, line at $0{,}294$ and $0{,}890$. Answers: $22{,}48^\circ$ with $n = 1{,}50$ and $22{,}65^\circ$ with the exact slope. Both are inside the 3 % tolerance. The task's numbers and figure id are the same as in fi.
- Recomputed the unchanged answers touched by the diff: $1{,}4986$ and $2{,}002 \cdot 10^{8}\,\text{m/s}$; $34{,}67\,\text{ps}$; $34{,}249^\circ$; $416{,}4\,\text{nm}$; $n$ per row $1{,}3274$, $1{,}3319$, $1{,}3344$, $1{,}3268$, mean $1{,}3301$. All agree with answers.py.
- Removing "(esimerkkiaineisto)" from the two captions changes no data.
- The paragraph splits (L1-06, L3-04) change no claim.
- The hash was the same at the start and the end.
