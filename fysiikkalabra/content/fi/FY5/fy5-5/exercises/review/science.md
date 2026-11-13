VERDICT: PASS
CONTENT-HASH: 60cf70e0190f7730
SCOPE: delta added-exercise from 0712046380ca6300 base 81db4a6fd727

## Blocking

## Polish
- lessons/FY5/fy5-5/figures.py (planeetat) — kuvassa Maan arvo on 9,80 m/s², mutta kurssi käyttää arvoa 9,81 m/s². Kumpikaan lisätty tehtävä ei käytä Maan arvoa, joten muutos ei ole kiireellinen.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09.
- Kierroksen 1 korjaukset on tehty. L2-09 käyttää nyt päiväntasaajan sädettä 7,15·10⁷ m, joten M = 24,8·(7,15·10⁷)²/γ = 1,900·10²⁷ kg, mikä on Jupiterin massa. Ratkaisu perustelee säteen valinnan.
- L2-09:n kolme merkitsevää numeroa vastaavat lähtötietoja 24,8 ja 7,15. Vastaus 1,9 ja toleranssi 2 % hyväksyvät myös arvon 1,90.
- L1-09: F = 85·3,71 = 315,35 N, ja vastaukseksi annetaan 3,2·10² N. Massa 85 kg on rajoittava tieto, ja ratkaisu sanoo tämän. Oikein pyöristänyt opiskelija saa 320, ja myös 315 on toleranssin sisällä (1,5 %).
- Järkevyystarkistukset ovat oikein: Jupiterin ja Maan massojen suhde on 318 ja kenttien suhde 2,53. Marsissa 0,38·834 N ≈ 320 N.
- Fysiikka on luvun mukainen: F = mg, missä g = γM/R², ja kappaleen massa supistuu. Merkinnät γ, M ja R ovat luvun.
- Kuva planeetat on käytössä vain lesson.md:ssä (Kenttä eri taivaankappaleilla) ja tehtävissä, ei inquiry.json:ssa. Kumpikin tehtävä lukee eri planeetan arvon. L1-04 (Marsin mönkijä) lasketaan gravitaatiolaista, joten se ei ole sama tehtävä.
