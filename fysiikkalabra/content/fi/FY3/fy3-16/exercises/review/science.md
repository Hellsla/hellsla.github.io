VERDICT: PASS
CONTENT-HASH: 2b0d3c5665d5edc6

## Blocking

## Polish
- exercises/solutions.md (fy3-16-L3-03, Kaava) — the wall's conducted energy $E = UA\Delta T\,t$ is put under $Q_\text{luovutettu}$ together with the drinks' heat; right as an energy balance, but "jään vastaanottama = seinän läpi tuleva + juomien luovuttama" says it more exactly than calling the wall's energy "luovutettu".
- The packet's diff drops the line breaks of the aligned blocks; every Kaava was read from the file on disk.

## Checked
- Every changed Kaava starts from the basic laws ($E = Pt$, $Q = cm\Delta T$, $Q = sm$, $Q = rm$, $P = UA\Delta T$, $\eta = E_\text{hyöty}/E$) and the balance $E = Q$ or $Q_\text{luovutettu} = Q_\text{vastaanotettu}$, then solves symbolically to the substituted form.
- L1-03 cool bag: $\Delta T = T_\text{ulko} - T_\text{sisä}$ is right here (heat flows in); 26,9 W.
- L2-01 and L2-07: $UA\Delta T\,t = sm$ solved for $m$ and for $t$; L1-08 and L2-09: $Pt = cm\Delta T$ for $t$ and $c$; L2-10 $t = Q/P$.
- L2-02: $Q = cm\Delta T + rm$; L2-04: $cm_\text{j}\Delta T = sm_\text{jää}$ (ice at 0 °C melting, drinks cooling).
- L3-01 sauna: $c_\text{k}m_\text{k}\Delta T_\text{k} = m_\text{v}(c_\text{v}\Delta T_\text{v} + r)$ → 25,95 K; assumptions (steam not warmed) stated.
- L3-02: $cm_\text{v}(T_\text{v} - T) = sm_\text{jää} + cm_\text{jää}T$ → $T = (cm_\text{v}T_\text{v} - sm_\text{jää})/(c(m_\text{v}+m_\text{jää}))$ correct.
- L3-03: $m = (UA\Delta T\,t + cm_\text{j}\Delta T_\text{j})/(c_\text{jää}\Delta T_\text{jää} + s) = 1{,}511\,\text{kg}$ → 1,6 kg rounded up as an "at least" value (house rule).
- L2-06: $E = UAt\,T_\text{sisä} - UAt\,T_\text{ulko}$, slope $k = -UAt$, $UA = -k/t = 139\,\text{W/K}$; sign right.
- L3-04: $E = UAt\,\Sigma\Delta T = 5443\,\text{kWh}$, $C_\text{A} = (E/\eta_\text{A})h_\text{A}$, $m = E/(\eta_\text{B}H)$; saving 480,6 € recomputed. L3-05: $Pt = m(c_\text{vesi}\Delta T_1 + s + c_\text{jää}\Delta T_3)$ correct.
- Numbers, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
