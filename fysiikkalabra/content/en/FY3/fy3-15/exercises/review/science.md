VERDICT: PASS
CONTENT-HASH: 1132258e3f06ce35

## Blocking

## Polish
- solutions.md fy3-15-L3-04 Formula — the row $P_\text{k,CHP} = 0.560\,P_{\text{o},\text{CHP}}$ puts a number into the symbolic chain. — Optional fix: name the heat share (for example $\eta_\text{k,B}$) and give 0.560 in the Given or Conversions.
- The previous round's polish items (L3-05 "Reading the graph" for a table; L1-05 "nearest megawatt"; L1-09 row ending at 13.4 MW against the answer 13 MW; L1-01 "kinetic energy of the water") still stand. The diff does not touch them.

## Checked
- Diff: only Formula steps changed. Each now starts from the definition of efficiency or the energy balance and solves symbolically to the form the unchanged Substitution uses.
- Chained efficiencies (L1-01, L2-01, L2-07): $P_{n} = \eta_n P_{n-1}$ gives $\eta = \eta_1\eta_2(\eta_3)$, with $P_\text{o}$ cancelling. This is correct. L2-02 inverts it for $\eta_2$ = 43.1 %.
- L1-03: $P = \eta IA$ = 4.20 kW. L2-03 and L3-02: $P_\text{o} = Hm/t$ and $Q_1 = Hm$ are solved for $m$ = 167 t and 13.6 kt. These are correct.
- L1-04, L2-06: the energy balance $P_\text{o} = P_\text{a} + P_\text{h}$ (no energy lost, the remainder is transferred as heat). The waste powers are 200, 1560, 768 and 238 MW.
- L2-04, L1-09, L3-05: $Q = cm\Delta T$ divided by $t$ gives $P = c\,q_m\,\Delta T$. The step $m/t = q_m$ is shown, and the condition (no change of state) holds for the cooling water. The results are 7.16 t/s and 13.4 MW; L3-05's ΔT_avg = 10.775 K is unchanged.
- L3-01: the linear trade-off $P_\text{s} = P_\text{s,0} - kP_\text{k}$ gives η_tot = 67.6 %. Total efficiency and electrical efficiency are kept apart (guardrail).
- L3-03: $W = Q_1/\varepsilon$ and $E_\text{fuel} = W/(\eta_\text{transm}\eta_\text{plant})$ give 87.7 kWh. The coefficient of performance is named as such, not as an efficiency.
- L3-04: fuel powers of separate and CHP production are $P_{\text{o},\text{A}}$ = 472 MW, $P_{\text{o},\text{CHP}}$ = 312.5 MW and $P_\text{k,CHP}$ = 175 MW.
- I recomputed every changed solution in one script, and all match. The hash is identical at start and end.
