VERDICT: PASS
CONTENT-HASH: 780ee5441798b468

## Blocking

## Polish
- solutions.md:234 (L3-05 Periaate) — "kohti keskipistä" appears four times. — Write "keskipistettä". This is language only.
- solutions.md (L3-05 Vastaus) — the answer is stored as 575 N with three figures, while T_b = 6,0 h has two, so the text also accepts 570 N. The 2 % tolerance covers both. — Optional: write "6,00 h" in the task so that 575 N is consistent.

## Checked
- The hash is the same at the start and the end (780ee5441798b468).
- Round-1 duplicate: L3-05 b) now asks for the scale reading with a 6,0 h day. I recomputed it myself: v = 1855 m/s, a_n = 4π²R/T² = 0,5397 m/s², and N = 62,0 kg · (9,81 − 0,5397) m/s² = 574,8 N. It matches exercises.json (575) and answers.py (574,76). It no longer duplicates fy5-6-L3-03, and the reading stays positive, as the check says.
- In the L3-05 Järkevyys, 4² = 16 and 16 · 0,0337 ≈ 0,54 m/s² are right. A 33 N drop and 5,5 % of 608 N are right.
- L3-05 c) now says "kokonaisvoiman mg − N on oltava m a_n". This agrees with fy5-4: keskeisvoima is a resultant, not a separate force. "ei kierrä" is fixed.
- The shuffled MC answers of L1-06, L1-07 and L1-08 are right. Each has exactly one correct option, the answer text equals that option, and every feedback still fits its option. L1-07 now reads "pienentää sen neljäsosaan".
- L2-06: the significant figures are now justified by the mean of four measurements, and "enintään noin 2,5 %" is right (+2,4 %).
- L2-07: "noin 0,2 %" is right (0,21 %). The new sentence "g r² on sama kuin γM" is right.
- L2-05: 2,37² ≈ 5,6 is right.
- The kind changes in L2-06 and L2-07 (graph removed) fit tasks that draw no graph.
- All other answers are unchanged, and my round-1 recomputation still holds (20/20 within tolerance).
- Scope and plan are unchanged and still fit: L3-05 uses the fy5-4 prerequisite only.
