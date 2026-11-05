# Palautuskokeilu FY3–1: käyttöönotto-ohje

Tällä ohjeella opettaja ottaa käyttöön FY3–1-luvun palautuksen ja arvioinnin:
Google Forms → Drive-palautuskansio → Google Sheets → Sheetsiin sidottu Apps Script.
Kaikki tehdään **kaupungin hyväksymällä eduespoo-tilillä**. Älä käytä henkilökohtaista Google-tiliä opiskelijatietoihin.

Julkinen RuukkiLabra ei vastaanota palautuksia, henkilötietoja eikä pisteitä. Se vain muodostaa opiskelijan
selaimessa tiedoston `fy3-1.ratkaisut.json`, joka tallentuu opiskelijan omalle laitteelle. Opiskelija palauttaa
tiedoston itse lomakkeella.

Valikoiden ja asetusten nimet voivat poiketa hieman tästä ohjeesta. Googlen käyttöliittymä muuttuu, ja kaupunki
voi rajata asetuksia. Kirjaa poikkeamat tämän ohjeen loppuun.

---

## 0. Mitä opiskelijalle kerrotaan

RuukkiLabrassa on FY3–1:n Tehtävät-osion alussa vain painike **Lataa kaikki ratkaisut**. Sivulla ei ole pitkää
ohjetta, joten kerro opiskelijoille itse (esim. lomakkeen kuvauksessa):

- Kirjoita ratkaisut tehtävien *Kirjoita ratkaisu* -editoriin. Liitä kuvakaappaus editoriin näppäimillä Ctrl+V.
  Rajaa kuvakaappaukseen vain tehtävään kuuluva sisältö.
- Tiedostoon tulevat vain editoriin kirjoitetut ratkaisut (teksti, kaavat, kuvakaappaukset). Tarkista-kenttien
  luvut ja valintatehtävien valinnat eivät tule mukaan, joten kirjoita vastaus ja valinta myös ratkaisuun.
- Tiedostossa ei ole nimeä, sähköpostia eikä muiden lukujen ratkaisuja. Se tallentuu vain omalle laitteelle
  (yleensä Lataukset-kansioon), ja se palautetaan tällä lomakkeella. Korjatun version voi palauttaa uudelleen.

## 1. Google Forms -lomake

1. Kirjaudu eduespoo-tilille ja luo uusi lomake (Forms → Tyhjä lomake). Anna sille nimi, esim.
   *FY3–1 ratkaisujen palautus (kokeilu)*.
2. Lisää **yksi kysymys**, tyyppi **Tiedoston lähetys** (File upload):
   - otsikko täsmälleen **Palauta vastaukset** (skripti etsii saraketta tällä nimellä)
   - **Pakollinen** päälle
   - **Salli vain tietyt tiedostotyypit: pois päältä.** JSON ei kuulu Formsin tyyppivalintoihin, joten
     tyyppirajaus estäisi palautuksen. Skripti tarkistaa tiedoston sisällön itse.
   - **Tiedostojen enimmäismäärä: 1**
   - **Tiedoston enimmäiskoko: 10 Mt.** RuukkiLabra ei tee yli 9 Mt:n tiedostoa.
3. Asetukset → **Vastaukset**:
   - **Kerää sähköpostiosoitteet: Vahvistettu** (Verified). Tämä on pakollinen. Tiedostonlähetyksen oma
     kirjautumisvaatimus ei yksin riitä, koska palauttajan henkilöllisyys luetaan tästä sarakkeesta.
   - **Rajoita käyttäjiin organisaatiossa** (eduespoo) päälle.
   - **Rajoita yhteen vastaukseen: pois päältä.** Opiskelija saa palauttaa korjatun version.
   - **Salli vastausten muokkaus: pois päältä.** Korjaus tehdään uutena palautuksena.
4. Asetukset → **Esitys**: **Näytä tulokset / yhteenvetokaaviot ja tekstivastaukset: pois päältä.**
   Opiskelijat eivät saa nähdä muiden vastauksia.
5. Jos lomakkeen julkaisuasetuksissa voi valita vastaajat (Julkaise → Vastaajat), rajaa vastaajiksi
   ryhmän opiskelijat tai koulun opiskelijaryhmä, älä "Kaikki, joilla on linkki". Jos rajaus ryhmään ei
   onnistu, organisaatiorajaus on vähimmäistaso. Kirjaa, kumpi oli käytössä.
