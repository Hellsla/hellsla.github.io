VERDICT: FAIL
CONTENT-HASH: 88538726b0fdf4c5

## Blocking
- solutions.md:146 (fy3-12-L2-05 b) — A, causality: the model answer names convection as the significant transfer the lid stops and leaves out evaporation. For open water at 80 °C, evaporation (the vapour carries the heat of vaporisation r away, fy3-7) is the main surface loss a lid removes; the lid also stops the air flow that carries vapour and warm air away. As written, a student who answers "haihtuminen" is marked against a weaker answer, and the wrong mechanism is taught. — Fix: model answer "Kansi estää ennen kaikkea haihtumisen: höyrystyvä vesi vie mukanaan höyrystymislämmön, ja konvektio kuljettaa höyryn ja lämpimän ilman pois. Kupin B vesi jäähtyy silti, koska lämpöä johtuu kupin seinän ja kannen läpi ja kuppi säteilee." Reword the question in exercises.json:169ff to "Mitä kansi estää avoimessa kupissa, ja miksi kupin B vesi silti jäähtyy?" (or accept evaporation plus convection explicitly).

## Polish
- solutions.md:180 (L3-04 c) — "Jään lisäys ei myöskään voi jatkua loputtomiin" says the opposite of what is meant — "Jään väheneminen ei voi jatkua loputtomiin, koska jäätä on vain rajallinen määrä." Also name the largest simplification: the September-minimum loss is used as if the sea were open all year at the annual mean 90 W/m², so the estimate is an upper bound.
- exercises.json:339 (L3-05) — typo "ilmakehä ei imenä" — "ilmakehä ei ime".
- solutions.md:189 (L3-05 Vastaus) — the rounding reason is muddled (three-digit table, then two significant figures); say the linear interpolation on a curved table limits the result to about ±0,5 K, so 16 °C.
- docs/exercise-bank/FY3.md plan for fy3-12 lists a wall temperature-profile figure task and an Earth radiation-budget graph at level 2; the new L2-06 (error) and L2-07 (U-value panel experiment) replace them. Fine physically; update the plan or note the swap.
- L2-06 is a one-formula task plus error spotting; at level 2 it is on the easy edge (acceptable as an error-analysis task).

## Checked
- One script recomputed all 20 answers from task text: L2-05 6,98 W, L2-06 57,6 W, L2-07 least-squares slope through origin 0,1753 W/K → U = 0,351, L3-04 0,343 W/m², L3-05 S = 398,3 W/m², T = 16,3 °C (exact σT⁴ inversion 16,4 °C, inside tolerance); all match answers.py and solutions.
- L3-05 table equals σT⁴ to ±1 W/m²; both balances (top 0,6S = 239, surface 239 + 0,4S = S) are consistent; −18 °C limit agrees with the lesson.
- L3-04 data near observed Arctic September minima; albedos 0,60/0,06 realistic.
- L1-06/07/08: exactly one correct option, every distractor wrong with correct feedback; L1-08 uses the guardrail net-transfer wording.
- L2-07: line through origin has a stated physical reason; slope read from fitted line, guardrail fit sentence used.
- Scope: only P = UAΔT, Q = cmΔT, energy balance and albedo; no Stefan–Boltzmann law needed (table given).
- No duplicates with L1-01…L3-03; L2-04 (global albedo) and L3-04 (sea-ice data) are distinct.
- Hash identical at start and end.
