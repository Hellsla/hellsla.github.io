VERDICT: PASS
CONTENT-HASH: 42e62b5db7bbd438
Mode: delta (Formula steps rewritten as aligned derivations from the basic equations)
Round 1

## Blocking
(none)

## Polish
- solutions.md fy5-8-L2-07 Formula — $E_\text{p} = \tfrac12 F_\text{v}x$ now appears with no source. The old line showed $E_\text{p} = \tfrac12 kx^2 = \tfrac12 F_\text{v}x$ — insert the row $E_\text{p} = \tfrac12 kx^2$ before it, so the chain starts from the basic formula.
- solutions.md fy5-8-L2-01 Formula — $E_\text{p} = \tfrac12 F_\text{v}x$ comes before the basic $E_\text{p} = \tfrac12 kx^2$, and the Substitution uses the latter — put $\tfrac12 kx^2$ first or drop the $\tfrac12 F_\text{v}x$ row.

## Checked
- All 11 Formula diffs: each chain starts from Hooke's law $F_\text{v} = kx$ (or $F = -kx$), $E_\text{p} = \tfrac12 kx^2$ or energy conservation, and is solved in symbols to the old end formula used in the Substitution. The algebra is right in every row.
- L2-03: $\Delta E_\text{p} = \tfrac12 k(x_2^2 - x_1^2)$, not $\tfrac12 k(\Delta x)^2$.
- L3-01: four springs share the added weight, so $4k\Delta x = \Delta m\,g$.
- L3-02: $E_\text{start} = E_\text{end}$, $\tfrac12 kx^2 = mgh$, which gives $h = kx^2/(2mg)$ (unchanged model).
- L3-03: parallel springs with the same $x$ give $|\Sigma F| = (k_1 + k_2)x$, with the signs right.
- L2-06: $x = L - L_0$ and $mg = kx$ (the weight in equilibrium) give $k = mg/(L - L_0)$.
- L3-05: $k$ from the full-draw force, then $E_\text{p}$, $E_\text{k}$ and $\eta = E_\text{k}/E_\text{p}$; the model is unchanged.
- The non-formula hunks are only paragraph splits (script: identical text).
- Substitutions, answers and tolerances are unchanged. Spot-recomputed: 9000 N/m, 0.15 m, 0.24 J, 500 N/m, 0.54 J, 24.5 kN/m, 0.184 m, 3.2 N, 24.5 N/m and 0.60 J.
- Hash is the same at the start and the end.
