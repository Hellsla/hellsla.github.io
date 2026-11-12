VERDICT: PASS
CONTENT-HASH: 55b5738c3399d275
Delta review (Johda itse round 2, 2026-11-12) of the version passed at 69db5cdd72902e76.

## Blocking
(none)

## Polish
(none)

## Checked
1. `unit.md`: $\eta = P/(GA)$ is a Lisätieto row; $\eta$, $P$ (maximum power point), $G$ (W/m²), $A$ defined with units; the perpendicular-light condition is stated. The removed Johda itse leaves no reference; the concept map (`figures.py`, `figures.json`, aria-label) now shows $P/(GA)$ in place of $P_\text{a}/P_\text{o}$, consistent with the table.
2. `inquiry.json` [7]: work $W = eU$ to kinetic energy from rest; recomputed $7.26\cdot10^6\,\text{m/s}$. [19]: $U = Ed$ in a uniform field with $E = E_\text{max}$, then $\tfrac12CU^2$; recomputed $320\,\text{V}$, $0.113\,\text{J}$.
3. The fi-easy text says the same physics as fi in every changed place; numbers identical.
4. Judged: `git diff 3ec8cc24` of this unit-language (review/ ignored); nothing else changed.
