VERDICT: PASS
CONTENT-HASH: 169cf2ec47db5201
## Blocking
(none)
## Polish
1. solutions.md:71 (fy3-5-L2-04) — "smoothie lämpenee": with frozen berries, part of ΔU can melt ice at about 0 °C, so the smoothie need not warm. — Write "smoothien sisäenergia kasvaa (se lämpenee tai sen jääkiteet sulavat), vaikka sekoitin ei lämmitä sitä millään vastuksella".
2. exercises.json:72 (fy3-5-L2-04) — Q = 2,0 kJ through the jug walls in 40 s is about 50 W of heat inflow. That is plausible but high (estimate 10–25 W). — Optionally use Q = 1,0 kJ and ΔU = 11 kJ. This keeps W = 10 kJ and t = 40 s.
3. lesson.md:8 — Heat is introduced only through contact ("kun kaksi … kappaletta koskettavat"). Radiation also transfers heat. — "kun kaksi eri lämpötilassa olevaa kappaletta ovat esimerkiksi kosketuksissa".
## Checked
- Lint 0/0. answers.py output matches all 12 `answer` values. Hash was the same at start and end.
- ΔU = Q + W (W > 0 when the surroundings do work on the system) has the same signs in lesson.md:15–17, the SVG, the example, every solution, answers.py and all three exit-ticket answers. Every answers.py line reads its signs correctly from the task text.
- Round-1 fixes are correct: L3-01 W = Fs = 18 J, solutions.md:77/:93 limited to a gas, lesson.md:43, :10, :52, glossary "eristetty systeemi".
- L3-03 (recomputed by hand): ΔU_A = 400 − 150 = 250 J and Q_B = 250 + 60 = 310 J. The path independence is correctly justified for a gas, and both routes are physically possible.
- L2-04 (recomputed by hand): W = ΔU − Q = 10 kJ, t = W/P = 40 s.
- L3-02 (recomputed by hand): h = 1000 J / (12 · 5,0 kg · 9,81 m/s²) = 1,699 m → 1,7 m. mgh comes from fy3-2:23.
- Exit ticket 3: the isolated system "termospullo ja sen sisältö" keeps U constant while heat flows from the coffee to the inner wall and air inside the boundary.
- Scope: first law only. There is no cmΔT, efficiency or second law.
- Magnitudes are realistic (pump 150 J, power stroke 320 J, balloon W/Q = 2/7).

Python output:
```
{"fy3-5-L1-01": 570, "fy3-5-L1-02": -8.4, "fy3-5-L1-03": 250, "fy3-5-L1-04": -500, "fy3-5-L1-05": -70, "fy3-5-L2-01": -15.0, "fy3-5-L2-02": 160.0, "fy3-5-L2-03": 800.0, "fy3-5-L2-04": 40.0, "fy3-5-L3-01": -18.0, "fy3-5-L3-02": 1.698947, "fy3-5-L3-03": 310}
```
