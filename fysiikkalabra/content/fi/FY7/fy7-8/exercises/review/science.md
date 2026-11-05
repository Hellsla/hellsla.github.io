VERDICT: PASS
CONTENT-HASH: b0742fa0acf09e72
ROUND: 2

## Blocking

## Polish
- solutions.md L2-06 Kaava: "oletus: virta ja jännite ovat samassa vaiheessa" is stated, but the low-load row (54 %) is where a magnetising current makes U₁I₁ overstate P₁ the most. One clause in b) would keep the explanation honest: "pienellä kuormalla oletus P₁ = U₁I₁ on epätarkin".
- solutions.md L3-05 Periaate: "ehto … saadaan tästä derivoimalla, mutta sitä ei johdeta tässä" is fine. Note that a least-squares fit of P_h − P₀ against P² gives 54,7 kW, which agrees with 54 kW.

## Checked
- Round-1 Blocking item L3-04 is resolved. The text now says "Oletetaan, että siirrettävä teho on vakio 200 MW koko vuoden", and the solution says "Koska teho on vakio, häviöenergia on P_h t".
- L3-04 resistance: the text now says "johtimien yhteinen resistanssi 0,040 Ω johdon kilometriä kohti", so there is no reason to double it. R = 6,0 Ω, I = 909/500 A, E_A = 43 450 MWh, E_B = 13 140 MWh, saving 1,515 M€.
- L2-06: the answer is 87,7 % with three significant figures and a correct reason (0,114 A; 11,5 V; 2,00 A). The P₁ = U₁I₁ assumption is now stated in the task. Losses are 2,12–3,22 W, and η runs 53,9 → 87,7 %.
- L3-05: the rounding reason is now based on 1,3 kW (two figures). The rows give 49 / 56,6 / 55,5 / 54,3 kW, which matches "49–57 kW".
- L1-06: "kun virta on asettunut vakioksi" removes the switch-on pulse case.
- L1-08: η = P₂ : P₁ is stated in the task, and 72/80 = 90 %.
- L2-05: the fit through the origin gives k = 0,012354 V per turn, so N₁ = 485,7. The unit in the solution is now V/kierros.
- I recomputed all new answers in one script, and they agree with answers.py and exercises.json: L1-07 210 kW, L1-08 90 %, L2-05 485,7, L2-06 87,72 %, L2-07 0,20 A, L3-04 1,5149 M€, L3-05 54,35 kW.
- Hash unchanged at start and end.
