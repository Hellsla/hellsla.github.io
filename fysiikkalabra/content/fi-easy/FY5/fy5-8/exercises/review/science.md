VERDICT: PASS
CONTENT-HASH: 17ed22ef1a49baa7
Mode: delta (Kaava steps rewritten as aligned derivations from the basic laws; paragraph splits)
Round 1

## Blocking
(none)

## Polish
(none)

## Checked
- Every rewritten Kaava block starts from its basic law and is simplified symbolically to the form the unchanged Sijoitus substitutes into. The laws used are $F_\text{v} = kx$, $E_\text{p} = \tfrac{1}{2}kx^2$, $E_\text{alku} = E_\text{loppu}$, $\Sigma F = F_1 + F_2$ and $\Delta E_\text{p} = E_\text{p2} - E_\text{p1}$.
- Car suspension: $4\,\Delta F = \Delta m\,g$ with $\Delta F = k\,\Delta x$ is the right model for springs that are already preloaded. It agrees with the Periaate ($F_2 - F_1 = k\,\Delta x$, a quarter of the load per spring).
- Spring toy: $E_\text{alku} = E_\text{loppu}$ comes under the condition the Periaate states (no air resistance, massless spring), with the zero level at the start point.
- Parallel springs: $F_1 = -k_1x$ and $F_2 = -k_2x$ give $\Sigma F = -(k_1 + k_2)\,x$. The signs are right with $x$ measured from equilibrium.
- Error analysis: $x = L - L_0$ is defined first, then $F_\text{v} = mg = kx$. The task's point, that the extension is not the length, is kept.
- $E_\text{p} = \tfrac{1}{2}F_\text{v}x$ and $\tfrac{1}{2}kx^2$ are used consistently (they are the same triangle area).
- Recomputed in one script: 9000 N/m, 0.15 m, 75 N/m, 0.24 J, 500 N/m, 0.54 J, 24 525 N/m, 0.1835 m, 3.2 N, 24.525 N/m, x₁ = 0.15 m, x₂ = 0.050 m, ΔE = 0.60 J, k = 302 N/m. All agree with the solutions.
- Sijoitus, answers and tolerances are unchanged. The paragraph splits (L1-07 Mallivastaus, L2-01 Kuvaajan lukeminen, the last task's conclusion) change no physics.
