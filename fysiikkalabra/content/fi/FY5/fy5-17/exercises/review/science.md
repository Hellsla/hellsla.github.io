VERDICT: FAIL
CONTENT-HASH: 6d2b813677c1b059

## Blocking
- exercises.json:332, solutions.md:218 (L2-09) — A, arviointi: tehtävä toistaa inquiry.json:n tehtävän samassa kuvassa. Kuvaa a-scan käytetään myös inquiry.json:ssa (kuvaluettelon `used_in`). lesson-answers.py laskee sille avaimet `ascan-BC-cm` (B:n ja C:n välisen kerroksen paksuus 3,08 cm) ja `ascan-BC-noHalf-cm` (virhe: aikaeroa ei puoliteta, jolloin tulee 6,16 cm). Luku siis kysyy jo saman suureen samasta kuvasta, ja vastaus on 3,08 cm. Kierroksella 1 kirjoitin virheellisesti, ettei kuvaa käytetä muualla. — Korjaus: kysy jotain, mitä luku ei kysy, esimerkiksi kerroksen A–B paksuus (2,31 cm) tai syvyys d_C. Toinen vaihtoehto on piirtää figures.py:hin muunnelma, jossa kaikujen ajat ovat eri.

## Polish
- solutions.md (L1-09, Vastaus) — ilmaus "Aika 20 ms on sovittu tarkaksi" ei ole kurssin käytäntö. Anna vastaus 14 m, koska ajassa 20 ms on kaksi merkitsevää numeroa. Toleranssi 4 % hyväksyy sekä 14 että 14,0.
- exercises.json (L1-09) — järven pohjan lähellä vesi on noin 4-asteista, ja pulssi kulkee myös jään läpi. Kumpikin vaikutus mahtuu 4 %:n toleranssiin, mutta lisäys "oletetaan koko vesi 0-asteiseksi" estäisi väärän mielikuvan.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09.
- Kierroksen 1 korjaus on tehty. Järkevyystarkastelussa sanotaan nyt oikein, että C on luun kaiku: luu heijastaa ja vaimentaa ultraäänen lähes kokonaan, joten luun takaa ei tule kaikuja. Syvyys 6,93 cm sopii reisiluun etäisyydeksi.
- Laskin uudelleen. L2-09: 1540·40 µs/2 = 3,08 cm. L1-09: 1402,4·0,020/2 = 14,02 m. Molemmat vastaavat answers.py:tä ja exercises.json:ia.
- L2-09:n piikit ovat 5 µs:n apuviivoilla, joten kolme merkitsevää numeroa ja toleranssi 2 % sopivat.
- Inquiry.json:ia en avannut. Toiston näyttö tulee kuvaluettelosta ja lesson-answers.py:stä.