6. Vastaukset → **Linkitä Sheetsiin** → *Luo uusi laskentataulukko*. Formsin ensimmäinen vastaus luo
   Driveen palautuskansion `<lomakkeen nimi> (File responses)` ja sen alle `Palauta vastaukset (File responses)`.

Lomake vastaanottaa tiedoston ennen kuin sitä tarkistetaan. Välitöntä kaksoispalautuksen estoa ei ole, vaan
tuonti merkitsee kaksoiskappaleet.

## 2. Palautuskansion tunniste

1. Tee lomakkeeseen itse yksi testipalautus (mikä tahansa RuukkiLabrasta ladattu tiedosto), jotta palautuskansio syntyy.
2. Avaa Drivessa kansio **Palauta vastaukset (File responses)**. Sen osoite on muotoa
   `https://drive.google.com/drive/folders/<TUNNISTE>`. Kopioi `<TUNNISTE>`.
   (Myös yläkansion `<lomakkeen nimi> (File responses)` tunniste käy.)
3. Kansion tunniste ei ole salaisuus, mutta älä jaa kansiota.

## 3. Apps Script taulukkoon

1. Avaa lomakkeeseen linkitetty taulukko. Älä muokkaa lomakkeen vastausvälilehteä (*Lomakevastaukset 1*).
2. **Laajennukset → Apps Script.** Anna projektille nimi, esim. *RuukkiLabra-arviointi*.
3. Lisää tiedostot tämän kansion `apps-script/`-alikansiosta. Kopioi sisältö kokonaan:
   - `Code.gs`: korvaa editorin valmis `Code.gs`.
   - `Tehtavat.gs`: **+ → Komentosarja**, nimi `Tehtavat`. Tiedosto on generoitu: FY3–1:n tehtävänannot
     kaavoineen ja kuvineen.
   - `Review.html`: **+ → HTML**, nimi `Review`.
   - `appsscript.json`: Projektin asetukset (⚙) → *Näytä appsscript.json-manifestitiedosto editorissa* →
     korvaa tiedoston sisältö.
4. Kirjoita `Code.gs`:n alussa olevaan kohtaan `RL_CONFIG`:
   - `SUBMISSION_FOLDER_ID: '<TUNNISTE>'` (vaihe 2)
   - tarvittaessa `RESPONSES_SHEET` (vastausvälilehden nimi, tyhjä = haetaan automaattisesti)
   - `HEADERS`: sarakeotsikot. Oletuksena ovat suomenkieliset *Aikaleima* ja *Sähköpostiosoite* ja englanninkieliset
     vastineet. Jos taulukossa on muu otsikko, lisää se listaan. Skripti kertoo virheilmoituksessa löytämänsä otsikot.
   - `EMAIL_DOMAIN`: halutessa koulun sähköpostien verkkotunnus. Tyhjä = ei tarkisteta.
   - `MAX_POINTS`: pisteiden yläraja (oletus 3). **Pisteet ovat kokonaislukuja 0 … MAX_POINTS. Tyhjä = arvioimaton,
     0 = annettu nolla pistettä.**
5. Tallenna (Ctrl+S). Palaa taulukkoon ja lataa sivu uudelleen. Valikkoriville tulee **RuukkiLabra**.
6. Ensimmäisellä käytöllä Google pyytää hyväksymään oikeudet (alla). Jos kaupungin hallinta estää hyväksynnän,
   pyydä eduespoon ylläpidolta lupa tälle sisäiselle skriptille. **Älä kierrä estoa** julkaisemalla skriptiä,
   taulukkoa tai kansiota laajemmin.

### Skriptin käyttämät Google-oikeudet

| Oikeus | Mihin sitä tarvitaan |
|---|---|
| `spreadsheets.currentonly` | Lukee lomakkeen vastausvälilehteä ja kirjoittaa välilehdille *RL Palautukset* ja *RL Pisteet*, **vain tässä taulukossa**. |
| `drive.readonly` | Lukee palautustiedostoja palautuskansiosta. Vain luku: skripti ei muuta, siirrä, jaa eikä poista tiedostoja. Skripti hyväksyy vain palautuskansiossa olevat tiedostot. |
| `script.container.ui` | Näyttää RuukkiLabra-valikon, ilmoitukset ja arviointinäkymän taulukon päällä. |

