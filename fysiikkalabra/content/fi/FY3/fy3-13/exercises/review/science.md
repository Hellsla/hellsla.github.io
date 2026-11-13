VERDICT: PASS
CONTENT-HASH: 72427445dbf0ffcd
SCOPE: delta added-exercise from b38642a6e641d4f2 base 81db4a6fd727

## Blocking

## Polish
- exercises/solutions.md (fy3-13-L2-10, Periaate) — still "Pisteet ovat suoralla"; "lähes suoralla" as in L2-09 would match the fits guardrail (carried over).
- exercises/solutions.md (fy3-13-L2-10, Kaava) — "$\theta = T - 273{,}15\,\text{K}$ (celsiusasteina)" mixes units; the brief's $T = \theta + T_0$ solved for $\theta$ is cleaner (carried over).
- exercises/solutions.md (fy3-13-L1-09, Järkevyys) — "nestetyppeä voi jäähdyttää pidemmälle" is not a check of the result; the sentence on no negative kelvin temperatures is enough.

## Checked
- L2-09 (zero point now from the slope): $k = (102{,}5 - 75)/100 = 0{,}275\,\text{kPa/°C}$, $\theta_0 = 0 - 75/0{,}275 = -272{,}7\,{}^\circ\text{C}$; answers.py agrees; the least-squares line gives −272,1 °C.
- L2-09 says correctly that the axis ends at −150 °C, so the zero cannot be read and must be computed; $\theta_0 = \theta_1 - p_1/k$ is the brief's own form.
- L2-09 tolerance 0,05 (−259,1…−286,4 °C) against the reading error: with 75 kPa on a grid line, an end-point reading of 101,5–103,5 kPa (±1 kPa, the precision the solution states) gives −283,0…−263,2 °C, all accepted. The statement that the uncertainty is about ten degrees or more is honest (±1 kPa gives ±10 °C).
- L2-09 check: $75\,\text{kPa}/273{,}15\,\text{K} = 0{,}275\,\text{kPa/K}$ agrees with the read slope, so the check really tests the result.
- L2-10: $p = 75 + 0{,}275 \cdot (-73{,}15) = 54{,}88\,\text{kPa}$; $p \propto T$ gives 54,9 kPa; the stated 53–57 kPa lies inside the tolerance (52,1–57,6 kPa); linearity outside the range is assumed in the task, and the K→°C conversion is shown.
- L1-09: $\theta_0 = -T_0 = -273{,}15\,{}^\circ\text{C}$ (MAFY 0 °C = 273,15 K); answers.py agrees.
- Closed rigid vessel (n, V constant) stated in L2-09 and L2-10; figure description lists the five points and gives no answer.
- Rest of the set unchanged since PASS; hash same at start and end.
