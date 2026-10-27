VERDICT: PASS
CONTENT-HASH: f0ce272aeebed2a0

## Blocking

## Polish
- lesson.md:252 — the rounded check gives "≈ 1,4 kW" and "≈ 34 kWh" next to the stated answers 1,5 kW and 35 kWh. A student may read that as a contradiction (1454 W is right at the rounding boundary) — say that the rough estimate 40 W/K · 36 K ≈ 1,4 kW agrees with 1454 W, so 1,5 kW is right, or use 40,4 W/K.
- solutions.md:39 (L1-04) and inquiry.json:272 (siirto) — "joten tulos on oikea" is drawn from a one-figure estimate, which only confirms the order of magnitude. L1-04 also assumes electric heating, which the task never states — write "oikeaa suuruusluokkaa" and drop "sähkölämmitteiselle".
- solutions.md:19 (L1-02) — "vanhan oven arvo on uuden oven luokkaa … kuten odottaa sopii" is a weak check: an old door is expected to be worse than a new one (typically about 1,4–2 W/(m²·K)). Recast it as "a little worse than a new door, far worse than a wall".
- lesson.md:3 — "säteilee avaruuteen yhtä paljon energiaa kuin saa Auringosta" should be "kuin imee". About 30 % is reflected and is not emitted as thermal radiation (L1-05 makes this exact distinction).

## Checked
- One script recomputed all 12 exercises, the worked example (1454 W, 34,9 kWh), tase-ennusta 150, epatasapaino 3,0 K, siirto 0,4608 kWh, check-2 140 and the exit ticket 300 W. All agree with answers.py and the stored answers.
- The rounded Vastaus lines (L1-01 430, L2-02 150, L2-03 210, L3-02 0,14, L3-03 980, siirto 0,46) are all within 2 %. Each names the datum that really limits the figures and matches what the data supports. None claims more precision than the data.
- The difference rule is applied correctly: whole-degree readings give ΔT = 36, 40, 45, 16 K (two figures); 2,8 − 0,80 = 2,0; 0,300 − 0,290 = 0,010; 240,0 − 236,4 = 3,6. 150 and 140 have three figures because the inputs are integer W/m², and the solutions say so.
- Principles are correct and justified: steady-state conduction P = UAΔT, parallel parts add, energy balance, Q = cmΔT (no phase change), W = Q/ε for the heat pump. Every unknown is solved in symbols first.
- Energy-balance model is self-consistent: σT⁴ gives 390 W/m² at 288 K and 240 W/m² at 255 K. The atmosphere absorbs 290 and emits 150 + 140; space receives 100 + 140 = 240. Forcing 3,6 W/m² / 1,2 W/(m²·K) = 3,0 K is realistic.
- L3-02 magnitudes: 2,6·10²⁰ kg for the top 700 m of the ocean is right. The atmosphere comparison ("kymmeniä kelvinejä") checks out at about 29 K. CO₂ 280 → 420 ppm and an imbalance of about 1 W/m² are current values.
- Reasonableness checks are real checks: back-substitution, energy-balance closure (L1-05, L2-03, check-2), limiting cases.
- Inquiry: every correct option and every feedback is physically right. Wrong-option feedback (conduction to space, energy "accumulating") repairs the misconception it reveals.
- Figure 4: 21 °C → −15 °C, ΔT = 36 K, with most of the drop across the insulation. Figure 3 is qualitatively correct.
- Scope: heat transfer, the U-value and energy balance fit the slot's LOPS goal. There is no Stefan–Boltzmann formula for students to use.
