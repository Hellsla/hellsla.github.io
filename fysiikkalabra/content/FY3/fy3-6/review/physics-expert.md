VERDICT: PASS
CONTENT-HASH: 1e7a584b2d14267a

## Blocking
(none)

## Polish
1. lesson.md:68 — The sim's default (this setup with tabulated copper 385) shows 24,6 °C, while the example uses the measured 24,5 °C. The 0,1 K gap is exactly the gap between 375 and 385, and its direction matches the losses named. — Add: "Häviöttömässä kalorimetrissä kuparikappale nostaisi veden 24,6 °C:seen (kokeile simulaatiossa); jo 0,1 K pienempi lukema selittää eron."
2. lesson.md:66 — ΔT_vesi = 4,5 K has 2 sf (±0,1 K ≈ ±2 % in c), so "375" overstates the precision. — Write "noin 370–380 J/(kg·K)" or note that the third figure is uncertain.
3. lesson.md:8 — Sand heating faster is attributed only to its low c. Sun heating a thin sand layer while energy spreads deep into water (cf. L3-02) is a comparable cause. — Add "ja aurinko lämmittää vain hiekan pintakerrosta, kun vedessä lämpö jakautuu syvemmälle".
4. lesson.md:17 — The sign rule assumes ΔT = T_loppu − T_alku, which is never stated. — State it.
5. solutions.md:79 — "Kiviä tarvitaan vähemmän, koska ne jäähtyvät enemmän" gives only half the reason: the smaller c (5,2×) works the other way and is outweighed by ΔT (8,7×). — Mention both.

## Checked
- lint 0/0; test_sims.py fy3-6 PASS.
- Q = cmΔT and c₁m₁(T₁−T) = c₂m₂(T−T₂): insulated, no phase change (sim ranges keep the water liquid).
- Table values realistic; SVG bar heights proportional (210/4190).
- Example: 5656,5 J, c = 374,6, C_v = 1257 J/K, C_k = 75 J/K; loss direction (computed c too small) consistent.
- Misconception and exit-ticket numbers: 9,3×, 35 °C, 65 °C, 420 kJ.
- answers.py: correct formula, sign (L1-04, L1-05) and conversions (g, kW, MJ) on every line; tolerances cover rounding.
- Hand recompute: L3-01 12,09 kg; L3-02 3,58 K; L3-03 3,27 m³.
- Contexts realistic (18 MJ/m² per day, 1600 kg/m³ sand, 3,5-min kettle).
- sim.js: Teq is the exact weighted mean, Q = QW; the common-τ relaxation conserves energy at every instant.

## Python output
answers.py: {"fy3-6-L1-01": 0.633528, "fy3-6-L1-02": 210.6, "fy3-6-L1-03": 720.0, "fy3-6-L1-04": -35.196, "fy3-6-L1-05": 18.9, "fy3-6-L2-01": 64.8, "fy3-6-L2-02": 209.5, "fy3-6-L2-03": 53.749403, "fy3-6-L2-04": 450.0, "fy3-6-L3-01": 12.086538, "fy3-6-L3-02": 3.579952, "fy3-6-L3-03": 3.273438}
sim default Teq 24.6177; c at T = 24,4 / 24,5 / 24,6 °C: 365.8 / 374.6 / 383.4
