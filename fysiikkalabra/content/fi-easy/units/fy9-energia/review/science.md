VERDICT: PASS
CONTENT-HASH: b2479eab4e3b1226
SCOPE: full, with the three new ```pysahdy boxes in unit.md judged first against content/fi/units/fy9-energia/unit.md.

## Blocking
- (none)

## Polish
- teacher.md (same in fi): "Kaikki aineistot ovat keksittyjä esimerkkejä, eivät tilastoja" does not hold for s7. s7 uses real NAF/Motor El Prix winter 2026 data with its source line. Also "muut viisi tehtävää" is out of date now that the set has nine tasks. Fix in both languages.
- Carried from the previous report: s8 a, the reasonableness clause "Sisäenergiaa syntyy suunnilleen yhtä paljon kummallakin osamatkalla, mikä sopii kitkan tasaiseen vaikutukseen" is still unsupported, because the A–B and B–C path lengths are not given.

## Checked
- Hash b2479eab4e3b1226 at start and end. `practice.py check units/fy9-energia`: OK in fi, en and fi-easy (9 tasks, 134 points).
- Pysähdy 1 (teho / hyötysuhde): same physics as fi, correct.
- Pysähdy 2: kWh is an energy unit, $1\,\text{kWh} = 3{,}6\,\text{MJ}$, kW is a power unit. Same as fi.
- Pysähdy 3: $0{,}90 \cdot 0{,}45 \cdot 0{,}98 = 0{,}397 < 0{,}45$ because every factor is below 1. "Pienempi kuin pienin luku" means the same as fi's "pienin tekijä". It matches the johda block and the Virheet list.
- Other diff: the hero and the ketju figure are now WebP images. The ketju image follows the old to-scale geometry: 500 MW is 180 px, so 198, 50, 248 and 4 MW give 71.5, 18, 89 and 1.5 px. "Mittakaavassa" still holds, and the labels are unchanged. The 500 MW label moved 5 px, as in fi.
- I recomputed everything in one independent script:
  - Unit text: 322 MJ ≈ 90 kWh, 17 h; the chain gives 450/203/198 MW, losses 50/248/4 MW, η ≈ 0,40.
  - s1 to s9: every number matches, including the least-squares slope −4,89 and the read slope −4,9 kWh/°C, 204 W/K, 230 kWh and 16,5 °C (s3); 245,25 MWh, 36 MW, 289 MWh and 74,8 % (s6); −28,9/−42,9/−45,8 %, 16,7/26,9 kWh and 600 N (s7); 4,7 m/s, 59 N and 5,6 m/s (s8); 1,5/0,50 kW, 22/7,2 € and 74 %/132 W (s9).
  - Inquiry: η₂ = 42,86 % and its three mistake values; sauna 43,2 MJ; sahkoauto 50,76 kW (mistakes 107,1, 4,43 and 39,47); pelletti 3,737 t (2,7, 3,176 and 1,038); hissi 8,371 kW (6,278, 4,709 and 188,4); tarkistus-2 67,5 kJ (54, 43,2 and 18,75).
  - Teacher extra: about 132 kWh/d, 4,1 MWh, of which 3,7 MWh is heating.
- Bar chart in aineisto: heights are to scale (0,525 px/MW).
- The six diagnostic and four Sovella choice tasks each have exactly one correct option, and the distractor feedback is right. The heat pump is treated with the lämpökerroin, not a 350 % efficiency.
- Energy wording follows P1 ("muuttuu sisäenergiaksi, joka siirtyy lämpönä"). Scope: FY2/FY3 content plus FY4–FY6 links in s7 c and s8, which suits a FY9 review unit.
