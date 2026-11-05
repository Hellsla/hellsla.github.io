VERDICT: PASS
CONTENT-HASH: 2c058d99010374be

Science review of the Selkeä suomi translation of fy9-energia against the reviewed Finnish source
(`content/fi/units/fy9-energia/`). `check_i18n.py`: fi-easy 0 errors; `practice.py check`: fi-easy 6 tasks, 90 points.
Every number of the unit was recomputed in one Python call with my own formulas: hook (322,5 MJ ≈ 90 kWh, 17 h),
the 500 MW chain (0,397; 198 MW), the bar-chart task (η₂ = 0,4286, η₁ = 0,875, η₃ = 0,933, product 0,35), the
diagnostics, sauna 43,2 MJ, car chain 50,76 kW, pellets 3737 kg, lift 8371 W, checks 1500/900 MW and 67,5 kJ,
exit ticket 69,4 kWh, and tasks s1–s6 (1,54 / 1,84 / 1,26 kWh; 110,8 MW, 27,1 %, 90,2 %, 59,4 t; least-squares
slope −4,89 kWh/°C → 204 W/K, 230 kWh at −28 °C, 16,5 °C; 5,26 GWh, 1,7 h, 2100 t; 83,4 %, 87 %, 88 %, 79 %;
245,3 MWh, 35,97 MW, 288,5 MWh, 0,748, 73 MWh). All agree with the translation, which keeps every value, unit,
tolerance, correct option, formula and rounding justification of the source. No step is dropped in any solution.

## Blocking
None.

## Polish
1. **Added explanations are correct** (lauhdevoimala "tuottaa vain sähköä", lauhdutin, kaukolämpö, säätövoima,
   päästökerroin "hiilidioksidia yhtä kilowattituntia kohti", pumppuvoimala energiavarastona, nimellisteho = suurin
   teho). One is narrower than the term: `sovella/tasks.json` fy9-energia-s3 text, "suora sähkölämmitys, eli talo
   lämmitetään sähköpattereilla" — direct electric heating also covers floor heating and radiant panels. Fix:
   "eli talo lämmitetään suoraan sähköllä, esimerkiksi sähköpattereilla".
2. `unit.md` "Hyötysuhde ja energiaketju", "Siinä $E_\text{h}$ on häviöt eli energia, joka ei tule hyödyksi" and
   "Häviöt … Yleensä häviöt muuttuvat lämmöksi" are faithful and correct; no change needed. The fixed source
   grammar "kokonaishyötysuhdetta verrataan" in "Yleisiä virheitä" is a welcome correction, not a physics change.
3. `inquiry.json` aineisto solution: "Lauhdutin on laite, jossa höyry jäähtyy takaisin vedeksi" — physically the
   steam condenses (tiivistyy) at constant temperature; suggest "jossa höyry tiivistyy eli muuttuu takaisin vedeksi",
   which also matches the wording "lauhdutetaan eli muutetaan vedeksi" used in task s2 and tarkistus-3.

## Shared issues
None.
