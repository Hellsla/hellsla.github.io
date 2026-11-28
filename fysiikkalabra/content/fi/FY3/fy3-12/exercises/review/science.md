VERDICT: PASS
CONTENT-HASH: 5c6002d8df8940b4

## Blocking

## Polish
- exercises/solutions.md:198 (fy3-12-L3-05, Kaava) — the top-of-atmosphere outgoing power is written $P_\text{im} = (1 - f)S + fS/2$. Correct by the energy balance (outgoing = absorbed), but naming the left side as the balance makes the principle visible: $P_\text{lähtö} = (1 - f)S + fS/2 = P_\text{im}$.
- The packet's diff drops the line breaks of the aligned blocks (e.g. "P = UA\Delta T U = …"); the file on disk is correct.

## Checked
- Every changed Kaava starts from $P = UA\Delta T$ (or the energy balance, $Q = cm\Delta T$, $E = Pt$) and solves symbolically to the substituted form; algebra checked on disk, lines 15–228.
- Door and wall: $U = P/(A\Delta T) = 1{,}2$; $\Delta T = P/(UA) = 30\,\text{K}$.
- Earth balance: $P_\text{säteily} = P_\text{im} = P_\text{tulo} - P_\text{heij} = 239\,\text{W/m}^2$.
- Radiators: parallel conduction $P = P_\text{s} + P_\text{y}$, $T_\text{ulko} = T_\text{sisä} - P/(\Sigma UA) = -20\,{}^\circ\text{C}$.
- Cost $H = hUA\Delta T\,t \approx 149\,\text{€}$; window saving $(U_\text{v} - U_\text{u})A\Delta T\,t = 212\,\text{kWh}$.
- Albedo: $P_\text{im} = (1 - r)P_\text{tulo}$, $\Delta P_\text{im} = (r_1 - r_2)P_\text{tulo} = 3{,}4\,\text{W/m}^2$ (sign right: less reflection, more absorbed). Sea ice: $\Delta P = I\Delta A(a_\text{jää} - a_\text{meri})$, 0,343 W/m².
- Thermos and ocean: $cm\Delta T = Pt$ → 20 K; $cm\Delta T = 10fIAt_\text{v}$ → 0,139 K; no change of state, as the guardrail requires for $Q = cm\Delta T$.
- Insulation with heat pump: $Q = (U_1 - U_2)A\Delta T\,t$, $W = Q/\varepsilon$ → 984 kWh; lid power $cm(T_\text{B} - T_\text{A})/t = 6{,}98\,\text{W}$.
- Slope $k = UA$, $U = k/A = 0{,}35$; $U = \lambda/d$, $P = (\lambda/d)A\Delta T = 210\,\text{W}$. Greenhouse model: $S = 239/(1 - f/2) = 398{,}3\,\text{W/m}^2$, 16 °C.
- Numbers, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
