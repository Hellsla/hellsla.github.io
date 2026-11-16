VERDICT: PASS
CONTENT-HASH: 28a3b421e466f8b3
SCOPE: delta added-exercise from 9cc21f77dd6113db base 71f5784fca44

## Blocking

## Polish
- exercises/solutions.md (fy3-11-L2-10, c) — "Ilma-vesilämpöpumpussa vaikutus on kaksinkertainen" can be read as "twice as large". What is meant is that two causes act together: colder outdoor air and warmer heating water. Optional: "vaikuttaa kaksi tekijää yhtä aikaa".
- Same c) — "Kovalla pakkasella lämpökerroin lähestyy arvoa 1": the source gives COP 1–2 at about −25 °C for a newish pump and the electric-heating level for older ones. Optional: "voi pudota lähelle arvoa 1" to keep it as the source says.

## Checked
- b) recomputed: Q₁ = εW = 4,0 · 2,5 kWh = 10 kWh and Q₂ = Q₁ − W = (ε − 1)W = 7,5 kWh. Both are two figures; the answer is 7,5 kWh with tolerance 0,02. The chain starts from energy conservation Q₁ = Q₂ + W and ε = Q₁/W, then solves symbolically. Symbols Q₁, Q₂, W, ε as in the brief's heat-pump formula.
- a) the lämpökerroin is not an efficiency, because Q₂ is not in the denominator. Efficiency ≤ 100 %, and a resistance heater's is practically 100 %. "hyötysuhde 300 prosenttia" is called imprecise for the right reason. This matches the guardrail and the glossary.
- c) a larger temperature difference means more electrical work per unit of heat, so ε falls. Warmer heating water in frost, COP 1–2 at −25 °C, and ε = 1 → Q₂ = 0 like a resistance heater. All right and consistent with the source facts.
- d) the claim is false: the balance closes (2,5 + 7,5 = 10 kWh), and the error is leaving out the outdoor heat. Right; no "energy created" picture.
- Järkevyys: the 75 % share, the 2,5 kWh for a resistance heater, and the limit that one instantaneous COP does not give the yearly consumption (source: yearly COP 1,4–3). Correct and quoted within the facts.
- Source quotations (COP definition, smaller temperature difference, −25 °C, 1,4–3) match the verified document text.
- Inside FY3 (energy conservation, heat pump as in the lesson; no cycle analysis).
- Hash the same at start and end.
