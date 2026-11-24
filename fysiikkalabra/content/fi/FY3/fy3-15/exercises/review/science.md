VERDICT: PASS
CONTENT-HASH: b5a901260dcdfe41

## Blocking

## Polish
- exercises/solutions.md (fy3-15-L3-04, Kaava) — the old last sentence "Erotus on $P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$" was dropped, so the Kaava no longer ends with the asked quantity. Add the row $\Delta P_\text{o} = P_{\text{o},\text{A}} - P_{\text{o},\text{B}}$. Also (unchanged): the task text writes the CHP heat as $0{,}560\,P_{\text{o},\text{B}}$, while the solution's $P_{\text{o},\text{B}}$ is option B's total (CHP + boiler) and the CHP plant's own is $P_{\text{o},\text{CHP}}$; one symbol for one quantity would help.
- The packet's diff drops the line breaks of the aligned blocks; every Kaava was read from the file on disk.

## Checked
- Chain efficiency (L1-01, L2-01, L2-07): $P_1 = \eta_1P_\text{o}$, $P_2 = \eta_2P_1$, $P_3 = \eta_3P_2$ → $\eta = P_3/P_\text{o} = \eta_1\eta_2\eta_3$, as the lesson; $\eta_2 = \eta/(\eta_1\eta_3)$ (L2-02) right.
- Solar panel: $P_\text{o} = IA$, $P = \eta IA$. Steam-cycle waste: $P_\text{o} = P_\text{a} + P_\text{h}$ → $P_\text{h} = P_1 - P_2$ with the stated identification.
- Wood chips (L2-03): $P_\text{s} = \eta P_\text{o}$, $P_\text{o} = Hm/t$ → $m = P_\text{s}t/(\eta H) = 166{,}7\,\text{t}$; the hour is exact.
- Condenser (L2-04, L3-05, L1-09): $Q = cm\Delta T$, $P = Q/t = cq_m\Delta T$, $q_m = P_\text{L}/(c\Delta T)$; notation as the lesson.
- L2-06: $P_\text{o} = P_\text{s} + P_\text{h}$; L3-02: $E = \eta Hm$ → $m = E/(\eta H)$.
- Heat pump chain (L3-03): $W = Q_1/\varepsilon$, $E_\text{polttoaine} = Q_1/(\eta_\text{siirto}\eta_\text{voimala}\varepsilon) = 87{,}7\,\text{kWh}$; lämpökerroin, not an efficiency.
- CHP vs separate (L3-04): 472,2 − 340,3 = 131,9 MW recomputed; the model (CHP sized to the electricity, boiler for the rest) matches the task.
- L3-01 linear electricity–heat trade-off $P_\text{s} = P_\text{s,0} - kP_\text{k}$ and $\eta_\text{kok}$ right.
- Numbers, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
