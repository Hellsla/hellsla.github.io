# Concept review: fuel (science)

Reviewed from `review-concepts/packet-fuel.md`; context opened only for fy2-1 check-1. Every number in the passages recomputed (fy2-5, fy2-2, fy2-8, fy3-10, fy3-11, fy3-15): all agree; petrol 0,750 kg/l · 43 MJ/kg = 32 MJ/l matches fy2-2, fy2-8 and fy3-11.

## Contradictions

1. `content/fi/FY2/fy2-5/lesson.md` (line 3, B) — "Polttoaine on aine, jonka kemiallista energiaa vapautetaan polttamalla." — fy2-1 check-1, fy2-6 (line 5), fy2-8 (lines 43–44: "Käytetty polttoaine on radioaktiivista jätettä") and fy3-15 call uranium polttoaine, which this definition excludes. Fix: append "Myös ydinvoimalan uraania sanotaan polttoaineeksi, vaikka se ei pala: sen energia on ydinenergiaa (luku *Energialajit ja energian säilyminen*)."
2. `content/fi/FY2/fy2-5/inquiry.json` (ennuste-1.choices[3].feedback, B) — "polttoaineiden lämpöarvot ovat kaikki samaa suuruusluokkaa, noin 10–50 MJ/kg" — fy2-8 (line 25) names hydrogen as a fuel, whose heating value is about 120 MJ/kg. Fix: "Ero on paljon pienempi: taulukon polttoaineiden lämpöarvot ovat kaikki samaa suuruusluokkaa, noin $10$–$50\,\text{MJ/kg}$."
3. `content/fi/FY3/fy3-15/exercises/solutions.md` (fy3-15-L3-03 Järkevyys, line 157, A) — "Lämpöpumppu säästää polttoainetta eniten, koska se siirtää energiaa ulkoilmasta sisälle sen sijaan, että muuttaisi sähkön lämmöksi." — contradicts fy3-11 (line 63, $Q_\text{sisälle} = Q_\text{ulko} + E_\text{s}$): the pump's electricity also ends up as heat indoors. Fix: "Lämpöpumppu säästää polttoainetta eniten, koska sisälle tulee käytetyn sähkön lisäksi ulkoilmasta siirretty lämpö, joten sähköä tarvitaan vain kolmasosa lämmöstä."
4. `content/fi/FY3/fy3-12/lesson.md` (line 31, B) — "Fossiilisten polttoaineiden käyttö on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan." — fy2-8 (hook) says the rise is "suurelta osin" due to fossil fuels; land-use change also contributes. Fix: "Ihmisen toiminta, pääosin fossiilisten polttoaineiden käyttö, on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan."

## Guardrail breaks

5. `content/fi/FY3/fy3-15/exercises/solutions.md` (fy3-15-L3-02 Järkevyys, line 145, A) — "ostettu polttoaine, joka muuttuu hukkalämmöksi ja päästöiksi" — drops the electricity and treats emissions as an energy destination (also reported in the efficiency review). Fix: "hiilivoimalassa nimittäjä on ostettu polttoaine, joka kuluu: sen energiasta noin $38\,\%$ muuttuu sähköksi ja loput hukkalämmöksi, ja palamisessa syntyy päästöjä, mutta tuulen energia ei ole varasto, jota kuluu."

Food vs fuel (fy2-5 lines 47–48, 105, ruoka, johtopaatos, exit ticket, L1-05, L2-01, L3-02) uses the guardrail words throughout. CO₂ only from carbon-containing fuels and hydrogen burning to water (fy2-5 line 98, fy2-8 lines 22–25, kertaus) agree.

## Consistent

- Energialajit (fy2-1): chemical vs nuclear energy fine; see item 1 for the term.
- Energian muuntuminen (fy2-2): chain 100 → 40 → 38 → 34 MJ consistent with fy2-4 and fy2-7.
- Hyötysuhde (fy2-4): petrol engine 25 % consistent with fy2-5 L2-04, fy3-11 (28–30 %).
- Polttoaineet ja lämpöarvo (fy2-5): values and sources match fy3-11 and fy3-15; net heating value and moisture consistent; apart from items 1–2.
- Energiantuotanto ja ilmastonmuutos (fy2-8): biomass, life-cycle factors (12 g/kWh), 420 ppm consistent with fy3-12.
- Ideaalikaasu (fy3-10): CO₂ molar mass and numbers consistent.
- Kaasun tekemä työ (fy3-11): 40 %/35 %, condenser loss, CHP 85–90 % consistent with fy3-15.
- Lämmön siirtyminen (fy3-12): apart from item 4.
- Energiantuotanto (fy3-15): "noin puolet" / "yli puolet" to the condenser agree (306/600 MW); apart from items 3 and 5.
- Energiantuotantotavat (fy2-6), Sisäenergia (fy3-5): consistent.
