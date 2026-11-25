VERDICT: PASS
CONTENT-HASH: 38b447f08cd0aafa

Delta review (work queue 11c): the new `hints` of s1–s8 in `sovella/tasks.json`, compared with each part's rubric, answer and `sovella/solutions.md`.

## Blocking
None.

## Polish
1. s6 a, hint 2 (fi): $E = Pt$ names the energy $E$, but in this unit $E$ is the source voltage (s1 d, s2 c, s3, s7, s8), and the solution writes $Pt = Q = cm\Delta T$. Replacement: "Veden lämmittämiseen tarvittava energia on $Q = cm\Delta T$ ja vastuksen antama energia $W = Pt$. Hyötysuhde on käytännössä $100\,\%$, joten $Pt = cm\Delta T$."

## Checked
- Every hint uses the model, symbols and sign conventions of its rubric and solution ($R_1 = U/I_1$, $R_1 = \rho l/A$ with $A = bh$, $U_\text{lat} = E + (R + R_\text{s})I$, $U = E - R_\text{s}I$ and slope $-R_\text{s}$, $\Delta x = p\cdot x + n\cdot r$, $U_\text{p} = E - IR_3$, $P = U^2/R$).
- Each number a hint states is right: $3{,}0\,\text{mm} = 3{,}0\cdot10^{-3}\,\text{m}$, $1\,\text{Wh} = 3600\,\text{J}$, $1\,\text{kWh} = 3{,}6\cdot10^{6}\,\text{J}$, $0{,}75\,\text{mm}^2 = 0{,}75\cdot10^{-6}\,\text{m}^2$, $4{,}0\,\text{cm} = 0{,}040\,\text{m}$, $400\,\text{mm}^2 = 4{,}00\cdot10^{-4}\,\text{m}^2$, $5{,}3\,\text{mA} = 0{,}0053\,\text{A}$, $1{,}6\,\text{kWh} = 1600\,\text{Wh}$. I recomputed every answer the hints lead to (162 W, 11,25 Ω, 9,78 µm, 136 W, 374 Wh, 27,7 km, 2,5 A and 35,5 V, 85,7 %, 4,11 W, ΔU = 0,023 V, ΔI = 0,25 mA, 6,40 h, 66,7 W, 2,74 kW, 2,33 kWh) and all agree with the answers.
- No hint states a part's final answer. The physical claims are correct: equal voltage across parallel branches, current is not used up, the hazard comes from the potential difference across the body, relative error is largest at the smallest reading, filament resistance rises with temperature, and the tangent slope is not the resistance.
- Numbers with units are LaTeX with decimal commas; 1–3 hints per part.
