VERDICT: PASS
CONTENT-HASH: d683ac7a621baa2e

## Blocking

## Polish
- exercises/solutions.md:176 (L2-07 Vastaus) — "299 kWh, kolme merkitsevää numeroa … noin 300 kWh" gives two precisions. The by-eye fit limits it, so give 300 kWh (two significant figures).
- exercises/solutions.md:172 (L2-07) — give the origin line its physical reason (guardrail "Fits"): "lukema oli 0,00 kWh hetkellä t = 0".
- exercises/solutions.md:196 (L3-05 c) — say which way the waste heat acts: the old fridge heats the home more, so with electric heating part of the saving is lost in winter.
- exercises/solutions.md:161 (L2-06) — the heading "Kuvaajan lukeminen" sits over a table. Use "Taulukon lukeminen".

## Checked
- All 20 answers recomputed in one script with my own formulas. New ones: 1,215 €; 25 h; 733,65 kWh; 335,1 W; 299,1 kWh (least squares through the origin; 299,3 kWh from the reading); 0,930 €; 12,96 a. All agree with answers.py and exercises.json. A by-eye L2-07 line (1,60–1,68 kWh) stays inside the 5 % tolerance.
- L2-05: daily energies 0,45 / 0,44 / 0,36 / 0,60 / 0,16 kWh. The vacuum cleaner is the largest and lighting second, as the solution says.
- L2-06: daily differences of 7,2–9,2 kWh are realistic. 56,3 kWh / 168 h = 335 W, and the cost is 9,0 €.
- L3-04: the costs add up to 267,44 snt over 19,0 kWh (14,1 snt/kWh). The 2,4 kWh of other use in 16–20 is consistent. Saving = 6,0 kWh · 15,5 snt/kWh. Part c names the right cause.
- L3-05: the saving is 37,74 €/a and the lifetime gain 77,1 €. The model's assumptions are stated in the task.
- L1-06 has exactly one correct option, and every distractor's feedback is right. L1-08's error (E·P) is explained with units.
- Notation E, P, t, a, K follows the brief. The data are labelled esimerkkiaineisto. Everything stays in scope.
- The L3-04 table at 1280 px renders cleanly.
- Set: 8/7/5, with no duplicates and every task matching the FY6.md plan.
