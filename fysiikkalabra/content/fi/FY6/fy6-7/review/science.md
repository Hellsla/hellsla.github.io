VERDICT: FAIL
CONTENT-HASH: a2b962dd2aa22135

## Blocking
- inquiry.json:89 (ennuste-2, standby option's feedback, changed in the round-2 fix) — A (quantitative, internal consistency): "vaikka se vaikuttaa ympäri vuoden ($8760\,\text{h}$), joten säästö on vuodessa noin $23\,\text{kWh}$" does not add up, because $3\,\text{W} \cdot 8760\,\text{h} \approx 26\,\text{kWh}$. The 23 kWh comes from the `saastot` table's $365 \cdot 21\,\text{h} = 7665\,\text{h}$, and the option itself cuts the standby only "öiksi ja päiviksi". — Fix: "…vaikka se vaikuttaa lähes ympäri vuoden ($365 \cdot 21\,\text{h} = 7665\,\text{h}$), joten säästö on vuodessa noin $23\,\text{kWh}$."

## Polish
- lessons/FY6/fy6-7/lesson-answers.py:35, 39 — still computes the removed charger saving and has no kettle saving ($2{,}0 \cdot 365 \cdot \tfrac{1}{6} = 121{,}7\,\text{kWh}$), which ennuste-2, the `saastot` solution and the johtopäätös model now quote. Replace the charger line with the kettle line.
- inquiry.json:93 (kettle feedback) — "kolminkertainen keittimen 2,0 kW:n verrattuna" mixes two constructions; this is language only.

## Checked
- Round-2 Blocking fixed: 365 · 10 min ≈ 61 h against 52 · 1,5 h = 78 h, so the difference is mainly the power (6,0 kW vs 2,0 kW). The ratio is 3,85 = 3 (power) × 1,28 (time), so "pääosin tehosta" is right.
- Round-2 Polish taken: the `saastot` intro and table have the kettle row (2,0 kW, 365 · 10 min) and no charger. The table matches the four ennuste-2 options.
- `saastot` solution order: sauna 468 > LED 191,6 > kettle 121,7 > standby 23,0 kWh, so "toiseksi … kolmanneksi" is right. The johtopäätös model agrees.
- ennuste-2 has exactly one correct option (sauna). Every distractor is really smaller.
- Recomputed in one script: 0,40/0,80 kWh; 191,6 (mistakes 38,3 and 219); 49,86 (40,86 and 36,24); 9,0 (5,4 and 9000); 150 kWh/27 €, 0,90 € a day; 60 W/885 Ω; 8,7 A; 8,76 kWh; 9,0 kWh = TV 90 h; 0,50 kWh; exit 7,2 MJ, 1,0 kWh.
- E = Pt keeps its constant-power condition. P = UI with the 230 V effective value is limited to heating devices.
- Electrical energy becomes internal energy that transfers as heat, the same in the glossary, the theory and tarkistus-3.
- The power–time figure is to scale; both areas are 0,20 kWh.
