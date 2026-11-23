VERDICT: PASS
CONTENT-HASH: 42b37dc582c33aaa

## Blocking

## Polish
- lesson.md:338 — the summary gives $t = sm/(UA\Delta T)$ with no condition, but the worked example shows that warm contents make the time shorter — add "kun sisältö on jo $0\,{}^\circ\text{C}$:ssa" (the Kaava section already states the 0 °C interior assumption).
- inquiry.json pred-1 / kayra — pred-1 has "jääpussi ja juomia", but kayra's model (and its curve after melting, $C = 4190\,\text{J/K}$) has only 1,0 kg of ice. The plateau is the same either way. Consider saying "jääpussi" alone in pred-1, or keep the drinks out of the kayra model on purpose and say so.
- inquiry.json kayra solution — $P$ is rounded to 25 W from 25,2 W, which gives 333 kJ against the exact $sm = 334\,\text{kJ}$. The tolerance covers it, and the reasonableness check already explains it, so no change is needed.
- lesson.md:140 — "vesi … kiehuu helposti": a cooling circuit is pressurised. This is a fair simplification (C); one could add that glycol also raises the boiling point.

## Checked
- I recomputed every number in one script with my own formulas: 80 K ≈ 334 kJ, sauna 67/452 kJ, example 41,9 kJ / 33,6 W / 2,415 h → 2,4 h, 2,8 h without drinks, 19 K/h, the mixing misconception 126 kJ, Etsi virhe 63/267 kJ / 0,19 kg / 10,7 °C, the table rows 8,59–2,86 h, pred-2 2,87 h, löyly 85,7 %, siirto 64,9 s (8,4 / 56,5 s mistakes), check-2 213 → 210 kJ, check-c2 34 kJ, check-3 13 %, exit ticket 175,5 kJ. All agree. lesson-answers.py is right.
- Both $T(t)$ graphs are to scale: $t_0$ at x = 257,9 (2,41 h) and x = 282,8 (3,68 h), and the exponential approach with $\tau = C/UA$ ends at y = 89,9 and y = 78,5, as drawn.
- The cool-bag bars (334 / 42 / 335 kJ) are proportional. In the cooling circuit, hot $T_2$ goes to the radiator, cool $T_1$ returns through the pump, and the same $P$ goes in and out in steady state.
- Model conditions are stated where they are used: interior at 0 °C while ice remains, uniform temperature, drinks cooling at once, all of the heater power going to the stones, and the 19 K/h figure being valid only at the start.
- The mixing boundary cases follow the guardrails (≥ in step 4; the summary states the "ice initially at 0 °C" condition).
- Net transfer is worded as in the guardrails ("nettomääräisesti"), and there is no "lämmöksi".
- Each choice item has exactly one correct option, and every distractor's feedback is physically right (including that ice conducts heat better than water).
- The explain model answers and the criteria match the theory. The check-3 criteria ask only what the task gives.
- Scope: $Q = cm\Delta T$, $sm$, $rm$, $P = UA\Delta T$ and energy conservation, all within FY3's central contents.
