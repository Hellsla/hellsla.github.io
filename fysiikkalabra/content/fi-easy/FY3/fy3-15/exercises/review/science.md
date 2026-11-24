VERDICT: PASS
CONTENT-HASH: a14dcf70d249d4ff

## Blocking

## Polish
- solutions.md (fy3-15-L3-04, Kaava): the row $P_\text{k,CHP} = 0{,}560\,P_{\text{o},\text{CHP}}$ puts a number into the symbolic chain. You could name the heat share, for example $\eta_\text{k,B}$, and give $0{,}560$ in Annettu.
- solutions.md:47–51 (L1-04): the Kaava's $P_\text{o}$ means the stage's input power, while the figure uses $P_\text{o} = 400\,\text{MW}$ for the fuel power. Writing $P_\text{h} = P_1 - P_2$ would avoid the clash. This item is unchanged from the last round.

## Checked
- solutions.md:268 (L3-04, Annettu): this now reads "kaukolämpöteho $0{,}560\,P_{\text{o},\text{CHP}}$". It agrees with the Kaava row $P_\text{k,CHP} = 0{,}560\,P_{\text{o},\text{CHP}}$ and with the task text ("0,560 times the plant's fuel power"). $P_{\text{o},\text{B}}$ is kept for plant plus boiler. Last round's Polish item is resolved.
- Recomputed: $P_{\text{o},\text{A}} = 250 + 222{,}22 = 472{,}22\,\text{MW}$, $P_{\text{o},\text{CHP}} = 312{,}5\,\text{MW}$, $P_\text{k,CHP} = 175{,}0\,\text{MW}$, the boiler $27{,}78\,\text{MW}$, $P_{\text{o},\text{B}} = 340{,}28\,\text{MW}$ and $\Delta P_\text{o} = 131{,}94\,\text{MW} \to 132\,\text{MW}$. These agree with answers.py.
- The total efficiency check holds: $0{,}880 \cdot 312{,}5\,\text{MW} = 275\,\text{MW} = 100\,\text{MW} + 175\,\text{MW}$. Electrical efficiency and total efficiency are kept apart (guardrail).
- Nothing else in the set changed. The hash was the same at the start and the end.
