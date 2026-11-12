VERDICT: PASS
CONTENT-HASH: 3c51572cd824ce9d
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 171efe1a28f81c37.

## Blocking
(none)

## Polish
1. `unit.md`, the intro sentence, the map hub (`figures.py`, `fy9sk-kartta`) and the glossary explanation in `unit.json` keep $\overline{F} = q\overline{E}$, while the theory and the map's boxes use $Q$. Fix: $\overline{F}_E = Q\overline{E}$.
2. `unit.md`, the capacitor sentence: $E$ is the stored energy there, next to $E_\text{max}$, the breakdown field strength, and to $E = F_E/Q$ above. Each is defined, but they clash. Fix: "($E$ tässä energia, $E_\text{max}$ kentän voimakkuus)".
3. `inquiry.json` uses $F = qE$, $q_1$ and $qU$. They are defined there, but they differ from the theory's $Q$. Fix: align them.

## Checked
$F_E = kQ_1Q_2/r^2$ is written for magnitudes, with the vector form $\overline{F}_E = Q\overline{E}$. $E = F_E/Q$. $U = Ed$ only in a uniform field. $V = E_\text{p}/Q$. $W = QU$ with $U = V_A - V_B$ has the right sign. $\tfrac12 mv^2 = |Q|U$. $Q = CU$, $C = \varepsilon_0\varepsilon_\text{r}A/d$ and $E = \tfrac12 CU^2 = \tfrac12 QU$. All conditions are kept, and they are MAFY's forms. The map boxes match. The fi-easy text says the same physics as fi. The other rows are unchanged.
