VERDICT: PASS
CONTENT-HASH: a82e14d314957d41

## Blocking

## Polish
- solutions.md:94 (L2-04, Vastaus) — names 21,9 K but not the two-figure 8,1 °C in the term m_j T; and the reading's ±0,05 K moves s by about ±1 kJ/kg, so the third figure is only just held. Add: "0,405 on pieni verrattuna lukuun 4,38, joten lukema 8,1 °C ei rajoita kolmea numeroa."
- inquiry.json:322 (siirto, Vastaus) — "vaikuttaa vain kolmannen numeron tuhansien paikkaan" is still muddled. Say that 8,0 K (±0,05 K) moves the 33 520 J/kg term by only about ±200 J/kg, below the thousands digit of 367 520, so it does not limit the three figures.
- sim-spec.md:1 — still promises "yhden rivin selitys, mikä neljästä tilanteesta toteutuu"; the sim.js readout has no such line, and the howto in inquiry.json:112 ("Lopputila kertoo neljästä tapauksesta yhden") reads as the same promise. Drop it or add the line.
- solutions.md:82 (L2-03, Järkevyys) — the estimate 134 kJ / 0,8 kJ/s ≈ 170 s leaves out the 8,4 kJ of heating that the line before it just named. Say it is the melting alone, so 170 s is a lower bound that the 177,5 s rightly exceeds.

## Checked
- One script (scratchpad/fy314_r3.py): all 12 answers recomputed with my own four-case equilibrium solver match answers.py and exercises.json. L3-03 is case 4, L3-02 is case 2.
- L3-03 split values: 4190 + 33 400 − 42 000 = −4410 J, denominator 2100 · 0,600 = 1260 J/K, T = −3,50 °C. The corrected Järkevyys is right (33,4 kJ of the needed 42 kJ, 4,4 kJ short), and the balance is 38 325 = 38 325 J with ΔT = 36,5 K.
- L2-03 split values: 8400 J + 133 600 J = 142 000 J, which gives 177,5 s. Heating is 5,9 % of the total.
- L2-04 split values: 4,380 − 0,405 = 3,975 kg·K, × 4190 / 0,0500 = 333 105 J/kg. With 8,0 °C the result would be 335,2 kJ/kg, as stated.
- Worked example: 25 140 / 17 540 / 7600 J, T = 6,046 °C. Without melting it would be 19,3 °C, melting takes 0,664 of the heat, and the balance is 18,8 kJ on both sides. The two figures are traced to m_j.
- Rounding lines name the limiting datum: L3-01 sum to thousands, L3-02 difference to the gram, L3-03 −4410 J to hundreds.
- inquiry.json: koe-1 (62,4 / 24,7 g, 26,57 °C, 10,07 °C), koe-2 / ennuste-2 (5,9 / 18,5 / 12,6 g, 31,4 kJ), virhe (−25,6 °C, 0,075 / 0,225 kg), siirto (39,9; mistakes 43,9 and 437,5 → 438), tarkistus-2 (40,06; 56; balance 25,1 / 25,1 kJ). Every correct option is right.
- Exit ticket (66,8 kJ, 4,19 kJ, 12,5 g), figures (0,375 / 0,025 kg, 25,1 / 2,1 + 33,4 kJ, kink at 26,6 °C, 40,07 °C at 80 °C).
- sim.js: four-case solve, Qend and the in-sequence stateAt are consistent. The largest bar is 209 kJ, under 250. The pace is labelled illustrative.
- Scope: inside FY3. Hash unchanged from start to end.
