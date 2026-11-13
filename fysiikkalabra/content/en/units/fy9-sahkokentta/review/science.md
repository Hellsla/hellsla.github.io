VERDICT: PASS
CONTENT-HASH: f2ccc4940864b96a
Delta review (round 3, Kaava sign convention, 2026-11-13) of the version reviewed at c63477ece610534e.

## Blocking
(none)

## Polish
- inquiry.json, the electron solution: the unit text (unit.md line 356) writes $U = U_{AB} = V_A - V_B$, but here $U = V - V_0 = -U_{AB}$. The solution defines both symbols explicitly, and *Derive it yourself* also uses $U$ as the size of the voltage, so this does not contradict the unit. A student could still stumble over it.

## Checked
- The only change is the **Formula** line of the electron task's solution. It uses $W = QU_{AB}$ with $U_{AB} = V_0 - V$ (start minus end, the unit's convention), $Q = -e$, so $W = e(V - V_0) = eU$, where $U = V - V_0 = 150\,\text{V} > 0$.
- This $U$ is now the same positive potential difference as in the **Principle** ("decreases by $eU$"). Round 2's sign clash is gone. The Sijoitus factor $(150\,\text{V} - 0\,\text{V})$ is $V - V_0$.
- The quantity is solved symbolically before any substitution.
- Recomputed in my own script: $U_{AB} = -150\,\text{V}$, $W = 2.403 \cdot 10^{-17}\,\text{J}$, $v = 7.264 \cdot 10^{6}\,\text{m/s}$, which is $2.4\,\%$ of $c$. These agree with the solution.
- The LaTeX in the changed line is balanced.
- `units.py hash` gives f2ccc4940864b96a at the start and at the end.
