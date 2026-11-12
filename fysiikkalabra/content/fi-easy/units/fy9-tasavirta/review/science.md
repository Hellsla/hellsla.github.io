VERDICT: PASS
CONTENT-HASH: ccddd23e0bb39d09
Delta review (Johda itse round 2, 2026-11-12) of the version passed at daf3229a457bf979.

## Blocking
(none)

## Polish
1. The round-1 Polish item (removed results used under Kaava: without a source) is resolved.

## Checked
1. `inquiry.json` [13] [15] [19] [20]: Kirchhoff's 2nd law $E - R_\text{s}I - RI = 0$ with $U = RI$ gives $U = E - R_\text{s}I$ (the external resistance $R$ is named: starter motor, lamp); $P = UI$ with Ohm's law gives $P = U^2/R$ and $P = RI^2$. Each step holds for an Ohmic resistor, as the unit states.
2. Recomputed: $R_\text{s} = 16\,\text{m}\Omega$; $l = 7.11\,\text{m}$; $R_\text{s} = 0.60\,\Omega$, $E = 4.58\,\text{V}$ from both measurements; $1322/529\,\Omega$, $0.124\,\text{A}$, $20/8\,\text{W}$. Every number unchanged and right.
3. The fi-easy text says the same physics as fi in every changed place; numbers identical.
4. Judged: `git diff 3ec8cc24` of this unit-language (review/ ignored); nothing else changed.
