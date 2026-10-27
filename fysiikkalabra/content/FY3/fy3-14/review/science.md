VERDICT: FAIL
CONTENT-HASH: 833cfd37a6beef62

## Blocking
- solutions.md:119 (L3-03, Järkevyys) — "lämpötila pysyy lähellä jään alkulämpötilaa mutta nousee hieman" is false: the ice warms from −40 °C to −3,5 °C, 36,5 K of 40 K, so the end state lies close to 0 °C, not to −40 °C. The lesson's key physics (freezing 0,100 kg of water releases 33,4 kJ, most of the 42 kJ the ice needs) gets the wrong check. I missed this in round 1. Fix: "Vaikka jäätä on viisinkertainen massa, lämpötila nousee lähelle 0 °C:ta, koska jäätyvä vesi luovuttaa 33,4 kJ eli suurimman osan jään lämmittämiseen tarvittavasta 42 kJ:sta; vain 4,4 kJ jää puuttumaan."

## Polish
- sim-spec.md:1 — still promises "yhden rivin selitys, mikä neljästä tilanteesta toteutuu"; the sim.js readout has no such line (only T, ice left, Q_v, Q_lämm, Q_sul). Drop the promise or add the line.
- inquiry.json:322 (siirto, Vastaus) — "vaikuttaa vain kolmannen numeron tuhansien paikkaan" is muddled. The point is that 8,0 K (±0,05) shifts the 33 520 J/kg term by about ±200 J/kg, below the thousands digit of 367 520, so it does not limit the three figures. Say that.
- solutions.md L2-04 Vastaus — names 21,9 K but not the two-figure T = 8,1 °C in the term m_j T. Add a sentence that 0,405 is small beside 4,38, so 8,1 does not limit the figures.

## Checked
- One script: all 12 answers recomputed with my own four-case equilibrium solver match answers.py and exercises.json within tolerance. L3-03 is case 4 (all water freezes), L3-02 is case 2.
- Round-1 fixes are in place: tarkistus-2 "neljäsosa" (0,050/0,20), siirto 22,0 − 8,0 = 14,0 K, L2-01 balance 23,55 = 23,55 kJ, L1-03 wording, L3-03 Kaava algebra and units.
- Worked example: 25 140 / 17 540 / 7600 J, T = 6,046 → 6,0 °C. The two figures are rightly traced to m_j = 0,050 kg (Q_j to hundreds of J). The checks (19,3 °C without melting, 2/3, 18,8 kJ balance) are correct.
- Rounding lines name the limiting datum: L3-01 sum to thousands of J/kg, L3-02 difference to the gram, L3-03 −4410 J to hundreds.
- inquiry.json: koe-1 (62,4 / 24,7 g, 26,57 °C, 10,07 °C at 40 °C), koe-2 / ennuste-2 (5,9 / 18,5 / 12,6 g, 31,4 kJ), virhe (−25,6 °C, 0,075 / 0,225 kg), siirto (39,9; mistakes 43,9 and 438), tarkistus-2 (40,06; 56; 35; balance 25,1 kJ): all correct. Each correct option is right.
- Exit ticket: 66,8 kJ, 4,19 kJ, 12,5 g.
- Figures: 0,375 / 0,025 kg, bars 25,1 / 2,1 + 33,4 = 35,5 kJ, kink at 26,6 °C, 40,07 °C at 80 °C.
- sim.js: four-case solve and Qend are consistent; the stateAt sequence ends at Tf on both sides (case 4 checked algebraically); the pace is labelled illustrative (τ 1,8 s, 8 s run).
- Experiments isolate TW0 and TI0, and simState carries Tf and iceLeftG. Tolerances accept the two-figure Vastaus (27 °C, 13 g).
- Scope: inside FY3.
