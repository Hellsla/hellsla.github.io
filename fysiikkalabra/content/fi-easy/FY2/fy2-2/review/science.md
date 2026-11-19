VERDICT: FAIL
CONTENT-HASH: 3cf4d09f285b2d5a

## Blocking
- lesson.md:560 — (A) The worked example's Tulos step says "Kokonaislukuna annettu $110\,\text{kJ}$ on tarkka arvo". That is wrong. The muscles' output is a given value, not an exact number, and an integer is not exact just because it is an integer. The house rule (NOTES §2, guardrails "Values and significant figures") says a given value's trailing zeros are significant. Fix: justify it with the subtraction rule, as the transfer task's solution already does: "Vähennyslaskussa tarkkuuden ratkaisee epätarkin tieto. $0{,}45\,\text{MJ} = 450\,\text{kJ}$ tunnetaan kymmenen kilojoulen tarkkuudella, joten tulos on $340\,\text{kJ}$."

## Polish
- lesson.md:442 — The photo caption says "lämmöksi", but the rest of the FY2 text says "lämpöenergiaksi". Write "lämpöenergiaksi" to keep the chapter consistent.
- inquiry.json:204 (johtopaatos model) — "Suuri osa muuttuu kuitenkin joka vaiheessa lämpöenergiaksi" does not fit the chain table: the grid step loses $2\,\text{MJ}$ of $40\,\text{MJ}$, and the transfer task calls transmission losses small. Suggest: "Joka vaiheessa osa muuttuu lämpöenergiaksi, ja lopulta suuri osa on hajaantunut ympäristöön."

## Checked
- I recomputed everything in one script: example 450 − 110 = 340 kJ; pysähdy 380 kJ, 4200 J, 3 MJ, 160; chain 66 MJ (60 + 2 + 4); transfer 51 GJ; checks 7,3 and 100; exit ticket 9 kJ; common mistake 1800 kJ. All right.
- Prediction 2: π·R²·1361 W/m²·3600 s = 6,25·10²⁰ J, compared with 620 EJ (2023). The "tuhat vuotta" option gives about 41 days, so "noin 40" holds. Exactly one option is correct in every choice item, and every distractor's feedback is right.
- Petrol 32 MJ/l (0,745 kg/l × 43 MJ/kg); tank 1,6 GJ; OL3 1,6 GW × 24 h = 138 TJ; apple 0,98 J and the other sim.js values have plausible magnitudes.
- The tikapuut figure is to scale: 33,2 px per decade; the 1 kJ, 10 MJ, 1,6 GJ and 140 TJ points sit at 195,6, 328,4, 401,6 and 565,7 px.
- The sailyminen Sankey is to scale: 96 px = 24 + 72 px for 800 = 200 + 600 kJ.
- The sim's simState gives E_MJ and E_EJ for koe-1 and koe-2 at their initial objects. The koe-2 capture shows 6,2·10²⁰ J = 620 EJ, which agrees with the johtopaatos model.
- The sim's model box says the values are rounded magnitudes with sources or estimates, and that the scale is logarithmic.
- Scope: no FY3 or FY4 formulas.
