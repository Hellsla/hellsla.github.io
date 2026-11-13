VERDICT: PASS
CONTENT-HASH: fdc29bc0621bfb24
SCOPE: delta added-exercise from caaeaa93666bca57 base 81db4a6fd727

## Blocking

## Polish
- solutions.md (L1-09, Vastaus) — ilmaus "Aika 20 ms on sovittu tarkaksi" ei ole kurssin käytäntö. — Perustele 14 m sillä, että ajassa 20 ms on kaksi merkitsevää numeroa. Toleranssi 4 % hyväksyy sekä 14 että 14,0.
- exercises.json (L1-09) — pohjan lähellä vesi on noin 4-asteista. Vaikutus mahtuu toleranssiin, mutta lisäys "oletetaan koko vesi 0-asteiseksi" estäisi väärän mielikuvan.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 4: arvioin tehtävät L1-09 ja L2-09.
- L2-09:n teksti on korjattu. Se kysyy nyt kaikujen A ja B hetkiä ja kerrosta A–B, mikä vastaa ratkaisua ja answers.py:tä. Δd = 1540·30 µs/2 = 2,31 cm. Inquiry-tarkistus kysyy kerrosta B–C (3,08 cm), joten toistoa ei ole.
- Piikit ovat 5 µs:n apuviivoilla (20 ja 50 µs). Kolme merkitsevää numeroa ja toleranssi 2 % sopivat.
- L1-09: 1402,4·0,020/2 = 14,02 m. Arvo 1402,4 m/s on mafy-arvot.tsv:n VERIFIED-riviltä.
- Järkevyystarkistukset ovat oikein: d_A = 1,54 cm, d_B = 3,85 cm, ja kudoksen arvolla L1-09:n tulos olisi 15,4 m.
