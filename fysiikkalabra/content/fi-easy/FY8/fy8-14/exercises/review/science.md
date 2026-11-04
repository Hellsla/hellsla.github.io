VERDICT: PASS
CONTENT-HASH: 1b0ae72e68f858d4

## Blocking

## Polish
- solutions.md:109 "Säde B puolittuu siis noin kolme kertaa useammin" — reads as "three times as often" (3,7 : 0,56 ≈ 6,6). Write "noin kolme kertaa enemmän kuin säde A" or "puolittuu noin kolme kertaa lisää". The same wording is in the Finnish original.
- solutions.md:49 "se pienenee selvästi alle 50 %" — still reads as "falls below 50 %". Write "pienenee vähemmän kuin puolella: noin 15 %". Carried over.
- exercises.json L3-02 — 20 keV stated, 30 keV assumed without a reason. Carried over.
- L3-03 — the half-value thickness is a narrow-beam value; buildup means a real shield needs somewhat more lead. Carried over.

## Checked
- One script recomputed every answer from the fi-easy task text: 25 %, 37,67 → 38 MBq, 5,7 mSv, 0,10 J, 31,52 → 32 kBq, 17 029 → 17 000 a, 0,303 mm, 572,5 → 570 d, 10 µSv, 15,6 → 16 Gy, 8,87 → 8,9, 16,86 → 17 mm. All within tolerance; lessons/FY8/fy8-14/answers.py agrees.
- Every number in exercises.json and solutions.md matches the passed Finnish version.
- Split sentences keep each task's conditions: L1-02 nothing leaves the body, L2-02 background subtracted and 60 keV, L2-04 point source and constant dose rate, L3-01 other beams not through the entry point, L3-02 equal-length beams.
- Solutions solve symbolically first; conversions and rounding by the limiting datum are right; the added "eksponentissa eli potenssin kohdalla" gloss is correct.
- Data agree with the fi-easy lesson (Tc-99m 6,01 h, Am-241 432 a, C-14 5700 a, 5,1 mSv/a, Pb 3,9 / 0,26 mm).
