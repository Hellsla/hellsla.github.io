VERDICT: PASS
CONTENT-HASH: 48e582d57b684a1c

## Blocking

## Polish

## Checked
- Hash at start and end: 48e582d57b684a1c.
- The round-1 polish item is fixed. In the L1-04 Vastaus (solutions.md:39) and the L2-09 Kuvaajan lukeminen and Vastaus, "tarkasti ruudukon viivoilla" now names only the bars P₁ and P₂. The L1-04 reading line says P_o, P₁ and P₂ are on gridlines, which is true (400, 350 and 150 MW, with a 50 MW step). It says P₃ ≈ 140 MW lies below 150, which matches `chain-bars`.
- The three-figure justification now rests only on the two bars that are exactly on gridlines. This holds for both 200 MW and η₂ = 150/350 = 42,86 % → 42,9 %. The independent chain check (0,875 · 0,4286 · 0,933 = 0,350 = 140/400) is right.
- I recomputed all 21 numeric answers in one script with my own formulas: chain η = η₁η₂η₃, P_h = P_o − P_a, η_kok = (P_s + P_k)/P_o, P_L = c q_m ΔT, and the fuel mass flow from P_o/H. Every one agrees with answers.py and lies inside its tolerance.
- L2-08: P_L = 4190 · 12 000 · 10 W = 503 MW, so the 500 MW option is correct. The distractors' values match the mistakes their feedback names.
- L3-01: P_s = 205,5 MW and η_kok = 67,6 %. L3-04: option A needs 472,2 MW and option B 340,3 MW, so the difference is 131,9 MW. L3-05: the mean ΔT is 10,775 K, so P_L = 1716 MW, which is below P_h = 1800 MW.
- L3-02 gives 13,64 kt and L3-03 gives 87,7 kWh. L1-09 with the MAFY value c = 4,182 kJ/(kg·K) gives 13,4 MW, inside the 4 % tolerance.
- The significant-figure reasons in the Vastaus lines match the limiting data.
- L1-06: exactly one option is correct, and the CHP mechanism and energy wording follow the guardrails.
