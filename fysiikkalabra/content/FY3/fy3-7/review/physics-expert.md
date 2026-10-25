VERDICT: PASS
CONTENT-HASH: e42d07cd351f74e0
## Blocking
(none)
## Polish
1. exercises.json:98 (L3-03): The loss power is equal in both runs only if the vessel and the water level are about the same. Run 1 removes 196 g. — Fix: add "Astiassa on kummankin mittauksen alussa yhtä paljon vettä." (optional).
2. solutions.md:95: You could add one clause on why the 400 W run is worse (2,67 against 2,45 MJ/kg): the same 60 W loss is a larger share of the smaller power. — Fix: "…ja pienemmällä teholla virhe on suurempi, koska sama häviöteho on suurempi osa tehosta."
## Checked
- `lint_lesson.py fy3-7`: 0 errors, 0 warnings. The hash was the same at the start and at the end (e42d07cd351f74e0).
- lesson.md:36 SVG: the drawing is to scale for 1 kg from −30 °C to 140 °C (0,155 px/kJ, 0,9 px/K). Every segment is within 0,5 px of the model. The plateaus are 52 : 351 px (334 : 2260). The slopes are ice 2,70, water 1,38 and steam 3,00 px/px. That makes ice and steam 1,95 and 2,17 times as steep as water (physical values 2,00 and 2,10). The round-1 blocking item is fixed.
- lesson.md:31: on a (Q, T) graph the slope is 1/(cm), so "pienempi c → jyrkempi" is correct.
- lesson.md:19, :21–29, :53–57: "Vakiopaineessa", the constants table (c values are standard; steam 2000 J/(kg·K) is fine) and the example's assumption and loss explanation are all correct.
- L3-03 physics: (P − P_h)t = rΔm for each run. Subtracting the equations gives r = 400 W · 600 s / 0,106 kg = 2,264 MJ/kg. The data are consistent: both runs give P_h = 60,4 W, which is a realistic loss for an open vessel. Each single run gives 2,45 or 2,67 MJ/kg, both too large, and the solution explains this correctly. The task needs two equations, so it does not repeat the example.
- answers.py: every line uses the right formula, unit conversion and sign. The L3-01 assert (all ice melts) is correct.
- I recomputed three answers by hand: L3-03 2,264 MJ/kg, L3-01 9,676 °C and L2-02 278,85 kJ. All three match.
- solutions.md: the reasoning holds. Shares: 90 % (L2-02), 24 % (L2-04), 87 %/13 % (L3-02). The 0 °C-water alternative in L3-01 gives 21 °C. The ice thicknesses (5 cm and 4 cm) are realistic.
- exit-ticket.json q1: the micro-model answer is correct (energy raises the interaction energy and the particles' kinetic energy does not grow). q2 and q3 are correct.
- sim.js:31–42, 64–70: the piecewise Q(T) with Q = Pt is exact. Plateau lengths sm/P and rm/P are correct. With the sliders locked (:67) and reset on input (:53), Q = Pt holds for the whole run. The note says the steam is assumed to stay in the vessel.

Python output:
```
{"fy3-7-L1-01": 400.8, "fy3-7-L1-02": 0.904, "fy3-7-L1-03": 15.03, "fy3-7-L1-04": 67.8, "fy3-7-L1-05": 167, "fy3-7-L2-01": 9.416667, "fy3-7-L2-02": 278.85, "fy3-7-L2-03": 35.928144, "fy3-7-L2-04": 0.9383, "fy3-7-L3-01": 9.676058, "fy3-7-L3-02": 27.033333, "fy3-7-L3-03": 2.264151}
ice model 9.8 27.0 drawn (10, 27) | melt 51.8 (52) | water 64.9 90.0 (65, 90) | boil 350.3 (351) | steam 12.4 36.0 (12, 36)
slopes px/px ice 2.70 water 1.38 steam 3.00 ratio 1.95 2.17 phys 2.00 2.10
L3-03 r 2264150.9 loss W 60.38 60.38 single 2448979.6 2666666.7
```
