# Dronelabra: suunnitelma

**Dronelabra – Lennä, ohjelmoi ja tutki** on Kiviruukin lukion koulukohtainen opintojakso (alustavasti 2 op), joka
pidetään Ahjo Makerspacessa (opettajan toimeksianto 12.11.2026; korvasi suunnitelmissa nimen Droonilab). Se ei
edellytä Ahjo 1:tä tai Ahjo 2:ta.

Tämä tiedosto on opettajan työmuistio. Sitä ei julkaista.

## Toteutus sivustolla

Dronelabra on Ahjon kolmas opintojakso samassa tiedostossa `jaksot/ahjo/jakso.json` (koodi `DRONELABRA`), ei oma
järjestelmänsä. Se käyttää Ahjon oppituntirakennetta (A–E, Kokeile / Muokkaa / Haasta itsesi, tuotos, tarvikkeet,
turvallisuus, vertaistehtävä, projektipäiväkirja), ohjepohjaa, projektipankkia ja turvallisuussivua.

| Sivu | Sisältö |
|---|---|
| `dronelabra.html` | opintojakson etusivu: 16 oppituntia viidessä kokonaisuudessa, tavoitteet, arviointi, Drone Challenge |
| `dronelabra-tunti-1.html` … `-16.html` | oppitunnit |
| `ahjo-drone-perehdytys.html` | turvallisuusperehdytys |
| `ahjo-airbit-kokoaminen.html`, `ahjo-airbit-ohjaus.html` | Air:bit 2:n kokoaminen, ohjain ja ohjausohjelma |
| `ahjo-drone-lentokokeet.html`, `ahjo-fpv-lento.html`, `ahjo-drone-data.html` | lentokokeet, FPV-lento, data-analyysi |
| `ahjo-projektit.html` | kahdeksan droneprojektia Ahjon projektipankissa |
| `ahjo-turvallisuus.html` | kahdeksan drone-aihetta, tila "valmisteilla" |
| `ahjo-aloitus/` | ohjaimen aloitusohjelma, lentopöytäkirja, esimerkkiaineisto, analyysiohjelma |

Oppitunnilla on kolme uutta kenttää: `status` (toteutettavuus), `diary` (projektipäiväkirjan kirjaukset) ja `teacher`
(ajankäyttö ja valmistelut, taitettuna). Projektikortilla `steps`, `safety` ja `need`.

Englanti ja selkosuomi: kurssin data on käännetty (`jaksot/ahjo/en|fi-easy/jakso.json`). Kuuden ohjeen tekstit ovat
toistaiseksi vain suomeksi, ja muut kielet näyttävät suomenkielisen ohjeen.

## Kalusto ja oletukset

- **Air:bit 2** (MakeKit): 10 sarjaa ja 20 micro:bitiä eli kaksi sarjaa kohti; sarjoissa on potkurisuojat (opettaja
  12.11.2026). Ryhmät ovat 2–3 opiskelijaa sarjaa kohti. Micro:bitit ovat versiota V2.
- **Kameradronet:** 2 × DJI Neo 2 Motion Fly More Combo (lasit Goggles N3, liikeohjain RC Motion 3). Toimeksiannossa
  luki "DJI Neo FPV": mallin on oletettu olevan sama kuin aiemmin ilmoitettu Neo 2. Sivuston teksteissä mallinimeä ei
  mainita, kuten ei Ahjon muussakaan laitteistossa.
- **Raspberry Pi 5 (8 Gt):** 10 kpl (opettaja 12.11.2026). Ei lento-ohjaimeksi. Data-analyysi tehdään opiskelijoiden omilla tietokoneilla (opettaja 12.11.2026); Raspberry Pit ovat vain konenäköprojektin käytössä, eivät varakoneina.
- **Oppitunnin pituus:** 75 min, kuten Ahjo 1:ssä.

Kaikilla ei ole omaa dronea. Lentotunnit on suunniteltu kiertopisteiksi: lento, mittaaminen ja kirjaus, datan
käsittely, suunnittelu. Jokaisella lentotunnilla on kenttä "Jos joudut odottamaan".

## Toteutettavuus oppitunneittain

a = onnistuu nykyisellä kalustolla, b = vaatii tietyn ohjaimen tai lisälaitteen, c = vaatii lisähankinnan,
d = vaatii opettajan turvallisuushyväksynnän (lentäminen).

