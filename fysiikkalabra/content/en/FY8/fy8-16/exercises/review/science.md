VERDICT: PASS
CONTENT-HASH: 23911fe276ddc524
Mode: delta (work queue 8g: Formula steps rewritten as basic laws, then the derived formula in aligned rows)

## Blocking
(none)

## Polish
- exercises/solutions.md:535 (L3-06, carried over) — "$4.2 \cdot 10^{2}\,\text{Mpc}$, about $416\,\text{Mpc}$" gives two precisions side by side. The two-figure reason is right. Fix: keep 416 only as the unrounded intermediate result.

## Checked
- Hash 23911fe276ddc524 (`--exercises --lang en`) at the start and the end.
- A word-level diff of the old and new text: only the Formula steps changed (and `\dfrac` became `\frac` inside the aligned blocks). No given value, number or answer changed. exercises.json and answers.py did not change.
- L2-01, L3-03, L2-06, L2-09: the chain from $z$, then $v = cz$, then $v = H_0 d$, gives $d = cz/H_0 = c(\lambda-\lambda_0)/(H_0\lambda_0)$. It is correct, and each Principle states the small-$z$ condition for $v = cz$ (z = 0.030 and 0.035).
- L2-02: $t = d/v$ with $v = H_0 d$ gives $t = 1/H_0$, and the condition of constant expansion speed is stated in the Principle.
- L2-03: $\lambda = \lambda_\text{now}/1100$, $E = hf$ and $f = c/\lambda$ give $E = 1100\,hc/\lambda_\text{now}$. The scaling with $1+z \approx 1100$ is correct.
- L2-04: equal $H_0$ for A and B gives $d_\text{B} = d_\text{A} v_\text{B}/v_\text{A}$. Correct.
- L3-01: $m_\text{He} = 2n\,m$ and $m_\text{tot} = (n+p)m$ give $Y = 2n/(n+p)$, the right helium mass fraction when every neutron ends up in helium.
- L3-02: $Q = (3m_\text{He} - m_\text{C})c^2$ with atomic masses is right, since the electrons balance (6 = 6).
- L3-05: $k = 1+z$, $T = (1+z)T_\text{now}$; the inverse proportionality of $T$ to the stretching is stated in the task. L3-06: $d = 0.10\,c/H_0$. L2-05: the slope and $H_0 = \sum dv/\sum d^2$ for a fit through the origin are both right.
- answers.py run against exercises.json: all 19 numeric answers are within tolerance. Every chain starts with the quantity and is simplified symbolically before substitution.
