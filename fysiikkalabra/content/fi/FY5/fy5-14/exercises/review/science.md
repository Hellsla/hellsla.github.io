VERDICT: FAIL
CONTENT-HASH: 4f2dd739c2e2da2c

## Blocking
- exercises.json:290, solutions.md:214 (L2-08) — A, arviointi: tehtävä toistaa inquiry.json:n tehtävän samassa kuvassa. Kuvaa huojunta-tehtava käytetään myös inquiry.json:ssa. Sen avaimet lesson-answers.py:ssä ovat `huojunta-fh` = 4,0 Hz ja `huojunta-m-period` (virhe: kaksi voimakasta hetkeä luetaan yhdeksi jaksoksi, jolloin tulee 2 Hz). Luku siis kysyy jo saman suureen, huojuntataajuuden, samasta kuvasta, ja ratkaisu on näytetty ennen Tehtäviä. — Korjaus: piirrä figures.py:hin muunnelma, jossa Δf on eri (esimerkiksi voimakkaat hetket 0,40 s:n välein ja vastaus 2,5 Hz). Toinen vaihtoehto on kysyä suure, jota luku ei kysy, ja tarkistaa vastaus kokonaislukuna, esimerkiksi voimakkaiden hetkien määrä 10 sekunnissa.
- exercises.json:152, solutions.md:203 (L1-10) — A, arviointi: sama ongelma kuin L2-08:ssa. Kuvaa spektri-tehtava käytetään myös inquiry.json:ssa. lesson-answers.py laskee kaikki piikit `spektri-f1…f5` ja suhteen `spektri-ratio` = voimakkain / perustaajuus = 2. Luku siis käsittelee jo saman lukemisen ja saman ansan (voimakkain piikki ei ole perustaajuus). — Korjaus: piirrä muunnelma, jossa perustaajuus on eri (esimerkiksi 150 Hz ja voimakkain piikki 450 Hz). Jos inquiry-tehtävä ei kysy perustaajuutta, kirjaa se tähän, niin tehtävä voi jäädä ennalleen.

## Polish
- lessons/FY5/fy5-14/figures.py (beats_task, docstring) — docstringissä lukee 440 Hz ja 444 Hz. Tämä vastaa nyt lesson-answers.py:tä, joten virhettä ei ole.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-10 ja L2-08.
- L2-08 on korjattu kierroksen 1 mukaisesti. Kysytty suure on nyt f_h = 1/0,25 s = 4,0 Hz, ja 2 %:n toleranssi erottaa sen virhelukemasta 2 Hz. Ratkaisu kertoo oikein, että pelkästä huojunnasta ei näe, kummalla äänellä on suurempi taajuus.
- L1-10: piikit ovat kohdissa 200·k Hz, ja perustaajuus on 200 Hz. Fysiikka ja ratkaisu ovat oikein.
- Laskin vastaukset uudelleen, ja answers.py vastaa exercises.json:ia.
- Inquiry.json:ia en avannut. Toiston näyttö tulee kuvaluettelon `used_in`-tiedoista ja lesson-answers.py:n avaimista.
