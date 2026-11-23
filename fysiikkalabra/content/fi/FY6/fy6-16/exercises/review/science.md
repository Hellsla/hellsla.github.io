VERDICT: PASS
CONTENT-HASH: 12b82b09f5af8447
SCOPE: delta md-paragraphs,numbers,reflow,typography from 9dcbe1d153d30989 base e238aa9

## Blocking

## Polish
- solutions.md:25 — the per-phase power is named $P_1$ ($P = 3P_1$, $P_1 = UI$); elsewhere in the set and in the brief $P_1$ is the first period's or device's power. Not wrong inside this task; $P_\text{v}$ or "yhden vaiheen teho $UI$" would avoid the overlap.

## Checked
- The packet's diff dropped the `\\ &` separators; I read the Kaava lines on disk (solutions.md:5–261): every one is a proper aligned block.
- Charging-time chains (lines 66, 116, 174) start from $\eta = W_\text{akku} : W_\text{verkko}$ and $W_\text{verkko} = Pt$ (and $P = UI$ or $3UI$), as the brief's Kaava does; recomputed 10,87 h, 7,157 A, 5,288 h.
- Three-phase and main-fuse chains (25, 76, 160, 246): $P = 3UI$ from equal phase currents, currents in one phase conductor summed; equality at the limit is right for the largest allowed current. Recomputed 15,94 A, 11,96 A, 10,45 kW, 7,609 A.
- Cable chains (86, 106, 246): $R = \rho\,2l : A$, $U_\text{h} = RI$, $P = RI^2$; 0,408 Ω, 6,53 V, 156 %, 23,6 W and 104,4 W recomputed.
- Energy and cost chains (5, 56, 96, 189, 232, 261): 41,6 kWh, 27,5 kWh, 59,7 € (59,65 unrounded), the trapezoid rewrite $\Delta t\,[(P_\text{alku} + P_\text{loppu}) : 2 + \sum P_\text{väli}]$ algebraically equal to $\sum W_i$, 22,85 kWh and 7,617 kW, 390,4 € and 1760,5 €, 17 kWh and 2,72 €.
- $\Delta K = K_1 - K_2$ has the right sign ($\eta_1 = 0{,}82$ is the costlier case).
- Every new chain is solved symbolically before substitution; substitutions, answers and roundings are unchanged.
- L1-06 model answer split into paragraphs: the wording and claims are unchanged.
- Notation ($W_\text{akku}$, $W_\text{verkko}$, $\eta$, $a$, $\rho$, $I_\text{p}$) is the same as in the brief.
- Hash read at start and end: unchanged.
