VERDICT: FAIL
CONTENT-HASH: 81ec0d4c8cbaa96e
Round: 1 (YO-skill task)

Scope: the new task L2-08 (ordering, added 2026-11-05). The rest of the set and answers.py are unchanged since the round-3 PASS.

## Blocking
- solutions.md L2-08 Mallivastaus, "Massan mukaan järjestys olisi täsmälleen päinvastainen". This is false (A). By mass, from largest to smallest, the order is teekannu 1,0, kattila 0,60, jääpussi 0,50, kiehuva vesi 0,10 kg. The answer's reverse is teekannu, jääpussi, kattila, kiehuva vesi. The jääpussi and kattila places differ. — Fix: "Massan mukaan (suurimmasta pienimpään: teekannu, kattila, jääpussi, kiehuva vesi) järjestys olisi lähes päinvastainen, joten massa ei ratkaise."
- solutions.md L2-08 Kattila: "$\ldots = 201\,000\,\text{J} \approx 201\,\text{kJ}$". The product is 201 120 J, so the "=" is wrong (A). — Fix: "$= 201\,120\,\text{J} \approx 201\,\text{kJ}$".

## Polish
- solutions.md L2-08 Periaate, "olomuodon muutoksen kerroin". This is vague. Fix: "ominaissulamis- tai ominaishöyrystymislämpö $s$ tai $r$".
- solutions.md L2-08 Mallivastaus: the four inline chains are about 400–430 px wide at 1280 px (Teekannu, Kattila), more than the 300 px phone budget, so they will wrap mid-chain. Fix: one aligned display block, or split each at "=".

## Checked
- My own script gives 83,8 / 167 / 201,1 / 226 kJ, so the order is teekannu < jääpussi < kattila < kiehuva vesi, as `order` says. The order holds over the rounding range of the two-figure masses: 0,10 kg gives at least 215 kJ against at most 203 kJ for the kattila.
- The conditions are given in the task: s, r and c, the states, and 100 °C for the evaporation. The kattila only heats to 100 °C and does not evaporate. Q = sm and rm have no ΔT, as the lesson says.
- The items target the lesson's warned mistake that a change of state with no rise in temperature needs little energy. The jääpussi needs 2× the teekannu, and the evaporation is the largest item.
- The task is within fy3-6 and fy3-7.
- Renders: I viewed review/shots/fy3-7-open-exercises-L2-1280-11.png (after the commit). The prompt, the shuffled items and the solution render. I judged the phone width from that image's scale, not from a 390 px shot.
- The hash was the same at the start and at the end.
