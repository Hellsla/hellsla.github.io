VERDICT: PASS
CONTENT-HASH: f6ad08df6e7380d7
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- s7 c closing sentence (round-1 Blocking): now "jokainen kilometri vaatii akusta enemmän energiaa ... Lisäksi kylmästä akusta saadaan vähemmän energiaa. Siksi toimintamatka lyhenee." Right: consumption per kilometre rises and the usable energy falls; it agrees with b's judgement of the equal-energy assumption and with the fourth criterion of c.
- s7 b Järkevyys: measured 21,2 and 21,6 kWh/100 km are said to be other cars' values that give only the order of magnitude; correct, and the model's 27 kWh (75 kWh / 279 km = 26,9) is unchanged. Factor 1/0,62 = 1,61.
- s7 c rubric: thermal criterion without the combustion-car clause still matches the task; electricity criterion accepts either the heater's P = UI or the larger internal resistance (R_s I^2, lower terminal voltage); the solution shows both.
- s7 d text: "toimintamatka jäi suhteellisesti eniten ilmoitetusta" states the same fact as before (Lucid Air −45,8 %), agrees with the solution and rubric.
- s7 e text: now asks for at least three factors, as the rubric requires; the solution names nine.
- unit.md: internal energy defined as the sum of the particles' kinetic energy and the energy of their interactions: agrees with the guardrails.
- `python scripts/practice.py check units/fy9-energia`: OK (7 tasks, 105 points). Hash equal at start and end.
