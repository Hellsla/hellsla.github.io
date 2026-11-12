VERDICT: PASS
CONTENT-HASH: 73830490b1b3a881
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at ccfacb064cf5f007.

## Blocking
(none)

## Polish
1. `unit.md`, after $\Delta U = Q + W$: $W$ is defined as the work done on the gas, but the next sentence uses the same $W$ for the work the heat engine does ($W = Q_1 - Q_2$, $\eta = W/Q_1$), which has the opposite sign. Each statement is correct, but a student who combines them gets the sign wrong. Fix: "tekee työn $W$ (tässä koneen tekemä työ, pääsäännön $W$:n vastaluku)".
2. `inquiry.json`, item `manta`: the hints, the mistakes and the solution use $\Delta U = Q - W_\text{k}$, and the hint points to the chapter that now shows $\Delta U = Q + W$. The answer is right in both conventions (1200 J − 450 J = 750 J), and $W_\text{k}$ is defined in the hint. But the 1650 J feedback ("työ vähennetään") reads against the theory's plus sign. Fix: add to the theory "Kaasun tekemä työ on $W_\text{k} = -W$, joten $\Delta U = Q - W_\text{k}$", or rewrite the item with $W = -p\Delta V$.
3. `unit.md`, hydrostatic pressure: "Astian muoto ei vaikuta siihen." now follows the $p_0$ sentence, so it refers to the air pressure. Fix: move it right after "Se riippuu vain syvyydestä ja tiheydestä."

## Checked
Gauge $p = \rho g h$ (total $p_0 + \rho g h$ stated). $pV/T$ = vakio with its two-state form. $W = p\Delta V$ with $|\Delta V|$. $\Delta U = Q + W$ with $W$ on the gas, $W = -p\Delta V$ in expansion (MAFY). Manta: 750 J. The map agrees. The fi-easy text says the same physics as fi. The other rows are unchanged.
