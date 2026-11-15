VERDICT: FAIL
CONTENT-HASH: c9fc6cae7eec5478

## Blocking
- exercises.json:316 (fy3-15-L3-05 d) and solutions.md:221 — **B**. The task asks why the condenser heat "ei voi enää tuottaa sähköä", and the solution answers "Siksi sillä ei voi enää tuottaa sähköä". Both treat this as impossible. It is impossible only in practice: between $28{,}4\,{}^\circ\text{C}$ and $17{,}8\,{}^\circ\text{C}$ the Carnot limit is about $3{,}5\,\%$, not zero. The brief's Yleinen virhekäsitys says the correct thing ("vaikea saada paljon mekaanista työtä tai sähköä; mitä pienempi lämpötilaero, sitä pienempi suurin mahdollinen hyötysuhde"). The guardrail allows "cannot" only where a law says so, and then only in part. Fix: in the task, ask "Miksi … ei käytännössä voi enää tuottaa sähköä?". In the solution, write "Lämpötilaero on vain noin $11\,\text{K}$, joten lämpövoimakoneen suurin mahdollinen hyötysuhde olisi vain muutama prosentti. Siksi lämmöstä ei käytännössä saada sähköä." The Finnish version (content/fi/…/exercises.json:316, solutions.md:221) has the same wording and needs the same fix.

## Polish
- exercises.json:321 (L3-05): the stored answer is 1716, but the Vastaus gives $1720\,\text{MW}$ (3 s.f.). Consider storing 1720. The tolerance covers both values.
- exercises.json:103 (L1-09): the stored answer is 13.3824, the Sijoitus gives $13{,}4\,\text{MW}$ and the Vastaus gives $13\,\text{MW}$. Consider making them agree, for example storing 13.4.
- solutions.md:215 (L3-05): the step heading says "Kuvaajan lukeminen", but the data is a table. "Taulukon lukeminen" would be accurate.
- solutions.md:145 (L2-07): typo "polttoaineteosta" should be "polttoainetehosta".

## Checked
- I recomputed all 21 numeric answers in one script with my own formulas, independently of answers.py. Every one lies within its tolerance. The formulas were the chain product, $P_\text{h} = P_\text{o} - P_\text{a}$, $\eta_\text{kok}$, $c\,q_m\,\Delta T$, $m = P_\text{s}t/(\eta H)$, the CHP interpolation and the A/B fuel balance.
- I compared the set with the Finnish version by script: same ids, answers, units, tolerances, figures, data, correct options and task numbers.
- L2-08: 502,8 MW, so the 500 MW option is correct. Each distractor reproduces the mistake its feedback names: 0,503 MW, 50,3 MW and 14 600 MW.
- L1-06: exactly one option is correct. The distractor feedback is right: same fuel, same energy; CHP gives less electricity; $\eta_\text{kok} \le 100\,\%$.
- The `chain-bars` figure gives P_o, P_1 and P_2 on gridlines. Its description lists the bar heights but no losses or efficiencies. L1-04 (200 MW) and L2-09 (42,9 %) read it correctly.
- L3-01 (67,6 %, bounds 40–88 %), L3-03 (heat pump 87,7 kWh against direct electric 263 kWh and oil 111 kWh) and L3-04 (132 MW, about 28 %) use the right models, symbolic first.
- Efficiency wording follows the guardrails: at most 100 %, and electricity and heat are not of equal value. Hydro and wind are not heat engines, and their denominator is stated.
- Significant figures follow the limiting data, and the reasonableness checks are real (energy balances, back-calculation).
- The hash was the same at the start and the end.
