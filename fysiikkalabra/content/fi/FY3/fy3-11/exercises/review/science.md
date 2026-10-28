VERDICT: PASS
CONTENT-HASH: 7ade301110d15aed

## Blocking

## Polish
- lessons/FY3/fy3-11/answers.py:12,14,34 — the comments end "-> 37 %", "-> 22 %", "-> 12 kW", but the answers are 37,2 %, 21,7 % and 12,0 kW — match the comments to exercises.json.
- exercises/solutions.md:98 — typo "polttoatehon" — "polttoainetehon".
- exercises/solutions.md (L2-04 Vastaus) — "480 kW, jonka kaksi ensimmäistä numeroa ovat varmoja" is an arbitrary reading of the trailing zero — say the answer follows the hundreds/tens precision of 480 kW, or give 720 kW as three digits.

## Checked
- All 12 answers recomputed in one script from the task text with my own formulas; all agree with answers.py and exercises.json.
- L1-02: 1 g of steam at 100 °C takes about 1,7 l (pV = nRT), and the work is about 7,5 % of the heat of evaporation. This matches the guardrail that part of the heat of evaporation is work against the surroundings.
- L2-03: W/Q = 200/700 = 2/7, which is consistent with a diatomic ideal gas at constant pressure. The sign is given and explained.
- L1-04 and L1-05 use W = Q₁ − Q₂ and η = W/Q₁ in steady operation (the engine's internal energy does not grow), which is stated.
- L3-01: separate production needs 240 + 200 MW against 320 MW; the CHP total efficiency of 86 % is kept apart from the electrical efficiency; the boiler's high efficiency is explained correctly (no heat-to-work conversion).
- L3-02: the lämpökerroin is used as a ratio, and the saved electricity equals Q_ulko = 9,60 MWh. The energy balance argument against a perpetual-motion reading is correct.
- L3-03: the fuel power is 43 kW and the waste power 31 kW, 54/15/17 kWh are right, and the EV argument is correct.
- Units, conversions (MWh → J, l → m³, TJ) and the significant-figure reasons are right; the symbols match the lesson (W_k, Q₁, Q₂, η, ε).