| Tunti | Aihe | Merkintä |
|---|---|---|
| 1 | Droneihin tutustuminen ja lentoturvallisuus | d (opettajan esittelylento) |
| 2 | Miksi drone lentää? Voimat ja momentit | a |
| 3 | Air:bit 2:n rakenne ja komponentit | a |
| 4 | Dronen kokoaminen ja toimintakokeet | a (ilman potkureita) |
| 5 | micro:bit, MakeCode ja radio-ohjaus | a |
| 6 | Ohjausohjelman tutkiminen ja muokkaaminen | a (ilman potkureita) |
| 7 | Air:bit 2:n ensimmäiset lentokokeet | d |
| 8 | Lentovakauden tutkiminen | d; säätöarvojen muuttaminen on koulun oma tehtävä, ei valmistajan ohjeesta |
| 9 | FPV-lentämisen perusteet | d |
| 10 | Tarkkuuslentokoe | d |
| 11 | Data-analyysi Pythonilla | a (millä tahansa koneella, jossa on Python) |
| 12 | Säätötekniikka ja kokeiden vertailu | d, jos lennetään |
| 13 | Projektin suunnittelu | a |
| 14–15 | Projektin rakentaminen ja testaus | d, jos lennetään |
| 16 | Drone Challenge ja esittely | d |

Projektit: tarkkuuslaskeutuminen d, FPV-esterata d, oma ohjainohjelma a, lentovakaus d, 3D-osa a, videoanalyysi a,
konenäkömerkki c (kamera Raspberry Pihin), lentoaika d. Merkintää b ei tarvittu: mikään tehtävä ei vaadi ohjainta,
jota kalustossa ei ole. Käsiohjattu (Manual) lentotila vaatisi eri ohjaimen, eikä sitä käytetä.

## Tarkistetut tiedot (luettu 12.11.2026)

### Air:bit 2

Lähteet: valmistajan dokumenttisivu (makekit.no/en/docs/airbit-docs), rakennus- ja ohjelmointiohje *Airbit 2 –
Building and coding ENG* (65 s., 1/2023), vianetsintäsivu, tuotesivu ja avoin lähdekoodi (github.com/gomakekit/Airbit_V2).

- Itse koottava nelikopteri: vanerirunko, neljä harjallista (coreless) tasavirtamoottoria, 65 mm:n potkurit
  (4 + 4 varalla), ohjainkortti, jossa on laturi. Akku 1 kenno, 3,7 V, 800 mAh. Lataus ohjainkortin micro-USB:stä,
  noin tunti, ei valvomatta.
- Kaksi micro:bitiä (myydään erikseen); dronessa suositus V2. Ohjain on toinen micro:bit: kallistus = roll ja pitch,
  A ja B = kaasu, A+B = käynnistyslupa, ravistus = hätäpysäytys. Arvot P, A, R, T, Y radiolla, oletusryhmä 7.
- Valmistajan aika-arvio: kokoaminen 2–3 h, ohjaimen ohjelmointi 3–4 h.
- Käynnistys tasaisella alustalla, näytöllä G, M, C. Nousu noin 50–60 %:n kaasulla, leijunta 10–30 cm. Korkeus
  ohjataan käsin.
- Potkurit kiinnitetään vasta, kun moottorien käynnistys ja pysäytys on kokeiltu (ohjeen turvallisuussivu), vaikka
  ohjeen sivujärjestys on toinen.
- Vakautus lasketaan micro:bitissä, ja ohjelma on avointa MakeCode-koodia.

**Ei saa väittää:** GPS, korkeuden tai paikan pito, autonominen lento (valmistajalla "tulevia päivityksiä"), lohkot
"nouse" tai "laskeudu", puhelinsovellusohjaus V2:lla, Python-lento-ohjelma, dronen massa, lentoaika minuutteina,
potkurisuojat jokaisessa sarjassa, valmistajan ikäsuositus, säätöarvot nykyisen ohjelman ominaisuutena, PID-viritys
valmistajan opetustehtävänä.

### Kameradrone (DJI Neo 2)

Lähteet: käyttöohje v1.2 (12/2025), Motion Fly More Combon turvallisuusohje v1.2, RC Motion 3:n ja Goggles N3:n
käyttöohjeet, DJI:n tukiartikkeli SDK-yhteensopivuudesta.

