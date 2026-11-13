VERDICT: FAIL
CONTENT-HASH: c63477ece610534e

Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at 83e0790e263a8568.

## Blocking
1. [Major] inquiry.json, electron exercise, solution (Principle vs Formula): the symbol $U$ has two meanings in one solution. The Principle line says "its potential energy decreases by $eU$, where $U$ is the potential difference travelled", i.e. $U = V - V_0$, positive. The new Formula line sets $U = V_0 - V$ ($= -150\,\text{V}$ here). The reader meets $eU$ with opposite signs; this hinders comprehension and breaks the order principle, symbol, substitution. Fix: make the Principle say "...and its potential energy decreases by $e(V - V_0)$ (chapter *Potential energy and potential in an electric field*)." and drop "where $U$ is the potential difference travelled".

## Polish
- [Minor] Formula line: "the voltage travelled" is unidiomatic; "the voltage from the start to the point" reads better.

## Checked
- Round-2 diff only: the rewritten Formula line and its interaction with the Principle line in the same solution (source). KaTeX of the new chain ($W = QU = (-e)(V_0 - V) = e(V - V_0)$, \dfrac, \tfrac, \,\text units, \cdot) is well-formed and the order principle, symbolic equation, substitution, result is kept. No captures opened: the change is text inside a collapsed solution and the layout is unchanged from the version reviewed before.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
