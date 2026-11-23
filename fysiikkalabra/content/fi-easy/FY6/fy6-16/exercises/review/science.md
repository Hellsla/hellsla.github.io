VERDICT: PASS
CONTENT-HASH: 3098d1d5d8e3fef6
SCOPE: delta md-paragraphs,numbers,reflow,typography from 2af55d67694057c3 base e238aa9

## Blocking

## Polish
- solutions.md:242 — L3-05 Sijoitus "virralla $16\,\text{A}$ $P_\text{johto} = …$": two formulas sit side by side with no separator — add a comma or "on".

## Checked
- Every changed Kaava step (L1-01, L1-03, L2-01, L2-02, L2-03, L2-04, L2-05, L2-06, L3-03, L2-08, L2-09, L2-07, L3-04, L3-05, L3-06) is on disk as an aligned block. Each starts from the basic law ($\eta = W_\text{akku} : W_\text{verkko}$, $W_\text{verkko} = Pt$, $P = UI$ per phase → $P = 3UI$, current sum at the main fuse, $U = RI$, $R = \rho\,2l : A$, $P = RI^2$, $K = aW_\text{verkko}$, $W_i = P_i\Delta t$). Each simplifies symbolically to the form that is substituted. Every row is algebraically right.
- Notation matches the brief: $W_\text{akku}$, $W_\text{verkko}$, $\eta$, $P = 3UI$ with $U = 230\,\text{V}$ phase voltage, $P_\text{johto} = \rho\,(2l : A)\,I^2$, $K = aW_\text{verkko}$.
- L2-07 trapezoid form $\Delta t\bigl(\tfrac{P_\text{alku}+P_\text{loppu}}{2} + \sum P_\text{väli}\bigr)$ equals $\sum W_i$, and its symbols are named. $W = 22{,}85\,\text{kWh}$, $P_\text{ka} = 7{,}617\,\text{kW}$.
- L3-04 b) $n = s : 100\,\text{km}$, $W_\text{akku} = nw$, $W_\text{verkko} = nw : \eta$: consistent with the 100 km consumption taken from the battery.
- L3-05 and L2-03: the limit is written as an equality to find the largest current. This is right for a maximum. The safe-side rounding (L2-03 11 A, L2-05 10,4 kW) is unchanged.
- One script recomputed every number and compared it with answers.py, and all agree: 41,6 kWh; 15,94 A; 27,5 kWh; 10,87 h; 11,96 A; 6,53 V; 59,7 €; 156 %; 7,157 A; 10,45 kW; 5,288 h; 22,85 kWh; 1370,1 €; 7,609 A / 23,6 W / 104,4 W; 2,72 €.
- No answer, unit, tolerance or number in the task data changed. The paragraph split in L1-06 changes no claim.
- Hash identical at start and end.
