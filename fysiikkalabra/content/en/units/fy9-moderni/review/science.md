VERDICT: PASS
CONTENT-HASH: 9dfe588468827c1b
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 3e3f4a33c6a16ade.

## Blocking
(none)

## Polish
1. `unit.md`: $\lambda$ is now both the wavelength and the decay constant on the same page. Fix: add "(here $\lambda$ is the decay constant, not the wavelength)".
2. `unit.md`: $\dot{H}_0$ is not named. Fix: add "$\dot{H}_0$ the dose rate without the shield".
3. `inquiry.json` writes the reaction energy as $Q = (\dots)c^2$, while the theory uses $E = \Delta m c^2$. Fix: align them.

## Checked
$N = N_0e^{-\lambda t}$ with $\lambda = \ln 2/T_{1/2}$ ($e^{-\lambda T_{1/2}} = 0.5$ exactly). The half-life form $N_0(\tfrac12)^{t/T_{1/2}}$ is still given, as the tasks need. $\Delta m$ = reactants − products and $E = \Delta m c^2$ are consistent with $E_\text{B}$. $p = E/c = h/\lambda$. $H = w_\text{R} D$. For $I = I_0 e^{-\mu x}$ with $d_{1/2} = \ln 2/\mu$ I recomputed $e^{-1.5}$ = 0.2231 = $0.5^{x/d_{1/2}}$. The map matches. The English text says the same physics as fi. The other rows are unchanged.
