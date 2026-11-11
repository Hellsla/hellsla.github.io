# Kuvituksen auditointi: yhteenveto

Tila 2026-11-11: **kaikki piirretyt opetuskuvat arvioitu** (1150 kuvaa). Tämä on arvio ja ehdotus; yhtään kuvaa,
`figures.py`-tiedostoa tai yhteistä työkalua ei ole muutettu. Jokaisen kuvan kohdalla opettajan päätös on ODOTTAA.

## Mistä mikäkin löytyy

- Arviointiluettelot: [FY1](FY1.md), [FY2](FY2.md), [FY3](FY3.md), [FY4](FY4.md), [FY5](FY5.md), [FY6](FY6.md),
  [FY7](FY7.md), [FY8](FY8.md), [FY9](FY9.md), [FY10](FY10.md), [FY14](FY14.md), [TVT-ohjeet](TVT.md),
  [Ahjo](AHJO.md). Lukumäärät: [COUNTS.md](COUNTS.md).
- Kuvakatalogi: `catalog/<KURSSI>.html`. Avaa tiedosto selaimessa repositorion paikallisesta kopiosta (se lukee
  tyylit ja KaTeXin hakemistosta `site/`). Painikkeet: kaikki, uudelleen piirrettävät ja korvattavat ensin, vain
  muutosehdotukset, puhelinleveys 360 px.
- Tärkeimmät ehdotukset: [PRIORITY.md](PRIORITY.md).
- Päätökset: kirjoita kuvan tunniste ja päätös, tai täytä rivin viimeinen sarake tiedostossa `data/<KURSSI>.tsv`.
  `python docs/illustration-audit/build.py` tuottaa luettelot ja katalogit uudelleen.

## Laajuus ja rajaukset

- FY1–FY8: 896 kuvaa kuvaluettelosta (`docs/figures/catalog.json`), mukana 23 käsin tekstiin upotettua kuvaa.
- FY9 (55), FY10 eli kokeelliset tutkimukset (105), FY14 (70), TVT-ohjeet (10) ja Ahjo-sivut (14): kuvat on luettu
  suoraan kunkin sivun `figures.py`-tiedostosta, koska ne eivät ole kuvaluettelossa.
- Ei mukana: valokuvat (147), logot ja kuvakkeet, simulaatiot, sivuston ulkopuoliset vanhat irtosivut sekä
  käsitekorttien ainoa kuva `kortit/kuvat/fy4-kalteva-taso.svg` (arvioitu erikseen: piirrä uudelleen, malliksi
  `fy4-16/esimerkki`).
- Kuvat on katsottu renderöityinä noin 500 px:n levyisinä sivuston tyyleillä ja KaTeX-merkinnöillä, epäilyttävät
  suurempina. Erillistä 360 px:n tarkistusta ei ole tehty kuva kuvalta: katalogin puhelinleveys-painike on sitä varten.
  Merkinnän "lukukelvoton puhelimella" olen antanut vain, kun teksti oli vaikea lukea jo 500 px:n leveydellä.
- Pisteet ovat yhden arvioijan arvio. Fysiikan 5 tarkoittaa, etten löytänyt virhettä; suuntaherkät kuvat (voimat
  magneettikentässä, induktio, kenttäviivat, kytkennät) ja mittakaavassa olevat kuvat tarkistin laskemalla, ja se on
  mainittu rivillä.

## Tulos

Pidä 940, kevyt korjaus 203, piirrä uudelleen 5, korvaa uudella 2, fysiikan virhe 0.

Fysiikan virheitä ei löytynyt. Kaksi kuvaa on merkitty fysiikasta arvosanalla 4: `fy5-6/cannon` (liian nopean
kappaleen rata piirretty ympyränä) ja `fy10-induktio/flux` (kenttäviivat ilman suuntaa ja napoja).

## Havainto ohjeista

`scripts/figstyle.py` ja kahdeksan FY1:n `figures.py`-tiedostoa viittaavat tiedostoon `docs/illustration-style.md`,
jota ei ole repositoriossa. Talotyyli on nyt kirjattu vain `figstyle.py`:n alkukommenttiin ja NOTES.md:n lukuun 3.

## Vahvuudet

1. Kuva kantaa fysiikan, ei vain kuvita sitä: `fy1-3/hero`, `fy3-1/scene`, `fy4-2/strobe`, `fy4-10/tarra`,
   `fy5-10/birth`, `fy8-4/buildup`, `fy8-9/ydin`.
