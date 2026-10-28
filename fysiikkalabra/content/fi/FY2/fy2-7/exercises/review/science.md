VERDICT: PASS
CONTENT-HASH: 77518f792a45647e

## Blocking

## Polish
- lessons/FY2/fy2-7/answers.py:16 — `1.20 / 0.80 * 1000` prints 1499.9999999999998; `1200 / 0.80` or a round() gives a clean 1500 (gate passes either way).
- exercises/solutions.md:8 — L1-01 "kolme merkitsevää numeroa kuten lähtötiedoissa": 4,0 % has two figures; the reason is that η = 0,960 is known to three (as the lesson example says).
- exercises/solutions.md (L1-05 Järkevyys) — rounding 2,5 kW up to 3 kW and getting 72 kWh is a loose check; 2,5 · 24 = 2,5 · 20 + 2,5 · 4 = 50 + 10 would be a real check.

## Checked
- All 12 answers recomputed with my own formulas (η = 1 − p, E_perille = ηE_lähtö, E_lähtö = E_perille/η, E = Pt): 480, 33, 96,0, 120, 60, 150, 1500, 10,96→11, 1200, 21,04→21, 13,0, 65,7→66 — all match exercises.json and answers.py within tolerance.
- The "percentage of the energy sent" model is used consistently, including L2-01 (base trap explained correctly: 120 MWh would be 17 %) and L3-01 (21 vs naive 18 MWh explained).
- Power tasks (L1-04, L2-04) apply the loss share to power as the brief's "Laskeminen häviöprosentista" allows; L2-03 and L3-03 use P = E/t with constant power stated.
- Magnitudes realistic: 4 % grid loss, ~9 % district-heat loss, "vanha/huonosti eristetty" networks at 20 %; 20 MWh/year per detached house; 11 MW mean loss for a 2,4 TWh region.
- Conversions right (GWh→MWh, TWh→MWh, kWh→MWh); every solution states given/asked, principle, symbolic solution before numbers, rounding reason, check.
- Significant figures follow the limiting datum (20 %, 80 %, 4,0 %, 9,0/6,0 %, 20 MWh).
- Notation (E_lähtö, E_perille, E_häviö, η, P_häviö) matches the brief.
- Scope: FY2 energy transfer only, no electrical or conduction formulas.
- Hash identical at start and end.
