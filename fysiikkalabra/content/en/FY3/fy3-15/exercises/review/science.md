VERDICT: PASS
CONTENT-HASH: 62b370cfcdb672b5

## Blocking
- none

## Polish
1. L3-01 uses P_s,0 (zero = no district heat) beside P_o (letter o); a word subscript avoids any confusion.

## Checked
Fix: L3-03 now uses MAFY's ε = Q₁/W with Q₁ the heat given indoors and W the electric energy the pump uses (defined in the Formula line), consistent with fy3-11; E_fuel = Q₁/(η_transm η_plant ε) = 100/(0,950·0,400·3,00) = 87,7 kWh, unchanged. answers.py output unchanged (L1-01 90,2 %; L1-02 42,0 %; L1-03 4,2 kW; L2-01 109 MW; L2-07 36,6 %; L3-01 206 MW; L3-02 13,6 kt; L3-04 132 MW). P_o, P_a, E_o consistent; only the L3-03 Given and Formula lines changed. Languages agree.
