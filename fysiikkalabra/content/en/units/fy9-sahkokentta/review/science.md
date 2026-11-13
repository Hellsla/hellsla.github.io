VERDICT: FAIL
CONTENT-HASH: c63477ece610534e
Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at 83e0790e263a8568.

## Blocking
1. inquiry.json, the electron task in the potential graph (solution, **Principle**). Class B, internal consistency. The new **Formula** line is right and follows the unit's $W = QU$ with $U = U_{AB} = V_A - V_B$ (unit.md line 356): $Q = -e$, $U = V_0 - V = -150\,\text{V}$, $W = e(V - V_0) = 2.40 \cdot 10^{-17}\,\text{J}$. But the unchanged **Principle** still says "its potential energy decreases by $eU$, where $U$ is the potential difference travelled". With the Formula's $U = V_0 - V$ ("the voltage travelled"), $eU = -2.40 \cdot 10^{-17}\,\text{J}$, so the sentence now says the potential energy *increases*. One symbol has two signs in one solution. Corrected text: "Its potential energy decreases by $e(V - V_0)$, where $V - V_0$ is the rise in potential (chapter *Potential energy and potential in an electric field*)."

## Polish
(none)

## Checked
- The Formula: $W = QU = (-e)(V_0 - V) = e(V - V_0)$ matches the unit's sign convention (start minus end) and the *Derive it yourself* result. Solved symbolically before any substitution. The Substitution factor $(150\,\text{V} - 0\,\text{V})$ is $V - V_0$.
- Recomputed in my own script: $W = 2.403 \cdot 10^{-17}\,\text{J}$, $v = 7.264 \cdot 10^{6}\,\text{m/s}$, which is $2.4\,\%$ of $c$. These agree with the solution.
- The LaTeX is balanced. `units.py hash` gives c63477ece610534e at the start and at the end.
