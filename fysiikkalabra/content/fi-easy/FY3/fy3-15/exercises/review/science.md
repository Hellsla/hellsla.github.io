VERDICT: PASS
CONTENT-HASH: aa08ba5b4a64f36f

## Blocking

## Polish
- solutions.md:268 (fy3-15-L3-04, Annettu): "kaukolämpöteho $0{,}560\,P_{\text{o},\text{B}}$" names the fuel power of the CHP plant $P_{\text{o},\text{B}}$. The Kaava, however, uses $P_{\text{o},\text{CHP}}$ for it, and $P_{\text{o},\text{B}}$ for plant plus boiler. Write $0{,}560\,P_{\text{o},\text{CHP}}$ in Annettu. This was there before the change; the numbers are right.
- solutions.md:47–51 (L1-04): the Kaava's $P_\text{o}$ means the stage's input power ($P_\text{o} = P_1$, defined under the block), but the task's figure uses $P_\text{o} = 400\,\text{MW}$ for the fuel power. Writing $P_1 = P_2 + P_\text{h}$, so $P_\text{h} = P_1 - P_2$, would avoid the clash.

## Checked
- solutions.md:271–276 (L3-04): the Kaava block now ends with $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$, which is the asked quantity solved in symbols. Round 1's Blocking item is resolved.
- L3-04 recomputed: $P_{\text{o},\text{A}} = 250 + 222{,}22 = 472{,}22\,\text{MW}$. $P_{\text{o},\text{CHP}} = 312{,}5\,\text{MW}$ and $P_\text{k,CHP} = 175{,}0\,\text{MW}$, so $P_{\text{o},\text{B}} = 312{,}5 + 25{,}0/0{,}900 = 340{,}28\,\text{MW}$. The difference is $131{,}9\,\text{MW}$, so $132\,\text{MW}$.
- I read every re-laid-out Kaava block on disk: L1-01, L1-03, L1-04, L2-01, L2-02, L2-03, L2-04, L2-06, L2-07, L3-01, L3-02, L3-03, L3-05 and L1-09. Each starts from $P_1 = \eta_1 P_\text{o}$, $\eta = P_\text{a}/P_\text{o}$, $P_\text{o} = P_\text{a} + P_\text{h}$ or $Q = cm\Delta T$, and solves the unknown in symbols. Every row is algebraically right.
- The chain products (L1-01, L2-01, L2-07) are derived by substituting rows, not stated. The results are still $90{,}16\,\%$, $108{,}66\,\text{MW}$ and $36{,}6\,\%$.
- L2-04, L3-05 and L1-09: $P = Q/t = c\,(m/t)\,\Delta T = c\,q_m\Delta T$, which agrees with the lesson's $P_\text{L}$.
- The paragraph splits in Järkevyys (L2-05, L2-06, L3-02, L3-05) leave the physics and numbers unchanged.
- No answer, unit or tolerance changed. The hash was the same at the start and the end.
