VERDICT: PASS
CONTENT-HASH: a689891c9b7cc5f2
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 97b2ac678f09a7f6.

## Blocking
(none)

## Polish
1. `unit.md`, after $\Delta U = Q + W$: $W$ is the work done on the gas, and the next sentence reuses $W$ for the work the engine does ($W = Q_1 - Q_2$), which has the opposite sign. Fix: "does the work $W$ (here the work done by the engine, the opposite of the $W$ in the first law)".
2. `inquiry.json`, item `manta`: it uses $\Delta U = Q - W_\text{g}$ (the work done by the gas) and points to the chapter that now shows $\Delta U = Q + W$. The answer of 750 J is right in both conventions. Fix: add to the theory "The work done by the gas is $W_\text{g} = -W$, so $\Delta U = Q - W_\text{g}$".

## Checked
Gauge $p = \rho g h$ (total $p_0 + \rho g h$ stated). $pV/T$ = vakio with its two-state form. $W = p\Delta V$ with $|\Delta V|$. $\Delta U = Q + W$ with $W$ on the gas, $W = -p\Delta V$ in expansion (MAFY). Manta: 750 J. The map agrees. The English text says the same physics as fi. The other rows are unchanged.
