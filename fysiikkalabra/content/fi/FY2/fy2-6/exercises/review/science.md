VERDICT: FAIL
CONTENT-HASH: 9bb9fde6012ead07
Round: 1

New since the last PASS (commit 18b454cd1): the order-of-magnitude multiple-choice task fy2-6-L1-09 (exercises.json, solutions.md, a comment in answers.py). Mode: full. Every numeric answer was recomputed again.

## Blocking
- content/fi/FY2/fy2-6/exercises/exercises.json:116–140 (L1-09) — **A, assessment.** The task does not separate the error that the lesson's Yleinen virhekäsitys names: using the rated power instead of the mean power. With rated power the answer is 3,0 MW · 8760 h : 5000 kWh = 5256 houses. Of the options 2 / 200 / 2000 / 20 000, the closest is "noin 2000" both on a log scale (the boundary is √(2000·20 000) ≈ 6300) and linearly. A student who ignores the 33 % therefore picks the keyed option and is told "Oikein". solutions.md:83 itself calls 5000 "väärin". So the 33 % datum is not needed to answer, and the solution contradicts what the key rewards. Fix: replace the "noin $20\,000$ taloa" distractor with "noin $5000$ taloa", with feedback that it uses the rated power although the wind turbine's mean power is only 33 % of it. Change "Valitse suuruusluokaltaan oikea vastaus" to "Valitse lähin arvo". Update "Muut vaihtoehdot" (solutions.md:83) to match.

## Polish
- exercises.json:139 (L1-09, "20 000" feedback, only if the option is kept) — "Silloin vuosi lasketaan kahteen kertaan" misnames the error. Dividing a year's production by one month's use counts house-months, not houses. Say that instead.
- exercises.json L2-07 and the L3-05 table — the IPCC life-cycle factors are CO₂ equivalents but are called "hiilidioksidimäärä" (carried over).
- exercises.json:398 (L3-05) — "Tehon säädettävyys: Tasainen" describes the output, not how adjustable it is (carried over).

## Checked
- L1-09 recomputed: 0,33 · 3000 kW = 990 kW; 990 kW · 8760 h = 8,67·10⁶ kWh; divided by 5000 kWh that is 1734 houses, which is "noin 2000". The figures in the solution and in the correct option's feedback agree with this.
- L1-09 distractors recomputed: 8670 MWh : 5000 = 1,7 ≈ 2; 3,3 % gives 173 ≈ 200; dividing by 417 kWh per month gives 20 800 ≈ 20 000. Each feedback's number and mechanism is right, except the wording noted under Polish.
- L1-09 data are realistic and marked as examples: a 3 MW turbine, a 33 % mean-to-rated ratio (typical in Finland) and 5000 kWh a year for a house. It uses the lesson's notation (P_ka, E = P·t, 8760 h) and there is exactly one correct option.
- answers.py vs exercises.json: one python run over all 19 numeric answers, all within tolerance; the largest deviations are L1-03 (+1,05 %), L3-02 (+1,0 %) and L2-07 (+1,0 %). L1-06 and L1-07 each have exactly one correct option.
- FY2 scope: only E = Pt, shares and factor × energy are used.
