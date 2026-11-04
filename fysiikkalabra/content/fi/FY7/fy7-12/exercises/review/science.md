VERDICT: PASS
CONTENT-HASH: 2d654420254bbbeb

Round 4: delta review of commit 3b9c8f03d (fy7-12-L1-08 time 0,50 ms → 0,500 ms in task and solution). The round-3 Blocking item is resolved.

## Blocking

## Polish
- lessons/FY7/fy7-12/answers.py:17 (fy7-12-L1-08) — the line still uses `0.50e-3`; numerically identical, but write `0.500e-3` so the answer source matches the task data.
- solutions.md:184 (fy7-12-L3-04, carried over): the Vastaus still says "kolme merkitsevää numeroa kuten taitekertoimet" and then that n₁ − n₂ = 0,03 has one significant figure, so the two statements pull against each other. — Write: "17,4° laskettuna annetuista arvoista; koska n₁ − n₂ = 0,03, tulos on herkkä taitekertoimien pyöristykselle."
- exercises.json fy7-12-L1-07 vs L1-03 and the plan (carried over): L1-07 (acrylic → water) has the same structure as L1-03 (glass → water), and the plan's "timantin hionta" was replaced by L3-05. — Update the plan or note the swap.
- solutions.md:192 (fy7-12-L3-05, carried over): the triangle geometry is described only in words. — Add a small figure (O, R − a, R + a).

## Checked
- Hash 2d654420254bbbeb at start and end. Diff 3b9c8f03d^..3b9c8f03d in the exercise set read in full: only exercises.json:84 and solutions.md:137, 141, 142, 143, 144 (L1-08) changed.
- Round-3 Blocking (L1-08 rounding, A) fixed: time is 0,500 ms in the task text and in Annettu, Muunnokset, Sijoitus and Järkevyys; all data (1,45; 0,500 ms; 3,00 · 10⁸ m/s) have three significant figures, so "103 km, kolme merkitsevää numeroa" with the reason naming the time is now correct.
- Recomputed: s = c t : n = 3,00 · 10⁸ · 0,500 · 10⁻³ : 1,45 m = 103,448 km; answer 103,4483, tolerance 0,02 and Vastaus 103 km (0,43 % off) agree; Järkevyys 150 km : 1,45 = 103 km right.
- No other 0,50 ms remains in L1-08; the 0,50 ms in L1-05 (solutions.md:47–48) and a = 0,50 mm in L3-05 are separate tasks with their own two-figure data, unchanged.
- answers.py run: all answers unchanged and equal to exercises.json.
- Round-3 checks of L1-06 and L3-04 still hold; nothing else touched.
