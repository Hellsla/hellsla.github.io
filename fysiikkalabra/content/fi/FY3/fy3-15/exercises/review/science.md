VERDICT: FAIL
CONTENT-HASH: 7308462ffdb06e37

## Blocking
1. (A, consistency) exercises.json and solutions.md, fy3-15-L2-09: the fuel power is written $P_0$ (zero) in the task text and in the "Kuvaajan lukeminen"/"Reading the graph" line. The chapter says outright that "$P_\text{o}$:n alaindeksi on o-kirjain, ei nolla", the figure fy3-15/chain-bars labels the bar $P_\text{o}$, and L1-04 in this set, with the same figure, writes $P_\text{o}$. Fix: $P_0$ -> $P_\text{o}$ in the text and the solution.

## Polish
1. answers.py docstring and comments still write P₀ and P_hyöty; use P_o and P_a as the chapter does.
2. L1-09: Answer gives c at 20 °C for hot district-heating water; one clause that c of 60-100 °C water is about 4,19-4,22 kJ/(kg·K) (still inside 4 %) would make the lookup honest.

## Checked
Hash at start and end. Full review of the set (added L1-09, L2-09; L3-03 full stop). Own script recomputed every numeric answer from the task text: L1-01 90,2 %; L1-02 42,0; L1-03 4,20 kW; L1-04 200 MW (largest drop 350->150); L1-05 90 %; L1-07 34 %; L1-08 12,0 GWh; L1-09 4182·80·40 = 13,4 MW; L2-01 109 MW; L2-02 43,1 %; L2-03 167 t; L2-04 7,16 t/s; L2-05 90,0 %; L2-06 1560 MW; L2-07 36,6 %; L2-08 503 MW -> 500 MW option; L2-09 150/350 = 42,9 %; L3-01 206 MW; L3-02 13,6 kt; L3-03 87,7 kWh; L3-04 132 MW; L3-05 1716 MW. All agree with exercises.json and answers.py within tolerance, in all three languages. chain-bars generator holds 400/350/150/140 MW on 50 MW gridlines, matching both figure tasks; stage efficiencies 0,875·0,429·0,933 = 0,35 plausible. P_k = c q_m ΔT defined in the task and consistent with Q = cmΔT (no change of state). Multiple choice: exactly one correct option each.
