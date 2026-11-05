# Palautuskokeilu FY3–1: testaus koulutileillä

Ensimmäinen koe tehdään **keksityillä vastauksilla**. Älä käytä oikeita opiskelijatietoja. Tarvitset:

- opettajatilin (eduespoo), jolla lomake, kansio, taulukko ja skripti on tehty (KAYTTOONOTTO.md)
- toisen opettajan tilin, jos mahdollista (jaettu arviointi)
- kaksi opiskelijan testitiliä (A ja B), eduespoo-tunnukset
- RuukkiLabran FY3–1-sivun, jossa on Lataa kaikki ratkaisut -painike (julkaistaan vasta, kun opettaja on yhdistänyt PR:n)

Merkitse jokaiseen kohtaan ✓, ✗ tai havainto.

## 1. Opiskelija A lataa ratkaisut
1. Avaa FY3–1 → Tehtävät. Painike **Lataa kaikki ratkaisut** näkyy tehtävien alussa.
2. Kirjoita tehtävään 1-1 tekstiä, kaava (Ctrl+E) ja liitä kuvakaappaus (Ctrl+V). Liitä tehtävään 1-4 toinen
   kuvakaappaus.
3. Kirjoita vielä muutama sana ja paina heti **Lataa kaikki ratkaisut**. Tiedosto `fy3-1.ratkaisut.json` latautuu, ja
   sivu sanoo: *Palauta ladattu tiedosto opettajan Google Forms -lomakkeella.* Viimeisetkin sanat ovat mukana (kohta 4).
4. Lataa uudelleen muuttamatta mitään ja palauta molemmat tiedostot (kohta 2): tuonti tunnistaa saman version.

## 2. Palautus lomakkeella
1. A avaa lomakkeen, kirjautuu eduespoo-tilillä ja palauttaa tiedoston. Lomake hyväksyy JSON-tiedoston.
2. A palauttaa **saman tiedoston** toisen kerran (kaksoispalautus).
3. A muuttaa ratkaisua tehtävässä 1-1, lataa uudelleen (uusi tunniste) ja palauttaa (korjattu versio).
4. B palauttaa oman ratkaisunsa. Lisäksi B palauttaa **A:n ensimmäisen tiedoston** (sama tunniste eri opiskelijalta).
5. B palauttaa jonkin muun tiedoston (esim. kuvan tai tekstitiedoston, nimetty `.json`-päätteiseksi).

## 3. Tuonti
1. Opettaja: **RuukkiLabra → Tuo palautukset**. Ilmoitus kertoo määrät.
2. Välilehdellä *RL Palautukset*: A:n ensimmäinen *Hyväksytty* → muuttuu *Tarkistettavaksi* B:n samalla
   tunnisteella; A:n toinen kerta *Kaksoiskappale*; A:n korjattu *Hyväksytty*; B:n oma *Hyväksytty*; B:n
   kopio *Tarkistettava*; muu tiedosto *Virheellinen* syineen.
3. Aja tuonti uudelleen: uusia rivejä 0, mikään ei muutu.
4. *Lomakevastaukset 1* -välilehti on ennallaan.

## 4. Arviointi
1. **RuukkiLabra → Avaa arviointi.** Tehtävälistassa näkyvät palautusten ja arvioitujen määrät.
2. Avaa tehtävä 1-1: A:n uusin versio, sähköposti, palautusaika, tehtävänanto, teksti, kaava ja kuvakaappaus
   oikeassa järjestyksessä. Kuva suurenee napsauttamalla.
3. Anna 2 pistettä ja paina ↓. Taulukon *RL Pisteet* -välilehdelle tulee rivi A | tunniste | tehtävä | 2.
4. Palaa ↑: pisteet 2 ja *Tallennettu ✓*. Anna 0: rivillä on 0. Tyhjennä kenttä: rivillä on tyhjä (arvioimaton).
5. Paina ↓ monta kertaa nopeasti: siirtyminen tapahtuu kerran, ja pisteet menevät oikealle opiskelijalle.
6. Pistekentässä ↓ ei vaihda opiskelijaa. Esc ja ↓ vaihtaa.
7. Valitse A:n vanhempi versio: siinä ei ole uuden version pisteitä. Uusimman version pisteet säilyvät.
8. Lajittele *RL Pisteet* esim. sähköpostin mukaan ja avaa arviointi uudelleen: pisteet ovat oikeilla opiskelijoilla.
9. Kirjoita *RL Palautukset* -välilehdellä B:n tarkistettavalle riville *Hyväksy* → Päivitä: rivi tulee jonoon.
10. *Vain arvioimattomat* näyttää vain ne, joilla ei ole pisteitä.
11. Toinen opettaja avaa saman taulukon ja arvioi toisen tehtävän samaan aikaan: molempien pisteet tallentuvat.

## 5. Opiskelija ei pääse aineistoon (tärkein)
Opiskelijan testitilillä, myös suoralla linkillä, jonka opettaja kopioi:
1. arviointitaulukko → *Pääsy evätty* tai käyttöoikeuspyyntö (älä hyväksy)
2. palautuskansio ja yksittäinen palautustiedosto → ei pääsyä
3. lomakkeen vastaukset tai yhteenveto → ei näy palautuksen jälkeen
4. Apps Script -projekti → ei pääsyä

## 6. Ulkopuolinen ei pääse
Organisaation ulkopuolisella tilillä tai kirjautumatta: lomake ei hyväksy palautusta, eikä taulukko, kansio tai
tiedosto aukea.

## 7. Siivous
Poista testivastaukset lomakkeesta, palautuskansion testitiedostot ja taulukon testirivit (KAYTTOONOTTO.md, kohta 6).

## Mitä on testattu jo automaattisesti (ilman Google-palveluja)
`python scripts/test_palautus.py` ajaa kaiken edellä olevan, paitsi kohdat 2, 5, 6 ja 4.11, Chromium-selaimessa:
RuukkiLabran oikean FY3–1-sivun vientiä sekä Apps Scriptin koodia jäljiteltyjä Sheets-, Drive- ja
google.script.run-palveluja vasten. **Oikeaa Formsia, Drivea, Sheetsiä ja eduespoon käyttöoikeuksia ei ole
testattu.** Ne varmistetaan tällä ohjeella.
