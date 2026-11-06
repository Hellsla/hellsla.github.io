VERDICT: PASS
CONTENT-HASH: fd4eb60f56237477

Round 3 (fy7-5-L1-09, ordering)

## Blocking
(none) The round-2 item is fixed: C is an electromagnet with an iron core, constant current, 500 turns, flux 8,0 mWb per turn. The wrong rule e = N·Φ gives 4,0 V, above B (3,0 V), so C wrongly lands last; the solution (solutions.md:229) says so.

## Polish
- exercises.json:92 — five calculations is heavy for level 1; consider four situations (unchanged since round 1).
- exercises.json:98 — "yhden kierroksen vuo tarkoittaa käämin yhden kierroksen läpi kulkevaa magneettivuota" is circular; say "Vuo on yhden kierroksen läpi kulkeva vuo."

## Checked
- Values recomputed: A 1,2 V, B 3,0 V, C 0, D 0,60 V, E 2,0 V; order C, D, A, E, B; direction stated in the prompt.
- Both warned mistakes are caught: forgotten N (A, B fall below D) and flux size (C jumps to last).
- Constant current stated in the stem, so "vuo ei muutu" follows without a trick; 1 T over 80 cm² is realistic.
- Solution step by step; within the chapter (induction law, e = vBl).
- Checked from text only (no renders; pedagogy role); inline formulas fit (at most 227 px at 390 px).
