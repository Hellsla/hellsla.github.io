VERDICT: PASS
CONTENT-HASH: c18c297dc5096d89

## Blocking
- none

## Polish
1. L2-04 still uses P_in and P_mek/P_mech (defined in its Formula line); MAFY's P_o/P_a would match L3-01 and fy3-15.
2. L3-02 writes ε = Q/W with Q the heat into the house; Q₁ would match the lesson's ε = Q₁/W.

## Checked
Fix: L3-01 Principle now states η = P_a/P_o with P_a the plant's useful power and P_o its fuel power, then P_o = P_a/η; consistent with fy3-15. Recomputed L3-01: 96/0,400 + 180/0,900 − 320 = 120 MW; L3-02 ΔE = Q₂ = 16,0 − 6,40 = 9,6 MWh; answers.py output unchanged (L1-01 12,0; L2-03 500 J; L2-04 720 kW; L3-04 2,74; L3-05 0,74 kJ). First-law sign: L2-03 and L3-05 define W as work done on the air and use ΔU = Q − pΔV; the gas's own work pΔV is labelled. Only the L3-01 Principle line changed; no number or answer changed. Languages agree.
