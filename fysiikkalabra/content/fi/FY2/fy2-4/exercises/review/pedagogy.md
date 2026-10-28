VERDICT: PASS
CONTENT-HASH: 35c3015164c2b5ea

## Blocking

## Polish
1. exercises.json L1-02, L1-03, L2-04 — numbers the lesson has already answered: L1-02 is the Etsi virhe case (8,0 W, 2,4 W, 30 %), L1-03 the lesson's 60 W, 5 %, 3 W, L2-04 the 60 / 15 / 45 kW of ennuste 1's feedback. Change the data (e.g. L1-02 ledilamppu 5,0 W ja 1,5 W; L2-04 hyötyteho 12 kW).
2. solutions.md L3-02 and L2-03 — "kaksi merkitsevää numeroa" next to the answer 2083 s (four figures) and 0,228 kWh in the Sijoitus line while Vastaus says 0,23 kWh; exercises.json stores 2083.33 and 0.228. Give 2,1 · 10³ s and 0,23 kWh in the Sijoitus line too, and store 2100 and 0.23 (tolerance 0,02 still holds).
3. Level 3 (L3-01, -02, -03) — all three are multi-step calculations; none asks for reasoning or a new context, which is the level's point. Replace L3-01 with an argued item, e.g. "Laite A ottaa 100 W ja laite B 500 W. Kumman hyötysuhde on parempi?" (cannot be answered, student explains what is missing), or a daily context (ledilamppu vs hehkulamppu cost of an hour) with a justification.
4. solutions.md, every "Muunnokset" line — "sijoittamalla 1 = 100 %" and "1 % = 0,01" read as false equations; write "kerrotaan luvulla 100 %" / "jaetaan sadalla".
5. L2-03 — kilowattitunti is not met in this lesson; add "(luku *Energian muuntuminen ja yksikkö joule*)" to the Muunnokset line where it says kW and h give kWh directly.

## Checked
- Levels 5 / 4 / 3 per rubric; no exercise repeats the kettle example (L2-01 is the same chain but asks Ea, not Eh).
- Every solution has the seven parts: given, principle with a reason, symbols first, conversions or why none, substitution with units, answer with figures, reasonableness.
- L1-04, L2-02, L2-04 and L3-02 solve backwards (Eo = Ea : η, t = Ea : (η · Po)) and explain why; a student who could not start can follow.
- Variety: energy, power, loss, reverse, comparison, time, Sankey scale (L3-03 is the only figure task and is fresh).
- Finnish checked: case after number+unit, terms hyötyteho, häviöteho, ottaa; no FY3 content.
- Hash unchanged at end: 35c3015164c2b5ea.