- Luokka C0, suurin lentoonlähtömassa 160 g.
- Liikeohjaimella tilat Normal ja Sport. Sport-tilassa ja Easy ACRO -tempuissa esteiden väistö on pois. Manual-tila
  vaatii eri ohjaimen.
- Lukituspainike: 2 × = moottorit, pohjassa = nousu noin 1,2 m:iin, 1 × = jarrutus ja leijunta, pohjassa leijunnassa =
  laskeutuminen, 4 × = moottorien pysäytys ilmassa (drone putoaa).
- Lasit eivät täytä suoran näköyhteyden vaatimusta. Tauot, lopetus pahoinvoinnin tullessa, lasien puhdistus.
- Sisätilat: "ole erityisen varovainen"; ilman paikannusta ATTI-tila, drone ajautuu; ei väistä liikkuvia ihmisiä;
  valkoiset seinät, lasi, peilit ja toistuvat kuviot häiritsevät antureita.
- Valmistaja: tuotetta ei ole tarkoitettu lapsille (ei ikärajaa); käyttötarkoitus yksityinen käyttö.
- Ei SDK-tukea, ei reittipisteitä: dronea ei ohjelmoida.
- Lasit tallentavat näkymän omalle microSD-kortilleen (korttia ei ole pakkauksessa).

**Vain jälleenmyyjän tai hakutulosten varassa (ei materiaalissa):** massa 151 g, lentoaika noin 19 min, nopeudet,
49 Gt:n muisti, latausaika. **Ei löytynyt:** mitä arvoja lasien näyttö näyttää, lentolokien vienti taulukoksi.

### Säännöt

Lähteet: Traficomin Miehittämätön ilmailu -sivut (avoin kategoria, rekisteröityminen ja teoriakoe, missä ei saa
lennättää, yksityisyys ja tietosuoja, vakuutukset), EASAn Easy Access Rules for UAS (6/2026) ja FPV-FAQ, asetus
(EU) 2019/947. droneinfo.fi ohjautuu nykyään Traficomin sivuille.

- Kameradrone alle 250 g: operaattorin rekisteröityminen, tunnus droneen. Operaattori täysi-ikäinen tai
  organisaatio. Kauko-ohjaajan ikäraja Suomessa 12 v.
- C0: ei koulutusvaatimusta, käyttöohje luettava, A1/A3-koe suositeltava.
- Enintään 120 m, suora näköyhteys, ei ihmisjoukkojen päällä.
- FPV: tähystäjä lentäjän vieressä, paljain silmin; lentäjä vastaa lennosta.
- Sisälento ei kuulu EU:n droneasetuksen soveltamisalaan, kun drone ei voi päästä ulos (EASA GM1 Article 1).
- Rakennussarjasta koottu drone ei ole "yksityisesti rakennettu": Air:bit 2:n luokka tai lelustatus on selvitettävä
  ennen ulkolentoa. Siksi sitä lennätetään vain sisällä.
- Vakuutus: pakollinen yli 20 kg:n droneille, kevyemmille suositeltava.

**Koulun tarkistettava itse:** operaattorirekisteröinti ja tunnukset; vastuuvakuutuksen kattavuus; tilan käyttö
(rehtori, kiinteistö); ilmatilavyöhykkeet koulun osoitteessa lentopäivänä; kuvaamisen luvat (koulu on
rekisterinpitäjä); akkujen lataus- ja säilytyspaikka; Tukesin litiumakkuohje (sivua ei saatu avattua, joten sitä ei
ole siteerattu); Traficomin ilmatilasovelluksen osoite.

## Avoinna opettajalle

- Videoiden käsittely omilla koneilla: tunnin ohje sallii vain videot, joissa ei näy ihmisiä, ja ne poistetaan työn jälkeen. Tarkista, että tämä sopii koulun kuvaamisohjeeseen.
- Laajuus 2 op ja opintojakson hyväksyminen.
- Tunnin 8 säätökoe: mitä arvoja saa muuttaa ja kuinka paljon. Opettajan kokeiltava ensin itse.
- Turvallisuusaiheet ovat tilassa "valmisteilla", kunnes koulun vastuuhenkilöt hyväksyvät ne.
- Aloitusohjelma `airbit-ohjain.ts` on testaamaton luonnos (ei laitetta käytössä kirjoitettaessa).
- Ohjeiden käännökset englanniksi ja selkosuomeksi.
- Oppituntien omat kuvitukset: nyt yksi kuva kokonaisuutta kohti.
