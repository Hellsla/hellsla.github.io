VERDICT: PASS
CONTENT-HASH: 5ee0755d24f7360c

## Blocking

## Polish
- lesson.md:248 — "häviö vähennetään yksikkönä prosentista" is hard to parse; e.g. "Kolmas virhe on vähentää prosenttiluku suoraan energiasta: häviö 4 % ei tarkoita 4 MWh …".
- inquiry.json:348 — tarkistus-2 mistake 469 says "Häviöprosentti lasketaan lähtevästä energiasta", but the task gives a hyötysuhde 75 %, not a häviöprosentti; "Hyötysuhde ja häviön osuus lasketaan lähtevästä energiasta" fits the task.
- lesson.md:115 — 4 % of 83 TWh is 3,3 TWh while the inquiry table rounds the loss to 3 TWh (3 : 83 = 3,6 %); harmless, but giving 3,3 TWh in the table would keep the two numbers consistent.

## Checked
- Worked example recomputed: 0,910 · 245 MWh = 222,95 → 223 MWh, loss 22,05 → 22 MWh; staged, symbolic first, figures justified (η 0,910 from 9,0 %, loss two figures), energy balance check real.
- District heat 36,0 − 32,7 = 3,3 TWh, 9,17 → 9,2 % (mistakes 10,1 and 3,3 correct); "erotus pääosin häviötä, arvio" states the condition.
- Voltage table consistent with P_häviö = (P/U)²R for one fixed R ≈ 3,2 Ω: 0,80 / 0,026 / 0,0020 MW; 20× voltage → 400× smaller loss; 8,0 % and 0,020 % correct; no FY-sähköoppi formula shown (qualitative, stated as later course).
- Battery transfer 1,8 : 12,0 = 15 % (mistakes 85 and 17,6 correct); check-2 375 : 0,75 = 500 MWh (mistakes 281, 469 correct); exit ticket 768 MWh, 48 kWh; virhe item 20 MWh / 480 MWh.
- Sankey figure to scale: 96/4 and 91/9 strip heights within 0,2 px.
- Grid voltages 110–400 kV, 20 kV, 0,4 kV, 230 V correct; losses explained by current heating the conductor; district-heat loss by temperature difference through the insulation.
- Every choice item has exactly one correct option; distractor feedback (incl. "korkea jännite voimakkaampaa", "johtaa paremmin", "turvallisempaa") says why it is wrong.
- Energy conservation wording (häviö muuttuu lämmöksi ympäristöön, ei katoa) the same in theory, misconception, summary, model answers and exit ticket; storage converts forms with heat loss.
- Statistics carry source and year (Energiateollisuus 2024); invented situations marked esimerkki / malli.
- FY2 scope kept (no chain product, no conduction formula); hash identical at start and end.
