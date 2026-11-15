VERDICT: PASS
CONTENT-HASH: a2e5e2d92c27c53b
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- Round-1 Blocking (s7 c closing paragraph): now "Jokainen kilometri vaatii siksi akusta enemmän energiaa kuin leudolla säällä, ja kylmästä akusta energiaa saadaan vähemmän, joten toimintamatka lyhenee." Agrees with the part's question, the three bullets above it and criterion 4 of c (energy for heating and losses is away from driving). Fixed.
- s7 b reasonableness: the new sentence says the measured 21,2 and 21,6 kWh/100 km belong to other cars and give only the order of magnitude: correct and enough. Numbers around it recomputed: 16,67 and 26,88 kWh/100 km, factor 1/0,62 = 1,61, E/s = 600 N.
- tasks.json c criteria: the thermal criterion no longer demands the combustion-car comparison (the solution still gives it as extra); the electricity criterion accepts either the heater power P = UI or the larger internal resistance (R_s I^2, lower terminal voltage): both are right physics and the solution shows both.
- d text: "toimintamatka jäi suhteellisesti eniten ilmoitetusta" matches the table (Lucid -45,8 %, Tesla -42,9 %, Inster -28,9 %) and the criteria.
- e text now asks for at least three factors, which is what criterion 1 already required: task and rubric agree.
- `practice.py check` OK (7 tasks, 105 points).
