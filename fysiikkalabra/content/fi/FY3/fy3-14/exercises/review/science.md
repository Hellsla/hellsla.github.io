VERDICT: PASS
CONTENT-HASH: 497163bfee90ee02

## Blocking

## Polish
- exercises/solutions.md:55 (L2-01) — "Jos $Q_\text{v} > s m_\text{j}$" uses a strict inequality; the lesson and the guardrail say ≥ for "all ice melts" (equality gives 0 °C). Write ≥ for consistency.

## Checked
- All 12 answers recomputed in one script with my own model (phase-case solver): 16,7 kJ; 83,5 kJ; 25,14 kJ; 179,6 g; 5,04 kJ; 13,94 °C; 67,7 g; 177,5 s; 333,1 kJ/kg; 234,0 g; 281,2 g; −3,50 °C — all match answers.py and exercises.json.
- L3-02 case check right (6300 J ≤ 12 570 J < 106 500 J: ice left at 0 °C); L3-03 right (37 590 J < 42 000 J: all water freezes, T < 0 °C), energy balance 38 325 J both sides.
- L2-04 rearrangement right; the 8,0 °C sensitivity remark (≈ 335 kJ/kg) right; three figures justified (ds/dT ≈ 21 kJ/(kg·K) per K, ±0,05 K → ±1 kJ/kg).
- Rounding reasons name the limiting datum; tolerance 0,02 admits every correctly rounded answer (84 vs 83,5; 180 vs 177,5 / 179,6).
- Assumptions stated in the tasks (insulated vessel / no losses / full heater power / thermos); every solution symbolic first, conversions and checks real.
- Notation (Q_v, Q_j, m_s, ΔT_j, s) and constants (4190, 2100, 334 kJ/kg) match the lesson brief; scope within FY3.
