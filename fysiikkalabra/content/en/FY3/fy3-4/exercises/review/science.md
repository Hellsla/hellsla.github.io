VERDICT: PASS
CONTENT-HASH: 6df7b6af9a2bf282

## Blocking

## Polish
- solutions.md (fy3-4-L2-07, Formula): $\Delta h_{\text{mean}} = \dfrac{\text{sum}}{3}$ uses a word in place of a symbol. $\dfrac{\Delta h_1 + \Delta h_2 + \Delta h_3}{3}$ would match the other blocks.

## Checked
- The diff changes only the Formula steps. No number, answer or Substitution changed.
- Checked each Formula block. L2-02: $h = \Delta p/(\rho g)$. L2-03: equal pressures with the same $p_0$ give $k_\text{A} h_\text{A} = k_\text{B} h_\text{B}$, which is correct. L2-04: the lid force $F = \Delta p\,A$ is the net force from the gauge pressure. L3-01: $A = mg/p_\text{max}$. L3-02: $\Delta F = \rho g h A$; the force depends on the head, not on the $0.40\,\textsf{l}$ of water, which is correct. L3-03: layered liquids add as $\rho_1 g h_1 + \rho_2 g h_2$. L3-04: the layered sum, the comparison and the depth error $h - \Delta p_\text{a}/(\rho g)$. L3-05: the mean pressure over a part is the mean of its edge values because $p$ is linear in depth, and $F_\text{tot} = \tfrac12 \rho g H \cdot Hw$. L2-05 and L2-08: slope $k = \rho g$.
- Recomputed: L2-03 $6.0\,\text{m}$, L3-04 $196.08\,\text{kPa}$, L3-05 $1962\,\text{kN}$. Each matches.
- The hash was the same at the start and the end.
