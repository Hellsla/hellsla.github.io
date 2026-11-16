VERDICT: PASS
CONTENT-HASH: a86d3985160cc30e

## Blocking

## Polish
- exercises.json:321 (L3-05): the stored answer is 1716, but the Vastaus gives $1720\,\text{MW}$ (3 s.f.). Storing 1720 would make them agree; the tolerance covers both.
- exercises.json:103 (L1-09): the stored answer is 13.3824, the Sijoitus gives $13{,}4\,\text{MW}$ and the Vastaus $13\,\text{MW}$ (2 s.f., 2,9 % off, inside 0,04). Storing 13.4 would make them agree.
- solutions.md:215 (L3-05): the step heading "Kuvaajan lukeminen" introduces a table; "Taulukon lukeminen" would be accurate.

## Checked
- Round-2 fix: L3-05 d now asks "ei voi enää käytännössä tuottaa sähköä", and the solution gives the reason, a temperature difference of about $11\,\text{K}$ and a maximum efficiency of only a few percent. My recomputation gives a Carnot limit of 3,5 % (July, 17,8 → 28,4 °C) and 3,8 % (January), so the wording is right. The previous B finding is resolved.
- Typo "polttoaineteosta" is gone.
- I recomputed all 21 numeric answers in one script with my own formulas (chain product, $P_\text{h} = P_\text{o} - P_\text{a}$, $\eta_\text{kok}$, $c\,q_m\,\Delta T$, $m = P_\text{s}t/(\eta H)$, CHP interpolation, A/B fuel balance). All agree with answers.py and lie inside their tolerances.
- L2-08: 502,8 MW (42 % of 1200 MW), so the 500 MW option is correct and each distractor reproduces the mistake its feedback names.
- L1-06: exactly one correct option; the distractor feedback is right (same fuel, same energy; CHP gives less electricity; $\eta_\text{kok} \le 100\,\%$).
- L2-05 side values: 35,0/32,0/30,0 % and 84,6/88,4/90,0 % are right.
- The `chain-bars` figure gives P_o, P_1 and P_2 on gridlines, and its description gives no losses. L1-04 (200 MW) and L2-09 (42,9 %) read it correctly.
- Efficiency wording follows the guardrails: at most 100 %, heat pump with a lämpökerroin, hydro, wind and solar not heat engines.
- Significant figures follow the limiting data, and the reasonableness checks are real.
- The hash was the same at the start and the end.
