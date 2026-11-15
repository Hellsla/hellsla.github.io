VERDICT: PASS
CONTENT-HASH: 20b8e6c3a3fdd3a2

## Blocking

## Polish
- exercises/solutions.md:256 (L2-08) — "arvot luetaan $0{,}4\,\text{kW}$:n … ruudukkoviivoilta", but the cooling stage $0{,}2\,\text{kW}$ lies midway between the dryer graph's $0{,}4\,\text{kW}$ gridlines — say it is read halfway between the lines $0$ and $0{,}4\,\text{kW}$.
- exercises/solutions.md:245 (L1-10) — "Vastaus kelpaa, kun se on noin $\pm 4\,\%$ sisällä" is checker information, not part of the model solution — drop it.
- exercises/solutions.md:179 (L2-07) — "Pisteet ovat silloin suoralla" — per the fit guardrail write "lähes suoralla" (the next step already says the points scatter about the line).

## Checked
- All 21 numeric answers recomputed in one script from the task texts (E = Pt, E = UIt, P = U²/R via I = U/R, K = aE + K_perus, payback H/(aΔE)): all agree with exercises.json and answers.py; L2-07 by my least-squares line through the origin ($0{,}03414\,\text{kWh/h}$, $1{,}639\,\text{kWh}$ at $48\,\text{h}$, $299{,}1\,\text{kWh/a}$) is 0,08 % from the key, inside its 5 %.
- Rounded answers a student would give (1,2 €, 11 kWh, 11 MJ, 7,3·10² kWh, 3,0·10² kWh, 13 a) all inside tolerance; significant-figure reasons follow P7 (230 V three figures in L1-03 and L3-03; 90 W, 60 W two; 1200 W four).
- L2-06 daily differences 7,7 / 7,2 / 8,2 / 7,5 / 9,1 / 9,2 / 7,4 kWh, sum 56,3 kWh, 335 W, 9,0 €.
- L3-04 period costs, 267,44 snt, 19,0 kWh, 14,08 snt/kWh, saving 93 snt; the 6,0 kWh heater load fits inside the 8,4 kWh of the 16–20 period and 3 h inside a 4 h period; prices stated as constant per period.
- L3-05: 222 kWh, 37,74 €/a, 12,96 a, 77,1 € (≈16 %); the "old fridge heats the flat" limitation is stated with its condition (electric heating).
- L1-09: every distractor really comes from the unit error its feedback names (0,0010; 3,6; 60 Wh→kWh; 3600); exactly one correct option. L1-06 single correct option, feedbacks right (kWh energy, not power).
- Figures washer and dryer: polylines carry exactly the values the solutions read; alt texts give the same values, no energy shown.
- Magnitudes realistic (iron 5,2 A, kettle 2,0 kW, standby 4,5 W, fridge 34 W mean, 8 kWh/d flat); scope within fy6-7 (E = Pt, kWh, bill, savings) and the fy6-6 prerequisite.
- Solutions complete, symbolic first, conversions right, reasonableness checks real.
- Hash identical at start and end.
