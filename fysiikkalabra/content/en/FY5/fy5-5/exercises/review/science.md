VERDICT: PASS
CONTENT-HASH: 8a6cb054cb3121bc
Mode: delta (Formula steps rewritten as aligned derivations from the basic equations)
Round 1

## Blocking
(none)

## Polish
(none)

## Checked
- All 15 Formula diffs: each chain now starts from $F = \gamma\frac{m_1m_2}{r^2}$, or from $mg = \gamma\frac{Mm}{R^2}$ for a surface $g$, and is solved in symbols to the old end formula that the Substitution uses. Every step was checked by hand.
- L1-05: $F' = \gamma\frac{m_1m_2}{(3r)^2} = F/9$. L2-01: $m^2 = Fr^2/\gamma$, $m = r\sqrt{F/\gamma}$.
- L2-03: $r = \sqrt{\gamma Mm/F}$ and $h = r - R$. L2-04 and L2-09: $g_h/g_0 = (R/(R+h))^2$; the relative change is $1 - (R/(R+h))^2$.
- L3-01: equal pulls give $(d-x)/x = \sqrt{m_\text{M}/M}$. The positive root is the right one for the point between the bodies; $x = d/(1+\sqrt{m_\text{M}/M})$.
- L3-02: $M = \rho\frac43\pi R^3$ gives $g = \frac43\pi\gamma\rho R$, so $g \propto R$ at the same density, which is the task's condition.
- L3-03 and L2-05: the ratios of forces and of $g$ are formed correctly from the two Newton expressions.
- L2-06 and L2-07: $\gamma = Fr^2/(Mm)$; $p = g(R+h)^2 = \gamma M$ is constant for every row, so the mean of $p$ is a valid estimate.
- L3-04: $M = gR^2/\gamma$, $\rho = M/(\frac43\pi R^3)$. L3-05: $mg - N = ma_\text{n}$ with $a_\text{n} = (2\pi R/T)^2/R$ is right for the equator of a rotating body.
- The non-formula hunks are only paragraph splits (script: identical text). Substitutions, answers and tolerances are unchanged; spot-recomputed 0.4015 µN, 4.0 µN, 37.9 kg, 0.344 %, 3.456·10⁵ km, 19.6 m/s², 315 N and 5.27 kN.
- Hash is the same at the start and the end.
