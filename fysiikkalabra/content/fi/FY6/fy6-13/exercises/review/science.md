VERDICT: FAIL
CONTENT-HASH: c45c7793ab039f02

## Blocking
- solutions.md:40 (fy6-13-L1-04, Järkevyys) — A: "Pinta-ala on 250 kertaa levyjen etäisyys metreinä, ja 250 · 8,854 pF ≈ 220 pF". A/d = 0,025 m² : 0,0010 m = 25 m, not 250, and 250 · 8,854 pF = 2210 pF, not 220 pF. The check is dimensionally muddled and its arithmetic is wrong. — fix: "A : d = 0,025 m² : 0,0010 m = 25 m, ja 25 m · 8,854 pF/m ≈ 220 pF".

## Polish
- solutions.md L2-04 — say once in Järkevyys that a real LED driver cannot use the energy right down to 0 V, so 73 s is an upper limit. The task's assumption already covers this.

## Checked
- All 12 answers recomputed independently with ε0 = 8,854·10⁻¹² F/m. They agree with answers.py and exercises.json: 0,40 µF; 4,23 mC; 0,2816 J; 221 pF; 360 µJ; 320 V; εr 3,73; 100 µF; 72,9 s; 15 µJ; 1,518 µC; 217 cm².
- L1-05: ex-qu (line to 70 µC, 14 V; C = 5 µF) puts (60 µC, 12 V) on gridlines. The caption gives the same data and no answer.
- L3-01: Q stays the same with the source disconnected, C halves and U doubles, so W goes from 15 to 30 µJ. The energy comes from the work of pulling the plates apart, which is correct.
- L3-02: with the source connected, ΔQ = (εr − 1)CU. The glass slab fills the gap, as the task says.
- L3-03: d = 2U/E_max = 0,50 mm and A = 217 cm². Polystyrene data are realistic.
- L2-02 εr 3,7 matches paper in the lesson table, and L2-01 paper 16 MV/m matches the table.
- Data are realistic: a defibrillator at 200 J / 2 kV, a supercapacitor at 10 F / 2,7 V, an audio PSU at 2200 µF / 16 V.
- Symbols (W for capacitor energy, E_max, εr) match the brief. Every solution is complete and symbolic first, and rounding is justified.
