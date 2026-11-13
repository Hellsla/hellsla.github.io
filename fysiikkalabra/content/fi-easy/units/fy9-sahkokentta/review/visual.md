VERDICT: FAIL
CONTENT-HASH: 7f560b98c5ecb9d0

Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at b9ac70fd7899fdc9.

## Blocking
1. [Major] inquiry.json, electron exercise, solution (Principle vs Formula): the symbol $U$ has two meanings in one solution. The Principle line says "Sen potentiaalienergia pienenee määrän $eU$, kun $U$ on kuljettu potentiaaliero", i.e. $U = V - V_0$, positive. The new Formula line sets $U = V_0 - V$ ($= -150\,\text{V}$ here). The reader meets $eU$ with opposite signs; this hinders comprehension and breaks the order principle, symbol, substitution. Fix: make the Principle say "Sen potentiaalienergia pienenee määrän $e(V - V_0)$ (luku *Potentiaalienergia ja potentiaali sähkökentässä*)." and drop "kun $U$ on kuljettu potentiaaliero".

## Polish
- [Minor] Formula line: "kuljettu jännite" is unclear for this reader; "jännite lähtöpisteestä tähän pisteeseen" is simpler.

## Checked
- Round-2 diff only: the rewritten Formula line and its interaction with the Principle line in the same solution (source). KaTeX of the new chain ($W = QU = (-e)(V_0 - V) = e(V - V_0)$, \dfrac, \tfrac, \,\text units, \cdot) is well-formed and the order principle, symbolic equation, substitution, result is kept. No captures opened: the change is text inside a collapsed solution and the layout is unchanged from the version reviewed before.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
