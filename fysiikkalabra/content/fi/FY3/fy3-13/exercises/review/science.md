VERDICT: FAIL
CONTENT-HASH: b2b8aa84997e9232
Round: 1

## Blocking
- exercises.json:345 (L2-09 `tolerance` 0.02) with solutions.md:264 and :268 — **A (assessment)**: the solution says a hand-drawn value between −260 and −285 °C "hyväksytään", but ±2 % of −272,7 accepts only −267,3 … −278,2 °C (the page shows −260 and −285 as "Lähellä", not right). Reading the 100 °C point as 102 or 103 kPa on a 25 kPa grid already gives −277,8 / −267,9 °C; ±1 kPa on both points (the precision the solution itself states) gives −251 … −298 °C, so "useita celsiusasteita" understates it. — Set `tolerance` to 0.05 (−259 … −286 °C, matching the stated range) and write the uncertainty as "noin kymmenen celsiusastetta tai enemmän" (or narrow the stated range to what the tolerance accepts).
- solutions.md:258 (L1-09 Järkevyys) — **A (causality)**: "selvästi alempana kuin nestetypen kiehumispiste −195,8 °C, eli kylmempää ei voi saada" draws the lowest possible temperature from being colder than liquid nitrogen; that does not follow. — Keep the comparison as a magnitude check and give the real reason separately, e.g. "Kelvinasteikko alkaa absoluuttisesta nollapisteestä, joten negatiivista kelvinlämpötilaa eikä tätä kylmempää lämpötilaa ole."

## Polish
- solutions.md:275 (L2-10) — stated accepted range 52–58 kPa is slightly wider than tolerance 0.05 (52,1–57,6 kPa); say "noin 52–57 kPa".
- L1-09 — tolerance 0.04 (±11 °C) on an exact table value is loose; harmless, but 0.01 would fit a lookup.
- L2-09 text "Mittauspisteet ovat suoralla" — the points lie on a line only within reading precision (slopes 0,28 … 0,26 kPa/°C between neighbours); "lähes suoralla" fits the guardrail on fits.

## Checked
- Only L1-09, L2-09, L2-10 judged (delta added-exercise); the rest unchanged per packet.
- L1-09: $\theta_0 = -T_0 = -273{,}15$ °C; MAFY 0 °C = 273,15 K matches docs/mafy-arvot.tsv (VERIFIED); answers.py −273,15.
- L2-09 recomputed: $k = 27{,}5/100 = 0{,}275$ kPa/°C, $\theta_0 = -75/0{,}275 = -272{,}7$ °C; least-squares through all five points gives −272,1 °C; answers.py −272,727.
- L2-10 recomputed: $\theta = -73{,}15$ °C, $p = 75 - 0{,}275 \cdot 73{,}15 = 54{,}88$ kPa; independent $p \propto T$: 54,9 kPa; ±1 kPa reading gives 52,4–57,3 kPa, inside tolerance 0.05.
- L2-10 states the linear-extrapolation assumption in the task and flags celsius axis vs kelvin value: conditions met.
- Figure fy3-3/extrapolation-points: five points as in the description, no line, axis to −150 °C; gives what both tasks need and not the answer.
- Rigid closed vessel (fixed $n$, $V$) stated; formulas and symbols as in the brief ($k$, $\theta_0 = \theta_1 - p_1/k$).
- Solutions otherwise complete (given/asked, principle, symbolic first, conversions, substitution, rounding reason, independent checks in L2-09/L2-10).
- Hash identical at start and end.
