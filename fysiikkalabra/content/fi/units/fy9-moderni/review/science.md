VERDICT: PASS
CONTENT-HASH: 31904913655a7b58
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at b942c369bb9ab315.

## Blocking
(none)

## Polish
1. `unit.md`: $\lambda$ is now both the wavelength ($E = hc/\lambda$, $p = h/\lambda$) and the decay constant ($N = N_0e^{-\lambda t}$, $A = \lambda N$) on the same page. MAFY does the same, and both meanings are defined. Fix: add "($\lambda$ on tässä hajoamisvakio, ei aallonpituus)".
2. `unit.md`, after the attenuation law: $\dot{H}_0$ in $\dot{H} = \dot{H}_0(\tfrac12)^{x/d_{1/2}}$ is not named. Fix: add "$\dot{H}_0$ annosnopeus ilman suojaa".
3. `inquiry.json` writes the reaction energy as $Q = (m_\text{alku} - m_\text{loppu})c^2$, while the theory and the map use $E = \Delta m c^2$. Fix: align them.

## Checked
$N = N_0e^{-\lambda t}$ with $\lambda = \ln 2/T_{1/2}$ ($e^{-\lambda T_{1/2}} = 0.5$ exactly). The half-life form $N_0(\tfrac12)^{t/T_{1/2}}$ is still given, as the tasks need. $\Delta m$ = reactants − products and $E = \Delta m c^2$ are consistent with $E_\text{B}$. $p = E/c = h/\lambda$. $H = w_\text{R} D$. For $I = I_0 e^{-\mu x}$ with $d_{1/2} = \ln 2/\mu$ I recomputed $e^{-1.5}$ = 0.2231 = $0.5^{x/d_{1/2}}$. The map matches. The other rows are unchanged.
