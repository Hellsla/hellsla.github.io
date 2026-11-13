VERDICT: FAIL
CONTENT-HASH: 7f560b98c5ecb9d0
Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at b9ac70fd7899fdc9.

## Blocking
1. inquiry.json, the electron task in the potential graph (solution, **Periaate**). Class B, internal consistency. The new **Kaava** line is right and follows the unit's $W = QU$ with $U = U_{AB} = V_A - V_B$ (unit.md line 356): $Q = -e$, $U = V_0 - V = -150\,\text{V}$, $W = e(V - V_0)$. But the unchanged **Periaate** still says "Sen potentiaalienergia pienenee määrän $eU$, kun $U$ on kuljettu potentiaaliero". With the Kaava's $U = V_0 - V$ ("kuljettu jännite"), $eU$ is negative, so the sentence now says the potential energy *grows*. One symbol has two signs in one solution. Corrected text: "Sen potentiaalienergia pienenee määrän $e(V - V_0)$. Tässä $V - V_0$ on se, kuinka paljon potentiaali nousee (luku *Potentiaalienergia ja potentiaali sähkökentässä*)."

## Polish
(none)

## Checked
- The Kaava: $W = QU = (-e)(V_0 - V) = e(V - V_0)$ matches the unit's sign convention and the *Johda itse* result. Solved symbolically first. The Sijoitus factor $(150\,\text{V} - 0\,\text{V})$ is $V - V_0$.
- Recomputed in my own script: $W = 2{,}403 \cdot 10^{-17}\,\text{J}$, $v = 7{,}264 \cdot 10^{6}\,\text{m/s}$, which is $2{,}4\,\%$ of $c$. These agree with the solution.
- The LaTeX is balanced. `units.py hash` gives 7f560b98c5ecb9d0 at the start and at the end.
