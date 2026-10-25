VERDICT: FAIL
CONTENT-HASH: 0a88a4ba2db42db7
## Blocking
1. lesson.md:26 — The heating-curve SVG has Q on the x axis, so slope = 1/(cm). The drawn slopes are ice 30/30 = 1,0, water 90/60 = 1,5 and steam 40/60 = 0,67 px/px. That makes ice and steam heat more slowly per joule than water, which implies c(jää), c(höyry) > c(vesi). Physically, ice is about 2,0× steeper than water (4190/2100) and steam about 2,1× steeper (4190/2000), as the sim draws them. Students meet "read c from the slope" tasks, so this teaches the wrong relation. — Fix: keep the plateau ratio and make the ice and steam segments steeper than the water segment, e.g. `points="70,218 76,200 116,200 170,110 450,110 462,74"`. Then set the dashed lines' x2 to 116 and 170 and move the labels to "sulaa" x=96, "vesi lämpenee" x=150 and "höyry" x=465.
## Polish
1. lesson.md:43 — The text says "Kuumentimen energia siirtyy kokonaan veteen" as a fact, and :47 then says part of it goes to the air. — Fix: "Oletetaan, että kuumentimen energia siirtyy kokonaan veteen". Also note that once the water boils, the vessel no longer warms up, so the loss goes mainly to the surroundings ("ilmaan").
2. lesson.md:19 — "lämpötila ei muutu" has no stated condition. — Fix: add "(vakiopaineessa)". This ties it to the boiling-point/pressure paragraph.
3. sim-spec.md / sim.js — An open container whose steam is heated to 130 °C is an idealisation (the steam would escape). — Fix: add one sentence to the note: "höyry oletetaan pysyvän astiassa".
## Checked
- `lint_lesson.py fy3-7`: 0 errors, 0 warnings. Hash unchanged at start and end (0a88a4ba2db42db7).
- Q = sm and Q = rm, the equal heat released on freezing and condensing, the micro-model, sublimation, and boiling point vs pressure (mountain, pressure cooker) are all correct and in FY3 scope (MAOL immersion-heater method, lesson.md:41–47).
- Ratios in lesson.md:10 and :50: r/s = 6,77 ("lähes seitsemän"), r/(c·100 K) = 5,39 ("yli viisi"), s/c = 79,7 K ("80 °C").
- Example: 300 kJ / 0,128 kg = 2,344 MJ/kg, 3,7 % above 2,26. Losses push r up, so the stated direction is right.
- `answers.py`: every line uses the right formula, unit conversion (g→kg, kJ/MJ, s→min) and sign. Released heat is positive as worded. The L1-05 data are self-consistent (m = 0,50 kg gives 18,9 kJ for 18 K).
- Hand re-check of the three least-trusted answers: L2-02 278,85 kJ, L3-01 9,676 °C, L3-03 73,98 %. All match.
- Magnitudes are realistic: 4,9 cm of first-night ice (Stefan bound ≈ 8 cm at −10 °C), 4 cm/day of spring melt, 27 K of stone cooling per ladle.
- solutions.md reasoning is sound: the 0 °C water alternative gives ≈ 21 °C, the 87 %/13 % sauna split, the 11 % melting share, and mass cancels in the L3-03 share.
- exit-ticket.json: 167 kJ ≈ 170 kJ (2 sf), and the plateau/slope answers are correct.
- sim.js:29–40, 64–66 match the piecewise Q(T) with Q = Pt exactly (no approximation). The plateau times sm/P and rm/P are correct, and SPEED 60 matches the note.

Python output:
```
{"fy3-7-L1-01": 400.8, "fy3-7-L1-02": 0.904, "fy3-7-L1-03": 15.03, "fy3-7-L1-04": 67.8, "fy3-7-L1-05": 167, "fy3-7-L2-01": 9.416667, "fy3-7-L2-02": 278.85, "fy3-7-L2-03": 35.928144, "fy3-7-L2-04": 0.9383, "fy3-7-L3-01": 9.676058, "fy3-7-L3-02": 27.033333, "fy3-7-L3-03": 73.977087}
L2-02 kJ 278.85 | L3-01 C 9.67606 | L3-03 % 73.977 | example r 2.34375 MJ/kg (ratio 1.037)
svg slopes: ice 1.0, water 1.5, steam 0.67; physical slope ratio ice/water 2.00, steam/water 2.10
```
