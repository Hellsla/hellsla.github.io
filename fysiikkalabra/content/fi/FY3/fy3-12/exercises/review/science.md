VERDICT: PASS
CONTENT-HASH: 3f9cb6957944b4de
Round: 2

## Blocking
(none)

## Polish
- docs/exercise-bank/FY3.md:91ff — the plan still lists a wall temperature-profile figure task and an Earth radiation-budget graph at level 2. The new L2-06 (error analysis) and L2-07 (U-value panel experiment) replace them (carried over). Update the plan or note the swap.
- L2-06 is a one-formula task plus spotting the error. At level 2 it sits on the easy edge, which is acceptable for an error-analysis task (carried over).
- solutions.md:155 (L2-06 Vastaus) — the answer field holds 57,6 W while the Vastaus gives 58 W. Both are inside the tolerance. Writing "58 W (laskettuna 57,6 W)" as in L3-05 would make them consistent.

## Checked
- Round-1 Blocking resolved: L2-05 b) now asks "Mitä kansi estää avoimessa kupissa, ja miksi kupin B vesi silti jäähtyy?". The model answer names evaporation first, with the heat of vaporisation leaving with the vapour and convection carrying the vapour and warm air away. It also says why cup B still cools: conduction through the wall and the lid, and radiation. This is the right mechanism.
- Round-1 Polish resolved: L3-04 c) now reads "Jään väheneminen ei voi jatkua loputtomiin" and names the upper-bound simplification. The L3-05 typo now reads "ilmakehä ei ime". The L3-05 rounding reason is now the interpolation limit of about ±0,5 K.
- One script recomputed every new answer from the task text: L2-05 6,98 W (field 7,0); L2-06 57,6 W; L2-07 least-squares slope through the origin 0,1753 W/K, which gives U = 0,351; L3-04 0,343 W/m²; L3-05 S = 398,3 W/m² and T = 16,3 °C (the exact σT⁴ inversion gives 16,4 °C). All agree with exercises.json and answers.py within tolerance.
- L1-06, L1-07 and L1-08 were reshuffled. Each has exactly one correct option, the answer field equals it, and every distractor is wrong with correct feedback. The guardrail wording for net transfer is used.
- L2-07: the line through the origin has a physical reason (ΔT = 0 gives P = 0). The slope is read from the fitted line, and the guardrail sentence on fits is used.
- L3-05: the top and surface balances are consistent, and the −18 °C limit agrees with the brief.
- Scope: P = UAΔT, Q = cmΔT, energy balance and albedo only. No duplicates.
- The hash was identical at the start and the end.
