VERDICT: PASS
CONTENT-HASH: 35f7cbd9c952c5d4

## Blocking

## Polish
- solutions.md:75 (L2-03, Kuvaajan lukeminen) — "pisteitä jää tasaisesti ... eli sen kulmakerroin on näiden arvojen keskiarvo" presents the mean of the point-wise pV values (2002 kPa·ml) as if it equalled the best line through the origin (least squares 2009 kPa·ml). Both give 2,0 J, so nothing is wrong in the answer. — Fix: "kulmakerroin on likimain näiden arvojen keskiarvo".
- solutions.md:79 (L2-03, Vastaus) — the two-figure count follows the rule, but every pressure is read to 1 kPa (66 ± 0,5 kPa ≈ 0,8 %), so the data would support 2,01 J. Optionally say in one clause that the counting rule is what is applied.
- inquiry.json check-2 solution, Järkevyys — "3,6/0,03 = 120" repeats the substitution. The comparison with 101 kPa is the real check, and it is enough on its own; the repeated sum could go.

## Checked
- One script recomputed all 12 exercise answers. They match answers.py and exercises.json; the largest difference is 0,2 % (L2-01 2,02 → 2,0). L2-03: pV per point 1980–2030, mean 2002, least squares 2009 kPa·ml.
- The principles fit: Boyle (syringe, tank, rocket, SCBA, bubble, pump), isobaric (balloons, open envelope), isochoric (freezer, bottle, tyre). Each solution gives a correct reason (closed sample, which quantity is constant), and each unknown is solved in symbols first.
- Conversions: bar→kPa (the factor is a definition), kPa·ml → J, ρgh in Pa→kPa, °C→K. Gauge → absolute in L3-02 and L3-03.
- Rounding (round-1 fix verified): L1-02 and L2-01 now name 24,0 l and 6,8 l as the limiting data and count 160,0, 280,0 and 300,0 as four figures. Differences follow NOTES §2: L2-02 363 K − 273,15 gives units, so 90 °C. L2-04 ΔT = 90 K gives 890 m³. L3-02 351 → 303 − 101 = 202. L3-03 40,0 − 10,1 = 29,9.
- Reasonableness checks are real ratio estimates. They include the wrong Celsius results (negative volume, 25 °C, a factor of ten) and the wrong gauge result of 216 kPa. The side estimates are right: 7 kN on the freezer lid, about 40 min of SCBA air, about 1,8 m³ real-gas volume for Z ≈ 1,1, and 24 % of the hot air expelled.
- Worked example: 1,036 l → 1,0 l, limited by 0,80 l and 78 kPa. The +30 % and the pV check of 80,8 kPa·l are correct.
- inquiry.json: siirto 1,07 l (mistakes 2,10 and 0,00107). Check-2 120 kPa (mistakes 108 and 0,12). Ruisku pV is 5040, and the 30 ml row is 5430, 7,7 % higher. Pred-1 200 kPa / 5,00 J; pred-2 60,2 ml and 0,171 ml/K = 1/293; virhe 252 kPa; kertaus 30 N.
- Exit ticket: 160 kPa and 308/280 = 1,1. The misconception example gives 1,035 l (+3,5 %).
- sim.js: V₀ = 50 ml, p₀ = 100 kPa, T₀ = 293,15 K, and pV/T is constant in all three modes. The slider ranges, 20–100 ml and −50–150 °C, cover every value the experiments ask for. exp-1 locks mode and Tc, and exp-2 locks mode. The calc box calls the values model values.
- Scope is FY3; ρgh and F = pA come from the prerequisite lesson.
