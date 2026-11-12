VERDICT: FAIL
CONTENT-HASH: b195e96769b3c55a

## Blocking
1. solutions.md, fy3-11-L3-01, Periaate: "P_in = P_a/η". P_a is not defined in this solution (it replaced the self-explaining P_hyöty), and the input symbol P_in is neither the solution's own P_pa nor the lesson's P_1. Fix: write "P_pa = P_a/η, missä P_a on hyödyksi saatu teho" (en: "…where P_a is the useful power"), or keep the relation in words.

## Polish
1. L2-04 uses P_in and P_mek/P_mech; align the input symbol with the lesson (P_1) or MAFY's P_o.
2. answers.py docstring still reads η = P_hyöty/P_in.

## Checked
Recomputed: L1-01 12,0 kJ; L1-02 172 J; L1-04 750 J; L2-03 ΔU = 700 − 200 = 500 J; L2-04 720 kW; L2-07 20,9 kWh; L3-01 120 MW; L3-02 9,6 MWh; L3-04 2,74; L3-05 0,74 kJ: all match. First-law sign: L2-03 and L3-05 say W is work done on the gas and use ΔU = Q − pΔV, while W = pΔV is the gas's own work in L1 tasks and L3-05 a), said each time. Heat pump tasks use Q₁, Q₂, W as the lesson. Numbers unchanged.
