VERDICT: PASS
CONTENT-HASH: 706354a0b2bb0af8

## Blocking
(none)

## Polish
- lesson.md:271 — "Jos kappaleen lämpökapasiteetti on suuri, kappale lämpenee ja jäähtyy hitaasti" is true for the same heating or cooling power; "samalla teholla" would close the condition (C as written).
- inquiry.json `siirto` — `answer` is 29.1 kg while the solution's stated answer is $29\,\text{kg}$ (two significant figures, from $8{,}0\,\text{K}$); both are inside the tolerance, but the shown answer and the solution could say the same number.

## Checked
- Recomputed in one script: worked example $c_\text{m} = 374{,}6\,\text{J/(kg·K)}$, its $24{,}6\,{}^\circ\text{C}$ sensitivity (383) and the lossless copper value $24{,}6\,{}^\circ\text{C}$; misconception $35\,{}^\circ\text{C}$; water/iron ratio 9,3, water/sand 5,2.
- Ennuste 1 / koe-1: sand $26{,}8\,{}^\circ\text{C}$, $8{,}5\,\text{kJ}$, $160\,\text{J/K}$; water $44{,}0\,{}^\circ\text{C}$, $30\,\text{kJ}$, $838\,\text{J/K}$; exactly one correct option, distractor feedback right. The koe-1 capture shows 26,8 °C at the initial state.
- Ennuste 2 / koe-2: 40,0 / 55,0 / 63,1 °C; the "yli 55 °C only if more hot water" condition is right for these temperatures.
- Experiments: each locks every other input and varies only cB or mB; the initial values are valid slider/select values; simState gives Teq and CB.
- Etsi virhe: wrong form gives 6,6 °C, correct 30,0 °C; the Kelvin distractor's feedback (the offset passes straight to the result) is correct.
- Siirto 29,09 kg, mistakes 220 and 21,3; tarkistus-2 890,6 → 891 (three sig. figs justified), mistakes 768 and 501, $C$ 838 vs 134 J/K; tarkistus-1 4500 vs 838 J/K; check-c2 35 °C, 65 °C distractor reasoning right.
- Exit ticket $419\,\text{kJ} \approx 420\,\text{kJ}$ and the ninefold iron rise; lake explanation and rubric consistent with the theory.
- Figures: water–sand thermometer rises 20 vs 105 px (ratio 5,25 = 4190/800), so "mittakaavassa" holds; c-bars lengths match 0,0935 px per J/(kg·K) for all six; calorimeter figure matches the example and is marked not to scale.
- Conditions stated: $Q = cm\Delta T$ without change of state; calorimeter's own heat capacity and losses neglected in the example, tasks and sim; the beach phenomenon also credits the thin heated sand layer and mixing depth (no single-cause claim).
- sim.js implements the weighted-mean equilibrium, $Q$ given = $Q$ taken, $C = cm$; exponential approach labelled as illustration with τ = 1,5 s as the model box says; no phase changes in the slider ranges; speed changes only pace.
