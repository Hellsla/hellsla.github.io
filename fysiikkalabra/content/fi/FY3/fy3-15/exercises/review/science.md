VERDICT: PASS
CONTENT-HASH: b41a8c9ef224a497

## Blocking

## Polish
- exercises/exercises.json:6 (L1-01) and solutions.md L1-01 — "turbiini muuttaa veden liike-energiasta": a hydro turbine takes mainly the energy of the water's drop (head), not its flow speed; write "veden mekaanisesta energiasta" (E_p itself is FY4).
- exercises/exercises.json (L3-02) — "1 GWh = 3,60 · 10¹² J" and "1 kt = 10⁶ kg" are plain text inside a LaTeX-converted task; write them as inline LaTeX like the other values.

## Checked
- All 12 answers recomputed in one script with my own formulas: 90,16 %; 42,0 %; 4,20 kW; 480 MW; 90,0 %; 108,66 MW; 43,08 %; 166,7 t; 7,160 t/s; 205,5 MW (η_kok 67,6 %); 13,64 kt; 87,72 kWh — all match answers.py and exercises.json.
- L3-03 comparison right: direct electric 263 kWh, oil 111 kWh, heat pump 87,7 kWh; lämpökerroin defined as in the prerequisite chapter (ε = Q_sisälle/E_s), not called an efficiency; resistance heating counted at 100 %.
- L3-01 end points and interpolation right (40 % and 88 % bounds, 0,17 MW electricity lost per MW heat); the "why not comparable" reasoning follows the lesson (value of electricity vs heat).
- L3-02: denominator is purchased fuel vs wind; 273 wagons of 50 t check right.
- L2-04: Q = cmΔT applies (water only warms), mass-flow check 2,70·10⁸ W.
- Rounding reasons name the limiting data; tolerance 0,02 fits the significant figures.
- Notation (η₁η₂η₃, P_h, η_kok, P_L = c q_m ΔT) and wording match the lesson brief; guardrail on efficiency ≤ 100 % and CHP respected; scope within FY3.
