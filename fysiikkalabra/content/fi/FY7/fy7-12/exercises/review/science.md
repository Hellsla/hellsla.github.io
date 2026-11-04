VERDICT: FAIL
CONTENT-HASH: ce7668f796b8c369

Round 2: The round-1 blocking item is fixed. In L2-06, I is 0 % at 49,0 and 49,2 µs, and the solution adds "Aiemmin valoa ei voi tulla". Four round-1 polish items are also fixed: 39,0°, "Taulukon lukeminen", and the precision notes in L1-08, L3-04 and L3-05. Two of those precision notes now conflict with the answer box (items 2–3 below, which my round-1 polish caused). The reorder of L1-06 broke one of its options.

## Blocking
- exercises.json:59–60 (fy7-12-L1-06) — A, assessment: option 2 now has the same text as option 4 ("Valo tulee ilmasta mihin tahansa ... kuin peili"), but option 2 keeps the feedback of the deleted small-angle option ("kohtisuoraan rajapintaan osuva säde ..."). The option is duplicated, its feedback answers another claim, and the Mallivastaus ("Pieni tulokulma ei riitä") refers to a missing option. — Fix: restore line 59 to "Valo tulee suuremman taitekertoimen aineesta pienempään, ja tulokulma on pieni, jolloin säde osuu rajapintaan lähes kohtisuorasti."
- solutions.md:143 vs exercises.json fy7-12-L1-08 — the answer does not match its solution. The Vastaus is "1,0 · 10² km (noin 100 km)", but the answer box expects 103,45 with tolerance 0,02, so the model answer 100 (3,3 % off) is rejected. — Fix: give the time as 0,500 ms in the task and solution and write the Vastaus as "103 km, kolme merkitsevää numeroa". Or keep 1,0 · 10² km with tolerance 0,04.
- solutions.md:184 vs exercises.json fy7-12-L3-04 — the same conflict. The Vastaus says "17°", but the answer is 17,367 with tolerance 0,02, so 17 is rejected (2,1 % off). — Fix: set the tolerance to 0,03. Or report 17,4°.

## Polish
- exercises.json fy7-12-L1-07 vs L1-03 and the plan (carried over): L1-07 (acrylic → water) has the same structure as L1-03 (glass → water), and the plan's "timantin hionta" was replaced by L3-05. — Update the plan or note the swap.
- solutions.md:192 (fy7-12-L3-05) — the triangle geometry is described only in words. Add a small figure (O, R − a, R + a).

## Checked
- All new answers were recomputed with my own formulas, and they agree with answers.py: 63,20°; 103,4 km; 1,4933; 800 ns (t₀ 49,33 µs); 38,79°; 17,37°/14,03°/9,82°; 16,06 mm.
- L2-06: the corrected table shows no light before t₀.
- All other Vastaus values lie inside their tolerances (L3-05: 16 mm, 0,35 % off).
- The hash was the same at the start and at the end.
