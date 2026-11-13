VERDICT: FAIL
CONTENT-HASH: c7b59c1d134016eb
Delta review (round 2, Kaava sign convention, 2026-11-13) of the version reviewed at 81704aa1f77b917f.

## Blocking
1. inquiry.json, the electron task in the potential graph (solution, **Periaate**). Class B, internal consistency. The new **Kaava** line is right and follows the unit's $W = QU$ with $U = U_{AB} = V_A - V_B$ (unit.md line 356): $Q = -e$, $U = V_0 - V = -150\,\text{V}$, $W = e(V - V_0) = 2{,}40 \cdot 10^{-17}\,\text{J}$. But the unchanged **Periaate** two lines above still says "sen potentiaalienergia pienenee määrän $eU$, kun $U$ on kuljettu potentiaaliero". With the Kaava's $U = V_0 - V$ (the same phrase, "kuljettu"), $eU = -2{,}40 \cdot 10^{-17}\,\text{J}$, so the sentence now says the potential energy *grows*. One symbol has two signs in one solution, which is exactly what round 1 fixed in the Kaava. Corrected text: "Sen potentiaalienergia pienenee määrän $e(V - V_0)$, kun $V - V_0$ on potentiaalin nousu (luku *Potentiaalienergia ja potentiaali sähkökentässä*)."

## Polish
(none)

## Checked
- The Kaava: $W = QU = (-e)(V_0 - V) = e(V - V_0)$ matches the unit's sign convention (start minus end) and the *Johda itse* result $\tfrac12 mv^2 = \lvert Q\rvert\,\lvert U\rvert$. Solved symbolically before any substitution. The Sijoitus factor $(150\,\text{V} - 0\,\text{V})$ is $V - V_0$, as in the Kaava.
- Recomputed in my own script: $U = -150\,\text{V}$, $W = 2{,}403 \cdot 10^{-17}\,\text{J}$, $v^2 = 5{,}276 \cdot 10^{13}\,\text{m}^2/\text{s}^2$, $v = 7{,}264 \cdot 10^{6}\,\text{m/s}$, which is $2{,}4\,\%$ of $c$. All of these agree with the solution.
- The LaTeX in the changed line is balanced. `units.py hash` gives c7b59c1d134016eb at the start and at the end.
