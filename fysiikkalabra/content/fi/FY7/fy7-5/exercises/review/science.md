VERDICT: PASS
CONTENT-HASH: 9d27715c7f4ae222

## Blocking

## Polish
- solutions.md:120 (L3-02) — the row after $|\Delta\Phi| = 2BA$ reads $|e| = N\,\Delta\Phi/\Delta t$ without the absolute value. — Write $|e| = N\,|\Delta\Phi|/\Delta t$.
- solutions.md:130 (L3-03) — $|A|$ for the area under the $(t, e)$ graph is easily confused with the loop area $A$ (carried). — Use $|A_\text{a}|$ as in L3-05.

## Checked
- Round-1 finding fixed: L1-03 now writes the charge as $|q|$: $F_\text{m} = |q|vB$, $F_\text{s} = |q|E$, $E = vB$, $e = El = vBl$. The symbol $e$ now means only the voltage.
- L1-04 and L1-08: $v = e/(Bl)$ and $B = e/(vl)$.
- L2-01: $\Phi = BA$ and $|e| = B(A_1 - A_2)/\Delta t$ with $N = 1$. Recomputed 48 mV.
- L2-03: $I = vBl/R$, valid because the task makes the rest of the circuit's resistance negligible. Recomputed 0,30 A.
- L2-04: $\Delta\Phi = Blv\Delta t$ gives $|e| = NBlv$. Recomputed 75 mV.
- L3-02: $\Phi_2 = -BA$ and $B = |e|\Delta t/(2NA)$. Recomputed 50 µT.
- L3-03: $N\Phi = \tfrac12 e_0\Delta t$. Recomputed 0,060 mWb.
- L3-05: $e\,\Delta t = -N\Delta\Phi$ summed gives $\Phi = |A_\text{a}|/N$. Recomputed 0,0778 mWb.
- L1-07: $e_2/e_1 = N_2/N_1$. L2-06: $k = Bl$. L3-04: $v = at$, so $k = aBl$; $s = \tfrac12 at^2$ = 1,18 m.
- The packet shows the aligned blocks flattened; the file has correct `aligned` rows. Hash identical at start and end.
