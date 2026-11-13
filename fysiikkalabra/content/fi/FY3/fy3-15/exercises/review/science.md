VERDICT: PASS
CONTENT-HASH: 645fa4cc0d0d8121
SCOPE: delta added-exercise from 6dc7d815de1ec77f base 89bcb63b7431

## Blocking
(none)

## Polish
- L2-09 Järkevyys — the figure (already passed with an earlier task) implies a generator-and-transformer efficiency of $140/150 = 93\,\%$, while real ones are about $98\,\%$, and an overall $35\,\%$ against the lesson's typical $38$–$42\,\%$. Not wrong for an old plant, but the check could say "vanhahko laitos" or the solution could avoid calling the values typical beyond $\eta_2$.
- L1-09 Vastaus — the answer field is 13,3824 while the stated rounded answer is 13 MW (2,9 % off, accepted only through the 0.04 tolerance); "13,4 MW" or "$1{,}3 \cdot 10^1$ MW" with the reason would sit closer to the check's ±2 % default. Optional.

## Checked
- Only L1-09 and L2-09 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $P_\text{k} = c\,q_m\,\Delta T = 4{,}182 \cdot 80 \cdot 40 = 13\,382$ kW = 13,4 MW; with the lesson's 4190 J/(kg·K) 13,41 MW; answers.py 13,3824. MAFY 4,182 kJ/(kg·K) matches docs/mafy-arvot.tsv (VERIFIED).
- L1-09: formula given in the task and derived in Periaate from $Q = cm\Delta T$ with steady flow; 20 °C table value for hot water noted (difference < 1 %); kJ/s = kW conversion right; check real.
- L2-09 recomputed: $\eta_2 = P_2/P_1 = 150/350 = 42{,}86\,\%$ → 43 %; answers.py 42,857; tolerance 0.03 accepts 43.
- L2-09 model: series chain $P_2 = \eta_2 P_1$ as in the brief; the solution correctly excludes $P_0$ and $P_3$; independent check $0{,}875 \cdot 0{,}4286 \cdot 0{,}933 = 0{,}350 = 140/400$ is right.
- figures.py chain-bars: bars 400, 350, 150, 140 MW on one axis from 0, to scale; $P_1$, $P_2$ on 50 MW gridlines; the description lists the same values; no efficiency shown.
- Both solutions complete (given/asked, principle with reason, symbolic first, conversions, substitution with units, rounding reason, check); symbols $P_0 \ldots P_3$, $\eta_2$, $q_m$ as in the brief.
- Inside FY3 (energiantuotanto, hyötysuhde).
- Hash identical at start and end.