2. Tilannekuva ja siitä erotettu voimakuvio rinnakkain läpi FY4:n ja FY5:n (`fy4-11/jarrutus`, `fy5-4/kaarre`).
3. Laitteet piirretään laitteina: `fy1-6/light-gates`, `fy6-2/multimeter`, `fy6-15/pistorasia`, FY10:n koeasetelmat.
4. Saman asian eri esitykset kohdakkain samalla akselilla: `fy6-5/potential-graph`, `fy7-7/phi-e`, `fy8-2/spectra`,
   `fy10-hissi/malli`.
5. Kuvat sanovat itse, ovatko ne mittakaavassa, ja väri ei kanna tietoa yksin.

## Yleisimmät ongelmat

1. **Akselin nimi leikkautuu kuva-alan yläreunaan** 26 kuvaajassa (FY10:n mallikuvaajat, vastausvaihtoehdot,
   `fy6-12`). Yhteinen syy piirtokoodissa: yksi korjaus korjaa kaikki.
2. **Aurinko sädekehällä** 24 kuvassa, vaikka talotyylissä se on kiekko hohteella.
3. **Sama asia piirretään eri tavalla eri luvuissa.** Energiavirtakaaviot viidellä tavalla (`fy2-2`, `fy2-4`,
   `fy2-7`, `fy3-15`, `fy6-9`, `fy9-energia`), voimanuolen väri FY3:ssa kolmella, ilmanvastus kahdella (`fy4-3` ja
   `fy4-14`), kasvihuoneilmiö kolmella (`fy2-8`, `fy3-12`, `fy8-2`), pinch-kuva kahdella (FY14), hissin matkustaja
   kolmella.
4. **Tekstit törmäävät**: merkintä toisen merkinnän, viivan tai reunan päällä noin 45 kuvassa.
5. **Yksiköt ja suureet pieninä pystymurtoina** akseleilla ja selitteissä (`fy5-4/kuvaaja`, `fy5-sovella/fy5-s2-graph`,
   `fy8-7/rate-graph`, `fy9-moderni/puolitus`), kun leipätekstissä ne ovat rivillä.
6. **Soveltavien tehtävien ja kokeiden kuvaajat** FY1–FY5:ssä eri piirrostavalla kuin lukujen kuvaajat.
7. **Tikku-ukot ja pallopäähahmot** muutamassa kuvassa (`fy4-sovella/fy4-s1-fbd`, `fy5-koe/fy5-k2-board`,
   `fy5-14/doppler`, `fy7-11/observer`), kun sarjan muut ihmiset ovat piirrettyjä hahmoja.

## Kurssien väliset erot

Tasaisimmat: FY7, FY8, FY6 ja FY5 (muutosehdotuksia 10–11 %). Epätasaisin: FY3 (37 %): voimanuolen väri vaihtelee,
lukujen 13–16 kuvat on upotettu käsin talotyylin ulkopuolelle ja avauskuvissa on sarjan harvimmat sommittelut. FY2:n
osuus (43 %) on suurempi, mutta kurssi on pieni ja korjaukset ovat kevyitä. FY10:n 23 korjauksesta 15 on sama
akselin nimen leikkautuminen.

## Viisi periaatetta jatkoon

1. Yksi esitystapa per asia koko sarjassa: päätä malli (energiavirta `fy2-4/lamp`, voimakuvio `fy4-16/esimerkki`,
   kasvihuoneilmiö `fy8-2/greenhouse`, Aurinko kiekkona) ja käytä sitä kaikkialla.
2. Voima on aina punainen ja alkaa kappaleesta, energian ja lämmön virta oranssi, nopeus sininen. Päätä erikseen,
   piirretäänkö työntävä voima kärki pinnassa.
3. Jokainen merkintä saa oman tilansa kuva-alan sisällä, ja yksikkö on samassa muodossa kuin leipätekstissä.
4. Toistuva kohde (ihminen, hissi, Maa, magneetti, lämpömittari) piirretään yhdellä yhteisellä piirrolla.
5. Kaikki kuvat `figures.py`:n kautta talotyylillä, myös tutkimusvaiheen ja kokeiden kuvaajat.

## Opettajan ryhmäpäätökset (2026-11-11)

Hyväksytty korjattaviksi: A akselin nimi leikkautuu yläreunaan, B Aurinko sädekehällä, C energiavirtakaaviot mallin
`fy2-4/lamp` mukaan (`fy2-2/sailyminen`, `fy2-7/sankey`, `fy3-15/~lesson-2`, `fy6-9/energia`, `fy9-energia/ketju`),
D kokeiden ja soveltavien tehtävien kuvaajat lukujen piirrostapaan, E vanha paksu viivatyyli talotyyliin,
F yksiköt pystymurroista rivimuotoon. Ryhmä on merkitty kunkin kuvan päätössarakkeeseen. Toteutus tehdään vasta, kun
kaikki päätökset on annettu.
