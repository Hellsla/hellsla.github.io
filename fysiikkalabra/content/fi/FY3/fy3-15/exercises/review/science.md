VERDICT: PASS
CONTENT-HASH: e0b178c42e148725

## Blocking

## Polish
- exercises/solutions.md:39 and :241 (L1-04, L2-09) — The text says "Pylväiden päät ovat tarkasti ruudukon viivoilla" without limiting it to two bars. In `fy3-15/chain-bars` the grid step is 50 MW, so P₃ = 140 MW lies between gridlines. The sentence holds only for P_o, P₁ and P₂. — Write "Pylväiden P₁ ja P₂ päät ovat tarkasti ruudukon viivoilla".

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas: η as a product along the chain, P_h = P_o − P_a, η_kok = (P_s + P_k)/P_o, P_L = c q_m ΔT. Each one agrees with answers.py and with the key.
- L1-04 and L2-09, edited sig-fig lines: the figure has P_o = 400, P₁ = 350, P₂ = 150 and P₃ = 140 MW. The largest drop is 200 MW, and η₂ = 150/350 = 42,86 % → 42,9 %. Three figures is justified, because 350 and 150 sit exactly on gridlines. The page shows the answer as "42,9 %", inside the tolerance of 0,03.
- Edited energy wording in L1-02, L1-03, L1-06 (feedback) and L3-02: the energy becomes internal energy and is transferred as heat to the surroundings or the district-heating water. This is correct and follows the guardrail, and the CHP feedback now names the real mechanism.
- L2-05: the electrical efficiency is 35 / 32 / 30 % and the total efficiency 84,6 / 88,4 / 90,0 %. The explanation (more district heat in a cold year) is correct.
- L2-06: the efficiencies are 35 / 36 / 32 % and the waste heat 1560 / 768 / 238 MW. "No" is right: the least efficient plant does not have the largest waste heat.
- L2-08: P_L = 503 MW, and each distractor's value matches the mistake its feedback names (0,50, 50 and 14 600 MW).
- L3-01: P_s = 205,5 MW and η_kok = 67,6 %. L3-03 gives 87,7 kWh, against 263 kWh for direct electric heating and 111 kWh for the oil boiler. L3-04: option A needs 472,2 MW and option B 340,3 MW, so the saving is 131,9 MW (28 %).
- L3-05: the ΔT values are 10,9 / 10,7 / 10,6 / 10,9 K, with mean 10,775 K, so P_L = 1716 MW → 1720 MW, which is below P_h = 1800 MW. L1-09 with the MAFY value c = 4,182 kJ/(kg·K) gives 13,4 MW.
- The hash was the same at the start and the end.
