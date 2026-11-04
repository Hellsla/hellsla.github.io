VERDICT: FAIL
CONTENT-HASH: 2dcdab9668d10d18

## Blocking
- content/fi/FY6/fy6-16/exercises/exercises.json:127 (L2-05 text) and solutions.md:159 (c) — B: the table gives one power value for each hour, but the main fuse responds to the current at each moment. The conclusion "muina tunteina kuormanhallintaa ei tarvita" holds only if the house power stays at the table value throughout each hour, and the task never states that (guardrails: state the model's assumptions in the task). For example, an hour that averages 5,2 kW can include a sauna-stove peak of 9 kW. — Fix: add to the task "Oletetaan, että talon teho pysyy kunkin tunnin ajan taulukon arvossa." In c), write "...ei tarvita tämän oletuksen mukaan; todellisuudessa tunnin sisäiset huiput voivat vaatia kuormanhallintaa."

## Polish
- content/fi/FY6/fy6-16/exercises/exercises.json:179 (L2-07) — at 3,0 h the power is still 1,4 kW, so the charge has not ended. Say that a) asks for the energy "mittausjakson 0–3,0 h aikana" and b) for the mean power over that period.
- content/fi/FY6/fy6-16/exercises/solutions.md:149 (L2-05 Kysytty) — part c) is missing from Kysytty. Add "c) milloin 11 kW sallitaan".
- content/fi/FY6/fy6-16/exercises/exercises.json:61 (L1-06 correct feedback) — "60 kWh:n akun täyttö vie tästä kuluvan ajan" does not read clearly. Suggested wording: "tyhjän 60 kWh:n akun täyttö vie ilman häviöitä noin 60 kWh : 11 kW ≈ 5,5 h".
- content/fi/FY6/fy6-16/exercises/solutions.md:196 (L3-04) — the rounding reason "kolme merkitsevää numeroa" ignores the 2-digit price 15 snt/kWh. Give 1370 € as rounded to 10 €, since the electricity cost (390 €) has two significant figures.
- docs/exercise-bank/FY6.md (fy6-16) — two plan items are not covered: the price comparison at different times (Taso 2) and the emission comparison (Taso 3, L3-04 has costs only). Update the plan, or add a c)/d) part.

## Checked
- All 20 answers recomputed in one script: answers.py, exercises.json and the solutions agree (L1-07 40,7 kWh; L1-08 64 W; L2-05 10,45 kW; L2-06 5,29 h; L2-07 22,85 kWh, mean 7,62 kW; L3-04 14 640 km, 390,4 €, 1760,5 €, difference 1370,1 €, public charging 1171,2 €; L3-05 7,61 A, 0,408 Ω, 23,6 W and 104 W).
- L2-05 b/c: P_max = 3UI_p = 17,25 kW, the limit 6,25 kW for 11 kW, only 19–20 exceeds it.
- L2-06: both planted errors (whole battery instead of 60 %, efficiency missing) are the ones named, and the corrected t = W_akku : (ηP).
- L2-07 trapezoid sum checked interval by interval.
- L3-05: the single-phase charger loads one phase; the even split of the house loads is stated; the reasoning about main fuse and cable heating is sound and does not overstate 104 W as dangerous.
- L1-06: exactly one correct option; the distractor feedback is right.
- Cost uses grid energy W_akku : η, as the brief says. P = 3UI holds only with equal phase currents, and the tasks state that.
- Level fit 8/7/5, no duplicates of existing tasks, all inside FY6 scope.
