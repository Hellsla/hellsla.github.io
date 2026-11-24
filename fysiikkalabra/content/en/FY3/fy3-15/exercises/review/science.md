VERDICT: FAIL
CONTENT-HASH: d08853a82594696f

## Blocking
- solutions.md:303 (fy3-15-L3-04, Given) — **A, internal consistency.** The Given says the district heating power is "$0.560\,P_{\text{o},\text{B}}$". In the Formula, and in the new last row $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$, the symbol $P_{\text{o},\text{B}}$ is the *total* fuel power of option B, the plant plus the boiler, $340.28\,\text{MW}$. The heat is $0.560\,P_{\text{o},\text{CHP}}$: $0.560 \cdot 312.5\,\text{MW} = 175\,\text{MW}$, whereas $0.560 \cdot 340.28\,\text{MW} = 190.6\,\text{MW}$. The task text says it correctly: "0.560 times the fuel power" of the plant. Now that the chain ends with $P_{\text{o},\text{B}}$ as the total, the Given contradicts it. — Fix: in the Given, write "$0.560\,P_{\text{o},\text{CHP}}$". The Finnish solutions.md:268 has the same symbol, and the developer should fix both.

## Polish
- solutions.md (fy3-15-L3-04, Formula): the row $P_\text{k,CHP} = 0.560\,P_{\text{o},\text{CHP}}$ still puts a number into the symbolic chain. You could name the heat share (for example $\eta_\text{k,B}$) and give $0.560$ in the Given.
- The earlier polish items still stand: L3-05 is headed "Reading the graph" although it reads a table, L1-05 says "nearest megawatt", L1-09's row ends at $13.4\,\text{MW}$ against the answer $13\,\text{MW}$, and L1-01 says "kinetic energy of the water".

## Checked
- The Round 1 item is fixed: the Formula now ends with $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$. This is the quantity the Find and the check ask for, and the Substitution's last step uses it.
- Recomputed: $P_{\text{o},\text{A}} = 250 + 222.22 = 472.22\,\text{MW}$, $P_{\text{o},\text{CHP}} = 312.5\,\text{MW}$, $P_\text{k,CHP} = 175.0\,\text{MW}$, the boiler $27.78\,\text{MW}$, $P_{\text{o},\text{B}} = 340.28\,\text{MW}$ and $\Delta P_\text{o} = 131.94\,\text{MW} \to 132\,\text{MW}$. These agree with answers.py and with `answer` 132 and `tolerance` 0.03.
- The physics is right: option B sizes the plant by the electricity need, the boiler supplies the missing $25\,\text{MW}$ of heat, and the saving is explained by the condenser heat being used.
- Nothing else in the set changed since the earlier PASS.
- The hash was the same at the start and the end.
