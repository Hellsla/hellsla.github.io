VERDICT: PASS
CONTENT-HASH: a49e621fe4bda732

Delta review: inquiry task `data-fi` (Finland's wind power 2024, 20,2 TWh, average power) changed in fi, fi-easy and en inquiry.json and in lessons/FY2/fy2-6/lesson-answers.py. The hash was the same at the start and at the end.

## Blocking
None.

## Major
None.

## Polish
- lesson.md:290 (summary) says "keskiteho on vuosienergia jaettuna vuoden tuntimäärällä $8760\,\text{h}$" with no condition. Theory line 153 does give the condition ("Tavallisessa 365 vuorokauden vuodessa"), and every other 8760 h use is a generic or hypothetical year (worked example 14 GWh, OL3 full-power year, 1,0 MW check, the 365·24 h distractor, the exercises). None of them uses 2024 data, so nothing contradicts the task. Writing "tavallisen vuoden tuntimäärällä" in the summary would match the theory line and the leap-year task. Category C, not a finding.
- Tolerance 0,02 GW also accepts 2,31 GW (20,2 TWh : 8760 h). That is a sensible leniency, since the 0,3 % difference is below the data's precision. Noted only.

## Checked
- Recomputed: 366 · 24 h = 8784 h. 20,2·10⁹ kWh : 8784 h = 2 299 635,7 kW, so the solution's 2 299 636 kW is right, and ≈ 2,30·10⁶ kW = 2,30 GW. answers.py gives 2,299636. Old value: 2,306 GW.
- Significant figures: 3, matching 20,2 TWh. 8784 h is exact for the calendar year 2024. The phrases "vuonna 2024 (karkausvuosi) on 8784 h", "karkausvuoden 2024 tuntimäärä 8784 h on tarkka luku" and the en "the leap year 2024" are physically and factually correct (2024 is a leap year, and the statistic is for the calendar year).
- Mistake 2300 (MW): 2299,6 MW, and its feedback 2300 MW = 2,30 GW is correct. Mistake 0,0023 (TWh→10⁶ kWh slip): 20,2·10⁶ : 8784 = 2299,6 kW = 0,0023 GW, correct and unchanged.
- Hint 3 now divides by 8784 h. Estimate: 20·10⁹ : 8800 = 2,27·10⁶ ≈ 2,3 GW, consistent. The rated-power sentence is still valid.
- No 2,31, 2306 or 2,306 is left in fi, fi-easy or en. The three languages carry identical numbers.
- Consistency: exercise L2-08 (exercises.json, solutions.md, answers.py) already uses 8784 h → 2,30 GW. The inquiry task and the exercise now agree. lesson.md has no other 2024 wind average-power figure.
