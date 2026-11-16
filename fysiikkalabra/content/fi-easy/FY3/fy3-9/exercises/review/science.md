VERDICT: PASS
CONTENT-HASH: dac5583058c958e9
Round: 1
Mode: delta

## Blocking

## Polish
- exercises/solutions.md:300 (fy3-9-L2-10 b) — "Vakiotermi on yhtä suuri kuin painelukeman heilahtelu" makes the Finnish "samaa suuruusluokkaa" stronger than it is: 32 kPa against about ±30 kPa is only an order-of-magnitude agreement. Fix: "Vakiotermi on suunnilleen yhtä suuri kuin painelukeman heilahtelu".

## Checked
- New fy3-9-L2-10: V and N are held constant ("pidä vakiona: tilavuus (V)", no pumping), the units are K and kPa, and the gauge is read several times, as in the source facts.
- The fit was recomputed independently. The line through the origin has k = 3.924 kPa/K. The free fit has a slope of 3.84 kPa/K and an intercept of 32 kPa. The residuals are +51 … +19 kPa, and the ratios p/T are 4.18 … 3.96. The prediction is 2358 kPa against 2346 kPa (12 kPa, 0.5 %). The ratio 450/300 = 1.50 matches the key (2 %).
- The guardrail wording on the outlier, the condition "harva kaasu, kaukana tiivistymisestä" and the particle model (etenemisliikkeen keskimääräinen liike-energia) are correct.
- A scripted comparison with the Finnish set (passed today) found the same answer, unit, tolerance and kind, and identical numbers in the text and in every solution section.
- Caption edits: "(esimerkkiaineisto)" removed only.
- Hash identical at start and end.
