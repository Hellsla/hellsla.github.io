VERDICT: FAIL
CONTENT-HASH: 07056cb7bbe3da5d
SCOPE: delta added-exercise from caaeaa93666bca57 base 81db4a6fd727

## Blocking
- fy5-17/exercises/solutions.md (L2-09, Järkevyys) — **A** (wrong cause). The solution says "kaiku C on viimeinen, koska sen jälkeen ei ole enää rajapintoja" and "Reisi on noin 7 cm syvä". The thigh does not end at C. The strong last echo is the bone, which reflects and absorbs almost all of the ultrasound, so no echo comes from behind it. Fix: "Kaiku C on luusta: luu heijastaa ja vaimentaa ultraäänen lähes kokonaan, joten sen takaa ei tule kaikuja. Syvyys 6,9 cm sopii reisiluun etäisyydeksi ihosta."

## Polish
- fy5-17/exercises/solutions.md (L1-09, Vastaus) — "Aika 20 ms on sovittu tarkaksi" is a convention the course does not use. 20 ms has 2 significant figures, so give 14 m and drop "tarkemmin 14,0 m" (the 4 % tolerance accepts both).
- fy5-17/exercises/exercises.json (L1-09) — Under ice the water is 0 °C only near the ice; deeper water in a lake is about 4 °C, and the pulse also crosses the ice. Both effects are inside the 4 % tolerance. Saying "oletetaan koko vesi 0-asteiseksi ja jään paksuus pieneksi" would avoid a wrong picture.

## Checked
- MAFY value: water (0 °C) 1402,4 m/s is the VERIFIED row fy5-17 in docs/mafy-arvot.tsv. The hint names only the section and the table.
- L1-09: d = vt/2 = 1402,4 · 0,020/2 = 14,02 m (recomputed). The comparison with 1540 m/s (15,4 m, +10 %) is right.
- L2-09: the A-scan figure (figures.py) has echoes at 20, 50 and 90 µs, narrow (σ 0,9 µs) and on the 5 µs grid lines, so they are read exactly. Δd = 1540 · 40 µs/2 = 3,08 cm, with d_B = 3,85 cm and d_C = 6,93 cm (recomputed).
- L2-09's 3 significant figures fit v = 1540 m/s and the exact grid reading; the tolerance is 2 %.
- No other exercise uses fy5-17/a-scan. L2-05's A-scan is a table, so nothing is repeated or given away. The alt text gives the same times as the drawing.
- answers.py agrees with exercises.json. The notation d = vt/2 is the lesson's.
- The hash was the same at the start and at the end.