Skripti ei lähetä mitään ulos, ei käytä analytiikkaa eikä tekoälypalveluja, eikä sitä julkaista verkkosovelluksena.
Virheiden lokitus on pois päältä (`exceptionLogging: NONE`), eikä skripti kirjoita vastauksia, kuvia tai
sähköposteja lokeihin. Lähdekoodissa ei ole salaisuuksia.

## 4. Käyttö

- **RuukkiLabra → Tuo palautukset** lukee uudet lomakevastaukset ja kirjaa ne välilehdelle **RL Palautukset**.
  Tuonnin voi ajaa milloin tahansa uudelleen: jo tuodut rivit ohitetaan, lukuvirheet yritetään uudelleen.
  Kaksi samanaikaista tuontia ei sotke toisiaan (lukitus).
  Tilat:
  - **Hyväksytty**: arviointijonossa.
  - **Kaksoiskappale**: sama opiskelija palautti saman version (sama tunniste tai sama sisältö) uudelleen. Ei lisätä jonoon.
  - **Tarkistettava**: sama palautustunniste kahdelta eri opiskelijalta (molemmat merkitään) tai sama tunniste
    eri sisällöllä. Ei jonossa ennen opettajan päätöstä.
  - **Virheellinen**: tiedosto ei kelpaa (syy sarakkeessa *Syy*), esimerkiksi rikkinäinen, liian suuri, väärästä
    luvusta, muutettu jälkikäteen, sallimaton kuva tai tiedosto ei ole palautuskansiossa.
  - **Lukuvirhe**: tiedostoa ei saatu luettua. Yritetään seuraavalla tuonnilla uudelleen.
- Sarakkeeseen **Opettajan päätös** voi kirjoittaa *Hyväksy* (tarkistettava jonoon) tai *Hylkää* (hyväksytty pois
  jonosta). Muita sarakkeita ei tarvitse muokata. Välilehdet on suojattu varoituksella.
- **RuukkiLabra → Avaa arviointi** avaa suuren ikkunan:
  - Aloitussivulla on tehtävälista: tehtävän numero, palautusten määrä (opiskelijat, joilla on hyväksytty palautus),
    joista tyhjiä, ja arvioitujen määrä. Luokan kokonaismäärää ei näytetä, koska sille ei ole tietolähdettä. Alla
    näkyy palautusten käsittelytila.
  - Tehtävän avaaminen näyttää yhden opiskelijan kerrallaan. Ylhäällä näkyvät *Opiskelija n/N* (N = tehtävän
    arviointijonon pituus), koulusähköposti, palautusaika ja versio, sitten tehtävänanto, opiskelijan vastaus ja
    pistekenttä. Kuvan saa isoksi napsauttamalla. Kaavat näkyvät kuvina, ja *Näytä kaavat LaTeX-muotoisina*
    näyttää niiden LaTeX-koodin.
  - Siirtyminen: **↓ / ↑** tai painikkeet *↓ Seuraava* / *↑ Edellinen*. Pisteet tallennetaan ennen siirtymistä.
    Jos tallennus epäonnistuu, siirtymistä ei tapahdu ja virhe näytetään. Kun kohdistin ei ole pistekentässä,
    numeronäppäin antaa pisteet ja ↓ tallentaa ja siirtyy. Pistekentässä nuolet toimivat normaalisti, Enter
    tallentaa ja siirtyy ja Esc poistuu kentästä.
  - Oletuksena näytetään opiskelijan uusin hyväksytty versio. Vanhemman version saa valinnasta *Palautusversio*.
    Pisteet kuuluvat aina yhdelle versiolle, eikä vanhan version pisteitä siirretä uuteen.
  - **Vain arvioimattomat** näyttää ne opiskelijat, joiden uusimmalla versiolla ei ole pisteitä tässä tehtävässä.
  - Pisteet ovat välilehdellä **RL Pisteet**, avaimena *sähköposti | palautustunniste | tehtävä*. Rivien järjestyksen
    voi muuttaa, eikä yhteys opiskelijaan, tehtävään ja versioon katoa.
