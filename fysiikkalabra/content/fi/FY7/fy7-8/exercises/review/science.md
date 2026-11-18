VERDICT: PASS
CONTENT-HASH: 619f4ca1980ab94e

## Blocking

## Polish
- solutions.md:189 (L3-04, Kaava) — the rewrite dropped the row $R = 0{,}040\,\tfrac{\Omega}{\text{km}} \cdot s$ that the old Kaava had, yet Sijoitus a) still uses it — put it back as the first row of the chain.
- solutions.md (L2-09, Kaava) — the chain stops at $R = P_\text{h}/I^2$; simplifying to the end gives $R = 0{,}030\,U^2/P$ (same number), as the rule "simplify symbolically to the end" asks.

## Checked
- Delta: Kaava steps rewritten as chains from $P = UI$, $P_\text{h} = RI^2$ and $P_1 = P_2$; several paragraphs split; no number, answer, Muunnokset or Sijoitus changed; hash identical at start and end.
- Ideal transformer: $P_1 = P_2$, $U_1 I_1 = U_2 I_2 \Rightarrow I_1 = U_2 I_2/U_1$: correct.
- Loss tasks: $I = P/U$, $P_\text{h} = RI^2 = RP^2/U^2$, $P_\text{h}/P = RP/U^2$: correct algebra, two-wire model stated in each Periaate.
- Resistance limit: $RP^2/U^2 = 0{,}010\,P \Rightarrow R = 0{,}010\,U^2/P$: correct; recomputed $4{,}0\,\Omega$.
- Same share, same $R$: $RP_1/U_1^2 = RP_2/U_2^2 \Rightarrow P_2/P_1 = U_2^2/U_1^2$: correct ($3{,}306$).
- Doubled voltage: $P_{\text{h},2}/P_{\text{h},1} = U_1^2/U_2^2$ at constant $P$, $R$: correct ($210\,\text{kW}$).
- Three-phase: $I = P/(\sqrt{3}\,U\cos\varphi)$, $P_\text{h} = 3RI^2 = RP^2/(U^2\cos^2\varphi)$: correct, $R$ per phase conductor as given.
- Paragraph splits (L2-07 answer, L2-08 Periaate, multiple-choice explanation, Fingrid task a) and d)): text identical.
- Every chain's last symbolic form is the one the unchanged Sijoitus uses.
