VERDICT: PASS
CONTENT-HASH: dba8f481af21facc

## Blocking

## Polish
- solutions.md (L1-10, graph reading) — the Kaava $I : I_0 = \cos^2\theta$, $I = I_0 \cdot (I : I_0)$ is circular; start from Malus's law $I = I_0\cos^2\theta$ and say the factor $\cos^2\theta$ is read from the graph.

## Checked
- Delta: only Kaava steps rewritten as aligned blocks (two-polariser, angle from Malus, Brewster refraction angle, three polarisers, background-light reading, slope fit, graph angle, Brewster error analysis, crossed-polariser maximum, glare, line fit) plus paragraph splits; no number, answer, unit or tolerance changed.
- Each chain starts from $I_1 = \tfrac12 I_0$ and Malus's law and simplifies to the final form before substitution: $I_2 = \tfrac12 I_0\cos^2\theta$, $I_3 = \tfrac12 I_0\cos^2\theta_1\cos^2\theta_2$, $I_3 = \tfrac18 I_0\sin^2 2\theta$ (identity checked), $\theta = \cos^{-1}\sqrt{I : I_0}$.
- Background model $E = E_0\cos^2\theta + E_\text{t}$ with $E_0 = E_\text{max} - E_\text{t}$ (from $\theta = 0$): right; slope $\Delta E = E_0\,\Delta(\cos^2\theta)$ right.
- Brewster: $\alpha_2 = 90^\circ - \alpha_\text{B} = 90^\circ - \tan^{-1}(n_2 : n_1)$, condition (reflected and refracted rays perpendicular) stated in the Periaate.
- Recomputed in one script: 264,1 W/m², 60,0°, 33,69°, 75,0 W/m², 117 lx, 314 lx, 50,77°, 53,67°, 120 W/m², 7,14 W/m², 44,2°: all unchanged and right.
- Hash dba8f481af21facc at the start and at the end.