- Sanallinen palaute annetaan Wilmassa. Järjestelmässä ei ole palautekenttää.

## 5. Käyttöoikeuksien tarkistus

Tee tarkistukset ennen kuin opiskelijat palauttavat mitään, ja kirjaa tulokset.

1. **Taulukko**: Jaa-painike → vain nimetyt opettajat *muokkaajina*. Ei opiskelijoita, ei ryhmiä, joissa on opiskelijoita.
   *Yleinen käyttöoikeus* = **Rajoitettu** (ei "Kaikki, joilla on linkki" eikä koko organisaatio).
2. **Palautuskansio** (molemmat *(File responses)*-kansiot): sama tarkistus kuin taulukolle. Tarkista myös, ettei
   kansio peri jaettua yläkansiota. Formsin tekemät kansiot ovat lomakkeen omistajan Drivessa.
3. **Lomake**: muokkaajina vain nimetyt opettajat. Vastaajat vain koulun tileiltä (kohta 1).
4. **Apps Script**: sidottu skripti kulkee taulukon mukana. Sen voi avata ja ajaa vain se, joka voi muokata
   taulukkoa. Älä tee skriptistä verkkosovellusta (Ota käyttöön → Verkkosovellus), äläkä jaa skriptiprojektia erikseen.
5. **Kokeile ulkopuolisena** (kohta TESTAUS.md, vaihe 6): opiskelijan testitili ei saa avata taulukkoa, kansiota
   eikä tiedostoa, eikä arviointinäkymää.
6. Älä koskaan ratkaise käyttöoikeusongelmaa avaamalla taulukkoa, kansiota tai näkymää kaikille tai linkillä.

## 6. Kaupungin asetuksista tarkistettavat asiat (eduespoo)

- Saako eduespoo-tili käyttää Apps Scriptiä ja hyväksyä edellä mainitut oikeudet sisäiselle skriptille.
- Salliiko Forms tiedostonlähetyksen, vahvistetun sähköpostin keräämisen ja organisaatiorajauksen.
- Voiko vastaajat rajata ryhmään (esim. kurssin opiskelijat).
- Onko organisaation ulkopuolinen jakaminen estetty Drivessa (pitäisi olla).
- Mikä on kaupungin linjaus opiskelijoiden palautusten **säilytysajasta** ja **poistamisesta**.
- Kuka omistaa lomakkeen, palautuskansion ja taulukon, jos opettaja vaihtaa koulua tai tili poistuu.

### Säilytysaika ja poistaminen

Kirjaa ennen käyttöä, kuinka kauan palautuksia säilytetään (esim. kurssin arvosanan vahvistamiseen ja
oikaisuvaatimusajan loppuun). Säilytysajan jälkeen poista palautuskansion tiedostot, lomakkeen vastaukset
(Forms → Vastaukset → Poista kaikki vastaukset) ja taulukon välilehdet *Lomakevastaukset*, *RL Palautukset* ja
*RL Pisteet*. Kokeilun testiaineisto poistetaan heti kokeilun jälkeen.

### Omistajuuden jatkuvuus

Lomakkeen, kansion ja taulukon omistaa yksi eduespoo-tili. Lisää vähintään toinen nimetty opettaja muokkaajaksi
kaikkiin kolmeen. Sovi ennen pidempää käyttöä, siirretäänkö aineisto koulun jaettuun Driveen (jos kaupunki
käyttää sellaista) tai kenelle omistajuus siirretään, kun omistaja lähtee.

## 7. Toisen luvun käyttöönotto myöhemmin

Kokeilu on rakennettu yhdelle luvulle. Uusi luku tarvitsee RuukkiLabraan rivin `build.py`:n
`SUBMISSION_PAGES`-listaan ja `palautus_tasks.py`:n `PAGES`-listaan, uuden `Tehtavat.gs`:n ja oman lomakkeen ja
taulukon. Tee tämä vasta, kun kokeilu on arvioitu.

## Poikkeamat ja havainnot käyttöönotossa

(Kirjaa tähän, mitä eduespoossa oli toisin kuin ohjeessa.)
