VERDICT: PASS
CONTENT-HASH: 282eb61fc0b60703

## Blocking
- none

## Polish
1. solutions.md L2-04: $P_\text{o}$ appears only in the Formula line; name it once ("polttoaineteho eli ottoteho $P_\text{o}$" / "fuel power, the input power $P_\text{o}$"). Note the fy3-11 chapter's worked example writes the fuel power $P_1$ ($\eta = P_\text{a}/P_1$), fy3-15 writes $P_\text{o}$; one symbol across both would be cleaner.
2. answers.py docstring still says η = P_hyöty/P_in and comments use E_s, P_mek; align with P_a/P_o and W.
3. L3-04 still names the monthly heat demand $Q$ while L3-02 now uses $Q_1$; consider $Q_1$ in the table and text.
4. L2-09: a 0,60 m piston stroke is long for a "pieni kaasumoottori"; "sylinteri" alone or a larger area would be more realistic (numbers unchanged otherwise).

## Checked
Hash at start and end. Full review (added L1-09, L2-09; L2-04 P_a/P_o; L3-02 Q₁). Own script recomputed every numeric answer from the task text: L1-01 12,0 kJ; L1-02 172 J; L1-03 37,2 %; L1-04 750 J; L1-05 21,7 %; L1-08 3,25; L1-09 101 325 Pa·0,0020 m³ = 203 J (200 J, 4 %); L2-01 41,0 %; L2-02 9,0 %; L2-03 ΔU = Q − pΔV = 500 J; L2-04 720 kW; L2-05 31,4 % (60 kW); L2-07 Q₂ = 20,9 kWh; L2-09 ΔV/A = 0,60 m; L3-01 120 MW; L3-02 9,60 MWh; L3-03 12,0 kW; L3-04 13,7/4,995 = 2,74; L3-05 0,74 kJ. All agree with exercises.json and answers.py in all three languages. ε = Q₁/W = Q₁/(Q₁ − Q₂) and η = P_a/P_o used correctly; heat pump has a lämpökerroin, not an efficiency. pv-isobaari generator: 250 kPa, 1,0->4,0 l on gridlines, as both tasks read. Gas work sign (W_k by the gas, W on the gas in ΔU = Q + W) consistent. MC: one correct option each.
