VERDICT: PASS
CONTENT-HASH: f51c4d028372b9fc

## Blocking

## Polish
- inquiry.json:364 (tarkistus-2, Järkevyys) — "Kuvaajan säteilyn energia on siis hieman suurempi kuin cesium-137:n" päättelee fotonienergian 5 cm vs 4 cm puoliintumispaksuudesta, vaikka betonin tiheys vaihtelee — pehmennä: "voi olla hieman suurempi, tai betoni on harvempaa", tai poista lause (sama kuin suomenkielisessä lähteessä).
- lesson.md:351 — "viitearvo eli enimmäisarvo" voi antaa kuvan sitovasta raja-arvosta; viitearvo on taso, jonka ylittyessä pitoisuutta on pienennettävä — esim. "viitearvo eli taso, jonka alle pitoisuuden tulisi jäädä" ilman sanaa enimmäisarvo (C-tason yksinkertaistus, ei virhe).
- Packet: `check_lesson.py has not been run`; aja deterministiset tarkistukset ennen julkaisua.

## Checked
- One script recomputed every number: Esimerkki (1,67 mGy; 33 mSv; 4,0 mSv), siirto 12,5 µSv and mistakes 37,5/25/50/750, virhe 1,2 mSv, koe-1/koe-2 model values, 1 Gy → 2,4·10⁻⁴ K, shares 68 %/86 %/5×, vaimennus graph 5,0 cm.
- Simplified sentences keep every condition of the Finnish lesson: inverse-square law (pieni lähde, ilma vaimentaa vähän), half-value-layer model (sironneet fotonit, varmuusvara), effective dose for small doses only.
- Added glosses (alipaine eli ulkoilmaa pienempi paine, kantama, kumoavat eli osoittavat vääräksi, paljas luku) are physically correct.
- ICRP 103 w_R and w_T values and their sum 1, STUK-A263 figures, 94 Bq/m³, 300/200 Bq/m³, 20/1 mSv limits, Rn-222 3,82 d: correct.
- Cs-137 half-value thickness 5,5 mm Pb / 4 cm concrete agrees with narrow-beam μ/ρ.
- Sim shared with fi; Finnish UI in the 1280 px capture matches the howto; experiments isolate r and x.
- Exactly one correct option in every choice item; distractor feedback right.
- tarkistus-3 model answer and criteria physically right; exit ticket matches theory.
- Glossary definitions (absorboitunut/efektiivinen annos, annosnopeus, puoliintumispaksuus, taustasäteily) consistent with the text.
