VERDICT: PASS
CONTENT-HASH: 7938fde08e8b26e2

## Blocking

## Polish
- solutions.md L2-04 — say once that a real LED driver cannot use the energy right down to 0 V, so 73 s is an upper limit. The task's assumption already covers this; carried over from round 1.

## Checked
- Round 2, full review. I re-ran answers.py and compared it with my independent recomputation: all 12 values agree (0,40 µF; 4,23 mC; 0,2816 J; 221 pF; 360 µJ; 320 V; 3,73; 100 µF; 72,9 s; 15 µJ; 1,518 µC; 217 cm²).
- Round-1 blocker resolved: the L1-04 Järkevyys now reads A : d = 0,025 m² : 0,0010 m = 25 m, and 25 m · 8,854 pF/m ≈ 220 pF. This is correct in both dimensions and arithmetic.
- L1-04 Vastaus: 2,2·10² pF = 220 pF, rounded to two significant figures, correct.
- L1-02: "Yksikkö täsmää: F·V = C" is correct.
- ex-qu figure: (60 µC, 12 V) on gridlines, C = 5 µF. L3-01, L3-02 and L3-03 models are unchanged and right. Polystyrene 2,6 / 24 MV/m is realistic.
- Symbols (W, E_max, εr) and ε0 = 8,854·10⁻¹² F/m match the course rules. No new errors in the diff.
