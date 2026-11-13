VERDICT: FAIL
CONTENT-HASH: 2fc1b9c79f47d46c

## Blocking
- exercises.json:136 (L1-11) — A: `"unit": "min"` on jäänne tehtävän vanhasta versiosta (kiertoaika). Tehtävä kysyy nyt putoamiskiihtyvyyttä ja vastaus on 1,45 m/s², joten sivu näyttäisi vastauksen "1,45 min". — Korjaa `"unit": "m/s²"`.

## Polish
- exercises.json (L1-11, hint) — "Arvot löytyvät" on monikossa, vaikka taulukosta haetaan nyt vain Kuun massa. — Kirjoita "Kuun massa löytyy MAFY-taulukon kohdasta *Aurinkokunta*."
- solutions.md (L1-10, Järkevyys) — "noin tuhannesosa" on karkea arvio: 5,93·10⁻³/9,81 ≈ 6·10⁻⁴. — Kirjoita "alle tuhannesosa".
- exercises.json (L1-11 ja L1-05) — molemmissa luotain kiertää Kuuta lähes samalla säteellä (1840 km ja 1847 km). Toistoa ei ole, koska L1-05 kysyy ratanopeutta ja L1-11 kentän voimakkuutta taulukkoarvolla. Säteen voisi silti vaihtaa, esimerkiksi 1900 km.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 5: arvioin muutetun tehtävän L1-11.
- L1-11: Kuun massa 7,346·10²² kg on docs/mafy-arvot.tsv:n VERIFIED-riviltä. g = γM/r² = 6,674·10⁻¹¹·7,346·10²²/(1,840·10⁶)² = 1,448 m/s² → 1,45. answers.py antaa saman.
- Arvolla 7,35·10²² kg tulee 1,449 m/s², joten toleranssi 4 % on väljä mutta riittävä. Pyöristysperusteena käytetään sädettä 1840 km, jossa on kolme merkitsevää numeroa.
- Massa supistuu oikein (g = F/m). Järkevyystarkistus 1,62·(1737/1840)² = 1,44 m/s² on aito tarkistus.
- Lainalaisuus kuuluu luvun aiheeseen gravitaatiolaki ja planetaarinen liike.
- L1-10 (5,934 mm/s²) ja L2-08 (√(5250/88) = 7,724 → 7,7) ovat ennallaan.
- Kaikkien kolmen kieliversion answer, unit ja tolerance ovat samat, ja käännösten ratkaisujen luvut vastaavat suomenkielistä.
