VERDICT: FAIL
CONTENT-HASH: 74f029926fd28de2

## Blocking
- solutions.md:125 (fy2-2-L1-06 Mallivastaus) — A: "Sillä on lukuarvoista toiseksi suurin" is false, because 3 200 000 is the largest numeric value of the four. It also lets a student pick the largest number and be right. Fix: make the correct option one that does not have the largest number, e.g. correct "0,0033 GJ" (3,3 MJ) and the distractor "3 000 000 J" (3,0 MJ), with the feedback, answer and solution updated to match.
- solutions.md:135 (L1-07 Järkevyys) — A: 1200 kJ is not "noin neljäsosa" of 10 MJ. It is about one eighth (12 %). Fix: "noin kahdeksasosa (12 %)".
- solutions.md:165 and exercises.json:166 (L2-06) — A: "Tulos sopii siihen, että päivän ruoan energia on kymmenisen megajoulea" is false, because 2,5 MJ is a quarter of 10 MJ. The task calls the 2,5 MJ "päivän ruoan energia", which contradicts L3-05 (10,35 MJ) and the lesson (10 MJ). Fix: in the task write "laskee aamupalan, lounaan ja välipalan energian yhteen", and in Järkevyys write "noin neljäsosa päivän tarpeesta 10 MJ, mikä sopii kolmelle kevyelle aterialle".

## Polish
- solutions.md:186 (L3-04) — "tuhansien talojen" understates the figure: 3,2·10⁶ GJ divided by about 70 GJ is about 45 000 houses. Write "kymmenien tuhansien".
- exercises.json:86 (L1-08) — the entry has no `kind` field. Add one.
- solutions.md L2-07 — the Periaate gives the model as E = ks, but the line that is read passes through (0; 8 kJ). Write "E on likimain verrannollinen matkaan".

## Checked
- I recomputed every new answer in one script: L1-07 1200 kJ; L1-08 350 MJ; L2-05 750 + 480 + 380 = 1610 kJ, so 7,32 km; L2-06 2,5 MJ; L2-07 least-squares slope 250,5 kJ/km (intercept 7,7 kJ), so 5,99 km; L3-04 64,8 / 504 / 4320 / 3,2·10⁶ GJ, ratio 49 383, so 49 000; L3-05 food 10,35 MJ against 11,45 MJ used, a deficit of 33 MJ, so 0,89 kg. All of them match answers.py and the solutions.
- L1-06 has one correct option. In L2-07 the slope is read from points on the fitted line, and the tolerance of 0,04 matches 5,8–6,2 km. The conversions in L3-04 and the energy fate in L3-05 are right.
- Scope: no mgh, no c·m·ΔT, no work or force. The plan's kettle experiment, which would need cmΔT, was correctly replaced by the walking-energy graph task.
- No new task duplicates an existing one, and the levels fit. The hash did not change.
