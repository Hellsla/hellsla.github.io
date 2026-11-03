VERDICT: FAIL
CONTENT-HASH: f0b8a4565206a2d8

## Blocking
- inquiry.json:93 (ennuste-2, new kettle option's feedback) — A (causality/assessment): "Keittimen teho on suuri, mutta ajan lyhennys on pieni … koska sauna kestää tunteja eikä minuutteja" gives the wrong reason. Over a year the time cut is 365 · 10 min ≈ 61 h, almost as much as the sauna's 52 · 1,5 h = 78 h; the factor ≈ 3,8 (122 vs 468 kWh) comes mainly from the power, 6,0 kW against 2,0 kW. Comparing one sauna session with one day's minutes is the per-occasion trap this lesson is meant to repair. — Fix: "Vuodessa käyttöaika lyhenee $365 \cdot \tfrac{1}{6}\,\text{h} \approx 61\,\text{h}$, ja säästö on $2{,}0\,\text{kW} \cdot 61\,\text{h} \approx 120\,\text{kWh}$. Saunassa aikaa säästyy lähes saman verran, $78\,\text{h}$, mutta kiukaan teho on kolminkertainen, joten säästö on $468\,\text{kWh}$."

## Polish
- inquiry.json:83 (ennuste-2 `pending`) and `saastot` table — the prediction now offers the kettle option, which the table does not contain, while the table still lists "laturi irti", which the prediction no longer offers. Add a kettle row (2,0 kW, 365 · 1/6 h) to the table, or accept that the feedback alone carries that number.
- inquiry.json:89 (ennuste-2, standby feedback) — "koska kiukaan teho on kaksituhatkertainen" names only the power; the standby time is about 100 times longer. "Teho on kaksituhatkertainen, mutta aika vain noin sadasosa" would show both factors (C as written).

## Checked
- Round-1 Blocking 1 fixed: glossary "sähköenergia" now reads "…laitteen sisäenergiaksi, joka siirtyy lämpönä ympäristöön". No "lämmöksi" anywhere in lesson, inquiry, exit ticket.
- Round-1 Blocking 2 fixed: tarkistus-3 prompt now asks where the energy ends up; criterion 3 matches it and the model answer.
- Round-1 Polish taken: summary "lämmittävän laitteen virta", "pääosin energiasta", "yleensä", 49,86 € ≈ 50 € with the reason, answers.py comment `fy6-7/washer`.
- ennuste-2: exactly one correct option (sauna 468 kWh > LED 191,6 > kettle 121,7 > standby 23,0 kWh); numbers in every feedback recomputed and right.
- All lesson and inquiry numbers recomputed in one script: 0,40; 191,6; 49,86; 9,0 (mistake 5,4); 468; 23; 150 kWh/27 €; exit 7,2 MJ and 1,0 kWh.
- Exercise answers (incl. the iron 1200 W : 230 V = 5,2 A) agree with my own formulas.
- E = Pt with its constant-power condition; P = UI with the 230 V effective value limited to heating devices in theory and summary.
- Power–time figure to scale, both areas 0,20 kWh.
