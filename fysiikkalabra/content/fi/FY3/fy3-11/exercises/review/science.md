VERDICT: PASS
CONTENT-HASH: 953b72bdbe61f2f5

## Blocking

## Polish
- exercises/solutions.md:282–287 (fy3-11-L3-05, Kaava) — the new row $\Delta U = Q - W$ is right with this task's $W = p\,\Delta V$ (the gas's work, as Kysytty and Periaate define it), but the lesson's first law is $\Delta U = Q + W$ with $W$ the work done on the gas. Write the gas's work $W_\text{k} = p\,\Delta V$ as fy3-11-L1-09 does, so that $\Delta U = Q - W_\text{k}$ cannot be read as a second form of the first law.
- The packet's diff shows these multi-line aligned blocks with their line breaks dropped (e.g. "W = F s F = pA …"); the file on disk is correct. Reviewed from `git diff ffa4ad2d81` on disk.

## Checked
- Steam engine: $W = Fs$, $F = pA$, $\Delta V = As$ → $W = p\,\Delta V$; 12,0 kJ.
- Boiler + engine: $\eta = W/Q_1$, $W = Pt$, $Q_1 = mH$ → $\eta = Pt/(mH)$; 9,0 % recomputed.
- Expanding air: $\Delta U = Q + W$, $W = -p\,\Delta V$ (work on the gas, as the lesson) → $\Delta U = Q - p\,\Delta V$; 500 J.
- Engine waste heat: $P_\text{o} = P_\text{a}/\eta$, $P_\text{o} = P_\text{a} + P_\text{hukka}$; 1200 kW and 720 kW.
- Separate vs combined production: $P = P_\text{a}/\eta$ per plant, $\Delta P = P_\text{s}/\eta_\text{lauh} + P_\text{kl}/\eta_\text{k} - P_\text{pa}$; 120 MW.
- Heat pump saving: $W = Q_1/\varepsilon$, $Q_1 = W + Q_2$ → $\Delta E = Q_2 = Q_1(1 - 1/\varepsilon)$; 9,60 MWh. The pump's COP is called lämpökerroin, not hyötysuhde (guardrail).
- Car: $W = \eta Q_1$, $Q_1 = mH$, $m = \rho V$, $t = s/v$ → $P = \eta\rho VH/t$; $5{,}418\cdot10^7\,\text{J}/4500\,\text{s} = 12{,}0\,\text{kW}$.
- COP from powers ($t$ cancels): 3,25; engine $\eta = P/(q_mH)$; four-day $Q_2 = Q_1 - W = 20{,}9\,\text{kWh}$; seasonal $\varepsilon_\text{kausi} = \Sigma Q/\Sigma W$ (not a mean of ratios) right.
- Piston: $\Delta s = (V_2 - V_1)/A = 0{,}60\,\text{m}$; L3-05: $Q = 1040\,\text{J}$, $W = 300\,\text{J}$, $\Delta U = 740\,\text{J}$. Last task: $Q_1 = \varepsilon W$, $Q_2 = (\varepsilon - 1)W$.
- Muunnokset, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
