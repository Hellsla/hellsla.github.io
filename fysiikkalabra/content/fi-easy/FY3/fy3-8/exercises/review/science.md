VERDICT: PASS
CONTENT-HASH: 0171826181598c8e

## Blocking

## Polish
- solutions.md:263–267 (fy3-8-L3-04): $\Delta T_\text{talvi}$ is defined as $T_\text{as} - T_\text{min} = 40\,\text{K}$ only in the Taulukon lukeminen line, above the block. That is enough, but repeating it under the block (as is done for $g_\text{raja}$) would make the sign of $g_\text{max} = g_\text{raja} - \alpha l_0\Delta T_\text{talvi}$ self-evident.

## Checked
- solutions.md:275 (L3-04 a): this now reads "$13{,}2\,\text{mm}$, käytännössä vähintään $14\,\text{mm}$". The minimum is rounded up, which is the safe side. Recomputed: $12\cdot10^{-6}\cdot 25{,}0\cdot 44 = 13{,}2\,\text{mm}$. A $14\,\text{mm}$ gap closes only at $8 + 14/0{,}30 = 54{,}7\,{}^\circ\text{C} > 52\,{}^\circ\text{C}$. Round 1's Blocking item is resolved.
- L3-04 b): $g_\text{max} = 30 - 12{,}0 = 18{,}0\,\text{mm}$, an "enintään" value, which is correct. The model answer for c) is still consistent: $15\,\text{mm}$ is at least $14\,\text{mm}$, and $15 + 12 = 27 < 30\,\text{mm}$.
- I read every re-laid-out Kaava block on disk as an aligned block: L2-01, L2-02, L2-03, L2-04, L3-01, L3-02, L3-03, L2-05, L2-06, L2-07, L3-04, L3-05, L2-09 and L2-10. Each starts from $\Delta l = \alpha l_0\Delta T$ or $\Delta V = \gamma V_0\Delta T$, and the unknown is isolated in symbols. The last row is the form the Sijoitus uses.
- L3-02: the new rows $\Delta l_\text{Cu}$ and $\Delta l_\text{Fe}$ and their difference factor correctly to $(\alpha_\text{Cu}-\alpha_\text{Fe})l_0\Delta T$, which is $20\,\mu\text{m}$.
- L3-03 and L3-05: $\gamma_\text{teräs}$ and $\gamma_\text{lasi}$ are each $\approx 3\alpha$, applied only to the solid container. L3-05: $h = (\Delta V_\text{etanoli}-\Delta V_\text{pallo})/(\pi r^2) = 75{,}9\,\text{mm}$.
- L2-10 c): the area $A$ cancels, which leaves $\Delta h = \gamma h_0\Delta T = 60\,\text{mm}$. L2-09: $k = 0{,}060\,\text{mm/K}$, so $T = 53{,}3\,{}^\circ\text{C}$.
- L2-07 c): the inequality chain gives $\Delta l \ge 10\,\text{mm}$ and $l_0 = 10{,}4\,\text{m}$. Both are correct.
- No answer, unit or tolerance changed. The hash was the same at the start and the end.
