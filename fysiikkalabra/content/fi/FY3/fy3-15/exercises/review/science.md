VERDICT: PASS
CONTENT-HASH: 6d5e4fe26062f07c

## Blocking

## Polish
- solutions.md:268 (fy3-15-L3-04 Annettu), carried over: the CHP heat is given as $0{,}560\,P_{\text{o},\text{B}}$. In the Kaava, $P_{\text{o},\text{B}}$ is option B's total (CHP plus boiler), and the CHP plant's own fuel power is $P_{\text{o},\text{CHP}}$. Fix: write $0{,}560\,P_{\text{o},\text{CHP}}$ in the Annettu so that one symbol means one quantity. The task text itself is unambiguous.

## Checked
- I read the changed Kaava block of L3-04 on disk (solutions.md:272–280). It now ends with the asked quantity, $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$, which is the Kysytty of the task (part c).
- The whole symbolic chain is right:
  - It starts from $P_\text{o} = P_\text{hyöty}/\eta$.
  - Option A: $P_{\text{o},\text{A}} = P_\text{s}/\eta_\text{s,A} + P_\text{k}/\eta_\text{kat}$.
  - Option B: $P_{\text{o},\text{CHP}} = P_\text{s}/\eta_\text{s,B}$ and $P_\text{k,CHP} = 0{,}560\,P_{\text{o},\text{CHP}}$, with the boiler covering $P_\text{k} - P_\text{k,CHP}$.
  - This is the model the task text describes.
- I recomputed with my own formulas: $P_{\text{o},\text{A}} = 250 + 222{,}2 = 472{,}2\,\text{MW}$ and $P_{\text{o},\text{B}} = 312{,}5 + 25{,}0/0{,}900 = 340{,}3\,\text{MW}$. The difference is $131{,}9\,\text{MW}$, so the answer $132\,\text{MW}$ is right. The saving is $131{,}9/472{,}2 = 28\,\%$, as stated.
- The reasonableness check is consistent: CHP total efficiency $0{,}880$ and $275\,\text{MW}$ useful power, against $0{,}635$ for option A.
- No Sijoitus, answer or answers.py value changed.
- The hash was the same at the start and the end.
