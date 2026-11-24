VERDICT: PASS
CONTENT-HASH: 1744afda0ee103a3

## Blocking

## Polish
- solutions.md:335 (L3-05) — the new row $\Delta U = Q - W$ uses $W$ as the work done *by* the gas. The task and the Principle of L3-05 say so, which makes the row correct here. But L2-03 (lines 88–90) writes $\Delta U = Q + W$ with $W$ done *on* the gas. A student comparing the two may read it as a sign error. — Fix (optional): write $W_\text{g}$ for the gas's work in L3-05, as solutions.md:387 does, or add "($W$ done by the gas)".

## Checked
- Diff: only Formula steps. The packet's diff shows them flattened onto one line, so I read each multi-line `aligned` block on disk (lines 5, 71, 88, 108, 123, 146, 168, 209, 224, 258, 283, 332, 398, 417).
- L1-01: the chain $W = Fs$, $F = pA$, $\Delta V = As$ gives $W = p\,\Delta V$ = 12.0 kJ. It is correctly derived from force times distance (FY3 scope: $W = Fs$).
- L2-02 and the petrol-car task: the chain starts from $\eta = W/Q_1$, then the basic laws $W = Pt$, $Q_1 = mH$, $m = \rho V$ and $t = s/v$, then the combined form. This follows the teacher's "basic principle first" rule. The answers are 9.0 % and 12.0 kW.
- L2-03: the chain $\Delta U = Q + W$, $W = -p\,\Delta V$ gives 500 J. The sign convention matches its Principle.
- L2-04: the efficiency and the energy balance $P_\text{o} = P_\text{a} + P_\text{waste}$ give 720 kW.
- CHP comparison: each fuel power comes from its own efficiency, giving $\Delta P$ = 120 MW.
- Heat pump tasks: $\varepsilon = Q_1/W$ with $Q_1 = Q_2 + W$ (energy conservation, no "produces energy"). The results are $\Delta E = Q_1(1 - 1/\varepsilon)$ = 9.60 MWh, $Q_2 = (\varepsilon - 1)W$, and the cancellation of $t$ in $\varepsilon = P_1/P_\text{el}$ = 3.25.
- Seasonal COP task: $Q_1 = Q$ identifies the heat demand with the heat delivered. This is correct for heating supplied by the pump.
- Piston-travel graph task: $\Delta s = \Delta V/A$ = 0.60 m.
- I recomputed every changed solution in one script, and all match. Substitutions are unchanged. The hash is identical at start and end.
