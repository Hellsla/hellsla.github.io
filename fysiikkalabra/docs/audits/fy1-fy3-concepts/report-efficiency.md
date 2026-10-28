# Concept review: efficiency (science)

Reviewed from `review-concepts/packet-efficiency.md`; context opened only for the fy2-2 L3 solution, fy2-4 lesson lines 33–44 and the fy3-15 L3-02 solution. All numbers in the passages recomputed (fy2-4 lamps, fy2-7 grids, fy3-11 example/L1–L3/siirto, fy3-15 example/ketju/kaukolämpö/virhe/check-2/exit ticket/L1–L3, Sovella c): all agree.

## Contradictions

1. `content/fi/FY2/fy2-4/lesson.md` (line 33, B) — "Kun laitteen hyöty on muuta kuin lämpöä, hyötysuhde jää yleensä selvästi alle 100 %." — contradicts the same lesson's table (sähkömoottori 90 %), fy3-15 (generaattori ja muuntaja 0,95–0,98, "yksi tehokkaimmista koneista", vesivoimala noin 90 %) and fy3-11 L3-03 (sähkömoottori 90 %). Fix: "Kun laitteen hyöty on muuta kuin lämpöä, hyötysuhde vaihtelee paljon: sähkömoottori pääsee noin $90\,\%$:iin, mutta lamppu ja polttomoottori jäävät selvästi alle $100\,\%$:n."
2. `content/fi/FY3/fy3-15/inquiry.json` (tyypit.text, table, B) — "Yhteistuotanto, sähkö | 0,25–0,35" — fy3-11 suunnittele uses a CHP plant with 45 % electricity and states its condition (maakaasu); fy3-15 gives the range without one. Fix: "| Yhteistuotanto (kiinteä polttoaine), sähkö | 0,25–0,35 |".
3. `content/fi/FY2/fy2-2/exercises/solutions.md` (L3 Järkevyys, line 109, B) — "Yhden vuorokauden hukkalämpö riittäisi siis kokonaisen pikkukaupungin vuoden lämmitykseen." — implies the condenser heat sent to the sea is directly usable; fy3-11 (line 125) and fy3-15 say it is usable only when the steam is condensed hotter, at the cost of electricity. Fix: "Energiamäärä vastaa siis pikkukaupungin vuoden lämmitystä, mutta mereen menevä lämpö on liian viileää kaukolämmöksi; yhteistuotannossa höyry lauhdutetaan kuumempana, jolloin lämpö saadaan talteen ja sähköä syntyy hieman vähemmän."

## Guardrail breaks

4. `content/fi/FY3/fy3-15/exercises/solutions.md` (fy3-15-L3-02 Järkevyys, line 109, A) — "ostettu polttoaine, joka muuttuu hukkalämmöksi ja päästöiksi" — leaves out the electricity and counts emissions as an energy destination. Fix: "hiilivoimalassa nimittäjä on ostettu polttoaine, joka kuluu: sen energiasta noin $38\,\%$ muuttuu sähköksi ja loput hukkalämmöksi, ja palamisessa syntyy päästöjä, mutta tuulen energia ei ole varasto, jota kuluu."

No other break: the efficiency limit (fy2-4 line 33) uses the guardrail words, the resistance heater is "lähes 100 %", the heat pump has a lämpökerroin "ei hyötysuhde" everywhere (fy3-11, fy3-12, fy3-15), the heat-engine loss is "ei voi kokonaan välttää" / "osa", and electrical and total CHP efficiency are kept apart (fy3-11, fy3-15 check-3, johtopaatos).

## Consistent

- Energian muuntuminen ja yksikkö joule (fy2-2): apart from item 3.
- Hyötysuhde (fy2-4): definition, purpose and boundary dependence, table, solutions; apart from item 1.
- Polttoaineet ja lämpöarvo (fy2-5): released vs useful energy consistent with fy2-4.
- Energian siirtäminen (fy2-7): grid efficiencies used correctly (divide vs multiply), realistic 4 % electric and 9–20 % district-heat losses.
- Energiantuotanto, ympäristö ja ilmastonmuutos (fy2-8): waste heat and CO₂ kept apart.
- Kaasun tekemä työ ja lämpövoimakone (fy3-11): W = Q₁ − Q₂, η < 100 %, CHP 85–90 %, COP > 1 and its reason; consistent.
- Lämmön siirtyminen ja ilmastonmuutos (fy3-12): COP use correct.
- Energiantuotanto ja voimalaitosten hyötysuhde (fy3-15): chain product, denominators, CHP; apart from items 2 and 4.
- FY3 Sovella itsenäisesti: collector efficiency as useful/incoming power; consistent.
