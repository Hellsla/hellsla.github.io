VERDICT: PASS
CONTENT-HASH: a6262ad6a5a59e36
SCOPE: delta added-exercise from 166963488269ae93 base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- exercises.json (fy6-16-L2-09) — the question is not the last sentence ("Kuinka paljon ... maksaa? Lue tarvittavat arvot ... ja vastaa euroina."). Reorder: "Lue tarvittavat arvot kuvaajasta ja vastaa euroina. Kuinka paljon talon sähkö maksaa yhteensä kello 18-22?"
- fy6-16-L2-09 uses the same house data as L2-05 (hourly table before the charging station, main fuses); only the question differs (cost, not fuse load). Acceptable, but the cost is easy: a step more would fit level 2 better, e.g. the cost of the hour of the highest power only, or the cost with the car charging; optional.
- solutions.md (fy6-16-L2-09, Järkevyys) — the second sentence repeats the first calculation; replace with one check: "Jos teho olisi koko ajan 7 kW, hinta olisi 4,5 €, joten tulos on sitä pienempi."

## Checked
- Text only (no render) of the added fy6-16-L2-09.
- Recomputed: W = (2 + 5 + 7 + 3) kW · 1,0 h = 17 kWh; K = 0,16 €/kWh · 17 kWh = 2,72 €; answer 2,72 with 2 % tolerance accepts 2,7 €.
- Figure talo-ex: four constant hourly steps 2, 5, 7, 3 kW, grid 1 h and 1 kW; the description gives the same data and no energy or price.
- Level 2: energy as area of four rectangles (not simply P · t) and a snt to € conversion; solution states why a sum of rectangles works and does the conversion explicitly.
- Everyday context (home electricity bill), fits the chapter's cost and energy theme from fy6-7; no repeat of the worked example or of L1-04 (energy given).
- Finnish and units correct ($16\,\text{snt/kWh}$, kWh and € in the solution).
- Hash unchanged at the start and end.
