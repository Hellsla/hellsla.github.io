VERDICT: PASS
CONTENT-HASH: af6e1c0f678902a1

## Blocking

## Polish
- solutions.md (fy3-15-L3-04, Formula): the row $P_\text{k,CHP} = 0.560\,P_{\text{o},\text{CHP}}$ still puts a number into the symbolic chain. You could name the heat share (for example $\eta_\text{k,B}$) and give $0.560$ in the Given.
- The earlier polish items still stand:
  - L3-05 is headed "Reading the graph" although it reads a table.
  - L1-05 says "nearest megawatt".
  - L1-09's row ends at $13.4\,\text{MW}$, while the answer is $13\,\text{MW}$.
  - L1-01 says "kinetic energy of the water".

## Checked
- The Round 2 blocking item is fixed. The Given now says the district heating power is $0.560\,P_{\text{o},\text{CHP}}$, which agrees with the task text, the Formula row $P_\text{k,CHP} = 0.560\,P_{\text{o},\text{CHP}}$ and the Substitution ($175.0\,\text{MW}$).
- $P_{\text{o},\text{B}}$ now consistently means the total fuel power of option B, the plant plus the boiler. The chain ends with $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$, as the Find asks.
- Recomputed: $P_{\text{o},\text{A}} = 472.22\,\text{MW}$, $P_{\text{o},\text{CHP}} = 312.5\,\text{MW}$, $P_\text{k,CHP} = 175.0\,\text{MW}$, $P_{\text{o},\text{B}} = 340.28\,\text{MW}$ and $\Delta P_\text{o} = 131.94\,\text{MW} \to 132\,\text{MW}$. These agree with answers.py and with `answer` 132.
- Nothing else in the set changed since the earlier PASS.
- The hash was the same at the start and the end.
