VERDICT: PASS
CONTENT-HASH: d0f3be8f9671a1e0

## Blocking
None. Round-1 items fixed:
1. fy2-k2: the charging station now "ottaa sähköverkosta tehon 11 kW". t = 42,7 kWh / 11 kW = 3,88 h, and the rubric criterion is now justified.
2. fy2-k3 c: "noin puolitoista kertaa" with the IPCC default factors 112 and 74 g/MJ (ratio 1,51). The model answer and the 2-point assumptions criterion state that the claim needs regrowth, and that CO₂ rises in the short term.
3. fy2-k5 c: Järkevyys now says 0,70 · 20 MW = 14 MW.

## Polish
- fy2-k5 a: the answer gives "noin 180 GWh", but the units_precision detail says "noin 175 GWh". Make them agree (20 MW may be read as exact for a mean load).

## Checked
Delta from round 1. Hash d0f3be8f9671a1e0 at start and end.
- Osa 1 reordering: b (index 0), h (vesivoima, index 3) and j (index 0) each still have exactly one correct option. The other indices are unchanged and still right. The e feedback now correctly says 3,3 = 400 J / 120 J.
- fy2-k4 b now has two answers, 5325 kWh and 35,5 % (5325 / 15 000). The criteria (2 + 1) match. The solution's "vain murto-osan" fits December and January (15 and 40 kWh).
- fy2-k4 d now asks whether solar alone could replace fossil electricity. The model answer is correct: zero emissions in use, it cuts fossil generation in summer, but winter production is near zero, so other generation, flexible capacity or storage is needed. The criteria (1 + 1 + 1 + 1) ask only for what the task and the table give. It stays in FY2 scope (qualitative, no radiative balance).
- fy2-k6 capacities are now labelled rounded estimates for 2025.
- Recomputed: k2 38,4 / 42,7 kWh, 52,7 min, 5,12 €; k4 0,608 kW, 10,1 %; k5 175,2 GWh, 8176 homes, 14 MW. `answers.py` agrees.
- Rubric sums: every part's criteria equal its points. Total 20 + 4 × 15 + 2 × 20 = 120 offered, maximum 70.
- Scope: still no Q = cmΔT, E_k/E_p, W = Fs or chain-efficiency product.
