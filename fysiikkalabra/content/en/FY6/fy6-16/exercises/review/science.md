VERDICT: PASS
CONTENT-HASH: a18be3521b5b027b
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 6c786ed6b0783012 base 98218de

## Blocking

## Polish
- solutions.md:100 (fy6-16-L3-01) — $\Delta K = K_1 - K_2$ uses $K_1$, $K_2$ without stating that they are the costs with $\eta_1$ and $\eta_2$ — add "$K_1 = aW_\text{battery} : \eta_1$" or a short "where".
- solutions.md:203 (fy6-16-L2-07) — the row $W_\text{grid} = \Delta t(\dots$ is split by hand with `\\ &\qquad +`. It is correct maths, but the house rule says never to split a chain by hand; mathlayout wraps it on a phone.

## Checked
- The new Formula steps start from the basic laws and are algebraically correct: L1-01 $W_1 = s_1W$, $W_2 = s_2W$; L1-03 $P = 3P_1$, $P_1 = UI$; L2-01 $W_1 + W_2$; L2-02, L2-08 (part 1), L3-03 $\eta = W_\text{battery} : W_\text{grid}$, $W_\text{grid} = Pt$, $P = UI$ or $3UI$; L2-03 and L3-05 the phase-current sum with $I_\text{f}$; L2-04 $U = RI$, $R = \rho\,2l : A$; L3-01; L3-02; L2-05; L2-07 trapezoid closed form $\Delta t\,[(P_\text{first} + P_\text{last}) : 2 + \sum P_\text{mid}]$; L3-04 $n = s : 100\,\text{km}$; L2-09.
- L2-03 now writes the main fuse as $I_\text{f}$ (was $I_\text{main}$), the same as L2-05 and L3-05.
- In L3-05 "$\le$" became "$=$" at the limit. That is correct for the greatest current asked.
- Recomputed in one script: 41.6 kWh, 1840 W, 15.94 A, 27.5 kWh, 10.87 h, 11.96 A, 6.53 V, 59.7 €, 156 %, 7.157 A, 10.45 kW, 5.288 h, 22.85 kWh and 7.617 kW, 390.4 € and 1760.5 €, 7.609 A, 23.6 W and 104.4 W, 2.72 €. All agree.
- The rest of the diff splits paragraphs. Numbers, signs and units are unchanged and in the same order.
- No Finnish word remains in the math. The subscripts are English (battery, grid, heater, charger, loss, house, cable, avg, e/p, s = station).
- Read the hash at the start and at the end: unchanged.
